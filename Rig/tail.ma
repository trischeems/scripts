//Maya ASCII 2020 scene
//Name: tail.ma
//Last modified: Wed, Jun 19, 2024 06:09:04 PM
//Codeset: 1252
requires maya "2020";
requires "mtoa" "4.1.1";
currentUnit -l centimeter -a degree -t film;
fileInfo "application" "maya";
fileInfo "product" "Maya 2020";
fileInfo "version" "2020";
fileInfo "cutIdentifier" "202011110415-b1e20b88e2";
fileInfo "osv" "Microsoft Windows 10 Technical Preview  (Build 22631)\n";
fileInfo "UUID" "5EE157A6-4584-35EC-09B7-9298D366FEEE";
createNode transform -s -n "persp";
	rename -uid "095F0A8D-4D97-84D2-B537-9AA285DC4AE4";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 30.125311962617452 11.221826400275813 -10.505283818252868 ;
	setAttr ".r" -type "double3" -13.538352729576365 98.59999999998908 0 ;
createNode camera -s -n "perspShape" -p "persp";
	rename -uid "DA503BF0-437D-F376-1CD7-3A95B21C2512";
	setAttr -k off ".v" no;
	setAttr ".fl" 34.999999999999993;
	setAttr ".coi" 33.11317520857839;
	setAttr ".imn" -type "string" "persp";
	setAttr ".den" -type "string" "persp_depth";
	setAttr ".man" -type "string" "persp_mask";
	setAttr ".tp" -type "double3" -3.5762786865234375e-07 0 -4.76837158203125e-07 ;
	setAttr ".hc" -type "string" "viewSet -p %camera";
	setAttr ".ai_translator" -type "string" "perspective";
createNode transform -s -n "top";
	rename -uid "8B3C681A-4B4B-C9CD-5FBA-8E9F65DBB37A";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 1000.1 0 ;
	setAttr ".r" -type "double3" -90 0 0 ;
createNode camera -s -n "topShape" -p "top";
	rename -uid "CF542E12-4084-7406-B4BA-2199F5369E8C";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 1000.1;
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "top";
	setAttr ".den" -type "string" "top_depth";
	setAttr ".man" -type "string" "top_mask";
	setAttr ".tp" -type "double3" -3.5762786865234375e-07 0 -4.76837158203125e-07 ;
	setAttr ".hc" -type "string" "viewSet -t %camera";
	setAttr ".o" yes;
	setAttr ".ai_translator" -type "string" "orthographic";
createNode transform -s -n "front";
	rename -uid "E7CE27D6-491E-28AD-70EF-718EA4D64385";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 0 1000.1 ;
createNode camera -s -n "frontShape" -p "front";
	rename -uid "9F0C63DF-472B-13A2-180C-3D9FE0D712D0";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 1000.1;
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "front";
	setAttr ".den" -type "string" "front_depth";
	setAttr ".man" -type "string" "front_mask";
	setAttr ".tp" -type "double3" -3.5762786865234375e-07 0 -4.76837158203125e-07 ;
	setAttr ".hc" -type "string" "viewSet -f %camera";
	setAttr ".o" yes;
	setAttr ".ai_translator" -type "string" "orthographic";
createNode transform -s -n "side";
	rename -uid "4E976744-4771-D740-69F6-3E8582C486DF";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 1000.1 0 0 ;
	setAttr ".r" -type "double3" 0 90 0 ;
createNode camera -s -n "sideShape" -p "side";
	rename -uid "73592B42-4AA2-D6C3-F24F-8BB30E318249";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 1000.1;
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "side";
	setAttr ".den" -type "string" "side_depth";
	setAttr ".man" -type "string" "side_mask";
	setAttr ".tp" -type "double3" -3.5762786865234375e-07 0 -4.76837158203125e-07 ;
	setAttr ".hc" -type "string" "viewSet -s %camera";
	setAttr ".o" yes;
	setAttr ".ai_translator" -type "string" "orthographic";
createNode joint -n "Jnt";
	rename -uid "0244B2F9-4B1D-9904-639B-98A037D659CE";
	setAttr ".t" -type "double3" 0 6.9172255761933616 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 90 0 ;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "Jnt1" -p "Jnt";
	rename -uid "F07947AB-415D-A239-20E6-DF97E0041749";
	setAttr ".t" -type "double3" 2 0 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "Jnt2" -p "Jnt1";
	rename -uid "DDA37A37-405B-F1A7-B75E-F3BA41B51EEC";
	setAttr ".t" -type "double3" 2 0 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "Jnt3" -p "Jnt2";
	rename -uid "D320CBB7-42C5-BC30-FCC1-A394F84D7CD5";
	setAttr ".t" -type "double3" 2 0 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "Jnt4" -p "Jnt3";
	rename -uid "6AB2F098-45CD-B6B2-C62C-EF936739A2B8";
	setAttr ".t" -type "double3" 2 0 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 -90 0 ;
	setAttr ".radi" 0.55172413793103448;
createNode ikEffector -n "effector1" -p "Jnt3";
	rename -uid "46FB4153-4E79-4A34-E24A-C08D64ADB8B6";
	setAttr ".v" no;
	setAttr ".hd" yes;
createNode nucleus -n "nucleus1";
	rename -uid "CBF64389-409C-B3D2-8765-C9AC5BF5BDF0";
	setAttr ".t" -type "double3" -0.022268998236043558 3.2243721181635019 -0.60570365066926235 ;
	setAttr ".grty" 372.34042358398438;
	setAttr ".grdi" -type "float3" 0 -10 0 ;
	setAttr ".ady" 0;
	setAttr ".clra" 2.6755318641662598;
	setAttr ".sstp" 1;
	setAttr ".mcit" 0;
createNode transform -n "hairSystem1Follicles";
	rename -uid "DCFA37AE-44B2-D316-FA73-128C35D7AB9A";
createNode transform -n "follicle1" -p "hairSystem1Follicles";
	rename -uid "E42E39BC-4DA9-C664-43C8-5983500A1025";
	setAttr ".v" no;
createNode follicle -n "follicleShape1" -p "follicle1";
	rename -uid "1E02EA91-4F7D-6C0A-639A-95A49E932205";
	setAttr -k off ".v";
	setAttr ".rsp" 1;
	setAttr ".sdr" 1;
	setAttr -s 2 ".sts[0:1]"  0 1 3 1 0.2 3;
	setAttr -s 2 ".cws[0:1]"  0 1 3 1 0.2 3;
	setAttr -s 2 ".ats[0:1]"  0 1 3 1 0.2 3;
createNode transform -n "baseCurve2" -p "follicle1";
	rename -uid "6502A0BD-4273-140B-0722-2CB52A1BD601";
	setAttr ".v" no;
createNode nurbsCurve -n "baseCurveShape2" -p "baseCurve2";
	rename -uid "1B7DBF19-466D-52C8-EA4D-CD9BD5DE137D";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".cc" -type "nurbsCurve" 
		3 2 0 no 3
		7 0 0 0 4 8 8 8
		5
		0 6.9172255761932879 -2.4919918857106893e-16
		-0 6.917225576193287 -1.3333333333333359
		0 6.9172255761932773 -3.9999999999999942
		0 6.9172255761932826 -6.6666666666666616
		0 6.9172255761932826 -7.9999999999999964
		;
createNode transform -n "dynJoint_HairStuff1";
	rename -uid "E218322D-4141-204A-8BD2-9288BA6CEAE8";
	setAttr ".rp" -type "double3" 0 4.4586127880966808 -4.2338915517241382 ;
	setAttr ".sp" -type "double3" 0 4.4586127880966808 -4.2338915517241382 ;
createNode ikHandle -n "hairHandle1" -p "dynJoint_HairStuff1";
	rename -uid "FF23337E-47EF-9491-6313-BB93C05F57BB";
	addAttr -ci true -sn "hairStiffness" -ln "hairStiffness" -dv 0.25 -min 0 -max 1 
		-at "double";
	addAttr -ci true -sn "hairGravity" -ln "hairGravity" -dv 20 -min -10 -max 100 -at "double";
	addAttr -ci true -sn "hairDamping" -ln "hairDamping" -min 0 -max 1 -at "double";
	addAttr -ci true -sn "hairFriction" -ln "hairFriction" -dv 0.1 -min 0 -max 1 -at "double";
	addAttr -ci true -sn "hairSolver" -ln "hairSolver" -dv 1 -min 0 -max 1 -en "Classic:Nucleus" 
		-at "enum";
	addAttr -ci true -sn "nts" -ln "notes" -dt "string";
	setAttr ".t" -type "double3" 0 6.9172255761933616 -8 ;
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr ".r" -type "double3" 0 90 0 ;
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".hdl" -type "double3" 0 2 0 ;
	setAttr ".dh" yes;
	setAttr -k off ".pvx";
	setAttr -k off ".pvy";
	setAttr -k off ".pvz";
	setAttr -k off ".off";
	setAttr -k off ".rol";
	setAttr -k off ".twi";
	setAttr ".roc" yes;
	setAttr -k off ".ikb";
	setAttr -k on ".hairStiffness" 0.5;
	setAttr -k on ".hairGravity";
	setAttr -k on ".hairDamping";
	setAttr -k on ".hairFriction";
	setAttr -k on ".hairSolver";
	setAttr ".nts" -type "string" "The hairHandle contains extra attributes that indirectly control the more common attrs that exist on the actual hairSystem node.  This is done so that you can easily access and edit the attrs from the channel box by selecting the hair handle.  You can remove these attrs or break their connection if you're more experienced with hair and want to work with the hairSystem directly.\r\n";
createNode transform -n "hairCurve2" -p "dynJoint_HairStuff1";
	rename -uid "FF046DD7-4763-D999-C4E9-0782A0416B3F";
	setAttr ".t" -type "double3" 0 2.1532300000000003e-07 0 ;
createNode nurbsCurve -n "hairCurveShape2" -p "hairCurve2";
	rename -uid "1BE580BE-48B3-098C-601D-86A6D9684BFE";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".tw" yes;
createNode transform -n "hairSystem1" -p "dynJoint_HairStuff1";
	rename -uid "978818BF-49D4-047A-C993-CABBBCAD4FA5";
createNode hairSystem -n "hairSystemShape1" -p "hairSystem1";
	rename -uid "7FA0B172-4C7D-DFCF-C6E6-74AB87E6D5A7";
	setAttr -k off ".v";
	setAttr ".stch" 160;
	setAttr -s 2 ".sts[0:1]"  0 1 1 1 0 0;
	setAttr -s 2 ".ats[0:1]"  0 1 1 1 0.2 1;
	setAttr ".cwd" 1e-05;
	setAttr -s 2 ".cws[0:1]"  0 1 3 1 0.2 3;
	setAttr ".clc[0]"  0 0.5 1;
	setAttr ".cfl[0]"  0 0 1;
	setAttr -s 2 ".hws[0:1]"  0.80000001 1 1 1 0.2 1;
	setAttr -s 3 ".hcs";
	setAttr ".hcs[0].hcsp" 0;
	setAttr ".hcs[0].hcsc" -type "float3" 0.5 0.5 0.5 ;
	setAttr ".hcs[0].hcsi" 1;
	setAttr ".hcs[1].hcsp" 0.30000001192092896;
	setAttr ".hcs[1].hcsc" -type "float3" 0.80000001 0.80000001 0.80000001 ;
	setAttr ".hcs[1].hcsi" 1;
	setAttr ".hcs[2].hcsp" 1;
	setAttr ".hcs[2].hcsc" -type "float3" 1 1 1 ;
	setAttr ".hcs[2].hcsi" 1;
	setAttr ".hpc" 1;
	setAttr ".dsc[0]"  0 1 1;
createNode transform -n "hairSystem1OutputCurves" -p "dynJoint_HairStuff1";
	rename -uid "24251761-479E-FB4C-07CD-94BB73C2BA41";
createNode joint -n "Hand";
	rename -uid "21A862B6-4E16-FB8A-D5F6-159954727BBC";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 90 0 ;
	setAttr ".bps" -type "matrix" 0 0 -1 0 0 1 0 0 1 0 0 0 0 6.9172255761933599 -2.4919918419480369e-16 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "Hand1" -p "Hand";
	rename -uid "D0DC1D13-4DC1-17EA-C474-DF892F67CE9C";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 1;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0 0 -1 0 0 1 0 0 1 0 0 0 0 6.9172255761933581 -2.0000000000000004 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "Hand2" -p "Hand1";
	rename -uid "94A76B33-4D51-AE63-3E05-4DAED4730095";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 2;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0 0 -1 0 0 1 0 0 1 0 0 0 0 6.9172255761933563 -4 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "Hand3" -p "Hand2";
	rename -uid "FBDE6C09-41B0-7E43-E8DE-2E832CEFADE5";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 3;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0 0 -1 0 0 1 0 0 1 0 0 0 0 6.9172255761933563 -6 1;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "Hand4" -p "Hand3";
	rename -uid "2601F365-47DC-B694-FE9E-B989BAC7CF34";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".uoc" 1;
	setAttr ".oc" 4;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 -90 0 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 6.9172255761933528 -8 1;
	setAttr ".radi" 0.55172413793103448;
createNode parentConstraint -n "Hand4_parentConstraint1" -p "Hand4";
	rename -uid "BB5061B9-42B4-1BD9-A6B9-0F8DE50A7B91";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "Hand4_CtrlW0" -dv 1 -min 0 -at "double";
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
	setAttr ".tg[0].tot" -type "double3" 0 -4.4408920985006262e-15 0 ;
	setAttr ".tg[0].tor" -type "double3" 0 -90 0 ;
	setAttr ".rst" -type "double3" 2 -3.5527136788005009e-15 0 ;
	setAttr -k on ".w0";
createNode parentConstraint -n "Hand3_parentConstraint1" -p "Hand3";
	rename -uid "F471C4D7-4885-742A-5F0C-F9AF8586C4A4";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "Hand3_CtrlW0" -dv 1 -min 0 -at "double";
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
	setAttr ".tg[0].tot" -type "double3" 0 -2.6645352591003757e-15 0 ;
	setAttr ".rst" -type "double3" 2 0 0 ;
	setAttr -k on ".w0";
createNode parentConstraint -n "Hand2_parentConstraint1" -p "Hand2";
	rename -uid "6F579768-43C0-674A-741F-44891256CC49";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "Hand2_CtrlW0" -dv 1 -min 0 -at "double";
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
	setAttr ".tg[0].tot" -type "double3" 0 -2.6645352591003757e-15 0 ;
	setAttr ".rst" -type "double3" 1.9999999999999996 -8.8817841970012523e-16 0 ;
	setAttr -k on ".w0";
createNode parentConstraint -n "Hand1_parentConstraint1" -p "Hand1";
	rename -uid "B7FB06A5-4930-FCA5-AF2B-E794B5340188";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "Hand1_CtrlW0" -dv 1 -min 0 -at "double";
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
	setAttr ".tg[0].tot" -type "double3" 0 -1.7763568394002505e-15 0 ;
	setAttr ".rst" -type "double3" 2 -8.8817841970012523e-16 0 ;
	setAttr -k on ".w0";
