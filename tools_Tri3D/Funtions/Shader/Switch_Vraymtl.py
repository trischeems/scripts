import maya.cmds as cmds
import maya.mel as mel





################### VRay Switch ##############################
def swShadermtl(*arg):

    blend_node = cmds.shadingNode('blendColors', asUtility=True)
    sw1_node = cmds.shadingNode('VRaySwitchMtl', asUtility=True)
    sw2_node = cmds.shadingNode('VRaySwitchMtl', asUtility=True)

    cmds.rename(blend_node, 'SwitchShader1')
    cmds.rename(sw1_node, 'Switchmt1')
    cmds.rename(sw2_node, 'Switchmt2')
    cmds.connectAttr('Switchmt1.outColor', 'SwitchShader1.color1', force=True)
    cmds.connectAttr('Switchmt2.outColor', 'SwitchShader1.color2', force=True)
    cmds.setAttr('SwitchShader1.blender', 1)
    mel.eval("""
    shadingNode -asShader VRayMtl;
    sets -renderable true -noSurfaceShader true -empty -name VRayMtl1SG;
    connectAttr -f VRayMtl1.outColor VRayMtl1SG.surfaceShader;
             """)
    mel.eval("""
    shadingNode -asTexture -isColorManaged file;
    shadingNode -asUtility place2dTexture;
    connectAttr -f place2dTexture1.coverage file1.coverage;
    connectAttr -f place2dTexture1.translateFrame file1.translateFrame;
    connectAttr -f place2dTexture1.rotateFrame file1.rotateFrame;
    connectAttr -f place2dTexture1.mirrorU file1.mirrorU;
    connectAttr -f place2dTexture1.mirrorV file1.mirrorV;
    connectAttr -f place2dTexture1.stagger file1.stagger;
    connectAttr -f place2dTexture1.wrapU file1.wrapU;
    connectAttr -f place2dTexture1.wrapV file1.wrapV;
    connectAttr -f place2dTexture1.repeatUV file1.repeatUV;
    connectAttr -f place2dTexture1.offset file1.offset;
    connectAttr -f place2dTexture1.rotateUV file1.rotateUV;
    connectAttr -f place2dTexture1.noiseUV file1.noiseUV;
    connectAttr -f place2dTexture1.vertexUvOne file1.vertexUvOne;
    connectAttr -f place2dTexture1.vertexUvTwo file1.vertexUvTwo;
    connectAttr -f place2dTexture1.vertexUvThree file1.vertexUvThree;
    connectAttr -f place2dTexture1.vertexCameraOne file1.vertexCameraOne;
    connectAttr place2dTexture1.outUV file1.uv;
    connectAttr place2dTexture1.outUvFilterSize file1.uvFilterSize;
    rename place2dTexture1 "place1" ;
    rename file1 "Text1" ;
             """)
    mel.eval("""
    shadingNode -asTexture -isColorManaged file;
    shadingNode -asUtility place2dTexture;
    connectAttr -f place2dTexture1.coverage file1.coverage;
    connectAttr -f place2dTexture1.translateFrame file1.translateFrame;
    connectAttr -f place2dTexture1.rotateFrame file1.rotateFrame;
    connectAttr -f place2dTexture1.mirrorU file1.mirrorU;
    connectAttr -f place2dTexture1.mirrorV file1.mirrorV;
    connectAttr -f place2dTexture1.stagger file1.stagger;
    connectAttr -f place2dTexture1.wrapU file1.wrapU;
    connectAttr -f place2dTexture1.wrapV file1.wrapV;
    connectAttr -f place2dTexture1.repeatUV file1.repeatUV;
    connectAttr -f place2dTexture1.offset file1.offset;
    connectAttr -f place2dTexture1.rotateUV file1.rotateUV;
    connectAttr -f place2dTexture1.noiseUV file1.noiseUV;
    connectAttr -f place2dTexture1.vertexUvOne file1.vertexUvOne;
    connectAttr -f place2dTexture1.vertexUvTwo file1.vertexUvTwo;
    connectAttr -f place2dTexture1.vertexUvThree file1.vertexUvThree;
    connectAttr -f place2dTexture1.vertexCameraOne file1.vertexCameraOne;
    connectAttr place2dTexture1.outUV file1.uv;
    connectAttr place2dTexture1.outUvFilterSize file1.uvFilterSize;
    rename place2dTexture1 "place1" ;
    rename file1 "Text1" ;
             """)
    mel.eval("""
    shadingNode -asTexture -isColorManaged file;
    shadingNode -asUtility place2dTexture;
    connectAttr -f place2dTexture1.coverage file1.coverage;
    connectAttr -f place2dTexture1.translateFrame file1.translateFrame;
    connectAttr -f place2dTexture1.rotateFrame file1.rotateFrame;
    connectAttr -f place2dTexture1.mirrorU file1.mirrorU;
    connectAttr -f place2dTexture1.mirrorV file1.mirrorV;
    connectAttr -f place2dTexture1.stagger file1.stagger;
    connectAttr -f place2dTexture1.wrapU file1.wrapU;
    connectAttr -f place2dTexture1.wrapV file1.wrapV;
    connectAttr -f place2dTexture1.repeatUV file1.repeatUV;
    connectAttr -f place2dTexture1.offset file1.offset;
    connectAttr -f place2dTexture1.rotateUV file1.rotateUV;
    connectAttr -f place2dTexture1.noiseUV file1.noiseUV;
    connectAttr -f place2dTexture1.vertexUvOne file1.vertexUvOne;
    connectAttr -f place2dTexture1.vertexUvTwo file1.vertexUvTwo;
    connectAttr -f place2dTexture1.vertexUvThree file1.vertexUvThree;
    connectAttr -f place2dTexture1.vertexCameraOne file1.vertexCameraOne;
    connectAttr place2dTexture1.outUV file1.uv;
    connectAttr place2dTexture1.outUvFilterSize file1.uvFilterSize;
    rename place2dTexture1 "place1" ;
    rename file1 "Text1" ;
             """)
    mel.eval("""
    shadingNode -asTexture -isColorManaged file;
    shadingNode -asUtility place2dTexture;
    connectAttr -f place2dTexture1.coverage file1.coverage;
    connectAttr -f place2dTexture1.translateFrame file1.translateFrame;
    connectAttr -f place2dTexture1.rotateFrame file1.rotateFrame;
    connectAttr -f place2dTexture1.mirrorU file1.mirrorU;
    connectAttr -f place2dTexture1.mirrorV file1.mirrorV;
    connectAttr -f place2dTexture1.stagger file1.stagger;
    connectAttr -f place2dTexture1.wrapU file1.wrapU;
    connectAttr -f place2dTexture1.wrapV file1.wrapV;
    connectAttr -f place2dTexture1.repeatUV file1.repeatUV;
    connectAttr -f place2dTexture1.offset file1.offset;
    connectAttr -f place2dTexture1.rotateUV file1.rotateUV;
    connectAttr -f place2dTexture1.noiseUV file1.noiseUV;
    connectAttr -f place2dTexture1.vertexUvOne file1.vertexUvOne;
    connectAttr -f place2dTexture1.vertexUvTwo file1.vertexUvTwo;
    connectAttr -f place2dTexture1.vertexUvThree file1.vertexUvThree;
    connectAttr -f place2dTexture1.vertexCameraOne file1.vertexCameraOne;
    connectAttr place2dTexture1.outUV file1.uv;
    connectAttr place2dTexture1.outUvFilterSize file1.uvFilterSize;
    rename place2dTexture1 "place1" ;
    rename file1 "Text1" ;
             """)
    mel.eval("""
    shadingNode -asTexture -isColorManaged file;
    shadingNode -asUtility place2dTexture;
    connectAttr -f place2dTexture1.coverage file1.coverage;
    connectAttr -f place2dTexture1.translateFrame file1.translateFrame;
    connectAttr -f place2dTexture1.rotateFrame file1.rotateFrame;
    connectAttr -f place2dTexture1.mirrorU file1.mirrorU;
    connectAttr -f place2dTexture1.mirrorV file1.mirrorV;
    connectAttr -f place2dTexture1.stagger file1.stagger;
    connectAttr -f place2dTexture1.wrapU file1.wrapU;
    connectAttr -f place2dTexture1.wrapV file1.wrapV;
    connectAttr -f place2dTexture1.repeatUV file1.repeatUV;
    connectAttr -f place2dTexture1.offset file1.offset;
    connectAttr -f place2dTexture1.rotateUV file1.rotateUV;
    connectAttr -f place2dTexture1.noiseUV file1.noiseUV;
    connectAttr -f place2dTexture1.vertexUvOne file1.vertexUvOne;
    connectAttr -f place2dTexture1.vertexUvTwo file1.vertexUvTwo;
    connectAttr -f place2dTexture1.vertexUvThree file1.vertexUvThree;
    connectAttr -f place2dTexture1.vertexCameraOne file1.vertexCameraOne;
    connectAttr place2dTexture1.outUV file1.uv;
    connectAttr place2dTexture1.outUvFilterSize file1.uvFilterSize;
    rename place2dTexture1 "place1" ;
    rename file1 "Text1" ;
             """)
    mel.eval("""
    shadingNode -asTexture -isColorManaged file;
    shadingNode -asUtility place2dTexture;
    connectAttr -f place2dTexture1.coverage file1.coverage;
    connectAttr -f place2dTexture1.translateFrame file1.translateFrame;
    connectAttr -f place2dTexture1.rotateFrame file1.rotateFrame;
    connectAttr -f place2dTexture1.mirrorU file1.mirrorU;
    connectAttr -f place2dTexture1.mirrorV file1.mirrorV;
    connectAttr -f place2dTexture1.stagger file1.stagger;
    connectAttr -f place2dTexture1.wrapU file1.wrapU;
    connectAttr -f place2dTexture1.wrapV file1.wrapV;
    connectAttr -f place2dTexture1.repeatUV file1.repeatUV;
    connectAttr -f place2dTexture1.offset file1.offset;
    connectAttr -f place2dTexture1.rotateUV file1.rotateUV;
    connectAttr -f place2dTexture1.noiseUV file1.noiseUV;
    connectAttr -f place2dTexture1.vertexUvOne file1.vertexUvOne;
    connectAttr -f place2dTexture1.vertexUvTwo file1.vertexUvTwo;
    connectAttr -f place2dTexture1.vertexUvThree file1.vertexUvThree;
    connectAttr -f place2dTexture1.vertexCameraOne file1.vertexCameraOne;
    connectAttr place2dTexture1.outUV file1.uv;
    connectAttr place2dTexture1.outUvFilterSize file1.uvFilterSize;
    rename place2dTexture1 "place1" ;
    rename file1 "Text1" ;
             """)
    mel.eval("""
    shadingNode -asTexture -isColorManaged file;
    shadingNode -asUtility place2dTexture;
    connectAttr -f place2dTexture1.coverage file1.coverage;
    connectAttr -f place2dTexture1.translateFrame file1.translateFrame;
    connectAttr -f place2dTexture1.rotateFrame file1.rotateFrame;
    connectAttr -f place2dTexture1.mirrorU file1.mirrorU;
    connectAttr -f place2dTexture1.mirrorV file1.mirrorV;
    connectAttr -f place2dTexture1.stagger file1.stagger;
    connectAttr -f place2dTexture1.wrapU file1.wrapU;
    connectAttr -f place2dTexture1.wrapV file1.wrapV;
    connectAttr -f place2dTexture1.repeatUV file1.repeatUV;
    connectAttr -f place2dTexture1.offset file1.offset;
    connectAttr -f place2dTexture1.rotateUV file1.rotateUV;
    connectAttr -f place2dTexture1.noiseUV file1.noiseUV;
    connectAttr -f place2dTexture1.vertexUvOne file1.vertexUvOne;
    connectAttr -f place2dTexture1.vertexUvTwo file1.vertexUvTwo;
    connectAttr -f place2dTexture1.vertexUvThree file1.vertexUvThree;
    connectAttr -f place2dTexture1.vertexCameraOne file1.vertexCameraOne;
    connectAttr place2dTexture1.outUV file1.uv;
    connectAttr place2dTexture1.outUvFilterSize file1.uvFilterSize;
    rename place2dTexture1 "place1" ;
    rename file1 "Text1" ;
             """)
    mel.eval("""
    shadingNode -asTexture -isColorManaged file;
    shadingNode -asUtility place2dTexture;
    connectAttr -f place2dTexture1.coverage file1.coverage;
    connectAttr -f place2dTexture1.translateFrame file1.translateFrame;
    connectAttr -f place2dTexture1.rotateFrame file1.rotateFrame;
    connectAttr -f place2dTexture1.mirrorU file1.mirrorU;
    connectAttr -f place2dTexture1.mirrorV file1.mirrorV;
    connectAttr -f place2dTexture1.stagger file1.stagger;
    connectAttr -f place2dTexture1.wrapU file1.wrapU;
    connectAttr -f place2dTexture1.wrapV file1.wrapV;
    connectAttr -f place2dTexture1.repeatUV file1.repeatUV;
    connectAttr -f place2dTexture1.offset file1.offset;
    connectAttr -f place2dTexture1.rotateUV file1.rotateUV;
    connectAttr -f place2dTexture1.noiseUV file1.noiseUV;
    connectAttr -f place2dTexture1.vertexUvOne file1.vertexUvOne;
    connectAttr -f place2dTexture1.vertexUvTwo file1.vertexUvTwo;
    connectAttr -f place2dTexture1.vertexUvThree file1.vertexUvThree;
    connectAttr -f place2dTexture1.vertexCameraOne file1.vertexCameraOne;
    connectAttr place2dTexture1.outUV file1.uv;
    connectAttr place2dTexture1.outUvFilterSize file1.uvFilterSize;
    rename place2dTexture1 "place1" ;
    rename file1 "Text1" ;
             """)
    mel.eval("""
    shadingNode -asTexture -isColorManaged file;
    shadingNode -asUtility place2dTexture;
    connectAttr -f place2dTexture1.coverage file1.coverage;
    connectAttr -f place2dTexture1.translateFrame file1.translateFrame;
    connectAttr -f place2dTexture1.rotateFrame file1.rotateFrame;
    connectAttr -f place2dTexture1.mirrorU file1.mirrorU;
    connectAttr -f place2dTexture1.mirrorV file1.mirrorV;
    connectAttr -f place2dTexture1.stagger file1.stagger;
    connectAttr -f place2dTexture1.wrapU file1.wrapU;
    connectAttr -f place2dTexture1.wrapV file1.wrapV;
    connectAttr -f place2dTexture1.repeatUV file1.repeatUV;
    connectAttr -f place2dTexture1.offset file1.offset;
    connectAttr -f place2dTexture1.rotateUV file1.rotateUV;
    connectAttr -f place2dTexture1.noiseUV file1.noiseUV;
    connectAttr -f place2dTexture1.vertexUvOne file1.vertexUvOne;
    connectAttr -f place2dTexture1.vertexUvTwo file1.vertexUvTwo;
    connectAttr -f place2dTexture1.vertexUvThree file1.vertexUvThree;
    connectAttr -f place2dTexture1.vertexCameraOne file1.vertexCameraOne;
    connectAttr place2dTexture1.outUV file1.uv;
    connectAttr place2dTexture1.outUvFilterSize file1.uvFilterSize;
    rename place2dTexture1 "place1" ;
    rename file1 "Text1" ;
             """)
    mel.eval("""
    shadingNode -asTexture -isColorManaged file;
    shadingNode -asUtility place2dTexture;
    connectAttr -f place2dTexture1.coverage file1.coverage;
    connectAttr -f place2dTexture1.translateFrame file1.translateFrame;
    connectAttr -f place2dTexture1.rotateFrame file1.rotateFrame;
    connectAttr -f place2dTexture1.mirrorU file1.mirrorU;
    connectAttr -f place2dTexture1.mirrorV file1.mirrorV;
    connectAttr -f place2dTexture1.stagger file1.stagger;
    connectAttr -f place2dTexture1.wrapU file1.wrapU;
    connectAttr -f place2dTexture1.wrapV file1.wrapV;
    connectAttr -f place2dTexture1.repeatUV file1.repeatUV;
    connectAttr -f place2dTexture1.offset file1.offset;
    connectAttr -f place2dTexture1.rotateUV file1.rotateUV;
    connectAttr -f place2dTexture1.noiseUV file1.noiseUV;
    connectAttr -f place2dTexture1.vertexUvOne file1.vertexUvOne;
    connectAttr -f place2dTexture1.vertexUvTwo file1.vertexUvTwo;
    connectAttr -f place2dTexture1.vertexUvThree file1.vertexUvThree;
    connectAttr -f place2dTexture1.vertexCameraOne file1.vertexCameraOne;
    connectAttr place2dTexture1.outUV file1.uv;
    connectAttr place2dTexture1.outUvFilterSize file1.uvFilterSize;
    rename place2dTexture1 "place1" ;
    rename file1 "Text1" ;
             """)
    mel.eval("""
    shadingNode -asTexture -isColorManaged file;
    shadingNode -asUtility place2dTexture;
    connectAttr -f place2dTexture1.coverage file1.coverage;
    connectAttr -f place2dTexture1.translateFrame file1.translateFrame;
    connectAttr -f place2dTexture1.rotateFrame file1.rotateFrame;
    connectAttr -f place2dTexture1.mirrorU file1.mirrorU;
    connectAttr -f place2dTexture1.mirrorV file1.mirrorV;
    connectAttr -f place2dTexture1.stagger file1.stagger;
    connectAttr -f place2dTexture1.wrapU file1.wrapU;
    connectAttr -f place2dTexture1.wrapV file1.wrapV;
    connectAttr -f place2dTexture1.repeatUV file1.repeatUV;
    connectAttr -f place2dTexture1.offset file1.offset;
    connectAttr -f place2dTexture1.rotateUV file1.rotateUV;
    connectAttr -f place2dTexture1.noiseUV file1.noiseUV;
    connectAttr -f place2dTexture1.vertexUvOne file1.vertexUvOne;
    connectAttr -f place2dTexture1.vertexUvTwo file1.vertexUvTwo;
    connectAttr -f place2dTexture1.vertexUvThree file1.vertexUvThree;
    connectAttr -f place2dTexture1.vertexCameraOne file1.vertexCameraOne;
    connectAttr place2dTexture1.outUV file1.uv;
    connectAttr place2dTexture1.outUvFilterSize file1.uvFilterSize;
    rename place2dTexture1 "place1" ;
    rename file1 "Text1" ;
             """)
    mel.eval("""
    shadingNode -asTexture -isColorManaged file;
    shadingNode -asUtility place2dTexture;
    connectAttr -f place2dTexture1.coverage file1.coverage;
    connectAttr -f place2dTexture1.translateFrame file1.translateFrame;
    connectAttr -f place2dTexture1.rotateFrame file1.rotateFrame;
    connectAttr -f place2dTexture1.mirrorU file1.mirrorU;
    connectAttr -f place2dTexture1.mirrorV file1.mirrorV;
    connectAttr -f place2dTexture1.stagger file1.stagger;
    connectAttr -f place2dTexture1.wrapU file1.wrapU;
    connectAttr -f place2dTexture1.wrapV file1.wrapV;
    connectAttr -f place2dTexture1.repeatUV file1.repeatUV;
    connectAttr -f place2dTexture1.offset file1.offset;
    connectAttr -f place2dTexture1.rotateUV file1.rotateUV;
    connectAttr -f place2dTexture1.noiseUV file1.noiseUV;
    connectAttr -f place2dTexture1.vertexUvOne file1.vertexUvOne;
    connectAttr -f place2dTexture1.vertexUvTwo file1.vertexUvTwo;
    connectAttr -f place2dTexture1.vertexUvThree file1.vertexUvThree;
    connectAttr -f place2dTexture1.vertexCameraOne file1.vertexCameraOne;
    connectAttr place2dTexture1.outUV file1.uv;
    connectAttr place2dTexture1.outUvFilterSize file1.uvFilterSize;
    rename place2dTexture1 "place1" ;
    rename file1 "Text1" ;
             """)
    mel.eval("""
    shadingNode -asTexture -isColorManaged file;
    shadingNode -asUtility place2dTexture;
    connectAttr -f place2dTexture1.coverage file1.coverage;
    connectAttr -f place2dTexture1.translateFrame file1.translateFrame;
    connectAttr -f place2dTexture1.rotateFrame file1.rotateFrame;
    connectAttr -f place2dTexture1.mirrorU file1.mirrorU;
    connectAttr -f place2dTexture1.mirrorV file1.mirrorV;
    connectAttr -f place2dTexture1.stagger file1.stagger;
    connectAttr -f place2dTexture1.wrapU file1.wrapU;
    connectAttr -f place2dTexture1.wrapV file1.wrapV;
    connectAttr -f place2dTexture1.repeatUV file1.repeatUV;
    connectAttr -f place2dTexture1.offset file1.offset;
    connectAttr -f place2dTexture1.rotateUV file1.rotateUV;
    connectAttr -f place2dTexture1.noiseUV file1.noiseUV;
    connectAttr -f place2dTexture1.vertexUvOne file1.vertexUvOne;
    connectAttr -f place2dTexture1.vertexUvTwo file1.vertexUvTwo;
    connectAttr -f place2dTexture1.vertexUvThree file1.vertexUvThree;
    connectAttr -f place2dTexture1.vertexCameraOne file1.vertexCameraOne;
    connectAttr place2dTexture1.outUV file1.uv;
    connectAttr place2dTexture1.outUvFilterSize file1.uvFilterSize;
    rename place2dTexture1 "place1" ;
    rename file1 "Text1" ;
             """)
    mel.eval("""
    shadingNode -asTexture -isColorManaged file;
    shadingNode -asUtility place2dTexture;
    connectAttr -f place2dTexture1.coverage file1.coverage;
    connectAttr -f place2dTexture1.translateFrame file1.translateFrame;
    connectAttr -f place2dTexture1.rotateFrame file1.rotateFrame;
    connectAttr -f place2dTexture1.mirrorU file1.mirrorU;
    connectAttr -f place2dTexture1.mirrorV file1.mirrorV;
    connectAttr -f place2dTexture1.stagger file1.stagger;
    connectAttr -f place2dTexture1.wrapU file1.wrapU;
    connectAttr -f place2dTexture1.wrapV file1.wrapV;
    connectAttr -f place2dTexture1.repeatUV file1.repeatUV;
    connectAttr -f place2dTexture1.offset file1.offset;
    connectAttr -f place2dTexture1.rotateUV file1.rotateUV;
    connectAttr -f place2dTexture1.noiseUV file1.noiseUV;
    connectAttr -f place2dTexture1.vertexUvOne file1.vertexUvOne;
    connectAttr -f place2dTexture1.vertexUvTwo file1.vertexUvTwo;
    connectAttr -f place2dTexture1.vertexUvThree file1.vertexUvThree;
    connectAttr -f place2dTexture1.vertexCameraOne file1.vertexCameraOne;
    connectAttr place2dTexture1.outUV file1.uv;
    connectAttr place2dTexture1.outUvFilterSize file1.uvFilterSize;
    rename place2dTexture1 "place1" ;
    rename file1 "Text1" ;
             """)
    mel.eval("""
    shadingNode -asTexture -isColorManaged file;
    shadingNode -asUtility place2dTexture;
    connectAttr -f place2dTexture1.coverage file1.coverage;
    connectAttr -f place2dTexture1.translateFrame file1.translateFrame;
    connectAttr -f place2dTexture1.rotateFrame file1.rotateFrame;
    connectAttr -f place2dTexture1.mirrorU file1.mirrorU;
    connectAttr -f place2dTexture1.mirrorV file1.mirrorV;
    connectAttr -f place2dTexture1.stagger file1.stagger;
    connectAttr -f place2dTexture1.wrapU file1.wrapU;
    connectAttr -f place2dTexture1.wrapV file1.wrapV;
    connectAttr -f place2dTexture1.repeatUV file1.repeatUV;
    connectAttr -f place2dTexture1.offset file1.offset;
    connectAttr -f place2dTexture1.rotateUV file1.rotateUV;
    connectAttr -f place2dTexture1.noiseUV file1.noiseUV;
    connectAttr -f place2dTexture1.vertexUvOne file1.vertexUvOne;
    connectAttr -f place2dTexture1.vertexUvTwo file1.vertexUvTwo;
    connectAttr -f place2dTexture1.vertexUvThree file1.vertexUvThree;
    connectAttr -f place2dTexture1.vertexCameraOne file1.vertexCameraOne;
    connectAttr place2dTexture1.outUV file1.uv;
    connectAttr place2dTexture1.outUvFilterSize file1.uvFilterSize;
    rename place2dTexture1 "place1" ;
    rename file1 "Text1" ;
             """)
    mel.eval("""
    shadingNode -asTexture -isColorManaged file;
    shadingNode -asUtility place2dTexture;
    connectAttr -f place2dTexture1.coverage file1.coverage;
    connectAttr -f place2dTexture1.translateFrame file1.translateFrame;
    connectAttr -f place2dTexture1.rotateFrame file1.rotateFrame;
    connectAttr -f place2dTexture1.mirrorU file1.mirrorU;
    connectAttr -f place2dTexture1.mirrorV file1.mirrorV;
    connectAttr -f place2dTexture1.stagger file1.stagger;
    connectAttr -f place2dTexture1.wrapU file1.wrapU;
    connectAttr -f place2dTexture1.wrapV file1.wrapV;
    connectAttr -f place2dTexture1.repeatUV file1.repeatUV;
    connectAttr -f place2dTexture1.offset file1.offset;
    connectAttr -f place2dTexture1.rotateUV file1.rotateUV;
    connectAttr -f place2dTexture1.noiseUV file1.noiseUV;
    connectAttr -f place2dTexture1.vertexUvOne file1.vertexUvOne;
    connectAttr -f place2dTexture1.vertexUvTwo file1.vertexUvTwo;
    connectAttr -f place2dTexture1.vertexUvThree file1.vertexUvThree;
    connectAttr -f place2dTexture1.vertexCameraOne file1.vertexCameraOne;
    connectAttr place2dTexture1.outUV file1.uv;
    connectAttr place2dTexture1.outUvFilterSize file1.uvFilterSize;
    rename place2dTexture1 "place1" ;
    rename file1 "Text1" ;
             """)
    mel.eval("""
    shadingNode -asTexture -isColorManaged file;
    shadingNode -asUtility place2dTexture;
    connectAttr -f place2dTexture1.coverage file1.coverage;
    connectAttr -f place2dTexture1.translateFrame file1.translateFrame;
    connectAttr -f place2dTexture1.rotateFrame file1.rotateFrame;
    connectAttr -f place2dTexture1.mirrorU file1.mirrorU;
    connectAttr -f place2dTexture1.mirrorV file1.mirrorV;
    connectAttr -f place2dTexture1.stagger file1.stagger;
    connectAttr -f place2dTexture1.wrapU file1.wrapU;
    connectAttr -f place2dTexture1.wrapV file1.wrapV;
    connectAttr -f place2dTexture1.repeatUV file1.repeatUV;
    connectAttr -f place2dTexture1.offset file1.offset;
    connectAttr -f place2dTexture1.rotateUV file1.rotateUV;
    connectAttr -f place2dTexture1.noiseUV file1.noiseUV;
    connectAttr -f place2dTexture1.vertexUvOne file1.vertexUvOne;
    connectAttr -f place2dTexture1.vertexUvTwo file1.vertexUvTwo;
    connectAttr -f place2dTexture1.vertexUvThree file1.vertexUvThree;
    connectAttr -f place2dTexture1.vertexCameraOne file1.vertexCameraOne;
    connectAttr place2dTexture1.outUV file1.uv;
    connectAttr place2dTexture1.outUvFilterSize file1.uvFilterSize;
    rename place2dTexture1 "place1" ;
    rename file1 "Text1" ;
             """)
    mel.eval("""
    shadingNode -asTexture -isColorManaged file;
    shadingNode -asUtility place2dTexture;
    connectAttr -f place2dTexture1.coverage file1.coverage;
    connectAttr -f place2dTexture1.translateFrame file1.translateFrame;
    connectAttr -f place2dTexture1.rotateFrame file1.rotateFrame;
    connectAttr -f place2dTexture1.mirrorU file1.mirrorU;
    connectAttr -f place2dTexture1.mirrorV file1.mirrorV;
    connectAttr -f place2dTexture1.stagger file1.stagger;
    connectAttr -f place2dTexture1.wrapU file1.wrapU;
    connectAttr -f place2dTexture1.wrapV file1.wrapV;
    connectAttr -f place2dTexture1.repeatUV file1.repeatUV;
    connectAttr -f place2dTexture1.offset file1.offset;
    connectAttr -f place2dTexture1.rotateUV file1.rotateUV;
    connectAttr -f place2dTexture1.noiseUV file1.noiseUV;
    connectAttr -f place2dTexture1.vertexUvOne file1.vertexUvOne;
    connectAttr -f place2dTexture1.vertexUvTwo file1.vertexUvTwo;
    connectAttr -f place2dTexture1.vertexUvThree file1.vertexUvThree;
    connectAttr -f place2dTexture1.vertexCameraOne file1.vertexCameraOne;
    connectAttr place2dTexture1.outUV file1.uv;
    connectAttr place2dTexture1.outUvFilterSize file1.uvFilterSize;
    rename place2dTexture1 "place1" ;
    rename file1 "Text1" ;
             """)
    mel.eval("""
    shadingNode -asTexture -isColorManaged file;
    shadingNode -asUtility place2dTexture;
    connectAttr -f place2dTexture1.coverage file1.coverage;
    connectAttr -f place2dTexture1.translateFrame file1.translateFrame;
    connectAttr -f place2dTexture1.rotateFrame file1.rotateFrame;
    connectAttr -f place2dTexture1.mirrorU file1.mirrorU;
    connectAttr -f place2dTexture1.mirrorV file1.mirrorV;
    connectAttr -f place2dTexture1.stagger file1.stagger;
    connectAttr -f place2dTexture1.wrapU file1.wrapU;
    connectAttr -f place2dTexture1.wrapV file1.wrapV;
    connectAttr -f place2dTexture1.repeatUV file1.repeatUV;
    connectAttr -f place2dTexture1.offset file1.offset;
    connectAttr -f place2dTexture1.rotateUV file1.rotateUV;
    connectAttr -f place2dTexture1.noiseUV file1.noiseUV;
    connectAttr -f place2dTexture1.vertexUvOne file1.vertexUvOne;
    connectAttr -f place2dTexture1.vertexUvTwo file1.vertexUvTwo;
    connectAttr -f place2dTexture1.vertexUvThree file1.vertexUvThree;
    connectAttr -f place2dTexture1.vertexCameraOne file1.vertexCameraOne;
    connectAttr place2dTexture1.outUV file1.uv;
    connectAttr place2dTexture1.outUvFilterSize file1.uvFilterSize;
    rename place2dTexture1 "place1" ;
    rename file1 "Text1" ;
             """)
    mel.eval("""
    shadingNode -asTexture -isColorManaged file;
    shadingNode -asUtility place2dTexture;
    connectAttr -f place2dTexture1.coverage file1.coverage;
    connectAttr -f place2dTexture1.translateFrame file1.translateFrame;
    connectAttr -f place2dTexture1.rotateFrame file1.rotateFrame;
    connectAttr -f place2dTexture1.mirrorU file1.mirrorU;
    connectAttr -f place2dTexture1.mirrorV file1.mirrorV;
    connectAttr -f place2dTexture1.stagger file1.stagger;
    connectAttr -f place2dTexture1.wrapU file1.wrapU;
    connectAttr -f place2dTexture1.wrapV file1.wrapV;
    connectAttr -f place2dTexture1.repeatUV file1.repeatUV;
    connectAttr -f place2dTexture1.offset file1.offset;
    connectAttr -f place2dTexture1.rotateUV file1.rotateUV;
    connectAttr -f place2dTexture1.noiseUV file1.noiseUV;
    connectAttr -f place2dTexture1.vertexUvOne file1.vertexUvOne;
    connectAttr -f place2dTexture1.vertexUvTwo file1.vertexUvTwo;
    connectAttr -f place2dTexture1.vertexUvThree file1.vertexUvThree;
    connectAttr -f place2dTexture1.vertexCameraOne file1.vertexCameraOne;
    connectAttr place2dTexture1.outUV file1.uv;
    connectAttr place2dTexture1.outUvFilterSize file1.uvFilterSize;
    rename place2dTexture1 "place1" ;
    rename file1 "Text1" ;
             """)        
    cmds.connectAttr('Text1.outColor', 'Switchmt1.material_0', force=True)
    cmds.connectAttr('Text2.outColor', 'Switchmt1.material_1', force=True)
    cmds.connectAttr('Text3.outColor', 'Switchmt1.material_2', force=True)
    cmds.connectAttr('Text4.outColor', 'Switchmt1.material_3', force=True)
    cmds.connectAttr('Text5.outColor', 'Switchmt1.material_4', force=True)
    cmds.connectAttr('Text6.outColor', 'Switchmt1.material_5', force=True)
    cmds.connectAttr('Text7.outColor', 'Switchmt1.material_6', force=True)
    cmds.connectAttr('Text8.outColor', 'Switchmt1.material_7', force=True)
    cmds.connectAttr('Text9.outColor', 'Switchmt1.material_8', force=True)
    cmds.connectAttr('Text10.outColor', 'Switchmt1.material_9', force=True)
    cmds.connectAttr('Text11.outColor', 'Switchmt2.material_0', force=True)
    cmds.connectAttr('Text12.outColor', 'Switchmt2.material_1', force=True)
    cmds.connectAttr('Text13.outColor', 'Switchmt2.material_2', force=True)
    cmds.connectAttr('Text14.outColor', 'Switchmt2.material_3', force=True)
    cmds.connectAttr('Text15.outColor', 'Switchmt2.material_4', force=True)
    cmds.connectAttr('Text16.outColor', 'Switchmt2.material_5', force=True)
    cmds.connectAttr('Text17.outColor', 'Switchmt2.material_6', force=True)
    cmds.connectAttr('Text18.outColor', 'Switchmt2.material_7', force=True)
    cmds.connectAttr('Text19.outColor', 'Switchmt2.material_8', force=True)
    cmds.connectAttr('Text20.outColor', 'Switchmt2.material_9', force=True)

    cmds.connectAttr('SwitchShader1.output', 'VRayMtl1.color', force=True)
    # mel.eval('sets -e -forceElement VRayMtl1SG;')
    cmds.setAttr('Text1.ignoreColorSpaceFileRules', True)
    cmds.setAttr('Text2.ignoreColorSpaceFileRules', True)
    cmds.setAttr('Text3.ignoreColorSpaceFileRules', True)
    cmds.setAttr('Text4.ignoreColorSpaceFileRules', True)
    cmds.setAttr('Text5.ignoreColorSpaceFileRules', True)
    cmds.setAttr('Text6.ignoreColorSpaceFileRules', True)
    cmds.setAttr('Text7.ignoreColorSpaceFileRules', True)
    cmds.setAttr('Text8.ignoreColorSpaceFileRules', True)
    cmds.setAttr('Text9.ignoreColorSpaceFileRules', True)
    cmds.setAttr('Text10.ignoreColorSpaceFileRules', True)
    cmds.setAttr('Text11.ignoreColorSpaceFileRules', True)
    cmds.setAttr('Text12.ignoreColorSpaceFileRules', True)
    cmds.setAttr('Text13.ignoreColorSpaceFileRules', True)
    cmds.setAttr('Text14.ignoreColorSpaceFileRules', True)
    cmds.setAttr('Text15.ignoreColorSpaceFileRules', True)
    cmds.setAttr('Text16.ignoreColorSpaceFileRules', True)
    cmds.setAttr('Text17.ignoreColorSpaceFileRules', True)
    cmds.setAttr('Text18.ignoreColorSpaceFileRules', True)
    cmds.setAttr('Text19.ignoreColorSpaceFileRules', True)
    cmds.setAttr('Text20.ignoreColorSpaceFileRules', True)

################################################################    
