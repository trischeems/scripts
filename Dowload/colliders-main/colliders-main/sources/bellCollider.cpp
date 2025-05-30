#include <set>
#include <map>

#include <maya/MGlobal.h>
#include <maya/MPlug.h>
#include <maya/MPlugArray.h>
#include <maya/MIntArray.h>
#include <maya/MFloatPointArray.h>
#include <maya/MFloatVectorArray.h>
#include <maya/MFnDependencyNode.h>

#include <maya/MTransformationMatrix.h>
#include <maya/MQuaternion.h>
#include <maya/MEulerRotation.h>

#include <maya/MFnMesh.h>
#include <maya/MFnMeshData.h>
#include <maya/MMeshIntersector.h>
#include <maya/MFnNurbsCurve.h>
#include <maya/MFnNurbsCurveData.h>

#include <maya/MArrayDataBuilder.h>
#include <maya/MArrayDataHandle.h>

#include <maya/MFnTypedAttribute.h>
#include <maya/MFnNumericAttribute.h>
#include <maya/MFnMatrixAttribute.h>
#include <maya/MFnEnumAttribute.h>

#include <tbb/parallel_for.h>

#include "bellCollider.h"
#include "utils.hpp"

#define RAD2DEG 57.2958
#define DEG2RAD 0.0174532862

using namespace std;

MTypeId BellCollider::typeId(1274434);

MObject BellCollider::attr_bellMatrix;
MObject BellCollider::attr_ringMatrix;
MObject BellCollider::attr_bellSubdivision;
MObject BellCollider::attr_ringSubdivision;
MObject BellCollider::attr_bellBottomRadius;
MObject BellCollider::attr_falloff;
MObject BellCollider::attr_collision;
MObject BellCollider::attr_positionCount;
MObject BellCollider::attr_drawColor;
MObject BellCollider::attr_drawOpacity;
MObject BellCollider::attr_outputPositions;
MObject BellCollider::attr_outputRotations;
MObject BellCollider::attr_outputCurve;
MObject BellCollider::attr_outputBellMesh;

MString BellCollider::drawDbClassification = "drawdb/geometry/bellCollider";
MString BellCollider::drawRegistrantId = "collidersPlugin";

MObject makeBellMesh(const MMatrix& matrix, unsigned int axis, unsigned int numSides, double height = 1, double bottomRadius = 1, double topRadius = 1)
{
    const int numVertices = numSides * 2 + 1;
    const int numPolygons = numSides * 2;

    MPointArray vertexArray;
    MIntArray polygonCounts, polygonConnects;

    vertexArray.append(MPoint(0, 0, 0) * matrix);

    // bottom
    for (int i = 0; i < numSides; i++)
    {
        const double rad = (double)i / numSides * 2 * M_PI;
        const double x = bottomRadius * cos(rad);
        const double z = bottomRadius * sin(rad);
        
        MPoint p;
        switch (axis)
        {
        case 0: p = MPoint(0, x, z); break;
        case 1: p = MPoint(x, 0, z); break;
        case 2: p = MPoint(x, z, 0); break;
        }

        vertexArray.append(p * matrix);

        polygonCounts.append(3);
        polygonConnects.append(0);
        polygonConnects.append(i + 1); // i=0 is center
        polygonConnects.append(i == numSides - 1 ? 1 : i + 2);
    }

    // top
    for (int i = 0; i < numSides; i++)
    {
        const double rad = (double)i / numSides * 2 * M_PI;
        const double x = topRadius * cos(rad);
        const double z = topRadius * sin(rad);

        MPoint p;
        switch (axis)
        {
        case 0: p = MPoint(height, x, z); break;
        case 1: p = MPoint(x, height, z); break;
        case 2: p = MPoint(x, z, height); break;
        }
        vertexArray.append(p * matrix);

        polygonCounts.append(4);
        polygonConnects.append(i + 1); // i=0 is center
        polygonConnects.append(numSides + i + 1);
        polygonConnects.append(i == numSides - 1 ? numSides + 1 : numSides + i + 2);
        polygonConnects.append(i == numSides - 1 ? 1 : i + 2);
    }

    MFnMeshData meshData;
    MObject meshObject = meshData.create();

    MFnMesh meshFn;
    meshFn.create(numVertices, numPolygons, vertexArray, polygonCounts, polygonConnects, meshObject);
    /*
    // UV
    MIntArray uvCounts;
    MIntArray uvIds;

    MFloatArray uArray;
    MFloatArray vArray;

    for (int i = 0; i < numSides; i++)
        uvCounts.append(0);

    const double width = 1.0 / numSides;
    for (int i = 0; i < numSides; i++)
    {
        uArray.append(i * width);
        vArray.append(0);
        uArray.append(i * width);
        vArray.append(1);

        uvCounts.append(4);
        const int idx = i * 2;
        uvIds.append(idx);
        uvIds.append(idx + 1);
        uvIds.append(idx + 3);
        uvIds.append(idx + 2);
    }

    uArray.append(1);
    vArray.append(0);
    uArray.append(1);
    vArray.append(1);

    meshFn.setUVs(uArray, vArray);
    meshFn.assignUVs(uvCounts, uvIds);
    */
    return meshObject;
}

