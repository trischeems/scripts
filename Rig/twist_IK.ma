//Maya ASCII 2020 scene
//Name: twist_IK.ma
//Last modified: Fri, Jun 14, 2024 12:45:17 PM
//Codeset: 1252
requires maya "2020";
requires -nodeType "floatMath" "lookdevKit" "1.0";
requires "mtoa" "4.1.1";
currentUnit -l centimeter -a degree -t film;
fileInfo "application" "maya";
fileInfo "product" "Maya 2020";
fileInfo "version" "2020";
fileInfo "cutIdentifier" "202011110415-b1e20b88e2";
fileInfo "osv" "Microsoft Windows 10 Technical Preview  (Build 22631)\n";
fileInfo "UUID" "98B7A370-4615-CB65-0963-77812E024860";
createNode transform -s -n "persp";
	rename -uid "3FE6FA48-4B4E-5ADD-2A43-FCA3BEC9BDF2";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 3.1895259075692972 6.0008152134913262 11.833193574769709 ;
	setAttr ".r" -type "double3" -24.938352729663425 -4.2000000000013769 -8.9693975630546302e-16 ;
createNode camera -s -n "perspShape" -p "persp";
	rename -uid "0906E731-4CBF-752A-CCBD-D08525D02CFC";
	setAttr -k off ".v" no;
	setAttr ".pze" yes;
	setAttr ".fl" 34.999999999999993;
	setAttr ".coi" 6.9525152606345335;
	setAttr ".imn" -type "string" "persp";
	setAttr ".den" -type "string" "persp_depth";
	setAttr ".man" -type "string" "persp_mask";
	setAttr ".tp" -type "double3" 7.6644010775628102 2.3957073158722242 1.1708652419602197 ;
	setAttr ".hc" -type "string" "viewSet -p %camera";
	setAttr ".ai_translator" -type "string" "perspective";
createNode transform -s -n "top";
	rename -uid "B638BCBC-4BA9-330C-6D56-74B8F87147ED";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 1000.1 0 ;
	setAttr ".r" -type "double3" -90 0 0 ;
createNode camera -s -n "topShape" -p "top";
	rename -uid "E9298CA2-4C02-A4EF-1E88-989E5533D2CF";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 1000.1;
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "top";
	setAttr ".den" -type "string" "top_depth";
	setAttr ".man" -type "string" "top_mask";
	setAttr ".tp" -type "double3" 7.6644010775628102 2.3957073158722242 1.1708652419602197 ;
	setAttr ".hc" -type "string" "viewSet -t %camera";
	setAttr ".o" yes;
	setAttr ".ai_translator" -type "string" "orthographic";
createNode transform -s -n "front";
	rename -uid "1185172A-4DAA-D030-FA17-70B19E55D0AD";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 0 1000.1 ;
createNode camera -s -n "frontShape" -p "front";
	rename -uid "1FE1EABD-4012-D1B2-42B9-3F82E5786365";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 1000.1;
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "front";
	setAttr ".den" -type "string" "front_depth";
	setAttr ".man" -type "string" "front_mask";
	setAttr ".tp" -type "double3" 7.6644010775628102 2.3957073158722242 1.1708652419602197 ;
	setAttr ".hc" -type "string" "viewSet -f %camera";
	setAttr ".o" yes;
	setAttr ".ai_translator" -type "string" "orthographic";
createNode transform -s -n "side";
	rename -uid "1B357501-4A5E-A8DB-530A-D78018E6E826";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 1000.1 0 0 ;
	setAttr ".r" -type "double3" 0 90 0 ;
createNode camera -s -n "sideShape" -p "side";
	rename -uid "9ACABAE4-46AE-3CE5-7274-8FACB2835119";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 1000.1;
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "side";
	setAttr ".den" -type "string" "side_depth";
	setAttr ".man" -type "string" "side_mask";
	setAttr ".tp" -type "double3" 7.6644010775628102 2.3957073158722242 1.1708652419602197 ;
	setAttr ".hc" -type "string" "viewSet -s %camera";
	setAttr ".o" yes;
	setAttr ".ai_translator" -type "string" "orthographic";
createNode joint -n "Shoulder";
	rename -uid "49BBF974-4AC9-E043-FEA2-0AA7652F9F15";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".r" -type "double3" 10.340464084986873 -11.596759423001121 20.486756246854746 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 14.036243467926484 0 ;
	setAttr ".bps" -type "matrix" 0.97014250014533188 0 -0.24253562503633305 0 0 1 0 0
		 0.24253562503633305 0 0.97014250014533188 0 0 0 0 1;
createNode joint -n "Elbow" -p "Shoulder";
	rename -uid "3F0F3EF3-4783-450E-0922-BE96B70CBDC1";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 1;
	setAttr ".t" -type "double3" 4.1231056256176606 0 3.3306690738754696e-16 ;
	setAttr ".r" -type "double3" 0 7.6039151603971851 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".dla" yes;
	setAttr ".jo" -type "double3" 0 -28.072486935852961 0 ;
	setAttr ".bps" -type "matrix" 0.97014250014533199 0 0.24253562503633297 0 0 1 0 0
		 -0.24253562503633297 0 0.97014250014533199 0 4 0 -1.0000000000000002 1;
createNode joint -n "Wrist" -p "Elbow";
	rename -uid "FB6F45C1-4558-9433-3DF0-6C8D59BAC6E5";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".oc" 2;
	setAttr ".t" -type "double3" 4.1231056256176597 0 3.3306690738754696e-16 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".dla" yes;
	setAttr ".bps" -type "matrix" 0.97014250014533199 0 0.24253562503633297 0 0 1 0 0
		 -0.24253562503633297 0 0.97014250014533199 0 8 0 -2.2204460492503131e-16 1;
createNode ikEffector -n "effector1" -p "Elbow";
	rename -uid "BABD2CCA-458F-6FC9-3BEB-B28986207F45";
	setAttr ".v" no;
	setAttr ".hd" yes;
createNode transform -n "loftedSurface1";
	rename -uid "E23CFC1B-4435-6CE5-FEE3-8DABC735A0FA";
createNode nurbsSurface -n "loftedSurfaceShape1" -p "loftedSurface1";
	rename -uid "43DBC148-4343-8460-5745-579110FA3782";
	setAttr -k off ".v";
	setAttr -s 2 ".iog[0].og";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".tw" yes;
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".dvu" 0;
	setAttr ".dvv" 0;
	setAttr ".cpr" 4;
	setAttr ".cps" 4;
createNode nurbsSurface -n "loftedSurfaceShape1Orig" -p "loftedSurface1";
	rename -uid "FCAC784D-4699-2B42-6533-09BD8BB61B97";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".dvu" 0;
	setAttr ".dvv" 0;
	setAttr ".cpr" 4;
	setAttr ".cps" 4;
	setAttr ".cc" -type "nurbsSurface" 
		3 1 0 0 no 
		8 0 0 0 1 2 3 3 3
		3 0 0.19999999999999998 0.39999999999999997
		
		18
		0 -0.20000000000000001 0
		0 0 0
		0 0.20000000000000001 0
		0.4444444550408303 -0.20000000000000001 -0.11111111376020757
		0.4444444550408303 0 -0.11111111376020757
		0.4444444550408303 0.20000000000000001 -0.11111111376020757
		1.3333333651224821 -0.20000000000000001 -0.33333334128062053
		1.3333333651224821 0 -0.33333334128062053
		1.3333333651224821 0.20000000000000001 -0.33333334128062053
		2.6666667779286772 -0.20000000000000001 -0.66666669448216931
		2.6666667779286772 0 -0.66666669448216931
		2.6666667779286772 0.20000000000000001 -0.66666669448216931
		3.5555555926429117 -0.20000000000000001 -0.88888889816072791
		3.5555555926429117 0 -0.88888889816072791
		3.5555555926429117 0.20000000000000001 -0.88888889816072791
		4.0000000000000195 -0.20000000000000001 -1.0000000000000049
		4.0000000000000195 0 -1.0000000000000049
		4.0000000000000195 0.20000000000000001 -1.0000000000000049
		
		;
createNode transform -n "loftedSurface2";
	rename -uid "4E92683F-49B1-3064-38D5-AD83B82D8BCA";
createNode nurbsSurface -n "loftedSurfaceShape2" -p "loftedSurface2";
	rename -uid "BC854CDF-4DA1-B56A-FE94-F99B2F53FC63";
	setAttr -k off ".v";
	setAttr -s 2 ".iog[0].og";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".tw" yes;
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".dvu" 0;
	setAttr ".dvv" 0;
	setAttr ".cpr" 4;
	setAttr ".cps" 4;
createNode nurbsSurface -n "loftedSurfaceShape2Orig" -p "loftedSurface2";
	rename -uid "48F84E26-481C-2DEA-67DB-08ACE512251E";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".dvu" 0;
	setAttr ".dvv" 0;
	setAttr ".cpr" 4;
	setAttr ".cps" 4;
	setAttr ".cc" -type "nurbsSurface" 
		3 1 0 0 no 
		8 0 0 0 1 2 3 3 3
		3 0 0.19999999999999998 0.39999999999999997
		
		18
		4.0000000000000471 0.20000000000000001 -1.000000000000012
		4.0000000000000471 0 -1.000000000000012
		4.0000000000000471 -0.20000000000000001 -1.000000000000012
		4.4444445504083117 0.20000000000000001 -0.88888889816073402
		4.4444445504083117 0 -0.88888889816073402
		4.4444445504083117 -0.20000000000000001 -0.88888889816073402
		5.3333336512248026 0.20000000000000001 -0.66666669448217308
		5.3333336512248026 0 -0.66666669448217308
		5.3333336512248026 -0.20000000000000001 -0.66666669448217308
		6.6666663487752302 0.20000000000000001 -0.33333334128061615
		6.6666663487752302 0 -0.33333334128061615
		6.6666663487752302 -0.20000000000000001 -0.33333334128061615
		7.5555554495917843 0.20000000000000001 -0.11111111376020616
		7.5555554495917843 0 -0.11111111376020616
		7.5555554495917843 -0.20000000000000001 -0.11111111376020616
		8.0000000000000391 0.20000000000000001 -2.7755575615628943e-16
		8.0000000000000391 0 -2.7755575615628943e-16
		8.0000000000000391 -0.20000000000000001 -2.7755575615628943e-16
		
		;
createNode transform -n "hairSystem1Follicles";
	rename -uid "03D7B464-431F-381E-CB17-F8B8BE0446F5";
createNode transform -n "Hand1" -p "hairSystem1Follicles";
	rename -uid "C831FC23-46D1-255B-2AC0-0CBE515A6F0E";
createNode follicle -n "HandShape1" -p "Hand1";
	rename -uid "94AAA514-414D-FD21-67C7-F89AEDAA4AD1";
	setAttr -k off ".v";
	setAttr ".pv" 0.5;
	setAttr -s 2 ".sts[0:1]"  0 1 3 1 0.2 3;
	setAttr -s 2 ".cws[0:1]"  0 1 3 1 0.2 3;
	setAttr -s 2 ".ats[0:1]"  0 1 3 1 0.2 3;
createNode transform -n "curve1" -p "Hand1";
	rename -uid "072773AD-4249-E4D7-50E3-A2A5E4C9F2A4";
createNode nurbsCurve -n "curveShape1" -p "curve1";
	rename -uid "77911B89-4CBE-D3F9-8BED-26827E745116";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 9 0 no 3
		10 0 1 2 3 4 5 6 7 8 9
		10
		0 0 0
		0 0 0.55555555560000003
		0 0 1.111111111
		0 0 1.6666666670000001
		0 0 2.2222222220000001
		0 0 2.7777777779999999
		0 0 3.3333333330000001
		0 0 3.888888889
		0 0 4.4444444440000002
		0 0 5
		;
createNode transform -n "Hand2" -p "hairSystem1Follicles";
	rename -uid "D97BB3D9-44CB-26AA-2852-3AA4FA78BDD7";
createNode follicle -n "HandShape2" -p "Hand2";
	rename -uid "521EF3EE-4A6A-146D-A53C-69B08177158A";
	setAttr -k off ".v";
	setAttr ".pu" 0.33333333333333331;
	setAttr ".pv" 0.5;
	setAttr -s 2 ".sts[0:1]"  0 1 3 1 0.2 3;
	setAttr -s 2 ".cws[0:1]"  0 1 3 1 0.2 3;
	setAttr -s 2 ".ats[0:1]"  0 1 3 1 0.2 3;
createNode transform -n "curve2" -p "Hand2";
	rename -uid "03262391-432D-86A1-9AFF-1EA95D49E709";
createNode nurbsCurve -n "curveShape2" -p "curve2";
	rename -uid "99F2D7F4-4901-0267-BD33-478028651318";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 9 0 no 3
		10 0 1 2 3 4 5 6 7 8 9
		10
		0 0 0
		0 0 0.55555555560000003
		0 0 1.111111111
		0 0 1.6666666670000001
		0 0 2.2222222220000001
		0 0 2.7777777779999999
		0 0 3.3333333330000001
		0 0 3.888888889
		0 0 4.4444444440000002
		0 0 5
		;
createNode transform -n "Hand3" -p "hairSystem1Follicles";
	rename -uid "CAD2C74A-472B-2787-E0A6-448F44A709A9";
createNode follicle -n "HandShape3" -p "Hand3";
	rename -uid "E3E0B626-4C34-289E-FF90-6294A481424C";
	setAttr -k off ".v";
	setAttr ".pu" 0.66666666666666663;
	setAttr ".pv" 0.5;
	setAttr -s 2 ".sts[0:1]"  0 1 3 1 0.2 3;
	setAttr -s 2 ".cws[0:1]"  0 1 3 1 0.2 3;
	setAttr -s 2 ".ats[0:1]"  0 1 3 1 0.2 3;
createNode transform -n "curve3" -p "Hand3";
	rename -uid "4A31986D-4888-D9D5-A3C3-A092D85CD933";
createNode nurbsCurve -n "curveShape3" -p "curve3";
	rename -uid "2E45728B-410C-6223-D41E-689454768B1E";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 9 0 no 3
		10 0 1 2 3 4 5 6 7 8 9
		10
		0 0 0
		0 0 0.55555555560000003
		0 0 1.111111111
		0 0 1.6666666670000001
		0 0 2.2222222220000001
		0 0 2.7777777779999999
		0 0 3.3333333330000001
		0 0 3.888888889
		0 0 4.4444444440000002
		0 0 5
		;
createNode transform -n "Hand4" -p "hairSystem1Follicles";
	rename -uid "820686E5-45F8-8B7E-A057-45922AF9B29D";
createNode follicle -n "HandShape4" -p "Hand4";
	rename -uid "D0B0FC32-4A85-1EE1-6CEF-19BD3680AB35";
	setAttr -k off ".v";
	setAttr ".pu" 1;
	setAttr ".pv" 0.5;
	setAttr -s 2 ".sts[0:1]"  0 1 3 1 0.2 3;
	setAttr -s 2 ".cws[0:1]"  0 1 3 1 0.2 3;
	setAttr -s 2 ".ats[0:1]"  0 1 3 1 0.2 3;
createNode transform -n "curve4" -p "Hand4";
	rename -uid "B831AB14-4341-96A1-DF44-4CB6F19C57C0";
createNode nurbsCurve -n "curveShape4" -p "curve4";
	rename -uid "4FE5B04A-4B28-B696-5EE2-72AE906AD8D3";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 9 0 no 3
		10 0 1 2 3 4 5 6 7 8 9
		10
		0 0 0
		0 0 0.55555555560000003
		0 0 1.111111111
		0 0 1.6666666670000001
		0 0 2.2222222220000001
		0 0 2.7777777779999999
		0 0 3.3333333330000001
		0 0 3.888888889
		0 0 4.4444444440000002
		0 0 5
		;
createNode transform -n "Hand5" -p "hairSystem1Follicles";
	rename -uid "3F63BF43-45E7-C8C4-2466-C7995F25B967";
createNode follicle -n "HandShape5" -p "Hand5";
	rename -uid "A78F022D-43F2-0704-9145-6985736CFA04";
	setAttr -k off ".v";
	setAttr ".pv" 0.5;
	setAttr -s 2 ".sts[0:1]"  0 1 3 1 0.2 3;
	setAttr -s 2 ".cws[0:1]"  0 1 3 1 0.2 3;
	setAttr -s 2 ".ats[0:1]"  0 1 3 1 0.2 3;
createNode transform -n "curve5" -p "Hand5";
	rename -uid "792BEB1E-488A-F796-F100-13B0B2C34996";
createNode nurbsCurve -n "curveShape5" -p "curve5";
	rename -uid "AE1708AF-48F1-25AE-E6B0-F4ACEC6D8326";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 9 0 no 3
		10 0 1 2 3 4 5 6 7 8 9
		10
		0 0 0
		0 0 0.55555555560000003
		0 0 1.111111111
		0 0 1.6666666670000001
		0 0 2.2222222220000001
		0 0 2.7777777779999999
		0 0 3.3333333330000001
		0 0 3.888888889
		0 0 4.4444444440000002
		0 0 5
		;
createNode transform -n "Hand6" -p "hairSystem1Follicles";
	rename -uid "FE1848EF-4345-92D4-D263-879FE01CA3EA";
createNode follicle -n "HandShape6" -p "Hand6";
	rename -uid "97974299-4CDF-8015-B12A-73A4F5EBCEC8";
	setAttr -k off ".v";
	setAttr ".pu" 0.33333333333333331;
	setAttr ".pv" 0.5;
	setAttr -s 2 ".sts[0:1]"  0 1 3 1 0.2 3;
	setAttr -s 2 ".cws[0:1]"  0 1 3 1 0.2 3;
	setAttr -s 2 ".ats[0:1]"  0 1 3 1 0.2 3;
createNode transform -n "curve6" -p "Hand6";
	rename -uid "33BE3857-454E-3362-4E74-A2A285DC9012";
createNode nurbsCurve -n "curveShape6" -p "curve6";
	rename -uid "6B4AD4A2-43C0-7260-2A86-ABB7CD158A30";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 9 0 no 3
		10 0 1 2 3 4 5 6 7 8 9
		10
		0 0 0
		0 0 0.55555555560000003
		0 0 1.111111111
		0 0 1.6666666670000001
		0 0 2.2222222220000001
		0 0 2.7777777779999999
		0 0 3.3333333330000001
		0 0 3.888888889
		0 0 4.4444444440000002
		0 0 5
		;
createNode transform -n "Hand7" -p "hairSystem1Follicles";
	rename -uid "19301B7E-4190-534C-5DAF-E999A6774447";
createNode follicle -n "HandShape7" -p "Hand7";
	rename -uid "89C2799D-412B-F945-4B93-4E8FDAFE2FBE";
	setAttr -k off ".v";
	setAttr ".pu" 0.66666666666666663;
	setAttr ".pv" 0.5;
	setAttr -s 2 ".sts[0:1]"  0 1 3 1 0.2 3;
	setAttr -s 2 ".cws[0:1]"  0 1 3 1 0.2 3;
	setAttr -s 2 ".ats[0:1]"  0 1 3 1 0.2 3;
createNode transform -n "curve7" -p "Hand7";
	rename -uid "5AABBDCF-4F5C-1F36-60DF-648CFA8A8A00";
createNode nurbsCurve -n "curveShape7" -p "curve7";
	rename -uid "DC026B28-4267-FCEB-8791-6F86D8C32642";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 9 0 no 3
		10 0 1 2 3 4 5 6 7 8 9
		10
		0 0 0
		0 0 0.55555555560000003
		0 0 1.111111111
		0 0 1.6666666670000001
		0 0 2.2222222220000001
		0 0 2.7777777779999999
		0 0 3.3333333330000001
		0 0 3.888888889
		0 0 4.4444444440000002
		0 0 5
		;
createNode transform -n "Hand8" -p "hairSystem1Follicles";
	rename -uid "5F566603-4596-AE86-A585-CE80176B77FF";
createNode follicle -n "HandShape8" -p "Hand8";
	rename -uid "4789EC3B-4B2E-AB67-33D9-3BA4416B2564";
	setAttr -k off ".v";
	setAttr ".pu" 1;
	setAttr ".pv" 0.5;
	setAttr -s 2 ".sts[0:1]"  0 1 3 1 0.2 3;
	setAttr -s 2 ".cws[0:1]"  0 1 3 1 0.2 3;
	setAttr -s 2 ".ats[0:1]"  0 1 3 1 0.2 3;
createNode transform -n "curve8" -p "Hand8";
	rename -uid "38CF8557-4F12-82F9-1809-91B290468663";
createNode nurbsCurve -n "curveShape8" -p "curve8";
	rename -uid "376A1386-42FD-ED5D-5DE9-96BC98C694B0";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 9 0 no 3
		10 0 1 2 3 4 5 6 7 8 9
		10
		0 0 0
		0 0 0.55555555560000003
		0 0 1.111111111
		0 0 1.6666666670000001
		0 0 2.2222222220000001
		0 0 2.7777777779999999
		0 0 3.3333333330000001
		0 0 3.888888889
		0 0 4.4444444440000002
		0 0 5
		;
createNode joint -n "joint24_jnt";
	rename -uid "E9280C53-4B7C-C26E-80CB-00AEB2C85DB3";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".v" no;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 4 0 -1.0000000000000002 1;
createNode pointConstraint -n "joint24_jnt_pointConstraint1" -p "joint24_jnt";
	rename -uid "B96A966A-4C06-ED9C-7956-598F053E3098";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "joint24W0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".rst" -type "double3" 4 0 -1.0000000000000002 ;
	setAttr -k on ".w0";
createNode aimConstraint -n "joint24_jnt_aimConstraint1" -p "joint24_jnt";
	rename -uid "82DB5698-4826-CF13-8DB5-00B82F33F34B";
	addAttr -dcb 0 -ci true -sn "w0" -ln "joint23_jntW0" -dv 1 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".o" -type "double3" 0 165.96375653207352 0 ;
	setAttr ".rsrr" -type "double3" 0 360 0 ;
	setAttr -k on ".w0";
createNode joint -n "joint23_jnt";
	rename -uid "DF62C2E9-4829-1D81-2DA5-A2988E393954";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".v" no;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
createNode pointConstraint -n "joint23_jnt_pointConstraint1" -p "joint23_jnt";
	rename -uid "0018ED25-44DF-B5AD-DFED-2894A662148E";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "joint23W0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr -k on ".w0";
createNode aimConstraint -n "joint23_jnt_aimConstraint1" -p "joint23_jnt";
	rename -uid "C07536FA-450F-832F-4C1B-64886FC15940";
	addAttr -dcb 0 -ci true -sn "w0" -ln "joint24_jntW0" -dv 1 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".o" -type "double3" 0 -14.036243467926484 0 ;
	setAttr -k on ".w0";
createNode transform -n "group1";
	rename -uid "A594C582-49F4-3194-F2AD-33A08C151B38";
createNode joint -n "curve1_jnt" -p "group1";
	rename -uid "BF8BD544-43D5-2DB0-12C0-73ABF0CD2545";
	setAttr ".v" no;
	setAttr ".dla" yes;
createNode parentConstraint -n "curve1_jnt_parentConstraint1" -p "curve1_jnt";
	rename -uid "BD2760D7-426C-BF6D-62A3-178DE71FA2CB";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "curve1W0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".tg[0].tor" -type "double3" 0 1.5902773407317584e-15 0 ;
	setAttr ".lr" -type "double3" 0 14.03624346792648 0 ;
	setAttr ".rsrr" -type "double3" 0 14.03624346792648 0 ;
	setAttr -k on ".w0";
createNode orientConstraint -n "curve1_jnt_orientConstraint1" -p "curve1_jnt";
	rename -uid "4BCC4B98-4C66-7F43-7306-33B211CE2A9C";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "curve1W0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".lr" -type "double3" 0 14.03624346792648 0 ;
	setAttr ".rsrr" -type "double3" 0 14.03624346792648 0 ;
	setAttr -k on ".w0";
createNode joint -n "curve2_jnt" -p "group1";
	rename -uid "B859102F-4475-4809-4237-F5905B97917D";
	setAttr ".v" no;
	setAttr ".dla" yes;
createNode parentConstraint -n "curve2_jnt_parentConstraint1" -p "curve2_jnt";
	rename -uid "959C96BC-4406-1A92-14D9-DBA97C4CF5AC";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "curve2W0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".tg[0].tot" -type "double3" 0 0 -1.8503722591624124e-17 ;
	setAttr ".tg[0].tor" -type "double3" 0 -1.5902773407317584e-15 0 ;
	setAttr ".lr" -type "double3" 0 14.036243467926486 0 ;
	setAttr ".rst" -type "double3" 1.3333333730697685 0 -0.33333334326744213 ;
	setAttr ".rsrr" -type "double3" 0 14.036243467926486 0 ;
	setAttr -k on ".w0";
createNode orientConstraint -n "curve2_jnt_orientConstraint1" -p "curve2_jnt";
	rename -uid "CB9B7761-43C0-994E-3B49-A8BF2CC19D95";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "curve2W0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".lr" -type "double3" 0 14.03624346792648 0 ;
	setAttr ".rsrr" -type "double3" 0 14.036243467926486 0 ;
	setAttr -k on ".w0";
createNode joint -n "curve3_jnt" -p "group1";
	rename -uid "13F7B48E-4B63-49A1-2280-2CA8278002A9";
	setAttr ".v" no;
	setAttr ".dla" yes;
createNode parentConstraint -n "curve3_jnt_parentConstraint1" -p "curve3_jnt";
	rename -uid "B6210309-42AA-F814-C32B-CDB85B96A28A";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "curve3W0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".tg[0].tor" -type "double3" 0 1.5902773407317584e-15 0 ;
	setAttr ".lr" -type "double3" 0 14.03624346792648 0 ;
	setAttr ".rst" -type "double3" 2.6666667461395366 0 -0.66666668653488426 ;
	setAttr ".rsrr" -type "double3" 0 14.03624346792648 0 ;
	setAttr -k on ".w0";
createNode orientConstraint -n "curve3_jnt_orientConstraint1" -p "curve3_jnt";
	rename -uid "43009C5F-4D52-FFEC-7DD6-E5BC642027E0";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "curve3W0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".lr" -type "double3" 0 14.03624346792648 0 ;
	setAttr ".rsrr" -type "double3" 0 14.03624346792648 0 ;
	setAttr -k on ".w0";
createNode joint -n "curve4_jnt" -p "group1";
	rename -uid "B89AE4F1-43C4-2E87-A5D8-CA9B3CA6CF1E";
	setAttr ".v" no;
createNode parentConstraint -n "curve4_jnt_parentConstraint1" -p "curve4_jnt";
	rename -uid "4AC98D41-4393-79CD-F7F2-94BE6B921967";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "curve4W0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".tg[0].tot" -type "double3" 0 0 -3.7470892997998061e-30 ;
	setAttr ".tg[0].tor" -type "double3" 0 -1.5902773407317584e-15 0 ;
	setAttr ".lr" -type "double3" 0 14.036243467926493 0 ;
	setAttr ".rst" -type "double3" 4.0000000000000195 0 -1.0000000000000051 ;
	setAttr ".rsrr" -type "double3" 0 14.036243467926493 0 ;
	setAttr -k on ".w0";
createNode orientConstraint -n "curve4_jnt_orientConstraint1" -p "curve4_jnt";
	rename -uid "708FC786-436D-753B-D2B8-ACA71314C525";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "curve4W0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".lr" -type "double3" 42.20673458741404 10.491234550145952 9.3774657151701923 ;
	setAttr ".rsrr" -type "double3" 0 14.036243467926493 0 ;
	setAttr -k on ".w0" 0;
createNode joint -n "curve5_jnt" -p "group1";
	rename -uid "FE5F7774-45D1-6C4B-5D2F-AB9FE4F2868B";
	setAttr ".v" no;
	setAttr ".jo" -type "double3" 2.0950126797879599e-16 1.5902773407317584e-15 -1.7018014598884889e-15 ;
createNode parentConstraint -n "curve5_jnt_parentConstraint1" -p "curve5_jnt";
	rename -uid "C9CF3E7F-48A2-FF03-BE71-7F88414E36DE";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "curve5W0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".tg[0].tot" -type "double3" 0 0 2.2204460492503131e-16 ;
	setAttr ".tg[0].tor" -type "double3" 1.4124500153760508e-30 1.5902773407317584e-15 
		0 ;
	setAttr ".lr" -type "double3" 180 -14.036239128748287 0 ;
	setAttr ".rst" -type "double3" 4.0000000000000471 -2.7192621468937821e-32 -1.0000000000000122 ;
	setAttr ".rsrr" -type "double3" 180 -14.036239128748287 0 ;
	setAttr -k on ".w0";
createNode orientConstraint -n "curve5_jnt_orientConstraint1" -p "curve5_jnt";
	rename -uid "C2345EFD-405B-8D04-A4DE-EC859D979562";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "curve5W0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".lr" -type "double3" 180 -14.036239128748273 0 ;
	setAttr ".rsrr" -type "double3" 180 -14.036239128748287 0 ;
	setAttr -k on ".w0";
createNode joint -n "curve6_jnt" -p "group1";
	rename -uid "1F43099B-4A89-3C88-87C0-EB8D7A3BBA43";
	setAttr ".v" no;
	setAttr ".dla" yes;
	setAttr ".jo" -type "double3" 2.0950143982211324e-16 -7.9513867036587919e-16 -1.7018021472618411e-15 ;
createNode parentConstraint -n "curve6_jnt_parentConstraint1" -p "curve6_jnt";
	rename -uid "747AB0F3-4E07-AC10-8E17-EA9F07984895";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "curve6W0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".tg[0].tor" -type "double3" 0 1.5902773407317584e-15 -3.5311250384401269e-31 ;
	setAttr ".lr" -type "double3" 180 -14.036244914320324 -1.8199002003295261e-31 ;
	setAttr ".rst" -type "double3" 5.3333334922790847 0 -0.66666668653488703 ;
	setAttr ".rsrr" -type "double3" 180 -14.036244914320324 -1.8199002003295261e-31 ;
	setAttr -k on ".w0";