createNode parentConstraint -n "Hand_parentConstraint1" -p "Hand";
	rename -uid "8B2BAD2D-4A5F-B9F9-17B7-7AA6F5788B13";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "Hand_CtrlW0" -dv 1 -min 0 -at "double";
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
	setAttr ".tg[0].tot" -type "double3" 0 -8.8817841970012523e-16 0 ;
	setAttr ".rst" -type "double3" 0 6.9172255761933608 -2.4919918419480369e-16 ;
	setAttr -k on ".w0";
createNode transform -n "Hand_grp";
	rename -uid "8BDFB5CF-4812-6618-E106-BC9FFCF5E0F3";
createNode transform -n "Hand_Ctrl" -p "Hand_grp";
	rename -uid "F1160ACC-4E58-F4AA-2826-A290CBEA00CB";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 1 1 0 ;
createNode nurbsCurve -n "Hand_CtrlShape" -p "Hand_Ctrl";
	rename -uid "9AC886BF-4551-52AD-9DD4-2287914D7E94";
	setAttr -k off ".v";
	setAttr ".tw" yes;
createNode transform -n "Hand1_grp" -p "Hand_Ctrl";
	rename -uid "948D62E9-46D8-F90B-BD08-EB925F478968";
createNode transform -n "Hand1_Ctrl" -p "Hand1_grp";
	rename -uid "075A4D77-425D-2AB0-E1A1-429ECF978BD3";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 1 1 0 ;
createNode nurbsCurve -n "Hand1_CtrlShape" -p "Hand1_Ctrl";
	rename -uid "CBDA10BF-4199-19CF-C1B4-009B92A5894A";
	setAttr -k off ".v";
	setAttr ".tw" yes;
createNode transform -n "Hand2_grp" -p "Hand1_Ctrl";
	rename -uid "5B442451-404B-5B6B-B7EA-7C961BD8D30D";
createNode transform -n "Hand2_Ctrl" -p "Hand2_grp";
	rename -uid "3E194F08-4855-EA9A-BD14-DA88718DBB72";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 1 1 0 ;
createNode nurbsCurve -n "Hand2_CtrlShape" -p "Hand2_Ctrl";
	rename -uid "724E9D6D-4513-A18A-38B2-E294239A8124";
	setAttr -k off ".v";
	setAttr ".tw" yes;
createNode transform -n "Hand3_grp" -p "Hand2_Ctrl";
	rename -uid "E20CE5EB-41F0-E692-4A90-EE91193EC12F";
createNode transform -n "Hand3_Ctrl" -p "Hand3_grp";
	rename -uid "59604928-4F66-4953-8F0C-4DB3D79AEA9F";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 1 1 0 ;
createNode nurbsCurve -n "Hand3_CtrlShape" -p "Hand3_Ctrl";
	rename -uid "3D6D6297-4E74-40F8-D73F-55A577521672";
	setAttr -k off ".v";
	setAttr ".tw" yes;
createNode transform -n "Hand4_grp" -p "Hand3_Ctrl";
	rename -uid "BC9C6297-4C3B-F332-13E9-9DBFCE5F0A59";
createNode transform -n "Hand4_Ctrl" -p "Hand4_grp";
	rename -uid "9BA98F61-4CD1-00E3-1967-528A12E5BFD8";
	setAttr ".ove" yes;
	setAttr ".ovrgbf" yes;
	setAttr ".ovrgb" -type "float3" 1 1 0 ;
createNode nurbsCurve -n "Hand4_CtrlShape" -p "Hand4_Ctrl";
	rename -uid "CECF18F9-4218-6E35-886C-D4B7DD5B1E2C";
	setAttr -k off ".v";
	setAttr ".tw" yes;
createNode parentConstraint -n "Hand_grp_parentConstraint1" -p "Hand_grp";
	rename -uid "B4D22A2E-417C-3269-B7B6-989BED7CBECE";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "JntW0" -dv 1 -min 0 -at "double";
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
	setAttr ".tg[0].tot" -type "double3" 0 -1.7763568394002505e-15 0 ;
	setAttr ".lr" -type "double3" 0 90 0 ;
	setAttr ".rst" -type "double3" 0 6.9172255761933599 -2.4919918419480369e-16 ;
	setAttr ".rsrr" -type "double3" 0 90 0 ;
	setAttr -k on ".w0";
createNode transform -n "pCylinder1";
	rename -uid "0AD4DDE0-4ACA-3F8F-5FFB-EDBCCF66EA7C";
	setAttr -l on ".tx";
	setAttr -l on ".ty";
	setAttr -l on ".tz";
	setAttr -l on ".rx";
	setAttr -l on ".ry";
	setAttr -l on ".rz";
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
	setAttr ".rp" -type "double3" 0 6.9172253608703613 -4.3445387207757715 ;
	setAttr ".sp" -type "double3" 0 6.9172253608703613 -4.3445387207757715 ;
createNode mesh -n "pCylinderShape1" -p "pCylinder1";
	rename -uid "2156B21B-49A9-FD41-AB9F-3F8ADCE7F6B0";
	setAttr -k off ".v";
	setAttr -s 4 ".iog[0].og";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".vcs" 2;
	setAttr ".ai_translator" -type "string" "polymesh";