MQuaternion mat2quat(const MMatrix& mat)
{
    float tr, s;
    float q[4];
    int i, j, k;
    MQuaternion quat;

    int nxt[3] = { 1, 2, 0 };
    tr = mat[0][0] + mat[1][1] + mat[2][2];

    // check the diagonal
    if (tr > 0.0)
    {
        s = sqrt(tr + float(1.0));
        quat.w = s / float(2.0);
        s = float(0.5) / s;

        quat.x = (mat[1][2] - mat[2][1]) * s;
        quat.y = (mat[2][0] - mat[0][2]) * s;
        quat.z = (mat[0][1] - mat[1][0]) * s;
    }
    else
    {
        // diagonal is negative
        i = 0;
        if (mat[1][1] > mat[0][0])
            i = 1;
        if (mat[2][2] > mat[i][i])
            i = 2;

        j = nxt[i];
        k = nxt[j];
        s = sqrt((mat[i][i] - (mat[j][j] + mat[k][k])) + float(1.0));

        q[i] = s * float(0.5);
        if (s != float(0.0))
            s = float(0.5) / s;

        q[3] = (mat[j][k] - mat[k][j]) * s;
        q[j] = (mat[i][j] + mat[j][i]) * s;
        q[k] = (mat[i][k] + mat[k][i]) * s;

        quat.x = q[0];
        quat.y = q[1];
        quat.z = q[2];
        quat.w = q[3];
    }

    return quat;
}

MObject makeBellCurve(const MPointArray &points, int bellSubdivision, bool use_bottom=false)
{
    const int START = use_bottom ? 1 : bellSubdivision + 1;
    const int END = use_bottom ? bellSubdivision : points.length();

    MPointArray cvs;
    MDoubleArray knots;
    for (int i = START; i < END; i++)
    {
        knots.append(cvs.length());
        cvs.append(points[i]);
    }

    knots.append(knots[knots.length() - 1] + 1);
    cvs.append(cvs[0]);

    MFnNurbsCurveData curveDataFn;
    MObject curveData = curveDataFn.create();

    MFnNurbsCurve curveFn;
    curveFn.create(cvs, knots, 1, MFnNurbsCurve::kPeriodic, false, false, curveData);
    return curveData;
}