createNode orientConstraint -n "curve6_jnt_orientConstraint1" -p "curve6_jnt";
	rename -uid "4C646D61-405F-4D1C-99D4-498C59E3C83D";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "curve6W0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".lr" -type "double3" 180 -14.036244914320324 -1.8199002003295261e-31 ;
	setAttr ".rsrr" -type "double3" 180 -14.036244914320324 -1.8199002003295261e-31 ;
	setAttr -k on ".w0";
createNode joint -n "curve7_jnt" -p "group1";
	rename -uid "70F8D4EB-4240-26CE-84DA-3B96CD69129A";
	setAttr ".v" no;
	setAttr ".dla" yes;
	setAttr ".jo" -type "double3" 2.0950146130251465e-16 7.9513867036587899e-16 -1.701802233183428e-15 ;
createNode parentConstraint -n "curve7_jnt_parentConstraint1" -p "curve7_jnt";
	rename -uid "809CD94D-4B85-30C8-6DD2-7EAEE006E1A2";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "curve7W0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".tg[0].tot" -type "double3" -8.8817841970012523e-16 -4.9303806576313238e-32 
		2.2204460492503131e-16 ;
	setAttr ".tg[0].tor" -type "double3" -1.4124500153760508e-30 -1.590277340731758e-15 
		-3.5311250384401265e-31 ;
	setAttr ".lr" -type "double3" 180 -14.036245637516153 0 ;
	setAttr ".rst" -type "double3" 6.6666665077209633 2.2111185107375417e-32 -0.33333334326744019 ;
	setAttr ".rsrr" -type "double3" 180 -14.036245637516153 0 ;
	setAttr -k on ".w0";
createNode orientConstraint -n "curve7_jnt_orientConstraint1" -p "curve7_jnt";
	rename -uid "671FAE72-473F-12D1-A3CD-17BA93E67B26";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "curve7W0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".lr" -type "double3" 180 -14.036245637516153 0 ;
	setAttr ".rsrr" -type "double3" 180 -14.036245637516153 0 ;
	setAttr -k on ".w0";
createNode joint -n "curve8_jnt" -p "group1";
	rename -uid "33F9FCDF-41BF-07D5-87AA-2DAC989D358C";
	setAttr ".v" no;
	setAttr ".jo" -type "double3" -2.0950131093961436e-16 0 1.7018016317318113e-15 ;
createNode parentConstraint -n "curve8_jnt_parentConstraint1" -p "curve8_jnt";
	rename -uid "0E9BEA9F-4F35-ECDE-6A08-0D85EE1C0FCF";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "curve8W0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".tg[0].tor" -type "double3" 1.4124500153760508e-30 0 3.5311250384401269e-31 ;
	setAttr ".lr" -type "double3" 180 -14.036240575141141 1.8199001658729196e-31 ;
	setAttr ".rst" -type "double3" 8.0000000000000391 0 -2.7755575615629052e-16 ;
	setAttr ".rsrr" -type "double3" 180 -14.036240575141141 1.8199001658729196e-31 ;
	setAttr -k on ".w0";
createNode orientConstraint -n "curve8_jnt_orientConstraint1" -p "curve8_jnt";
	rename -uid "21F4915F-47C5-4618-C52B-A2A86590F3F2";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "curve8W0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".lr" -type "double3" 180 -14.036240575141143 1.8199001658729196e-31 ;
	setAttr ".rsrr" -type "double3" 180 -14.036240575141141 1.8199001658729196e-31 ;
	setAttr -k on ".w0";
createNode transform -n "group2" -p "group1";
	rename -uid "9FEC1AC7-4162-A6BC-E3AB-A0AD3C36384C";
	setAttr ".v" no;
createNode joint -n "curve1_jnt1" -p "group2";
	rename -uid "7584C79D-4867-9A8F-75C7-3FA1BE5F74E4";
	setAttr ".dla" yes;
createNode parentConstraint -n "curve1_jnt1_parentConstraint1" -p "curve1_jnt1";
	rename -uid "680AD312-4806-91BA-49D2-B5A32AD69635";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "curve1_jntW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v" no;
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".lr" -type "double3" 0 14.036243438720703 0 ;
	setAttr ".rsrr" -type "double3" 0 14.036243438720703 0 ;
	setAttr -k on ".w0";
createNode joint -n "curve2_jnt1" -p "group2";
	rename -uid "24ECE51A-47F6-0F53-6D4F-D1989256D97E";
	setAttr ".dla" yes;
createNode parentConstraint -n "curve2_jnt1_parentConstraint1" -p "curve2_jnt1";
	rename -uid "D09218DB-42E1-7308-4A1F-90A1CD815DF5";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "curve2_jntW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v" no;
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".tg[0].tot" -type "double3" 0 0 2.0878511187763339e-17 ;
	setAttr ".lr" -type "double3" 0 14.036243438720703 0 ;
	setAttr ".rst" -type "double3" 1.3333333730697685 0 -0.33333334326744213 ;
	setAttr ".rsrr" -type "double3" 0 14.036243438720703 0 ;
	setAttr -k on ".w0";
createNode joint -n "curve3_jnt1" -p "group2";
	rename -uid "B3EE0267-42BB-83ED-0EA7-B9B09E7876BB";
	setAttr ".dla" yes;
createNode parentConstraint -n "curve3_jnt1_parentConstraint1" -p "curve3_jnt1";
	rename -uid "A703DDFB-4B70-87CA-8597-0F8800DE6BED";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "curve3_jntW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v" no;
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".tg[0].tot" -type "double3" 0 0 4.749590427169761e-18 ;
	setAttr ".lr" -type "double3" 0 14.036243438720703 0 ;
	setAttr ".rst" -type "double3" 2.6666667461395366 0 -0.66666668653488426 ;
	setAttr ".rsrr" -type "double3" 0 14.036243438720703 0 ;
	setAttr -k on ".w0";
createNode joint -n "curve4_jnt1" -p "group2";
	rename -uid "1C8E9A55-4EB0-7500-BDAB-C0852B7F74CA";
	setAttr ".v" no;
	setAttr ".dla" yes;
createNode parentConstraint -n "curve4_jnt1_parentConstraint1" -p "curve4_jnt1";
	rename -uid "B2CE559B-418B-C04E-65D0-F98DF6AB6152";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "curve4_jntW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v" no;
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".tg[0].tot" -type "double3" 0 0 1.075334796318936e-23 ;
	setAttr ".lr" -type "double3" 0 14.036243438720703 0 ;
	setAttr ".rst" -type "double3" 4.0000000000000195 0 -1.0000000000000051 ;
	setAttr ".rsrr" -type "double3" 0 14.036243438720703 0 ;
	setAttr -k on ".w0";
createNode joint -n "curve5_jnt1" -p "group2";
	rename -uid "304F9E34-4259-51FA-6941-F0B7F59CADEE";
	setAttr ".dla" yes;
createNode parentConstraint -n "curve5_jnt1_parentConstraint1" -p "curve5_jnt1";
	rename -uid "4FFCE36A-4006-1991-AC2F-7D97C5F167FF";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "curve5_jntW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v" no;
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".tg[0].tot" -type "double3" 4.4408920985006262e-16 -2.2204460492503131e-16 
		-1.1102230246251565e-16 ;
	setAttr ".lr" -type "double3" 180 -14.036238670349125 0 ;
	setAttr ".rst" -type "double3" 4.000000000000048 3.6972927779961167e-17 -1.0000000000000124 ;
	setAttr ".rsrr" -type "double3" 72.000000000000014 -14.036238670349121 -8.196101640757175e-16 ;
	setAttr -k on ".w0";
createNode joint -n "curve6_jnt1" -p "group2";
	rename -uid "76442B0E-440B-1E6A-0C75-98B9ACB3D41A";
	setAttr ".dla" yes;
createNode parentConstraint -n "curve6_jnt1_parentConstraint1" -p "curve6_jnt1";
	rename -uid "8D5766C2-4E5B-35DC-F235-D58992DFC109";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "curve6_jntW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v" no;
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".tg[0].tot" -type "double3" 0 0 2.2204460492503131e-16 ;
	setAttr ".lr" -type "double3" 180 -14.036245346069336 0 ;
	setAttr ".rst" -type "double3" 5.3333334922790847 0 -0.66666668653488681 ;
	setAttr ".rsrr" -type "double3" 0 -14.036245346069336 0 ;
	setAttr -k on ".w0";
createNode joint -n "curve7_jnt1" -p "group2";
	rename -uid "A094CF70-4B59-2912-84DB-5F959302C67F";
	setAttr ".dla" yes;
createNode parentConstraint -n "curve7_jnt1_parentConstraint1" -p "curve7_jnt1";
	rename -uid "87F10E02-48C6-D6F5-9115-F29209B3165D";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "curve7_jntW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v" no;
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".lr" -type "double3" 180 -14.036245346069336 0 ;
	setAttr ".rst" -type "double3" 6.6666665077209633 -4.9303806576313238e-32 -0.33333334326743974 ;
	setAttr ".rsrr" -type "double3" 0 -14.036245346069336 0 ;
	setAttr -k on ".w0";
createNode joint -n "curve8_jnt1" -p "group2";
	rename -uid "F269BE6F-413A-A8AC-6647-B29FEA011CE3";
createNode parentConstraint -n "curve8_jnt1_parentConstraint1" -p "curve8_jnt1";
	rename -uid "4FBF169F-47F0-E0B9-86FA-F0A99B92FD28";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "curve8_jntW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v" no;
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".tg[0].tor" -type "double3" -1.4124500153760508e-30 1.5902773407317588e-15 
		3.5311250384401278e-31 ;
	setAttr ".lr" -type "double3" 180 -14.03624057769775 1.8199001658932207e-31 ;
	setAttr ".rst" -type "double3" 8.0000000000000391 0 -2.7755575615629052e-16 ;
	setAttr ".rsrr" -type "double3" 180 -14.03624057769775 1.8199001658932207e-31 ;
	setAttr -k on ".w0";
createNode transform -n "Wrist_grp";
	rename -uid "0B3787E0-4D11-42FC-9B18-C79D9708DC0D";
	setAttr ".t" -type "double3" 8 0 -2.2204460492503131e-16 ;
createNode transform -n "Wrist_Ctrl" -p "Wrist_grp";
	rename -uid "01455F85-47AA-6D56-D4DE-BDA679ECC24B";
	setAttr ".t" -type "double3" -0.33559892243718981 2.3957073158722242 1.1708652419602199 ;
createNode nurbsCurve -n "curveShape9" -p "Wrist_Ctrl";
	rename -uid "65068664-4CDD-46FA-B149-E5B17499C32D";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".cc" -type "nurbsCurve" 
		1 15 0 no 3
		16 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
		16
		0.32925246982855133 0.32925246982855133 0.32925246982855133
		0.32925246982855133 0.32925246982855133 -0.32925246982855133
		0.32925246982855133 -0.32925246982855133 -0.32925246982855133
		0.32925246982855133 -0.32925246982855133 0.32925246982855133
		-0.32925246982855133 -0.32925246982855133 0.32925246982855133
		-0.32925246982855133 0.32925246982855133 0.32925246982855133
		0.32925246982855133 0.32925246982855133 0.32925246982855133
		0.32925246982855133 -0.32925246982855133 0.32925246982855133
		-0.32925246982855133 -0.32925246982855133 0.32925246982855133
		-0.32925246982855133 -0.32925246982855133 -0.32925246982855133
		-0.32925246982855133 0.32925246982855133 -0.32925246982855133
		0.32925246982855133 0.32925246982855133 -0.32925246982855133
		0.32925246982855133 -0.32925246982855133 -0.32925246982855133
		-0.32925246982855133 -0.32925246982855133 -0.32925246982855133
		-0.32925246982855133 0.32925246982855133 -0.32925246982855133
		-0.32925246982855133 0.32925246982855133 0.32925246982855133
		;
createNode ikHandle -n "ikHandle_Hand" -p "Wrist_Ctrl";
	rename -uid "756A5195-446B-EAC8-D71D-A0853049641A";
	setAttr ".v" no;
	setAttr ".roc" yes;
createNode poleVectorConstraint -n "ikHandle_Hand_poleVectorConstraint1" -p "ikHandle_Hand";
	rename -uid "5CB783C3-416C-0179-A0FE-D182827A7F8F";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "Elbow_CtrlW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".rst" -type "double3" 4 0 -4.9437704552412463 ;
	setAttr -k on ".w0";
createNode transform -n "locator1";
	rename -uid "617A6997-4121-0044-D58C-EBBB03D0EBA5";
	setAttr ".v" no;
createNode locator -n "locatorShape1" -p "locator1";
	rename -uid "E9805E37-4D91-4E5C-D449-568B8C751BA1";
	setAttr -k off ".v";
createNode pointConstraint -n "locator1_pointConstraint1" -p "locator1";
	rename -uid "BDB8C268-43B3-7BDF-06D1-078FA8CBC33E";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "ShoulderW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr -k on ".w0";
createNode transform -n "locator2";
	rename -uid "FF4B7662-40D0-32D9-3D82-BFAE64C6E53D";
	setAttr ".v" no;
createNode locator -n "locatorShape2" -p "locator2";
	rename -uid "DF66FAA3-47B8-5DF8-2585-FC9F6BDD73C8";
	setAttr -k off ".v";
createNode pointConstraint -n "locator2_pointConstraint1" -p "locator2";
	rename -uid "26E749C8-4E13-BA4B-C219-B3B26BA372BB";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "Wrist_CtrlW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".rst" -type "double3" 8 0 -2.2204460492503131e-16 ;
	setAttr -k on ".w0";
createNode transform -n "distanceDimension1";
	rename -uid "8D7277EC-41B9-E66F-BE70-179C08FDFECB";
	setAttr ".v" no;
createNode distanceDimShape -n "distanceDimensionShape1" -p "distanceDimension1";
	rename -uid "AC48FE5C-4AC1-3E1D-1517-029F4501D6F0";
	setAttr -k off ".v";
createNode transform -n "Elbow_grp";
	rename -uid "6D36D25D-4ED2-E0F8-4C2E-8B9AA1CA6FD4";
createNode transform -n "Elbow_Ctrl" -p "Elbow_grp";
	rename -uid "863CE8A1-405E-7B65-F2F3-6DA9A3F1FBB6";
createNode nurbsCurve -n "curveShape10" -p "Elbow_Ctrl";
	rename -uid "FB86916B-4D2A-474E-9BA5-9497316FCA17";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 14;
	setAttr ".cc" -type "nurbsCurve" 
		1 52 0 no 3
		53 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52
		53
		0 0.30320196066835575 0
		0 0.27894580381488732 0.11521674505397518
		0 0.21527339207453258 0.21527339207453258
		0 0.11521674505397518 0.27894580381488732
		0 0 0.30320196066835575
		0 -0.11521674505397518 0.27894580381488732
		0 -0.21527339207453258 0.21527339207453258
		0 -0.27894580381488732 0.11521674505397518
		0 -0.30320196066835575 0
		0 -0.27894580381488732 -0.11521674505397518
		0 -0.21527339207453258 -0.21527339207453258
		0 -0.11521674505397518 -0.27894580381488732
		0 0 -0.30320196066835575
		0 0.11521674505397518 -0.27894580381488732
		0 0.21527339207453258 -0.21527339207453258
		0 0.27894580381488732 -0.11521674505397518
		0 0.30320196066835575 0
		0.11521674505397518 0.27894580381488732 0
		0.21527339207453258 0.21527339207453258 0
		0.27894580381488732 0.11521674505397518 0
		0.30320196066835575 0 0
		0.27894580381488732 -0.11521674505397518 0
		0.21527339207453258 -0.21527339207453258 0
		0.11521674505397518 -0.27894580381488732 0
		0 -0.30320196066835575 0
		-0.11521674505397518 -0.27894580381488732 0
		-0.21527339207453258 -0.21527339207453258 0
		-0.27894580381488732 -0.11521674505397518 0
		-0.30320196066835575 0 0
		-0.27894580381488732 0.11521674505397518 0
		-0.21527339207453258 0.21527339207453258 0
		-0.11521674505397518 0.27894580381488732 0
		0 0.30320196066835575 0
		0 0.27894580381488732 -0.11521674505397518
		0 0.21527339207453258 -0.21527339207453258
		0 0.11521674505397518 -0.27894580381488732
		0 0 -0.30320196066835575
		-0.11521674505397518 0 -0.27894580381488732
		-0.21527339207453258 0 -0.21527339207453258
		-0.27894580381488732 0 -0.11521674505397518
		-0.30320196066835575 0 0
		-0.27894580381488732 0 0.11521674505397518
		-0.21527339207453258 0 0.21527339207453258
		-0.11521674505397518 0 0.27894580381488732
		0 0 0.30320196066835575
		0.11521674505397518 0 0.27894580381488732
		0.21527339207453258 0 0.21527339207453258
		0.27894580381488732 0 0.11521674505397518
		0.30320196066835575 0 0
		0.27894580381488732 0 -0.11521674505397518
		0.21527339207453258 0 -0.21527339207453258
		0.11521674505397518 0 -0.27894580381488732
		0 0 -0.30320196066835575
		;
createNode parentConstraint -n "Elbow_grp_parentConstraint1" -p "Elbow_grp";
	rename -uid "B4FFDFA2-4EAE-62A7-218B-8EB0A491DB36";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "Wrist_CtrlW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".tg[0].tot" -type "double3" -4 0 -4.9437704552412463 ;
	setAttr ".rst" -type "double3" 4 0 -4.9437704552412463 ;
	setAttr -k on ".w0";
createNode joint -n "joint25";
	rename -uid "84753B11-45E5-2231-4547-CDA06D688963";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".radi" 0.5;
createNode parentConstraint -n "joint25_parentConstraint1" -p "joint25";
	rename -uid "E3FB5DA5-47B8-1400-30B3-469B983CC536";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "ShoulderW0" -dv 1 -min 0 -at "double";
	addAttr -dcb 0 -ci true -k true -sn "w1" -ln "ElbowW1" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr -s 2 ".tg";
	setAttr ".lr" -type "double3" 0 4.8068470512608018e-15 0 ;
	setAttr ".rst" -type "double3" 2 0 -0.50000000000000011 ;
	setAttr ".rsrr" -type "double3" 0 4.8068470512608018e-15 0 ;
	setAttr -k on ".w0";
	setAttr -k on ".w1";
createNode aimConstraint -n "joint25_aimConstraint1" -p "joint25";
	rename -uid "31ABD569-463C-F16D-EC0F-69A15D06AC05";
	addAttr -dcb 0 -ci true -sn "w0" -ln "ElbowW0" -dv 1 -at "double";
	addAttr -dcb 0 -ci true -sn "w1" -ln "ShoulderW1" -dv 1 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr -s 2 ".tg";
	setAttr ".o" -type "double3" 0 14.258675726498252 0 ;
	setAttr ".rsrr" -type "double3" 0 14.258675726498256 0 ;
	setAttr -k on ".w0";
	setAttr -k on ".w1";
createNode joint -n "joint26";
	rename -uid "E15894AC-4159-B747-FB37-29B306E7446A";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".radi" 0.5;
createNode parentConstraint -n "joint26_parentConstraint1" -p "joint26";
	rename -uid "6FF5E8F8-471B-FE30-31D9-5AAB75A238A8";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "ElbowW0" -dv 1 -min 0 -at "double";
	addAttr -dcb 0 -ci true -k true -sn "w1" -ln "WristW1" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr -s 2 ".tg";
	setAttr ".lr" -type "double3" 0 -14.036243467926475 0 ;
	setAttr ".rst" -type "double3" 6 0 -0.50000000000000022 ;
	setAttr ".rsrr" -type "double3" 0 -14.036243467926475 0 ;
	setAttr -k on ".w0";
	setAttr -k on ".w1";
createNode aimConstraint -n "joint26_aimConstraint1" -p "joint26";
	rename -uid "EE7D34A7-4EBC-8BE2-453D-DDA87413C189";
	addAttr -dcb 0 -ci true -sn "w0" -ln "WristW0" -dv 1 -at "double";
	addAttr -dcb 0 -ci true -sn "w1" -ln "ElbowW1" -dv 1 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr -s 2 ".tg";
	setAttr ".o" -type "double3" 0 -14.191809624171039 0 ;
	setAttr ".rsrr" -type "double3" 0 -14.191809624171039 0 ;
	setAttr -k on ".w0";
	setAttr -k on ".w1";
createNode lightLinker -s -n "lightLinker1";
	rename -uid "5793E8FA-45AC-7F4E-EF67-209697FE0737";
	setAttr -s 2 ".lnk";
	setAttr -s 2 ".slnk";
createNode shapeEditorManager -n "shapeEditorManager";
	rename -uid "3DDF441F-423F-1FCF-1FBC-AD93AE8EE1F1";
createNode poseInterpolatorManager -n "poseInterpolatorManager";
	rename -uid "DCF4A5FE-4EA6-C3C5-462D-D4937B2C8656";
createNode displayLayerManager -n "layerManager";
	rename -uid "613C3F21-4FC5-1C3F-67FF-459765DF2CED";
createNode displayLayer -n "defaultLayer";
	rename -uid "6BA91A6A-4A35-FA0A-CA13-AFB596FE12DF";
createNode renderLayerManager -n "renderLayerManager";
	rename -uid "87AB7969-4115-FA5A-D699-5CAB9979626F";
createNode renderLayer -n "defaultRenderLayer";
	rename -uid "462B9C20-4332-CB05-DDCB-4082B2FC8414";
	setAttr ".g" yes;
createNode ikRPsolver -n "ikRPsolver";
	rename -uid "85249F01-49E0-33B6-9F44-D3BA887C60C3";
createNode tweak -n "tweak1";
	rename -uid "9178B5ED-431F-F374-5D64-23BCBB8634CB";
createNode objectSet -n "tweakSet1";
	rename -uid "C634D09A-4075-B64C-941F-3AB6FF0E81CB";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "groupId2";
	rename -uid "E0863393-435A-20BB-3AA1-588CEF84E331";
	setAttr ".ihi" 0;
createNode groupParts -n "groupParts2";
	rename -uid "DDA658ED-4933-3653-C17D-6EB552F1A2C4";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[*][*]";
createNode multiplyDivide -n "multiplyDivide1";
	rename -uid "0EFC0A4D-4F25-A8DD-4A0A-C1ADA2C0AB7F";
	setAttr ".op" 2;
	setAttr ".i2" -type "float3" 8.2460003 1 1 ;
createNode mute -n "aTools_StoreNode";
	rename -uid "303DEB0C-4245-7A54-6D5A-D1BBA19A3181";
createNode mute -n "scene";
	rename -uid "8FA05EC5-4C6F-B8D6-C2A0-ADA9BC5E8E18";
	addAttr -ci true -sn "id" -ln "id" -dt "string";
	setAttr ".id" -type "string" "1718260714.09";
createNode condition -n "condition1";
	rename -uid "B9021350-41BE-3287-A6B2-5C9CC44C5D29";
	setAttr ".op" 3;
	setAttr ".ft" 8.2460002899169922;
	setAttr ".ct" -type "float3" 8.2460003 1 1 ;