createNode mesh -n "pCylinderShape1Orig" -p "pCylinder1";
	rename -uid "959B4BC5-4230-6D23-0431-648ECCC05712";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 147 ".uvst[0].uvsp[0:146]" -type "float2" 0.57812506 0.020933539
		 0.42187503 0.020933509 0.34375 0.15624997 0.421875 0.29156646 0.578125 0.29156649
		 0.65625 0.15625 0.375 0.3125 0.41666666 0.3125 0.45833331 0.3125 0.49999997 0.3125
		 0.54166663 0.3125 0.58333331 0.3125 0.625 0.3125 0.375 0.33338556 0.41666666 0.33338556
		 0.45833331 0.33338556 0.49999997 0.33338556 0.54166663 0.33338556 0.58333331 0.33338556
		 0.625 0.33338556 0.375 0.35427111 0.41666666 0.35427111 0.45833331 0.35427111 0.49999997
		 0.35427111 0.54166663 0.35427111 0.58333331 0.35427111 0.625 0.35427111 0.375 0.37515667
		 0.41666666 0.37515667 0.45833331 0.37515667 0.49999997 0.37515667 0.54166663 0.37515667
		 0.58333331 0.37515667 0.625 0.37515667 0.375 0.39604223 0.41666666 0.39604223 0.45833331
		 0.39604223 0.49999997 0.39604223 0.54166663 0.39604223 0.58333331 0.39604223 0.625
		 0.39604223 0.375 0.41692778 0.41666666 0.41692778 0.45833331 0.41692778 0.49999997
		 0.41692778 0.54166663 0.41692778 0.58333331 0.41692778 0.625 0.41692778 0.375 0.43781334
		 0.41666666 0.43781334 0.45833331 0.43781334 0.49999997 0.43781334 0.54166663 0.43781334
		 0.58333331 0.43781334 0.625 0.43781334 0.375 0.4586989 0.41666666 0.4586989 0.45833331
		 0.4586989 0.49999997 0.4586989 0.54166663 0.4586989 0.58333331 0.4586989 0.625 0.4586989
		 0.375 0.47958446 0.41666666 0.47958446 0.45833331 0.47958446 0.49999997 0.47958446
		 0.54166663 0.47958446 0.58333331 0.47958446 0.625 0.47958446 0.375 0.50046998 0.41666666
		 0.50046998 0.45833331 0.50046998 0.49999997 0.50046998 0.54166663 0.50046998 0.58333331
		 0.50046998 0.625 0.50046998 0.375 0.52135551 0.41666666 0.52135551 0.45833331 0.52135551
		 0.49999997 0.52135551 0.54166663 0.52135551 0.58333331 0.52135551 0.625 0.52135551
		 0.375 0.54224104 0.41666666 0.54224104 0.45833331 0.54224104 0.49999997 0.54224104
		 0.54166663 0.54224104 0.58333331 0.54224104 0.625 0.54224104 0.375 0.56312656 0.41666666
		 0.56312656 0.45833331 0.56312656 0.49999997 0.56312656 0.54166663 0.56312656 0.58333331
		 0.56312656 0.625 0.56312656 0.375 0.58401209 0.41666666 0.58401209 0.45833331 0.58401209
		 0.49999997 0.58401209 0.54166663 0.58401209 0.58333331 0.58401209 0.625 0.58401209
		 0.375 0.60489762 0.41666666 0.60489762 0.45833331 0.60489762 0.49999997 0.60489762
		 0.54166663 0.60489762 0.58333331 0.60489762 0.625 0.60489762 0.375 0.62578315 0.41666666
		 0.62578315 0.45833331 0.62578315 0.49999997 0.62578315 0.54166663 0.62578315 0.58333331
		 0.62578315 0.625 0.62578315 0.375 0.64666867 0.41666666 0.64666867 0.45833331 0.64666867
		 0.49999997 0.64666867 0.54166663 0.64666867 0.58333331 0.64666867 0.625 0.64666867
		 0.375 0.6675542 0.41666666 0.6675542 0.45833331 0.6675542 0.49999997 0.6675542 0.54166663
		 0.6675542 0.58333331 0.6675542 0.625 0.6675542 0.375 0.68843973 0.41666666 0.68843973
		 0.45833331 0.68843973 0.49999997 0.68843973 0.54166663 0.68843973 0.58333331 0.68843973
		 0.625 0.68843973 0.57812506 0.70843351 0.42187503 0.70843351 0.34375 0.84375 0.421875
		 0.97906649 0.578125 0.97906649 0.65625 0.84375 0.5 0.15000001 0.5 0.83749998;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 116 ".vt[0:115]"  0.50000024 7.78325081 -8.87656021 -0.49999985 7.78325081 -8.87656021
		 -1 6.91722536 -8.87656021 -0.50000012 6.051199913 -8.87656021 0.49999997 6.051199913 -8.87656021
		 1 6.91722536 -8.87656021 0.50000024 7.78325081 -8.37300301 -0.49999985 7.78325081 -8.37300301
		 -1 6.91722536 -8.37300301 -0.50000012 6.051199913 -8.37300301 0.49999997 6.051199913 -8.37300301
		 1 6.91722536 -8.37300301 0.50000024 7.78325081 -7.86944485 -0.49999985 7.78325081 -7.86944485
		 -1 6.91722536 -7.86944485 -0.50000012 6.051199913 -7.86944485 0.49999997 6.051199913 -7.86944485
		 1 6.91722536 -7.86944485 0.50000024 7.78325081 -7.36588669 -0.49999985 7.78325081 -7.36588669
		 -1 6.91722536 -7.36588669 -0.50000012 6.051199913 -7.36588669 0.49999997 6.051199913 -7.36588669
		 1 6.91722536 -7.36588669 0.50000024 7.78325081 -6.86232853 -0.49999985 7.78325081 -6.86232853
		 -1 6.91722536 -6.86232853 -0.50000012 6.051199913 -6.86232853 0.49999997 6.051199913 -6.86232853
		 1 6.91722536 -6.86232853 0.50000024 7.78325081 -6.35877085 -0.49999985 7.78325081 -6.35877085
		 -1 6.91722536 -6.35877085 -0.50000012 6.051199913 -6.35877085 0.49999997 6.051199913 -6.35877085
		 1 6.91722536 -6.35877085 0.50000024 7.78325081 -5.85521317 -0.49999985 7.78325081 -5.85521317
		 -1 6.91722536 -5.85521317 -0.50000012 6.051199913 -5.85521317 0.49999997 6.051199913 -5.85521317
		 1 6.91722536 -5.85521317 0.50000024 7.78325081 -5.35165501 -0.49999985 7.78325081 -5.35165501
		 -1 6.91722536 -5.35165501 -0.50000012 6.051199913 -5.35165501 0.49999997 6.051199913 -5.35165501
		 1 6.91722536 -5.35165501 0.50000024 7.78325081 -4.84809685 -0.49999985 7.78325081 -4.84809685
		 -1 6.91722536 -4.84809685 -0.50000012 6.051199913 -4.84809685 0.49999997 6.051199913 -4.84809685
		 1 6.91722536 -4.84809685 0.50000024 7.78325081 -4.34453869 -0.49999985 7.78325081 -4.34453869
		 -1 6.91722536 -4.34453869 -0.50000012 6.051199913 -4.34453869 0.49999997 6.051199913 -4.34453869
		 1 6.91722536 -4.34453869 0.50000024 7.78325081 -3.84098101 -0.49999985 7.78325081 -3.84098101
		 -1 6.91722536 -3.84098101 -0.50000012 6.051199913 -3.84098101 0.49999997 6.051199913 -3.84098101
		 1 6.91722536 -3.84098101 0.50000024 7.78325081 -3.33742285 -0.49999985 7.78325081 -3.33742285
		 -1 6.91722536 -3.33742285 -0.50000012 6.051199913 -3.33742285 0.49999997 6.051199913 -3.33742285
		 1 6.91722536 -3.33742285 0.50000024 7.78325081 -2.83386493 -0.49999985 7.78325081 -2.83386493
		 -1 6.91722536 -2.83386493 -0.50000012 6.051199913 -2.83386493 0.49999997 6.051199913 -2.83386493
		 1 6.91722536 -2.83386493 0.50000024 7.78325081 -2.33030701 -0.49999985 7.78325081 -2.33030701
		 -1 6.91722536 -2.33030701 -0.50000012 6.051199913 -2.33030701 0.49999997 6.051199913 -2.33030701
		 1 6.91722536 -2.33030701 0.50000024 7.78325081 -1.82674885 -0.49999985 7.78325081 -1.82674885
		 -1 6.91722536 -1.82674885 -0.50000012 6.051199913 -1.82674885 0.49999997 6.051199913 -1.82674885
		 1 6.91722536 -1.82674885 0.50000024 7.78325081 -1.32319093 -0.49999985 7.78325081 -1.32319093
		 -1 6.91722536 -1.32319093 -0.50000012 6.051199913 -1.32319093 0.49999997 6.051199913 -1.32319093
		 1 6.91722536 -1.32319093 0.50000024 7.78325081 -0.81963301 -0.49999985 7.78325081 -0.81963301
		 -1 6.91722536 -0.81963301 -0.50000012 6.051199913 -0.81963301 0.49999997 6.051199913 -0.81963301
		 1 6.91722536 -0.81963301 0.50000024 7.78325081 -0.31607485 -0.49999985 7.78325081 -0.31607485
		 -1 6.91722536 -0.31607485 -0.50000012 6.051199913 -0.31607485 0.49999997 6.051199913 -0.31607485
		 1 6.91722536 -0.31607485 0.50000024 7.78325081 0.18748331 -0.49999985 7.78325081 0.18748331
		 -1 6.91722536 0.18748331 -0.50000012 6.051199913 0.18748331 0.49999997 6.051199913 0.18748331
		 1 6.91722536 0.18748331 0 6.91722536 -8.87656021 0 6.91722536 0.18748331;
	setAttr -s 234 ".ed";
	setAttr ".ed[0:165]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 0 0 6 7 1 7 8 1 8 9 1
		 9 10 1 10 11 1 11 6 1 12 13 1 13 14 1 14 15 1 15 16 1 16 17 1 17 12 1 18 19 1 19 20 1
		 20 21 1 21 22 1 22 23 1 23 18 1 24 25 1 25 26 1 26 27 1 27 28 1 28 29 1 29 24 1 30 31 1
		 31 32 1 32 33 1 33 34 1 34 35 1 35 30 1 36 37 1 37 38 1 38 39 1 39 40 1 40 41 1 41 36 1
		 42 43 1 43 44 1 44 45 1 45 46 1 46 47 1 47 42 1 48 49 1 49 50 1 50 51 1 51 52 1 52 53 1
		 53 48 1 54 55 1 55 56 1 56 57 1 57 58 1 58 59 1 59 54 1 60 61 1 61 62 1 62 63 1 63 64 1
		 64 65 1 65 60 1 66 67 1 67 68 1 68 69 1 69 70 1 70 71 1 71 66 1 72 73 1 73 74 1 74 75 1
		 75 76 1 76 77 1 77 72 1 78 79 1 79 80 1 80 81 1 81 82 1 82 83 1 83 78 1 84 85 1 85 86 1
		 86 87 1 87 88 1 88 89 1 89 84 1 90 91 1 91 92 1 92 93 1 93 94 1 94 95 1 95 90 1 96 97 1
		 97 98 1 98 99 1 99 100 1 100 101 1 101 96 1 102 103 1 103 104 1 104 105 1 105 106 1
		 106 107 1 107 102 1 108 109 0 109 110 0 110 111 0 111 112 0 112 113 0 113 108 0 0 6 0
		 1 7 0 2 8 0 3 9 0 4 10 0 5 11 0 6 12 0 7 13 0 8 14 0 9 15 0 10 16 0 11 17 0 12 18 0
		 13 19 0 14 20 0 15 21 0 16 22 0 17 23 0 18 24 0 19 25 0 20 26 0 21 27 0 22 28 0 23 29 0
		 24 30 0 25 31 0 26 32 0 27 33 0 28 34 0 29 35 0 30 36 0 31 37 0 32 38 0 33 39 0 34 40 0
		 35 41 0 36 42 0 37 43 0 38 44 0 39 45 0 40 46 0 41 47 0 42 48 0 43 49 0 44 50 0 45 51 0
		 46 52 0 47 53 0 48 54 0 49 55 0 50 56 0 51 57 0;
	setAttr ".ed[166:233]" 52 58 0 53 59 0 54 60 0 55 61 0 56 62 0 57 63 0 58 64 0
		 59 65 0 60 66 0 61 67 0 62 68 0 63 69 0 64 70 0 65 71 0 66 72 0 67 73 0 68 74 0 69 75 0
		 70 76 0 71 77 0 72 78 0 73 79 0 74 80 0 75 81 0 76 82 0 77 83 0 78 84 0 79 85 0 80 86 0
		 81 87 0 82 88 0 83 89 0 84 90 0 85 91 0 86 92 0 87 93 0 88 94 0 89 95 0 90 96 0 91 97 0
		 92 98 0 93 99 0 94 100 0 95 101 0 96 102 0 97 103 0 98 104 0 99 105 0 100 106 0 101 107 0
		 102 108 0 103 109 0 104 110 0 105 111 0 106 112 0 107 113 0 114 0 1 114 1 1 114 2 1
		 114 3 1 114 4 1 114 5 1 108 115 1 109 115 1 110 115 1 111 115 1 112 115 1 113 115 1;
	setAttr -s 120 -ch 468 ".fc[0:119]" -type "polyFaces" 
		f 4 0 115 -7 -115
		mu 0 4 6 7 14 13
		f 4 1 116 -8 -116
		mu 0 4 7 8 15 14
		f 4 2 117 -9 -117
		mu 0 4 8 9 16 15
		f 4 3 118 -10 -118
		mu 0 4 9 10 17 16
		f 4 4 119 -11 -119
		mu 0 4 10 11 18 17
		f 4 5 114 -12 -120
		mu 0 4 11 12 19 18
		f 4 6 121 -13 -121
		mu 0 4 13 14 21 20
		f 4 7 122 -14 -122
		mu 0 4 14 15 22 21
		f 4 8 123 -15 -123
		mu 0 4 15 16 23 22
		f 4 9 124 -16 -124
		mu 0 4 16 17 24 23
		f 4 10 125 -17 -125
		mu 0 4 17 18 25 24
		f 4 11 120 -18 -126
		mu 0 4 18 19 26 25
		f 4 12 127 -19 -127
		mu 0 4 20 21 28 27
		f 4 13 128 -20 -128
		mu 0 4 21 22 29 28
		f 4 14 129 -21 -129
		mu 0 4 22 23 30 29
		f 4 15 130 -22 -130
		mu 0 4 23 24 31 30
		f 4 16 131 -23 -131
		mu 0 4 24 25 32 31
		f 4 17 126 -24 -132
		mu 0 4 25 26 33 32
		f 4 18 133 -25 -133
		mu 0 4 27 28 35 34
		f 4 19 134 -26 -134
		mu 0 4 28 29 36 35
		f 4 20 135 -27 -135
		mu 0 4 29 30 37 36
		f 4 21 136 -28 -136
		mu 0 4 30 31 38 37
		f 4 22 137 -29 -137
		mu 0 4 31 32 39 38
		f 4 23 132 -30 -138
		mu 0 4 32 33 40 39
		f 4 24 139 -31 -139
		mu 0 4 34 35 42 41
		f 4 25 140 -32 -140
		mu 0 4 35 36 43 42
		f 4 26 141 -33 -141
		mu 0 4 36 37 44 43
		f 4 27 142 -34 -142
		mu 0 4 37 38 45 44
		f 4 28 143 -35 -143
		mu 0 4 38 39 46 45
		f 4 29 138 -36 -144
		mu 0 4 39 40 47 46
		f 4 30 145 -37 -145
		mu 0 4 41 42 49 48
		f 4 31 146 -38 -146
		mu 0 4 42 43 50 49
		f 4 32 147 -39 -147
		mu 0 4 43 44 51 50
		f 4 33 148 -40 -148
		mu 0 4 44 45 52 51
		f 4 34 149 -41 -149
		mu 0 4 45 46 53 52
		f 4 35 144 -42 -150
		mu 0 4 46 47 54 53
		f 4 36 151 -43 -151
		mu 0 4 48 49 56 55
		f 4 37 152 -44 -152
		mu 0 4 49 50 57 56
		f 4 38 153 -45 -153
		mu 0 4 50 51 58 57
		f 4 39 154 -46 -154
		mu 0 4 51 52 59 58
		f 4 40 155 -47 -155
		mu 0 4 52 53 60 59
		f 4 41 150 -48 -156
		mu 0 4 53 54 61 60
		f 4 42 157 -49 -157
		mu 0 4 55 56 63 62
		f 4 43 158 -50 -158
		mu 0 4 56 57 64 63
		f 4 44 159 -51 -159
		mu 0 4 57 58 65 64
		f 4 45 160 -52 -160
		mu 0 4 58 59 66 65
		f 4 46 161 -53 -161
		mu 0 4 59 60 67 66
		f 4 47 156 -54 -162
		mu 0 4 60 61 68 67
		f 4 48 163 -55 -163
		mu 0 4 62 63 70 69
		f 4 49 164 -56 -164
		mu 0 4 63 64 71 70
		f 4 50 165 -57 -165
		mu 0 4 64 65 72 71
		f 4 51 166 -58 -166
		mu 0 4 65 66 73 72
		f 4 52 167 -59 -167
		mu 0 4 66 67 74 73
		f 4 53 162 -60 -168
		mu 0 4 67 68 75 74
		f 4 54 169 -61 -169
		mu 0 4 69 70 77 76
		f 4 55 170 -62 -170
		mu 0 4 70 71 78 77
		f 4 56 171 -63 -171
		mu 0 4 71 72 79 78
		f 4 57 172 -64 -172
		mu 0 4 72 73 80 79
		f 4 58 173 -65 -173
		mu 0 4 73 74 81 80
		f 4 59 168 -66 -174
		mu 0 4 74 75 82 81
		f 4 60 175 -67 -175
		mu 0 4 76 77 84 83
		f 4 61 176 -68 -176
		mu 0 4 77 78 85 84
		f 4 62 177 -69 -177
		mu 0 4 78 79 86 85
		f 4 63 178 -70 -178
		mu 0 4 79 80 87 86
		f 4 64 179 -71 -179
		mu 0 4 80 81 88 87
		f 4 65 174 -72 -180
		mu 0 4 81 82 89 88
		f 4 66 181 -73 -181
		mu 0 4 83 84 91 90
		f 4 67 182 -74 -182
		mu 0 4 84 85 92 91
		f 4 68 183 -75 -183
		mu 0 4 85 86 93 92
		f 4 69 184 -76 -184
		mu 0 4 86 87 94 93
		f 4 70 185 -77 -185
		mu 0 4 87 88 95 94
		f 4 71 180 -78 -186
		mu 0 4 88 89 96 95
		f 4 72 187 -79 -187
		mu 0 4 90 91 98 97
		f 4 73 188 -80 -188
		mu 0 4 91 92 99 98
		f 4 74 189 -81 -189
		mu 0 4 92 93 100 99
		f 4 75 190 -82 -190
		mu 0 4 93 94 101 100
		f 4 76 191 -83 -191
		mu 0 4 94 95 102 101
		f 4 77 186 -84 -192
		mu 0 4 95 96 103 102
		f 4 78 193 -85 -193
		mu 0 4 97 98 105 104
		f 4 79 194 -86 -194
		mu 0 4 98 99 106 105
		f 4 80 195 -87 -195
		mu 0 4 99 100 107 106
		f 4 81 196 -88 -196
		mu 0 4 100 101 108 107
		f 4 82 197 -89 -197
		mu 0 4 101 102 109 108
		f 4 83 192 -90 -198
		mu 0 4 102 103 110 109
		f 4 84 199 -91 -199
		mu 0 4 104 105 112 111
		f 4 85 200 -92 -200
		mu 0 4 105 106 113 112
		f 4 86 201 -93 -201
		mu 0 4 106 107 114 113
		f 4 87 202 -94 -202
		mu 0 4 107 108 115 114
		f 4 88 203 -95 -203
		mu 0 4 108 109 116 115
		f 4 89 198 -96 -204
		mu 0 4 109 110 117 116
		f 4 90 205 -97 -205
		mu 0 4 111 112 119 118
		f 4 91 206 -98 -206
		mu 0 4 112 113 120 119
		f 4 92 207 -99 -207
		mu 0 4 113 114 121 120
		f 4 93 208 -100 -208
		mu 0 4 114 115 122 121
		f 4 94 209 -101 -209
		mu 0 4 115 116 123 122
		f 4 95 204 -102 -210
		mu 0 4 116 117 124 123
		f 4 96 211 -103 -211
		mu 0 4 118 119 126 125
		f 4 97 212 -104 -212
		mu 0 4 119 120 127 126
		f 4 98 213 -105 -213
		mu 0 4 120 121 128 127
		f 4 99 214 -106 -214
		mu 0 4 121 122 129 128
		f 4 100 215 -107 -215
		mu 0 4 122 123 130 129
		f 4 101 210 -108 -216
		mu 0 4 123 124 131 130
		f 4 102 217 -109 -217
		mu 0 4 125 126 133 132
		f 4 103 218 -110 -218
		mu 0 4 126 127 134 133
		f 4 104 219 -111 -219
		mu 0 4 127 128 135 134
		f 4 105 220 -112 -220
		mu 0 4 128 129 136 135
		f 4 106 221 -113 -221
		mu 0 4 129 130 137 136
		f 4 107 216 -114 -222
		mu 0 4 130 131 138 137
		f 3 -1 -223 223
		mu 0 3 1 0 145
		f 3 -2 -224 224
		mu 0 3 2 1 145
		f 3 -3 -225 225
		mu 0 3 3 2 145
		f 3 -4 -226 226
		mu 0 3 4 3 145
		f 3 -5 -227 227
		mu 0 3 5 4 145
		f 3 -6 -228 222
		mu 0 3 0 5 145
		f 3 108 229 -229
		mu 0 3 143 142 146
		f 3 109 230 -230
		mu 0 3 142 141 146
		f 3 110 231 -231
		mu 0 3 141 140 146
		f 3 111 232 -232
		mu 0 3 140 139 146
		f 3 112 233 -233
		mu 0 3 139 144 146
		f 3 113 228 -234
		mu 0 3 144 143 146;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ai_translator" -type "string" "polymesh";
createNode transform -n "pCylinder2";
	rename -uid "CC193863-4B5B-5165-AAF0-07B068A81981";