MStatus BellCollider::compute(const MPlug &plug, MDataBlock &dataBlock)
{
    if (plug != attr_outputPositions && plug != attr_outputRotations && plug != attr_outputCurve && plug != attr_outputBellMesh)
        return MS::kFailure;

    const MMatrix bellMatrix = dataBlock.inputValue(attr_bellMatrix).asMatrix();
    const MMatrix bellMatrixInverse = bellMatrix.inverse();

    auto ringMatrixHandle = dataBlock.inputArrayValue(attr_ringMatrix);

    if (ringMatrixHandle.elementCount() == 0)
        return MS::kFailure;

    const int bellSubdivision = dataBlock.inputValue(attr_bellSubdivision).asInt();
    const int ringSubdivision = dataBlock.inputValue(attr_ringSubdivision).asInt();

    const float bellBottomRadius = dataBlock.inputValue(attr_bellBottomRadius).asFloat();
    const float falloff = dataBlock.inputValue(attr_falloff).asFloat();
    const float collision = dataBlock.inputValue(attr_collision).asFloat();
    const int positionCount = dataBlock.inputValue(attr_positionCount).asInt();

    auto outputPositionsHandle = dataBlock.outputArrayValue(attr_outputPositions);
    auto outputRotationsHandle = dataBlock.outputArrayValue(attr_outputRotations);

    const MVector color = dataBlock.inputValue(attr_drawColor).asVector();
    const float drawOpacity = dataBlock.inputValue(attr_drawOpacity).asFloat();

    const MPoint bell_translate = taxis(bellMatrix);
    const MVector bellAxis = maxis(bellMatrix, 1); // Y axis
    const MVector bellNormal = bellAxis.normal();
    const Plane bellPlane(bell_translate, bellNormal);

    drawData.color = MColor(color.x, color.y, color.z, drawOpacity);
    drawData.bellCenter = bell_translate;
    drawData.collisionPointBellList.clear();
    drawData.collisionPointRingList.clear();
    drawData.ringDirectionList.clear();
    drawData.ringPositionList.clear();
    drawData.ringMeshList.clear();

    MObject bellMesh = makeBellMesh(bellMatrix, 1, bellSubdivision, 1, bellBottomRadius, 1);
    MFnMesh bellMeshFn(bellMesh);

    MPointArray baseBellPoints;
    bellMeshFn.getPoints(baseBellPoints);

    vector<MPointArray> bellPointsList; // bell points per ring
    vector<MObject> ringMeshList;

    for (int i = 0; i < ringMatrixHandle.elementCount(); i++)
    {
        ringMatrixHandle.jumpToElement(i);

        const MMatrix ringMatrix = ringMatrixHandle.inputValue().asMatrix();
        const MMatrix ringMatrixInverse = ringMatrix.inverse();

        const MVector ringDirection = maxis(ringMatrix, 1); // Y axis

        const MPoint ring_translate = taxis(ringMatrix);
        const MVector ringNormal = ringDirection.normal();
        const Plane ringPlane(ring_translate, ringNormal);

        const MPoint ring_translate_proj = bellPlane.projectPoint(taxis(ringMatrix));
        const MVector ringDirection_proj = bellPlane.projectVector(ringDirection);

        drawData.ringDirectionList.push_back(ringDirection_proj);
        drawData.ringPositionList.push_back(taxis(ringMatrix));

        MPointArray bellPoints = baseBellPoints;

        if (ringDirection_proj.length() > 1e-3)
        {
            const MPointArray hitPoints = findSphereLineIntersection(ring_translate_proj * bellMatrixInverse, ringDirection_proj * bellMatrixInverse, MPoint(0,0,0), 1.001);

            MPoint collisionPointBell, collisionPointRing;
            if (hitPoints.length() > 0)
            {
                collisionPointBell = hitPoints[0] * bellMatrix + bellAxis;

                const double linePointCoeff = ringNormal * bellNormal > 0 ? 1 : -1;

                const MVector ring_proj = ringPlane.projectVector(ringDirection_proj * linePointCoeff);
                const double delta = ring_proj.length() / (ring_proj * ringMatrixInverse).length();
                const MVector ring_proj_scaled = ring_proj.normal() * delta; // scale vector
                const MPoint linePoint = ring_translate + ring_proj_scaled;

                const MPointArray sphereLinePoints = findSphereLineIntersection(linePoint, ringDirection, ring_translate, (collisionPointBell - ring_translate).length());

                for (int k = 0; k < sphereLinePoints.length(); k++)
                {
                    if ((sphereLinePoints[k] - ring_translate) * ringDirection > 0)
                        collisionPointRing = sphereLinePoints[k];
                }

                drawData.collisionPointRingList.push_back(linePoint);
                drawData.collisionPointRingList.push_back(collisionPointRing);
            }
            else
                MGlobal::displayError(MFnDependencyNode(thisMObject()).name() + ": no hits with ringMatrix[" + MSTR(i) + "]");            

            const double collisionDelta = (bellPlane.distance(collisionPointRing) - bellPlane.distance(collisionPointBell)) / bellAxis.length();
            if (collisionDelta < 0)
            {
                MTransformationMatrix rotationMatrixFn;
                rotationMatrixFn.setTranslation(ring_translate, MSpace::kWorld);
                const MMatrix rotateMatrixInverse = rotationMatrixFn.asMatrixInverse();

                const MQuaternion quat(collisionPointBell - ring_translate, collisionPointRing - ring_translate); // rotate X to final point
                rotationMatrixFn.rotateBy(quat, MSpace::kTransform);
                const MMatrix rotateMatrix = rotationMatrixFn.asMatrix();

                const Plane upperBellPlane(bell_translate + bellAxis, bellNormal);

                // bell top deformation
                tbb::parallel_for(tbb::blocked_range<int>(bellSubdivision + 1, bellPoints.length()), [&](tbb::blocked_range<int>& r)
                    {
                        for (auto i = r.begin(); i != r.end(); i++)
                        {
                            const MPoint bellPoint_proj = bellPlane.projectPoint(bellPoints[i]);
                            const MVector offset_proj = bellPoint_proj * bellMatrixInverse - ring_translate_proj * bellMatrixInverse;

                            double weight = offset_proj.normal() * (ringDirection_proj * bellMatrixInverse).normal(); // -1..1

                            if (weight > falloff)
                            {
                                weight = (weight - falloff) / (1.0 - falloff);

                                const MPoint rp = bellPoints[i] * rotateMatrixInverse * rotateMatrix;

                                // constrain by upper plane
                                MPoint p = rp;
                                if (upperBellPlane.distance(rp) > 0)
                                    p = upperBellPlane.projectPoint(rp);

                                bellPoints[i] = p * weight + bellPoints[i] * (1.0 - weight);                               
                            }
                        }
                    });
            }

            drawData.collisionPointBellList.push_back(collisionPointBell);
        }

        // ring collision
        if (collision > 1e-5)
            tbb::parallel_for(tbb::blocked_range<int>(bellSubdivision + 1, bellPoints.length()), [&](tbb::blocked_range<int>& r)
                {
                    for (auto i = r.begin(); i != r.end(); i++)
                    {                    
                        const MVector vec = ringPlane.projectPoint(bellPoints[i]) - ring_translate;

                        const double delta = vec.length() / (vec * ringMatrixInverse).length();
                        const MVector vec_proj_scaled = vec.normal() * delta; // scale vector

                        if (vec_proj_scaled.length() > vec.length())
                            bellPoints[i] += vec.normal() * (vec_proj_scaled.length() - vec.length()) * collision;
                     }
                });

        ringMeshList.push_back(makeBellMesh(ringMatrix, 1, ringSubdivision, 1)); // Y axis
        bellPointsList.push_back(bellPoints);
    }

    // Average top points
    MPointArray outBellPoints = baseBellPoints;

    tbb::parallel_for(tbb::blocked_range<size_t>(bellSubdivision+1, baseBellPoints.length()), [&](tbb::blocked_range<size_t>& r) {
        for (auto i = r.begin(); i != r.end(); i++)
        {
            double sum = 0;
            double maxDist = 0;
            for (const auto& bellPoints : bellPointsList)
            {
                const MVector vec = bellPoints[i] - baseBellPoints[i];
                const double d = vec.length();
                sum += pow(d, 2);

                if (d > maxDist)
                    maxDist = d;
            }

            if (sum > 0)
            {
                MVector wp;
                for (const auto& bellPoints : bellPointsList)
                {
                    const MVector vec = bellPoints[i] - baseBellPoints[i];
                    const double d = pow(vec.length(), 2);
                    const double w = d / sum;

                    wp += vec * w;
                }

                outBellPoints[i] += wp.normal()* maxDist;
            }
        }
    });

    bellMeshFn.setPoints(outBellPoints);    

    drawData.bellMesh = bellMesh;
    drawData.ringMeshList = ringMeshList;

    MObject bottomBellCurve = makeBellCurve(outBellPoints, bellSubdivision, true);
    MFnNurbsCurve bottomBellCurveFn(bottomBellCurve);

    MObject outCurve = makeBellCurve(outBellPoints, bellSubdivision);
    MFnNurbsCurve outCurveFn(outCurve);

    double minParam, maxParam;
    outCurveFn.getKnotDomain(minParam, maxParam);

    auto positionsBuilder = outputPositionsHandle.builder();
    auto rotationsBuilder = outputRotationsHandle.builder();

    for (int i = 0; i < positionCount; i++)
    {
        const double param = (double)i / positionCount * (maxParam - minParam) + minParam; // 0..bellSubdivision

        MPoint position, bottomPosition;
        outCurveFn.getPointAtParam(param, position);
        bottomBellCurveFn.getPointAtParam(param, bottomPosition);

        auto h = positionsBuilder.addElement(i);
        h.setMVector(position);
        
        // get rotation
        const double ROUGH = 1.0;
        MPoint p1, p2;        
        outCurveFn.getPointAtParam(param+ROUGH < maxParam ? param+ROUGH : ROUGH, p1);
        outCurveFn.getPointAtParam(param-ROUGH > minParam ? param-ROUGH : maxParam-ROUGH, p2);
        MVector tg = (p2-p1).normal();

        const MVector xAxis = (bottomPosition - position).normal();
        MVector yAxis = xAxis ^ tg;
        MVector zAxis = xAxis ^ yAxis;

        MMatrix mat;
        mat[0][0] = xAxis.x;
        mat[0][1] = xAxis.y;
        mat[0][2] = xAxis.z;

        mat[1][0] = yAxis.x;
        mat[1][1] = yAxis.y;
        mat[1][2] = yAxis.z;

        mat[2][0] = zAxis.x;
        mat[2][1] = zAxis.y;
        mat[2][2] = zAxis.z;

        auto euler = mat2quat(mat).asEulerRotation();
        h = rotationsBuilder.addElement(i);
        h.setMVector(euler.asVector()* RAD2DEG);
    }                                                                                    
    outputPositionsHandle.set(positionsBuilder);
    outputPositionsHandle.setClean();
    outputPositionsHandle.setAllClean();

    outputRotationsHandle.set(rotationsBuilder);
    outputRotationsHandle.setClean();
    outputRotationsHandle.setAllClean();

    dataBlock.outputValue(attr_outputCurve).setMObject(outCurve);
    dataBlock.outputValue(attr_outputBellMesh).setMObject(bellMesh);

    dataBlock.setClean(attr_outputCurve);
    dataBlock.setClean(attr_outputBellMesh);
    dataBlock.setClean(attr_outputPositions);    

	return MS::kSuccess;
}