createNode script -n "uiConfigurationScriptNode";
	rename -uid "7DA7BDFC-4B76-06E4-C36E-1D82427DDB89";
	setAttr ".b" -type "string" (
		"// Maya Mel UI Configuration File.\n//\n//  This script is machine generated.  Edit at your own risk.\n//\n//\n\nglobal string $gMainPane;\nif (`paneLayout -exists $gMainPane`) {\n\n\tglobal int $gUseScenePanelConfig;\n\tint    $useSceneConfig = $gUseScenePanelConfig;\n\tint    $nodeEditorPanelVisible = stringArrayContains(\"nodeEditorPanel1\", `getPanel -vis`);\n\tint    $nodeEditorWorkspaceControlOpen = (`workspaceControl -exists nodeEditorPanel1Window` && `workspaceControl -q -visible nodeEditorPanel1Window`);\n\tint    $menusOkayInPanels = `optionVar -q allowMenusInPanels`;\n\tint    $nVisPanes = `paneLayout -q -nvp $gMainPane`;\n\tint    $nPanes = 0;\n\tstring $editorName;\n\tstring $panelName;\n\tstring $itemFilterName;\n\tstring $panelConfig;\n\n\t//\n\t//  get current state of the UI\n\t//\n\tsceneUIReplacement -update $gMainPane;\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Top View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Top View\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"top\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 32768\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n"
		+ "            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -controllers 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n"
		+ "            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 1\n            -height 1\n            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n"
		+ "\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Side View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Side View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"side\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n"
		+ "            -textureDisplay \"modulate\" \n            -textureMaxSize 32768\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n"
		+ "            -sortTransparent 1\n            -controllers 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 1\n            -height 1\n"
		+ "            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Front View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Front View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"front\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n"
		+ "            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 32768\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n"
		+ "            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -controllers 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n"
		+ "            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 1\n            -height 1\n            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Persp View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Persp View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"persp\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n"
		+ "            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 32768\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n"
		+ "            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -controllers 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n"
		+ "            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 1319\n            -height 637\n            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"outlinerPanel\" (localizedPanelLabel(\"ToggledOutliner\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\toutlinerPanel -edit -l (localizedPanelLabel(\"ToggledOutliner\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\t$editorName = $panelName;\n        outlinerEditor -e \n            -showShapes 0\n            -showAssignedMaterials 0\n            -showTimeEditor 1\n            -showReferenceNodes 1\n            -showReferenceMembers 1\n            -showAttributes 0\n            -showConnected 0\n            -showAnimCurvesOnly 0\n            -showMuteInfo 0\n            -organizeByLayer 1\n            -organizeByClip 1\n            -showAnimLayerWeight 1\n            -autoExpandLayers 1\n            -autoExpand 0\n            -autoExpandAnimatedShapes 1\n            -showDagOnly 1\n            -showAssets 1\n            -showContainedOnly 1\n            -showPublishedAsConnected 0\n            -showParentContainers 0\n            -showContainerContents 1\n            -ignoreDagHierarchy 0\n            -expandConnections 0\n            -showUpstreamCurves 1\n            -showUnitlessCurves 1\n            -showCompounds 1\n            -showLeafs 1\n            -showNumericAttrsOnly 0\n            -highlightActive 1\n            -autoSelectNewObjects 0\n            -doNotSelectNewObjects 0\n"
		+ "            -dropIsParent 1\n            -transmitFilters 0\n            -setFilter \"defaultSetFilter\" \n            -showSetMembers 1\n            -allowMultiSelection 1\n            -alwaysToggleSelect 0\n            -directSelect 0\n            -isSet 0\n            -isSetMember 0\n            -displayMode \"DAG\" \n            -expandObjects 0\n            -setsIgnoreFilters 1\n            -containersIgnoreFilters 0\n            -editAttrName 0\n            -showAttrValues 0\n            -highlightSecondary 0\n            -showUVAttrsOnly 0\n            -showTextureNodesOnly 0\n            -attrAlphaOrder \"default\" \n            -animLayerFilterOptions \"allAffecting\" \n            -sortOrder \"none\" \n            -longNames 0\n            -niceNames 1\n            -showNamespace 1\n            -showPinIcons 0\n            -mapMotionTrails 0\n            -ignoreHiddenAttribute 0\n            -ignoreOutlinerColor 0\n            -renderFilterVisible 0\n            -renderFilterIndex 0\n            -selectionOrder \"chronological\" \n            -expandAttribute 0\n"
		+ "            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"outlinerPanel\" (localizedPanelLabel(\"Outliner\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\toutlinerPanel -edit -l (localizedPanelLabel(\"Outliner\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        outlinerEditor -e \n            -showShapes 0\n            -showAssignedMaterials 0\n            -showTimeEditor 1\n            -showReferenceNodes 0\n            -showReferenceMembers 0\n            -showAttributes 0\n            -showConnected 0\n            -showAnimCurvesOnly 0\n            -showMuteInfo 0\n            -organizeByLayer 1\n            -organizeByClip 1\n            -showAnimLayerWeight 1\n            -autoExpandLayers 1\n            -autoExpand 0\n            -autoExpandAnimatedShapes 1\n            -showDagOnly 1\n            -showAssets 1\n            -showContainedOnly 1\n            -showPublishedAsConnected 0\n            -showParentContainers 0\n"
		+ "            -showContainerContents 1\n            -ignoreDagHierarchy 0\n            -expandConnections 0\n            -showUpstreamCurves 1\n            -showUnitlessCurves 1\n            -showCompounds 1\n            -showLeafs 1\n            -showNumericAttrsOnly 0\n            -highlightActive 1\n            -autoSelectNewObjects 0\n            -doNotSelectNewObjects 0\n            -dropIsParent 1\n            -transmitFilters 0\n            -setFilter \"defaultSetFilter\" \n            -showSetMembers 1\n            -allowMultiSelection 1\n            -alwaysToggleSelect 0\n            -directSelect 0\n            -displayMode \"DAG\" \n            -expandObjects 0\n            -setsIgnoreFilters 1\n            -containersIgnoreFilters 0\n            -editAttrName 0\n            -showAttrValues 0\n            -highlightSecondary 0\n            -showUVAttrsOnly 0\n            -showTextureNodesOnly 0\n            -attrAlphaOrder \"default\" \n            -animLayerFilterOptions \"allAffecting\" \n            -sortOrder \"none\" \n            -longNames 0\n"
		+ "            -niceNames 1\n            -showNamespace 1\n            -showPinIcons 0\n            -mapMotionTrails 0\n            -ignoreHiddenAttribute 0\n            -ignoreOutlinerColor 0\n            -renderFilterVisible 0\n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"graphEditor\" (localizedPanelLabel(\"Graph Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Graph Editor\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"OutlineEd\");\n            outlinerEditor -e \n                -showShapes 1\n                -showAssignedMaterials 0\n                -showTimeEditor 1\n                -showReferenceNodes 0\n                -showReferenceMembers 0\n                -showAttributes 1\n                -showConnected 1\n                -showAnimCurvesOnly 1\n                -showMuteInfo 0\n                -organizeByLayer 1\n                -organizeByClip 1\n"
		+ "                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n                -autoExpand 1\n                -autoExpandAnimatedShapes 1\n                -showDagOnly 0\n                -showAssets 1\n                -showContainedOnly 0\n                -showPublishedAsConnected 0\n                -showParentContainers 0\n                -showContainerContents 0\n                -ignoreDagHierarchy 0\n                -expandConnections 1\n                -showUpstreamCurves 1\n                -showUnitlessCurves 1\n                -showCompounds 0\n                -showLeafs 1\n                -showNumericAttrsOnly 1\n                -highlightActive 0\n                -autoSelectNewObjects 1\n                -doNotSelectNewObjects 0\n                -dropIsParent 1\n                -transmitFilters 1\n                -setFilter \"0\" \n                -showSetMembers 0\n                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n                -directSelect 0\n                -displayMode \"DAG\" \n                -expandObjects 0\n"
		+ "                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n                -showAttrValues 0\n                -highlightSecondary 0\n                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n                -animLayerFilterOptions \"allAffecting\" \n                -sortOrder \"none\" \n                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 1\n                -mapMotionTrails 1\n                -ignoreHiddenAttribute 0\n                -ignoreOutlinerColor 0\n                -renderFilterVisible 0\n                $editorName;\n\n\t\t\t$editorName = ($panelName+\"GraphEd\");\n            animCurveEditor -e \n                -displayValues 0\n                -snapTime \"integer\" \n                -snapValue \"none\" \n                -showPlayRangeShades \"on\" \n                -lockPlayRangeShades \"off\" \n                -smoothness \"fine\" \n                -resultSamples 1\n"
		+ "                -resultScreenSamples 0\n                -resultUpdate \"delayed\" \n                -showUpstreamCurves 1\n                -stackedCurvesMin -1\n                -stackedCurvesMax 1\n                -stackedCurvesSpace 0.2\n                -preSelectionHighlight 0\n                -constrainDrag 0\n                -valueLinesToggle 1\n                -highlightAffectedCurves 0\n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dopeSheetPanel\" (localizedPanelLabel(\"Dope Sheet\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Dope Sheet\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"OutlineEd\");\n            outlinerEditor -e \n                -showShapes 1\n                -showAssignedMaterials 0\n                -showTimeEditor 1\n                -showReferenceNodes 0\n                -showReferenceMembers 0\n                -showAttributes 1\n"
		+ "                -showConnected 1\n                -showAnimCurvesOnly 1\n                -showMuteInfo 0\n                -organizeByLayer 1\n                -organizeByClip 1\n                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n                -autoExpand 0\n                -autoExpandAnimatedShapes 1\n                -showDagOnly 0\n                -showAssets 1\n                -showContainedOnly 0\n                -showPublishedAsConnected 0\n                -showParentContainers 0\n                -showContainerContents 0\n                -ignoreDagHierarchy 0\n                -expandConnections 1\n                -showUpstreamCurves 1\n                -showUnitlessCurves 0\n                -showCompounds 1\n                -showLeafs 1\n                -showNumericAttrsOnly 1\n                -highlightActive 0\n                -autoSelectNewObjects 0\n                -doNotSelectNewObjects 1\n                -dropIsParent 1\n                -transmitFilters 0\n                -setFilter \"0\" \n                -showSetMembers 0\n"
		+ "                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n                -directSelect 0\n                -displayMode \"DAG\" \n                -expandObjects 0\n                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n                -showAttrValues 0\n                -highlightSecondary 0\n                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n                -animLayerFilterOptions \"allAffecting\" \n                -sortOrder \"none\" \n                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 0\n                -mapMotionTrails 1\n                -ignoreHiddenAttribute 0\n                -ignoreOutlinerColor 0\n                -renderFilterVisible 0\n                $editorName;\n\n\t\t\t$editorName = ($panelName+\"DopeSheetEd\");\n            dopeSheetEditor -e \n                -displayValues 0\n                -snapTime \"integer\" \n"
		+ "                -snapValue \"none\" \n                -outliner \"dopeSheetPanel1OutlineEd\" \n                -showSummary 1\n                -showScene 0\n                -hierarchyBelow 0\n                -showTicks 1\n                -selectionWindow 0 0 0 0 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"timeEditorPanel\" (localizedPanelLabel(\"Time Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Time Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"clipEditorPanel\" (localizedPanelLabel(\"Trax Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Trax Editor\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = clipEditorNameFromPanel($panelName);\n"
		+ "            clipEditor -e \n                -displayValues 0\n                -snapTime \"none\" \n                -snapValue \"none\" \n                -initialized 0\n                -manageSequencer 0 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"sequenceEditorPanel\" (localizedPanelLabel(\"Camera Sequencer\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Camera Sequencer\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = sequenceEditorNameFromPanel($panelName);\n            clipEditor -e \n                -displayValues 0\n                -snapTime \"none\" \n                -snapValue \"none\" \n                -initialized 0\n                -manageSequencer 1 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"hyperGraphPanel\" (localizedPanelLabel(\"Hypergraph Hierarchy\")) `;\n"
		+ "\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Hypergraph Hierarchy\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"HyperGraphEd\");\n            hyperGraph -e \n                -graphLayoutStyle \"hierarchicalLayout\" \n                -orientation \"horiz\" \n                -mergeConnections 0\n                -zoom 1\n                -animateTransition 0\n                -showRelationships 1\n                -showShapes 0\n                -showDeformers 0\n                -showExpressions 0\n                -showConstraints 0\n                -showConnectionFromSelected 0\n                -showConnectionToSelected 0\n                -showConstraintLabels 0\n                -showUnderworld 0\n                -showInvisible 0\n                -transitionFrames 1\n                -opaqueContainers 0\n                -freeform 0\n                -imagePosition 0 0 \n                -imageScale 1\n                -imageEnabled 0\n                -graphType \"DAG\" \n"
		+ "                -heatMapDisplay 0\n                -updateSelection 1\n                -updateNodeAdded 1\n                -useDrawOverrideColor 0\n                -limitGraphTraversal -1\n                -range 0 0 \n                -iconSize \"smallIcons\" \n                -showCachedConnections 0\n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"hyperShadePanel\" (localizedPanelLabel(\"Hypershade\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Hypershade\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"visorPanel\" (localizedPanelLabel(\"Visor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Visor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n"
		+ "\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"nodeEditorPanel\" (localizedPanelLabel(\"Node Editor\")) `;\n\tif ($nodeEditorPanelVisible || $nodeEditorWorkspaceControlOpen) {\n\t\tif (\"\" == $panelName) {\n\t\t\tif ($useSceneConfig) {\n\t\t\t\t$panelName = `scriptedPanel -unParent  -type \"nodeEditorPanel\" -l (localizedPanelLabel(\"Node Editor\")) -mbv $menusOkayInPanels `;\n\n\t\t\t$editorName = ($panelName+\"NodeEditorEd\");\n            nodeEditor -e \n                -allAttributes 0\n                -allNodes 0\n                -autoSizeNodes 1\n                -consistentNameSize 1\n                -createNodeCommand \"nodeEdCreateNodeCommand\" \n                -connectNodeOnCreation 0\n                -connectOnDrop 0\n                -copyConnectionsOnPaste 0\n                -connectionStyle \"bezier\" \n                -connectionMinSegment 0.03\n                -connectionOffset 0.03\n                -connectionRoundness 0.8\n                -connectionTension -100\n                -defaultPinnedState 0\n"
		+ "                -additiveGraphingMode 0\n                -settingsChangedCallback \"nodeEdSyncControls\" \n                -traversalDepthLimit -1\n                -keyPressCommand \"nodeEdKeyPressCommand\" \n                -nodeTitleMode \"name\" \n                -gridSnap 0\n                -gridVisibility 1\n                -crosshairOnEdgeDragging 0\n                -popupMenuScript \"nodeEdBuildPanelMenus\" \n                -showNamespace 1\n                -showShapes 1\n                -showSGShapes 0\n                -showTransforms 1\n                -useAssets 1\n                -syncedSelection 1\n                -extendToShapes 1\n                -editorMode \"default\" \n                -hasWatchpoint 0\n                $editorName;\n\t\t\t}\n\t\t} else {\n\t\t\t$label = `panel -q -label $panelName`;\n\t\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Node Editor\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"NodeEditorEd\");\n            nodeEditor -e \n                -allAttributes 0\n                -allNodes 0\n                -autoSizeNodes 1\n"
		+ "                -consistentNameSize 1\n                -createNodeCommand \"nodeEdCreateNodeCommand\" \n                -connectNodeOnCreation 0\n                -connectOnDrop 0\n                -copyConnectionsOnPaste 0\n                -connectionStyle \"bezier\" \n                -connectionMinSegment 0.03\n                -connectionOffset 0.03\n                -connectionRoundness 0.8\n                -connectionTension -100\n                -defaultPinnedState 0\n                -additiveGraphingMode 0\n                -settingsChangedCallback \"nodeEdSyncControls\" \n                -traversalDepthLimit -1\n                -keyPressCommand \"nodeEdKeyPressCommand\" \n                -nodeTitleMode \"name\" \n                -gridSnap 0\n                -gridVisibility 1\n                -crosshairOnEdgeDragging 0\n                -popupMenuScript \"nodeEdBuildPanelMenus\" \n                -showNamespace 1\n                -showShapes 1\n                -showSGShapes 0\n                -showTransforms 1\n                -useAssets 1\n                -syncedSelection 1\n"
		+ "                -extendToShapes 1\n                -editorMode \"default\" \n                -hasWatchpoint 0\n                $editorName;\n\t\t\tif (!$useSceneConfig) {\n\t\t\t\tpanel -e -l $label $panelName;\n\t\t\t}\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"createNodePanel\" (localizedPanelLabel(\"Create Node\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Create Node\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"polyTexturePlacementPanel\" (localizedPanelLabel(\"UV Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"UV Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"renderWindowPanel\" (localizedPanelLabel(\"Render View\")) `;\n"
		+ "\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Render View\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"shapePanel\" (localizedPanelLabel(\"Shape Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tshapePanel -edit -l (localizedPanelLabel(\"Shape Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"posePanel\" (localizedPanelLabel(\"Pose Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tposePanel -edit -l (localizedPanelLabel(\"Pose Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dynRelEdPanel\" (localizedPanelLabel(\"Dynamic Relationships\")) `;\n\tif (\"\" != $panelName) {\n"
		+ "\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Dynamic Relationships\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"relationshipPanel\" (localizedPanelLabel(\"Relationship Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Relationship Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"referenceEditorPanel\" (localizedPanelLabel(\"Reference Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Reference Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"componentEditorPanel\" (localizedPanelLabel(\"Component Editor\")) `;\n"
		+ "\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Component Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dynPaintScriptedPanelType\" (localizedPanelLabel(\"Paint Effects\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Paint Effects\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"scriptEditorPanel\" (localizedPanelLabel(\"Script Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Script Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"profilerPanel\" (localizedPanelLabel(\"Profiler Tool\")) `;\n"
		+ "\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Profiler Tool\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"contentBrowserPanel\" (localizedPanelLabel(\"Content Browser\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Content Browser\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\tif ($useSceneConfig) {\n        string $configName = `getPanel -cwl (localizedPanelLabel(\"Current Layout\"))`;\n        if (\"\" != $configName) {\n\t\t\tpanelConfiguration -edit -label (localizedPanelLabel(\"Current Layout\")) \n\t\t\t\t-userCreated false\n\t\t\t\t-defaultImage \"vacantCell.xP:/\"\n\t\t\t\t-image \"\"\n\t\t\t\t-sc false\n\t\t\t\t-configString \"global string $gMainPane; paneLayout -e -cn \\\"single\\\" -ps 1 100 100 $gMainPane;\"\n\t\t\t\t-removeAllPanels\n\t\t\t\t-ap false\n"
		+ "\t\t\t\t\t(localizedPanelLabel(\"Persp View\")) \n\t\t\t\t\t\"modelPanel\"\n"
		+ "\t\t\t\t\t\"$panelName = `modelPanel -unParent -l (localizedPanelLabel(\\\"Persp View\\\")) -mbv $menusOkayInPanels `;\\n$editorName = $panelName;\\nmodelEditor -e \\n    -cam `findStartUpCamera persp` \\n    -useInteractiveMode 0\\n    -displayLights \\\"default\\\" \\n    -displayAppearance \\\"smoothShaded\\\" \\n    -activeOnly 0\\n    -ignorePanZoom 0\\n    -wireframeOnShaded 0\\n    -headsUpDisplay 1\\n    -holdOuts 1\\n    -selectionHiliteDisplay 1\\n    -useDefaultMaterial 0\\n    -bufferMode \\\"double\\\" \\n    -twoSidedLighting 0\\n    -backfaceCulling 0\\n    -xray 0\\n    -jointXray 0\\n    -activeComponentsXray 0\\n    -displayTextures 0\\n    -smoothWireframe 0\\n    -lineWidth 1\\n    -textureAnisotropic 0\\n    -textureHilight 1\\n    -textureSampling 2\\n    -textureDisplay \\\"modulate\\\" \\n    -textureMaxSize 32768\\n    -fogging 0\\n    -fogSource \\\"fragment\\\" \\n    -fogMode \\\"linear\\\" \\n    -fogStart 0\\n    -fogEnd 100\\n    -fogDensity 0.1\\n    -fogColor 0.5 0.5 0.5 1 \\n    -depthOfFieldPreview 1\\n    -maxConstantTransparency 1\\n    -rendererName \\\"vp2Renderer\\\" \\n    -objectFilterShowInHUD 1\\n    -isFiltered 0\\n    -colorResolution 256 256 \\n    -bumpResolution 512 512 \\n    -textureCompression 0\\n    -transparencyAlgorithm \\\"frontAndBackCull\\\" \\n    -transpInShadows 0\\n    -cullingOverride \\\"none\\\" \\n    -lowQualityLighting 0\\n    -maximumNumHardwareLights 1\\n    -occlusionCulling 0\\n    -shadingModel 0\\n    -useBaseRenderer 0\\n    -useReducedRenderer 0\\n    -smallObjectCulling 0\\n    -smallObjectThreshold -1 \\n    -interactiveDisableShadows 0\\n    -interactiveBackFaceCull 0\\n    -sortTransparent 1\\n    -controllers 1\\n    -nurbsCurves 1\\n    -nurbsSurfaces 1\\n    -polymeshes 1\\n    -subdivSurfaces 1\\n    -planes 1\\n    -lights 1\\n    -cameras 1\\n    -controlVertices 1\\n    -hulls 1\\n    -grid 1\\n    -imagePlane 1\\n    -joints 1\\n    -ikHandles 1\\n    -deformers 1\\n    -dynamics 1\\n    -particleInstancers 1\\n    -fluids 1\\n    -hairSystems 1\\n    -follicles 1\\n    -nCloths 1\\n    -nParticles 1\\n    -nRigids 1\\n    -dynamicConstraints 1\\n    -locators 1\\n    -manipulators 1\\n    -pluginShapes 1\\n    -dimensions 1\\n    -handles 1\\n    -pivots 1\\n    -textures 1\\n    -strokes 1\\n    -motionTrails 1\\n    -clipGhosts 1\\n    -greasePencils 1\\n    -shadows 0\\n    -captureSequenceNumber -1\\n    -width 1319\\n    -height 637\\n    -sceneRenderFilter 0\\n    $editorName;\\nmodelEditor -e -viewSelected 0 $editorName;\\nmodelEditor -e \\n    -pluginObjects \\\"gpuCacheDisplayFilter\\\" 1 \\n    $editorName\"\n"
		+ "\t\t\t\t\t\"modelPanel -edit -l (localizedPanelLabel(\\\"Persp View\\\")) -mbv $menusOkayInPanels  $panelName;\\n$editorName = $panelName;\\nmodelEditor -e \\n    -cam `findStartUpCamera persp` \\n    -useInteractiveMode 0\\n    -displayLights \\\"default\\\" \\n    -displayAppearance \\\"smoothShaded\\\" \\n    -activeOnly 0\\n    -ignorePanZoom 0\\n    -wireframeOnShaded 0\\n    -headsUpDisplay 1\\n    -holdOuts 1\\n    -selectionHiliteDisplay 1\\n    -useDefaultMaterial 0\\n    -bufferMode \\\"double\\\" \\n    -twoSidedLighting 0\\n    -backfaceCulling 0\\n    -xray 0\\n    -jointXray 0\\n    -activeComponentsXray 0\\n    -displayTextures 0\\n    -smoothWireframe 0\\n    -lineWidth 1\\n    -textureAnisotropic 0\\n    -textureHilight 1\\n    -textureSampling 2\\n    -textureDisplay \\\"modulate\\\" \\n    -textureMaxSize 32768\\n    -fogging 0\\n    -fogSource \\\"fragment\\\" \\n    -fogMode \\\"linear\\\" \\n    -fogStart 0\\n    -fogEnd 100\\n    -fogDensity 0.1\\n    -fogColor 0.5 0.5 0.5 1 \\n    -depthOfFieldPreview 1\\n    -maxConstantTransparency 1\\n    -rendererName \\\"vp2Renderer\\\" \\n    -objectFilterShowInHUD 1\\n    -isFiltered 0\\n    -colorResolution 256 256 \\n    -bumpResolution 512 512 \\n    -textureCompression 0\\n    -transparencyAlgorithm \\\"frontAndBackCull\\\" \\n    -transpInShadows 0\\n    -cullingOverride \\\"none\\\" \\n    -lowQualityLighting 0\\n    -maximumNumHardwareLights 1\\n    -occlusionCulling 0\\n    -shadingModel 0\\n    -useBaseRenderer 0\\n    -useReducedRenderer 0\\n    -smallObjectCulling 0\\n    -smallObjectThreshold -1 \\n    -interactiveDisableShadows 0\\n    -interactiveBackFaceCull 0\\n    -sortTransparent 1\\n    -controllers 1\\n    -nurbsCurves 1\\n    -nurbsSurfaces 1\\n    -polymeshes 1\\n    -subdivSurfaces 1\\n    -planes 1\\n    -lights 1\\n    -cameras 1\\n    -controlVertices 1\\n    -hulls 1\\n    -grid 1\\n    -imagePlane 1\\n    -joints 1\\n    -ikHandles 1\\n    -deformers 1\\n    -dynamics 1\\n    -particleInstancers 1\\n    -fluids 1\\n    -hairSystems 1\\n    -follicles 1\\n    -nCloths 1\\n    -nParticles 1\\n    -nRigids 1\\n    -dynamicConstraints 1\\n    -locators 1\\n    -manipulators 1\\n    -pluginShapes 1\\n    -dimensions 1\\n    -handles 1\\n    -pivots 1\\n    -textures 1\\n    -strokes 1\\n    -motionTrails 1\\n    -clipGhosts 1\\n    -greasePencils 1\\n    -shadows 0\\n    -captureSequenceNumber -1\\n    -width 1319\\n    -height 637\\n    -sceneRenderFilter 0\\n    $editorName;\\nmodelEditor -e -viewSelected 0 $editorName;\\nmodelEditor -e \\n    -pluginObjects \\\"gpuCacheDisplayFilter\\\" 1 \\n    $editorName\"\n"
		+ "\t\t\t\t$configName;\n\n            setNamedPanelLayout (localizedPanelLabel(\"Current Layout\"));\n        }\n\n        panelHistory -e -clear mainPanelHistory;\n        sceneUIReplacement -clear;\n\t}\n\n\ngrid -spacing 5 -size 12 -divisions 5 -displayAxes yes -displayGridLines yes -displayDivisionLines yes -displayPerspectiveLabels no -displayOrthographicLabels no -displayAxesBold yes -perspectiveLabelPosition axis -orthographicLabelPosition edge;\nviewManip -drawCompass 0 -compassAngle 0 -frontParameters \"\" -homeParameters \"\" -selectionLockParameters \"\";\n}\n");
	setAttr ".st" 3;
createNode script -n "sceneConfigurationScriptNode";
	rename -uid "72864282-4E16-2684-C291-F9A3C5BE81D7";
	setAttr ".b" -type "string" "playbackOptions -min 1 -max 120 -ast 1 -aet 200 ";
	setAttr ".st" 6;
createNode blendColors -n "curve6_jnt_orientConstraint1_bc";
	rename -uid "50821E1F-4F6B-AEDE-EFEE-D8BE3A76E699";
createNode blendColors -n "curve3_jnt_orientConstraint1_bc";
	rename -uid "5B5230C2-4DE0-6701-7A3D-16B41ED18052";
createNode unitConversion -n "unitConversion2";
	rename -uid "CDF914E0-4BD2-4F36-F1E5-7BBEC1D1C076";
	setAttr ".cf" 57.295779513082323;
createNode unitConversion -n "unitConversion3";
	rename -uid "5066E570-4722-903C-E511-1381CC964AC6";
	setAttr ".cf" 57.295779513082323;
createNode unitConversion -n "unitConversion4";
	rename -uid "D32D6624-410D-05C6-BD7B-E0A4AE3A2E1B";
	setAttr ".cf" 57.295779513082323;
createNode blendColors -n "curve7_jnt_orientConstraint1_bc";
	rename -uid "F91D6243-4E6E-1305-1389-CDB2E22B26A0";
createNode unitConversion -n "unitConversion5";
	rename -uid "0B07266E-48CC-A5C0-5060-998091DBD50F";
	setAttr ".cf" 57.295779513082323;
createNode unitConversion -n "unitConversion6";
	rename -uid "8D24EE67-4A5B-FE48-E078-13AE564F8E46";
	setAttr ".cf" 57.295779513082323;
createNode unitConversion -n "unitConversion7";
	rename -uid "66BBFE3E-4E81-E7DE-C74B-FB878AFC0433";
	setAttr ".cf" 57.295779513082323;
createNode blendColors -n "curve8_jnt_orientConstraint1_bc";
	rename -uid "935BCC13-49AB-AA33-F016-818734D2BF69";
createNode unitConversion -n "unitConversion8";
	rename -uid "765BE7AB-4707-CA82-C3D4-F0AFEF2C1469";
	setAttr ".cf" 57.295779513082323;
createNode unitConversion -n "unitConversion9";
	rename -uid "01644D72-4FC1-F059-9984-04BDFCD107AC";
	setAttr ".cf" 57.295779513082323;
createNode unitConversion -n "unitConversion10";
	rename -uid "CE637908-4D2F-FE58-3DEC-339036BAE328";
	setAttr ".cf" 57.295779513082323;
createNode blendColors -n "curve5_jnt_orientConstraint1_bc";
	rename -uid "1D2F4DE4-4767-96DC-F11B-1FAED5AE29AA";
createNode unitConversion -n "unitConversion11";
	rename -uid "CC6C29E3-432F-731C-9228-5C8B8DD53968";
	setAttr ".cf" 57.295779513082323;
createNode unitConversion -n "unitConversion12";
	rename -uid "FA79D331-4328-592A-916E-DFAD1C6F5E7F";
	setAttr ".cf" 57.295779513082323;
createNode unitConversion -n "unitConversion13";
	rename -uid "DFCFD0B4-461A-00DD-610B-4DB081E6DFB8";
	setAttr ".cf" 57.295779513082323;
createNode blendColors -n "curve4_jnt_orientConstraint1_bc";
	rename -uid "CE02FB7A-4F4D-805C-B5F3-7DAF7D2F7CE9";
createNode unitConversion -n "unitConversion14";
	rename -uid "4EE07416-4546-6C30-7441-64BECD8D1FF0";
	setAttr ".cf" 57.295779513082323;
createNode unitConversion -n "unitConversion15";
	rename -uid "C59CDBA6-42B4-9137-EEDA-518C56FE5C50";
	setAttr ".cf" 57.295779513082323;
createNode unitConversion -n "unitConversion16";
	rename -uid "1C516F37-43D9-7DD4-24A4-70AED3806DE6";
	setAttr ".cf" 57.295779513082323;
createNode blendColors -n "curve2_jnt_orientConstraint1_bc";
	rename -uid "29BCD9F9-4270-C1F1-F93A-C8892AFCF7C8";
createNode unitConversion -n "unitConversion17";
	rename -uid "B1863C7C-4C0C-2024-2D7D-54BEE9908DB3";
	setAttr ".cf" 57.295779513082323;
createNode unitConversion -n "unitConversion18";
	rename -uid "0C01FE3E-4109-C132-1519-DA955C74A176";
	setAttr ".cf" 57.295779513082323;
createNode unitConversion -n "unitConversion19";
	rename -uid "85193425-4CAA-33AE-B4BB-6C80FB6CE1CE";
	setAttr ".cf" 57.295779513082323;
createNode blendColors -n "curve1_jnt_orientConstraint1_bc";
	rename -uid "00672DC6-46F6-51E6-FDEF-CEB3405BAA43";
createNode unitConversion -n "unitConversion20";
	rename -uid "EF870D41-42A3-9628-28C5-EB89D2F2CD82";
	setAttr ".cf" 57.295779513082323;
createNode unitConversion -n "unitConversion21";
	rename -uid "51F50AD0-44DF-0D64-2F38-5CB2DCC87D0D";
	setAttr ".cf" 57.295779513082323;
createNode unitConversion -n "unitConversion22";
	rename -uid "5C6E8B9E-4219-D38F-923B-2DB99EDDA7A0";
	setAttr ".cf" 57.295779513082323;
createNode unitConversion -n "unitConversion23";
	rename -uid "24CD89D6-45A7-C14C-B9D9-C59BC70A2600";
	setAttr ".cf" 57.295779513082323;
createNode unitConversion -n "unitConversion24";
	rename -uid "2D2E0291-4CA0-7CCB-F682-90B7DAA5D118";
	setAttr ".cf" 57.295779513082323;
createNode unitConversion -n "unitConversion25";
	rename -uid "D763B0F4-48E1-DC53-7F12-44B332F12E02";
	setAttr ".cf" 57.295779513082323;
createNode unitConversion -n "unitConversion26";
	rename -uid "38583585-486C-02BA-ED98-408795133689";
	setAttr ".cf" 0.017453292519943295;
createNode unitConversion -n "unitConversion27";
	rename -uid "7A61E812-4488-04AC-CD63-059B42671620";
	setAttr ".cf" 0.017453292519943295;
createNode unitConversion -n "unitConversion28";
	rename -uid "3475F96E-4728-4D46-6364-D6AC27DB3E80";
	setAttr ".cf" 0.017453292519943295;
createNode unitConversion -n "unitConversion29";
	rename -uid "12BAA60D-4FB8-A4A0-30D2-2FBF90D1F1F5";
	setAttr ".cf" 0.017453292519943295;
createNode unitConversion -n "unitConversion30";
	rename -uid "96E4D759-4263-377E-E51C-D9A8EB475965";
	setAttr ".cf" 0.017453292519943295;
createNode unitConversion -n "unitConversion31";
	rename -uid "C9402316-4B57-35A6-0B5F-C9A33F3D4688";
	setAttr ".cf" 0.017453292519943295;
createNode unitConversion -n "unitConversion32";
	rename -uid "BAF9C200-44C7-C9FA-2359-9AB02C92C57F";
	setAttr ".cf" 0.017453292519943295;
createNode unitConversion -n "unitConversion33";
	rename -uid "C93F9590-441A-3046-1D6F-9D856BA636DB";
	setAttr ".cf" 0.017453292519943295;
createNode unitConversion -n "unitConversion34";
	rename -uid "5C1DEF66-4A18-8E01-8BFC-DC8DDFC96B44";
	setAttr ".cf" 0.017453292519943295;
createNode unitConversion -n "unitConversion35";
	rename -uid "E0431350-4D14-B776-D1EC-03AC5362BF41";
	setAttr ".cf" 0.017453292519943295;
createNode unitConversion -n "unitConversion36";
	rename -uid "2F0B0B3E-498A-F533-B1A9-3B891AE6EC4E";
	setAttr ".cf" 0.017453292519943295;
createNode unitConversion -n "unitConversion37";
	rename -uid "FA7A5EE9-4356-E9A2-E4D2-F29F38203570";
	setAttr ".cf" 0.017453292519943295;
createNode unitConversion -n "unitConversion38";
	rename -uid "29834281-4730-28D3-7717-4F82FF8F1B7C";
	setAttr ".cf" 0.017453292519943295;
createNode unitConversion -n "unitConversion39";
	rename -uid "1A94BEA2-4261-D9A7-8BD0-759C3AF27D5C";
	setAttr ".cf" 0.017453292519943295;
createNode unitConversion -n "unitConversion40";
	rename -uid "CBDDF398-47EC-2C6C-D23A-85B3DF11DBC5";
	setAttr ".cf" 0.017453292519943295;
createNode unitConversion -n "unitConversion41";
	rename -uid "C8C82726-4C4A-BB36-DEF3-F999E4CC954D";
	setAttr ".cf" 0.017453292519943295;
createNode unitConversion -n "unitConversion42";
	rename -uid "C0CBCE6A-4672-8726-0B0E-60A50C111816";
	setAttr ".cf" 0.017453292519943295;
createNode unitConversion -n "unitConversion43";
	rename -uid "F91282CE-4F4E-8F09-1CA2-B293848770EC";
	setAttr ".cf" 0.017453292519943295;
createNode unitConversion -n "unitConversion44";
	rename -uid "16081A5A-4725-A4C4-0E7C-4F99485AD261";
	setAttr ".cf" 0.017453292519943295;
createNode unitConversion -n "unitConversion45";
	rename -uid "CD258042-4B9D-219F-ADF7-71B0F9352544";
	setAttr ".cf" 0.017453292519943295;
createNode unitConversion -n "unitConversion46";
	rename -uid "312A4570-4C61-10B7-EA01-F280C789C458";
	setAttr ".cf" 0.017453292519943295;