createNode mesh -n "pCylinderShape2" -p "pCylinder2";
	rename -uid "689663C7-4271-E0F4-011F-D2B2AB653F43";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 84 ".uvst[0].uvsp[0:83]" -type "float2" 0.64860266 0.10796607
		 0.62640899 0.064408496 0.59184152 0.029841021 0.54828393 0.0076473355 0.5 -7.4505806e-08
		 0.45171607 0.0076473504 0.40815851 0.029841051 0.37359107 0.064408526 0.3513974 0.1079661
		 0.34374997 0.15625 0.3513974 0.2045339 0.37359107 0.24809146 0.40815854 0.28265893
		 0.4517161 0.3048526 0.5 0.3125 0.54828387 0.3048526 0.59184146 0.28265893 0.62640893
		 0.24809146 0.6486026 0.2045339 0.65625 0.15625 0.375 0.3125 0.38749999 0.3125 0.39999998
		 0.3125 0.41249996 0.3125 0.42499995 0.3125 0.43749994 0.3125 0.44999993 0.3125 0.46249992
		 0.3125 0.4749999 0.3125 0.48749989 0.3125 0.49999988 0.3125 0.51249987 0.3125 0.52499986
		 0.3125 0.53749985 0.3125 0.54999983 0.3125 0.56249982 0.3125 0.57499981 0.3125 0.5874998
		 0.3125 0.59999979 0.3125 0.61249977 0.3125 0.62499976 0.3125 0.375 0.68843985 0.38749999
		 0.68843985 0.39999998 0.68843985 0.41249996 0.68843985 0.42499995 0.68843985 0.43749994
		 0.68843985 0.44999993 0.68843985 0.46249992 0.68843985 0.4749999 0.68843985 0.48749989
		 0.68843985 0.49999988 0.68843985 0.51249987 0.68843985 0.52499986 0.68843985 0.53749985
		 0.68843985 0.54999983 0.68843985 0.56249982 0.68843985 0.57499981 0.68843985 0.5874998
		 0.68843985 0.59999979 0.68843985 0.61249977 0.68843985 0.62499976 0.68843985 0.64860266
		 0.79546607 0.62640899 0.75190848 0.59184152 0.71734101 0.54828393 0.69514734 0.5
		 0.68749994 0.45171607 0.69514734 0.40815851 0.71734107 0.37359107 0.75190854 0.3513974
		 0.79546607 0.34374997 0.84375 0.3513974 0.89203393 0.37359107 0.93559146 0.40815854
		 0.97015893 0.4517161 0.9923526 0.5 1 0.54828387 0.9923526 0.59184146 0.97015893 0.62640893
		 0.93559146 0.6486026 0.89203393 0.65625 0.84375 0.5 0.15000001 0.5 0.83749998;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 42 ".pt[8:41]" -type "float3"  0 0 -5.9604645e-08 0 0 0 
		0 0 5.9604645e-08 0 0 0 0 0 0 -5.9604645e-08 0 0 0 0 0 0 0 0 0 0 -1.1920929e-07 0 
		0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 -5.9604645e-08 
		0 0 0 0 0 5.9604645e-08 0 0 0 0 0 0 -5.9604645e-08 0 0 0 0 0 0 0 0 0 0 -1.1920929e-07 
		0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;
	setAttr -s 42 ".vt[0:41]"  2.92944717 -3.080200911 -0.95183498 2.49193645 -3.080200911 -1.81049776
		 1.81049776 -3.080200911 -2.49193645 0.95183492 -3.080200911 -2.9294467 0 -3.080200911 -3.080202341
		 -0.95183492 -3.080200911 -2.92944646 -1.8104974 -3.080200911 -2.49193573 -2.49193573 -3.080200911 -1.81049716
		 -2.92944598 -3.080200911 -0.95183468 -3.080201626 -3.080200911 0 -2.92944598 -3.080200911 0.95183468
		 -2.49193549 -3.080200911 1.81049705 -1.81049705 -3.080200911 2.49193525 -0.95183468 -3.080200911 2.92944551
		 -9.1797141e-08 -3.080200911 3.080201387 0.95183438 -3.080200911 2.92944551 1.81049669 -3.080200911 2.49193478
		 2.49193501 -3.080200911 1.81049681 2.92944527 -3.080200911 0.95183444 3.080200911 -3.080200911 0
		 2.92944717 3.080200911 -0.95183498 2.49193645 3.080200911 -1.81049776 1.81049776 3.080200911 -2.49193645
		 0.95183492 3.080200911 -2.9294467 0 3.080200911 -3.080202341 -0.95183492 3.080200911 -2.92944646
		 -1.8104974 3.080200911 -2.49193573 -2.49193573 3.080200911 -1.81049716 -2.92944598 3.080200911 -0.95183468
		 -3.080201626 3.080200911 0 -2.92944598 3.080200911 0.95183468 -2.49193549 3.080200911 1.81049705
		 -1.81049705 3.080200911 2.49193525 -0.95183468 3.080200911 2.92944551 -9.1797141e-08 3.080200911 3.080201387
		 0.95183438 3.080200911 2.92944551 1.81049669 3.080200911 2.49193478 2.49193501 3.080200911 1.81049681
		 2.92944527 3.080200911 0.95183444 3.080200911 3.080200911 0 0 -3.080200911 0 0 3.080200911 0;
	setAttr -s 100 ".ed[0:99]"  0 1 0 1 2 0 2 3 0 3 4 0 4 5 0 5 6 0 6 7 0
		 7 8 0 8 9 0 9 10 0 10 11 0 11 12 0 12 13 0 13 14 0 14 15 0 15 16 0 16 17 0 17 18 0
		 18 19 0 19 0 0 20 21 0 21 22 0 22 23 0 23 24 0 24 25 0 25 26 0 26 27 0 27 28 0 28 29 0
		 29 30 0 30 31 0 31 32 0 32 33 0 33 34 0 34 35 0 35 36 0 36 37 0 37 38 0 38 39 0 39 20 0
		 0 20 1 1 21 1 2 22 1 3 23 1 4 24 1 5 25 1 6 26 1 7 27 1 8 28 1 9 29 1 10 30 1 11 31 1
		 12 32 1 13 33 1 14 34 1 15 35 1 16 36 1 17 37 1 18 38 1 19 39 1 40 0 1 40 1 1 40 2 1
		 40 3 1 40 4 1 40 5 1 40 6 1 40 7 1 40 8 1 40 9 1 40 10 1 40 11 1 40 12 1 40 13 1
		 40 14 1 40 15 1 40 16 1 40 17 1 40 18 1 40 19 1 20 41 1 21 41 1 22 41 1 23 41 1 24 41 1
		 25 41 1 26 41 1 27 41 1 28 41 1 29 41 1 30 41 1 31 41 1 32 41 1 33 41 1 34 41 1 35 41 1
		 36 41 1 37 41 1 38 41 1 39 41 1;
	setAttr -s 60 -ch 200 ".fc[0:59]" -type "polyFaces" 
		f 4 0 41 -21 -41
		mu 0 4 20 21 42 41
		f 4 1 42 -22 -42
		mu 0 4 21 22 43 42
		f 4 2 43 -23 -43
		mu 0 4 22 23 44 43
		f 4 3 44 -24 -44
		mu 0 4 23 24 45 44
		f 4 4 45 -25 -45
		mu 0 4 24 25 46 45
		f 4 5 46 -26 -46
		mu 0 4 25 26 47 46
		f 4 6 47 -27 -47
		mu 0 4 26 27 48 47
		f 4 7 48 -28 -48
		mu 0 4 27 28 49 48
		f 4 8 49 -29 -49
		mu 0 4 28 29 50 49
		f 4 9 50 -30 -50
		mu 0 4 29 30 51 50
		f 4 10 51 -31 -51
		mu 0 4 30 31 52 51
		f 4 11 52 -32 -52
		mu 0 4 31 32 53 52
		f 4 12 53 -33 -53
		mu 0 4 32 33 54 53
		f 4 13 54 -34 -54
		mu 0 4 33 34 55 54
		f 4 14 55 -35 -55
		mu 0 4 34 35 56 55
		f 4 15 56 -36 -56
		mu 0 4 35 36 57 56
		f 4 16 57 -37 -57
		mu 0 4 36 37 58 57
		f 4 17 58 -38 -58
		mu 0 4 37 38 59 58
		f 4 18 59 -39 -59
		mu 0 4 38 39 60 59
		f 4 19 40 -40 -60
		mu 0 4 39 40 61 60
		f 3 -1 -61 61
		mu 0 3 1 0 82
		f 3 -2 -62 62
		mu 0 3 2 1 82
		f 3 -3 -63 63
		mu 0 3 3 2 82
		f 3 -4 -64 64
		mu 0 3 4 3 82
		f 3 -5 -65 65
		mu 0 3 5 4 82
		f 3 -6 -66 66
		mu 0 3 6 5 82
		f 3 -7 -67 67
		mu 0 3 7 6 82
		f 3 -8 -68 68
		mu 0 3 8 7 82
		f 3 -9 -69 69
		mu 0 3 9 8 82
		f 3 -10 -70 70
		mu 0 3 10 9 82
		f 3 -11 -71 71
		mu 0 3 11 10 82
		f 3 -12 -72 72
		mu 0 3 12 11 82
		f 3 -13 -73 73
		mu 0 3 13 12 82
		f 3 -14 -74 74
		mu 0 3 14 13 82
		f 3 -15 -75 75
		mu 0 3 15 14 82
		f 3 -16 -76 76
		mu 0 3 16 15 82
		f 3 -17 -77 77
		mu 0 3 17 16 82
		f 3 -18 -78 78
		mu 0 3 18 17 82
		f 3 -19 -79 79
		mu 0 3 19 18 82
		f 3 -20 -80 60
		mu 0 3 0 19 82
		f 3 20 81 -81
		mu 0 3 80 79 83
		f 3 21 82 -82
		mu 0 3 79 78 83
		f 3 22 83 -83
		mu 0 3 78 77 83
		f 3 23 84 -84
		mu 0 3 77 76 83
		f 3 24 85 -85
		mu 0 3 76 75 83
		f 3 25 86 -86
		mu 0 3 75 74 83
		f 3 26 87 -87
		mu 0 3 74 73 83
		f 3 27 88 -88
		mu 0 3 73 72 83
		f 3 28 89 -89
		mu 0 3 72 71 83
		f 3 29 90 -90
		mu 0 3 71 70 83
		f 3 30 91 -91
		mu 0 3 70 69 83
		f 3 31 92 -92
		mu 0 3 69 68 83
		f 3 32 93 -93
		mu 0 3 68 67 83
		f 3 33 94 -94
		mu 0 3 67 66 83
		f 3 34 95 -95
		mu 0 3 66 65 83
		f 3 35 96 -96
		mu 0 3 65 64 83
		f 3 36 97 -97
		mu 0 3 64 63 83
		f 3 37 98 -98
		mu 0 3 63 62 83
		f 3 38 99 -99
		mu 0 3 62 81 83
		f 3 39 80 -100
		mu 0 3 81 80 83;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ai_translator" -type "string" "polymesh";
createNode lightLinker -s -n "lightLinker1";
	rename -uid "BA785A3B-4045-0D70-9BD0-5A938FA1F467";
	setAttr -s 2 ".lnk";
	setAttr -s 2 ".slnk";
createNode shapeEditorManager -n "shapeEditorManager";
	rename -uid "0229F6AD-41DD-5379-857E-E881901DE155";
createNode poseInterpolatorManager -n "poseInterpolatorManager";
	rename -uid "FF133899-4DF8-9C9A-32EE-A6A5EF28167F";
createNode displayLayerManager -n "layerManager";
	rename -uid "FCAFCC7D-4132-BEF2-A0AC-8CB55F28F9FA";
createNode displayLayer -n "defaultLayer";
	rename -uid "00D614D4-48EF-1BC4-B005-859D7075FC80";
createNode renderLayerManager -n "renderLayerManager";
	rename -uid "0E084BC0-435B-9C36-D2A6-96B81612E1BB";
createNode renderLayer -n "defaultRenderLayer";
	rename -uid "47331998-41B0-D8B6-8564-DF9107271597";
	setAttr ".g" yes;
createNode ikSplineSolver -n "ikSplineSolver";
	rename -uid "6EAC1665-4DBA-31D3-2A68-FAA39D2C9545";
createNode makeNurbCircle -n "makeNurbCircle1";
	rename -uid "86D9AD34-4957-08A3-3C7E-2EA7B24647FF";
	setAttr ".nr" -type "double3" 90 0 1 ;
createNode makeNurbCircle -n "makeNurbCircle2";
	rename -uid "142FF99B-4E4D-FE20-7D2B-788FCFB870DA";
	setAttr ".nr" -type "double3" 90 0 1 ;
createNode makeNurbCircle -n "makeNurbCircle3";
	rename -uid "E2B98F1F-447A-43AC-F3A6-FCA199E94D9E";
	setAttr ".nr" -type "double3" 90 0 1 ;
createNode makeNurbCircle -n "makeNurbCircle4";
	rename -uid "A5EBAB4E-4A5B-0843-9C73-B1BFB9A52A34";
	setAttr ".nr" -type "double3" 90 0 1 ;
createNode makeNurbCircle -n "makeNurbCircle5";
	rename -uid "6CA2B691-436B-F8DB-53A4-36B4EEB85607";
	setAttr ".nr" -type "double3" 90 0 1 ;