MStatus BellCollider::initialize()
{
    MFnNumericAttribute nAttr;
    MFnMatrixAttribute mAttr;
    MFnEnumAttribute eAttr;
    MFnTypedAttribute tAttr;
    
    attr_bellMatrix = mAttr.create("bellMatrix", "bellMatrix");
    mAttr.setHidden(true);
    addAttribute(attr_bellMatrix);

    attr_ringMatrix = mAttr.create("ringMatrix", "ringMatrix");
    mAttr.setArray(true);
    mAttr.setHidden(true);
    addAttribute(attr_ringMatrix);

    attr_bellSubdivision = nAttr.create("bellSubdivision", "bellSubdivision", MFnNumericData::kInt, 16);
    nAttr.setMin(3);
    nAttr.setKeyable(true);
    addAttribute(attr_bellSubdivision);

    attr_ringSubdivision = nAttr.create("ringSubdivision", "ringSubdivision", MFnNumericData::kInt, 16);
    nAttr.setMin(3);
    nAttr.setKeyable(true);
    addAttribute(attr_ringSubdivision);

    attr_bellBottomRadius = nAttr.create("bellBottomRadius", "bellBottomRadius", MFnNumericData::kFloat, 0.8);
    nAttr.setMin(0);
    nAttr.setKeyable(true);
    addAttribute(attr_bellBottomRadius);

    attr_falloff = nAttr.create("falloff", "falloff", MFnNumericData::kFloat, 0);
    nAttr.setMin(-1);
    nAttr.setMax(1);
    nAttr.setKeyable(true);
    addAttribute(attr_falloff);

    attr_collision = nAttr.create("collision", "collision", MFnNumericData::kFloat, 0);
    nAttr.setMin(0);
    nAttr.setMax(1);
    nAttr.setKeyable(true);
    addAttribute(attr_collision);

    attr_drawColor = nAttr.create("drawColor", "drawColor", MFnNumericData::k3Double);
    nAttr.setDefault(0.0, 0.01, 0.11);
    nAttr.setMin(0, 0, 0);
    nAttr.setMax(1, 1, 1);
    nAttr.setKeyable(true);
    addAttribute(attr_drawColor);

    attr_drawOpacity = nAttr.create("drawOpacity", "drawOpacity", MFnNumericData::kFloat, 0.3);
    nAttr.setMin(0);
    nAttr.setMax(1);
    nAttr.setKeyable(true);
    addAttribute(attr_drawOpacity);

    attr_positionCount = nAttr.create("positionCount", "positionCount", MFnNumericData::kInt, 6);
    nAttr.setMin(0);
    nAttr.setChannelBox(true);
    addAttribute(attr_positionCount);

    attr_outputPositions = nAttr.create("outputPositions", "outputPositions", MFnNumericData::k3Double);
    nAttr.setArray(true);
    nAttr.setUsesArrayDataBuilder(true);
    addAttribute(attr_outputPositions);

    attr_outputRotations = nAttr.create("outputRotations", "outputRotations", MFnNumericData::k3Double);
    nAttr.setArray(true);
    nAttr.setUsesArrayDataBuilder(true);
    addAttribute(attr_outputRotations);

    attr_outputCurve = tAttr.create("outputCurve", "outputCurve", MFnData::kNurbsCurve);
    tAttr.setHidden(true);
    addAttribute(attr_outputCurve);

    attr_outputBellMesh = tAttr.create("outputBellMesh", "outputBellMesh", MFnData::kMesh);
    tAttr.setHidden(true);
    addAttribute(attr_outputBellMesh);

    attributeAffects(attr_bellMatrix, attr_outputPositions);
    attributeAffects(attr_ringMatrix, attr_outputPositions);
    attributeAffects(attr_bellSubdivision, attr_outputPositions);
    attributeAffects(attr_ringSubdivision, attr_outputPositions);
    attributeAffects(attr_bellBottomRadius, attr_outputPositions);
    attributeAffects(attr_falloff, attr_outputPositions);
    attributeAffects(attr_collision, attr_outputPositions);
    attributeAffects(attr_positionCount, attr_outputPositions);
    attributeAffects(attr_drawColor, attr_outputPositions);
    attributeAffects(attr_drawOpacity, attr_outputPositions);

    attributeAffects(attr_bellMatrix, attr_outputRotations);
    attributeAffects(attr_ringMatrix, attr_outputRotations);
    attributeAffects(attr_bellSubdivision, attr_outputRotations);
    attributeAffects(attr_ringSubdivision, attr_outputRotations);
    attributeAffects(attr_bellBottomRadius, attr_outputRotations);
    attributeAffects(attr_falloff, attr_outputRotations);
    attributeAffects(attr_collision, attr_outputRotations);
    attributeAffects(attr_positionCount, attr_outputRotations);
    attributeAffects(attr_drawColor, attr_outputRotations);
    attributeAffects(attr_drawOpacity, attr_outputRotations);

    attributeAffects(attr_bellMatrix, attr_outputCurve);
    attributeAffects(attr_ringMatrix, attr_outputCurve);
    attributeAffects(attr_bellSubdivision, attr_outputCurve);
    attributeAffects(attr_ringSubdivision, attr_outputCurve);
    attributeAffects(attr_bellBottomRadius, attr_outputCurve);
    attributeAffects(attr_falloff, attr_outputCurve);
    attributeAffects(attr_collision, attr_outputCurve);
    attributeAffects(attr_drawColor, attr_outputCurve);
    attributeAffects(attr_drawOpacity, attr_outputCurve);

    attributeAffects(attr_bellMatrix, attr_outputBellMesh);
    attributeAffects(attr_ringMatrix, attr_outputBellMesh);
    attributeAffects(attr_bellSubdivision, attr_outputBellMesh);
    attributeAffects(attr_ringSubdivision, attr_outputBellMesh);
    attributeAffects(attr_bellBottomRadius, attr_outputBellMesh);
    attributeAffects(attr_falloff, attr_outputBellMesh);
    attributeAffects(attr_collision, attr_outputBellMesh);
    attributeAffects(attr_drawColor, attr_outputBellMesh);
    attributeAffects(attr_drawOpacity, attr_outputBellMesh);

    return MS::kSuccess;
}