createNode unitConversion -n "unitConversion47";
	rename -uid "5A5D00FF-405C-E6DB-A2AE-9BACB8E9430B";
	setAttr ".cf" 0.017453292519943295;
createNode unitConversion -n "unitConversion48";
	rename -uid "B82BF1A8-4DDA-ED3E-5D0D-7085673CD8C8";
	setAttr ".cf" 0.017453292519943295;
createNode unitConversion -n "unitConversion49";
	rename -uid "7B1AAB83-428A-BED4-CA25-49B4BC95F88D";
	setAttr ".cf" 0.017453292519943295;
createNode unitConversion -n "unitConversion50";
	rename -uid "7B227EF8-4F57-AD83-4449-0693CBC7BEA7";
	setAttr ".cf" 57.295779513082323;
createNode unitConversion -n "unitConversion51";
	rename -uid "64410970-4FE1-38A9-A89D-4E93A3FE42E5";
	setAttr ".cf" 57.295779513082323;
createNode unitConversion -n "unitConversion52";
	rename -uid "1EFD0589-4641-B0E9-D2D7-A7922E07A051";
	setAttr ".cf" 57.295779513082323;
createNode unitConversion -n "unitConversion53";
	rename -uid "7DE3AAE5-43F5-4DEE-CCF5-D7922BFE0EFA";
	setAttr ".cf" 57.295779513082323;
createNode unitConversion -n "unitConversion54";
	rename -uid "152F9E03-49D1-D436-7D3C-C4B313A94CE5";
	setAttr ".cf" 57.295779513082323;
createNode unitConversion -n "unitConversion55";
	rename -uid "FA0E7578-4097-15FE-B6F2-1B96047DE59F";
	setAttr ".cf" 57.295779513082323;
createNode unitConversion -n "unitConversion56";
	rename -uid "D85FF4B3-43A0-742C-08ED-A5AA869BD6F0";
	setAttr ".cf" 57.295779513082323;
createNode unitConversion -n "unitConversion57";
	rename -uid "83F64231-4A4A-0C8E-3D7C-ADA5AB8B89C6";
	setAttr ".cf" 57.295779513082323;
createNode unitConversion -n "unitConversion58";
	rename -uid "13FD94B2-434D-1C2E-DD7B-D0B01CE0B1D3";
	setAttr ".cf" 57.295779513082323;
createNode unitConversion -n "unitConversion59";
	rename -uid "D4BC0B73-439A-3B7E-17E3-A0BB76767EE9";
	setAttr ".cf" 57.295779513082323;
createNode unitConversion -n "unitConversion60";
	rename -uid "A77AE39C-4156-98A7-5EAA-BD951002AFAC";
	setAttr ".cf" 57.295779513082323;
createNode unitConversion -n "unitConversion61";
	rename -uid "A6B1CC50-4F9D-D4D9-B7D3-85A7CC013566";
	setAttr ".cf" 57.295779513082323;
createNode unitConversion -n "unitConversion62";
	rename -uid "709EEE1D-4618-FBE0-C7DB-9783D468206D";
	setAttr ".cf" 57.295779513082323;
createNode unitConversion -n "unitConversion63";
	rename -uid "66C44D4F-49B4-B5C3-DD68-869CD88EC501";
	setAttr ".cf" 57.295779513082323;
createNode unitConversion -n "unitConversion64";
	rename -uid "7F662DF6-480D-B3B5-7F44-9285CC2F8709";
	setAttr ".cf" 57.295779513082323;
createNode unitConversion -n "unitConversion65";
	rename -uid "4BA967F5-4B97-5303-E9BC-BAAFAB30F673";
	setAttr ".cf" 57.295779513082323;
createNode unitConversion -n "unitConversion66";
	rename -uid "E644B02A-4198-E343-DC6C-C69F6865E1F4";
	setAttr ".cf" 57.295779513082323;
createNode unitConversion -n "unitConversion67";
	rename -uid "E69ECF58-4DDF-F232-3C10-1B8328A1A1B1";
	setAttr ".cf" 57.295779513082323;
createNode unitConversion -n "unitConversion68";
	rename -uid "A2613ABC-4D79-8EE7-4796-3599ECB5F2B4";
	setAttr ".cf" 57.295779513082323;
createNode unitConversion -n "unitConversion69";
	rename -uid "AAC81B99-4CE9-60EF-3ECD-B1A9B7045E3B";
	setAttr ".cf" 57.295779513082323;
createNode unitConversion -n "unitConversion70";
	rename -uid "98199AF3-40B9-86C0-4654-17814F477343";
	setAttr ".cf" 57.295779513082323;
createNode unitConversion -n "unitConversion71";
	rename -uid "BF0FE7FE-42C0-ED8F-619E-E5BACAB98671";
	setAttr ".cf" 57.295779513082323;
createNode unitConversion -n "unitConversion72";
	rename -uid "A389EF61-46A2-DF96-D32F-26A1A0D82CB0";
	setAttr ".cf" 57.295779513082323;
createNode unitConversion -n "unitConversion73";
	rename -uid "CE86B86C-456B-3AD6-BF19-C0ADD7575831";
	setAttr ".cf" 57.295779513082323;
createNode floatMath -n "curve1_jnt_orientConstraint1_bc_fm";
	rename -uid "A1DAF6B3-41F2-1B66-A0BE-93B00961AD02";
	setAttr "._fb" 4;
	setAttr "._cnd" 3;
createNode floatMath -n "curve2_jnt_orientConstraint1_bc_fm";
	rename -uid "08A6A04F-4593-A266-0CC4-5CADC9C3290D";
	setAttr "._fb" 3;
	setAttr "._cnd" 3;
createNode floatMath -n "curve3_jnt_orientConstraint1_bc_fm";
	rename -uid "D4257637-4412-DDF8-286F-D69DD5D74398";
	setAttr "._fb" 2;
	setAttr "._cnd" 3;
createNode floatMath -n "curve4_jnt_orientConstraint1_bc_fm";
	rename -uid "AA1E193B-4026-6B3B-98D4-A2A684F6DF3B";
	setAttr "._cnd" 3;
createNode floatMath -n "curve5_jnt_orientConstraint1_bc_fm";
	rename -uid "4894B067-48D6-0F6C-A873-20A8D2AA2CCB";
	setAttr "._cnd" 3;
createNode floatMath -n "curve6_jnt_orientConstraint1_bc_fm";
	rename -uid "A790A7A8-4BA6-E9DD-71F6-F8A43F5178E2";
	setAttr "._cnd" 3;
createNode floatMath -n "curve7_jnt_orientConstraint1_bc_fm";
	rename -uid "3FDFE866-4702-7CA3-6402-2D84D7DFC8EE";
	setAttr "._cnd" 3;
createNode floatMath -n "curve8_jnt_orientConstraint1_bc_fm";
	rename -uid "D32E0DEE-4D1A-FB42-200E-8DA8B6BC6139";
	setAttr "._cnd" 3;
createNode unitConversion -n "unitConversion74";
	rename -uid "B19FBE76-40E1-1CFA-D07C-139C0CACC00B";
	setAttr ".cf" 0.017453292519943295;
createNode unitConversion -n "unitConversion75";
	rename -uid "D67623BE-4F7F-9697-0D0C-FAB0680B10C8";
	setAttr ".cf" 0.017453292519943295;
createNode unitConversion -n "unitConversion76";
	rename -uid "8978A384-4D75-0DCD-160E-498F6A129EC0";
	setAttr ".cf" 0.017453292519943295;
createNode unitConversion -n "unitConversion77";
	rename -uid "49ED7953-4AB6-B76C-4884-F0813F1F431C";
	setAttr ".cf" 0.017453292519943295;
createNode unitConversion -n "unitConversion78";
	rename -uid "514517A3-46FF-445E-18A2-D0A04287C9CE";
	setAttr ".cf" 0.017453292519943295;
createNode unitConversion -n "unitConversion79";
	rename -uid "2368C3E0-4EC4-DED0-AC48-098B6818C19F";
	setAttr ".cf" 0.017453292519943295;
createNode unitConversion -n "unitConversion80";
	rename -uid "CDEEBD8A-478A-D4BF-87E1-7E92AFC548A5";
	setAttr ".cf" 0.017453292519943295;
createNode unitConversion -n "unitConversion81";
	rename -uid "AA2907BE-4E41-A6EA-1A9C-A4A7E12DB19B";
	setAttr ".cf" 0.017453292519943295;
createNode objectSet -n "tweakSet2";
	rename -uid "0010AE8D-4B08-FDB6-B83B-E2A2BC0B7F3F";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "groupId4";
	rename -uid "46983F60-4397-58C5-2940-78B09550B337";
	setAttr ".ihi" 0;
createNode groupParts -n "groupParts4";
	rename -uid "342A8F49-44DF-44A0-1A62-19827F09C6D4";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "cv[*][*]";
createNode tweak -n "tweak2";
	rename -uid "E5044A69-4573-AA38-188D-7D9705E7FBD2";