createNode skinCluster -n "skinCluster1";
	rename -uid "64C62D9F-4467-C911-2E40-93AA9A5BDE49";
	setAttr -s 116 ".wl";
	setAttr ".wl[0:99].w"
		5 0 0.00065653099972376211 1 0.0024927866038792338 2 0.01779618391024337 
		3 0.48952724924307683 4 0.48952724924307683
		5 0 0.00065653072757117497 1 0.002492785608485531 2 0.017796177734404124 
		3 0.48952725296476957 4 0.48952725296476957
		5 0 0.00065653104061780048 1 0.0024927867534485183 2 0.017796184838233784 
		3 0.48952724868384995 4 0.48952724868384995
		5 0 0.00065653143994685967 1 0.0024927882139880713 2 0.0177961939000316 
		3 0.48952724322301672 4 0.48952724322301672
		5 0 0.00065653133527275088 1 0.0024927878311442231 2 0.017796191524708453 
		3 0.48952724465443731 4 0.48952724465443731
		5 0 0.00065653104061780048 1 0.0024927867534485183 2 0.017796184838233784 
		3 0.48952724868384995 4 0.48952724868384995
		5 0 0.00036847475488323246 1 0.0015758645021122575 2 0.014512232018815035 
		3 0.49177171436209477 4 0.49177171436209477
		5 0 0.00036847451457504337 1 0.0015758635057186838 2 0.014512223979937853 
		3 0.49177171899988426 4 0.49177171899988426
		5 0 0.00036847479099228809 1 0.0015758646518317938 2 0.014512233226748224 
		3 0.49177171366521388 4 0.49177171366521388
		5 0 0.00036847514359616664 1 0.0015758661138386661 2 0.014512245022179305 
		3 0.491771706860193 4 0.49177170686019289
		5 0 0.00036847505116988755 1 0.001575865730610174 2 0.014512241930302601 
		3 0.49177170864395864 4 0.49177170864395864
		5 0 0.00036847479099228809 1 0.0015758646518317938 2 0.014512233226748224 
		3 0.49177171366521388 4 0.49177171366521388
		5 0 0.00039372881856146002 1 0.0019394904529973561 2 0.024491404031631005 
		3 0.49481073302657258 4 0.47836464367023762
		5 0 0.00039372853100941334 1 0.0019394890882245147 2 0.024491389831554192 
		3 0.49481074424520666 4 0.47836464830400538
		5 0 0.00039372886176944702 1 0.001939490658070095 2 0.024491406165354789 
		3 0.49481073134084491 4 0.4783646429739607
		5 0 0.0003937292836941907 1 0.0019394926605993954 2 0.024491427001102278 
		3 0.49481071487976852 4 0.4783646361748356
		5 0 0.00039372917309718079 1 0.0019394921356864769 2 0.024491421539533289 
		3 0.49481071919462666 4 0.47836463795705642
		5 0 0.00039372886176944702 1 0.001939490658070095 2 0.024491406165354789 
		3 0.49481073134084491 4 0.4783646429739607
		5 0 0.00068773909260234662 1 0.0040158297187936672 2 0.074336036970173602 
		3 0.61044234476831782 4 0.31051804945011252
		5 0 0.00068773865315405918 1 0.0040158273007177905 2 0.074336007638112239 
		3 0.61044241184176418 4 0.31051801456625172
		5 0 0.00068773915863448081 1 0.0040158300821372273 2 0.074336041377650333 
		3 0.61044233468976894 4 0.31051805469180899
		5 0 0.00068773980343630407 1 0.0040158336301761013 2 0.074336084416516512 
		3 0.6104422362730989 4 0.31051810587677214
		5 0 0.00068773963441765495 1 0.0040158327001466 2 0.074336073134958061 
		3 0.61044226207055396 4 0.31051809245992368
		5 0 0.00068773915863448081 1 0.0040158300821372273 2 0.074336041377650333 
		3 0.61044233468976894 4 0.31051805469180899
		5 0 0.0010746617347223804 1 0.0077219095965127167 2 0.21465113331383756 
		3 0.65257758892488482 4 0.12397470643004252
		5 0 0.001074661076859437 1 0.0077219052775421232 2 0.21465109055475473 
		3 0.65257767458085636 4 0.12397466850998747
		5 0 0.0010746618335738163 1 0.0077219102454874422 2 0.21465113973887581 
		3 0.6525775760540995 4 0.12397471212796345
		5 0 0.0010746627988550859 1 0.007721916582705473 2 0.21465120247914232 
		3 0.65257745037133752 4 0.1239747677679596
		5 0 0.0010746625458307841 1 0.0077219149215626099 2 0.21465118603336023 
		3 0.65257748331591348 4 0.1239747531833329
		5 0 0.0010746618335738163 1 0.0077219102454874422 2 0.21465113973887581 
		3 0.6525775760540995 4 0.12397471212796345
		5 0 0.0013271557496387818 1 0.012320340852806044 2 0.41664259148985827 
		3 0.53080307880030086 4 0.038906833107396052
		5 0 0.0013271548627738852 1 0.012320333596871676 2 0.41664258295156853 
		3 0.53080311482615183 4 0.038906813762634031
		5 0 0.0013271558829003887 1 0.012320341943093189 2 0.41664259277283172 
		3 0.53080307338700705 4 0.03890683601416773
		5 0 0.0013271571841959849 1 0.012320352589713488 2 0.41664260530101371 
		3 0.53080302052637784 4 0.038906864398698934
		5 0 0.0013271568430939323 1 0.012320349798968787 2 0.41664260201706832 
		3 0.53080303438246279 4 0.038906856958406032
		5 0 0.0013271558829003887 1 0.012320341943093189 2 0.41664259277283172 
		3 0.53080307338700705 4 0.03890683601416773
		5 0 0.001942507522946661 1 0.024773884617994742 2 0.48878205874035496 
		3 0.46891600346995033 4 0.015585545648753378
		5 0 0.001942506178057631 1 0.024773870577439436 2 0.48878207519543282 
		3 0.46891601179574771 4 0.015585536253322282
		5 0 0.0019425077250316443 1 0.024773886727748749 2 0.48878205626779159 
		3 0.46891600221890356 4 0.015585547060524447
		5 0 0.0019425096983854233 1 0.024773907329430148 2 0.48878203212329091 
		3 0.46891599000246897 4 0.015585560846424625
		5 0 0.0019425091811201476 1 0.024773901929215865 2 0.48878203845216611 
		3 0.46891599320470162 4 0.015585557232796402
		5 0 0.0019425077250316443 1 0.024773886727748749 2 0.48878205626779159 
		3 0.46891600221890356 4 0.015585547060524447
		5 0 0.004066641778952846 1 0.076155466014936266 2 0.60861674668459909 
		3 0.30168407065800651 4 0.0094770748635053335
		5 0 0.0040666393597757772 1 0.076155436761606785 2 0.60861681767272624 
		3 0.30168403666405191 4 0.0094770695418394529
		5 0 0.0040666421424618987 1 0.076155470410582973 2 0.60861673601782373 
		3 0.30168407576598483 4 0.0094770756631465582
		5 0 0.0040666456921165158 1 0.076155513333925159 2 0.60861663185715065 
		3 0.30168412564518987 4 0.0094770834716177785
		5 0 0.0040666447616635034 1 0.076155502082648666 2 0.60861665916025154 
		3 0.30168411257061362 4 0.0094770814248227708
		5 0 0.0040666421424618987 1 0.076155470410582973 2 0.60861673601782373 
		3 0.30168407576598483 4 0.0094770756631465582
		5 0 0.0078041189728576682 1 0.21919528595390531 2 0.64791572978372014 
		3 0.11966584050132925 4 0.0054190247881877058
		5 0 0.0078041146283815933 1 0.21919524407910324 2 0.64791581604060011 
		3 0.11966580355726888 4 0.005419021694646118
		5 0 0.00780411962566492 1 0.21919529224607054 2 0.64791571682264093 
		3 0.11966584605259589 4 0.0054190252530277499
		5 0 0.0078041260003070961 1 0.21919535368883247 2 0.64791559025816647 
		3 0.11966590026051795 4 0.0054190297921760909
		5 0 0.0078041243293544438 1 0.21919533758315893 2 0.647915623433861 
		3 0.11966588605127348 4 0.0054190286023521181
		5 0 0.00780411962566492 1 0.21919529224607054 2 0.64791571682264093 
		3 0.11966584605259589 4 0.0054190252530277499
		5 0 0.012475466234957587 1 0.42075706957944542 2 0.52657964428747495 
		3 0.037635058986000433 4 0.0025527609121216766
		5 0 0.012475458879253592 1 0.42075706274589231 2 0.52657967903121616 
		3 0.037635040103395336 4 0.0025527592402425649
		5 0 0.01247546734023635 1 0.42075707060626338 2 0.52657963906683158 
		3 0.037635061823327945 4 0.0025527611633406788
		5 0 0.012475478133248523 1 0.42075708063309081 2 0.52657958808743655 
		3 0.03763508952973757 4 0.0025527636164864565
		5 0 0.012475475304130882 1 0.42075707800481277 2 0.52657960145040339 
		3 0.037635082267197237 4 0.002552762973455738
		5 0 0.01247546734023635 1 0.42075707060626338 2 0.52657963906683158 
		3 0.037635061823327945 4 0.0025527611633406788
		5 0 0.025477445938530303 1 0.49082746781883152 2 0.46691510282691612 
		3 0.01531393539591208 4 0.0014660480198099065
		5 0 0.025477431586777358 1 0.49082748500313256 2 0.46691511025095683 
		3 0.015313926161893861 4 0.0014660469972392171
		5 0 0.02547744809504545 1 0.49082746523669379 2 0.46691510171136885 
		3 0.015313936783429086 4 0.001466048173462876
		5 0 0.02547746915334664 1 0.49082744002220707 2 0.46691509081807825 
		3 0.015313950332488502 4 0.0014660496738794348
		5 0 0.025477463633440965 1 0.49082744663155181 2 0.46691509367348216 
		3 0.015313946780942164 4 0.0014660492805828086
		5 0 0.02547744809504545 1 0.49082746523669379 2 0.46691510171136885 
		3 0.015313936783429086 4 0.001466048173462876
		5 0 0.078949588035124113 1 0.6139789115657035 2 0.29650138825850658 
		3 0.009382740197484583 4 0.0011873719431813058
		5 0 0.078949558000858872 1 0.61397898314335575 2 0.29650135273400313 
		3 0.0093827349197646258 4 0.0011873712020176426
		5 0 0.07894959254811551 1 0.61397890081034512 2 0.29650139359646716 
		3 0.0093827409905224528 4 0.001187372054549641
		5 0 0.078949636617322627 1 0.61397879578466441 2 0.29650144572144305 
		3 0.0093827487345119354 4 0.0011873731420579674
		5 0 0.078949625065686521 1 0.61397882331450537 2 0.29650143205819401 
		3 0.0093827467046192058 4 0.001187372856994904
		5 0 0.07894959254811551 1 0.61397890081034512 2 0.29650139359646716 
		3 0.0093827409905224528 4 0.001187372054549641
		5 0 0.22636512763582559 1 0.65060651150642657 2 0.11682662938238308 
		3 0.005353126970681057 4 0.00084860450468371602
		5 0 0.22636508478603434 1 0.65060659511581564 2 0.11682659223128075 
		3 0.005353123886933632 4 0.00084860397993547247
		5 0 0.22636513407449477 1 0.65060649894316214 2 0.11682663496476051 
		3 0.0053531274340494388 4 0.00084860458353315483
		5 0 0.22636519694785665 1 0.65060637626334417 2 0.11682668947647694 
		3 0.0053531319588269064 4 0.00084860535349545209
		5 0 0.22636518046718745 1 0.65060640842077311 2 0.11682667518760033 
		3 0.0053531307727699038 4 0.00084860515166912637
		5 0 0.22636513407449477 1 0.65060649894316214 2 0.11682663496476051 
		3 0.0053531274340494388 4 0.00084860458353315483
		5 0 0.43050746539085277 1 0.52957104526090726 2 0.036909060239297353 
		3 0.0025303956713754682 4 0.00048203343756712613
		5 0 0.43050745670664087 1 0.52957107494401234 2 0.03690904125896452 
		3 0.002530393988036464 4 0.00048203310234585167
		5 0 0.43050746669575363 1 0.52957104080068207 2 0.03690906309130966 
		3 0.0025303959243164593 4 0.00048203348793796844
		5 0 0.43050747943805201 1 0.52957099724674705 2 0.036909090941115941 
		3 0.0025303983942773817 4 0.00048203397980769877
		5 0 0.43050747609798096 1 0.52957100866331597 2 0.036909083640987723 
		3 0.0025303977468389915 4 0.00048203385087636571
		5 0 0.43050746669575363 1 0.52957104080068207 2 0.03690906309130966 
		3 0.0025303959243164593 4 0.00048203348793796844
		5 0 0.50589350097272467 1 0.47683836382400047 2 0.015445730210061282 
		3 0.0014916510986159404 4 0.000330753894597655
		5 0 0.50589351209582412 1 0.47683836354105269 2 0.015445720672634932 
		3 0.0014916500383532925 4 0.00033075365213503508
		5 0 0.50589349930135197 1 0.47683836386651607 2 0.015445731643168889 
		3 0.0014916512579325667 4 0.00033075393103044586
		5 0 0.50589348298045689 1 0.47683836428167398 2 0.015445745637419161 
		3 0.0014916528136545426 4 0.00033075428679554282
		5 0 0.50589348725856942 1 0.47683836417285186 2 0.015445741969177145 
		3 0.0014916524058609818 4 0.00033075419354062927
		5 0 0.50589349930135197 1 0.47683836386651607 2 0.015445731643168889 
		3 0.0014916512579325667 4 0.00033075393103044586
		5 0 0.6721490907842147 1 0.31616117774196245 2 0.010081393236231098 
		3 0.0012848033427238985 4 0.00032353489486779987
		5 0 0.67214914792758029 1 0.31616112765697801 2 0.010081387238327478 
		3 0.0012848024999350387 4 0.00032353467717915026
		5 0 0.67214908219777203 1 0.31616118526780257 2 0.010081394137484875 
		3 0.0012848034693625921 4 0.00032353492757801705
		5 0 0.67214899835148145 1 0.31616125875734158 2 0.010081402938199221 
		3 0.0012848047059854963 4 0.00032353524699227728
		5 0 0.67214902032967716 1 0.31616123949390884 2 0.010081400631312508 
		3 0.0012848043818357755 4 0.00032353516326582801
		5 0 0.67214908219777203 1 0.31616118526780257 2 0.010081394137484875 
		3 0.0012848034693625921 4 0.00032353492757801705
		5 0 0.84435446095266675 1 0.1474153623585 2 0.0068348123063548772 
		3 0.001089694575562307 4 0.000305669806916054
		5 0 0.84435452205356742 1 0.14741530652794213 2 0.0068348079814107374 
		3 0.0010896938403890167 4 0.00030566959669062947
		5 0 0.84435445177155777 1 0.14741537074767949 2 0.0068348129562273178 
		3 0.0010896946860305269 4 0.00030566983850483577
		5 0 0.84435436211835013 1 0.14741545266772133 2 0.0068348193022110771 
		3 0.0010896957647492428 4 0.00030567014696830923;
	setAttr ".wl[100:115].w"
		5 0 0.84435438561868692 1 0.14741543119444006 2 0.0068348176387704514 
		3 0.0010896954819901517 4 0.00030567006611233524
		5 0 0.84435445177155777 1 0.14741537074767949 2 0.0068348129562273178 
		3 0.0010896946860305269 4 0.00030566983850483577
		5 0 0.93121922651158717 1 0.063297184070566018 2 0.0043858625583012359 
		3 0.00083942271496699049 4 0.00025830414457863075
		5 0 0.93121926399525912 1 0.063297150359093987 2 0.0043858595696384768 
		3 0.00083942211784871813 4 0.00025830395815976018
		5 0 0.93121922087923603 1 0.063297189136100843 2 0.0043858630073821065 
		3 0.00083942280469086422 4 0.00025830417259020596
		5 0 0.93121916587951414 1 0.063297238600879061 2 0.0043858673926426683 
		3 0.00083942368084170241 4 0.00025830444612237022
		5 0 0.93121918029631179 1 0.06329722563492822 2 0.004385866243156465 
		3 0.00083942345118070223 4 0.00025830437442276303
		5 0 0.93121922087923603 1 0.063297189136100843 2 0.0043858630073821065 
		3 0.00083942280469086422 4 0.00025830417259020596
		5 0 0.9651928899761909 1 0.03090305509965733 2 0.003010472615701048 
		3 0.00067014414762585502 4 0.00022343816082483873
		5 0 0.96519291099232052 1 0.030903036779280645 2 0.0030104705536186183 
		3 0.00067014367379991961 4 0.0002234380009803728
		5 0 0.96519288681827653 1 0.030903057852503975 2 0.0030104729255526 
		3 0.00067014421882364097 4 0.00022343818484330493
		5 0 0.96519285598134386 1 0.030903084733962246 2 0.0030104759512433145 
		3 0.00067014491406781776 4 0.00022343841938288539
		5 0 0.96519286406447291 1 0.030903077687661783 2 0.0030104751581342746 
		3 0.00067014473182696655 4 0.00022343835790420693
		5 0 0.96519288681827653 1 0.030903057852503975 2 0.0030104729255526 
		3 0.00067014421882364097 4 0.00022343818484330493
		5 0 0.00013135934740864246 1 0.00051938765021362692 2 0.0042899487753954389 
		3 0.49752965211349115 4 0.49752965211349115
		5 0 0.99994090740871155 1 5.3956751945424881e-05 2 4.0180231523363598e-06 
		3 8.4288559036151561e-07 4 2.7493060043997559e-07;
	setAttr -s 5 ".pm";
	setAttr ".pm[0]" -type "matrix" 0 -0 1 -0 -0 1 -0 0 -1 -0 0 -0 -2.4919918419480369e-16 -6.9172255761933599 -0 1;
	setAttr ".pm[1]" -type "matrix" 0 -0 1 -0 -0 1 -0 0 -1 -0 0 -0 -2.0000000000000004 -6.9172255761933581 -0 1;
	setAttr ".pm[2]" -type "matrix" 0 -0 1 -0 -0 1 -0 0 -1 -0 0 -0 -4 -6.9172255761933563 -0 1;
	setAttr ".pm[3]" -type "matrix" 0 -0 1 -0 -0 1 -0 0 -1 -0 0 -0 -6 -6.9172255761933563 -0 1;
	setAttr ".pm[4]" -type "matrix" 1 -0 0 -0 -0 1 -0 0 0 -0 1 -0 -0 -6.9172255761933528 8 1;
	setAttr ".gm" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
	setAttr -s 5 ".ma";
	setAttr -s 5 ".dpf[0:4]"  4 4 4 4 4;
	setAttr -s 5 ".lw";
	setAttr -s 5 ".lw";
	setAttr ".mmi" yes;
	setAttr ".mi" 5;
	setAttr ".ucm" yes;
	setAttr -s 5 ".ifcl";
	setAttr -s 5 ".ifcl";
createNode tweak -n "tweak1";
	rename -uid "E04E1BF1-49DB-4D63-DF70-96A0D8402C65";