void drawCylinder(MHWRender::MUIDrawManager& drawManager, const MObject& mesh)
{
    if (mesh.isNull())
        return;

    const MFnMesh meshFn(mesh);
    const int numSides = (meshFn.numVertices() - 1) / 2;

    MPointArray points;
    meshFn.getPoints(points);

    for (int i = 0; i < numSides; i++)
    {
        drawManager.line(points[i + 1], i == numSides - 1 ? points[1] : points[i + 2]); // buttom
        drawManager.line(points[numSides + i + 1], i == numSides - 1 ? points[numSides + 1] : points[numSides + i + 2]); // top
        drawManager.line(points[i + 1], points[numSides + i + 1]); // edge
    }
}

void drawMesh(MHWRender::MUIDrawManager& drawManager, const MObject& mesh, const MColor &color)
{
    MIntArray triangleCount, triangleIndices;
    MFnMesh meshFn(mesh);

    MPointArray points;
    meshFn.getTriangles(triangleCount, triangleIndices);
    meshFn.getPoints(points);

    //MFloatVectorArray meshNormals;
    //meshFn.getVertexNormals(true, meshNormals);

    MFloatPointArray positions(triangleIndices.length());
    MColorArray colors(triangleIndices.length(), color);
    //MFloatVectorArray normals;

    for (int i = 0; i < triangleIndices.length(); i++)
    {
        positions[i] = points[triangleIndices[i]];
        //normals.append(meshNormals[triangleIndices[i]]);
    }

    drawManager.mesh(MUIDrawManager::kTriangles, positions, NULL, &colors);
}