createNode nodeGraphEditorInfo -n "MayaNodeEditorSavedTabsInfo";
	rename -uid "F33B7791-46CE-5D6E-D344-A28D8D41F06B";
	setAttr -s 7 ".tgi";
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -2627.5011228875273 -1522.6189871156048 ;
	setAttr ".tgi[0].vh" -type "double2" 2522.7392222884869 1101.1904324330999 ;
	setAttr -s 20 ".tgi[0].ni";
	setAttr ".tgi[0].ni[0].x" 1425.7142333984375;
	setAttr ".tgi[0].ni[0].y" -178.57142639160156;
	setAttr ".tgi[0].ni[0].nvs" 18304;
	setAttr ".tgi[0].ni[1].x" -301.42855834960938;
	setAttr ".tgi[0].ni[1].y" -114.28571319580078;
	setAttr ".tgi[0].ni[1].nvs" 18304;
	setAttr ".tgi[0].ni[2].x" -301.42855834960938;
	setAttr ".tgi[0].ni[2].y" -634.28570556640625;
	setAttr ".tgi[0].ni[2].nvs" 18304;
	setAttr ".tgi[0].ni[3].x" -301.42855834960938;
	setAttr ".tgi[0].ni[3].y" 15.714285850524902;
	setAttr ".tgi[0].ni[3].nvs" 18304;
	setAttr ".tgi[0].ni[4].x" -301.42855834960938;
	setAttr ".tgi[0].ni[4].y" -244.28572082519531;
	setAttr ".tgi[0].ni[4].nvs" 18304;
	setAttr ".tgi[0].ni[5].x" -1172.857177734375;
	setAttr ".tgi[0].ni[5].y" -180;
	setAttr ".tgi[0].ni[5].nvs" 18304;
	setAttr ".tgi[0].ni[6].x" -301.42855834960938;
	setAttr ".tgi[0].ni[6].y" 145.71427917480469;
	setAttr ".tgi[0].ni[6].nvs" 18304;
	setAttr ".tgi[0].ni[7].x" -1172.857177734375;
	setAttr ".tgi[0].ni[7].y" 22.857143402099609;
	setAttr ".tgi[0].ni[7].nvs" 18304;
	setAttr ".tgi[0].ni[8].x" -2094.28564453125;
	setAttr ".tgi[0].ni[8].y" -247.14285278320313;
	setAttr ".tgi[0].ni[8].nvs" 18304;
	setAttr ".tgi[0].ni[9].x" -1172.857177734375;
	setAttr ".tgi[0].ni[9].y" -281.42855834960938;
	setAttr ".tgi[0].ni[9].nvs" 18304;
	setAttr ".tgi[0].ni[10].x" 1272.857177734375;
	setAttr ".tgi[0].ni[10].y" 365.71429443359375;
	setAttr ".tgi[0].ni[10].nvs" 18304;
	setAttr ".tgi[0].ni[11].x" 14.285714149475098;
	setAttr ".tgi[0].ni[11].y" -504.28570556640625;
	setAttr ".tgi[0].ni[11].nvs" 18304;
	setAttr ".tgi[0].ni[12].x" -2094.28564453125;
	setAttr ".tgi[0].ni[12].y" -145.71427917480469;
	setAttr ".tgi[0].ni[12].nvs" 18304;
	setAttr ".tgi[0].ni[13].x" -1172.857177734375;
	setAttr ".tgi[0].ni[13].y" -78.571426391601563;
	setAttr ".tgi[0].ni[13].nvs" 18304;
	setAttr ".tgi[0].ni[14].x" -301.42855834960938;
	setAttr ".tgi[0].ni[14].y" 275.71429443359375;
	setAttr ".tgi[0].ni[14].nvs" 18304;
	setAttr ".tgi[0].ni[15].x" 1118.5714111328125;
	setAttr ".tgi[0].ni[15].y" -178.57142639160156;
	setAttr ".tgi[0].ni[15].nvs" 18304;
	setAttr ".tgi[0].ni[16].x" 1272.857177734375;
	setAttr ".tgi[0].ni[16].y" 625.71429443359375;
	setAttr ".tgi[0].ni[16].nvs" 18304;
	setAttr ".tgi[0].ni[17].x" -142.85714721679688;
	setAttr ".tgi[0].ni[17].y" 722.85711669921875;
	setAttr ".tgi[0].ni[17].nvs" 18304;
	setAttr ".tgi[0].ni[18].x" 1272.857177734375;
	setAttr ".tgi[0].ni[18].y" 495.71429443359375;
	setAttr ".tgi[0].ni[18].nvs" 18304;
	setAttr ".tgi[0].ni[19].x" 14.285714149475098;
	setAttr ".tgi[0].ni[19].y" -374.28570556640625;
	setAttr ".tgi[0].ni[19].nvs" 18304;
	setAttr ".tgi[1].tn" -type "string" "Untitled_2";
	setAttr ".tgi[1].vl" -type "double2" 927.00413596730675 -1052.3809105630921 ;
	setAttr ".tgi[1].vh" -type "double2" 4224.1861355332585 627.38092745107406 ;
	setAttr -s 17 ".tgi[1].ni";
	setAttr ".tgi[1].ni[0].x" 1830;
	setAttr ".tgi[1].ni[0].y" -231.42857360839844;
	setAttr ".tgi[1].ni[0].nvs" 18306;
	setAttr ".tgi[1].ni[1].x" 1762.857177734375;
	setAttr ".tgi[1].ni[1].y" 250;
	setAttr ".tgi[1].ni[1].nvs" 18304;
	setAttr ".tgi[1].ni[2].x" 2471.428466796875;
	setAttr ".tgi[1].ni[2].y" -830;
	setAttr ".tgi[1].ni[2].nvs" 18304;
	setAttr ".tgi[1].ni[3].x" 3365.71435546875;
	setAttr ".tgi[1].ni[3].y" -40;
	setAttr ".tgi[1].ni[3].nvs" 18304;
	setAttr ".tgi[1].ni[4].x" 2751.428466796875;
	setAttr ".tgi[1].ni[4].y" 377.14285278320313;
	setAttr ".tgi[1].ni[4].nvs" 18306;
	setAttr ".tgi[1].ni[5].x" 1522.857177734375;
	setAttr ".tgi[1].ni[5].y" -592.85711669921875;
	setAttr ".tgi[1].ni[5].nvs" 18304;
	setAttr ".tgi[1].ni[6].x" 2491.428466796875;
	setAttr ".tgi[1].ni[6].y" -960;
	setAttr ".tgi[1].ni[6].nvs" 18304;
	setAttr ".tgi[1].ni[7].x" 2444.28564453125;
	setAttr ".tgi[1].ni[7].y" 18.571428298950195;
	setAttr ".tgi[1].ni[7].nvs" 18306;
	setAttr ".tgi[1].ni[8].x" 1379.88818359375;
	setAttr ".tgi[1].ni[8].y" 63.755855560302734;
	setAttr ".tgi[1].ni[8].nvs" 18304;
	setAttr ".tgi[1].ni[9].x" 3905.71435546875;
	setAttr ".tgi[1].ni[9].y" -178.57142639160156;
	setAttr ".tgi[1].ni[9].nvs" 18304;
	setAttr ".tgi[1].ni[10].x" 2010;
	setAttr ".tgi[1].ni[10].y" -712.85711669921875;
	setAttr ".tgi[1].ni[10].nvs" 18304;
	setAttr ".tgi[1].ni[11].x" 2317.142822265625;
	setAttr ".tgi[1].ni[11].y" -712.85711669921875;
	setAttr ".tgi[1].ni[11].nvs" 18304;
	setAttr ".tgi[1].ni[12].x" 2137.142822265625;
	setAttr ".tgi[1].ni[12].y" -72.857139587402344;
	setAttr ".tgi[1].ni[12].nvs" 18306;
	setAttr ".tgi[1].ni[13].x" 3058.571533203125;
	setAttr ".tgi[1].ni[13].y" -62.857143402099609;
	setAttr ".tgi[1].ni[13].nvs" 18304;
	setAttr ".tgi[1].ni[14].x" 3598.571533203125;
	setAttr ".tgi[1].ni[14].y" -178.57142639160156;
	setAttr ".tgi[1].ni[14].nvs" 18304;
	setAttr ".tgi[1].ni[15].x" 1522.857177734375;
	setAttr ".tgi[1].ni[15].y" -491.42855834960938;
	setAttr ".tgi[1].ni[15].nvs" 18304;
	setAttr ".tgi[1].ni[16].x" 3365.71435546875;
	setAttr ".tgi[1].ni[16].y" -141.42857360839844;
	setAttr ".tgi[1].ni[16].nvs" 18306;
	setAttr ".tgi[2].tn" -type "string" "Untitled_3";
	setAttr ".tgi[2].vl" -type "double2" 157.38362566265585 -7339.9643404029812 ;
	setAttr ".tgi[2].vh" -type "double2" 4264.3730095754281 -5247.6430681364964 ;
	setAttr -s 112 ".tgi[2].ni";
	setAttr ".tgi[2].ni[0].x" 447.14285278320313;
	setAttr ".tgi[2].ni[0].y" -6268.5712890625;
	setAttr ".tgi[2].ni[0].nvs" 18304;
	setAttr ".tgi[2].ni[1].x" 447.14285278320313;
	setAttr ".tgi[2].ni[1].y" -4524.28564453125;
	setAttr ".tgi[2].ni[1].nvs" 18304;
	setAttr ".tgi[2].ni[2].x" 447.14285278320313;
	setAttr ".tgi[2].ni[2].y" -7248.5712890625;
	setAttr ".tgi[2].ni[2].nvs" 18304;
	setAttr ".tgi[2].ni[3].x" 447.14285278320313;
	setAttr ".tgi[2].ni[3].y" -9972.857421875;
	setAttr ".tgi[2].ni[3].nvs" 18304;
	setAttr ".tgi[2].ni[4].x" 447.14285278320313;
	setAttr ".tgi[2].ni[4].y" -9250;
	setAttr ".tgi[2].ni[4].nvs" 18304;
	setAttr ".tgi[2].ni[5].x" 2014.2857666015625;
	setAttr ".tgi[2].ni[5].y" -9058.5712890625;
	setAttr ".tgi[2].ni[5].nvs" 18304;
	setAttr ".tgi[2].ni[6].x" 2321.428466796875;
	setAttr ".tgi[2].ni[6].y" -6934.28564453125;
	setAttr ".tgi[2].ni[6].nvs" 18304;
	setAttr ".tgi[2].ni[7].x" 1061.4285888671875;
	setAttr ".tgi[2].ni[7].y" -6302.85693359375;
	setAttr ".tgi[2].ni[7].nvs" 18305;
	setAttr ".tgi[2].ni[8].x" 447.14285278320313;
	setAttr ".tgi[2].ni[8].y" -5418.5712890625;
	setAttr ".tgi[2].ni[8].nvs" 18304;
	setAttr ".tgi[2].ni[9].x" 2321.428466796875;
	setAttr ".tgi[2].ni[9].y" -9054.2861328125;
	setAttr ".tgi[2].ni[9].nvs" 18304;
	setAttr ".tgi[2].ni[10].x" 2014.2857666015625;
	setAttr ".tgi[2].ni[10].y" -6927.14306640625;
	setAttr ".tgi[2].ni[10].nvs" 18304;
	setAttr ".tgi[2].ni[11].x" 1372.857177734375;
	setAttr ".tgi[2].ni[11].y" -6301.4287109375;
	setAttr ".tgi[2].ni[11].nvs" 18304;
	setAttr ".tgi[2].ni[12].x" 1372.857177734375;
	setAttr ".tgi[2].ni[12].y" -7274.28564453125;
	setAttr ".tgi[2].ni[12].nvs" 18304;
	setAttr ".tgi[2].ni[13].x" 2321.428466796875;
	setAttr ".tgi[2].ni[13].y" -6114.28564453125;
	setAttr ".tgi[2].ni[13].nvs" 18304;
	setAttr ".tgi[2].ni[14].x" 447.14285278320313;
	setAttr ".tgi[2].ni[14].y" -8584.2861328125;
	setAttr ".tgi[2].ni[14].nvs" 18304;
	setAttr ".tgi[2].ni[15].x" 447.14285278320313;
	setAttr ".tgi[2].ni[15].y" -7852.85693359375;
	setAttr ".tgi[2].ni[15].nvs" 18304;
	setAttr ".tgi[2].ni[16].x" 2014.2857666015625;
	setAttr ".tgi[2].ni[16].y" -7597.14306640625;
	setAttr ".tgi[2].ni[16].nvs" 18304;
	setAttr ".tgi[2].ni[17].x" 754.28570556640625;
	setAttr ".tgi[2].ni[17].y" -7421.4287109375;
	setAttr ".tgi[2].ni[17].nvs" 18304;
	setAttr ".tgi[2].ni[18].x" 2014.2857666015625;
	setAttr ".tgi[2].ni[18].y" -9802.857421875;
	setAttr ".tgi[2].ni[18].nvs" 18304;
	setAttr ".tgi[2].ni[19].x" 1395.7142333984375;
	setAttr ".tgi[2].ni[19].y" -8398.5712890625;
	setAttr ".tgi[2].ni[19].nvs" 18305;
	setAttr ".tgi[2].ni[20].x" 1372.857177734375;
	setAttr ".tgi[2].ni[20].y" -5530;
	setAttr ".tgi[2].ni[20].nvs" 18304;
	setAttr ".tgi[2].ni[21].x" 1088.5714111328125;
	setAttr ".tgi[2].ni[21].y" -10007.142578125;
	setAttr ".tgi[2].ni[21].nvs" 18304;
	setAttr ".tgi[2].ni[22].x" 1395.7142333984375;
	setAttr ".tgi[2].ni[22].y" -9077.142578125;
	setAttr ".tgi[2].ni[22].nvs" 18305;
	setAttr ".tgi[2].ni[23].x" 1372.857177734375;
	setAttr ".tgi[2].ni[23].y" -5124.28564453125;
	setAttr ".tgi[2].ni[23].nvs" 18304;
	setAttr ".tgi[2].ni[24].x" 2014.2857666015625;
	setAttr ".tgi[2].ni[24].y" -7698.5712890625;
	setAttr ".tgi[2].ni[24].nvs" 18304;
	setAttr ".tgi[2].ni[25].x" 754.28570556640625;
	setAttr ".tgi[2].ni[25].y" -4501.4287109375;
	setAttr ".tgi[2].ni[25].nvs" 18305;
	setAttr ".tgi[2].ni[26].x" 1061.4285888671875;
	setAttr ".tgi[2].ni[26].y" -5438.5712890625;
	setAttr ".tgi[2].ni[26].nvs" 18305;
	setAttr ".tgi[2].ni[27].x" 1372.857177734375;
	setAttr ".tgi[2].ni[27].y" -4252.85693359375;
	setAttr ".tgi[2].ni[27].nvs" 18304;
	setAttr ".tgi[2].ni[28].x" 1702.857177734375;
	setAttr ".tgi[2].ni[28].y" -9721.4287109375;
	setAttr ".tgi[2].ni[28].nvs" 18305;
	setAttr ".tgi[2].ni[29].x" 754.28570556640625;
	setAttr ".tgi[2].ni[29].y" -9848.5712890625;
	setAttr ".tgi[2].ni[29].nvs" 18305;
	setAttr ".tgi[2].ni[30].x" 1372.857177734375;
	setAttr ".tgi[2].ni[30].y" -4965.71435546875;
	setAttr ".tgi[2].ni[30].nvs" 18304;
	setAttr ".tgi[2].ni[31].x" 754.28570556640625;
	setAttr ".tgi[2].ni[31].y" -7792.85693359375;
	setAttr ".tgi[2].ni[31].nvs" 18305;
	setAttr ".tgi[2].ni[32].x" 1680;
	setAttr ".tgi[2].ni[32].y" -5091.4287109375;
	setAttr ".tgi[2].ni[32].nvs" 18305;
	setAttr ".tgi[2].ni[33].x" 754.28570556640625;
	setAttr ".tgi[2].ni[33].y" -4837.14306640625;
	setAttr ".tgi[2].ni[33].nvs" 18304;
	setAttr ".tgi[2].ni[34].x" 2014.2857666015625;
	setAttr ".tgi[2].ni[34].y" -9904.2861328125;
	setAttr ".tgi[2].ni[34].nvs" 18304;
	setAttr ".tgi[2].ni[35].x" 754.28570556640625;
	setAttr ".tgi[2].ni[35].y" -9204.2861328125;
	setAttr ".tgi[2].ni[35].nvs" 18305;
	setAttr ".tgi[2].ni[36].x" 1395.7142333984375;
	setAttr ".tgi[2].ni[36].y" -10071.4287109375;
	setAttr ".tgi[2].ni[36].nvs" 18304;
	setAttr ".tgi[2].ni[37].x" 1372.857177734375;
	setAttr ".tgi[2].ni[37].y" -4354.28564453125;
	setAttr ".tgi[2].ni[37].nvs" 18304;
	setAttr ".tgi[2].ni[38].x" 1088.5714111328125;
	setAttr ".tgi[2].ni[38].y" -7965.71435546875;
	setAttr ".tgi[2].ni[38].nvs" 18304;
	setAttr ".tgi[2].ni[39].x" 2014.2857666015625;
	setAttr ".tgi[2].ni[39].y" -7800;
	setAttr ".tgi[2].ni[39].nvs" 18304;
	setAttr ".tgi[2].ni[40].x" 1680;
	setAttr ".tgi[2].ni[40].y" -6010;
	setAttr ".tgi[2].ni[40].nvs" 18305;
	setAttr ".tgi[2].ni[41].x" 2014.2857666015625;
	setAttr ".tgi[2].ni[41].y" -8337.142578125;
	setAttr ".tgi[2].ni[41].nvs" 18304;
	setAttr ".tgi[2].ni[42].x" 1372.857177734375;
	setAttr ".tgi[2].ni[42].y" -6200;
	setAttr ".tgi[2].ni[42].nvs" 18304;
	setAttr ".tgi[2].ni[43].x" 1395.7142333984375;
	setAttr ".tgi[2].ni[43].y" -7990;
	setAttr ".tgi[2].ni[43].nvs" 18304;
	setAttr ".tgi[2].ni[44].x" 2321.428466796875;
	setAttr ".tgi[2].ni[44].y" -9798.5712890625;
	setAttr ".tgi[2].ni[44].nvs" 18304;
	setAttr ".tgi[2].ni[45].x" 2014.2857666015625;
	setAttr ".tgi[2].ni[45].y" -8438.5712890625;
	setAttr ".tgi[2].ni[45].nvs" 18304;
	setAttr ".tgi[2].ni[46].x" 1372.857177734375;
	setAttr ".tgi[2].ni[46].y" -6098.5712890625;
	setAttr ".tgi[2].ni[46].nvs" 18304;
	setAttr ".tgi[2].ni[47].x" 754.28570556640625;
	setAttr ".tgi[2].ni[47].y" -8514.2861328125;
	setAttr ".tgi[2].ni[47].nvs" 18306;
	setAttr ".tgi[2].ni[48].x" 1372.857177734375;
	setAttr ".tgi[2].ni[48].y" -5838.5712890625;
	setAttr ".tgi[2].ni[48].nvs" 18304;
	setAttr ".tgi[2].ni[49].x" 1680;
	setAttr ".tgi[2].ni[49].y" -4267.14306640625;
	setAttr ".tgi[2].ni[49].nvs" 18305;
	setAttr ".tgi[2].ni[50].x" 754.28570556640625;
	setAttr ".tgi[2].ni[50].y" -5708.5712890625;
	setAttr ".tgi[2].ni[50].nvs" 18304;
	setAttr ".tgi[2].ni[51].x" 1372.857177734375;
	setAttr ".tgi[2].ni[51].y" -5225.71435546875;
	setAttr ".tgi[2].ni[51].nvs" 18304;
	setAttr ".tgi[2].ni[52].x" 2014.2857666015625;
	setAttr ".tgi[2].ni[52].y" -8540;
	setAttr ".tgi[2].ni[52].nvs" 18304;
	setAttr ".tgi[2].ni[53].x" 1372.857177734375;
	setAttr ".tgi[2].ni[53].y" -4094.28564453125;
	setAttr ".tgi[2].ni[53].nvs" 18304;
	setAttr ".tgi[2].ni[54].x" 2014.2857666015625;
	setAttr ".tgi[2].ni[54].y" -8641.4287109375;
	setAttr ".tgi[2].ni[54].nvs" 18304;
	setAttr ".tgi[2].ni[55].x" 1680;
	setAttr ".tgi[2].ni[55].y" -6804.28564453125;
	setAttr ".tgi[2].ni[55].nvs" 18305;
	setAttr ".tgi[2].ni[56].x" 2014.2857666015625;
	setAttr ".tgi[2].ni[56].y" -9160;
	setAttr ".tgi[2].ni[56].nvs" 18304;
	setAttr ".tgi[2].ni[57].x" 2014.2857666015625;
	setAttr ".tgi[2].ni[57].y" -10005.7138671875;
	setAttr ".tgi[2].ni[57].nvs" 18304;
	setAttr ".tgi[2].ni[58].x" 2014.2857666015625;
	setAttr ".tgi[2].ni[58].y" -7028.5712890625;
	setAttr ".tgi[2].ni[58].nvs" 18304;
	setAttr ".tgi[2].ni[59].x" 2321.428466796875;
	setAttr ".tgi[2].ni[59].y" -4370;
	setAttr ".tgi[2].ni[59].nvs" 18304;
	setAttr ".tgi[2].ni[60].x" 1088.5714111328125;
	setAttr ".tgi[2].ni[60].y" -8168.5712890625;
	setAttr ".tgi[2].ni[60].nvs" 18304;
	setAttr ".tgi[2].ni[61].x" 1088.5714111328125;
	setAttr ".tgi[2].ni[61].y" -8687.142578125;
	setAttr ".tgi[2].ni[61].nvs" 18304;
	setAttr ".tgi[2].ni[62].x" 1088.5714111328125;
	setAttr ".tgi[2].ni[62].y" -8067.14306640625;
	setAttr ".tgi[2].ni[62].nvs" 18304;
	setAttr ".tgi[2].ni[63].x" 1088.5714111328125;
	setAttr ".tgi[2].ni[63].y" -9490;
	setAttr ".tgi[2].ni[63].nvs" 18304;
	setAttr ".tgi[2].ni[64].x" 2014.2857666015625;
	setAttr ".tgi[2].ni[64].y" -4451.4287109375;
	setAttr ".tgi[2].ni[64].nvs" 18304;
	setAttr ".tgi[2].ni[65].x" 2321.428466796875;
	setAttr ".tgi[2].ni[65].y" -8332.857421875;
	setAttr ".tgi[2].ni[65].nvs" 18304;
	setAttr ".tgi[2].ni[66].x" 1061.4285888671875;
	setAttr ".tgi[2].ni[66].y" -7212.85693359375;
	setAttr ".tgi[2].ni[66].nvs" 18305;
	setAttr ".tgi[2].ni[67].x" 1088.5714111328125;
	setAttr ".tgi[2].ni[67].y" -8890;
	setAttr ".tgi[2].ni[67].nvs" 18304;
	setAttr ".tgi[2].ni[68].x" 2014.2857666015625;
	setAttr ".tgi[2].ni[68].y" -6194.28564453125;
	setAttr ".tgi[2].ni[68].nvs" 18304;
	setAttr ".tgi[2].ni[69].x" 1702.857177734375;
	setAttr ".tgi[2].ni[69].y" -9020;
	setAttr ".tgi[2].ni[69].nvs" 18305;
	setAttr ".tgi[2].ni[70].x" 1372.857177734375;
	setAttr ".tgi[2].ni[70].y" -4455.71435546875;
	setAttr ".tgi[2].ni[70].nvs" 18304;
	setAttr ".tgi[2].ni[71].x" 754.28570556640625;
	setAttr ".tgi[2].ni[71].y" -6244.28564453125;
	setAttr ".tgi[2].ni[71].nvs" 18305;
	setAttr ".tgi[2].ni[72].x" 2014.2857666015625;
	setAttr ".tgi[2].ni[72].y" -9261.4287109375;
	setAttr ".tgi[2].ni[72].nvs" 18304;
	setAttr ".tgi[2].ni[73].x" 754.28570556640625;
	setAttr ".tgi[2].ni[73].y" -6580;
	setAttr ".tgi[2].ni[73].nvs" 18304;
	setAttr ".tgi[2].ni[74].x" 1088.5714111328125;
	setAttr ".tgi[2].ni[74].y" -10108.5712890625;
	setAttr ".tgi[2].ni[74].nvs" 18304;
	setAttr ".tgi[2].ni[75].x" 2014.2857666015625;
	setAttr ".tgi[2].ni[75].y" -10107.142578125;
	setAttr ".tgi[2].ni[75].nvs" 18304;
	setAttr ".tgi[2].ni[76].x" 1372.857177734375;
	setAttr ".tgi[2].ni[76].y" -4658.5712890625;
	setAttr ".tgi[2].ni[76].nvs" 18304;
	setAttr ".tgi[2].ni[77].x" 2014.2857666015625;
	setAttr ".tgi[2].ni[77].y" -5274.28564453125;
	setAttr ".tgi[2].ni[77].nvs" 18304;
	setAttr ".tgi[2].ni[78].x" 1088.5714111328125;
	setAttr ".tgi[2].ni[78].y" -9591.4287109375;
	setAttr ".tgi[2].ni[78].nvs" 18304;
	setAttr ".tgi[2].ni[79].x" 1372.857177734375;
	setAttr ".tgi[2].ni[79].y" -4557.14306640625;
	setAttr ".tgi[2].ni[79].nvs" 18304;
	setAttr ".tgi[2].ni[80].x" 1395.7142333984375;
	setAttr ".tgi[2].ni[80].y" -7654.28564453125;
	setAttr ".tgi[2].ni[80].nvs" 18305;
	setAttr ".tgi[2].ni[81].x" 2014.2857666015625;
	setAttr ".tgi[2].ni[81].y" -5375.71435546875;
	setAttr ".tgi[2].ni[81].nvs" 18304;
	setAttr ".tgi[2].ni[82].x" 2321.428466796875;
	setAttr ".tgi[2].ni[82].y" -7588.5712890625;
	setAttr ".tgi[2].ni[82].nvs" 18304;
	setAttr ".tgi[2].ni[83].x" 754.28570556640625;
	setAttr ".tgi[2].ni[83].y" -5372.85693359375;
	setAttr ".tgi[2].ni[83].nvs" 18305;
	setAttr ".tgi[2].ni[84].x" 1395.7142333984375;
	setAttr ".tgi[2].ni[84].y" -9412.857421875;
	setAttr ".tgi[2].ni[84].nvs" 18304;
	setAttr ".tgi[2].ni[85].x" 1702.857177734375;
	setAttr ".tgi[2].ni[85].y" -8298.5712890625;
	setAttr ".tgi[2].ni[85].nvs" 18305;
	setAttr ".tgi[2].ni[86].x" 2014.2857666015625;
	setAttr ".tgi[2].ni[86].y" -4552.85693359375;
	setAttr ".tgi[2].ni[86].nvs" 18304;
	setAttr ".tgi[2].ni[87].x" 1088.5714111328125;
	setAttr ".tgi[2].ni[87].y" -10210;
	setAttr ".tgi[2].ni[87].nvs" 18304;
	setAttr ".tgi[2].ni[88].x" 1395.7142333984375;
	setAttr ".tgi[2].ni[88].y" -9735.7138671875;
	setAttr ".tgi[2].ni[88].nvs" 18305;
	setAttr ".tgi[2].ni[89].x" 2014.2857666015625;
	setAttr ".tgi[2].ni[89].y" -9362.857421875;
	setAttr ".tgi[2].ni[89].nvs" 18304;
	setAttr ".tgi[2].ni[90].x" 1372.857177734375;
	setAttr ".tgi[2].ni[90].y" -6710;
	setAttr ".tgi[2].ni[90].nvs" 18304;
	setAttr ".tgi[2].ni[91].x" 2014.2857666015625;
	setAttr ".tgi[2].ni[91].y" -7901.4287109375;
	setAttr ".tgi[2].ni[91].nvs" 18304;
	setAttr ".tgi[2].ni[92].x" 1372.857177734375;
	setAttr ".tgi[2].ni[92].y" -7172.85693359375;
	setAttr ".tgi[2].ni[92].nvs" 18304;
	setAttr ".tgi[2].ni[93].x" 2014.2857666015625;
	setAttr ".tgi[2].ni[93].y" -8002.85693359375;
	setAttr ".tgi[2].ni[93].nvs" 18304;
	setAttr ".tgi[2].ni[94].x" 2321.428466796875;
	setAttr ".tgi[2].ni[94].y" -5235.71435546875;
	setAttr ".tgi[2].ni[94].nvs" 18304;
	setAttr ".tgi[2].ni[95].x" 1372.857177734375;
	setAttr ".tgi[2].ni[95].y" -7071.4287109375;
	setAttr ".tgi[2].ni[95].nvs" 18304;
	setAttr ".tgi[2].ni[96].x" 1395.7142333984375;
	setAttr ".tgi[2].ni[96].y" -8734.2861328125;
	setAttr ".tgi[2].ni[96].nvs" 18304;
	setAttr ".tgi[2].ni[97].x" 754.28570556640625;
	setAttr ".tgi[2].ni[97].y" -7294.28564453125;
	setAttr ".tgi[2].ni[97].nvs" 18304;
	setAttr ".tgi[2].ni[98].x" 1088.5714111328125;
	setAttr ".tgi[2].ni[98].y" -8788.5712890625;
	setAttr ".tgi[2].ni[98].nvs" 18304;
	setAttr ".tgi[2].ni[99].x" 1372.857177734375;
	setAttr ".tgi[2].ni[99].y" -6970;
	setAttr ".tgi[2].ni[99].nvs" 18304;
	setAttr ".tgi[2].ni[100].x" 1372.857177734375;
	setAttr ".tgi[2].ni[100].y" -5327.14306640625;
	setAttr ".tgi[2].ni[100].nvs" 18304;
	setAttr ".tgi[2].ni[101].x" 2014.2857666015625;
	setAttr ".tgi[2].ni[101].y" -10208.5712890625;
	setAttr ".tgi[2].ni[101].nvs" 18304;
	setAttr ".tgi[2].ni[102].x" 1372.857177734375;
	setAttr ".tgi[2].ni[102].y" -6868.5712890625;
	setAttr ".tgi[2].ni[102].nvs" 18304;
	setAttr ".tgi[2].ni[103].x" 1372.857177734375;
	setAttr ".tgi[2].ni[103].y" -5428.5712890625;
	setAttr ".tgi[2].ni[103].nvs" 18304;
	setAttr ".tgi[2].ni[104].x" 2014.2857666015625;
	setAttr ".tgi[2].ni[104].y" -8742.857421875;
	setAttr ".tgi[2].ni[104].nvs" 18304;
	setAttr ".tgi[2].ni[105].x" 2014.2857666015625;
	setAttr ".tgi[2].ni[105].y" -9464.2861328125;
	setAttr ".tgi[2].ni[105].nvs" 18304;
	setAttr ".tgi[2].ni[106].x" 1702.857177734375;
	setAttr ".tgi[2].ni[106].y" -7554.28564453125;
	setAttr ".tgi[2].ni[106].nvs" 18305;
	setAttr ".tgi[2].ni[107].x" 1061.4285888671875;
	setAttr ".tgi[2].ni[107].y" -4558.5712890625;
	setAttr ".tgi[2].ni[107].nvs" 18305;
	setAttr ".tgi[2].ni[108].x" 2014.2857666015625;
	setAttr ".tgi[2].ni[108].y" -6295.71435546875;
	setAttr ".tgi[2].ni[108].nvs" 18304;
	setAttr ".tgi[2].ni[109].x" 1372.857177734375;
	setAttr ".tgi[2].ni[109].y" -6402.85693359375;
	setAttr ".tgi[2].ni[109].nvs" 18304;
	setAttr ".tgi[2].ni[110].x" 1372.857177734375;
	setAttr ".tgi[2].ni[110].y" -5997.14306640625;
	setAttr ".tgi[2].ni[110].nvs" 18304;
	setAttr ".tgi[2].ni[111].x" 1088.5714111328125;
	setAttr ".tgi[2].ni[111].y" -9388.5712890625;
	setAttr ".tgi[2].ni[111].nvs" 18304;
	setAttr ".tgi[3].tn" -type "string" "Untitled_4";
	setAttr ".tgi[3].vl" -type "double2" -1529.864936754039 -736.90473262279875 ;
	setAttr ".tgi[3].vh" -type "double2" 1103.6744774988504 604.76188073082665 ;
	setAttr -s 7 ".tgi[3].ni";
	setAttr ".tgi[3].ni[0].x" -228.57142639160156;
	setAttr ".tgi[3].ni[0].y" -385.71429443359375;
	setAttr ".tgi[3].ni[0].nvs" 18304;
	setAttr ".tgi[3].ni[1].x" -228.57142639160156;
	setAttr ".tgi[3].ni[1].y" 394.28570556640625;
	setAttr ".tgi[3].ni[1].nvs" 18304;
	setAttr ".tgi[3].ni[2].x" -228.57142639160156;
	setAttr ".tgi[3].ni[2].y" 4.2857141494750977;
	setAttr ".tgi[3].ni[2].nvs" 18304;
	setAttr ".tgi[3].ni[3].x" -228.57142639160156;
	setAttr ".tgi[3].ni[3].y" -255.71427917480469;
	setAttr ".tgi[3].ni[3].nvs" 18304;
	setAttr ".tgi[3].ni[4].x" -228.57142639160156;
	setAttr ".tgi[3].ni[4].y" 134.28572082519531;
	setAttr ".tgi[3].ni[4].nvs" 18304;
	setAttr ".tgi[3].ni[5].x" -228.57142639160156;
	setAttr ".tgi[3].ni[5].y" -125.71428680419922;
	setAttr ".tgi[3].ni[5].nvs" 18304;
	setAttr ".tgi[3].ni[6].x" -228.57142639160156;
	setAttr ".tgi[3].ni[6].y" 264.28570556640625;
	setAttr ".tgi[3].ni[6].nvs" 18304;
	setAttr ".tgi[4].tn" -type "string" "Untitled_5";
	setAttr ".tgi[4].vl" -type "double2" -854.4881840132897 -284.52379821784956 ;
	setAttr ".tgi[4].vh" -type "double2" 748.53580727107783 532.14283599740065 ;
	setAttr -s 4 ".tgi[4].ni";
	setAttr ".tgi[4].ni[0].x" -602.18487548828125;
	setAttr ".tgi[4].ni[0].y" 391.76470947265625;
	setAttr ".tgi[4].ni[0].nvs" 18306;
	setAttr ".tgi[4].ni[1].x" -468.57144165039063;
	setAttr ".tgi[4].ni[1].y" 92.857139587402344;
	setAttr ".tgi[4].ni[1].nvs" 18304;
	setAttr ".tgi[4].ni[2].x" 315.71429443359375;
	setAttr ".tgi[4].ni[2].y" 364.03359985351563;
	setAttr ".tgi[4].ni[2].nvs" 18306;
	setAttr ".tgi[4].ni[3].x" 172.85714721679688;
	setAttr ".tgi[4].ni[3].y" 92.857139587402344;
	setAttr ".tgi[4].ni[3].nvs" 18304;
	setAttr ".tgi[5].tn" -type "string" "Untitled_6";
	setAttr ".tgi[5].vl" -type "double2" 1779.0421913758616 1987.0470056898496 ;
	setAttr ".tgi[5].vh" -type "double2" 4044.5883463163982 3141.2380615156485 ;
	setAttr -s 14 ".tgi[5].ni";
	setAttr ".tgi[5].ni[0].x" 3584.28564453125;
	setAttr ".tgi[5].ni[0].y" 2738.571533203125;
	setAttr ".tgi[5].ni[0].nvs" 18304;
	setAttr ".tgi[5].ni[1].x" 3891.428466796875;
	setAttr ".tgi[5].ni[1].y" 2455.71435546875;
	setAttr ".tgi[5].ni[1].nvs" 18304;
	setAttr ".tgi[5].ni[2].x" 4198.5712890625;
	setAttr ".tgi[5].ni[2].y" 2512.857177734375;
	setAttr ".tgi[5].ni[2].nvs" 18304;
	setAttr ".tgi[5].ni[3].x" 3891.428466796875;
	setAttr ".tgi[5].ni[3].y" 2738.571533203125;
	setAttr ".tgi[5].ni[3].nvs" 18304;
	setAttr ".tgi[5].ni[4].x" 3584.28564453125;
	setAttr ".tgi[5].ni[4].y" 2455.71435546875;
	setAttr ".tgi[5].ni[4].nvs" 18304;
	setAttr ".tgi[5].ni[5].x" 4198.5712890625;
	setAttr ".tgi[5].ni[5].y" 2724.28564453125;
	setAttr ".tgi[5].ni[5].nvs" 18304;
	setAttr ".tgi[5].ni[6].x" 1434.2857666015625;
	setAttr ".tgi[5].ni[6].y" 2575.71435546875;
	setAttr ".tgi[5].ni[6].nvs" 18304;
	setAttr ".tgi[5].ni[7].x" 2355.71435546875;
	setAttr ".tgi[5].ni[7].y" 2625.71435546875;
	setAttr ".tgi[5].ni[7].nvs" 18304;
	setAttr ".tgi[5].ni[8].x" 2048.571533203125;
	setAttr ".tgi[5].ni[8].y" 2625.71435546875;
	setAttr ".tgi[5].ni[8].nvs" 18304;
	setAttr ".tgi[5].ni[9].x" 3277.142822265625;
	setAttr ".tgi[5].ni[9].y" 2681.428466796875;
	setAttr ".tgi[5].ni[9].nvs" 18304;
	setAttr ".tgi[5].ni[10].x" 1741.4285888671875;
	setAttr ".tgi[5].ni[10].y" 2625.71435546875;
	setAttr ".tgi[5].ni[10].nvs" 18304;
	setAttr ".tgi[5].ni[11].x" 2970;
	setAttr ".tgi[5].ni[11].y" 2670;
	setAttr ".tgi[5].ni[11].nvs" 18304;
	setAttr ".tgi[5].ni[12].x" 1434.2857666015625;
	setAttr ".tgi[5].ni[12].y" 2677.142822265625;
	setAttr ".tgi[5].ni[12].nvs" 18304;
	setAttr ".tgi[5].ni[13].x" 2662.857177734375;
	setAttr ".tgi[5].ni[13].y" 2597.142822265625;
	setAttr ".tgi[5].ni[13].nvs" 18304;
	setAttr ".tgi[6].tn" -type "string" "Untitled_7";
	setAttr ".tgi[6].vl" -type "double2" -1707.8745025819001 -881.92927276087573 ;
	setAttr ".tgi[6].vh" -type "double2" 1772.9775927784408 891.40399010652482 ;
	setAttr -s 30 ".tgi[6].ni";
	setAttr ".tgi[6].ni[0].x" 565.71429443359375;
	setAttr ".tgi[6].ni[0].y" 834.28570556640625;
	setAttr ".tgi[6].ni[0].nvs" 18304;
	setAttr ".tgi[6].ni[1].x" 565.71429443359375;
	setAttr ".tgi[6].ni[1].y" 732.85711669921875;
	setAttr ".tgi[6].ni[1].nvs" 18304;
	setAttr ".tgi[6].ni[2].x" -694.28570556640625;
	setAttr ".tgi[6].ni[2].y" 544.28570556640625;
	setAttr ".tgi[6].ni[2].nvs" 18304;
	setAttr ".tgi[6].ni[3].x" 565.71429443359375;
	setAttr ".tgi[6].ni[3].y" 631.4285888671875;
	setAttr ".tgi[6].ni[3].nvs" 18304;
	setAttr ".tgi[6].ni[4].x" -694.28570556640625;
	setAttr ".tgi[6].ni[4].y" -58.571430206298828;
	setAttr ".tgi[6].ni[4].nvs" 18304;
	setAttr ".tgi[6].ni[5].x" 227.14285278320313;
	setAttr ".tgi[6].ni[5].y" 207.14285278320313;
	setAttr ".tgi[6].ni[5].nvs" 18304;
	setAttr ".tgi[6].ni[6].x" 565.71429443359375;
	setAttr ".tgi[6].ni[6].y" -772.85711669921875;
	setAttr ".tgi[6].ni[6].nvs" 18304;
	setAttr ".tgi[6].ni[7].x" -387.14285278320313;
	setAttr ".tgi[6].ni[7].y" 391.42855834960938;
	setAttr ".tgi[6].ni[7].nvs" 18304;
	setAttr ".tgi[6].ni[8].x" 565.71429443359375;
	setAttr ".tgi[6].ni[8].y" 530;
	setAttr ".tgi[6].ni[8].nvs" 18304;
	setAttr ".tgi[6].ni[9].x" 227.14285278320313;
	setAttr ".tgi[6].ni[9].y" 422.85714721679688;
	setAttr ".tgi[6].ni[9].nvs" 18304;
	setAttr ".tgi[6].ni[10].x" 227.14285278320313;
	setAttr ".tgi[6].ni[10].y" 625.71429443359375;
	setAttr ".tgi[6].ni[10].nvs" 18304;
	setAttr ".tgi[6].ni[11].x" 565.71429443359375;
	setAttr ".tgi[6].ni[11].y" 428.57144165039063;
	setAttr ".tgi[6].ni[11].nvs" 18304;
	setAttr ".tgi[6].ni[12].x" 227.14285278320313;
	setAttr ".tgi[6].ni[12].y" 524.28570556640625;
	setAttr ".tgi[6].ni[12].nvs" 18304;
	setAttr ".tgi[6].ni[13].x" 227.14285278320313;
	setAttr ".tgi[6].ni[13].y" 785.71429443359375;
	setAttr ".tgi[6].ni[13].nvs" 18304;
	setAttr ".tgi[6].ni[14].x" 565.71429443359375;
	setAttr ".tgi[6].ni[14].y" -642.85711669921875;
	setAttr ".tgi[6].ni[14].nvs" 18304;
	setAttr ".tgi[6].ni[15].x" -694.28570556640625;
	setAttr ".tgi[6].ni[15].y" 442.85714721679688;
	setAttr ".tgi[6].ni[15].nvs" 18304;
	setAttr ".tgi[6].ni[16].x" -387.14285278320313;
	setAttr ".tgi[6].ni[16].y" 94.285713195800781;
	setAttr ".tgi[6].ni[16].nvs" 18304;
	setAttr ".tgi[6].ni[17].x" 565.71429443359375;
	setAttr ".tgi[6].ni[17].y" 124.28571319580078;
	setAttr ".tgi[6].ni[17].nvs" 18304;
	setAttr ".tgi[6].ni[18].x" 227.14285278320313;
	setAttr ".tgi[6].ni[18].y" -110;
	setAttr ".tgi[6].ni[18].nvs" 18304;
	setAttr ".tgi[6].ni[19].x" 565.71429443359375;
	setAttr ".tgi[6].ni[19].y" 22.857143402099609;
	setAttr ".tgi[6].ni[19].nvs" 18304;
	setAttr ".tgi[6].ni[20].x" -694.28570556640625;
	setAttr ".tgi[6].ni[20].y" 42.857143402099609;
	setAttr ".tgi[6].ni[20].nvs" 18304;
	setAttr ".tgi[6].ni[21].x" 565.71429443359375;
	setAttr ".tgi[6].ni[21].y" -281.42855834960938;
	setAttr ".tgi[6].ni[21].nvs" 18304;
	setAttr ".tgi[6].ni[22].x" 227.14285278320313;
	setAttr ".tgi[6].ni[22].y" -268.57144165039063;
	setAttr ".tgi[6].ni[22].nvs" 18304;
	setAttr ".tgi[6].ni[23].x" 565.71429443359375;
	setAttr ".tgi[6].ni[23].y" -78.571426391601563;
	setAttr ".tgi[6].ni[23].nvs" 18304;
	setAttr ".tgi[6].ni[24].x" 565.71429443359375;
	setAttr ".tgi[6].ni[24].y" -180;
	setAttr ".tgi[6].ni[24].nvs" 18304;
	setAttr ".tgi[6].ni[25].x" 565.71429443359375;
	setAttr ".tgi[6].ni[25].y" -512.85711669921875;
	setAttr ".tgi[6].ni[25].nvs" 18304;
	setAttr ".tgi[6].ni[26].x" -80;
	setAttr ".tgi[6].ni[26].y" 442.85714721679688;
	setAttr ".tgi[6].ni[26].nvs" 18304;
	setAttr ".tgi[6].ni[27].x" 565.71429443359375;
	setAttr ".tgi[6].ni[27].y" -382.85714721679688;
	setAttr ".tgi[6].ni[27].nvs" 18304;
	setAttr ".tgi[6].ni[28].x" 227.14285278320313;
	setAttr ".tgi[6].ni[28].y" -8.5714282989501953;
	setAttr ".tgi[6].ni[28].nvs" 18304;
	setAttr ".tgi[6].ni[29].x" -80;
	setAttr ".tgi[6].ni[29].y" 42.857143402099609;
	setAttr ".tgi[6].ni[29].nvs" 18304;
select -ne :time1;
	setAttr ".o" 1;
	setAttr ".unw" 1;
select -ne :hardwareRenderingGlobals;
	setAttr ".otfna" -type "stringArray" 22 "NURBS Curves" "NURBS Surfaces" "Polygons" "Subdiv Surface" "Particles" "Particle Instance" "Fluids" "Strokes" "Image Planes" "UI" "Lights" "Cameras" "Locators" "Joints" "IK Handles" "Deformers" "Motion Trails" "Components" "Hair Systems" "Follicles" "Misc. UI" "Ornaments"  ;
	setAttr ".otfva" -type "Int32Array" 22 0 1 1 1 1 1
		 1 1 1 0 0 0 0 0 0 0 0 0
		 0 0 0 0 ;
	setAttr ".fprt" yes;
select -ne :renderPartition;
	setAttr -s 2 ".st";
select -ne :renderGlobalsList1;
select -ne :defaultShaderList1;
	setAttr -s 5 ".s";
select -ne :postProcessList1;
	setAttr -s 2 ".p";
select -ne :defaultRenderUtilityList1;
	setAttr -s 3 ".u";
select -ne :defaultRenderingList1;
select -ne :initialShadingGroup;
	setAttr -s 2 ".dsm";
	setAttr ".ro" yes;
select -ne :initialParticleSE;
	setAttr ".ro" yes;
select -ne :defaultRenderGlobals;
	addAttr -ci true -h true -sn "dss" -ln "defaultSurfaceShader" -dt "string";
	setAttr ".ren" -type "string" "arnold";
	setAttr ".dss" -type "string" "lambert1";
select -ne :defaultResolution;
	setAttr ".pa" 1;
select -ne :hardwareRenderGlobals;
	setAttr ".ctrs" 256;
	setAttr ".btrs" 512;
select -ne :ikSystem;
	setAttr -s 4 ".sol";
connectAttr "multiplyDivide1.ox" "Shoulder.sx";
connectAttr "multiplyDivide1.ox" "Elbow.sx";
connectAttr "Shoulder.s" "Elbow.is";
connectAttr "Elbow.s" "Wrist.is";
connectAttr "Wrist.tx" "effector1.tx";
connectAttr "Wrist.ty" "effector1.ty";
connectAttr "Wrist.tz" "effector1.tz";
connectAttr "Wrist.opm" "effector1.opm";
connectAttr "groupId2.id" "loftedSurfaceShape1.iog.og[1].gid";
connectAttr "tweakSet1.mwc" "loftedSurfaceShape1.iog.og[1].gco";
connectAttr "tweak1.og[0]" "loftedSurfaceShape1.cr";
connectAttr "tweak1.pl[0].cp[0]" "loftedSurfaceShape1.twl";
connectAttr "groupId4.id" "loftedSurfaceShape2.iog.og[1].gid";
connectAttr "tweakSet2.mwc" "loftedSurfaceShape2.iog.og[1].gco";
connectAttr "tweak2.og[0]" "loftedSurfaceShape2.cr";
connectAttr "tweak2.pl[0].cp[0]" "loftedSurfaceShape2.twl";
connectAttr "HandShape1.ot" "Hand1.t" -l on;
connectAttr "HandShape1.or" "Hand1.r" -l on;
connectAttr "loftedSurfaceShape1.wm" "HandShape1.iwm";
connectAttr "loftedSurfaceShape1.l" "HandShape1.is";
connectAttr "curveShape1.l" "HandShape1.sp";
connectAttr "curve1.wm" "HandShape1.spm";
connectAttr "HandShape2.ot" "Hand2.t" -l on;
connectAttr "HandShape2.or" "Hand2.r" -l on;
connectAttr "loftedSurfaceShape1.wm" "HandShape2.iwm";
connectAttr "loftedSurfaceShape1.l" "HandShape2.is";
connectAttr "curveShape2.l" "HandShape2.sp";
connectAttr "curve2.wm" "HandShape2.spm";
connectAttr "HandShape3.ot" "Hand3.t" -l on;
connectAttr "HandShape3.or" "Hand3.r" -l on;
connectAttr "loftedSurfaceShape1.wm" "HandShape3.iwm";
connectAttr "loftedSurfaceShape1.l" "HandShape3.is";
connectAttr "curveShape3.l" "HandShape3.sp";
connectAttr "curve3.wm" "HandShape3.spm";
connectAttr "HandShape4.ot" "Hand4.t" -l on;
connectAttr "HandShape4.or" "Hand4.r" -l on;
connectAttr "loftedSurfaceShape1.wm" "HandShape4.iwm";
connectAttr "loftedSurfaceShape1.l" "HandShape4.is";
connectAttr "curveShape4.l" "HandShape4.sp";
connectAttr "curve4.wm" "HandShape4.spm";
connectAttr "HandShape5.ot" "Hand5.t" -l on;
connectAttr "HandShape5.or" "Hand5.r" -l on;
connectAttr "loftedSurfaceShape2.wm" "HandShape5.iwm";
connectAttr "loftedSurfaceShape2.l" "HandShape5.is";
connectAttr "curveShape5.l" "HandShape5.sp";
connectAttr "curve5.wm" "HandShape5.spm";
connectAttr "HandShape6.ot" "Hand6.t" -l on;
connectAttr "HandShape6.or" "Hand6.r" -l on;
connectAttr "loftedSurfaceShape2.wm" "HandShape6.iwm";
connectAttr "loftedSurfaceShape2.l" "HandShape6.is";
connectAttr "curveShape6.l" "HandShape6.sp";
connectAttr "curve6.wm" "HandShape6.spm";
connectAttr "HandShape7.ot" "Hand7.t" -l on;
connectAttr "HandShape7.or" "Hand7.r" -l on;
connectAttr "loftedSurfaceShape2.wm" "HandShape7.iwm";
connectAttr "loftedSurfaceShape2.l" "HandShape7.is";
connectAttr "curveShape7.l" "HandShape7.sp";
connectAttr "curve7.wm" "HandShape7.spm";
connectAttr "HandShape8.ot" "Hand8.t" -l on;
connectAttr "HandShape8.or" "Hand8.r" -l on;
connectAttr "loftedSurfaceShape2.wm" "HandShape8.iwm";
connectAttr "loftedSurfaceShape2.l" "HandShape8.is";
connectAttr "curveShape8.l" "HandShape8.sp";
connectAttr "curve8.wm" "HandShape8.spm";
connectAttr "joint24_jnt_pointConstraint1.ctx" "joint24_jnt.tx";
connectAttr "joint24_jnt_pointConstraint1.cty" "joint24_jnt.ty";
connectAttr "joint24_jnt_pointConstraint1.ctz" "joint24_jnt.tz";
connectAttr "joint24_jnt_aimConstraint1.crx" "joint24_jnt.rx";
connectAttr "joint24_jnt_aimConstraint1.cry" "joint24_jnt.ry";
connectAttr "joint24_jnt_aimConstraint1.crz" "joint24_jnt.rz";
connectAttr "joint24_jnt.pim" "joint24_jnt_pointConstraint1.cpim";
connectAttr "joint24_jnt.rp" "joint24_jnt_pointConstraint1.crp";
connectAttr "joint24_jnt.rpt" "joint24_jnt_pointConstraint1.crt";
connectAttr "Elbow.t" "joint24_jnt_pointConstraint1.tg[0].tt";
connectAttr "Elbow.rp" "joint24_jnt_pointConstraint1.tg[0].trp";
connectAttr "Elbow.rpt" "joint24_jnt_pointConstraint1.tg[0].trt";
connectAttr "Elbow.pm" "joint24_jnt_pointConstraint1.tg[0].tpm";
connectAttr "joint24_jnt_pointConstraint1.w0" "joint24_jnt_pointConstraint1.tg[0].tw"
		;