createNode objectSet -n "skinCluster1Set";
	rename -uid "D3D2EC7F-4CCD-DA2A-723B-599D7241F7F2";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "skinCluster1GroupId";
	rename -uid "DDB5EF0D-4521-0365-D3EF-19BB302A9D42";
	setAttr ".ihi" 0;
createNode groupParts -n "skinCluster1GroupParts";
	rename -uid "4B6A4130-4192-2EE2-DEED-3DA6E5C29CDC";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "vtx[*]";
createNode objectSet -n "tweakSet1";
	rename -uid "6EC5BD50-4A90-D9F4-0698-D79A55B7D2F4";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "groupId2";
	rename -uid "62206441-4E27-23DF-D164-47A1F1E8471A";
	setAttr ".ihi" 0;
createNode groupParts -n "groupParts2";
	rename -uid "016426E9-430A-4650-561B-3AB25C793CA3";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "vtx[*]";
createNode dagPose -n "bindPose1";
	rename -uid "C3BEC59E-46C9-392F-40DA-4AB730D37755";
	setAttr -s 5 ".wm";
	setAttr -s 5 ".xm";
	setAttr ".xm[0]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 6.9172255761933599 -2.4919918419480369e-16 0
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0.70710678118654757 0 0.70710678118654757 1
		 1 1 yes;
	setAttr ".xm[1]" -type "matrix" "xform" 1 1 1 0 0 0 0 2 -1.7763568394002505e-15
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[2]" -type "matrix" "xform" 1 1 1 0 0 0 0 1.9999999999999996 -1.7763568394002505e-15
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[3]" -type "matrix" "xform" 1 1 1 0 0 0 0 2 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[4]" -type "matrix" "xform" 1 1 1 0 0 0 0 2 -3.5527136788005009e-15
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 -0.70710678118654757 0 0.70710678118654757 1
		 1 1 yes;
	setAttr -s 5 ".m";
	setAttr -s 5 ".p";
	setAttr ".bp" yes;
createNode mute -n "aTools_StoreNode";
	rename -uid "D568D48E-49A2-86F5-ECAF-418C4A4FAFBF";
createNode mute -n "scene";
	rename -uid "D5BBFADA-4D1E-C13B-A811-16802767DC06";
	addAttr -ci true -sn "id" -ln "id" -dt "string";
	setAttr ".id" -type "string" "1718791162.1";
createNode animCurveTU -n "pCylinder2_scaleX";
	rename -uid "ABDE5608-40D5-27B5-4344-68B8C8E11E38";
	setAttr ".tan" 2;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  1 1;
createNode animCurveTU -n "pCylinder2_scaleY";
	rename -uid "A52BC7BB-4D5F-BEE9-745F-2A8F083CD7A7";
	setAttr ".tan" 2;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  1 1;
createNode animCurveTU -n "pCylinder2_scaleZ";
	rename -uid "471B87D8-459B-7799-9CD7-6282A1572A53";
	setAttr ".tan" 2;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  1 1;
createNode animCurveTU -n "pCylinder2_visibility";
	rename -uid "080D926A-493D-4A8F-A372-BC9EA42F8995";
	setAttr ".tan" 9;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  1 1;
	setAttr ".kot[0]"  5;
createNode animCurveTL -n "pCylinder2_translateX";
	rename -uid "7831CA64-4A17-7A6B-92FA-B5B079E521D5";
	setAttr ".tan" 2;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  1 0;
createNode animCurveTL -n "pCylinder2_translateY";
	rename -uid "C0435922-4DC2-6025-4554-49994EA32536";
	setAttr ".tan" 2;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  1 0;
createNode animCurveTL -n "pCylinder2_translateZ";
	rename -uid "3BB82DD7-4772-B93E-3BEC-9D9DFF80445B";
	setAttr ".tan" 2;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  1 0;
createNode animCurveTA -n "pCylinder2_rotateX";
	rename -uid "1E6EEE72-4F20-1B18-81C9-05ACD7580A2F";
	setAttr ".tan" 2;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  1 0;
createNode animCurveTA -n "pCylinder2_rotateY";
	rename -uid "7C50709B-4DF0-47C8-F74B-E19EB4F32DDB";
	setAttr ".tan" 2;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  1 0;
createNode animCurveTA -n "pCylinder2_rotateZ";
	rename -uid "4EEF0CFC-4AFC-6137-F937-1BA9BA19EBEB";
	setAttr ".tan" 2;
	setAttr ".wgt" no;
	setAttr ".ktv[0]"  1 0;
createNode script -n "uiConfigurationScriptNode";
	rename -uid "77A867A2-490A-413B-2B68-BC8D88E06A88";
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
		+ "            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 1106\n            -height 637\n            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"outlinerPanel\" (localizedPanelLabel(\"ToggledOutliner\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\toutlinerPanel -edit -l (localizedPanelLabel(\"ToggledOutliner\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\t$editorName = $panelName;\n        outlinerEditor -e \n            -docTag \"isolOutln_fromSeln\" \n            -showShapes 0\n            -showAssignedMaterials 0\n            -showTimeEditor 1\n            -showReferenceNodes 1\n            -showReferenceMembers 1\n            -showAttributes 0\n            -showConnected 0\n            -showAnimCurvesOnly 0\n            -showMuteInfo 0\n            -organizeByLayer 1\n            -organizeByClip 1\n            -showAnimLayerWeight 1\n            -autoExpandLayers 1\n            -autoExpand 0\n            -autoExpandAnimatedShapes 1\n            -showDagOnly 1\n            -showAssets 1\n            -showContainedOnly 1\n            -showPublishedAsConnected 0\n            -showParentContainers 0\n            -showContainerContents 1\n            -ignoreDagHierarchy 0\n            -expandConnections 0\n            -showUpstreamCurves 1\n            -showUnitlessCurves 1\n            -showCompounds 1\n            -showLeafs 1\n            -showNumericAttrsOnly 0\n            -highlightActive 1\n"
		+ "            -autoSelectNewObjects 0\n            -doNotSelectNewObjects 0\n            -dropIsParent 1\n            -transmitFilters 0\n            -setFilter \"defaultSetFilter\" \n            -showSetMembers 1\n            -allowMultiSelection 1\n            -alwaysToggleSelect 0\n            -directSelect 0\n            -isSet 0\n            -isSetMember 0\n            -displayMode \"DAG\" \n            -expandObjects 0\n            -setsIgnoreFilters 1\n            -containersIgnoreFilters 0\n            -editAttrName 0\n            -showAttrValues 0\n            -highlightSecondary 0\n            -showUVAttrsOnly 0\n            -showTextureNodesOnly 0\n            -attrAlphaOrder \"default\" \n            -animLayerFilterOptions \"allAffecting\" \n            -sortOrder \"none\" \n            -longNames 0\n            -niceNames 1\n            -selectCommand \"print(\\\"\\\")\" \n            -showNamespace 1\n            -showPinIcons 0\n            -mapMotionTrails 0\n            -ignoreHiddenAttribute 0\n            -ignoreOutlinerColor 0\n            -renderFilterVisible 0\n"
		+ "            -renderFilterIndex 0\n            -selectionOrder \"chronological\" \n            -expandAttribute 0\n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"outlinerPanel\" (localizedPanelLabel(\"Outliner\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\toutlinerPanel -edit -l (localizedPanelLabel(\"Outliner\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        outlinerEditor -e \n            -showShapes 0\n            -showAssignedMaterials 0\n            -showTimeEditor 1\n            -showReferenceNodes 0\n            -showReferenceMembers 0\n            -showAttributes 0\n            -showConnected 0\n            -showAnimCurvesOnly 0\n            -showMuteInfo 0\n            -organizeByLayer 1\n            -organizeByClip 1\n            -showAnimLayerWeight 1\n            -autoExpandLayers 1\n            -autoExpand 0\n            -autoExpandAnimatedShapes 1\n            -showDagOnly 1\n"
		+ "            -showAssets 1\n            -showContainedOnly 1\n            -showPublishedAsConnected 0\n            -showParentContainers 0\n            -showContainerContents 1\n            -ignoreDagHierarchy 0\n            -expandConnections 0\n            -showUpstreamCurves 1\n            -showUnitlessCurves 1\n            -showCompounds 1\n            -showLeafs 1\n            -showNumericAttrsOnly 0\n            -highlightActive 1\n            -autoSelectNewObjects 0\n            -doNotSelectNewObjects 0\n            -dropIsParent 1\n            -transmitFilters 0\n            -setFilter \"0\" \n            -showSetMembers 1\n            -allowMultiSelection 1\n            -alwaysToggleSelect 0\n            -directSelect 0\n            -displayMode \"DAG\" \n            -expandObjects 0\n            -setsIgnoreFilters 1\n            -containersIgnoreFilters 0\n            -editAttrName 0\n            -showAttrValues 0\n            -highlightSecondary 0\n            -showUVAttrsOnly 0\n            -showTextureNodesOnly 0\n            -attrAlphaOrder \"default\" \n"
		+ "            -animLayerFilterOptions \"allAffecting\" \n            -sortOrder \"none\" \n            -longNames 0\n            -niceNames 1\n            -showNamespace 1\n            -showPinIcons 0\n            -mapMotionTrails 0\n            -ignoreHiddenAttribute 0\n            -ignoreOutlinerColor 0\n            -renderFilterVisible 0\n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"graphEditor\" (localizedPanelLabel(\"Graph Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Graph Editor\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"OutlineEd\");\n            outlinerEditor -e \n                -showShapes 1\n                -showAssignedMaterials 0\n                -showTimeEditor 1\n                -showReferenceNodes 0\n                -showReferenceMembers 0\n                -showAttributes 1\n                -showConnected 1\n                -showAnimCurvesOnly 1\n"
		+ "                -showMuteInfo 0\n                -organizeByLayer 1\n                -organizeByClip 1\n                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n                -autoExpand 1\n                -autoExpandAnimatedShapes 1\n                -showDagOnly 0\n                -showAssets 1\n                -showContainedOnly 0\n                -showPublishedAsConnected 0\n                -showParentContainers 0\n                -showContainerContents 0\n                -ignoreDagHierarchy 0\n                -expandConnections 1\n                -showUpstreamCurves 1\n                -showUnitlessCurves 1\n                -showCompounds 0\n                -showLeafs 1\n                -showNumericAttrsOnly 1\n                -highlightActive 0\n                -autoSelectNewObjects 1\n                -doNotSelectNewObjects 0\n                -dropIsParent 1\n                -transmitFilters 1\n                -setFilter \"0\" \n                -showSetMembers 0\n                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n"
		+ "                -directSelect 0\n                -displayMode \"DAG\" \n                -expandObjects 0\n                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n                -showAttrValues 0\n                -highlightSecondary 0\n                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n                -animLayerFilterOptions \"allAffecting\" \n                -sortOrder \"none\" \n                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 1\n                -mapMotionTrails 1\n                -ignoreHiddenAttribute 0\n                -ignoreOutlinerColor 0\n                -renderFilterVisible 0\n                $editorName;\n\n\t\t\t$editorName = ($panelName+\"GraphEd\");\n            animCurveEditor -e \n                -displayValues 0\n                -snapTime \"integer\" \n                -snapValue \"none\" \n                -showPlayRangeShades \"on\" \n                -lockPlayRangeShades \"off\" \n"
		+ "                -smoothness \"fine\" \n                -resultSamples 1\n                -resultScreenSamples 0\n                -resultUpdate \"delayed\" \n                -showUpstreamCurves 1\n                -stackedCurvesMin -1\n                -stackedCurvesMax 1\n                -stackedCurvesSpace 0.2\n                -preSelectionHighlight 0\n                -constrainDrag 0\n                -valueLinesToggle 1\n                -highlightAffectedCurves 0\n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dopeSheetPanel\" (localizedPanelLabel(\"Dope Sheet\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Dope Sheet\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"OutlineEd\");\n            outlinerEditor -e \n                -showShapes 1\n                -showAssignedMaterials 0\n                -showTimeEditor 1\n                -showReferenceNodes 0\n"
		+ "                -showReferenceMembers 0\n                -showAttributes 1\n                -showConnected 1\n                -showAnimCurvesOnly 1\n                -showMuteInfo 0\n                -organizeByLayer 1\n                -organizeByClip 1\n                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n                -autoExpand 0\n                -autoExpandAnimatedShapes 1\n                -showDagOnly 0\n                -showAssets 1\n                -showContainedOnly 0\n                -showPublishedAsConnected 0\n                -showParentContainers 0\n                -showContainerContents 0\n                -ignoreDagHierarchy 0\n                -expandConnections 1\n                -showUpstreamCurves 1\n                -showUnitlessCurves 0\n                -showCompounds 1\n                -showLeafs 1\n                -showNumericAttrsOnly 1\n                -highlightActive 0\n                -autoSelectNewObjects 0\n                -doNotSelectNewObjects 1\n                -dropIsParent 1\n                -transmitFilters 0\n"
		+ "                -setFilter \"0\" \n                -showSetMembers 0\n                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n                -directSelect 0\n                -displayMode \"DAG\" \n                -expandObjects 0\n                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n                -showAttrValues 0\n                -highlightSecondary 0\n                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n                -animLayerFilterOptions \"allAffecting\" \n                -sortOrder \"none\" \n                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 0\n                -mapMotionTrails 1\n                -ignoreHiddenAttribute 0\n                -ignoreOutlinerColor 0\n                -renderFilterVisible 0\n                $editorName;\n\n\t\t\t$editorName = ($panelName+\"DopeSheetEd\");\n            dopeSheetEditor -e \n                -displayValues 0\n"
		+ "                -snapTime \"integer\" \n                -snapValue \"none\" \n                -outliner \"dopeSheetPanel1OutlineEd\" \n                -showSummary 1\n                -showScene 0\n                -hierarchyBelow 0\n                -showTicks 1\n                -selectionWindow 0 0 0 0 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"timeEditorPanel\" (localizedPanelLabel(\"Time Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Time Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"clipEditorPanel\" (localizedPanelLabel(\"Trax Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Trax Editor\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = clipEditorNameFromPanel($panelName);\n"
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
		+ "\t\t\t\t\t\"$panelName = `modelPanel -unParent -l (localizedPanelLabel(\\\"Persp View\\\")) -mbv $menusOkayInPanels `;\\n$editorName = $panelName;\\nmodelEditor -e \\n    -cam `findStartUpCamera persp` \\n    -useInteractiveMode 0\\n    -displayLights \\\"default\\\" \\n    -displayAppearance \\\"smoothShaded\\\" \\n    -activeOnly 0\\n    -ignorePanZoom 0\\n    -wireframeOnShaded 0\\n    -headsUpDisplay 1\\n    -holdOuts 1\\n    -selectionHiliteDisplay 1\\n    -useDefaultMaterial 0\\n    -bufferMode \\\"double\\\" \\n    -twoSidedLighting 0\\n    -backfaceCulling 0\\n    -xray 0\\n    -jointXray 0\\n    -activeComponentsXray 0\\n    -displayTextures 0\\n    -smoothWireframe 0\\n    -lineWidth 1\\n    -textureAnisotropic 0\\n    -textureHilight 1\\n    -textureSampling 2\\n    -textureDisplay \\\"modulate\\\" \\n    -textureMaxSize 32768\\n    -fogging 0\\n    -fogSource \\\"fragment\\\" \\n    -fogMode \\\"linear\\\" \\n    -fogStart 0\\n    -fogEnd 100\\n    -fogDensity 0.1\\n    -fogColor 0.5 0.5 0.5 1 \\n    -depthOfFieldPreview 1\\n    -maxConstantTransparency 1\\n    -rendererName \\\"vp2Renderer\\\" \\n    -objectFilterShowInHUD 1\\n    -isFiltered 0\\n    -colorResolution 256 256 \\n    -bumpResolution 512 512 \\n    -textureCompression 0\\n    -transparencyAlgorithm \\\"frontAndBackCull\\\" \\n    -transpInShadows 0\\n    -cullingOverride \\\"none\\\" \\n    -lowQualityLighting 0\\n    -maximumNumHardwareLights 1\\n    -occlusionCulling 0\\n    -shadingModel 0\\n    -useBaseRenderer 0\\n    -useReducedRenderer 0\\n    -smallObjectCulling 0\\n    -smallObjectThreshold -1 \\n    -interactiveDisableShadows 0\\n    -interactiveBackFaceCull 0\\n    -sortTransparent 1\\n    -controllers 1\\n    -nurbsCurves 1\\n    -nurbsSurfaces 1\\n    -polymeshes 1\\n    -subdivSurfaces 1\\n    -planes 1\\n    -lights 1\\n    -cameras 1\\n    -controlVertices 1\\n    -hulls 1\\n    -grid 1\\n    -imagePlane 1\\n    -joints 1\\n    -ikHandles 1\\n    -deformers 1\\n    -dynamics 1\\n    -particleInstancers 1\\n    -fluids 1\\n    -hairSystems 1\\n    -follicles 1\\n    -nCloths 1\\n    -nParticles 1\\n    -nRigids 1\\n    -dynamicConstraints 1\\n    -locators 1\\n    -manipulators 1\\n    -pluginShapes 1\\n    -dimensions 1\\n    -handles 1\\n    -pivots 1\\n    -textures 1\\n    -strokes 1\\n    -motionTrails 1\\n    -clipGhosts 1\\n    -greasePencils 1\\n    -shadows 0\\n    -captureSequenceNumber -1\\n    -width 1106\\n    -height 637\\n    -sceneRenderFilter 0\\n    $editorName;\\nmodelEditor -e -viewSelected 0 $editorName;\\nmodelEditor -e \\n    -pluginObjects \\\"gpuCacheDisplayFilter\\\" 1 \\n    $editorName\"\n"
		+ "\t\t\t\t\t\"modelPanel -edit -l (localizedPanelLabel(\\\"Persp View\\\")) -mbv $menusOkayInPanels  $panelName;\\n$editorName = $panelName;\\nmodelEditor -e \\n    -cam `findStartUpCamera persp` \\n    -useInteractiveMode 0\\n    -displayLights \\\"default\\\" \\n    -displayAppearance \\\"smoothShaded\\\" \\n    -activeOnly 0\\n    -ignorePanZoom 0\\n    -wireframeOnShaded 0\\n    -headsUpDisplay 1\\n    -holdOuts 1\\n    -selectionHiliteDisplay 1\\n    -useDefaultMaterial 0\\n    -bufferMode \\\"double\\\" \\n    -twoSidedLighting 0\\n    -backfaceCulling 0\\n    -xray 0\\n    -jointXray 0\\n    -activeComponentsXray 0\\n    -displayTextures 0\\n    -smoothWireframe 0\\n    -lineWidth 1\\n    -textureAnisotropic 0\\n    -textureHilight 1\\n    -textureSampling 2\\n    -textureDisplay \\\"modulate\\\" \\n    -textureMaxSize 32768\\n    -fogging 0\\n    -fogSource \\\"fragment\\\" \\n    -fogMode \\\"linear\\\" \\n    -fogStart 0\\n    -fogEnd 100\\n    -fogDensity 0.1\\n    -fogColor 0.5 0.5 0.5 1 \\n    -depthOfFieldPreview 1\\n    -maxConstantTransparency 1\\n    -rendererName \\\"vp2Renderer\\\" \\n    -objectFilterShowInHUD 1\\n    -isFiltered 0\\n    -colorResolution 256 256 \\n    -bumpResolution 512 512 \\n    -textureCompression 0\\n    -transparencyAlgorithm \\\"frontAndBackCull\\\" \\n    -transpInShadows 0\\n    -cullingOverride \\\"none\\\" \\n    -lowQualityLighting 0\\n    -maximumNumHardwareLights 1\\n    -occlusionCulling 0\\n    -shadingModel 0\\n    -useBaseRenderer 0\\n    -useReducedRenderer 0\\n    -smallObjectCulling 0\\n    -smallObjectThreshold -1 \\n    -interactiveDisableShadows 0\\n    -interactiveBackFaceCull 0\\n    -sortTransparent 1\\n    -controllers 1\\n    -nurbsCurves 1\\n    -nurbsSurfaces 1\\n    -polymeshes 1\\n    -subdivSurfaces 1\\n    -planes 1\\n    -lights 1\\n    -cameras 1\\n    -controlVertices 1\\n    -hulls 1\\n    -grid 1\\n    -imagePlane 1\\n    -joints 1\\n    -ikHandles 1\\n    -deformers 1\\n    -dynamics 1\\n    -particleInstancers 1\\n    -fluids 1\\n    -hairSystems 1\\n    -follicles 1\\n    -nCloths 1\\n    -nParticles 1\\n    -nRigids 1\\n    -dynamicConstraints 1\\n    -locators 1\\n    -manipulators 1\\n    -pluginShapes 1\\n    -dimensions 1\\n    -handles 1\\n    -pivots 1\\n    -textures 1\\n    -strokes 1\\n    -motionTrails 1\\n    -clipGhosts 1\\n    -greasePencils 1\\n    -shadows 0\\n    -captureSequenceNumber -1\\n    -width 1106\\n    -height 637\\n    -sceneRenderFilter 0\\n    $editorName;\\nmodelEditor -e -viewSelected 0 $editorName;\\nmodelEditor -e \\n    -pluginObjects \\\"gpuCacheDisplayFilter\\\" 1 \\n    $editorName\"\n"
		+ "\t\t\t\t$configName;\n\n            setNamedPanelLayout (localizedPanelLabel(\"Current Layout\"));\n        }\n\n        panelHistory -e -clear mainPanelHistory;\n        sceneUIReplacement -clear;\n\t}\n\n\ngrid -spacing 5 -size 12 -divisions 5 -displayAxes yes -displayGridLines yes -displayDivisionLines yes -displayPerspectiveLabels no -displayOrthographicLabels no -displayAxesBold yes -perspectiveLabelPosition axis -orthographicLabelPosition edge;\nviewManip -drawCompass 0 -compassAngle 0 -frontParameters \"\" -homeParameters \"\" -selectionLockParameters \"\";\n}\n");
	setAttr ".st" 3;