void BellCollider::drawUI(MHWRender::MUIDrawManager& drawManager)
{
    //drawManager.beginDrawInXray();

    if (drawData.bellMesh.isNull())
        return;

    drawMesh(drawManager, drawData.bellMesh, drawData.color);
    drawManager.setColor(MColor(0, 0, 0));
    drawCylinder(drawManager, drawData.bellMesh); // wireframe

    for (const auto& m : drawData.ringMeshList)
    {
        drawMesh(drawManager, m, drawData.color * 0.5);
        drawManager.setColor(MColor(0, 0, 0));
        drawCylinder(drawManager, m); // wireframe
    }

    drawManager.setColor(MColor(0,0,0));
    drawManager.setPointSize(5);

    for (const auto& p : drawData.collisionPointBellList)
        drawManager.point(p);

    for (const auto& p : drawData.collisionPointRingList)
        drawManager.point(p);

    for (int i = 0; i < drawData.ringDirectionList.size();i++)
        drawManager.line(drawData.ringPositionList[i], drawData.ringPositionList[i] + drawData.ringDirectionList[i]);

    //drawManager.endDrawInXray();
}

MUserData* BellColliderDrawOverride::prepareForDraw(
    const MDagPath& objPath, 
    const MDagPath& cameraPath, 
    const MHWRender::MFrameContext& frameContext, 
    MUserData* oldData)
{
    MStatus stat;

    MObject obj = objPath.node(&stat);
    if (stat != MS::kSuccess)
        return NULL;

    auto* data = dynamic_cast<BellColliderDrawData*>(oldData);

    if (!data)
        data = new BellColliderDrawData();

    MFnDependencyNode locatorFn(obj);
    data->bellCollider = dynamic_cast<BellCollider*>(locatorFn.userNode());

    return data;
}

void BellColliderDrawOverride::addUIDrawables(
    const MDagPath& objPath, 
    MHWRender::MUIDrawManager& drawManager, 
    const MHWRender::MFrameContext& frameContext, 
    const MUserData* data)
{
    auto* bellColliderData = dynamic_cast<const BellColliderDrawData*>(data);

    if (bellColliderData && bellColliderData->bellCollider)
    {
        drawManager.beginDrawable();
        bellColliderData->bellCollider->drawUI(drawManager);
        drawManager.endDrawable();
    }
}