connectAttr "joint24_jnt.pim" "joint24_jnt_aimConstraint1.cpim";
connectAttr "joint24_jnt.t" "joint24_jnt_aimConstraint1.ct";
connectAttr "joint24_jnt.rp" "joint24_jnt_aimConstraint1.crp";
connectAttr "joint24_jnt.rpt" "joint24_jnt_aimConstraint1.crt";
connectAttr "joint24_jnt.ro" "joint24_jnt_aimConstraint1.cro";
connectAttr "joint24_jnt.jo" "joint24_jnt_aimConstraint1.cjo";
connectAttr "joint24_jnt.is" "joint24_jnt_aimConstraint1.is";
connectAttr "joint23_jnt.t" "joint24_jnt_aimConstraint1.tg[0].tt";
connectAttr "joint23_jnt.rp" "joint24_jnt_aimConstraint1.tg[0].trp";
connectAttr "joint23_jnt.rpt" "joint24_jnt_aimConstraint1.tg[0].trt";
connectAttr "joint23_jnt.pm" "joint24_jnt_aimConstraint1.tg[0].tpm";
connectAttr "joint24_jnt_aimConstraint1.w0" "joint24_jnt_aimConstraint1.tg[0].tw"
		;
connectAttr "joint23_jnt_pointConstraint1.ctx" "joint23_jnt.tx";
connectAttr "joint23_jnt_pointConstraint1.cty" "joint23_jnt.ty";
connectAttr "joint23_jnt_pointConstraint1.ctz" "joint23_jnt.tz";
connectAttr "joint23_jnt_aimConstraint1.crx" "joint23_jnt.rx";
connectAttr "joint23_jnt_aimConstraint1.cry" "joint23_jnt.ry";
connectAttr "joint23_jnt_aimConstraint1.crz" "joint23_jnt.rz";
connectAttr "joint23_jnt.pim" "joint23_jnt_pointConstraint1.cpim";
connectAttr "joint23_jnt.rp" "joint23_jnt_pointConstraint1.crp";
connectAttr "joint23_jnt.rpt" "joint23_jnt_pointConstraint1.crt";
connectAttr "Shoulder.t" "joint23_jnt_pointConstraint1.tg[0].tt";
connectAttr "Shoulder.rp" "joint23_jnt_pointConstraint1.tg[0].trp";
connectAttr "Shoulder.rpt" "joint23_jnt_pointConstraint1.tg[0].trt";
connectAttr "Shoulder.pm" "joint23_jnt_pointConstraint1.tg[0].tpm";
connectAttr "joint23_jnt_pointConstraint1.w0" "joint23_jnt_pointConstraint1.tg[0].tw"
		;
connectAttr "joint23_jnt.pim" "joint23_jnt_aimConstraint1.cpim";
connectAttr "joint23_jnt.t" "joint23_jnt_aimConstraint1.ct";
connectAttr "joint23_jnt.rp" "joint23_jnt_aimConstraint1.crp";
connectAttr "joint23_jnt.rpt" "joint23_jnt_aimConstraint1.crt";
connectAttr "joint23_jnt.ro" "joint23_jnt_aimConstraint1.cro";
connectAttr "joint23_jnt.jo" "joint23_jnt_aimConstraint1.cjo";
connectAttr "joint23_jnt.is" "joint23_jnt_aimConstraint1.is";
connectAttr "joint24_jnt.t" "joint23_jnt_aimConstraint1.tg[0].tt";
connectAttr "joint24_jnt.rp" "joint23_jnt_aimConstraint1.tg[0].trp";
connectAttr "joint24_jnt.rpt" "joint23_jnt_aimConstraint1.tg[0].trt";
connectAttr "joint24_jnt.pm" "joint23_jnt_aimConstraint1.tg[0].tpm";
connectAttr "joint23_jnt_aimConstraint1.w0" "joint23_jnt_aimConstraint1.tg[0].tw"
		;
connectAttr "curve1_jnt_parentConstraint1.ctx" "curve1_jnt.tx";
connectAttr "curve1_jnt_parentConstraint1.cty" "curve1_jnt.ty";
connectAttr "curve1_jnt_parentConstraint1.ctz" "curve1_jnt.tz";
connectAttr "unitConversion81.o" "curve1_jnt.rx";
connectAttr "unitConversion36.o" "curve1_jnt.ry";
connectAttr "unitConversion28.o" "curve1_jnt.rz";
connectAttr "curve1_jnt.ro" "curve1_jnt_parentConstraint1.cro";
connectAttr "curve1_jnt.pim" "curve1_jnt_parentConstraint1.cpim";
connectAttr "curve1_jnt.rp" "curve1_jnt_parentConstraint1.crp";
connectAttr "curve1_jnt.rpt" "curve1_jnt_parentConstraint1.crt";
connectAttr "curve1_jnt.jo" "curve1_jnt_parentConstraint1.cjo";
connectAttr "curve1.t" "curve1_jnt_parentConstraint1.tg[0].tt";
connectAttr "curve1.rp" "curve1_jnt_parentConstraint1.tg[0].trp";
connectAttr "curve1.rpt" "curve1_jnt_parentConstraint1.tg[0].trt";
connectAttr "curve1.r" "curve1_jnt_parentConstraint1.tg[0].tr";
connectAttr "curve1.ro" "curve1_jnt_parentConstraint1.tg[0].tro";
connectAttr "curve1.s" "curve1_jnt_parentConstraint1.tg[0].ts";
connectAttr "curve1.pm" "curve1_jnt_parentConstraint1.tg[0].tpm";
connectAttr "curve1_jnt_parentConstraint1.w0" "curve1_jnt_parentConstraint1.tg[0].tw"
		;
connectAttr "curve1_jnt.ro" "curve1_jnt_orientConstraint1.cro";
connectAttr "curve1_jnt.pim" "curve1_jnt_orientConstraint1.cpim";
connectAttr "curve1_jnt.jo" "curve1_jnt_orientConstraint1.cjo";
connectAttr "curve1_jnt.is" "curve1_jnt_orientConstraint1.is";
connectAttr "curve1.r" "curve1_jnt_orientConstraint1.tg[0].tr";
connectAttr "curve1.ro" "curve1_jnt_orientConstraint1.tg[0].tro";
connectAttr "curve1.pm" "curve1_jnt_orientConstraint1.tg[0].tpm";
connectAttr "curve1_jnt_orientConstraint1.w0" "curve1_jnt_orientConstraint1.tg[0].tw"
		;
connectAttr "curve2_jnt_parentConstraint1.ctx" "curve2_jnt.tx";
connectAttr "curve2_jnt_parentConstraint1.cty" "curve2_jnt.ty";
connectAttr "curve2_jnt_parentConstraint1.ctz" "curve2_jnt.tz";
connectAttr "unitConversion80.o" "curve2_jnt.rx";
connectAttr "unitConversion37.o" "curve2_jnt.ry";
connectAttr "unitConversion29.o" "curve2_jnt.rz";
connectAttr "curve2_jnt.ro" "curve2_jnt_parentConstraint1.cro";
connectAttr "curve2_jnt.pim" "curve2_jnt_parentConstraint1.cpim";
connectAttr "curve2_jnt.rp" "curve2_jnt_parentConstraint1.crp";
connectAttr "curve2_jnt.rpt" "curve2_jnt_parentConstraint1.crt";
connectAttr "curve2_jnt.jo" "curve2_jnt_parentConstraint1.cjo";
connectAttr "curve2.t" "curve2_jnt_parentConstraint1.tg[0].tt";
connectAttr "curve2.rp" "curve2_jnt_parentConstraint1.tg[0].trp";
connectAttr "curve2.rpt" "curve2_jnt_parentConstraint1.tg[0].trt";
connectAttr "curve2.r" "curve2_jnt_parentConstraint1.tg[0].tr";
connectAttr "curve2.ro" "curve2_jnt_parentConstraint1.tg[0].tro";
connectAttr "curve2.s" "curve2_jnt_parentConstraint1.tg[0].ts";
connectAttr "curve2.pm" "curve2_jnt_parentConstraint1.tg[0].tpm";
connectAttr "curve2_jnt_parentConstraint1.w0" "curve2_jnt_parentConstraint1.tg[0].tw"
		;
connectAttr "curve2_jnt.ro" "curve2_jnt_orientConstraint1.cro";
connectAttr "curve2_jnt.pim" "curve2_jnt_orientConstraint1.cpim";
connectAttr "curve2_jnt.jo" "curve2_jnt_orientConstraint1.cjo";
connectAttr "curve2_jnt.is" "curve2_jnt_orientConstraint1.is";
connectAttr "curve2.r" "curve2_jnt_orientConstraint1.tg[0].tr";
connectAttr "curve2.ro" "curve2_jnt_orientConstraint1.tg[0].tro";
connectAttr "curve2.pm" "curve2_jnt_orientConstraint1.tg[0].tpm";
connectAttr "curve2_jnt_orientConstraint1.w0" "curve2_jnt_orientConstraint1.tg[0].tw"
		;
connectAttr "curve3_jnt_parentConstraint1.ctx" "curve3_jnt.tx";
connectAttr "curve3_jnt_parentConstraint1.cty" "curve3_jnt.ty";
connectAttr "curve3_jnt_parentConstraint1.ctz" "curve3_jnt.tz";
connectAttr "unitConversion74.o" "curve3_jnt.rx";
connectAttr "unitConversion38.o" "curve3_jnt.ry";
connectAttr "unitConversion30.o" "curve3_jnt.rz";
connectAttr "curve3_jnt.ro" "curve3_jnt_parentConstraint1.cro";
connectAttr "curve3_jnt.pim" "curve3_jnt_parentConstraint1.cpim";
connectAttr "curve3_jnt.rp" "curve3_jnt_parentConstraint1.crp";
connectAttr "curve3_jnt.rpt" "curve3_jnt_parentConstraint1.crt";
connectAttr "curve3_jnt.jo" "curve3_jnt_parentConstraint1.cjo";
connectAttr "curve3.t" "curve3_jnt_parentConstraint1.tg[0].tt";
connectAttr "curve3.rp" "curve3_jnt_parentConstraint1.tg[0].trp";
connectAttr "curve3.rpt" "curve3_jnt_parentConstraint1.tg[0].trt";
connectAttr "curve3.r" "curve3_jnt_parentConstraint1.tg[0].tr";
connectAttr "curve3.ro" "curve3_jnt_parentConstraint1.tg[0].tro";
connectAttr "curve3.s" "curve3_jnt_parentConstraint1.tg[0].ts";
connectAttr "curve3.pm" "curve3_jnt_parentConstraint1.tg[0].tpm";
connectAttr "curve3_jnt_parentConstraint1.w0" "curve3_jnt_parentConstraint1.tg[0].tw"
		;
connectAttr "curve3_jnt.ro" "curve3_jnt_orientConstraint1.cro";
connectAttr "curve3_jnt.pim" "curve3_jnt_orientConstraint1.cpim";
connectAttr "curve3_jnt.jo" "curve3_jnt_orientConstraint1.cjo";
connectAttr "curve3_jnt.is" "curve3_jnt_orientConstraint1.is";
connectAttr "curve3.r" "curve3_jnt_orientConstraint1.tg[0].tr";
connectAttr "curve3.ro" "curve3_jnt_orientConstraint1.tg[0].tro";
connectAttr "curve3.pm" "curve3_jnt_orientConstraint1.tg[0].tpm";
connectAttr "curve3_jnt_orientConstraint1.w0" "curve3_jnt_orientConstraint1.tg[0].tw"
		;
connectAttr "curve4_jnt_parentConstraint1.ctx" "curve4_jnt.tx";
connectAttr "curve4_jnt_parentConstraint1.cty" "curve4_jnt.ty";
connectAttr "curve4_jnt_parentConstraint1.ctz" "curve4_jnt.tz";
connectAttr "unitConversion75.o" "curve4_jnt.rx";
connectAttr "unitConversion35.o" "curve4_jnt.ry";
connectAttr "unitConversion27.o" "curve4_jnt.rz";
connectAttr "curve4_jnt.ro" "curve4_jnt_parentConstraint1.cro";
connectAttr "curve4_jnt.pim" "curve4_jnt_parentConstraint1.cpim";
connectAttr "curve4_jnt.rp" "curve4_jnt_parentConstraint1.crp";
connectAttr "curve4_jnt.rpt" "curve4_jnt_parentConstraint1.crt";
connectAttr "curve4_jnt.jo" "curve4_jnt_parentConstraint1.cjo";
connectAttr "curve4.t" "curve4_jnt_parentConstraint1.tg[0].tt";
connectAttr "curve4.rp" "curve4_jnt_parentConstraint1.tg[0].trp";
connectAttr "curve4.rpt" "curve4_jnt_parentConstraint1.tg[0].trt";
connectAttr "curve4.r" "curve4_jnt_parentConstraint1.tg[0].tr";
connectAttr "curve4.ro" "curve4_jnt_parentConstraint1.tg[0].tro";
connectAttr "curve4.s" "curve4_jnt_parentConstraint1.tg[0].ts";
connectAttr "curve4.pm" "curve4_jnt_parentConstraint1.tg[0].tpm";
connectAttr "curve4_jnt_parentConstraint1.w0" "curve4_jnt_parentConstraint1.tg[0].tw"
		;
connectAttr "curve4_jnt.ro" "curve4_jnt_orientConstraint1.cro";
connectAttr "curve4_jnt.pim" "curve4_jnt_orientConstraint1.cpim";
connectAttr "curve4_jnt.jo" "curve4_jnt_orientConstraint1.cjo";
connectAttr "curve4_jnt.is" "curve4_jnt_orientConstraint1.is";
connectAttr "curve4.r" "curve4_jnt_orientConstraint1.tg[0].tr";
connectAttr "curve4.ro" "curve4_jnt_orientConstraint1.tg[0].tro";
connectAttr "curve4.pm" "curve4_jnt_orientConstraint1.tg[0].tpm";
connectAttr "curve4_jnt_orientConstraint1.w0" "curve4_jnt_orientConstraint1.tg[0].tw"
		;
connectAttr "curve5_jnt_parentConstraint1.ctx" "curve5_jnt.tx";
connectAttr "curve5_jnt_parentConstraint1.cty" "curve5_jnt.ty";
connectAttr "curve5_jnt_parentConstraint1.ctz" "curve5_jnt.tz";
connectAttr "unitConversion76.o" "curve5_jnt.rx";
connectAttr "unitConversion39.o" "curve5_jnt.ry";
connectAttr "unitConversion31.o" "curve5_jnt.rz";
connectAttr "curve5_jnt.ro" "curve5_jnt_parentConstraint1.cro";
connectAttr "curve5_jnt.pim" "curve5_jnt_parentConstraint1.cpim";
connectAttr "curve5_jnt.rp" "curve5_jnt_parentConstraint1.crp";
connectAttr "curve5_jnt.rpt" "curve5_jnt_parentConstraint1.crt";
connectAttr "curve5_jnt.jo" "curve5_jnt_parentConstraint1.cjo";
connectAttr "curve5.t" "curve5_jnt_parentConstraint1.tg[0].tt";
connectAttr "curve5.rp" "curve5_jnt_parentConstraint1.tg[0].trp";
connectAttr "curve5.rpt" "curve5_jnt_parentConstraint1.tg[0].trt";
connectAttr "curve5.r" "curve5_jnt_parentConstraint1.tg[0].tr";
connectAttr "curve5.ro" "curve5_jnt_parentConstraint1.tg[0].tro";
connectAttr "curve5.s" "curve5_jnt_parentConstraint1.tg[0].ts";
connectAttr "curve5.pm" "curve5_jnt_parentConstraint1.tg[0].tpm";
connectAttr "curve5_jnt_parentConstraint1.w0" "curve5_jnt_parentConstraint1.tg[0].tw"
		;
connectAttr "curve5_jnt.ro" "curve5_jnt_orientConstraint1.cro";
connectAttr "curve5_jnt.pim" "curve5_jnt_orientConstraint1.cpim";
connectAttr "curve5_jnt.jo" "curve5_jnt_orientConstraint1.cjo";
connectAttr "curve5_jnt.is" "curve5_jnt_orientConstraint1.is";
connectAttr "curve5.r" "curve5_jnt_orientConstraint1.tg[0].tr";
connectAttr "curve5.ro" "curve5_jnt_orientConstraint1.tg[0].tro";
connectAttr "curve5.pm" "curve5_jnt_orientConstraint1.tg[0].tpm";
connectAttr "curve5_jnt_orientConstraint1.w0" "curve5_jnt_orientConstraint1.tg[0].tw"
		;
connectAttr "curve6_jnt_parentConstraint1.ctx" "curve6_jnt.tx";
connectAttr "curve6_jnt_parentConstraint1.cty" "curve6_jnt.ty";
connectAttr "curve6_jnt_parentConstraint1.ctz" "curve6_jnt.tz";
connectAttr "curve6_jnt_orientConstraint1.cr" "curve6_jnt.r";
connectAttr "unitConversion77.o" "curve6_jnt.rx";
connectAttr "unitConversion41.o" "curve6_jnt.ry";
connectAttr "unitConversion33.o" "curve6_jnt.rz";
connectAttr "curve6_jnt.ro" "curve6_jnt_parentConstraint1.cro";
connectAttr "curve6_jnt.pim" "curve6_jnt_parentConstraint1.cpim";
connectAttr "curve6_jnt.rp" "curve6_jnt_parentConstraint1.crp";
connectAttr "curve6_jnt.rpt" "curve6_jnt_parentConstraint1.crt";
connectAttr "curve6_jnt.jo" "curve6_jnt_parentConstraint1.cjo";
connectAttr "curve6.t" "curve6_jnt_parentConstraint1.tg[0].tt";
connectAttr "curve6.rp" "curve6_jnt_parentConstraint1.tg[0].trp";
connectAttr "curve6.rpt" "curve6_jnt_parentConstraint1.tg[0].trt";
connectAttr "curve6.r" "curve6_jnt_parentConstraint1.tg[0].tr";
connectAttr "curve6.ro" "curve6_jnt_parentConstraint1.tg[0].tro";
connectAttr "curve6.s" "curve6_jnt_parentConstraint1.tg[0].ts";
connectAttr "curve6.pm" "curve6_jnt_parentConstraint1.tg[0].tpm";
connectAttr "curve6_jnt_parentConstraint1.w0" "curve6_jnt_parentConstraint1.tg[0].tw"
		;
connectAttr "curve6_jnt.ro" "curve6_jnt_orientConstraint1.cro";
connectAttr "curve6_jnt.pim" "curve6_jnt_orientConstraint1.cpim";
connectAttr "curve6_jnt.jo" "curve6_jnt_orientConstraint1.cjo";
connectAttr "curve6_jnt.is" "curve6_jnt_orientConstraint1.is";
connectAttr "curve6.r" "curve6_jnt_orientConstraint1.tg[0].tr";
connectAttr "curve6.ro" "curve6_jnt_orientConstraint1.tg[0].tro";
connectAttr "curve6.pm" "curve6_jnt_orientConstraint1.tg[0].tpm";
connectAttr "curve6_jnt_orientConstraint1.w0" "curve6_jnt_orientConstraint1.tg[0].tw"
		;
connectAttr "curve7_jnt_parentConstraint1.ctx" "curve7_jnt.tx";
connectAttr "curve7_jnt_parentConstraint1.cty" "curve7_jnt.ty";
connectAttr "curve7_jnt_parentConstraint1.ctz" "curve7_jnt.tz";
connectAttr "unitConversion78.o" "curve7_jnt.rx";
connectAttr "unitConversion40.o" "curve7_jnt.ry";
connectAttr "unitConversion32.o" "curve7_jnt.rz";
connectAttr "curve7_jnt.ro" "curve7_jnt_parentConstraint1.cro";
connectAttr "curve7_jnt.pim" "curve7_jnt_parentConstraint1.cpim";
connectAttr "curve7_jnt.rp" "curve7_jnt_parentConstraint1.crp";
connectAttr "curve7_jnt.rpt" "curve7_jnt_parentConstraint1.crt";
connectAttr "curve7_jnt.jo" "curve7_jnt_parentConstraint1.cjo";
connectAttr "curve7.t" "curve7_jnt_parentConstraint1.tg[0].tt";
connectAttr "curve7.rp" "curve7_jnt_parentConstraint1.tg[0].trp";
connectAttr "curve7.rpt" "curve7_jnt_parentConstraint1.tg[0].trt";
connectAttr "curve7.r" "curve7_jnt_parentConstraint1.tg[0].tr";
connectAttr "curve7.ro" "curve7_jnt_parentConstraint1.tg[0].tro";
connectAttr "curve7.s" "curve7_jnt_parentConstraint1.tg[0].ts";
connectAttr "curve7.pm" "curve7_jnt_parentConstraint1.tg[0].tpm";
connectAttr "curve7_jnt_parentConstraint1.w0" "curve7_jnt_parentConstraint1.tg[0].tw"
		;
connectAttr "curve7_jnt.ro" "curve7_jnt_orientConstraint1.cro";
connectAttr "curve7_jnt.pim" "curve7_jnt_orientConstraint1.cpim";
connectAttr "curve7_jnt.jo" "curve7_jnt_orientConstraint1.cjo";
connectAttr "curve7_jnt.is" "curve7_jnt_orientConstraint1.is";
connectAttr "curve7.r" "curve7_jnt_orientConstraint1.tg[0].tr";
connectAttr "curve7.ro" "curve7_jnt_orientConstraint1.tg[0].tro";
connectAttr "curve7.pm" "curve7_jnt_orientConstraint1.tg[0].tpm";
connectAttr "curve7_jnt_orientConstraint1.w0" "curve7_jnt_orientConstraint1.tg[0].tw"
		;
connectAttr "curve8_jnt_parentConstraint1.ctx" "curve8_jnt.tx";
connectAttr "curve8_jnt_parentConstraint1.cty" "curve8_jnt.ty";
connectAttr "curve8_jnt_parentConstraint1.ctz" "curve8_jnt.tz";
connectAttr "unitConversion79.o" "curve8_jnt.rx";
connectAttr "unitConversion34.o" "curve8_jnt.ry";
connectAttr "unitConversion26.o" "curve8_jnt.rz";
connectAttr "curve8_jnt.ro" "curve8_jnt_parentConstraint1.cro";
connectAttr "curve8_jnt.pim" "curve8_jnt_parentConstraint1.cpim";
connectAttr "curve8_jnt.rp" "curve8_jnt_parentConstraint1.crp";
connectAttr "curve8_jnt.rpt" "curve8_jnt_parentConstraint1.crt";
connectAttr "curve8_jnt.jo" "curve8_jnt_parentConstraint1.cjo";
connectAttr "curve8.t" "curve8_jnt_parentConstraint1.tg[0].tt";
connectAttr "curve8.rp" "curve8_jnt_parentConstraint1.tg[0].trp";
connectAttr "curve8.rpt" "curve8_jnt_parentConstraint1.tg[0].trt";
connectAttr "curve8.r" "curve8_jnt_parentConstraint1.tg[0].tr";
connectAttr "curve8.ro" "curve8_jnt_parentConstraint1.tg[0].tro";
connectAttr "curve8.s" "curve8_jnt_parentConstraint1.tg[0].ts";
connectAttr "curve8.pm" "curve8_jnt_parentConstraint1.tg[0].tpm";
connectAttr "curve8_jnt_parentConstraint1.w0" "curve8_jnt_parentConstraint1.tg[0].tw"
		;
connectAttr "curve8_jnt.ro" "curve8_jnt_orientConstraint1.cro";
connectAttr "curve8_jnt.pim" "curve8_jnt_orientConstraint1.cpim";
connectAttr "curve8_jnt.jo" "curve8_jnt_orientConstraint1.cjo";
connectAttr "curve8_jnt.is" "curve8_jnt_orientConstraint1.is";
connectAttr "curve8.r" "curve8_jnt_orientConstraint1.tg[0].tr";
connectAttr "curve8.ro" "curve8_jnt_orientConstraint1.tg[0].tro";
connectAttr "curve8.pm" "curve8_jnt_orientConstraint1.tg[0].tpm";
connectAttr "curve8_jnt_orientConstraint1.w0" "curve8_jnt_orientConstraint1.tg[0].tw"
		;
connectAttr "curve1_jnt1_parentConstraint1.ctx" "curve1_jnt1.tx";
connectAttr "curve1_jnt1_parentConstraint1.cty" "curve1_jnt1.ty";
connectAttr "curve1_jnt1_parentConstraint1.ctz" "curve1_jnt1.tz";
connectAttr "curve1_jnt1_parentConstraint1.crx" "curve1_jnt1.rx";
connectAttr "curve1_jnt1_parentConstraint1.cry" "curve1_jnt1.ry";
connectAttr "curve1_jnt1_parentConstraint1.crz" "curve1_jnt1.rz";
connectAttr "curve1_jnt1.ro" "curve1_jnt1_parentConstraint1.cro";
connectAttr "curve1_jnt1.pim" "curve1_jnt1_parentConstraint1.cpim";
connectAttr "curve1_jnt1.rp" "curve1_jnt1_parentConstraint1.crp";
connectAttr "curve1_jnt1.rpt" "curve1_jnt1_parentConstraint1.crt";
connectAttr "curve1_jnt1.jo" "curve1_jnt1_parentConstraint1.cjo";
connectAttr "curve1_jnt.t" "curve1_jnt1_parentConstraint1.tg[0].tt";
connectAttr "curve1_jnt.rp" "curve1_jnt1_parentConstraint1.tg[0].trp";
connectAttr "curve1_jnt.rpt" "curve1_jnt1_parentConstraint1.tg[0].trt";
connectAttr "curve1_jnt.r" "curve1_jnt1_parentConstraint1.tg[0].tr";
connectAttr "curve1_jnt.ro" "curve1_jnt1_parentConstraint1.tg[0].tro";
connectAttr "curve1_jnt.s" "curve1_jnt1_parentConstraint1.tg[0].ts";
connectAttr "curve1_jnt.pm" "curve1_jnt1_parentConstraint1.tg[0].tpm";
connectAttr "curve1_jnt.jo" "curve1_jnt1_parentConstraint1.tg[0].tjo";
connectAttr "curve1_jnt.ssc" "curve1_jnt1_parentConstraint1.tg[0].tsc";
connectAttr "curve1_jnt.is" "curve1_jnt1_parentConstraint1.tg[0].tis";
connectAttr "curve1_jnt1_parentConstraint1.w0" "curve1_jnt1_parentConstraint1.tg[0].tw"
		;
connectAttr "curve2_jnt1_parentConstraint1.ctx" "curve2_jnt1.tx";
connectAttr "curve2_jnt1_parentConstraint1.cty" "curve2_jnt1.ty";
connectAttr "curve2_jnt1_parentConstraint1.ctz" "curve2_jnt1.tz";
connectAttr "curve2_jnt1_parentConstraint1.crx" "curve2_jnt1.rx";
connectAttr "curve2_jnt1_parentConstraint1.cry" "curve2_jnt1.ry";
connectAttr "curve2_jnt1_parentConstraint1.crz" "curve2_jnt1.rz";
connectAttr "curve2_jnt1.ro" "curve2_jnt1_parentConstraint1.cro";
connectAttr "curve2_jnt1.pim" "curve2_jnt1_parentConstraint1.cpim";
connectAttr "curve2_jnt1.rp" "curve2_jnt1_parentConstraint1.crp";
connectAttr "curve2_jnt1.rpt" "curve2_jnt1_parentConstraint1.crt";
connectAttr "curve2_jnt1.jo" "curve2_jnt1_parentConstraint1.cjo";
connectAttr "curve2_jnt.t" "curve2_jnt1_parentConstraint1.tg[0].tt";
connectAttr "curve2_jnt.rp" "curve2_jnt1_parentConstraint1.tg[0].trp";
connectAttr "curve2_jnt.rpt" "curve2_jnt1_parentConstraint1.tg[0].trt";
connectAttr "curve2_jnt.r" "curve2_jnt1_parentConstraint1.tg[0].tr";
connectAttr "curve2_jnt.ro" "curve2_jnt1_parentConstraint1.tg[0].tro";
connectAttr "curve2_jnt.s" "curve2_jnt1_parentConstraint1.tg[0].ts";
connectAttr "curve2_jnt.pm" "curve2_jnt1_parentConstraint1.tg[0].tpm";
connectAttr "curve2_jnt.jo" "curve2_jnt1_parentConstraint1.tg[0].tjo";
connectAttr "curve2_jnt.ssc" "curve2_jnt1_parentConstraint1.tg[0].tsc";
connectAttr "curve2_jnt.is" "curve2_jnt1_parentConstraint1.tg[0].tis";
connectAttr "curve2_jnt1_parentConstraint1.w0" "curve2_jnt1_parentConstraint1.tg[0].tw"
		;