createNode script -n "sceneConfigurationScriptNode";
	rename -uid "40DE906E-45C4-4703-4D34-378857559341";
	setAttr ".b" -type "string" "playbackOptions -min 1 -max 2000 -ast 1 -aet 2000 ";
	setAttr ".st" 6;
createNode nodeGraphEditorInfo -n "MayaNodeEditorSavedTabsInfo";
	rename -uid "9BDF49F1-467C-E220-9A82-01B3F7CBEE96";
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -1281.4739304239165 -218.81319699979372 ;
	setAttr ".tgi[0].vh" -type "double2" 1095.0208205034912 991.90104060503052 ;
	setAttr -s 13 ".tgi[0].ni";
	setAttr ".tgi[0].ni[0].x" -271.42855834960938;
	setAttr ".tgi[0].ni[0].y" 467.14285278320313;
	setAttr ".tgi[0].ni[0].nvs" 18304;
	setAttr ".tgi[0].ni[1].x" -271.42855834960938;
	setAttr ".tgi[0].ni[1].y" -40;
	setAttr ".tgi[0].ni[1].nvs" 18304;
	setAttr ".tgi[0].ni[2].x" -799.39984130859375;
	setAttr ".tgi[0].ni[2].y" 591.03826904296875;
	setAttr ".tgi[0].ni[2].nvs" 18304;
	setAttr ".tgi[0].ni[3].x" 35.714286804199219;
	setAttr ".tgi[0].ni[3].y" 112.85713958740234;
	setAttr ".tgi[0].ni[3].nvs" 18304;
	setAttr ".tgi[0].ni[4].x" -271.42855834960938;
	setAttr ".tgi[0].ni[4].y" 365.71429443359375;
	setAttr ".tgi[0].ni[4].nvs" 18304;
	setAttr ".tgi[0].ni[5].x" -271.42855834960938;
	setAttr ".tgi[0].ni[5].y" -141.42857360839844;
	setAttr ".tgi[0].ni[5].nvs" 18304;
	setAttr ".tgi[0].ni[6].x" 35.714286804199219;
	setAttr ".tgi[0].ni[6].y" -474.28570556640625;
	setAttr ".tgi[0].ni[6].nvs" 18304;
	setAttr ".tgi[0].ni[7].x" -271.42855834960938;
	setAttr ".tgi[0].ni[7].y" -474.28570556640625;
	setAttr ".tgi[0].ni[7].nvs" 18304;
	setAttr ".tgi[0].ni[8].x" -271.42855834960938;
	setAttr ".tgi[0].ni[8].y" 162.85714721679688;
	setAttr ".tgi[0].ni[8].nvs" 18304;
	setAttr ".tgi[0].ni[9].x" -271.42855834960938;
	setAttr ".tgi[0].ni[9].y" -242.85714721679688;
	setAttr ".tgi[0].ni[9].nvs" 18304;
	setAttr ".tgi[0].ni[10].x" -271.42855834960938;
	setAttr ".tgi[0].ni[10].y" 264.28570556640625;
	setAttr ".tgi[0].ni[10].nvs" 18304;
	setAttr ".tgi[0].ni[11].x" -271.42855834960938;
	setAttr ".tgi[0].ni[11].y" -344.28570556640625;
	setAttr ".tgi[0].ni[11].nvs" 18304;
	setAttr ".tgi[0].ni[12].x" -271.42855834960938;
	setAttr ".tgi[0].ni[12].y" 61.428569793701172;
	setAttr ".tgi[0].ni[12].nvs" 18304;
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
connectAttr "Jnt.s" "Jnt1.is";
connectAttr "Jnt1.s" "Jnt2.is";
connectAttr "Jnt2.s" "Jnt3.is";
connectAttr "Jnt3.s" "Jnt4.is";
connectAttr "Jnt4.tx" "effector1.tx";
connectAttr "Jnt4.ty" "effector1.ty";
connectAttr "Jnt4.tz" "effector1.tz";
connectAttr "Jnt4.opm" "effector1.opm";
connectAttr ":time1.o" "nucleus1.cti";
connectAttr "hairSystemShape1.cust" "nucleus1.niao[0]";
connectAttr "hairSystemShape1.stst" "nucleus1.nias[0]";
connectAttr "baseCurveShape2.l" "follicleShape1.sp";
connectAttr "baseCurve2.wm" "follicleShape1.spm";
connectAttr "hairSystemShape1.oh[0]" "follicleShape1.crp";
connectAttr "Jnt.msg" "hairHandle1.hsj";
connectAttr "effector1.hp" "hairHandle1.hee";
connectAttr "ikSplineSolver.msg" "hairHandle1.hsv";
connectAttr "hairCurveShape2.ws" "hairHandle1.ic";
connectAttr "follicleShape1.ocr" "hairCurveShape2.cr";
connectAttr ":time1.o" "hairSystemShape1.cti";
connectAttr "nucleus1.noao[0]" "hairSystemShape1.nxst";
connectAttr "nucleus1.stf" "hairSystemShape1.stf";
connectAttr "follicleShape1.oha" "hairSystemShape1.ih[0]";
connectAttr "hairHandle1.hairStiffness" "hairSystemShape1.sfn";
connectAttr "hairHandle1.hairGravity" "hairSystemShape1.grv";
connectAttr "hairHandle1.hairDamping" "hairSystemShape1.dmp";
connectAttr "hairHandle1.hairFriction" "hairSystemShape1.frc";
connectAttr "hairHandle1.hairSolver" "hairSystemShape1.actv";
connectAttr "Hand_parentConstraint1.crx" "Hand.rx";
connectAttr "Hand_parentConstraint1.cry" "Hand.ry";
connectAttr "Hand_parentConstraint1.crz" "Hand.rz";
connectAttr "Hand_parentConstraint1.ctx" "Hand.tx";
connectAttr "Hand_parentConstraint1.cty" "Hand.ty";
connectAttr "Hand_parentConstraint1.ctz" "Hand.tz";
connectAttr "Hand.s" "Hand1.is";
connectAttr "Hand1_parentConstraint1.crx" "Hand1.rx";
connectAttr "Hand1_parentConstraint1.cry" "Hand1.ry";
connectAttr "Hand1_parentConstraint1.crz" "Hand1.rz";
connectAttr "Hand1_parentConstraint1.ctx" "Hand1.tx";
connectAttr "Hand1_parentConstraint1.cty" "Hand1.ty";
connectAttr "Hand1_parentConstraint1.ctz" "Hand1.tz";
connectAttr "Hand1.s" "Hand2.is";
connectAttr "Hand2_parentConstraint1.crx" "Hand2.rx";
connectAttr "Hand2_parentConstraint1.cry" "Hand2.ry";
connectAttr "Hand2_parentConstraint1.crz" "Hand2.rz";
connectAttr "Hand2_parentConstraint1.ctx" "Hand2.tx";
connectAttr "Hand2_parentConstraint1.cty" "Hand2.ty";
connectAttr "Hand2_parentConstraint1.ctz" "Hand2.tz";
connectAttr "Hand2.s" "Hand3.is";
connectAttr "Hand3_parentConstraint1.crx" "Hand3.rx";
connectAttr "Hand3_parentConstraint1.cry" "Hand3.ry";
connectAttr "Hand3_parentConstraint1.crz" "Hand3.rz";
connectAttr "Hand3_parentConstraint1.ctx" "Hand3.tx";
connectAttr "Hand3_parentConstraint1.cty" "Hand3.ty";
connectAttr "Hand3_parentConstraint1.ctz" "Hand3.tz";
connectAttr "Hand3.s" "Hand4.is";
connectAttr "Hand4_parentConstraint1.ctx" "Hand4.tx";
connectAttr "Hand4_parentConstraint1.cty" "Hand4.ty";
connectAttr "Hand4_parentConstraint1.ctz" "Hand4.tz";
connectAttr "Hand4_parentConstraint1.crx" "Hand4.rx";
connectAttr "Hand4_parentConstraint1.cry" "Hand4.ry";
connectAttr "Hand4_parentConstraint1.crz" "Hand4.rz";
connectAttr "Hand4.ro" "Hand4_parentConstraint1.cro";
connectAttr "Hand4.pim" "Hand4_parentConstraint1.cpim";
connectAttr "Hand4.rp" "Hand4_parentConstraint1.crp";
connectAttr "Hand4.rpt" "Hand4_parentConstraint1.crt";
connectAttr "Hand4.jo" "Hand4_parentConstraint1.cjo";
connectAttr "Hand4_Ctrl.t" "Hand4_parentConstraint1.tg[0].tt";
connectAttr "Hand4_Ctrl.rp" "Hand4_parentConstraint1.tg[0].trp";
connectAttr "Hand4_Ctrl.rpt" "Hand4_parentConstraint1.tg[0].trt";
connectAttr "Hand4_Ctrl.r" "Hand4_parentConstraint1.tg[0].tr";
connectAttr "Hand4_Ctrl.ro" "Hand4_parentConstraint1.tg[0].tro";
connectAttr "Hand4_Ctrl.s" "Hand4_parentConstraint1.tg[0].ts";
connectAttr "Hand4_Ctrl.pm" "Hand4_parentConstraint1.tg[0].tpm";
connectAttr "Hand4_parentConstraint1.w0" "Hand4_parentConstraint1.tg[0].tw";
connectAttr "Hand3.ro" "Hand3_parentConstraint1.cro";
connectAttr "Hand3.pim" "Hand3_parentConstraint1.cpim";
connectAttr "Hand3.rp" "Hand3_parentConstraint1.crp";
connectAttr "Hand3.rpt" "Hand3_parentConstraint1.crt";
connectAttr "Hand3.jo" "Hand3_parentConstraint1.cjo";
connectAttr "Hand3_Ctrl.t" "Hand3_parentConstraint1.tg[0].tt";
connectAttr "Hand3_Ctrl.rp" "Hand3_parentConstraint1.tg[0].trp";
connectAttr "Hand3_Ctrl.rpt" "Hand3_parentConstraint1.tg[0].trt";
connectAttr "Hand3_Ctrl.r" "Hand3_parentConstraint1.tg[0].tr";
connectAttr "Hand3_Ctrl.ro" "Hand3_parentConstraint1.tg[0].tro";
connectAttr "Hand3_Ctrl.s" "Hand3_parentConstraint1.tg[0].ts";
connectAttr "Hand3_Ctrl.pm" "Hand3_parentConstraint1.tg[0].tpm";
connectAttr "Hand3_parentConstraint1.w0" "Hand3_parentConstraint1.tg[0].tw";
connectAttr "Hand2.ro" "Hand2_parentConstraint1.cro";
connectAttr "Hand2.pim" "Hand2_parentConstraint1.cpim";
connectAttr "Hand2.rp" "Hand2_parentConstraint1.crp";
connectAttr "Hand2.rpt" "Hand2_parentConstraint1.crt";
connectAttr "Hand2.jo" "Hand2_parentConstraint1.cjo";
connectAttr "Hand2_Ctrl.t" "Hand2_parentConstraint1.tg[0].tt";
connectAttr "Hand2_Ctrl.rp" "Hand2_parentConstraint1.tg[0].trp";
connectAttr "Hand2_Ctrl.rpt" "Hand2_parentConstraint1.tg[0].trt";
connectAttr "Hand2_Ctrl.r" "Hand2_parentConstraint1.tg[0].tr";
connectAttr "Hand2_Ctrl.ro" "Hand2_parentConstraint1.tg[0].tro";
connectAttr "Hand2_Ctrl.s" "Hand2_parentConstraint1.tg[0].ts";
connectAttr "Hand2_Ctrl.pm" "Hand2_parentConstraint1.tg[0].tpm";
connectAttr "Hand2_parentConstraint1.w0" "Hand2_parentConstraint1.tg[0].tw";
connectAttr "Hand1.ro" "Hand1_parentConstraint1.cro";
connectAttr "Hand1.pim" "Hand1_parentConstraint1.cpim";
connectAttr "Hand1.rp" "Hand1_parentConstraint1.crp";
connectAttr "Hand1.rpt" "Hand1_parentConstraint1.crt";
connectAttr "Hand1.jo" "Hand1_parentConstraint1.cjo";
connectAttr "Hand1_Ctrl.t" "Hand1_parentConstraint1.tg[0].tt";
connectAttr "Hand1_Ctrl.rp" "Hand1_parentConstraint1.tg[0].trp";
connectAttr "Hand1_Ctrl.rpt" "Hand1_parentConstraint1.tg[0].trt";
connectAttr "Hand1_Ctrl.r" "Hand1_parentConstraint1.tg[0].tr";
connectAttr "Hand1_Ctrl.ro" "Hand1_parentConstraint1.tg[0].tro";
connectAttr "Hand1_Ctrl.s" "Hand1_parentConstraint1.tg[0].ts";
connectAttr "Hand1_Ctrl.pm" "Hand1_parentConstraint1.tg[0].tpm";
connectAttr "Hand1_parentConstraint1.w0" "Hand1_parentConstraint1.tg[0].tw";
connectAttr "Hand.ro" "Hand_parentConstraint1.cro";
connectAttr "Hand.pim" "Hand_parentConstraint1.cpim";
connectAttr "Hand.rp" "Hand_parentConstraint1.crp";
connectAttr "Hand.rpt" "Hand_parentConstraint1.crt";
connectAttr "Hand.jo" "Hand_parentConstraint1.cjo";
connectAttr "Hand_Ctrl.t" "Hand_parentConstraint1.tg[0].tt";
connectAttr "Hand_Ctrl.rp" "Hand_parentConstraint1.tg[0].trp";
connectAttr "Hand_Ctrl.rpt" "Hand_parentConstraint1.tg[0].trt";
connectAttr "Hand_Ctrl.r" "Hand_parentConstraint1.tg[0].tr";
connectAttr "Hand_Ctrl.ro" "Hand_parentConstraint1.tg[0].tro";
connectAttr "Hand_Ctrl.s" "Hand_parentConstraint1.tg[0].ts";
connectAttr "Hand_Ctrl.pm" "Hand_parentConstraint1.tg[0].tpm";
connectAttr "Hand_parentConstraint1.w0" "Hand_parentConstraint1.tg[0].tw";
connectAttr "Hand_grp_parentConstraint1.ctx" "Hand_grp.tx";
connectAttr "Hand_grp_parentConstraint1.cty" "Hand_grp.ty";
connectAttr "Hand_grp_parentConstraint1.ctz" "Hand_grp.tz";
connectAttr "Hand_grp_parentConstraint1.crx" "Hand_grp.rx";
connectAttr "Hand_grp_parentConstraint1.cry" "Hand_grp.ry";
connectAttr "Hand_grp_parentConstraint1.crz" "Hand_grp.rz";
connectAttr "makeNurbCircle1.oc" "Hand_CtrlShape.cr";
connectAttr "Jnt1.t" "Hand1_grp.t";
connectAttr "Jnt1.r" "Hand1_grp.r";
connectAttr "makeNurbCircle2.oc" "Hand1_CtrlShape.cr";
connectAttr "Jnt2.t" "Hand2_grp.t";
connectAttr "Jnt2.r" "Hand2_grp.r";
connectAttr "makeNurbCircle3.oc" "Hand2_CtrlShape.cr";
connectAttr "Jnt3.t" "Hand3_grp.t";
connectAttr "Jnt3.r" "Hand3_grp.r";
connectAttr "makeNurbCircle4.oc" "Hand3_CtrlShape.cr";
connectAttr "Jnt4.t" "Hand4_grp.t";
connectAttr "Jnt4.r" "Hand4_grp.r";
connectAttr "makeNurbCircle5.oc" "Hand4_CtrlShape.cr";
connectAttr "Hand_grp.ro" "Hand_grp_parentConstraint1.cro";
connectAttr "Hand_grp.pim" "Hand_grp_parentConstraint1.cpim";
connectAttr "Hand_grp.rp" "Hand_grp_parentConstraint1.crp";
connectAttr "Hand_grp.rpt" "Hand_grp_parentConstraint1.crt";
connectAttr "Jnt.t" "Hand_grp_parentConstraint1.tg[0].tt";
connectAttr "Jnt.rp" "Hand_grp_parentConstraint1.tg[0].trp";
connectAttr "Jnt.rpt" "Hand_grp_parentConstraint1.tg[0].trt";
connectAttr "Jnt.r" "Hand_grp_parentConstraint1.tg[0].tr";
connectAttr "Jnt.ro" "Hand_grp_parentConstraint1.tg[0].tro";
connectAttr "Jnt.s" "Hand_grp_parentConstraint1.tg[0].ts";
connectAttr "Jnt.pm" "Hand_grp_parentConstraint1.tg[0].tpm";
connectAttr "Jnt.jo" "Hand_grp_parentConstraint1.tg[0].tjo";
connectAttr "Jnt.ssc" "Hand_grp_parentConstraint1.tg[0].tsc";
connectAttr "Jnt.is" "Hand_grp_parentConstraint1.tg[0].tis";
connectAttr "Hand_grp_parentConstraint1.w0" "Hand_grp_parentConstraint1.tg[0].tw"
		;