connectAttr "curve3_jnt1_parentConstraint1.ctx" "curve3_jnt1.tx";
connectAttr "curve3_jnt1_parentConstraint1.cty" "curve3_jnt1.ty";
connectAttr "curve3_jnt1_parentConstraint1.ctz" "curve3_jnt1.tz";
connectAttr "curve3_jnt1_parentConstraint1.crx" "curve3_jnt1.rx";
connectAttr "curve3_jnt1_parentConstraint1.cry" "curve3_jnt1.ry";
connectAttr "curve3_jnt1_parentConstraint1.crz" "curve3_jnt1.rz";
connectAttr "curve3_jnt1.ro" "curve3_jnt1_parentConstraint1.cro";
connectAttr "curve3_jnt1.pim" "curve3_jnt1_parentConstraint1.cpim";
connectAttr "curve3_jnt1.rp" "curve3_jnt1_parentConstraint1.crp";
connectAttr "curve3_jnt1.rpt" "curve3_jnt1_parentConstraint1.crt";
connectAttr "curve3_jnt1.jo" "curve3_jnt1_parentConstraint1.cjo";
connectAttr "curve3_jnt.t" "curve3_jnt1_parentConstraint1.tg[0].tt";
connectAttr "curve3_jnt.rp" "curve3_jnt1_parentConstraint1.tg[0].trp";
connectAttr "curve3_jnt.rpt" "curve3_jnt1_parentConstraint1.tg[0].trt";
connectAttr "curve3_jnt.r" "curve3_jnt1_parentConstraint1.tg[0].tr";
connectAttr "curve3_jnt.ro" "curve3_jnt1_parentConstraint1.tg[0].tro";
connectAttr "curve3_jnt.s" "curve3_jnt1_parentConstraint1.tg[0].ts";
connectAttr "curve3_jnt.pm" "curve3_jnt1_parentConstraint1.tg[0].tpm";
connectAttr "curve3_jnt.jo" "curve3_jnt1_parentConstraint1.tg[0].tjo";
connectAttr "curve3_jnt.ssc" "curve3_jnt1_parentConstraint1.tg[0].tsc";
connectAttr "curve3_jnt.is" "curve3_jnt1_parentConstraint1.tg[0].tis";
connectAttr "curve3_jnt1_parentConstraint1.w0" "curve3_jnt1_parentConstraint1.tg[0].tw"
		;
connectAttr "curve4_jnt1_parentConstraint1.ctx" "curve4_jnt1.tx";
connectAttr "curve4_jnt1_parentConstraint1.cty" "curve4_jnt1.ty";
connectAttr "curve4_jnt1_parentConstraint1.ctz" "curve4_jnt1.tz";
connectAttr "curve4_jnt1_parentConstraint1.crx" "curve4_jnt1.rx";
connectAttr "curve4_jnt1_parentConstraint1.cry" "curve4_jnt1.ry";
connectAttr "curve4_jnt1_parentConstraint1.crz" "curve4_jnt1.rz";
connectAttr "curve4_jnt1.ro" "curve4_jnt1_parentConstraint1.cro";
connectAttr "curve4_jnt1.pim" "curve4_jnt1_parentConstraint1.cpim";
connectAttr "curve4_jnt1.rp" "curve4_jnt1_parentConstraint1.crp";
connectAttr "curve4_jnt1.rpt" "curve4_jnt1_parentConstraint1.crt";
connectAttr "curve4_jnt1.jo" "curve4_jnt1_parentConstraint1.cjo";
connectAttr "curve4_jnt.t" "curve4_jnt1_parentConstraint1.tg[0].tt";
connectAttr "curve4_jnt.rp" "curve4_jnt1_parentConstraint1.tg[0].trp";
connectAttr "curve4_jnt.rpt" "curve4_jnt1_parentConstraint1.tg[0].trt";
connectAttr "curve4_jnt.r" "curve4_jnt1_parentConstraint1.tg[0].tr";
connectAttr "curve4_jnt.ro" "curve4_jnt1_parentConstraint1.tg[0].tro";
connectAttr "curve4_jnt.s" "curve4_jnt1_parentConstraint1.tg[0].ts";
connectAttr "curve4_jnt.pm" "curve4_jnt1_parentConstraint1.tg[0].tpm";
connectAttr "curve4_jnt.jo" "curve4_jnt1_parentConstraint1.tg[0].tjo";
connectAttr "curve4_jnt.ssc" "curve4_jnt1_parentConstraint1.tg[0].tsc";
connectAttr "curve4_jnt.is" "curve4_jnt1_parentConstraint1.tg[0].tis";
connectAttr "curve4_jnt1_parentConstraint1.w0" "curve4_jnt1_parentConstraint1.tg[0].tw"
		;
connectAttr "curve5_jnt1_parentConstraint1.ctx" "curve5_jnt1.tx";
connectAttr "curve5_jnt1_parentConstraint1.cty" "curve5_jnt1.ty";
connectAttr "curve5_jnt1_parentConstraint1.ctz" "curve5_jnt1.tz";
connectAttr "curve5_jnt1_parentConstraint1.crx" "curve5_jnt1.rx";
connectAttr "curve5_jnt1_parentConstraint1.cry" "curve5_jnt1.ry";
connectAttr "curve5_jnt1_parentConstraint1.crz" "curve5_jnt1.rz";
connectAttr "curve5_jnt1.ro" "curve5_jnt1_parentConstraint1.cro";
connectAttr "curve5_jnt1.pim" "curve5_jnt1_parentConstraint1.cpim";
connectAttr "curve5_jnt1.rp" "curve5_jnt1_parentConstraint1.crp";
connectAttr "curve5_jnt1.rpt" "curve5_jnt1_parentConstraint1.crt";
connectAttr "curve5_jnt1.jo" "curve5_jnt1_parentConstraint1.cjo";
connectAttr "curve5_jnt.t" "curve5_jnt1_parentConstraint1.tg[0].tt";
connectAttr "curve5_jnt.rp" "curve5_jnt1_parentConstraint1.tg[0].trp";
connectAttr "curve5_jnt.rpt" "curve5_jnt1_parentConstraint1.tg[0].trt";
connectAttr "curve5_jnt.r" "curve5_jnt1_parentConstraint1.tg[0].tr";
connectAttr "curve5_jnt.ro" "curve5_jnt1_parentConstraint1.tg[0].tro";
connectAttr "curve5_jnt.s" "curve5_jnt1_parentConstraint1.tg[0].ts";
connectAttr "curve5_jnt.pm" "curve5_jnt1_parentConstraint1.tg[0].tpm";
connectAttr "curve5_jnt.jo" "curve5_jnt1_parentConstraint1.tg[0].tjo";
connectAttr "curve5_jnt.ssc" "curve5_jnt1_parentConstraint1.tg[0].tsc";
connectAttr "curve5_jnt.is" "curve5_jnt1_parentConstraint1.tg[0].tis";
connectAttr "curve5_jnt1_parentConstraint1.w0" "curve5_jnt1_parentConstraint1.tg[0].tw"
		;
connectAttr "curve6_jnt1_parentConstraint1.ctx" "curve6_jnt1.tx";
connectAttr "curve6_jnt1_parentConstraint1.cty" "curve6_jnt1.ty";
connectAttr "curve6_jnt1_parentConstraint1.ctz" "curve6_jnt1.tz";
connectAttr "curve6_jnt1_parentConstraint1.crx" "curve6_jnt1.rx";
connectAttr "curve6_jnt1_parentConstraint1.cry" "curve6_jnt1.ry";
connectAttr "curve6_jnt1_parentConstraint1.crz" "curve6_jnt1.rz";
connectAttr "curve6_jnt1.ro" "curve6_jnt1_parentConstraint1.cro";
connectAttr "curve6_jnt1.pim" "curve6_jnt1_parentConstraint1.cpim";
connectAttr "curve6_jnt1.rp" "curve6_jnt1_parentConstraint1.crp";
connectAttr "curve6_jnt1.rpt" "curve6_jnt1_parentConstraint1.crt";
connectAttr "curve6_jnt1.jo" "curve6_jnt1_parentConstraint1.cjo";
connectAttr "curve6_jnt.t" "curve6_jnt1_parentConstraint1.tg[0].tt";
connectAttr "curve6_jnt.rp" "curve6_jnt1_parentConstraint1.tg[0].trp";
connectAttr "curve6_jnt.rpt" "curve6_jnt1_parentConstraint1.tg[0].trt";
connectAttr "curve6_jnt.r" "curve6_jnt1_parentConstraint1.tg[0].tr";
connectAttr "curve6_jnt.ro" "curve6_jnt1_parentConstraint1.tg[0].tro";
connectAttr "curve6_jnt.s" "curve6_jnt1_parentConstraint1.tg[0].ts";
connectAttr "curve6_jnt.pm" "curve6_jnt1_parentConstraint1.tg[0].tpm";
connectAttr "curve6_jnt.jo" "curve6_jnt1_parentConstraint1.tg[0].tjo";
connectAttr "curve6_jnt.ssc" "curve6_jnt1_parentConstraint1.tg[0].tsc";
connectAttr "curve6_jnt.is" "curve6_jnt1_parentConstraint1.tg[0].tis";
connectAttr "curve6_jnt1_parentConstraint1.w0" "curve6_jnt1_parentConstraint1.tg[0].tw"
		;
connectAttr "curve7_jnt1_parentConstraint1.ctx" "curve7_jnt1.tx";
connectAttr "curve7_jnt1_parentConstraint1.cty" "curve7_jnt1.ty";
connectAttr "curve7_jnt1_parentConstraint1.ctz" "curve7_jnt1.tz";
connectAttr "curve7_jnt1_parentConstraint1.crx" "curve7_jnt1.rx";
connectAttr "curve7_jnt1_parentConstraint1.cry" "curve7_jnt1.ry";
connectAttr "curve7_jnt1_parentConstraint1.crz" "curve7_jnt1.rz";
connectAttr "curve7_jnt1.ro" "curve7_jnt1_parentConstraint1.cro";
connectAttr "curve7_jnt1.pim" "curve7_jnt1_parentConstraint1.cpim";
connectAttr "curve7_jnt1.rp" "curve7_jnt1_parentConstraint1.crp";
connectAttr "curve7_jnt1.rpt" "curve7_jnt1_parentConstraint1.crt";
connectAttr "curve7_jnt1.jo" "curve7_jnt1_parentConstraint1.cjo";
connectAttr "curve7_jnt.t" "curve7_jnt1_parentConstraint1.tg[0].tt";
connectAttr "curve7_jnt.rp" "curve7_jnt1_parentConstraint1.tg[0].trp";
connectAttr "curve7_jnt.rpt" "curve7_jnt1_parentConstraint1.tg[0].trt";
connectAttr "curve7_jnt.r" "curve7_jnt1_parentConstraint1.tg[0].tr";
connectAttr "curve7_jnt.ro" "curve7_jnt1_parentConstraint1.tg[0].tro";
connectAttr "curve7_jnt.s" "curve7_jnt1_parentConstraint1.tg[0].ts";
connectAttr "curve7_jnt.pm" "curve7_jnt1_parentConstraint1.tg[0].tpm";
connectAttr "curve7_jnt.jo" "curve7_jnt1_parentConstraint1.tg[0].tjo";
connectAttr "curve7_jnt.ssc" "curve7_jnt1_parentConstraint1.tg[0].tsc";
connectAttr "curve7_jnt.is" "curve7_jnt1_parentConstraint1.tg[0].tis";
connectAttr "curve7_jnt1_parentConstraint1.w0" "curve7_jnt1_parentConstraint1.tg[0].tw"
		;
connectAttr "curve8_jnt1_parentConstraint1.ctx" "curve8_jnt1.tx";
connectAttr "curve8_jnt1_parentConstraint1.cty" "curve8_jnt1.ty";
connectAttr "curve8_jnt1_parentConstraint1.ctz" "curve8_jnt1.tz";
connectAttr "curve8_jnt1_parentConstraint1.crx" "curve8_jnt1.rx";
connectAttr "curve8_jnt1_parentConstraint1.cry" "curve8_jnt1.ry";
connectAttr "curve8_jnt1_parentConstraint1.crz" "curve8_jnt1.rz";
connectAttr "curve8_jnt1.ro" "curve8_jnt1_parentConstraint1.cro";
connectAttr "curve8_jnt1.pim" "curve8_jnt1_parentConstraint1.cpim";
connectAttr "curve8_jnt1.rp" "curve8_jnt1_parentConstraint1.crp";
connectAttr "curve8_jnt1.rpt" "curve8_jnt1_parentConstraint1.crt";
connectAttr "curve8_jnt1.jo" "curve8_jnt1_parentConstraint1.cjo";
connectAttr "curve8_jnt.t" "curve8_jnt1_parentConstraint1.tg[0].tt";
connectAttr "curve8_jnt.rp" "curve8_jnt1_parentConstraint1.tg[0].trp";
connectAttr "curve8_jnt.rpt" "curve8_jnt1_parentConstraint1.tg[0].trt";
connectAttr "curve8_jnt.r" "curve8_jnt1_parentConstraint1.tg[0].tr";
connectAttr "curve8_jnt.ro" "curve8_jnt1_parentConstraint1.tg[0].tro";
connectAttr "curve8_jnt.s" "curve8_jnt1_parentConstraint1.tg[0].ts";
connectAttr "curve8_jnt.pm" "curve8_jnt1_parentConstraint1.tg[0].tpm";
connectAttr "curve8_jnt.jo" "curve8_jnt1_parentConstraint1.tg[0].tjo";
connectAttr "curve8_jnt.ssc" "curve8_jnt1_parentConstraint1.tg[0].tsc";
connectAttr "curve8_jnt.is" "curve8_jnt1_parentConstraint1.tg[0].tis";
connectAttr "curve8_jnt1_parentConstraint1.w0" "curve8_jnt1_parentConstraint1.tg[0].tw"
		;
connectAttr "Shoulder.msg" "ikHandle_Hand.hsj";
connectAttr "effector1.hp" "ikHandle_Hand.hee";
connectAttr "ikRPsolver.msg" "ikHandle_Hand.hsv";
connectAttr "ikHandle_Hand_poleVectorConstraint1.ctx" "ikHandle_Hand.pvx";
connectAttr "ikHandle_Hand_poleVectorConstraint1.cty" "ikHandle_Hand.pvy";
connectAttr "ikHandle_Hand_poleVectorConstraint1.ctz" "ikHandle_Hand.pvz";
connectAttr "ikHandle_Hand.pim" "ikHandle_Hand_poleVectorConstraint1.cpim";
connectAttr "Shoulder.pm" "ikHandle_Hand_poleVectorConstraint1.ps";
connectAttr "Shoulder.t" "ikHandle_Hand_poleVectorConstraint1.crp";
connectAttr "Elbow_Ctrl.t" "ikHandle_Hand_poleVectorConstraint1.tg[0].tt";
connectAttr "Elbow_Ctrl.rp" "ikHandle_Hand_poleVectorConstraint1.tg[0].trp";
connectAttr "Elbow_Ctrl.rpt" "ikHandle_Hand_poleVectorConstraint1.tg[0].trt";
connectAttr "Elbow_Ctrl.pm" "ikHandle_Hand_poleVectorConstraint1.tg[0].tpm";
connectAttr "ikHandle_Hand_poleVectorConstraint1.w0" "ikHandle_Hand_poleVectorConstraint1.tg[0].tw"
		;
connectAttr "locator1_pointConstraint1.ctx" "locator1.tx";
connectAttr "locator1_pointConstraint1.cty" "locator1.ty";
connectAttr "locator1_pointConstraint1.ctz" "locator1.tz";
connectAttr "locator1.pim" "locator1_pointConstraint1.cpim";
connectAttr "locator1.rp" "locator1_pointConstraint1.crp";
connectAttr "locator1.rpt" "locator1_pointConstraint1.crt";
connectAttr "Shoulder.t" "locator1_pointConstraint1.tg[0].tt";
connectAttr "Shoulder.rp" "locator1_pointConstraint1.tg[0].trp";
connectAttr "Shoulder.rpt" "locator1_pointConstraint1.tg[0].trt";
connectAttr "Shoulder.pm" "locator1_pointConstraint1.tg[0].tpm";
connectAttr "locator1_pointConstraint1.w0" "locator1_pointConstraint1.tg[0].tw";
connectAttr "locator2_pointConstraint1.ctx" "locator2.tx";
connectAttr "locator2_pointConstraint1.cty" "locator2.ty";
connectAttr "locator2_pointConstraint1.ctz" "locator2.tz";
connectAttr "locator2.pim" "locator2_pointConstraint1.cpim";
connectAttr "locator2.rp" "locator2_pointConstraint1.crp";
connectAttr "locator2.rpt" "locator2_pointConstraint1.crt";
connectAttr "Wrist_Ctrl.t" "locator2_pointConstraint1.tg[0].tt";
connectAttr "Wrist_Ctrl.rp" "locator2_pointConstraint1.tg[0].trp";
connectAttr "Wrist_Ctrl.rpt" "locator2_pointConstraint1.tg[0].trt";
connectAttr "Wrist_Ctrl.pm" "locator2_pointConstraint1.tg[0].tpm";
connectAttr "locator2_pointConstraint1.w0" "locator2_pointConstraint1.tg[0].tw";
connectAttr "locatorShape1.wp" "distanceDimensionShape1.sp";
connectAttr "locatorShape2.wp" "distanceDimensionShape1.ep";
connectAttr "Elbow_grp_parentConstraint1.ctx" "Elbow_grp.tx";
connectAttr "Elbow_grp_parentConstraint1.cty" "Elbow_grp.ty";
connectAttr "Elbow_grp_parentConstraint1.ctz" "Elbow_grp.tz";
connectAttr "Elbow_grp_parentConstraint1.crx" "Elbow_grp.rx";
connectAttr "Elbow_grp_parentConstraint1.cry" "Elbow_grp.ry";
connectAttr "Elbow_grp_parentConstraint1.crz" "Elbow_grp.rz";
connectAttr "Elbow_grp.ro" "Elbow_grp_parentConstraint1.cro";
connectAttr "Elbow_grp.pim" "Elbow_grp_parentConstraint1.cpim";
connectAttr "Elbow_grp.rp" "Elbow_grp_parentConstraint1.crp";
connectAttr "Elbow_grp.rpt" "Elbow_grp_parentConstraint1.crt";
connectAttr "Wrist_Ctrl.t" "Elbow_grp_parentConstraint1.tg[0].tt";
connectAttr "Wrist_Ctrl.rp" "Elbow_grp_parentConstraint1.tg[0].trp";
connectAttr "Wrist_Ctrl.rpt" "Elbow_grp_parentConstraint1.tg[0].trt";
connectAttr "Wrist_Ctrl.r" "Elbow_grp_parentConstraint1.tg[0].tr";
connectAttr "Wrist_Ctrl.ro" "Elbow_grp_parentConstraint1.tg[0].tro";
connectAttr "Wrist_Ctrl.s" "Elbow_grp_parentConstraint1.tg[0].ts";
connectAttr "Wrist_Ctrl.pm" "Elbow_grp_parentConstraint1.tg[0].tpm";
connectAttr "Elbow_grp_parentConstraint1.w0" "Elbow_grp_parentConstraint1.tg[0].tw"
		;
connectAttr "joint25_parentConstraint1.ctx" "joint25.tx";
connectAttr "joint25_parentConstraint1.cty" "joint25.ty";
connectAttr "joint25_parentConstraint1.ctz" "joint25.tz";
connectAttr "joint25_aimConstraint1.crx" "joint25.rx";
connectAttr "joint25_aimConstraint1.cry" "joint25.ry";
connectAttr "joint25_aimConstraint1.crz" "joint25.rz";
connectAttr "joint25.ro" "joint25_parentConstraint1.cro";
connectAttr "joint25.pim" "joint25_parentConstraint1.cpim";
connectAttr "joint25.rp" "joint25_parentConstraint1.crp";
connectAttr "joint25.rpt" "joint25_parentConstraint1.crt";
connectAttr "joint25.jo" "joint25_parentConstraint1.cjo";
connectAttr "Shoulder.t" "joint25_parentConstraint1.tg[0].tt";
connectAttr "Shoulder.rp" "joint25_parentConstraint1.tg[0].trp";
connectAttr "Shoulder.rpt" "joint25_parentConstraint1.tg[0].trt";
connectAttr "Shoulder.r" "joint25_parentConstraint1.tg[0].tr";
connectAttr "Shoulder.ro" "joint25_parentConstraint1.tg[0].tro";
connectAttr "Shoulder.s" "joint25_parentConstraint1.tg[0].ts";
connectAttr "Shoulder.pm" "joint25_parentConstraint1.tg[0].tpm";
connectAttr "Shoulder.jo" "joint25_parentConstraint1.tg[0].tjo";
connectAttr "Shoulder.ssc" "joint25_parentConstraint1.tg[0].tsc";
connectAttr "Shoulder.is" "joint25_parentConstraint1.tg[0].tis";
connectAttr "joint25_parentConstraint1.w0" "joint25_parentConstraint1.tg[0].tw";
connectAttr "Elbow.t" "joint25_parentConstraint1.tg[1].tt";
connectAttr "Elbow.rp" "joint25_parentConstraint1.tg[1].trp";
connectAttr "Elbow.rpt" "joint25_parentConstraint1.tg[1].trt";
connectAttr "Elbow.r" "joint25_parentConstraint1.tg[1].tr";
connectAttr "Elbow.ro" "joint25_parentConstraint1.tg[1].tro";
connectAttr "Elbow.s" "joint25_parentConstraint1.tg[1].ts";
connectAttr "Elbow.pm" "joint25_parentConstraint1.tg[1].tpm";
connectAttr "Elbow.jo" "joint25_parentConstraint1.tg[1].tjo";
connectAttr "Elbow.ssc" "joint25_parentConstraint1.tg[1].tsc";
connectAttr "Elbow.is" "joint25_parentConstraint1.tg[1].tis";
connectAttr "joint25_parentConstraint1.w1" "joint25_parentConstraint1.tg[1].tw";
connectAttr "joint25.pim" "joint25_aimConstraint1.cpim";
connectAttr "joint25.t" "joint25_aimConstraint1.ct";
connectAttr "joint25.rp" "joint25_aimConstraint1.crp";
connectAttr "joint25.rpt" "joint25_aimConstraint1.crt";
connectAttr "joint25.ro" "joint25_aimConstraint1.cro";
connectAttr "joint25.jo" "joint25_aimConstraint1.cjo";
connectAttr "joint25.is" "joint25_aimConstraint1.is";
connectAttr "Elbow.t" "joint25_aimConstraint1.tg[0].tt";
connectAttr "Elbow.rp" "joint25_aimConstraint1.tg[0].trp";
connectAttr "Elbow.rpt" "joint25_aimConstraint1.tg[0].trt";
connectAttr "Elbow.pm" "joint25_aimConstraint1.tg[0].tpm";
connectAttr "joint25_aimConstraint1.w0" "joint25_aimConstraint1.tg[0].tw";
connectAttr "Shoulder.t" "joint25_aimConstraint1.tg[1].tt";
connectAttr "Shoulder.rp" "joint25_aimConstraint1.tg[1].trp";
connectAttr "Shoulder.rpt" "joint25_aimConstraint1.tg[1].trt";
connectAttr "Shoulder.pm" "joint25_aimConstraint1.tg[1].tpm";
connectAttr "joint25_aimConstraint1.w1" "joint25_aimConstraint1.tg[1].tw";
connectAttr "joint26_parentConstraint1.ctx" "joint26.tx";
connectAttr "joint26_parentConstraint1.cty" "joint26.ty";
connectAttr "joint26_parentConstraint1.ctz" "joint26.tz";
connectAttr "joint26_aimConstraint1.crx" "joint26.rx";
connectAttr "joint26_aimConstraint1.cry" "joint26.ry";
connectAttr "joint26_aimConstraint1.crz" "joint26.rz";
connectAttr "joint26.ro" "joint26_parentConstraint1.cro";
connectAttr "joint26.pim" "joint26_parentConstraint1.cpim";
connectAttr "joint26.rp" "joint26_parentConstraint1.crp";
connectAttr "joint26.rpt" "joint26_parentConstraint1.crt";
connectAttr "joint26.jo" "joint26_parentConstraint1.cjo";
connectAttr "Elbow.t" "joint26_parentConstraint1.tg[0].tt";
connectAttr "Elbow.rp" "joint26_parentConstraint1.tg[0].trp";
connectAttr "Elbow.rpt" "joint26_parentConstraint1.tg[0].trt";
connectAttr "Elbow.r" "joint26_parentConstraint1.tg[0].tr";
connectAttr "Elbow.ro" "joint26_parentConstraint1.tg[0].tro";
connectAttr "Elbow.s" "joint26_parentConstraint1.tg[0].ts";
connectAttr "Elbow.pm" "joint26_parentConstraint1.tg[0].tpm";
connectAttr "Elbow.jo" "joint26_parentConstraint1.tg[0].tjo";
connectAttr "Elbow.ssc" "joint26_parentConstraint1.tg[0].tsc";
connectAttr "Elbow.is" "joint26_parentConstraint1.tg[0].tis";
connectAttr "joint26_parentConstraint1.w0" "joint26_parentConstraint1.tg[0].tw";
connectAttr "Wrist.t" "joint26_parentConstraint1.tg[1].tt";
connectAttr "Wrist.rp" "joint26_parentConstraint1.tg[1].trp";
connectAttr "Wrist.rpt" "joint26_parentConstraint1.tg[1].trt";
connectAttr "Wrist.r" "joint26_parentConstraint1.tg[1].tr";
connectAttr "Wrist.ro" "joint26_parentConstraint1.tg[1].tro";
connectAttr "Wrist.s" "joint26_parentConstraint1.tg[1].ts";
connectAttr "Wrist.pm" "joint26_parentConstraint1.tg[1].tpm";
connectAttr "Wrist.jo" "joint26_parentConstraint1.tg[1].tjo";
connectAttr "Wrist.ssc" "joint26_parentConstraint1.tg[1].tsc";
connectAttr "Wrist.is" "joint26_parentConstraint1.tg[1].tis";
connectAttr "joint26_parentConstraint1.w1" "joint26_parentConstraint1.tg[1].tw";
connectAttr "joint26.pim" "joint26_aimConstraint1.cpim";
connectAttr "joint26.t" "joint26_aimConstraint1.ct";
connectAttr "joint26.rp" "joint26_aimConstraint1.crp";
connectAttr "joint26.rpt" "joint26_aimConstraint1.crt";
connectAttr "joint26.ro" "joint26_aimConstraint1.cro";
connectAttr "joint26.jo" "joint26_aimConstraint1.cjo";
connectAttr "joint26.is" "joint26_aimConstraint1.is";
connectAttr "Wrist.t" "joint26_aimConstraint1.tg[0].tt";
connectAttr "Wrist.rp" "joint26_aimConstraint1.tg[0].trp";
connectAttr "Wrist.rpt" "joint26_aimConstraint1.tg[0].trt";
connectAttr "Wrist.pm" "joint26_aimConstraint1.tg[0].tpm";
connectAttr "joint26_aimConstraint1.w0" "joint26_aimConstraint1.tg[0].tw";
connectAttr "Elbow.t" "joint26_aimConstraint1.tg[1].tt";
connectAttr "Elbow.rp" "joint26_aimConstraint1.tg[1].trp";
connectAttr "Elbow.rpt" "joint26_aimConstraint1.tg[1].trt";
connectAttr "Elbow.pm" "joint26_aimConstraint1.tg[1].tpm";
connectAttr "joint26_aimConstraint1.w1" "joint26_aimConstraint1.tg[1].tw";
relationship "link" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
connectAttr "layerManager.dli[0]" "defaultLayer.id";
connectAttr "renderLayerManager.rlmi[0]" "defaultRenderLayer.rlid";
connectAttr "groupParts2.og" "tweak1.ip[0].ig";
connectAttr "groupId2.id" "tweak1.ip[0].gi";
connectAttr "groupId2.msg" "tweakSet1.gn" -na;
connectAttr "loftedSurfaceShape1.iog.og[1]" "tweakSet1.dsm" -na;
connectAttr "tweak1.msg" "tweakSet1.ub[0]";
connectAttr "loftedSurfaceShape1Orig.ws" "groupParts2.ig";
connectAttr "groupId2.id" "groupParts2.gi";
connectAttr "condition1.ocr" "multiplyDivide1.i1x";
connectAttr "aTools_StoreNode.o" "scene.m";
connectAttr "distanceDimensionShape1.dist" "condition1.st";
connectAttr "distanceDimensionShape1.dist" "condition1.cfr";
connectAttr "unitConversion23.o" "curve6_jnt_orientConstraint1_bc.c1g";
connectAttr "unitConversion24.o" "curve6_jnt_orientConstraint1_bc.c1b";
connectAttr "unitConversion25.o" "curve6_jnt_orientConstraint1_bc.c1r";
connectAttr "unitConversion57.o" "curve6_jnt_orientConstraint1_bc.c2r";
connectAttr "unitConversion65.o" "curve6_jnt_orientConstraint1_bc.c2g";
connectAttr "unitConversion73.o" "curve6_jnt_orientConstraint1_bc.c2b";
connectAttr "unitConversion2.o" "curve3_jnt_orientConstraint1_bc.c1r";
connectAttr "unitConversion3.o" "curve3_jnt_orientConstraint1_bc.c1g";
connectAttr "unitConversion4.o" "curve3_jnt_orientConstraint1_bc.c1b";
connectAttr "unitConversion52.o" "curve3_jnt_orientConstraint1_bc.c2r";
connectAttr "unitConversion60.o" "curve3_jnt_orientConstraint1_bc.c2g";
connectAttr "unitConversion68.o" "curve3_jnt_orientConstraint1_bc.c2b";
connectAttr "curve3_jnt_orientConstraint1.crx" "unitConversion2.i";
connectAttr "curve3_jnt_orientConstraint1.cry" "unitConversion3.i";
connectAttr "curve3_jnt_orientConstraint1.crz" "unitConversion4.i";
connectAttr "unitConversion5.o" "curve7_jnt_orientConstraint1_bc.c1r";
connectAttr "unitConversion6.o" "curve7_jnt_orientConstraint1_bc.c1g";
connectAttr "unitConversion7.o" "curve7_jnt_orientConstraint1_bc.c1b";
connectAttr "unitConversion53.o" "curve7_jnt_orientConstraint1_bc.c2r";
connectAttr "unitConversion61.o" "curve7_jnt_orientConstraint1_bc.c2g";
connectAttr "unitConversion69.o" "curve7_jnt_orientConstraint1_bc.c2b";
connectAttr "curve7_jnt_orientConstraint1.crx" "unitConversion5.i";
connectAttr "curve7_jnt_orientConstraint1.cry" "unitConversion6.i";
connectAttr "curve7_jnt_orientConstraint1.crz" "unitConversion7.i";
connectAttr "unitConversion8.o" "curve8_jnt_orientConstraint1_bc.c1r";
connectAttr "unitConversion9.o" "curve8_jnt_orientConstraint1_bc.c1g";
connectAttr "unitConversion10.o" "curve8_jnt_orientConstraint1_bc.c1b";
connectAttr "unitConversion50.o" "curve8_jnt_orientConstraint1_bc.c2r";
connectAttr "unitConversion58.o" "curve8_jnt_orientConstraint1_bc.c2g";
connectAttr "unitConversion66.o" "curve8_jnt_orientConstraint1_bc.c2b";
connectAttr "curve8_jnt_orientConstraint1.crx" "unitConversion8.i";
connectAttr "curve8_jnt_orientConstraint1.cry" "unitConversion9.i";
connectAttr "curve8_jnt_orientConstraint1.crz" "unitConversion10.i";
connectAttr "unitConversion11.o" "curve5_jnt_orientConstraint1_bc.c1r";
connectAttr "unitConversion12.o" "curve5_jnt_orientConstraint1_bc.c1g";
connectAttr "unitConversion13.o" "curve5_jnt_orientConstraint1_bc.c1b";
connectAttr "unitConversion55.o" "curve5_jnt_orientConstraint1_bc.c2r";
connectAttr "unitConversion63.o" "curve5_jnt_orientConstraint1_bc.c2g";
connectAttr "unitConversion71.o" "curve5_jnt_orientConstraint1_bc.c2b";
connectAttr "curve5_jnt_orientConstraint1.crx" "unitConversion11.i";
connectAttr "curve5_jnt_orientConstraint1.cry" "unitConversion12.i";
connectAttr "curve5_jnt_orientConstraint1.crz" "unitConversion13.i";
connectAttr "unitConversion14.o" "curve4_jnt_orientConstraint1_bc.c1r";
connectAttr "unitConversion15.o" "curve4_jnt_orientConstraint1_bc.c1g";
connectAttr "unitConversion16.o" "curve4_jnt_orientConstraint1_bc.c1b";
connectAttr "unitConversion56.o" "curve4_jnt_orientConstraint1_bc.c2r";
connectAttr "unitConversion64.o" "curve4_jnt_orientConstraint1_bc.c2g";
connectAttr "unitConversion72.o" "curve4_jnt_orientConstraint1_bc.c2b";
connectAttr "curve4_jnt_orientConstraint1.crx" "unitConversion14.i";
connectAttr "curve4_jnt_orientConstraint1.cry" "unitConversion15.i";
connectAttr "curve4_jnt_orientConstraint1.crz" "unitConversion16.i";
connectAttr "unitConversion17.o" "curve2_jnt_orientConstraint1_bc.c1r";
connectAttr "unitConversion18.o" "curve2_jnt_orientConstraint1_bc.c1g";
connectAttr "unitConversion19.o" "curve2_jnt_orientConstraint1_bc.c1b";
connectAttr "unitConversion54.o" "curve2_jnt_orientConstraint1_bc.c2r";
connectAttr "unitConversion62.o" "curve2_jnt_orientConstraint1_bc.c2g";
connectAttr "unitConversion70.o" "curve2_jnt_orientConstraint1_bc.c2b";
connectAttr "curve2_jnt_orientConstraint1.crx" "unitConversion17.i";
connectAttr "curve2_jnt_orientConstraint1.cry" "unitConversion18.i";
connectAttr "curve2_jnt_orientConstraint1.crz" "unitConversion19.i";
connectAttr "unitConversion20.o" "curve1_jnt_orientConstraint1_bc.c1r";
connectAttr "unitConversion21.o" "curve1_jnt_orientConstraint1_bc.c1g";
connectAttr "unitConversion22.o" "curve1_jnt_orientConstraint1_bc.c1b";
connectAttr "unitConversion59.o" "curve1_jnt_orientConstraint1_bc.c2g";
connectAttr "unitConversion67.o" "curve1_jnt_orientConstraint1_bc.c2b";
connectAttr "unitConversion51.o" "curve1_jnt_orientConstraint1_bc.c2r";
connectAttr "curve1_jnt_orientConstraint1.crx" "unitConversion20.i";
connectAttr "curve1_jnt_orientConstraint1.cry" "unitConversion21.i";
connectAttr "curve1_jnt_orientConstraint1.crz" "unitConversion22.i";
connectAttr "curve6_jnt_orientConstraint1.cry" "unitConversion23.i";
connectAttr "curve6_jnt_orientConstraint1.crz" "unitConversion24.i";
connectAttr "curve6_jnt_orientConstraint1.crx" "unitConversion25.i";
connectAttr "curve8_jnt_orientConstraint1_bc.opb" "unitConversion26.i";
connectAttr "curve4_jnt_orientConstraint1_bc.opb" "unitConversion27.i";
connectAttr "curve1_jnt_orientConstraint1_bc.opb" "unitConversion28.i";
connectAttr "curve2_jnt_orientConstraint1_bc.opb" "unitConversion29.i";
connectAttr "curve3_jnt_orientConstraint1_bc.opb" "unitConversion30.i";
connectAttr "curve5_jnt_orientConstraint1_bc.opb" "unitConversion31.i";
connectAttr "curve7_jnt_orientConstraint1_bc.opb" "unitConversion32.i";
connectAttr "curve6_jnt_orientConstraint1_bc.opb" "unitConversion33.i";
connectAttr "curve8_jnt_orientConstraint1_bc.opg" "unitConversion34.i";
connectAttr "curve4_jnt_orientConstraint1_bc.opg" "unitConversion35.i";
connectAttr "curve1_jnt_orientConstraint1_bc.opg" "unitConversion36.i";
connectAttr "curve2_jnt_orientConstraint1_bc.opg" "unitConversion37.i";
connectAttr "curve3_jnt_orientConstraint1_bc.opg" "unitConversion38.i";
connectAttr "curve5_jnt_orientConstraint1_bc.opg" "unitConversion39.i";
connectAttr "curve7_jnt_orientConstraint1_bc.opg" "unitConversion40.i";
connectAttr "curve6_jnt_orientConstraint1_bc.opg" "unitConversion41.i";
connectAttr "curve8_jnt_orientConstraint1_bc.opr" "unitConversion42.i";
connectAttr "curve4_jnt_orientConstraint1_bc.opr" "unitConversion43.i";
connectAttr "curve1_jnt_orientConstraint1_bc.opr" "unitConversion44.i";
connectAttr "curve2_jnt_orientConstraint1_bc.opr" "unitConversion45.i";
connectAttr "curve3_jnt_orientConstraint1_bc.opr" "unitConversion46.i";
connectAttr "curve5_jnt_orientConstraint1_bc.opr" "unitConversion47.i";
connectAttr "curve7_jnt_orientConstraint1_bc.opr" "unitConversion48.i";
connectAttr "curve6_jnt_orientConstraint1_bc.opr" "unitConversion49.i";
connectAttr "curve8_jnt_orientConstraint1.crx" "unitConversion50.i";
connectAttr "curve1_jnt_orientConstraint1.crx" "unitConversion51.i";
connectAttr "curve3_jnt_orientConstraint1.crx" "unitConversion52.i";
connectAttr "curve7_jnt_orientConstraint1.crx" "unitConversion53.i";
connectAttr "curve2_jnt_orientConstraint1.crx" "unitConversion54.i";
connectAttr "curve5_jnt_orientConstraint1.crx" "unitConversion55.i";
connectAttr "curve4_jnt_orientConstraint1.crx" "unitConversion56.i";
connectAttr "curve6_jnt_orientConstraint1.crx" "unitConversion57.i";
connectAttr "curve8_jnt_orientConstraint1.cry" "unitConversion58.i";
connectAttr "curve1_jnt_orientConstraint1.cry" "unitConversion59.i";
connectAttr "curve3_jnt_orientConstraint1.cry" "unitConversion60.i";
connectAttr "curve7_jnt_orientConstraint1.cry" "unitConversion61.i";
connectAttr "curve2_jnt_orientConstraint1.cry" "unitConversion62.i";
connectAttr "curve5_jnt_orientConstraint1.cry" "unitConversion63.i";
connectAttr "curve4_jnt_orientConstraint1.cry" "unitConversion64.i";
connectAttr "curve6_jnt_orientConstraint1.cry" "unitConversion65.i";
connectAttr "curve8_jnt_orientConstraint1.crz" "unitConversion66.i";
connectAttr "curve1_jnt_orientConstraint1.crz" "unitConversion67.i";
connectAttr "curve3_jnt_orientConstraint1.crz" "unitConversion68.i";
connectAttr "curve7_jnt_orientConstraint1.crz" "unitConversion69.i";
connectAttr "curve2_jnt_orientConstraint1.crz" "unitConversion70.i";
connectAttr "curve5_jnt_orientConstraint1.crz" "unitConversion71.i";
connectAttr "curve4_jnt_orientConstraint1.crz" "unitConversion72.i";
connectAttr "curve6_jnt_orientConstraint1.crz" "unitConversion73.i";
connectAttr "curve1_jnt_orientConstraint1_bc.opr" "curve1_jnt_orientConstraint1_bc_fm._fa"
		;
connectAttr "curve2_jnt_orientConstraint1_bc.opr" "curve2_jnt_orientConstraint1_bc_fm._fa"
		;
connectAttr "curve3_jnt_orientConstraint1_bc.opr" "curve3_jnt_orientConstraint1_bc_fm._fa"
		;
connectAttr "curve4_jnt_orientConstraint1_bc.opr" "curve4_jnt_orientConstraint1_bc_fm._fa"
		;
connectAttr "curve5_jnt_orientConstraint1_bc.opr" "curve5_jnt_orientConstraint1_bc_fm._fa"
		;
connectAttr "curve6_jnt_orientConstraint1_bc.opr" "curve6_jnt_orientConstraint1_bc_fm._fa"
		;
connectAttr "curve7_jnt_orientConstraint1_bc.opr" "curve7_jnt_orientConstraint1_bc_fm._fa"
		;
connectAttr "curve8_jnt_orientConstraint1_bc.opr" "curve8_jnt_orientConstraint1_bc_fm._fa"
		;
connectAttr "curve3_jnt_orientConstraint1_bc_fm.of" "unitConversion74.i";
connectAttr "curve4_jnt_orientConstraint1_bc_fm.of" "unitConversion75.i";
connectAttr "curve5_jnt_orientConstraint1_bc_fm.of" "unitConversion76.i";
connectAttr "curve6_jnt_orientConstraint1_bc_fm.of" "unitConversion77.i";
connectAttr "curve7_jnt_orientConstraint1_bc_fm.of" "unitConversion78.i";
connectAttr "curve8_jnt_orientConstraint1_bc_fm.of" "unitConversion79.i";
connectAttr "curve2_jnt_orientConstraint1_bc_fm.of" "unitConversion80.i";
connectAttr "curve1_jnt_orientConstraint1_bc_fm.of" "unitConversion81.i";
connectAttr "groupId4.msg" "tweakSet2.gn" -na;
connectAttr "loftedSurfaceShape2.iog.og[1]" "tweakSet2.dsm" -na;
connectAttr "tweak2.msg" "tweakSet2.ub[0]";
connectAttr "loftedSurfaceShape2Orig.ws" "groupParts4.ig";
connectAttr "groupId4.id" "groupParts4.gi";
connectAttr "groupParts4.og" "tweak2.ip[0].ig";
connectAttr "groupId4.id" "tweak2.ip[0].gi";
connectAttr "ikHandle_Hand.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[0].dn";
connectAttr "curve1_jnt.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[1].dn";
connectAttr "curve8_jnt.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[2].dn";
connectAttr "curve6_jnt.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[3].dn";
connectAttr "curve5_jnt.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[4].dn";
connectAttr "joint24_jnt_pointConstraint1.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[5].dn"
		;
connectAttr "curve2_jnt.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[6].dn";
connectAttr "joint23_jnt_aimConstraint1.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[7].dn"
		;
connectAttr "joint23_jnt.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[8].dn";
connectAttr "joint23_jnt_pointConstraint1.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[9].dn"
		;
connectAttr "Wrist_grp.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[10].dn";
connectAttr "curve4_jnt.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[11].dn";
connectAttr "joint24_jnt.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[12].dn";
connectAttr "joint24_jnt_aimConstraint1.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[13].dn"
		;
connectAttr "curve7_jnt.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[14].dn";
connectAttr "effector1.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[15].dn";
connectAttr "Wrist_Ctrl.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[16].dn";
connectAttr "group1.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[17].dn";
connectAttr "curveShape9.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[18].dn";
connectAttr "curve3_jnt.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[19].dn";
connectAttr "distanceDimensionShape1.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[0].dn"
		;
connectAttr "Elbow_grp.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[1].dn";
connectAttr "sceneConfigurationScriptNode.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[2].dn"
		;
connectAttr "locator1.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[3].dn";
connectAttr "Shoulder.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[4].dn";
connectAttr "locatorShape2.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[5].dn";
connectAttr "uiConfigurationScriptNode.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[6].dn"
		;
connectAttr "multiplyDivide1.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[7].dn";
connectAttr "distanceDimension1.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[8].dn"
		;
connectAttr "locator2_pointConstraint1.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[9].dn"
		;
connectAttr "aTools_StoreNode.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[10].dn"
		;
connectAttr "scene.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[11].dn";
connectAttr "condition1.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[12].dn";
connectAttr "locator1_pointConstraint1.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[13].dn"
		;
connectAttr "locator2.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[14].dn";
connectAttr "locatorShape1.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[15].dn";
connectAttr "Elbow.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[16].dn";
connectAttr "unitConversion43.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[0].dn"
		;
connectAttr "unitConversion26.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[1].dn"
		;
connectAttr "unitConversion49.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[2].dn"
		;
connectAttr "unitConversion69.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[3].dn"
		;
connectAttr "unitConversion19.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[4].dn"
		;
connectAttr "unitConversion17.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[5].dn"
		;
connectAttr "curve6_jnt_orientConstraint1_bc_fm.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[6].dn"
		;
connectAttr "curve4_jnt_orientConstraint1.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[7].dn"
		;
connectAttr "unitConversion46.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[8].dn"
		;
connectAttr "curve2_jnt_orientConstraint1_bc_fm.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[9].dn"
		;
connectAttr "unitConversion33.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[10].dn"
		;
connectAttr "unitConversion56.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[11].dn"
		;
connectAttr "unitConversion65.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[12].dn"
		;
connectAttr "curve4_jnt_orientConstraint1_bc_fm.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[13].dn"
		;
connectAttr "unitConversion22.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[14].dn"
		;
connectAttr "unitConversion71.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[15].dn"
		;
connectAttr "unitConversion11.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[16].dn"
		;
connectAttr "curve6.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[17].dn";
connectAttr "unitConversion53.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[18].dn"
		;
connectAttr "curve1_jnt.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[19].dn";
connectAttr "unitConversion4.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[20].dn"
		;
connectAttr "unitConversion32.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[21].dn"
		;
connectAttr "curve2_jnt.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[22].dn";
connectAttr "unitConversion60.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[23].dn"
		;
connectAttr "unitConversion55.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[24].dn"
		;
connectAttr "curve8_jnt.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[25].dn";
connectAttr "curve3_jnt_orientConstraint1.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[26].dn"
		;
connectAttr "unitConversion10.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[27].dn"
		;
connectAttr "curve7_jnt_orientConstraint1.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[28].dn"
		;
connectAttr "curve7_jnt_orientConstraint1_bc.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[29].dn"
		;
connectAttr "unitConversion2.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[30].dn"
		;
connectAttr "curve5_jnt_orientConstraint1_bc.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[31].dn"
		;
connectAttr "curve3_jnt_orientConstraint1_bc.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[32].dn"
		;
connectAttr "curve8.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[33].dn";
connectAttr "unitConversion6.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[34].dn"
		;
connectAttr "curve2_jnt_orientConstraint1_bc.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[35].dn"
		;
connectAttr "curve7.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[36].dn";
connectAttr "unitConversion8.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[37].dn"
		;
connectAttr "unitConversion31.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[38].dn"
		;
connectAttr "unitConversion63.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[39].dn"
		;
connectAttr "curve4_jnt_orientConstraint1_bc.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[40].dn"
		;
connectAttr "unitConversion59.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[41].dn"
		;
connectAttr "unitConversion14.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[42].dn"
		;
connectAttr "curve5.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[43].dn";
connectAttr "curve7_jnt_orientConstraint1_bc_fm.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[44].dn"
		;
connectAttr "unitConversion21.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[45].dn"
		;
connectAttr "unitConversion72.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[46].dn"
		;
connectAttr "curve1_jnt_orientConstraint1_bc.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[47].dn"
		;
connectAttr "unitConversion15.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[48].dn"
		;
connectAttr "curve8_jnt_orientConstraint1_bc.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[49].dn"
		;
connectAttr "curve3.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[50].dn";
connectAttr "unitConversion52.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[51].dn"
		;
connectAttr "unitConversion20.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[52].dn"
		;
connectAttr "unitConversion66.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[53].dn"
		;
connectAttr "unitConversion51.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[54].dn"
		;
connectAttr "curve6_jnt_orientConstraint1_bc.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[55].dn"
		;
connectAttr "unitConversion62.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[56].dn"
		;
connectAttr "unitConversion61.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[57].dn"
		;
connectAttr "unitConversion41.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[58].dn"
		;
connectAttr "curve8_jnt_orientConstraint1_bc_fm.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[59].dn"
		;
connectAttr "unitConversion39.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[60].dn"
		;
connectAttr "unitConversion36.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[61].dn"
		;
connectAttr "unitConversion47.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[62].dn"
		;
connectAttr "unitConversion29.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[63].dn"
		;
connectAttr "unitConversion34.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[64].dn"
		;
connectAttr "curve1_jnt_orientConstraint1_bc_fm.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[65].dn"
		;
connectAttr "curve6_jnt_orientConstraint1.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[66].dn"
		;
connectAttr "unitConversion28.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[67].dn"
		;
connectAttr "unitConversion27.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[68].dn"
		;
connectAttr "curve2_jnt_orientConstraint1.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[69].dn"
		;
connectAttr "unitConversion9.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[70].dn"
		;
connectAttr "curve4_jnt.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[71].dn";
connectAttr "unitConversion70.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[72].dn"
		;
connectAttr "curve4.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[73].dn";
connectAttr "unitConversion48.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[74].dn"
		;
connectAttr "unitConversion5.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[75].dn"
		;
connectAttr "unitConversion58.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[76].dn"
		;
connectAttr "unitConversion30.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[77].dn"
		;
connectAttr "unitConversion45.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[78].dn"
		;
connectAttr "unitConversion50.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[79].dn"
		;
connectAttr "curve5_jnt.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[80].dn";
connectAttr "unitConversion38.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[81].dn"
		;
connectAttr "curve5_jnt_orientConstraint1_bc_fm.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[82].dn"
		;
connectAttr "curve3_jnt.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[83].dn";
connectAttr "curve2.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[84].dn";
connectAttr "curve1_jnt_orientConstraint1.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[85].dn"
		;
connectAttr "unitConversion42.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[86].dn"
		;
connectAttr "unitConversion40.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[87].dn"
		;
connectAttr "curve7_jnt.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[88].dn";
connectAttr "unitConversion54.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[89].dn"
		;
connectAttr "unitConversion25.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[90].dn"
		;
connectAttr "unitConversion12.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[91].dn"
		;
connectAttr "unitConversion24.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[92].dn"
		;
connectAttr "unitConversion13.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[93].dn"
		;
connectAttr "curve3_jnt_orientConstraint1_bc_fm.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[94].dn"
		;
connectAttr "unitConversion57.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[95].dn"
		;
connectAttr "curve1.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[96].dn";
connectAttr "curve6_jnt.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[97].dn";
connectAttr "unitConversion44.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[98].dn"
		;
connectAttr "unitConversion23.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[99].dn"
		;
connectAttr "unitConversion3.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[100].dn"
		;
connectAttr "unitConversion7.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[101].dn"
		;
connectAttr "unitConversion73.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[102].dn"
		;
connectAttr "unitConversion68.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[103].dn"
		;
connectAttr "unitConversion67.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[104].dn"
		;
connectAttr "unitConversion18.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[105].dn"
		;
connectAttr "curve5_jnt_orientConstraint1.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[106].dn"
		;
connectAttr "curve8_jnt_orientConstraint1.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[107].dn"
		;
connectAttr "unitConversion35.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[108].dn"
		;
connectAttr "unitConversion16.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[109].dn"
		;
connectAttr "unitConversion64.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[110].dn"
		;
connectAttr "unitConversion37.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[111].dn"
		;
connectAttr "curve1_jnt_orientConstraint1_bc.msg" "MayaNodeEditorSavedTabsInfo.tgi[3].ni[0].dn"
		;
connectAttr "curve8_jnt_orientConstraint1_bc.msg" "MayaNodeEditorSavedTabsInfo.tgi[3].ni[1].dn"
		;
connectAttr "curve3_jnt_orientConstraint1_bc.msg" "MayaNodeEditorSavedTabsInfo.tgi[3].ni[2].dn"
		;
connectAttr "curve2_jnt_orientConstraint1_bc.msg" "MayaNodeEditorSavedTabsInfo.tgi[3].ni[3].dn"
		;
connectAttr "curve5_jnt_orientConstraint1_bc.msg" "MayaNodeEditorSavedTabsInfo.tgi[3].ni[4].dn"
		;
connectAttr "curve7_jnt_orientConstraint1_bc.msg" "MayaNodeEditorSavedTabsInfo.tgi[3].ni[5].dn"
		;
connectAttr "curve4_jnt_orientConstraint1_bc.msg" "MayaNodeEditorSavedTabsInfo.tgi[3].ni[6].dn"
		;
connectAttr "curve4_jnt_orientConstraint1_bc.msg" "MayaNodeEditorSavedTabsInfo.tgi[4].ni[0].dn"
		;
connectAttr "curve8_jnt_orientConstraint1_bc.msg" "MayaNodeEditorSavedTabsInfo.tgi[4].ni[1].dn"
		;
connectAttr "curve4_jnt.msg" "MayaNodeEditorSavedTabsInfo.tgi[4].ni[2].dn";
connectAttr "curve8_jnt.msg" "MayaNodeEditorSavedTabsInfo.tgi[4].ni[3].dn";
connectAttr "joint26_aimConstraint1.msg" "MayaNodeEditorSavedTabsInfo.tgi[5].ni[0].dn"
		;
connectAttr "joint25.msg" "MayaNodeEditorSavedTabsInfo.tgi[5].ni[1].dn";
connectAttr "joint25_aimConstraint1.msg" "MayaNodeEditorSavedTabsInfo.tgi[5].ni[2].dn"
		;
connectAttr "joint26.msg" "MayaNodeEditorSavedTabsInfo.tgi[5].ni[3].dn";
connectAttr "joint25_parentConstraint1.msg" "MayaNodeEditorSavedTabsInfo.tgi[5].ni[4].dn"
		;
connectAttr "joint26_parentConstraint1.msg" "MayaNodeEditorSavedTabsInfo.tgi[5].ni[5].dn"
		;
connectAttr "locatorShape2.msg" "MayaNodeEditorSavedTabsInfo.tgi[5].ni[6].dn";
connectAttr "multiplyDivide1.msg" "MayaNodeEditorSavedTabsInfo.tgi[5].ni[7].dn";
connectAttr "condition1.msg" "MayaNodeEditorSavedTabsInfo.tgi[5].ni[8].dn";
connectAttr "Wrist.msg" "MayaNodeEditorSavedTabsInfo.tgi[5].ni[9].dn";
connectAttr "distanceDimensionShape1.msg" "MayaNodeEditorSavedTabsInfo.tgi[5].ni[10].dn"
		;
connectAttr "Elbow.msg" "MayaNodeEditorSavedTabsInfo.tgi[5].ni[11].dn";
connectAttr "locatorShape1.msg" "MayaNodeEditorSavedTabsInfo.tgi[5].ni[12].dn";
connectAttr "Shoulder.msg" "MayaNodeEditorSavedTabsInfo.tgi[5].ni[13].dn";
connectAttr "Hand3.msg" "MayaNodeEditorSavedTabsInfo.tgi[6].ni[0].dn";
connectAttr "tweakSet1.msg" "MayaNodeEditorSavedTabsInfo.tgi[6].ni[1].dn";
connectAttr "Shoulder.msg" "MayaNodeEditorSavedTabsInfo.tgi[6].ni[2].dn";
connectAttr "Hand2.msg" "MayaNodeEditorSavedTabsInfo.tgi[6].ni[3].dn";
connectAttr "Wrist.msg" "MayaNodeEditorSavedTabsInfo.tgi[6].ni[4].dn";
connectAttr "HandShape1.msg" "MayaNodeEditorSavedTabsInfo.tgi[6].ni[5].dn";
connectAttr "loftedSurfaceShape2Orig.msg" "MayaNodeEditorSavedTabsInfo.tgi[6].ni[6].dn"
		;
connectAttr "tweak1.msg" "MayaNodeEditorSavedTabsInfo.tgi[6].ni[7].dn";
connectAttr "Hand6.msg" "MayaNodeEditorSavedTabsInfo.tgi[6].ni[8].dn";
connectAttr "HandShape4.msg" "MayaNodeEditorSavedTabsInfo.tgi[6].ni[9].dn";
connectAttr "HandShape2.msg" "MayaNodeEditorSavedTabsInfo.tgi[6].ni[10].dn";
connectAttr "Hand4.msg" "MayaNodeEditorSavedTabsInfo.tgi[6].ni[11].dn";
connectAttr "HandShape6.msg" "MayaNodeEditorSavedTabsInfo.tgi[6].ni[12].dn";
connectAttr "HandShape3.msg" "MayaNodeEditorSavedTabsInfo.tgi[6].ni[13].dn";
connectAttr "loftedSurface2.msg" "MayaNodeEditorSavedTabsInfo.tgi[6].ni[14].dn";
connectAttr "joint23_jnt.msg" "MayaNodeEditorSavedTabsInfo.tgi[6].ni[15].dn";
connectAttr "tweak2.msg" "MayaNodeEditorSavedTabsInfo.tgi[6].ni[16].dn";
connectAttr "Hand1.msg" "MayaNodeEditorSavedTabsInfo.tgi[6].ni[17].dn";
connectAttr "HandShape5.msg" "MayaNodeEditorSavedTabsInfo.tgi[6].ni[18].dn";
connectAttr ":initialShadingGroup.msg" "MayaNodeEditorSavedTabsInfo.tgi[6].ni[19].dn"
		;
connectAttr "Elbow.msg" "MayaNodeEditorSavedTabsInfo.tgi[6].ni[20].dn";
connectAttr "tweakSet2.msg" "MayaNodeEditorSavedTabsInfo.tgi[6].ni[21].dn";
connectAttr "HandShape8.msg" "MayaNodeEditorSavedTabsInfo.tgi[6].ni[22].dn";
connectAttr "Hand7.msg" "MayaNodeEditorSavedTabsInfo.tgi[6].ni[23].dn";
connectAttr "Hand5.msg" "MayaNodeEditorSavedTabsInfo.tgi[6].ni[24].dn";
connectAttr "loftedSurfaceShape1Orig.msg" "MayaNodeEditorSavedTabsInfo.tgi[6].ni[25].dn"
		;
connectAttr "loftedSurfaceShape1.msg" "MayaNodeEditorSavedTabsInfo.tgi[6].ni[26].dn"
		;
connectAttr "Hand8.msg" "MayaNodeEditorSavedTabsInfo.tgi[6].ni[27].dn";
connectAttr "HandShape7.msg" "MayaNodeEditorSavedTabsInfo.tgi[6].ni[28].dn";
connectAttr "loftedSurfaceShape2.msg" "MayaNodeEditorSavedTabsInfo.tgi[6].ni[29].dn"
		;
connectAttr "multiplyDivide1.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "condition1.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "curve6_jnt_orientConstraint1_bc.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "defaultRenderLayer.msg" ":defaultRenderingList1.r" -na;
connectAttr "loftedSurfaceShape1.iog" ":initialShadingGroup.dsm" -na;
connectAttr "loftedSurfaceShape2.iog" ":initialShadingGroup.dsm" -na;
connectAttr "ikRPsolver.msg" ":ikSystem.sol" -na;
// End of twist_IK.ma