connectAttr "skinCluster1GroupId.id" "pCylinderShape1.iog.og[0].gid";
connectAttr "skinCluster1Set.mwc" "pCylinderShape1.iog.og[0].gco";
connectAttr "groupId2.id" "pCylinderShape1.iog.og[1].gid";
connectAttr "tweakSet1.mwc" "pCylinderShape1.iog.og[1].gco";
connectAttr "skinCluster1.og[0]" "pCylinderShape1.i";
connectAttr "tweak1.vl[0].vt[0]" "pCylinderShape1.twl";
connectAttr "pCylinder2_scaleX.o" "pCylinder2.sx";
connectAttr "pCylinder2_scaleY.o" "pCylinder2.sy";
connectAttr "pCylinder2_scaleZ.o" "pCylinder2.sz";
connectAttr "pCylinder2_visibility.o" "pCylinder2.v";
connectAttr "pCylinder2_translateX.o" "pCylinder2.tx";
connectAttr "pCylinder2_translateY.o" "pCylinder2.ty";
connectAttr "pCylinder2_translateZ.o" "pCylinder2.tz";
connectAttr "pCylinder2_rotateX.o" "pCylinder2.rx";
connectAttr "pCylinder2_rotateY.o" "pCylinder2.ry";
connectAttr "pCylinder2_rotateZ.o" "pCylinder2.rz";
relationship "link" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
connectAttr "layerManager.dli[0]" "defaultLayer.id";
connectAttr "renderLayerManager.rlmi[0]" "defaultRenderLayer.rlid";
connectAttr "skinCluster1GroupParts.og" "skinCluster1.ip[0].ig";
connectAttr "skinCluster1GroupId.id" "skinCluster1.ip[0].gi";
connectAttr "bindPose1.msg" "skinCluster1.bp";
connectAttr "Hand.wm" "skinCluster1.ma[0]";
connectAttr "Hand1.wm" "skinCluster1.ma[1]";
connectAttr "Hand2.wm" "skinCluster1.ma[2]";
connectAttr "Hand3.wm" "skinCluster1.ma[3]";
connectAttr "Hand4.wm" "skinCluster1.ma[4]";
connectAttr "Hand.liw" "skinCluster1.lw[0]";
connectAttr "Hand1.liw" "skinCluster1.lw[1]";
connectAttr "Hand2.liw" "skinCluster1.lw[2]";
connectAttr "Hand3.liw" "skinCluster1.lw[3]";
connectAttr "Hand4.liw" "skinCluster1.lw[4]";
connectAttr "Hand.obcc" "skinCluster1.ifcl[0]";
connectAttr "Hand1.obcc" "skinCluster1.ifcl[1]";
connectAttr "Hand2.obcc" "skinCluster1.ifcl[2]";
connectAttr "Hand3.obcc" "skinCluster1.ifcl[3]";
connectAttr "Hand4.obcc" "skinCluster1.ifcl[4]";
connectAttr "groupParts2.og" "tweak1.ip[0].ig";
connectAttr "groupId2.id" "tweak1.ip[0].gi";
connectAttr "skinCluster1GroupId.msg" "skinCluster1Set.gn" -na;
connectAttr "pCylinderShape1.iog.og[0]" "skinCluster1Set.dsm" -na;
connectAttr "skinCluster1.msg" "skinCluster1Set.ub[0]";
connectAttr "tweak1.og[0]" "skinCluster1GroupParts.ig";
connectAttr "skinCluster1GroupId.id" "skinCluster1GroupParts.gi";
connectAttr "groupId2.msg" "tweakSet1.gn" -na;
connectAttr "pCylinderShape1.iog.og[1]" "tweakSet1.dsm" -na;
connectAttr "tweak1.msg" "tweakSet1.ub[0]";
connectAttr "pCylinderShape1Orig.w" "groupParts2.ig";
connectAttr "groupId2.id" "groupParts2.gi";
connectAttr "Hand.msg" "bindPose1.m[0]";
connectAttr "Hand1.msg" "bindPose1.m[1]";
connectAttr "Hand2.msg" "bindPose1.m[2]";
connectAttr "Hand3.msg" "bindPose1.m[3]";
connectAttr "Hand4.msg" "bindPose1.m[4]";
connectAttr "bindPose1.w" "bindPose1.p[0]";
connectAttr "bindPose1.m[0]" "bindPose1.p[1]";
connectAttr "bindPose1.m[1]" "bindPose1.p[2]";
connectAttr "bindPose1.m[2]" "bindPose1.p[3]";
connectAttr "bindPose1.m[3]" "bindPose1.p[4]";
connectAttr "Hand.bps" "bindPose1.wm[0]";
connectAttr "Hand1.bps" "bindPose1.wm[1]";
connectAttr "Hand2.bps" "bindPose1.wm[2]";
connectAttr "Hand3.bps" "bindPose1.wm[3]";
connectAttr "Hand4.bps" "bindPose1.wm[4]";
connectAttr "aTools_StoreNode.o" "scene.m";
connectAttr "pCylinder2_translateX.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[0].dn"
		;
connectAttr "pCylinder2_scaleX.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[1].dn"
		;
connectAttr "pCylinder2_scaleY.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[2].dn"
		;
connectAttr "pCylinder2.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[3].dn";
connectAttr "pCylinder2_translateZ.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[4].dn"
		;
connectAttr "pCylinder2_rotateZ.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[5].dn"
		;
connectAttr ":initialShadingGroup.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[6].dn"
		;
connectAttr "pCylinderShape2.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[7].dn";
connectAttr "pCylinder2_translateY.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[8].dn"
		;
connectAttr "pCylinder2_scaleZ.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[9].dn"
		;
connectAttr "pCylinder2_rotateY.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[10].dn"
		;
connectAttr "pCylinder2_visibility.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[11].dn"
		;
connectAttr "pCylinder2_rotateX.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[12].dn"
		;
connectAttr "defaultRenderLayer.msg" ":defaultRenderingList1.r" -na;
connectAttr "pCylinderShape1.iog" ":initialShadingGroup.dsm" -na;
connectAttr "pCylinderShape2.iog" ":initialShadingGroup.dsm" -na;
connectAttr "ikSplineSolver.msg" ":ikSystem.sol" -na;
// End of tail.ma
