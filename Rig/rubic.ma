//Maya ASCII 2020 scene
//Name: rubic.ma
//Last modified: Sat, May 24, 2025 04:53:18 PM
//Codeset: 1252
requires maya "2020";
requires "mtoa" "4.1.1";
currentUnit -l centimeter -a degree -t film;
fileInfo "application" "maya";
fileInfo "product" "Maya 2020";
fileInfo "version" "2020";
fileInfo "cutIdentifier" "202011110415-b1e20b88e2";
fileInfo "osv" "Microsoft Windows 10 Technical Preview  (Build 19045)\n";
fileInfo "UUID" "385C2A08-4865-88A3-E17D-FEB9E08D9DE0";
createNode transform -s -n "persp";
	rename -uid "3A145ABF-4793-C3AD-80DF-6695F85BC1D8";
	setAttr ".v" no;
	setAttr ".t" -type "double3" -8.6224654406802266 16.334389207579509 3.9755806861889722 ;
	setAttr ".r" -type "double3" -56.138352729599852 -432.19999999984128 1.0404329506532442e-14 ;
createNode camera -s -n "perspShape" -p "persp";
	rename -uid "77F49B76-46F8-696A-023E-1C9A831678C0";
	setAttr -k off ".v" no;
	setAttr ".fl" 34.999999999999993;
	setAttr ".coi" 18.815359678830998;
	setAttr ".imn" -type "string" "persp";
	setAttr ".den" -type "string" "persp_depth";
	setAttr ".man" -type "string" "persp_mask";
	setAttr ".hc" -type "string" "viewSet -p %camera";
	setAttr ".ai_translator" -type "string" "perspective";
createNode transform -s -n "top";
	rename -uid "A5A32C35-4552-479D-38F1-2DAE5FFBA438";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 1000.1 0 ;
	setAttr ".r" -type "double3" -90 0 0 ;
createNode camera -s -n "topShape" -p "top";
	rename -uid "977C3D31-45B4-3C7A-AF93-EA9BF188A250";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 1000.1;
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "top";
	setAttr ".den" -type "string" "top_depth";
	setAttr ".man" -type "string" "top_mask";
	setAttr ".hc" -type "string" "viewSet -t %camera";
	setAttr ".o" yes;
	setAttr ".ai_translator" -type "string" "orthographic";
createNode transform -s -n "front";
	rename -uid "E7F1C208-4CC8-573F-3581-34A589E4CC35";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 0 1000.1 ;
createNode camera -s -n "frontShape" -p "front";
	rename -uid "EF6D4F2D-4E2B-F41B-9BF3-01A5888A56A1";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 1000.1;
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "front";
	setAttr ".den" -type "string" "front_depth";
	setAttr ".man" -type "string" "front_mask";
	setAttr ".hc" -type "string" "viewSet -f %camera";
	setAttr ".o" yes;
	setAttr ".ai_translator" -type "string" "orthographic";
createNode transform -s -n "side";
	rename -uid "A958C63C-46D8-31C6-1AA5-AAADF6BC954D";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 1000.1 0 0 ;
	setAttr ".r" -type "double3" 0 90 0 ;
createNode camera -s -n "sideShape" -p "side";
	rename -uid "7BEE4264-487D-6C8D-C00B-44A2DD554EDE";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 1000.1;
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "side";
	setAttr ".den" -type "string" "side_depth";
	setAttr ".man" -type "string" "side_mask";
	setAttr ".hc" -type "string" "viewSet -s %camera";
	setAttr ".o" yes;
	setAttr ".ai_translator" -type "string" "orthographic";
createNode transform -n "old";
	rename -uid "C246B799-4F9C-79C5-C62D-B7BE1193D942";
	setAttr ".v" no;
createNode transform -n "l" -p "old";
	rename -uid "826228D2-48C8-7908-AFF3-7A95B0558F96";
createNode locator -n "lShape" -p "l";
	rename -uid "97543D58-43EA-7B91-48A1-A998FE070700";
	setAttr -k off ".v";
createNode transform -n "gg" -p "old";
	rename -uid "A09AFE45-4E9D-C88F-04E1-AC9A21D0C3D1";
createNode transform -n "d" -p "gg";
	rename -uid "B4D5F8F2-420E-5BC3-2623-778B4EF21D4E";
	setAttr ".t" -type "double3" -6.1673667906751959 -3.5527136788005009e-15 -9.2296065696424421 ;
createNode mesh -n "dShape" -p "d";
	rename -uid "2CF4AD07-4303-B39C-656D-648AA137800F";
	setAttr -k off ".v";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 14 ".uvst[0].uvsp[0:13]" -type "float2" 0.375 0 0.625 0 0.375
		 0.25 0.625 0.25 0.375 0.5 0.625 0.5 0.375 0.75 0.625 0.75 0.375 1 0.625 1 0.875 0
		 0.875 0.25 0.125 0 0.125 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 8 ".vt[0:7]"  -0.5 -0.5 0.5 0.5 -0.5 0.5 -0.5 0.5 0.5 0.5 0.5 0.5
		 -0.5 0.5 -0.5 0.5 0.5 -0.5 -0.5 -0.5 -0.5 0.5 -0.5 -0.5;
	setAttr -s 12 ".ed[0:11]"  0 1 0 2 3 0 4 5 0 6 7 0 0 2 0 1 3 0 2 4 0
		 3 5 0 4 6 0 5 7 0 6 0 0 7 1 0;
	setAttr -s 6 -ch 24 ".fc[0:5]" -type "polyFaces" 
		f 4 0 5 -2 -5
		mu 0 4 0 1 3 2
		f 4 1 7 -3 -7
		mu 0 4 2 3 5 4
		f 4 2 9 -4 -9
		mu 0 4 4 5 7 6
		f 4 3 11 -1 -11
		mu 0 4 6 7 9 8
		f 4 -12 -10 -8 -6
		mu 0 4 1 10 11 3
		f 4 10 4 6 8
		mu 0 4 12 0 2 13;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ai_translator" -type "string" "polymesh";
createNode transform -n "t" -p "old";
	rename -uid "DD7BF931-4F8A-AA6B-19AF-57B045EDF762";
	setAttr ".t" -type "double3" 0.98263734717231799 -7.1054273576010019e-15 16.822399247342943 ;
createNode transform -n "tc" -p "t";
	rename -uid "C7D2A410-49EF-0049-8759-0EAD5AD9A076";
	setAttr ".t" -type "double3" 1.281237202716401 -1.4210854715202004e-14 -26.847320453538838 ;
createNode nurbsCurve -n "tcShape" -p "tc";
	rename -uid "E3C216A9-4A29-5141-5D89-409E69B300D2";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 14;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		1.5612123041540806 9.5596682553587958e-17 -1.5612123041540809
		1.3519412498515946e-16 1.3519412498515946e-16 -2.2078876142784498
		-1.5612123041540806 9.5596682553587934e-17 -1.5612123041540804
		-2.2078876142784507 7.0084873127241219e-33 -1.1445728380793065e-16
		-1.5612123041540806 -9.5596682553587946e-17 1.5612123041540806
		-2.2116561236575422e-16 -1.3519412498515956e-16 2.2078876142784511
		1.5612123041540806 -9.5596682553587934e-17 1.5612123041540804
		2.2078876142784507 -1.8436375090178285e-32 3.0108885440299045e-16
		1.5612123041540806 9.5596682553587958e-17 -1.5612123041540809
		1.3519412498515946e-16 1.3519412498515946e-16 -2.2078876142784498
		-1.5612123041540806 9.5596682553587934e-17 -1.5612123041540804
		;
createNode transform -n "tc1" -p "tc";
	rename -uid "88F7AC0C-4B12-80FE-10BA-58AE3DA69A62";
createNode nurbsCurve -n "tcShape1" -p "tc1";
	rename -uid "D0C9A8F5-4233-0F03-87DF-6E98EAA6979B";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 21;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		0.87234734199057151 5.3415869005672758e-17 -0.87234734199057196
		7.5541446393767042e-17 7.5541446393767042e-17 -1.2336854421431867
		-0.87234734199057151 5.3415869005672758e-17 -0.87234734199057151
		-1.2336854421431873 -5.0718633278977781e-32 6.3905376601145636e-16
		-0.87234734199057151 -5.3415869005672758e-17 0.87234734199057151
		-1.2357911449559118e-16 -7.5541446393767079e-17 1.2336854421431873
		0.87234734199057151 -5.3415869005672758e-17 0.87234734199057151
		1.2336854421431873 -6.4936275572358714e-32 8.71245485342774e-16
		0.87234734199057151 5.3415869005672758e-17 -0.87234734199057196
		7.5541446393767042e-17 7.5541446393767042e-17 -1.2336854421431867
		-0.87234734199057151 5.3415869005672758e-17 -0.87234734199057151
		;
createNode transform -n "geo";
	rename -uid "8F81E4EC-4F9B-65C4-0282-18B294CF038E";
createNode transform -n "rbg1" -p "geo";
	rename -uid "6D3CC153-4861-E7DD-F2E1-108C5226AD5A";
createNode mesh -n "rbgShape1" -p "rbg1";
	rename -uid "670CB044-4F57-0EF5-43D5-26858B9515A1";
	setAttr -k off ".v";
	setAttr -s 2 ".iog[0].og";
	setAttr ".iog[0].og[0].gcl" -type "componentList" 2 "f[0:2]" "f[4:5]";
	setAttr ".iog[0].og[1].gcl" -type "componentList" 1 "f[3]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 14 ".uvst[0].uvsp[0:13]" -type "float2" 0.375 0 0.625 0 0.375
		 0.25 0.625 0.25 0.375 0.5 0.625 0.5 0.375 0.75 0.625 0.75 0.375 1 0.625 1 0.875 0
		 0.875 0.25 0.125 0 0.125 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 8 ".vt[0:7]"  -0.5 -0.5 0.5 0.5 -0.5 0.5 -0.5 0.5 0.5 0.5 0.5 0.5
		 -0.5 0.5 -0.5 0.5 0.5 -0.5 -0.5 -0.5 -0.5 0.5 -0.5 -0.5;
	setAttr -s 12 ".ed[0:11]"  0 1 0 2 3 0 4 5 0 6 7 0 0 2 0 1 3 0 2 4 0
		 3 5 0 4 6 0 5 7 0 6 0 0 7 1 0;
	setAttr -s 6 -ch 24 ".fc[0:5]" -type "polyFaces" 
		f 4 0 5 -2 -5
		mu 0 4 0 1 3 2
		f 4 1 7 -3 -7
		mu 0 4 2 3 5 4
		f 4 2 9 -4 -9
		mu 0 4 4 5 7 6
		f 4 3 11 -1 -11
		mu 0 4 6 7 9 8
		f 4 -12 -10 -8 -6
		mu 0 4 1 10 11 3
		f 4 10 4 6 8
		mu 0 4 12 0 2 13;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ai_translator" -type "string" "polymesh";
createNode transform -n "rbg2" -p "geo";
	rename -uid "56DE6F61-4C15-ACEF-81FE-1A99740EF0E9";
	setAttr ".rp" -type "double3" 1.1000000238418579 0 0 ;
	setAttr ".sp" -type "double3" 1.1000000238418579 0 0 ;
createNode mesh -n "rbgShape2" -p "rbg2";
	rename -uid "A08249B9-4B2E-5EB4-915B-8B94FEE2967F";
	setAttr -k off ".v";
	setAttr -s 3 ".iog[0].og";
	setAttr ".iog[0].og[0].gcl" -type "componentList" 2 "f[0:2]" "f[5]";
	setAttr ".iog[0].og[1].gcl" -type "componentList" 1 "f[4]";
	setAttr ".iog[0].og[2].gcl" -type "componentList" 1 "f[3]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 14 ".uvst[0].uvsp[0:13]" -type "float2" 0.375 0 0.625 0 0.375
		 0.25 0.625 0.25 0.375 0.5 0.625 0.5 0.375 0.75 0.625 0.75 0.375 1 0.625 1 0.875 0
		 0.875 0.25 0.125 0 0.125 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 8 ".pt[0:7]" -type "float3"  1.1 0 0 1.1 0 0 1.1 0 0 1.1 
		0 0 1.1 0 0 1.1 0 0 1.1 0 0 1.1 0 0;
	setAttr -s 8 ".vt[0:7]"  -0.5 -0.5 0.5 0.5 -0.5 0.5 -0.5 0.5 0.5 0.5 0.5 0.5
		 -0.5 0.5 -0.5 0.5 0.5 -0.5 -0.5 -0.5 -0.5 0.5 -0.5 -0.5;
	setAttr -s 12 ".ed[0:11]"  0 1 0 2 3 0 4 5 0 6 7 0 0 2 0 1 3 0 2 4 0
		 3 5 0 4 6 0 5 7 0 6 0 0 7 1 0;
	setAttr -s 6 -ch 24 ".fc[0:5]" -type "polyFaces" 
		f 4 0 5 -2 -5
		mu 0 4 0 1 3 2
		f 4 1 7 -3 -7
		mu 0 4 2 3 5 4
		f 4 2 9 -4 -9
		mu 0 4 4 5 7 6
		f 4 3 11 -1 -11
		mu 0 4 6 7 9 8
		f 4 -12 -10 -8 -6
		mu 0 4 1 10 11 3
		f 4 10 4 6 8
		mu 0 4 12 0 2 13;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ai_translator" -type "string" "polymesh";
createNode transform -n "rbg3" -p "geo";
	rename -uid "7492A599-43DB-6D55-B84C-EDA3FF89253C";
	setAttr ".rp" -type "double3" -1.1000000238418579 0 0 ;
	setAttr ".sp" -type "double3" -1.1000000238418579 0 0 ;
createNode mesh -n "rbgShape3" -p "rbg3";
	rename -uid "D49F400E-42D6-4AFC-E57B-8990877FA64B";
	setAttr -k off ".v";
	setAttr -s 3 ".iog[0].og";
	setAttr ".iog[0].og[0].gcl" -type "componentList" 2 "f[0:2]" "f[4]";
	setAttr ".iog[0].og[1].gcl" -type "componentList" 1 "f[5]";
	setAttr ".iog[0].og[2].gcl" -type "componentList" 1 "f[3]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 14 ".uvst[0].uvsp[0:13]" -type "float2" 0.375 0 0.625 0 0.375
		 0.25 0.625 0.25 0.375 0.5 0.625 0.5 0.375 0.75 0.625 0.75 0.375 1 0.625 1 0.875 0
		 0.875 0.25 0.125 0 0.125 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 8 ".pt[0:7]" -type "float3"  -1.1 0 0 -1.1 0 0 -1.1 0 
		0 -1.1 0 0 -1.1 0 0 -1.1 0 0 -1.1 0 0 -1.1 0 0;
	setAttr -s 8 ".vt[0:7]"  -0.5 -0.5 0.5 0.5 -0.5 0.5 -0.5 0.5 0.5 0.5 0.5 0.5
		 -0.5 0.5 -0.5 0.5 0.5 -0.5 -0.5 -0.5 -0.5 0.5 -0.5 -0.5;
	setAttr -s 12 ".ed[0:11]"  0 1 0 2 3 0 4 5 0 6 7 0 0 2 0 1 3 0 2 4 0
		 3 5 0 4 6 0 5 7 0 6 0 0 7 1 0;
	setAttr -s 6 -ch 24 ".fc[0:5]" -type "polyFaces" 
		f 4 0 5 -2 -5
		mu 0 4 0 1 3 2
		f 4 1 7 -3 -7
		mu 0 4 2 3 5 4
		f 4 2 9 -4 -9
		mu 0 4 4 5 7 6
		f 4 3 11 -1 -11
		mu 0 4 6 7 9 8
		f 4 -12 -10 -8 -6
		mu 0 4 1 10 11 3
		f 4 10 4 6 8
		mu 0 4 12 0 2 13;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ai_translator" -type "string" "polymesh";
createNode transform -n "rbg4" -p "geo";
	rename -uid "9CBDFA4C-468A-31BF-3C31-FD88410DACC1";
	setAttr ".rp" -type "double3" -1.1000000238418579 0 1.1000000238418579 ;
	setAttr ".sp" -type "double3" -1.1000000238418579 0 1.1000000238418579 ;
createNode mesh -n "rbgShape4" -p "rbg4";
	rename -uid "F6B5884C-4AC6-3A5E-18BB-B2897ECE8DEB";
	setAttr -k off ".v";
	setAttr -s 4 ".iog[0].og";
	setAttr ".iog[0].og[0].gcl" -type "componentList" 2 "f[1:2]" "f[4]";
	setAttr ".iog[0].og[1].gcl" -type "componentList" 1 "f[0]";
	setAttr ".iog[0].og[2].gcl" -type "componentList" 1 "f[5]";
	setAttr ".iog[0].og[3].gcl" -type "componentList" 1 "f[3]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 14 ".uvst[0].uvsp[0:13]" -type "float2" 0.375 0 0.625 0 0.375
		 0.25 0.625 0.25 0.375 0.5 0.625 0.5 0.375 0.75 0.625 0.75 0.375 1 0.625 1 0.875 0
		 0.875 0.25 0.125 0 0.125 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 8 ".pt[0:7]" -type "float3"  -1.1 0 1.1 -1.1 0 1.1 -1.1 
		0 1.1 -1.1 0 1.1 -1.1 0 1.1 -1.1 0 1.1 -1.1 0 1.1 -1.1 0 1.1;
	setAttr -s 8 ".vt[0:7]"  -0.5 -0.5 0.5 0.5 -0.5 0.5 -0.5 0.5 0.5 0.5 0.5 0.5
		 -0.5 0.5 -0.5 0.5 0.5 -0.5 -0.5 -0.5 -0.5 0.5 -0.5 -0.5;
	setAttr -s 12 ".ed[0:11]"  0 1 0 2 3 0 4 5 0 6 7 0 0 2 0 1 3 0 2 4 0
		 3 5 0 4 6 0 5 7 0 6 0 0 7 1 0;
	setAttr -s 6 -ch 24 ".fc[0:5]" -type "polyFaces" 
		f 4 0 5 -2 -5
		mu 0 4 0 1 3 2
		f 4 1 7 -3 -7
		mu 0 4 2 3 5 4
		f 4 2 9 -4 -9
		mu 0 4 4 5 7 6
		f 4 3 11 -1 -11
		mu 0 4 6 7 9 8
		f 4 -12 -10 -8 -6
		mu 0 4 1 10 11 3
		f 4 10 4 6 8
		mu 0 4 12 0 2 13;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ai_translator" -type "string" "polymesh";
createNode transform -n "rbg5" -p "geo";
	rename -uid "E8170F93-4003-604A-1C05-80987819182F";
	setAttr ".rp" -type "double3" 0 0 1.1000000238418579 ;
	setAttr ".sp" -type "double3" 0 0 1.1000000238418579 ;
createNode mesh -n "rbgShape5" -p "rbg5";
	rename -uid "1DCB0AF1-42EC-6DC0-2E9E-139CECA823C1";
	setAttr -k off ".v";
	setAttr -s 3 ".iog[0].og";
	setAttr ".iog[0].og[0].gcl" -type "componentList" 2 "f[1:2]" "f[4:5]";
	setAttr ".iog[0].og[1].gcl" -type "componentList" 1 "f[0]";
	setAttr ".iog[0].og[2].gcl" -type "componentList" 1 "f[3]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 14 ".uvst[0].uvsp[0:13]" -type "float2" 0.375 0 0.625 0 0.375
		 0.25 0.625 0.25 0.375 0.5 0.625 0.5 0.375 0.75 0.625 0.75 0.375 1 0.625 1 0.875 0
		 0.875 0.25 0.125 0 0.125 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 8 ".pt[0:7]" -type "float3"  0 0 1.1 0 0 1.1 0 0 1.1 0 
		0 1.1 0 0 1.1 0 0 1.1 0 0 1.1 0 0 1.1;
	setAttr -s 8 ".vt[0:7]"  -0.5 -0.5 0.5 0.5 -0.5 0.5 -0.5 0.5 0.5 0.5 0.5 0.5
		 -0.5 0.5 -0.5 0.5 0.5 -0.5 -0.5 -0.5 -0.5 0.5 -0.5 -0.5;
	setAttr -s 12 ".ed[0:11]"  0 1 0 2 3 0 4 5 0 6 7 0 0 2 0 1 3 0 2 4 0
		 3 5 0 4 6 0 5 7 0 6 0 0 7 1 0;
	setAttr -s 6 -ch 24 ".fc[0:5]" -type "polyFaces" 
		f 4 0 5 -2 -5
		mu 0 4 0 1 3 2
		f 4 1 7 -3 -7
		mu 0 4 2 3 5 4
		f 4 2 9 -4 -9
		mu 0 4 4 5 7 6
		f 4 3 11 -1 -11
		mu 0 4 6 7 9 8
		f 4 -12 -10 -8 -6
		mu 0 4 1 10 11 3
		f 4 10 4 6 8
		mu 0 4 12 0 2 13;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ai_translator" -type "string" "polymesh";
createNode transform -n "rbg6" -p "geo";
	rename -uid "DBABDDE4-4D8A-712F-ECF7-F9A579B3343E";
	setAttr ".rp" -type "double3" 1.1000000238418579 0 1.1000000238418579 ;
	setAttr ".sp" -type "double3" 1.1000000238418579 0 1.1000000238418579 ;
createNode mesh -n "rbgShape6" -p "rbg6";
	rename -uid "BC3A1B6F-4791-AD1C-451C-F6A06738C46C";
	setAttr -k off ".v";
	setAttr -s 4 ".iog[0].og";
	setAttr ".iog[0].og[0].gcl" -type "componentList" 2 "f[1:2]" "f[5]";
	setAttr ".iog[0].og[1].gcl" -type "componentList" 1 "f[0]";
	setAttr ".iog[0].og[2].gcl" -type "componentList" 1 "f[4]";
	setAttr ".iog[0].og[3].gcl" -type "componentList" 1 "f[3]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 14 ".uvst[0].uvsp[0:13]" -type "float2" 0.375 0 0.625 0 0.375
		 0.25 0.625 0.25 0.375 0.5 0.625 0.5 0.375 0.75 0.625 0.75 0.375 1 0.625 1 0.875 0
		 0.875 0.25 0.125 0 0.125 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 8 ".pt[0:7]" -type "float3"  1.1 0 1.1 1.1 0 1.1 1.1 0 
		1.1 1.1 0 1.1 1.1 0 1.1 1.1 0 1.1 1.1 0 1.1 1.1 0 1.1;
	setAttr -s 8 ".vt[0:7]"  -0.5 -0.5 0.5 0.5 -0.5 0.5 -0.5 0.5 0.5 0.5 0.5 0.5
		 -0.5 0.5 -0.5 0.5 0.5 -0.5 -0.5 -0.5 -0.5 0.5 -0.5 -0.5;
	setAttr -s 12 ".ed[0:11]"  0 1 0 2 3 0 4 5 0 6 7 0 0 2 0 1 3 0 2 4 0
		 3 5 0 4 6 0 5 7 0 6 0 0 7 1 0;
	setAttr -s 6 -ch 24 ".fc[0:5]" -type "polyFaces" 
		f 4 0 5 -2 -5
		mu 0 4 0 1 3 2
		f 4 1 7 -3 -7
		mu 0 4 2 3 5 4
		f 4 2 9 -4 -9
		mu 0 4 4 5 7 6
		f 4 3 11 -1 -11
		mu 0 4 6 7 9 8
		f 4 -12 -10 -8 -6
		mu 0 4 1 10 11 3
		f 4 10 4 6 8
		mu 0 4 12 0 2 13;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ai_translator" -type "string" "polymesh";
createNode transform -n "rbg7" -p "geo";
	rename -uid "6C70CE66-441E-D789-9143-B98401CB4992";
	setAttr ".rp" -type "double3" -1.1000000238418579 0 -1.1000000238418579 ;
	setAttr ".sp" -type "double3" -1.1000000238418579 0 -1.1000000238418579 ;
createNode mesh -n "rbgShape7" -p "rbg7";
	rename -uid "72C4A39D-440D-D54F-720E-869AB194C24E";
	setAttr -k off ".v";
	setAttr -s 4 ".iog[0].og";
	setAttr ".iog[0].og[0].gcl" -type "componentList" 2 "f[0:1]" "f[4]";
	setAttr ".iog[0].og[1].gcl" -type "componentList" 1 "f[2]";
	setAttr ".iog[0].og[2].gcl" -type "componentList" 1 "f[5]";
	setAttr ".iog[0].og[3].gcl" -type "componentList" 1 "f[3]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 14 ".uvst[0].uvsp[0:13]" -type "float2" 0.375 0 0.625 0 0.375
		 0.25 0.625 0.25 0.375 0.5 0.625 0.5 0.375 0.75 0.625 0.75 0.375 1 0.625 1 0.875 0
		 0.875 0.25 0.125 0 0.125 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 8 ".pt[0:7]" -type "float3"  -1.1 0 -1.1 -1.1 0 -1.1 -1.1 
		0 -1.1 -1.1 0 -1.1 -1.1 0 -1.1 -1.1 0 -1.1 -1.1 0 -1.1 -1.1 0 -1.1;
	setAttr -s 8 ".vt[0:7]"  -0.5 -0.5 0.5 0.5 -0.5 0.5 -0.5 0.5 0.5 0.5 0.5 0.5
		 -0.5 0.5 -0.5 0.5 0.5 -0.5 -0.5 -0.5 -0.5 0.5 -0.5 -0.5;
	setAttr -s 12 ".ed[0:11]"  0 1 0 2 3 0 4 5 0 6 7 0 0 2 0 1 3 0 2 4 0
		 3 5 0 4 6 0 5 7 0 6 0 0 7 1 0;
	setAttr -s 6 -ch 24 ".fc[0:5]" -type "polyFaces" 
		f 4 0 5 -2 -5
		mu 0 4 0 1 3 2
		f 4 1 7 -3 -7
		mu 0 4 2 3 5 4
		f 4 2 9 -4 -9
		mu 0 4 4 5 7 6
		f 4 3 11 -1 -11
		mu 0 4 6 7 9 8
		f 4 -12 -10 -8 -6
		mu 0 4 1 10 11 3
		f 4 10 4 6 8
		mu 0 4 12 0 2 13;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ai_translator" -type "string" "polymesh";
createNode transform -n "rbg8" -p "geo";
	rename -uid "98CCDBE9-4B1B-7FEB-6946-DAB8B1C6C2FB";
	setAttr ".rp" -type "double3" 0 0 -1.1000000238418579 ;
	setAttr ".sp" -type "double3" 0 0 -1.1000000238418579 ;
createNode mesh -n "rbgShape8" -p "rbg8";
	rename -uid "0D2473F7-48D4-D384-7D90-1E8AA5C1FB6F";
	setAttr -k off ".v";
	setAttr -s 3 ".iog[0].og";
	setAttr ".iog[0].og[0].gcl" -type "componentList" 2 "f[0:1]" "f[4:5]";
	setAttr ".iog[0].og[1].gcl" -type "componentList" 1 "f[2]";
	setAttr ".iog[0].og[2].gcl" -type "componentList" 1 "f[3]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 14 ".uvst[0].uvsp[0:13]" -type "float2" 0.375 0 0.625 0 0.375
		 0.25 0.625 0.25 0.375 0.5 0.625 0.5 0.375 0.75 0.625 0.75 0.375 1 0.625 1 0.875 0
		 0.875 0.25 0.125 0 0.125 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 8 ".pt[0:7]" -type "float3"  0 0 -1.1 0 0 -1.1 0 0 -1.1 
		0 0 -1.1 0 0 -1.1 0 0 -1.1 0 0 -1.1 0 0 -1.1;
	setAttr -s 8 ".vt[0:7]"  -0.5 -0.5 0.5 0.5 -0.5 0.5 -0.5 0.5 0.5 0.5 0.5 0.5
		 -0.5 0.5 -0.5 0.5 0.5 -0.5 -0.5 -0.5 -0.5 0.5 -0.5 -0.5;
	setAttr -s 12 ".ed[0:11]"  0 1 0 2 3 0 4 5 0 6 7 0 0 2 0 1 3 0 2 4 0
		 3 5 0 4 6 0 5 7 0 6 0 0 7 1 0;
	setAttr -s 6 -ch 24 ".fc[0:5]" -type "polyFaces" 
		f 4 0 5 -2 -5
		mu 0 4 0 1 3 2
		f 4 1 7 -3 -7
		mu 0 4 2 3 5 4
		f 4 2 9 -4 -9
		mu 0 4 4 5 7 6
		f 4 3 11 -1 -11
		mu 0 4 6 7 9 8
		f 4 -12 -10 -8 -6
		mu 0 4 1 10 11 3
		f 4 10 4 6 8
		mu 0 4 12 0 2 13;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ai_translator" -type "string" "polymesh";
createNode transform -n "rbg9" -p "geo";
	rename -uid "31AA2B24-415B-B86C-7556-4CA5339F76DE";
	setAttr ".rp" -type "double3" 1.1000000238418579 0 -1.1000000238418579 ;
	setAttr ".sp" -type "double3" 1.1000000238418579 0 -1.1000000238418579 ;
createNode mesh -n "rbgShape9" -p "rbg9";
	rename -uid "94EB9079-439B-8EEF-52F0-62BBBF3F0C27";
	setAttr -k off ".v";
	setAttr -s 4 ".iog[0].og";
	setAttr ".iog[0].og[0].gcl" -type "componentList" 2 "f[0:1]" "f[5]";
	setAttr ".iog[0].og[1].gcl" -type "componentList" 1 "f[4]";
	setAttr ".iog[0].og[2].gcl" -type "componentList" 1 "f[2]";
	setAttr ".iog[0].og[3].gcl" -type "componentList" 1 "f[3]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 14 ".uvst[0].uvsp[0:13]" -type "float2" 0.375 0 0.625 0 0.375
		 0.25 0.625 0.25 0.375 0.5 0.625 0.5 0.375 0.75 0.625 0.75 0.375 1 0.625 1 0.875 0
		 0.875 0.25 0.125 0 0.125 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 8 ".pt[0:7]" -type "float3"  1.1 0 -1.1 1.1 0 -1.1 1.1 
		0 -1.1 1.1 0 -1.1 1.1 0 -1.1 1.1 0 -1.1 1.1 0 -1.1 1.1 0 -1.1;
	setAttr -s 8 ".vt[0:7]"  -0.5 -0.5 0.5 0.5 -0.5 0.5 -0.5 0.5 0.5 0.5 0.5 0.5
		 -0.5 0.5 -0.5 0.5 0.5 -0.5 -0.5 -0.5 -0.5 0.5 -0.5 -0.5;
	setAttr -s 12 ".ed[0:11]"  0 1 0 2 3 0 4 5 0 6 7 0 0 2 0 1 3 0 2 4 0
		 3 5 0 4 6 0 5 7 0 6 0 0 7 1 0;
	setAttr -s 6 -ch 24 ".fc[0:5]" -type "polyFaces" 
		f 4 0 5 -2 -5
		mu 0 4 0 1 3 2
		f 4 1 7 -3 -7
		mu 0 4 2 3 5 4
		f 4 2 9 -4 -9
		mu 0 4 4 5 7 6
		f 4 3 11 -1 -11
		mu 0 4 6 7 9 8
		f 4 -12 -10 -8 -6
		mu 0 4 1 10 11 3
		f 4 10 4 6 8
		mu 0 4 12 0 2 13;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ai_translator" -type "string" "polymesh";
createNode transform -n "rbg10" -p "geo";
	rename -uid "54016D17-4E5A-2C71-626A-0985AF47E605";
	setAttr ".rp" -type "double3" 1.1000000238418579 1.1000000238418579 -1.1000000238418579 ;
	setAttr ".sp" -type "double3" 1.1000000238418579 1.1000000238418579 -1.1000000238418579 ;
createNode mesh -n "rbgShape10" -p "rbg10";
	rename -uid "D2DDFB6F-4BD2-C53C-F151-B1AE48DE3070";
	setAttr -k off ".v";
	setAttr -s 3 ".iog[0].og";
	setAttr ".iog[0].og[0].gcl" -type "componentList" 3 "f[0:1]" "f[3]" "f[5]";
	setAttr ".iog[0].og[1].gcl" -type "componentList" 1 "f[4]";
	setAttr ".iog[0].og[2].gcl" -type "componentList" 1 "f[2]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 14 ".uvst[0].uvsp[0:13]" -type "float2" 0.375 0 0.625 0 0.375
		 0.25 0.625 0.25 0.375 0.5 0.625 0.5 0.375 0.75 0.625 0.75 0.375 1 0.625 1 0.875 0
		 0.875 0.25 0.125 0 0.125 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 8 ".pt[0:7]" -type "float3"  1.1 1.1 -1.1 1.1 1.1 -1.1 
		1.1 1.1 -1.1 1.1 1.1 -1.1 1.1 1.1 -1.1 1.1 1.1 -1.1 1.1 1.1 -1.1 1.1 1.1 -1.1;
	setAttr -s 8 ".vt[0:7]"  -0.5 -0.5 0.5 0.5 -0.5 0.5 -0.5 0.5 0.5 0.5 0.5 0.5
		 -0.5 0.5 -0.5 0.5 0.5 -0.5 -0.5 -0.5 -0.5 0.5 -0.5 -0.5;
	setAttr -s 12 ".ed[0:11]"  0 1 0 2 3 0 4 5 0 6 7 0 0 2 0 1 3 0 2 4 0
		 3 5 0 4 6 0 5 7 0 6 0 0 7 1 0;
	setAttr -s 6 -ch 24 ".fc[0:5]" -type "polyFaces" 
		f 4 0 5 -2 -5
		mu 0 4 0 1 3 2
		f 4 1 7 -3 -7
		mu 0 4 2 3 5 4
		f 4 2 9 -4 -9
		mu 0 4 4 5 7 6
		f 4 3 11 -1 -11
		mu 0 4 6 7 9 8
		f 4 -12 -10 -8 -6
		mu 0 4 1 10 11 3
		f 4 10 4 6 8
		mu 0 4 12 0 2 13;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ai_translator" -type "string" "polymesh";
createNode transform -n "rbg11" -p "geo";
	rename -uid "A57F469E-474B-E619-9B3D-C59225095171";
	setAttr ".rp" -type "double3" 0 1.1000000238418579 -1.1000000238418579 ;
	setAttr ".sp" -type "double3" 0 1.1000000238418579 -1.1000000238418579 ;
createNode mesh -n "rbgShape11" -p "rbg11";
	rename -uid "AF396592-4ED3-33D9-BB84-6D8FCB6C7FA4";
	setAttr -k off ".v";
	setAttr -s 2 ".iog[0].og";
	setAttr ".iog[0].og[0].gcl" -type "componentList" 2 "f[0:1]" "f[3:5]";
	setAttr ".iog[0].og[1].gcl" -type "componentList" 1 "f[2]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 14 ".uvst[0].uvsp[0:13]" -type "float2" 0.375 0 0.625 0 0.375
		 0.25 0.625 0.25 0.375 0.5 0.625 0.5 0.375 0.75 0.625 0.75 0.375 1 0.625 1 0.875 0
		 0.875 0.25 0.125 0 0.125 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 8 ".pt[0:7]" -type "float3"  0 1.1 -1.1 0 1.1 -1.1 0 1.1 
		-1.1 0 1.1 -1.1 0 1.1 -1.1 0 1.1 -1.1 0 1.1 -1.1 0 1.1 -1.1;
	setAttr -s 8 ".vt[0:7]"  -0.5 -0.5 0.5 0.5 -0.5 0.5 -0.5 0.5 0.5 0.5 0.5 0.5
		 -0.5 0.5 -0.5 0.5 0.5 -0.5 -0.5 -0.5 -0.5 0.5 -0.5 -0.5;
	setAttr -s 12 ".ed[0:11]"  0 1 0 2 3 0 4 5 0 6 7 0 0 2 0 1 3 0 2 4 0
		 3 5 0 4 6 0 5 7 0 6 0 0 7 1 0;
	setAttr -s 6 -ch 24 ".fc[0:5]" -type "polyFaces" 
		f 4 0 5 -2 -5
		mu 0 4 0 1 3 2
		f 4 1 7 -3 -7
		mu 0 4 2 3 5 4
		f 4 2 9 -4 -9
		mu 0 4 4 5 7 6
		f 4 3 11 -1 -11
		mu 0 4 6 7 9 8
		f 4 -12 -10 -8 -6
		mu 0 4 1 10 11 3
		f 4 10 4 6 8
		mu 0 4 12 0 2 13;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ai_translator" -type "string" "polymesh";
createNode transform -n "rbg12" -p "geo";
	rename -uid "720ACC1F-4EB7-29B7-478F-398E9C7130DC";
	setAttr ".rp" -type "double3" -1.1000000238418579 1.1000000238418579 -1.1000000238418579 ;
	setAttr ".sp" -type "double3" -1.1000000238418579 1.1000000238418579 -1.1000000238418579 ;
createNode mesh -n "rbgShape12" -p "rbg12";
	rename -uid "34B85063-40A9-59C9-22F2-8EA403092442";
	setAttr -k off ".v";
	setAttr -s 3 ".iog[0].og";
	setAttr ".iog[0].og[0].gcl" -type "componentList" 2 "f[0:1]" "f[3:4]";
	setAttr ".iog[0].og[1].gcl" -type "componentList" 1 "f[2]";
	setAttr ".iog[0].og[2].gcl" -type "componentList" 1 "f[5]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 14 ".uvst[0].uvsp[0:13]" -type "float2" 0.375 0 0.625 0 0.375
		 0.25 0.625 0.25 0.375 0.5 0.625 0.5 0.375 0.75 0.625 0.75 0.375 1 0.625 1 0.875 0
		 0.875 0.25 0.125 0 0.125 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 8 ".pt[0:7]" -type "float3"  -1.1 1.1 -1.1 -1.1 1.1 -1.1 
		-1.1 1.1 -1.1 -1.1 1.1 -1.1 -1.1 1.1 -1.1 -1.1 1.1 -1.1 -1.1 1.1 -1.1 -1.1 1.1 -1.1;
	setAttr -s 8 ".vt[0:7]"  -0.5 -0.5 0.5 0.5 -0.5 0.5 -0.5 0.5 0.5 0.5 0.5 0.5
		 -0.5 0.5 -0.5 0.5 0.5 -0.5 -0.5 -0.5 -0.5 0.5 -0.5 -0.5;
	setAttr -s 12 ".ed[0:11]"  0 1 0 2 3 0 4 5 0 6 7 0 0 2 0 1 3 0 2 4 0
		 3 5 0 4 6 0 5 7 0 6 0 0 7 1 0;
	setAttr -s 6 -ch 24 ".fc[0:5]" -type "polyFaces" 
		f 4 0 5 -2 -5
		mu 0 4 0 1 3 2
		f 4 1 7 -3 -7
		mu 0 4 2 3 5 4
		f 4 2 9 -4 -9
		mu 0 4 4 5 7 6
		f 4 3 11 -1 -11
		mu 0 4 6 7 9 8
		f 4 -12 -10 -8 -6
		mu 0 4 1 10 11 3
		f 4 10 4 6 8
		mu 0 4 12 0 2 13;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ai_translator" -type "string" "polymesh";
createNode transform -n "rbg13" -p "geo";
	rename -uid "130D25FD-47EE-3AB6-7665-80A2B299D1F9";
	setAttr ".rp" -type "double3" 1.1000000238418579 1.1000000238418579 1.1000000238418579 ;
	setAttr ".sp" -type "double3" 1.1000000238418579 1.1000000238418579 1.1000000238418579 ;
createNode mesh -n "rbgShape13" -p "rbg13";
	rename -uid "FCAFD60C-454F-F5BE-3E62-4581925650BE";
	setAttr -k off ".v";
	setAttr -s 3 ".iog[0].og";
	setAttr ".iog[0].og[0].gcl" -type "componentList" 2 "f[1:3]" "f[5]";
	setAttr ".iog[0].og[1].gcl" -type "componentList" 1 "f[0]";
	setAttr ".iog[0].og[2].gcl" -type "componentList" 1 "f[4]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 14 ".uvst[0].uvsp[0:13]" -type "float2" 0.375 0 0.625 0 0.375
		 0.25 0.625 0.25 0.375 0.5 0.625 0.5 0.375 0.75 0.625 0.75 0.375 1 0.625 1 0.875 0
		 0.875 0.25 0.125 0 0.125 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 8 ".pt[0:7]" -type "float3"  1.1 1.1 1.1 1.1 1.1 1.1 1.1 
		1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1 1.1;
	setAttr -s 8 ".vt[0:7]"  -0.5 -0.5 0.5 0.5 -0.5 0.5 -0.5 0.5 0.5 0.5 0.5 0.5
		 -0.5 0.5 -0.5 0.5 0.5 -0.5 -0.5 -0.5 -0.5 0.5 -0.5 -0.5;
	setAttr -s 12 ".ed[0:11]"  0 1 0 2 3 0 4 5 0 6 7 0 0 2 0 1 3 0 2 4 0
		 3 5 0 4 6 0 5 7 0 6 0 0 7 1 0;
	setAttr -s 6 -ch 24 ".fc[0:5]" -type "polyFaces" 
		f 4 0 5 -2 -5
		mu 0 4 0 1 3 2
		f 4 1 7 -3 -7
		mu 0 4 2 3 5 4
		f 4 2 9 -4 -9
		mu 0 4 4 5 7 6
		f 4 3 11 -1 -11
		mu 0 4 6 7 9 8
		f 4 -12 -10 -8 -6
		mu 0 4 1 10 11 3
		f 4 10 4 6 8
		mu 0 4 12 0 2 13;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ai_translator" -type "string" "polymesh";
createNode transform -n "rbg14" -p "geo";
	rename -uid "632436B3-4BCB-0079-3379-FD924D0475F3";
	setAttr ".rp" -type "double3" 0 1.1000000238418579 1.1000000238418579 ;
	setAttr ".sp" -type "double3" 0 1.1000000238418579 1.1000000238418579 ;
createNode mesh -n "rbgShape14" -p "rbg14";
	rename -uid "6D44D287-4208-B9AD-757B-CD8A5ABAF7EA";
	setAttr -k off ".v";
	setAttr -s 2 ".iog[0].og";
	setAttr ".iog[0].og[0].gcl" -type "componentList" 1 "f[1:5]";
	setAttr ".iog[0].og[1].gcl" -type "componentList" 1 "f[0]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 14 ".uvst[0].uvsp[0:13]" -type "float2" 0.375 0 0.625 0 0.375
		 0.25 0.625 0.25 0.375 0.5 0.625 0.5 0.375 0.75 0.625 0.75 0.375 1 0.625 1 0.875 0
		 0.875 0.25 0.125 0 0.125 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 8 ".pt[0:7]" -type "float3"  0 1.1 1.1 0 1.1 1.1 0 1.1 
		1.1 0 1.1 1.1 0 1.1 1.1 0 1.1 1.1 0 1.1 1.1 0 1.1 1.1;
	setAttr -s 8 ".vt[0:7]"  -0.5 -0.5 0.5 0.5 -0.5 0.5 -0.5 0.5 0.5 0.5 0.5 0.5
		 -0.5 0.5 -0.5 0.5 0.5 -0.5 -0.5 -0.5 -0.5 0.5 -0.5 -0.5;
	setAttr -s 12 ".ed[0:11]"  0 1 0 2 3 0 4 5 0 6 7 0 0 2 0 1 3 0 2 4 0
		 3 5 0 4 6 0 5 7 0 6 0 0 7 1 0;
	setAttr -s 6 -ch 24 ".fc[0:5]" -type "polyFaces" 
		f 4 0 5 -2 -5
		mu 0 4 0 1 3 2
		f 4 1 7 -3 -7
		mu 0 4 2 3 5 4
		f 4 2 9 -4 -9
		mu 0 4 4 5 7 6
		f 4 3 11 -1 -11
		mu 0 4 6 7 9 8
		f 4 -12 -10 -8 -6
		mu 0 4 1 10 11 3
		f 4 10 4 6 8
		mu 0 4 12 0 2 13;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ai_translator" -type "string" "polymesh";
createNode transform -n "rbg15" -p "geo";
	rename -uid "AA6E9BAC-4C34-D250-17F8-D0AD1C0213E5";
	setAttr ".rp" -type "double3" -1.1000000238418579 1.1000000238418579 1.1000000238418579 ;
	setAttr ".sp" -type "double3" -1.1000000238418579 1.1000000238418579 1.1000000238418579 ;
createNode mesh -n "rbgShape15" -p "rbg15";
	rename -uid "DA123C23-4FE3-15B4-9FD0-F2B6C0774A48";
	setAttr -k off ".v";
	setAttr -s 3 ".iog[0].og";
	setAttr ".iog[0].og[0].gcl" -type "componentList" 1 "f[1:4]";
	setAttr ".iog[0].og[1].gcl" -type "componentList" 1 "f[0]";
	setAttr ".iog[0].og[2].gcl" -type "componentList" 1 "f[5]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 14 ".uvst[0].uvsp[0:13]" -type "float2" 0.375 0 0.625 0 0.375
		 0.25 0.625 0.25 0.375 0.5 0.625 0.5 0.375 0.75 0.625 0.75 0.375 1 0.625 1 0.875 0
		 0.875 0.25 0.125 0 0.125 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 8 ".pt[0:7]" -type "float3"  -1.1 1.1 1.1 -1.1 1.1 1.1 
		-1.1 1.1 1.1 -1.1 1.1 1.1 -1.1 1.1 1.1 -1.1 1.1 1.1 -1.1 1.1 1.1 -1.1 1.1 1.1;
	setAttr -s 8 ".vt[0:7]"  -0.5 -0.5 0.5 0.5 -0.5 0.5 -0.5 0.5 0.5 0.5 0.5 0.5
		 -0.5 0.5 -0.5 0.5 0.5 -0.5 -0.5 -0.5 -0.5 0.5 -0.5 -0.5;
	setAttr -s 12 ".ed[0:11]"  0 1 0 2 3 0 4 5 0 6 7 0 0 2 0 1 3 0 2 4 0
		 3 5 0 4 6 0 5 7 0 6 0 0 7 1 0;
	setAttr -s 6 -ch 24 ".fc[0:5]" -type "polyFaces" 
		f 4 0 5 -2 -5
		mu 0 4 0 1 3 2
		f 4 1 7 -3 -7
		mu 0 4 2 3 5 4
		f 4 2 9 -4 -9
		mu 0 4 4 5 7 6
		f 4 3 11 -1 -11
		mu 0 4 6 7 9 8
		f 4 -12 -10 -8 -6
		mu 0 4 1 10 11 3
		f 4 10 4 6 8
		mu 0 4 12 0 2 13;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ai_translator" -type "string" "polymesh";
createNode transform -n "rbg16" -p "geo";
	rename -uid "FE71EB7B-4538-AD4E-B84F-9EA8EE21A957";
	setAttr ".rp" -type "double3" -1.1000000238418579 1.1000000238418579 0 ;
	setAttr ".sp" -type "double3" -1.1000000238418579 1.1000000238418579 0 ;
createNode mesh -n "rbgShape16" -p "rbg16";
	rename -uid "D2A1E0DF-4FB8-1FC8-8260-8E9FDAA793DE";
	setAttr -k off ".v";
	setAttr -s 2 ".iog[0].og";
	setAttr ".iog[0].og[0].gcl" -type "componentList" 1 "f[0:4]";
	setAttr ".iog[0].og[1].gcl" -type "componentList" 1 "f[5]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 14 ".uvst[0].uvsp[0:13]" -type "float2" 0.375 0 0.625 0 0.375
		 0.25 0.625 0.25 0.375 0.5 0.625 0.5 0.375 0.75 0.625 0.75 0.375 1 0.625 1 0.875 0
		 0.875 0.25 0.125 0 0.125 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 8 ".pt[0:7]" -type "float3"  -1.1 1.1 0 -1.1 1.1 0 -1.1 
		1.1 0 -1.1 1.1 0 -1.1 1.1 0 -1.1 1.1 0 -1.1 1.1 0 -1.1 1.1 0;
	setAttr -s 8 ".vt[0:7]"  -0.5 -0.5 0.5 0.5 -0.5 0.5 -0.5 0.5 0.5 0.5 0.5 0.5
		 -0.5 0.5 -0.5 0.5 0.5 -0.5 -0.5 -0.5 -0.5 0.5 -0.5 -0.5;
	setAttr -s 12 ".ed[0:11]"  0 1 0 2 3 0 4 5 0 6 7 0 0 2 0 1 3 0 2 4 0
		 3 5 0 4 6 0 5 7 0 6 0 0 7 1 0;
	setAttr -s 6 -ch 24 ".fc[0:5]" -type "polyFaces" 
		f 4 0 5 -2 -5
		mu 0 4 0 1 3 2
		f 4 1 7 -3 -7
		mu 0 4 2 3 5 4
		f 4 2 9 -4 -9
		mu 0 4 4 5 7 6
		f 4 3 11 -1 -11
		mu 0 4 6 7 9 8
		f 4 -12 -10 -8 -6
		mu 0 4 1 10 11 3
		f 4 10 4 6 8
		mu 0 4 12 0 2 13;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ai_translator" -type "string" "polymesh";
createNode transform -n "rbg17" -p "geo";
	rename -uid "10A48F21-4BA6-31CC-B45A-D38BC913A7C5";
	setAttr ".rp" -type "double3" 1.1000000238418579 1.1000000238418579 0 ;
	setAttr ".sp" -type "double3" 1.1000000238418579 1.1000000238418579 0 ;
createNode mesh -n "rbgShape17" -p "rbg17";
	rename -uid "CF8073FA-4FFF-9517-62CC-1AA0342CB964";
	setAttr -k off ".v";
	setAttr -s 2 ".iog[0].og";
	setAttr ".iog[0].og[0].gcl" -type "componentList" 2 "f[0:3]" "f[5]";
	setAttr ".iog[0].og[1].gcl" -type "componentList" 1 "f[4]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 14 ".uvst[0].uvsp[0:13]" -type "float2" 0.375 0 0.625 0 0.375
		 0.25 0.625 0.25 0.375 0.5 0.625 0.5 0.375 0.75 0.625 0.75 0.375 1 0.625 1 0.875 0
		 0.875 0.25 0.125 0 0.125 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 8 ".pt[0:7]" -type "float3"  1.1 1.1 0 1.1 1.1 0 1.1 1.1 
		0 1.1 1.1 0 1.1 1.1 0 1.1 1.1 0 1.1 1.1 0 1.1 1.1 0;
	setAttr -s 8 ".vt[0:7]"  -0.5 -0.5 0.5 0.5 -0.5 0.5 -0.5 0.5 0.5 0.5 0.5 0.5
		 -0.5 0.5 -0.5 0.5 0.5 -0.5 -0.5 -0.5 -0.5 0.5 -0.5 -0.5;
	setAttr -s 12 ".ed[0:11]"  0 1 0 2 3 0 4 5 0 6 7 0 0 2 0 1 3 0 2 4 0
		 3 5 0 4 6 0 5 7 0 6 0 0 7 1 0;
	setAttr -s 6 -ch 24 ".fc[0:5]" -type "polyFaces" 
		f 4 0 5 -2 -5
		mu 0 4 0 1 3 2
		f 4 1 7 -3 -7
		mu 0 4 2 3 5 4
		f 4 2 9 -4 -9
		mu 0 4 4 5 7 6
		f 4 3 11 -1 -11
		mu 0 4 6 7 9 8
		f 4 -12 -10 -8 -6
		mu 0 4 1 10 11 3
		f 4 10 4 6 8
		mu 0 4 12 0 2 13;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ai_translator" -type "string" "polymesh";
createNode transform -n "rbg18" -p "geo";
	rename -uid "E8A5D390-45A0-2376-8CD3-33BEF1417A7D";
	setAttr ".rp" -type "double3" 1.1000000238418579 2.2000000476837158 -1.1000000238418579 ;
	setAttr ".sp" -type "double3" 1.1000000238418579 2.2000000476837158 -1.1000000238418579 ;
createNode mesh -n "rbgShape18" -p "rbg18";
	rename -uid "BEBE0F8F-4398-A166-7A58-F68348505369";
	setAttr -k off ".v";
	setAttr -s 4 ".iog[0].og";
	setAttr ".iog[0].og[0].gcl" -type "componentList" 3 "f[0]" "f[3]" "f[5]";
	setAttr ".iog[0].og[1].gcl" -type "componentList" 1 "f[1]";
	setAttr ".iog[0].og[2].gcl" -type "componentList" 1 "f[4]";
	setAttr ".iog[0].og[3].gcl" -type "componentList" 1 "f[2]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 14 ".uvst[0].uvsp[0:13]" -type "float2" 0.375 0 0.625 0 0.375
		 0.25 0.625 0.25 0.375 0.5 0.625 0.5 0.375 0.75 0.625 0.75 0.375 1 0.625 1 0.875 0
		 0.875 0.25 0.125 0 0.125 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 8 ".pt[0:7]" -type "float3"  1.1 2.2 -1.1 1.1 2.2 -1.1 
		1.1 2.2 -1.1 1.1 2.2 -1.1 1.1 2.2 -1.1 1.1 2.2 -1.1 1.1 2.2 -1.1 1.1 2.2 -1.1;
	setAttr -s 8 ".vt[0:7]"  -0.5 -0.5 0.5 0.5 -0.5 0.5 -0.5 0.5 0.5 0.5 0.5 0.5
		 -0.5 0.5 -0.5 0.5 0.5 -0.5 -0.5 -0.5 -0.5 0.5 -0.5 -0.5;
	setAttr -s 12 ".ed[0:11]"  0 1 0 2 3 0 4 5 0 6 7 0 0 2 0 1 3 0 2 4 0
		 3 5 0 4 6 0 5 7 0 6 0 0 7 1 0;
	setAttr -s 6 -ch 24 ".fc[0:5]" -type "polyFaces" 
		f 4 0 5 -2 -5
		mu 0 4 0 1 3 2
		f 4 1 7 -3 -7
		mu 0 4 2 3 5 4
		f 4 2 9 -4 -9
		mu 0 4 4 5 7 6
		f 4 3 11 -1 -11
		mu 0 4 6 7 9 8
		f 4 -12 -10 -8 -6
		mu 0 4 1 10 11 3
		f 4 10 4 6 8
		mu 0 4 12 0 2 13;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ai_translator" -type "string" "polymesh";
createNode transform -n "rbg19" -p "geo";
	rename -uid "51A60E01-4D59-B8D2-D0C8-67BD26BB4225";
	setAttr ".rp" -type "double3" 0 2.2000000476837158 -1.1000000238418579 ;
	setAttr ".sp" -type "double3" 0 2.2000000476837158 -1.1000000238418579 ;
createNode mesh -n "rbgShape19" -p "rbg19";
	rename -uid "C8C2D137-4F92-EA21-7148-E7A4D41ACD4B";
	setAttr -k off ".v";
	setAttr -s 3 ".iog[0].og";
	setAttr ".iog[0].og[0].gcl" -type "componentList" 2 "f[0]" "f[3:5]";
	setAttr ".iog[0].og[1].gcl" -type "componentList" 1 "f[1]";
	setAttr ".iog[0].og[2].gcl" -type "componentList" 1 "f[2]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 14 ".uvst[0].uvsp[0:13]" -type "float2" 0.375 0 0.625 0 0.375
		 0.25 0.625 0.25 0.375 0.5 0.625 0.5 0.375 0.75 0.625 0.75 0.375 1 0.625 1 0.875 0
		 0.875 0.25 0.125 0 0.125 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 8 ".pt[0:7]" -type "float3"  0 2.2 -1.1 0 2.2 -1.1 0 2.2 
		-1.1 0 2.2 -1.1 0 2.2 -1.1 0 2.2 -1.1 0 2.2 -1.1 0 2.2 -1.1;
	setAttr -s 8 ".vt[0:7]"  -0.5 -0.5 0.5 0.5 -0.5 0.5 -0.5 0.5 0.5 0.5 0.5 0.5
		 -0.5 0.5 -0.5 0.5 0.5 -0.5 -0.5 -0.5 -0.5 0.5 -0.5 -0.5;
	setAttr -s 12 ".ed[0:11]"  0 1 0 2 3 0 4 5 0 6 7 0 0 2 0 1 3 0 2 4 0
		 3 5 0 4 6 0 5 7 0 6 0 0 7 1 0;
	setAttr -s 6 -ch 24 ".fc[0:5]" -type "polyFaces" 
		f 4 0 5 -2 -5
		mu 0 4 0 1 3 2
		f 4 1 7 -3 -7
		mu 0 4 2 3 5 4
		f 4 2 9 -4 -9
		mu 0 4 4 5 7 6
		f 4 3 11 -1 -11
		mu 0 4 6 7 9 8
		f 4 -12 -10 -8 -6
		mu 0 4 1 10 11 3
		f 4 10 4 6 8
		mu 0 4 12 0 2 13;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ai_translator" -type "string" "polymesh";
createNode transform -n "rbg20" -p "geo";
	rename -uid "A71CD619-48D4-BF99-7380-B1A95DDC1CEE";
	setAttr ".rp" -type "double3" -1.1000000238418579 2.2000000476837158 -1.1000000238418579 ;
	setAttr ".sp" -type "double3" -1.1000000238418579 2.2000000476837158 -1.1000000238418579 ;
createNode mesh -n "rbgShape20" -p "rbg20";
	rename -uid "B20576F8-44A5-4FB5-656D-1D9EAA3905ED";
	setAttr -k off ".v";
	setAttr -s 4 ".iog[0].og";
	setAttr ".iog[0].og[0].gcl" -type "componentList" 2 "f[0]" "f[3:4]";
	setAttr ".iog[0].og[1].gcl" -type "componentList" 1 "f[1]";
	setAttr ".iog[0].og[2].gcl" -type "componentList" 1 "f[2]";
	setAttr ".iog[0].og[3].gcl" -type "componentList" 1 "f[5]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 14 ".uvst[0].uvsp[0:13]" -type "float2" 0.375 0 0.625 0 0.375
		 0.25 0.625 0.25 0.375 0.5 0.625 0.5 0.375 0.75 0.625 0.75 0.375 1 0.625 1 0.875 0
		 0.875 0.25 0.125 0 0.125 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 8 ".pt[0:7]" -type "float3"  -1.1 2.2 -1.1 -1.1 2.2 -1.1 
		-1.1 2.2 -1.1 -1.1 2.2 -1.1 -1.1 2.2 -1.1 -1.1 2.2 -1.1 -1.1 2.2 -1.1 -1.1 2.2 -1.1;
	setAttr -s 8 ".vt[0:7]"  -0.5 -0.5 0.5 0.5 -0.5 0.5 -0.5 0.5 0.5 0.5 0.5 0.5
		 -0.5 0.5 -0.5 0.5 0.5 -0.5 -0.5 -0.5 -0.5 0.5 -0.5 -0.5;
	setAttr -s 12 ".ed[0:11]"  0 1 0 2 3 0 4 5 0 6 7 0 0 2 0 1 3 0 2 4 0
		 3 5 0 4 6 0 5 7 0 6 0 0 7 1 0;
	setAttr -s 6 -ch 24 ".fc[0:5]" -type "polyFaces" 
		f 4 0 5 -2 -5
		mu 0 4 0 1 3 2
		f 4 1 7 -3 -7
		mu 0 4 2 3 5 4
		f 4 2 9 -4 -9
		mu 0 4 4 5 7 6
		f 4 3 11 -1 -11
		mu 0 4 6 7 9 8
		f 4 -12 -10 -8 -6
		mu 0 4 1 10 11 3
		f 4 10 4 6 8
		mu 0 4 12 0 2 13;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ai_translator" -type "string" "polymesh";
createNode transform -n "rbg21" -p "geo";
	rename -uid "4D216C05-47DE-8684-FE70-CAADCF2F2C06";
	setAttr ".rp" -type "double3" 1.1000000238418579 2.2000000476837158 1.1000000238418579 ;
	setAttr ".sp" -type "double3" 1.1000000238418579 2.2000000476837158 1.1000000238418579 ;
createNode mesh -n "rbgShape21" -p "rbg21";
	rename -uid "FDD2DF53-4DF9-3AC6-292C-C59A46038E34";
	setAttr -k off ".v";
	setAttr -s 4 ".iog[0].og";
	setAttr ".iog[0].og[0].gcl" -type "componentList" 2 "f[2:3]" "f[5]";
	setAttr ".iog[0].og[1].gcl" -type "componentList" 1 "f[0]";
	setAttr ".iog[0].og[2].gcl" -type "componentList" 1 "f[1]";
	setAttr ".iog[0].og[3].gcl" -type "componentList" 1 "f[4]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 14 ".uvst[0].uvsp[0:13]" -type "float2" 0.375 0 0.625 0 0.375
		 0.25 0.625 0.25 0.375 0.5 0.625 0.5 0.375 0.75 0.625 0.75 0.375 1 0.625 1 0.875 0
		 0.875 0.25 0.125 0 0.125 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 8 ".pt[0:7]" -type "float3"  1.1 2.2 1.1 1.1 2.2 1.1 1.1 
		2.2 1.1 1.1 2.2 1.1 1.1 2.2 1.1 1.1 2.2 1.1 1.1 2.2 1.1 1.1 2.2 1.1;
	setAttr -s 8 ".vt[0:7]"  -0.5 -0.5 0.5 0.5 -0.5 0.5 -0.5 0.5 0.5 0.5 0.5 0.5
		 -0.5 0.5 -0.5 0.5 0.5 -0.5 -0.5 -0.5 -0.5 0.5 -0.5 -0.5;
	setAttr -s 12 ".ed[0:11]"  0 1 0 2 3 0 4 5 0 6 7 0 0 2 0 1 3 0 2 4 0
		 3 5 0 4 6 0 5 7 0 6 0 0 7 1 0;
	setAttr -s 6 -ch 24 ".fc[0:5]" -type "polyFaces" 
		f 4 0 5 -2 -5
		mu 0 4 0 1 3 2
		f 4 1 7 -3 -7
		mu 0 4 2 3 5 4
		f 4 2 9 -4 -9
		mu 0 4 4 5 7 6
		f 4 3 11 -1 -11
		mu 0 4 6 7 9 8
		f 4 -12 -10 -8 -6
		mu 0 4 1 10 11 3
		f 4 10 4 6 8
		mu 0 4 12 0 2 13;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ai_translator" -type "string" "polymesh";
createNode transform -n "rbg22" -p "geo";
	rename -uid "52FBAAC4-49A4-FB48-12EE-84870D59F1C8";
	setAttr ".rp" -type "double3" 0 2.2000000476837158 1.1000000238418579 ;
	setAttr ".sp" -type "double3" 0 2.2000000476837158 1.1000000238418579 ;
createNode mesh -n "rbgShape22" -p "rbg22";
	rename -uid "C1F30FC0-49CF-72E7-8AD2-FC90674D5A7B";
	setAttr -k off ".v";
	setAttr -s 3 ".iog[0].og";
	setAttr ".iog[0].og[0].gcl" -type "componentList" 1 "f[2:5]";
	setAttr ".iog[0].og[1].gcl" -type "componentList" 1 "f[0]";
	setAttr ".iog[0].og[2].gcl" -type "componentList" 1 "f[1]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 14 ".uvst[0].uvsp[0:13]" -type "float2" 0.375 0 0.625 0 0.375
		 0.25 0.625 0.25 0.375 0.5 0.625 0.5 0.375 0.75 0.625 0.75 0.375 1 0.625 1 0.875 0
		 0.875 0.25 0.125 0 0.125 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 8 ".pt[0:7]" -type "float3"  0 2.2 1.1 0 2.2 1.1 0 2.2 
		1.1 0 2.2 1.1 0 2.2 1.1 0 2.2 1.1 0 2.2 1.1 0 2.2 1.1;
	setAttr -s 8 ".vt[0:7]"  -0.5 -0.5 0.5 0.5 -0.5 0.5 -0.5 0.5 0.5 0.5 0.5 0.5
		 -0.5 0.5 -0.5 0.5 0.5 -0.5 -0.5 -0.5 -0.5 0.5 -0.5 -0.5;
	setAttr -s 12 ".ed[0:11]"  0 1 0 2 3 0 4 5 0 6 7 0 0 2 0 1 3 0 2 4 0
		 3 5 0 4 6 0 5 7 0 6 0 0 7 1 0;
	setAttr -s 6 -ch 24 ".fc[0:5]" -type "polyFaces" 
		f 4 0 5 -2 -5
		mu 0 4 0 1 3 2
		f 4 1 7 -3 -7
		mu 0 4 2 3 5 4
		f 4 2 9 -4 -9
		mu 0 4 4 5 7 6
		f 4 3 11 -1 -11
		mu 0 4 6 7 9 8
		f 4 -12 -10 -8 -6
		mu 0 4 1 10 11 3
		f 4 10 4 6 8
		mu 0 4 12 0 2 13;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ai_translator" -type "string" "polymesh";
createNode transform -n "rbg23" -p "geo";
	rename -uid "13D645EB-43A2-A935-5FF3-83B753A14FDA";
	setAttr ".rp" -type "double3" -1.1000000238418579 2.2000000476837158 1.1000000238418579 ;
	setAttr ".sp" -type "double3" -1.1000000238418579 2.2000000476837158 1.1000000238418579 ;
createNode mesh -n "rbgShape23" -p "rbg23";
	rename -uid "F5681574-4524-1F3A-87D8-F8A7AFAA192F";
	setAttr -k off ".v";
	setAttr -s 4 ".iog[0].og";
	setAttr ".iog[0].og[0].gcl" -type "componentList" 1 "f[2:4]";
	setAttr ".iog[0].og[1].gcl" -type "componentList" 1 "f[0]";
	setAttr ".iog[0].og[2].gcl" -type "componentList" 1 "f[1]";
	setAttr ".iog[0].og[3].gcl" -type "componentList" 1 "f[5]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 14 ".uvst[0].uvsp[0:13]" -type "float2" 0.375 0 0.625 0 0.375
		 0.25 0.625 0.25 0.375 0.5 0.625 0.5 0.375 0.75 0.625 0.75 0.375 1 0.625 1 0.875 0
		 0.875 0.25 0.125 0 0.125 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 8 ".pt[0:7]" -type "float3"  -1.1 2.2 1.1 -1.1 2.2 1.1 
		-1.1 2.2 1.1 -1.1 2.2 1.1 -1.1 2.2 1.1 -1.1 2.2 1.1 -1.1 2.2 1.1 -1.1 2.2 1.1;
	setAttr -s 8 ".vt[0:7]"  -0.5 -0.5 0.5 0.5 -0.5 0.5 -0.5 0.5 0.5 0.5 0.5 0.5
		 -0.5 0.5 -0.5 0.5 0.5 -0.5 -0.5 -0.5 -0.5 0.5 -0.5 -0.5;
	setAttr -s 12 ".ed[0:11]"  0 1 0 2 3 0 4 5 0 6 7 0 0 2 0 1 3 0 2 4 0
		 3 5 0 4 6 0 5 7 0 6 0 0 7 1 0;
	setAttr -s 6 -ch 24 ".fc[0:5]" -type "polyFaces" 
		f 4 0 5 -2 -5
		mu 0 4 0 1 3 2
		f 4 1 7 -3 -7
		mu 0 4 2 3 5 4
		f 4 2 9 -4 -9
		mu 0 4 4 5 7 6
		f 4 3 11 -1 -11
		mu 0 4 6 7 9 8
		f 4 -12 -10 -8 -6
		mu 0 4 1 10 11 3
		f 4 10 4 6 8
		mu 0 4 12 0 2 13;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ai_translator" -type "string" "polymesh";
createNode transform -n "rbg24" -p "geo";
	rename -uid "FF4CA99E-41C3-64F1-6327-02A90A58E967";
	setAttr ".rp" -type "double3" -1.1000000238418579 2.2000000476837158 0 ;
	setAttr ".sp" -type "double3" -1.1000000238418579 2.2000000476837158 0 ;
createNode mesh -n "rbgShape24" -p "rbg24";
	rename -uid "1D3B6073-4D5C-409C-C9E0-D68B9F2CF22E";
	setAttr -k off ".v";
	setAttr -s 3 ".iog[0].og";
	setAttr ".iog[0].og[0].gcl" -type "componentList" 2 "f[0]" "f[2:4]";
	setAttr ".iog[0].og[1].gcl" -type "componentList" 1 "f[1]";
	setAttr ".iog[0].og[2].gcl" -type "componentList" 1 "f[5]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 14 ".uvst[0].uvsp[0:13]" -type "float2" 0.375 0 0.625 0 0.375
		 0.25 0.625 0.25 0.375 0.5 0.625 0.5 0.375 0.75 0.625 0.75 0.375 1 0.625 1 0.875 0
		 0.875 0.25 0.125 0 0.125 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 8 ".pt[0:7]" -type "float3"  -1.1 2.2 0 -1.1 2.2 0 -1.1 
		2.2 0 -1.1 2.2 0 -1.1 2.2 0 -1.1 2.2 0 -1.1 2.2 0 -1.1 2.2 0;
	setAttr -s 8 ".vt[0:7]"  -0.5 -0.5 0.5 0.5 -0.5 0.5 -0.5 0.5 0.5 0.5 0.5 0.5
		 -0.5 0.5 -0.5 0.5 0.5 -0.5 -0.5 -0.5 -0.5 0.5 -0.5 -0.5;
	setAttr -s 12 ".ed[0:11]"  0 1 0 2 3 0 4 5 0 6 7 0 0 2 0 1 3 0 2 4 0
		 3 5 0 4 6 0 5 7 0 6 0 0 7 1 0;
	setAttr -s 6 -ch 24 ".fc[0:5]" -type "polyFaces" 
		f 4 0 5 -2 -5
		mu 0 4 0 1 3 2
		f 4 1 7 -3 -7
		mu 0 4 2 3 5 4
		f 4 2 9 -4 -9
		mu 0 4 4 5 7 6
		f 4 3 11 -1 -11
		mu 0 4 6 7 9 8
		f 4 -12 -10 -8 -6
		mu 0 4 1 10 11 3
		f 4 10 4 6 8
		mu 0 4 12 0 2 13;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ai_translator" -type "string" "polymesh";
createNode transform -n "rbg25" -p "geo";
	rename -uid "F33B1E8C-4D56-7116-A51A-658D778891B5";
	setAttr ".rp" -type "double3" 0 2.2000000476837158 0 ;
	setAttr ".sp" -type "double3" 0 2.2000000476837158 0 ;
createNode mesh -n "rbgShape25" -p "rbg25";
	rename -uid "E77574A7-46C6-A400-47AE-8882B7CE546D";
	setAttr -k off ".v";
	setAttr -s 2 ".iog[0].og";
	setAttr ".iog[0].og[0].gcl" -type "componentList" 2 "f[0]" "f[2:5]";
	setAttr ".iog[0].og[1].gcl" -type "componentList" 1 "f[1]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 14 ".uvst[0].uvsp[0:13]" -type "float2" 0.375 0 0.625 0 0.375
		 0.25 0.625 0.25 0.375 0.5 0.625 0.5 0.375 0.75 0.625 0.75 0.375 1 0.625 1 0.875 0
		 0.875 0.25 0.125 0 0.125 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 8 ".pt[0:7]" -type "float3"  0 2.2 0 0 2.2 0 0 2.2 0 0 
		2.2 0 0 2.2 0 0 2.2 0 0 2.2 0 0 2.2 0;
	setAttr -s 8 ".vt[0:7]"  -0.5 -0.5 0.5 0.5 -0.5 0.5 -0.5 0.5 0.5 0.5 0.5 0.5
		 -0.5 0.5 -0.5 0.5 0.5 -0.5 -0.5 -0.5 -0.5 0.5 -0.5 -0.5;
	setAttr -s 12 ".ed[0:11]"  0 1 0 2 3 0 4 5 0 6 7 0 0 2 0 1 3 0 2 4 0
		 3 5 0 4 6 0 5 7 0 6 0 0 7 1 0;
	setAttr -s 6 -ch 24 ".fc[0:5]" -type "polyFaces" 
		f 4 0 5 -2 -5
		mu 0 4 0 1 3 2
		f 4 1 7 -3 -7
		mu 0 4 2 3 5 4
		f 4 2 9 -4 -9
		mu 0 4 4 5 7 6
		f 4 3 11 -1 -11
		mu 0 4 6 7 9 8
		f 4 -12 -10 -8 -6
		mu 0 4 1 10 11 3
		f 4 10 4 6 8
		mu 0 4 12 0 2 13;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ai_translator" -type "string" "polymesh";
createNode transform -n "rbg26" -p "geo";
	rename -uid "0E1BE957-4E54-4656-EEAA-EFB71BA55384";
	setAttr ".rp" -type "double3" 1.1000000238418579 2.2000000476837158 0 ;
	setAttr ".sp" -type "double3" 1.1000000238418579 2.2000000476837158 0 ;
createNode mesh -n "rbgShape26" -p "rbg26";
	rename -uid "CC80FB05-47E7-E1B6-7827-BE914189C491";
	setAttr -k off ".v";
	setAttr -s 3 ".iog[0].og";
	setAttr ".iog[0].og[0].gcl" -type "componentList" 3 "f[0]" "f[2:3]" "f[5]";
	setAttr ".iog[0].og[1].gcl" -type "componentList" 1 "f[1]";
	setAttr ".iog[0].og[2].gcl" -type "componentList" 1 "f[4]";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 14 ".uvst[0].uvsp[0:13]" -type "float2" 0.375 0 0.625 0 0.375
		 0.25 0.625 0.25 0.375 0.5 0.625 0.5 0.375 0.75 0.625 0.75 0.375 1 0.625 1 0.875 0
		 0.875 0.25 0.125 0 0.125 0.25;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 8 ".pt[0:7]" -type "float3"  1.1 2.2 0 1.1 2.2 0 1.1 2.2 
		0 1.1 2.2 0 1.1 2.2 0 1.1 2.2 0 1.1 2.2 0 1.1 2.2 0;
	setAttr -s 8 ".vt[0:7]"  -0.5 -0.5 0.5 0.5 -0.5 0.5 -0.5 0.5 0.5 0.5 0.5 0.5
		 -0.5 0.5 -0.5 0.5 0.5 -0.5 -0.5 -0.5 -0.5 0.5 -0.5 -0.5;
	setAttr -s 12 ".ed[0:11]"  0 1 0 2 3 0 4 5 0 6 7 0 0 2 0 1 3 0 2 4 0
		 3 5 0 4 6 0 5 7 0 6 0 0 7 1 0;
	setAttr -s 6 -ch 24 ".fc[0:5]" -type "polyFaces" 
		f 4 0 5 -2 -5
		mu 0 4 0 1 3 2
		f 4 1 7 -3 -7
		mu 0 4 2 3 5 4
		f 4 2 9 -4 -9
		mu 0 4 4 5 7 6
		f 4 3 11 -1 -11
		mu 0 4 6 7 9 8
		f 4 -12 -10 -8 -6
		mu 0 4 1 10 11 3
		f 4 10 4 6 8
		mu 0 4 12 0 2 13;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
	setAttr ".ai_translator" -type "string" "polymesh";
createNode transform -n "jnt";
	rename -uid "91050102-410A-2DB1-6AB0-768F35586191";
createNode joint -n "rbg26J" -p "jnt";
	rename -uid "7457283E-4449-5E59-97CA-74AA5494215F";
	setAttr ".t" -type "double3" 1.1000000238418579 2.2000000476837158 0 ;
	setAttr ".radi" 0.5;
createNode joint -n "rbg1J" -p "jnt";
	rename -uid "564A577C-46F5-562B-3B87-E28DB897340B";
	setAttr ".radi" 0.5;
createNode joint -n "rbg2J" -p "jnt";
	rename -uid "CC0F5E71-45B1-C808-09B5-75B71E1A579C";
	setAttr ".t" -type "double3" 1.1000000238418579 0 0 ;
	setAttr ".radi" 0.5;
createNode joint -n "rbg3J" -p "jnt";
	rename -uid "9B59C85F-407E-EA05-FC20-89B1ADDBF4D5";
	setAttr ".t" -type "double3" -1.1000000238418579 0 0 ;
	setAttr ".radi" 0.5;
createNode joint -n "rbg4J" -p "jnt";
	rename -uid "E60A7ADA-4CAF-80AA-F0E8-66AA8FEEA3AC";
	setAttr ".t" -type "double3" -1.1000000238418579 0 1.1000000238418579 ;
	setAttr ".radi" 0.5;
createNode joint -n "rbg5J" -p "jnt";
	rename -uid "23D73578-4AAF-B783-F33B-A58E61876347";
	setAttr ".t" -type "double3" 0 0 1.1000000238418579 ;
	setAttr ".radi" 0.5;
createNode joint -n "rbg6J" -p "jnt";
	rename -uid "041620A5-49AC-C5CF-FF71-7F940115760D";
	setAttr ".t" -type "double3" 1.1000000238418579 0 1.1000000238418579 ;
	setAttr ".radi" 0.5;
createNode joint -n "rbg7J" -p "jnt";
	rename -uid "893279DB-423E-457B-B51C-23BD607469E6";
	setAttr ".t" -type "double3" -1.1000000238418579 0 -1.1000000238418579 ;
	setAttr ".radi" 0.5;
createNode joint -n "rbg8J" -p "jnt";
	rename -uid "77667181-4AA6-7952-EF59-0B8C5655BCA7";
	setAttr ".t" -type "double3" 0 0 -1.1000000238418579 ;
	setAttr ".radi" 0.5;
createNode joint -n "rbg9J" -p "jnt";
	rename -uid "CE324709-4F60-0C77-CD6F-9D845D583B26";
	setAttr ".t" -type "double3" 1.1000000238418579 0 -1.1000000238418579 ;
	setAttr ".radi" 0.5;
createNode joint -n "rbg10J" -p "jnt";
	rename -uid "F06B62C8-4E93-0047-4F1F-718E936C88EF";
	setAttr ".t" -type "double3" 1.1000000238418579 1.1000000238418579 -1.1000000238418579 ;
	setAttr ".radi" 0.5;
createNode joint -n "rbg11J" -p "jnt";
	rename -uid "B639309E-41B5-AE6E-1562-429EF4EB3601";
	setAttr ".t" -type "double3" 0 1.1000000238418579 -1.1000000238418579 ;
	setAttr ".radi" 0.5;
createNode joint -n "rbg12J" -p "jnt";
	rename -uid "4649E63B-4365-DEB8-FCA4-BF84E7C9577C";
	setAttr ".t" -type "double3" -1.1000000238418579 1.1000000238418579 -1.1000000238418579 ;
	setAttr ".radi" 0.5;
createNode joint -n "rbg13J" -p "jnt";
	rename -uid "179974BC-49A8-D723-1BAC-3B8C2F600889";
	setAttr ".t" -type "double3" 1.1000000238418579 1.1000000238418579 1.1000000238418579 ;
	setAttr ".radi" 0.5;
createNode joint -n "rbg14J" -p "jnt";
	rename -uid "BEDD15D9-4496-02B4-3653-9D81B4819BF0";
	setAttr ".t" -type "double3" 0 1.1000000238418579 1.1000000238418579 ;
	setAttr ".radi" 0.5;
createNode joint -n "rbg15J" -p "jnt";
	rename -uid "70E5D19A-4BE1-6AAD-FED1-EB9D5FA9CFA3";
	setAttr ".t" -type "double3" -1.1000000238418579 1.1000000238418579 1.1000000238418579 ;
	setAttr ".radi" 0.5;
createNode joint -n "rbg16J" -p "jnt";
	rename -uid "D4BECB89-46AB-1BB9-712E-D09EF102262D";
	setAttr ".t" -type "double3" -1.1000000238418579 1.1000000238418579 0 ;
	setAttr ".radi" 0.5;
createNode joint -n "rbg17J" -p "jnt";
	rename -uid "C9F03F22-41C4-5AA3-2E00-B095DEF093F5";
	setAttr ".t" -type "double3" 1.1000000238418579 1.1000000238418579 0 ;
	setAttr ".radi" 0.5;
createNode joint -n "rbg18J" -p "jnt";
	rename -uid "DBDC418C-4868-6403-8C04-25921DDE08F1";
	setAttr ".t" -type "double3" 1.1000000238418579 2.2000000476837158 -1.1000000238418579 ;
	setAttr ".radi" 0.5;
createNode joint -n "rbg19J" -p "jnt";
	rename -uid "7F98AFD0-4693-F610-79FE-07946B4A157F";
	setAttr ".t" -type "double3" 0 2.2000000476837158 -1.1000000238418579 ;
	setAttr ".radi" 0.5;
createNode joint -n "rbg20J" -p "jnt";
	rename -uid "70CE153E-46F3-3307-2723-47B3E5524C60";
	setAttr ".t" -type "double3" -1.1000000238418579 2.2000000476837158 -1.1000000238418579 ;
	setAttr ".radi" 0.5;
createNode joint -n "rbg21J" -p "jnt";
	rename -uid "D5945029-420B-2A3F-FF40-D08832D5B322";
	setAttr ".t" -type "double3" 1.1000000238418579 2.2000000476837158 1.1000000238418579 ;
	setAttr ".radi" 0.5;
createNode joint -n "rbg22J" -p "jnt";
	rename -uid "21B5B3B6-48BF-39C1-A0D4-1887F3990F77";
	setAttr ".t" -type "double3" 0 2.2000000476837158 1.1000000238418579 ;
	setAttr ".radi" 0.5;
createNode joint -n "rbg23J" -p "jnt";
	rename -uid "80AF69BE-4FFD-E8DD-E21C-ACBB40D7416B";
	setAttr ".t" -type "double3" -1.1000000238418579 2.2000000476837158 1.1000000238418579 ;
	setAttr ".radi" 0.5;
createNode joint -n "rbg24J" -p "jnt";
	rename -uid "CBB3ED25-4F10-C382-3A74-0193CE26746D";
	setAttr ".t" -type "double3" -1.1000000238418579 2.2000000476837158 0 ;
	setAttr ".radi" 0.5;
createNode joint -n "rbg25J" -p "jnt";
	rename -uid "9E5C94BF-4E10-64A3-2991-8D819D113713";
	setAttr ".t" -type "double3" 0 2.2000000476837158 0 ;
	setAttr ".radi" 0.5;
createNode lightLinker -s -n "lightLinker1";
	rename -uid "B707F72E-4DDA-9CD7-B86B-3FA4B1A8E7B9";
	setAttr -s 8 ".lnk";
	setAttr -s 8 ".slnk";
createNode shapeEditorManager -n "shapeEditorManager";
	rename -uid "1C0FCB49-4A2D-E2A1-E7E7-C7B0525D49BD";
createNode poseInterpolatorManager -n "poseInterpolatorManager";
	rename -uid "A185032A-41EC-F8BF-4CAC-91B216154A80";
createNode displayLayerManager -n "layerManager";
	rename -uid "30355B8B-4D15-B251-E566-C3916A485093";
createNode displayLayer -n "defaultLayer";
	rename -uid "8D8CEBB7-40C8-E15E-E9D8-53A35C197F85";
createNode renderLayerManager -n "renderLayerManager";
	rename -uid "937C28EC-4FFA-D9F9-540F-FE943354660F";
createNode renderLayer -n "defaultRenderLayer";
	rename -uid "BCBC221A-4110-6666-69B1-73BDAF3DFFED";
	setAttr ".g" yes;
createNode multMatrix -n "mamamama";
	rename -uid "DD1E5958-4EF8-5715-3D06-8AB6625BBB4E";
	setAttr -s 3 ".i";
createNode decomposeMatrix -n "mama";
	rename -uid "69116D39-40B4-2D90-BC12-D8BF53C974E7";
createNode decomposeMatrix -n "mama1";
	rename -uid "3212EFCF-4117-9338-1E87-95BF1BFD7B5D";
createNode lambert -n "red";
	rename -uid "872455DC-4BE8-C40B-90FF-4A913D0EAD1C";
	setAttr ".c" -type "float3" 1 0 0 ;
createNode shadingEngine -n "lambert2SG";
	rename -uid "A56415A4-4A06-23F9-82D8-5AB3F1FCF392";
	setAttr ".ihi" 0;
	setAttr -s 9 ".dsm";
	setAttr ".ro" yes;
	setAttr -s 9 ".gn";
createNode materialInfo -n "materialInfo1";
	rename -uid "12517EB0-4810-0723-4E06-809915796494";
createNode groupId -n "groupId1";
	rename -uid "6597FBD6-4DED-D60A-9511-0586CDDA04B6";
	setAttr ".ihi" 0;
createNode groupId -n "groupId2";
	rename -uid "524D71AE-4034-47FC-7D95-2191ECF54532";
	setAttr ".ihi" 0;
createNode groupId -n "groupId3";
	rename -uid "0C7D020D-452F-BD70-6F57-6996D1E80B37";
	setAttr ".ihi" 0;
createNode groupId -n "groupId4";
	rename -uid "7B2131BC-478C-6D1B-AA05-7BBF88AC95A3";
	setAttr ".ihi" 0;
createNode groupId -n "groupId5";
	rename -uid "D436B516-4196-5448-BF48-2EBF8BF0AD48";
	setAttr ".ihi" 0;
createNode groupId -n "groupId6";
	rename -uid "1AB62F9E-4332-32E6-1DB0-77B99BB284D5";
	setAttr ".ihi" 0;
createNode groupId -n "groupId7";
	rename -uid "8E3ADB18-416A-82C9-EFCD-EEA71B078D4B";
	setAttr ".ihi" 0;
createNode groupId -n "groupId8";
	rename -uid "19CB1E17-42A7-9A02-C4BC-8AA82E7A6F94";
	setAttr ".ihi" 0;
createNode groupId -n "groupId9";
	rename -uid "83ABB774-45D0-2FBE-849A-278C40FCAACB";
	setAttr ".ihi" 0;
createNode groupId -n "groupId10";
	rename -uid "F35EE250-4CC1-F349-6B08-9187DB2631E5";
	setAttr ".ihi" 0;
createNode groupId -n "groupId11";
	rename -uid "DAE9B4A6-4050-10A0-456D-17895A120988";
	setAttr ".ihi" 0;
createNode groupId -n "groupId12";
	rename -uid "D61AB85B-4DD8-D1CB-9B1A-66AC25FFDF12";
	setAttr ".ihi" 0;
createNode groupId -n "groupId13";
	rename -uid "EE273C97-46CF-C61C-C710-25976F30FB7C";
	setAttr ".ihi" 0;
createNode groupId -n "groupId14";
	rename -uid "4EB05C36-4712-5336-37CF-0DACC93100F0";
	setAttr ".ihi" 0;
createNode groupId -n "groupId15";
	rename -uid "5E73A916-4550-9FCD-C4BD-8486DDD01A72";
	setAttr ".ihi" 0;
createNode groupId -n "groupId16";
	rename -uid "B3A3393D-48A7-7306-A241-FD9013D741DA";
	setAttr ".ihi" 0;
createNode groupId -n "groupId17";
	rename -uid "0C29CED3-451F-F9A6-2AE2-EA8DB08E8CE6";
	setAttr ".ihi" 0;
createNode groupId -n "groupId18";
	rename -uid "B31158C4-4072-248F-1615-1FBB112CCDDC";
	setAttr ".ihi" 0;
createNode groupId -n "groupId19";
	rename -uid "EF453A44-48DC-9611-3E79-6E8243BF252E";
	setAttr ".ihi" 0;
createNode groupId -n "groupId20";
	rename -uid "BA05C7D4-4B34-268D-7D4F-9CB98CB2A51D";
	setAttr ".ihi" 0;
createNode groupId -n "groupId21";
	rename -uid "387B3398-4F14-1EFC-CAF6-639896A52DF1";
	setAttr ".ihi" 0;
createNode groupId -n "groupId22";
	rename -uid "67316B97-4914-59BE-BAEE-1E94E111281B";
	setAttr ".ihi" 0;
createNode groupId -n "groupId23";
	rename -uid "46065106-4767-101A-EF12-8AB4BB4709B5";
	setAttr ".ihi" 0;
createNode groupId -n "groupId24";
	rename -uid "A7E0EA64-42F9-F6A2-10EC-51873C34E815";
	setAttr ".ihi" 0;
createNode groupId -n "groupId25";
	rename -uid "12F4B240-4153-0EFF-A0EE-3DBB1697661A";
	setAttr ".ihi" 0;
createNode groupId -n "groupId26";
	rename -uid "F0229252-4707-DE21-0688-0887B71CDBF7";
	setAttr ".ihi" 0;
createNode groupId -n "groupId27";
	rename -uid "5F9C9F1B-4F94-5A39-B844-149AC802E490";
	setAttr ".ihi" 0;
createNode lambert -n "green";
	rename -uid "2204986A-4DBE-0755-4CC0-EFA3E9D47A98";
	setAttr ".c" -type "float3" 0 1 0 ;
createNode shadingEngine -n "lambert3SG";
	rename -uid "21AA969C-4403-35FA-B640-B9BD6079E9EC";
	setAttr ".ihi" 0;
	setAttr -s 9 ".dsm";
	setAttr ".ro" yes;
	setAttr -s 9 ".gn";
createNode materialInfo -n "materialInfo2";
	rename -uid "99590594-4B4D-7781-3090-3A8346E3467B";
createNode groupId -n "groupId28";
	rename -uid "4D5A6025-4226-8DF6-66F1-EC83BC6D9EA4";
	setAttr ".ihi" 0;
createNode groupId -n "groupId29";
	rename -uid "0A52FF91-4765-78FD-C572-FE807A49A8C0";
	setAttr ".ihi" 0;
createNode groupId -n "groupId30";
	rename -uid "974F1A9F-4878-12C3-E13B-B2A6D9E95BFE";
	setAttr ".ihi" 0;
createNode groupId -n "groupId31";
	rename -uid "5DD91944-40F4-D9CA-1103-DD978007FEC2";
	setAttr ".ihi" 0;
createNode groupId -n "groupId32";
	rename -uid "A6CD24F2-4794-A329-CA5C-F78C50851AFB";
	setAttr ".ihi" 0;
createNode groupId -n "groupId33";
	rename -uid "9DFBBD20-4517-A974-3DD8-6697956F8454";
	setAttr ".ihi" 0;
createNode groupId -n "groupId34";
	rename -uid "5DFA7CEE-4922-9086-0C38-439BE7BE0946";
	setAttr ".ihi" 0;
createNode groupId -n "groupId35";
	rename -uid "C43FDAC5-4117-9F9A-408F-A9AC93868CA9";
	setAttr ".ihi" 0;
createNode groupId -n "groupId36";
	rename -uid "8F04E194-406E-A68A-AC9F-54B14C635AB2";
	setAttr ".ihi" 0;
createNode groupId -n "groupId37";
	rename -uid "B285F320-44F2-4414-17AD-8CAC9A672AFF";
	setAttr ".ihi" 0;
createNode groupId -n "groupId38";
	rename -uid "20740E7E-46CC-F57E-BD16-0181D60D0B72";
	setAttr ".ihi" 0;
createNode groupId -n "groupId39";
	rename -uid "1B405988-422B-7518-8ABF-DBB4CA52B6D7";
	setAttr ".ihi" 0;
createNode groupId -n "groupId40";
	rename -uid "209BC41F-48DD-A855-690A-A1BBF07D241F";
	setAttr ".ihi" 0;
createNode groupId -n "groupId41";
	rename -uid "081DBEB2-4A89-BF3D-9F39-949C9C601FBE";
	setAttr ".ihi" 0;
createNode groupId -n "groupId42";
	rename -uid "6C6B60AC-4DAD-11EA-9EB8-CDB8A1E80AF3";
	setAttr ".ihi" 0;
createNode groupId -n "groupId43";
	rename -uid "4E5A3DA7-4038-3B77-EDA1-D4B8F6E5BA27";
	setAttr ".ihi" 0;
createNode groupId -n "groupId44";
	rename -uid "4D418657-4633-9750-E8C2-DEB2D500198D";
	setAttr ".ihi" 0;
createNode groupId -n "groupId45";
	rename -uid "3B19F2C1-491B-30C5-0812-D0AF028F28DA";
	setAttr ".ihi" 0;
createNode groupId -n "groupId46";
	rename -uid "8E0A482D-4671-7609-1F88-54BEAB4D9926";
	setAttr ".ihi" 0;
createNode groupId -n "groupId47";
	rename -uid "D2274953-4ECF-60AC-1E6D-188CA0B327D8";
	setAttr ".ihi" 0;
createNode groupId -n "groupId48";
	rename -uid "B17867FB-47EA-0974-1067-6EAE0D27B42B";
	setAttr ".ihi" 0;
createNode lambert -n "white";
	rename -uid "13E6830A-4D0C-9552-061E-01B7ACB509F2";
	setAttr ".c" -type "float3" 1 1 1 ;
createNode shadingEngine -n "lambert4SG";
	rename -uid "6F0B51F7-41B1-BD4C-01C4-CCB192DC97E5";
	setAttr ".ihi" 0;
	setAttr -s 9 ".dsm";
	setAttr ".ro" yes;
	setAttr -s 9 ".gn";
createNode materialInfo -n "materialInfo3";
	rename -uid "FB07C522-4D3C-B8E6-F720-309E6358A89D";
createNode groupId -n "groupId49";
	rename -uid "0CFDE23B-46FE-5EEE-C515-30BBC185F73F";
	setAttr ".ihi" 0;
createNode groupId -n "groupId50";
	rename -uid "A27A1138-49A1-B60D-082F-30A7895AC6D9";
	setAttr ".ihi" 0;
createNode groupId -n "groupId51";
	rename -uid "58AF1A67-4FF3-C917-8267-FE95FCD6D485";
	setAttr ".ihi" 0;
createNode groupId -n "groupId52";
	rename -uid "0168C86D-4F4E-ABA5-EC55-84864720A8A9";
	setAttr ".ihi" 0;
createNode groupId -n "groupId53";
	rename -uid "11C06741-4FB6-3AEE-A1DD-59B3596D0765";
	setAttr ".ihi" 0;
createNode groupId -n "groupId54";
	rename -uid "E93513A2-442D-5D4A-1806-2EAF7F256430";
	setAttr ".ihi" 0;
createNode groupId -n "groupId55";
	rename -uid "2AC337C4-4ACB-E2B3-6039-F5BF387FFEB0";
	setAttr ".ihi" 0;
createNode groupId -n "groupId56";
	rename -uid "D68CC005-4AB7-001C-E9CD-8E8909AAEAE2";
	setAttr ".ihi" 0;
createNode groupId -n "groupId57";
	rename -uid "F0A03245-4AFB-80EE-DCDC-1C9461D94492";
	setAttr ".ihi" 0;
createNode groupId -n "groupId58";
	rename -uid "F661CFD8-4E95-0189-467E-48BDB870EB53";
	setAttr ".ihi" 0;
createNode groupId -n "groupId59";
	rename -uid "41ACCAE7-4007-C2E0-B1A0-3392B3406355";
	setAttr ".ihi" 0;
createNode groupId -n "groupId60";
	rename -uid "F34B0C4C-46FB-F871-B22E-89801114F583";
	setAttr ".ihi" 0;
createNode groupId -n "groupId61";
	rename -uid "9CDB3C53-4D98-8719-DBC3-17AAD3DD9411";
	setAttr ".ihi" 0;
createNode groupId -n "groupId62";
	rename -uid "9A179419-4034-6624-503F-32B890F7731E";
	setAttr ".ihi" 0;
createNode groupId -n "groupId63";
	rename -uid "9AB744A1-4365-DBAD-574F-7BBF3B90BF92";
	setAttr ".ihi" 0;
createNode groupId -n "groupId64";
	rename -uid "C4B21AF8-43A3-B3FD-91E0-6E91D1B0B453";
	setAttr ".ihi" 0;
createNode groupId -n "groupId65";
	rename -uid "84D32129-47AF-69A0-C159-7CAE04949CC9";
	setAttr ".ihi" 0;
createNode lambert -n "blue";
	rename -uid "FD567D72-4D1A-B558-CB5B-7C9DE52E56E6";
	setAttr ".c" -type "float3" 0 0 1 ;
createNode shadingEngine -n "lambert5SG";
	rename -uid "AFB8FFBF-42E1-DDA2-F4B5-60ACD82484AA";
	setAttr ".ihi" 0;
	setAttr -s 9 ".dsm";
	setAttr ".ro" yes;
	setAttr -s 9 ".gn";
createNode materialInfo -n "materialInfo4";
	rename -uid "74B7FA39-4176-9CF2-2832-3C8168D575FC";
createNode groupId -n "groupId66";
	rename -uid "7614CF19-436E-B3D3-C832-AE8C0BDD5566";
	setAttr ".ihi" 0;
createNode groupId -n "groupId67";
	rename -uid "44F61F14-4AFD-FB67-7565-D6A5A10C0219";
	setAttr ".ihi" 0;
createNode groupId -n "groupId68";
	rename -uid "A7F97B4B-456E-7CC1-4160-A7BE3CF1FFAC";
	setAttr ".ihi" 0;
createNode groupId -n "groupId69";
	rename -uid "D7A4292A-4992-76DC-D717-A9AE124DDA4B";
	setAttr ".ihi" 0;
createNode groupId -n "groupId70";
	rename -uid "BE975A83-4A25-58EB-A158-EBBF2940073C";
	setAttr ".ihi" 0;
createNode groupId -n "groupId71";
	rename -uid "3CA213F9-467B-0A56-C918-F8B9CD3392D6";
	setAttr ".ihi" 0;
createNode groupId -n "groupId72";
	rename -uid "D84B7C67-4A48-7A58-D583-9FA6A86AED78";
	setAttr ".ihi" 0;
createNode groupId -n "groupId73";
	rename -uid "476824EB-49A5-D8CC-D16A-B698FFA79D15";
	setAttr ".ihi" 0;
createNode groupId -n "groupId74";
	rename -uid "F3A267A4-4AA4-417D-7DF8-44AAC44C24BF";
	setAttr ".ihi" 0;
createNode groupId -n "groupId75";
	rename -uid "765CA842-4CA9-A12F-EE65-0981EEE4229A";
	setAttr ".ihi" 0;
createNode groupId -n "groupId76";
	rename -uid "180945EC-4E69-E17E-9AB3-76B5F370779C";
	setAttr ".ihi" 0;
createNode groupId -n "groupId77";
	rename -uid "22482F24-4719-3C86-2FDC-21933ACDEAD3";
	setAttr ".ihi" 0;
createNode groupId -n "groupId78";
	rename -uid "CE7DC604-493C-7E07-EE39-10BF02DE10C8";
	setAttr ".ihi" 0;
createNode groupId -n "groupId79";
	rename -uid "00B3A4CB-4AB2-3E90-B707-53AA50A6EEA9";
	setAttr ".ihi" 0;
createNode groupId -n "groupId80";
	rename -uid "64BC3E44-4EED-66C6-6DA6-F9BC8B744DC9";
	setAttr ".ihi" 0;
createNode groupId -n "groupId81";
	rename -uid "87B3DAC1-43F6-22DE-8F72-03BEEB3AEFD7";
	setAttr ".ihi" 0;
createNode groupId -n "groupId82";
	rename -uid "8C04E311-47F2-9B36-7586-7ABA4819390F";
	setAttr ".ihi" 0;
createNode lambert -n "yellow";
	rename -uid "EFC37064-4538-0A05-E443-11AB666F08F0";
	setAttr ".c" -type "float3" 1 1 0 ;
createNode shadingEngine -n "lambert6SG";
	rename -uid "BCF7B781-4B88-4765-94EE-848E1DFEF7B1";
	setAttr ".ihi" 0;
	setAttr -s 9 ".dsm";
	setAttr ".ro" yes;
	setAttr -s 9 ".gn";
createNode materialInfo -n "materialInfo5";
	rename -uid "B024327D-4732-0C18-3D70-1CAA2D060A15";
createNode groupId -n "groupId83";
	rename -uid "CF94D07A-40F5-94FA-CFAA-92B812035296";
	setAttr ".ihi" 0;
createNode groupId -n "groupId84";
	rename -uid "CB5C6A3A-41AC-F4F6-820C-A9B5E9D8C2C3";
	setAttr ".ihi" 0;
createNode groupId -n "groupId85";
	rename -uid "D83FFDE3-4DAB-6892-0F10-238E4227DBE6";
	setAttr ".ihi" 0;
createNode groupId -n "groupId86";
	rename -uid "B1E60064-4693-B960-7DF8-A49FD7B9C23C";
	setAttr ".ihi" 0;
createNode groupId -n "groupId87";
	rename -uid "74FBCBFE-4350-0177-E5DE-6A94C81DEF9A";
	setAttr ".ihi" 0;
createNode groupId -n "groupId88";
	rename -uid "3AA82E5A-4383-B62D-43C7-319BF3E1FDCD";
	setAttr ".ihi" 0;
createNode groupId -n "groupId89";
	rename -uid "BED7885F-47AD-B31F-44BB-43A2FCC6E028";
	setAttr ".ihi" 0;
createNode groupId -n "groupId90";
	rename -uid "BD4B0C64-4FEB-1920-056E-64AB7395F701";
	setAttr ".ihi" 0;
createNode groupId -n "groupId91";
	rename -uid "66BDB696-43FC-8462-AD06-7B93E00FADE9";
	setAttr ".ihi" 0;
createNode groupId -n "groupId92";
	rename -uid "40A78C05-439F-9E1F-3F48-0F91704E74BC";
	setAttr ".ihi" 0;
createNode groupId -n "groupId93";
	rename -uid "6B71E4FC-44C6-4255-913D-518DB20EE034";
	setAttr ".ihi" 0;
createNode groupId -n "groupId94";
	rename -uid "A576F9B4-4FC8-62DA-6F49-B68AF9478D5E";
	setAttr ".ihi" 0;
createNode groupId -n "groupId95";
	rename -uid "FE42AC13-4A4D-F8BB-A23D-D492BB46DB1D";
	setAttr ".ihi" 0;
createNode lambert -n "orange";
	rename -uid "06CD91EF-4306-BCAA-FC38-5A8996BF53B8";
	setAttr ".c" -type "float3" 1 0.333 0 ;
createNode shadingEngine -n "lambert7SG";
	rename -uid "A66EE7BA-41E4-0A47-FF62-01A99C152C3C";
	setAttr ".ihi" 0;
	setAttr -s 9 ".dsm";
	setAttr ".ro" yes;
	setAttr -s 9 ".gn";
createNode materialInfo -n "materialInfo6";
	rename -uid "B6EBE129-4AF3-65C6-5371-5DB533C55A84";
createNode groupId -n "groupId96";
	rename -uid "CC6D6AAF-488C-2176-2CB8-3EAC9862A9FD";
	setAttr ".ihi" 0;
createNode groupId -n "groupId97";
	rename -uid "5F2EDE5A-4854-05C2-12F2-249BE2AE811F";
	setAttr ".ihi" 0;
createNode groupId -n "groupId98";
	rename -uid "C2A18C77-4361-EAA7-C65C-6A9B7E1C1F45";
	setAttr ".ihi" 0;
createNode groupId -n "groupId99";
	rename -uid "63BE02F7-4DE4-D880-A66A-11896E0C7B32";
	setAttr ".ihi" 0;
createNode groupId -n "groupId100";
	rename -uid "072475DB-4E31-B4D5-9D46-E6926410DA89";
	setAttr ".ihi" 0;
createNode groupId -n "groupId101";
	rename -uid "946E125E-4990-4E47-3661-118E7A1656ED";
	setAttr ".ihi" 0;
createNode groupId -n "groupId102";
	rename -uid "98101C2D-4805-7B35-99CF-BD87E8A40335";
	setAttr ".ihi" 0;
createNode groupId -n "groupId103";
	rename -uid "5047D15E-4DEA-5421-F17E-A3BE975DC9DD";
	setAttr ".ihi" 0;
createNode groupId -n "groupId104";
	rename -uid "BCDCBF2D-4EC8-37D5-4998-2392E668E325";
	setAttr ".ihi" 0;
createNode groupId -n "groupId105";
	rename -uid "7085DF65-42D4-862E-AFE1-348454D74DD9";
	setAttr ".ihi" 0;
createNode groupId -n "groupId106";
	rename -uid "EFA9D139-4702-7A68-3195-248EEFB663CE";
	setAttr ".ihi" 0;
createNode script -n "uiConfigurationScriptNode";
	rename -uid "2E139323-4237-9810-E8DA-43B07C961F0D";
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
		+ "            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 1\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 32768\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n"
		+ "            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -controllers 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n"
		+ "            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 1749\n            -height 746\n            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"outlinerPanel\" (localizedPanelLabel(\"ToggledOutliner\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\toutlinerPanel -edit -l (localizedPanelLabel(\"ToggledOutliner\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\t$editorName = $panelName;\n        outlinerEditor -e \n            -showShapes 0\n            -showAssignedMaterials 0\n            -showTimeEditor 1\n            -showReferenceNodes 1\n            -showReferenceMembers 1\n            -showAttributes 0\n            -showConnected 0\n            -showAnimCurvesOnly 0\n            -showMuteInfo 0\n            -organizeByLayer 1\n            -organizeByClip 1\n            -showAnimLayerWeight 1\n            -autoExpandLayers 1\n            -autoExpand 0\n            -autoExpandAnimatedShapes 1\n            -showDagOnly 1\n            -showAssets 1\n            -showContainedOnly 1\n            -showPublishedAsConnected 0\n            -showParentContainers 0\n            -showContainerContents 1\n            -ignoreDagHierarchy 0\n            -expandConnections 0\n            -showUpstreamCurves 1\n            -showUnitlessCurves 1\n            -showCompounds 1\n            -showLeafs 1\n            -showNumericAttrsOnly 0\n            -highlightActive 1\n            -autoSelectNewObjects 0\n            -doNotSelectNewObjects 0\n"
		+ "            -dropIsParent 1\n            -transmitFilters 0\n            -setFilter \"defaultSetFilter\" \n            -showSetMembers 1\n            -allowMultiSelection 1\n            -alwaysToggleSelect 0\n            -directSelect 0\n            -isSet 0\n            -isSetMember 0\n            -displayMode \"DAG\" \n            -expandObjects 0\n            -setsIgnoreFilters 1\n            -containersIgnoreFilters 0\n            -editAttrName 0\n            -showAttrValues 0\n            -highlightSecondary 0\n            -showUVAttrsOnly 0\n            -showTextureNodesOnly 0\n            -attrAlphaOrder \"default\" \n            -animLayerFilterOptions \"allAffecting\" \n            -sortOrder \"none\" \n            -longNames 0\n            -niceNames 1\n            -showNamespace 1\n            -showPinIcons 0\n            -mapMotionTrails 0\n            -ignoreHiddenAttribute 0\n            -ignoreOutlinerColor 0\n            -renderFilterVisible 0\n            -renderFilterIndex 0\n            -selectionOrder \"chronological\" \n            -expandAttribute 0\n"
		+ "            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"outlinerPanel\" (localizedPanelLabel(\"Outliner\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\toutlinerPanel -edit -l (localizedPanelLabel(\"Outliner\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        outlinerEditor -e \n            -showShapes 0\n            -showAssignedMaterials 0\n            -showTimeEditor 1\n            -showReferenceNodes 0\n            -showReferenceMembers 0\n            -showAttributes 0\n            -showConnected 0\n            -showAnimCurvesOnly 0\n            -showMuteInfo 0\n            -organizeByLayer 1\n            -organizeByClip 1\n            -showAnimLayerWeight 1\n            -autoExpandLayers 1\n            -autoExpand 0\n            -autoExpandAnimatedShapes 1\n            -showDagOnly 1\n            -showAssets 1\n            -showContainedOnly 1\n            -showPublishedAsConnected 0\n            -showParentContainers 0\n"
		+ "            -showContainerContents 1\n            -ignoreDagHierarchy 0\n            -expandConnections 0\n            -showUpstreamCurves 1\n            -showUnitlessCurves 1\n            -showCompounds 1\n            -showLeafs 1\n            -showNumericAttrsOnly 0\n            -highlightActive 1\n            -autoSelectNewObjects 0\n            -doNotSelectNewObjects 0\n            -dropIsParent 1\n            -transmitFilters 0\n            -setFilter \"0\" \n            -showSetMembers 1\n            -allowMultiSelection 1\n            -alwaysToggleSelect 0\n            -directSelect 0\n            -displayMode \"DAG\" \n            -expandObjects 0\n            -setsIgnoreFilters 1\n            -containersIgnoreFilters 0\n            -editAttrName 0\n            -showAttrValues 0\n            -highlightSecondary 0\n            -showUVAttrsOnly 0\n            -showTextureNodesOnly 0\n            -attrAlphaOrder \"default\" \n            -animLayerFilterOptions \"allAffecting\" \n            -sortOrder \"none\" \n            -longNames 0\n            -niceNames 1\n"
		+ "            -showNamespace 1\n            -showPinIcons 0\n            -mapMotionTrails 0\n            -ignoreHiddenAttribute 0\n            -ignoreOutlinerColor 0\n            -renderFilterVisible 0\n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"graphEditor\" (localizedPanelLabel(\"Graph Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Graph Editor\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"OutlineEd\");\n            outlinerEditor -e \n                -showShapes 1\n                -showAssignedMaterials 0\n                -showTimeEditor 1\n                -showReferenceNodes 0\n                -showReferenceMembers 0\n                -showAttributes 1\n                -showConnected 1\n                -showAnimCurvesOnly 1\n                -showMuteInfo 0\n                -organizeByLayer 1\n                -organizeByClip 1\n"
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
		+ "\t\t\t\t\t\"$panelName = `modelPanel -unParent -l (localizedPanelLabel(\\\"Persp View\\\")) -mbv $menusOkayInPanels `;\\n$editorName = $panelName;\\nmodelEditor -e \\n    -cam `findStartUpCamera persp` \\n    -useInteractiveMode 0\\n    -displayLights \\\"default\\\" \\n    -displayAppearance \\\"smoothShaded\\\" \\n    -activeOnly 0\\n    -ignorePanZoom 0\\n    -wireframeOnShaded 0\\n    -headsUpDisplay 1\\n    -holdOuts 1\\n    -selectionHiliteDisplay 1\\n    -useDefaultMaterial 0\\n    -bufferMode \\\"double\\\" \\n    -twoSidedLighting 0\\n    -backfaceCulling 0\\n    -xray 0\\n    -jointXray 1\\n    -activeComponentsXray 0\\n    -displayTextures 0\\n    -smoothWireframe 0\\n    -lineWidth 1\\n    -textureAnisotropic 0\\n    -textureHilight 1\\n    -textureSampling 2\\n    -textureDisplay \\\"modulate\\\" \\n    -textureMaxSize 32768\\n    -fogging 0\\n    -fogSource \\\"fragment\\\" \\n    -fogMode \\\"linear\\\" \\n    -fogStart 0\\n    -fogEnd 100\\n    -fogDensity 0.1\\n    -fogColor 0.5 0.5 0.5 1 \\n    -depthOfFieldPreview 1\\n    -maxConstantTransparency 1\\n    -rendererName \\\"vp2Renderer\\\" \\n    -objectFilterShowInHUD 1\\n    -isFiltered 0\\n    -colorResolution 256 256 \\n    -bumpResolution 512 512 \\n    -textureCompression 0\\n    -transparencyAlgorithm \\\"frontAndBackCull\\\" \\n    -transpInShadows 0\\n    -cullingOverride \\\"none\\\" \\n    -lowQualityLighting 0\\n    -maximumNumHardwareLights 1\\n    -occlusionCulling 0\\n    -shadingModel 0\\n    -useBaseRenderer 0\\n    -useReducedRenderer 0\\n    -smallObjectCulling 0\\n    -smallObjectThreshold -1 \\n    -interactiveDisableShadows 0\\n    -interactiveBackFaceCull 0\\n    -sortTransparent 1\\n    -controllers 1\\n    -nurbsCurves 1\\n    -nurbsSurfaces 1\\n    -polymeshes 1\\n    -subdivSurfaces 1\\n    -planes 1\\n    -lights 1\\n    -cameras 1\\n    -controlVertices 1\\n    -hulls 1\\n    -grid 1\\n    -imagePlane 1\\n    -joints 1\\n    -ikHandles 1\\n    -deformers 1\\n    -dynamics 1\\n    -particleInstancers 1\\n    -fluids 1\\n    -hairSystems 1\\n    -follicles 1\\n    -nCloths 1\\n    -nParticles 1\\n    -nRigids 1\\n    -dynamicConstraints 1\\n    -locators 1\\n    -manipulators 1\\n    -pluginShapes 1\\n    -dimensions 1\\n    -handles 1\\n    -pivots 1\\n    -textures 1\\n    -strokes 1\\n    -motionTrails 1\\n    -clipGhosts 1\\n    -greasePencils 1\\n    -shadows 0\\n    -captureSequenceNumber -1\\n    -width 1749\\n    -height 746\\n    -sceneRenderFilter 0\\n    $editorName;\\nmodelEditor -e -viewSelected 0 $editorName;\\nmodelEditor -e \\n    -pluginObjects \\\"gpuCacheDisplayFilter\\\" 1 \\n    $editorName\"\n"
		+ "\t\t\t\t\t\"modelPanel -edit -l (localizedPanelLabel(\\\"Persp View\\\")) -mbv $menusOkayInPanels  $panelName;\\n$editorName = $panelName;\\nmodelEditor -e \\n    -cam `findStartUpCamera persp` \\n    -useInteractiveMode 0\\n    -displayLights \\\"default\\\" \\n    -displayAppearance \\\"smoothShaded\\\" \\n    -activeOnly 0\\n    -ignorePanZoom 0\\n    -wireframeOnShaded 0\\n    -headsUpDisplay 1\\n    -holdOuts 1\\n    -selectionHiliteDisplay 1\\n    -useDefaultMaterial 0\\n    -bufferMode \\\"double\\\" \\n    -twoSidedLighting 0\\n    -backfaceCulling 0\\n    -xray 0\\n    -jointXray 1\\n    -activeComponentsXray 0\\n    -displayTextures 0\\n    -smoothWireframe 0\\n    -lineWidth 1\\n    -textureAnisotropic 0\\n    -textureHilight 1\\n    -textureSampling 2\\n    -textureDisplay \\\"modulate\\\" \\n    -textureMaxSize 32768\\n    -fogging 0\\n    -fogSource \\\"fragment\\\" \\n    -fogMode \\\"linear\\\" \\n    -fogStart 0\\n    -fogEnd 100\\n    -fogDensity 0.1\\n    -fogColor 0.5 0.5 0.5 1 \\n    -depthOfFieldPreview 1\\n    -maxConstantTransparency 1\\n    -rendererName \\\"vp2Renderer\\\" \\n    -objectFilterShowInHUD 1\\n    -isFiltered 0\\n    -colorResolution 256 256 \\n    -bumpResolution 512 512 \\n    -textureCompression 0\\n    -transparencyAlgorithm \\\"frontAndBackCull\\\" \\n    -transpInShadows 0\\n    -cullingOverride \\\"none\\\" \\n    -lowQualityLighting 0\\n    -maximumNumHardwareLights 1\\n    -occlusionCulling 0\\n    -shadingModel 0\\n    -useBaseRenderer 0\\n    -useReducedRenderer 0\\n    -smallObjectCulling 0\\n    -smallObjectThreshold -1 \\n    -interactiveDisableShadows 0\\n    -interactiveBackFaceCull 0\\n    -sortTransparent 1\\n    -controllers 1\\n    -nurbsCurves 1\\n    -nurbsSurfaces 1\\n    -polymeshes 1\\n    -subdivSurfaces 1\\n    -planes 1\\n    -lights 1\\n    -cameras 1\\n    -controlVertices 1\\n    -hulls 1\\n    -grid 1\\n    -imagePlane 1\\n    -joints 1\\n    -ikHandles 1\\n    -deformers 1\\n    -dynamics 1\\n    -particleInstancers 1\\n    -fluids 1\\n    -hairSystems 1\\n    -follicles 1\\n    -nCloths 1\\n    -nParticles 1\\n    -nRigids 1\\n    -dynamicConstraints 1\\n    -locators 1\\n    -manipulators 1\\n    -pluginShapes 1\\n    -dimensions 1\\n    -handles 1\\n    -pivots 1\\n    -textures 1\\n    -strokes 1\\n    -motionTrails 1\\n    -clipGhosts 1\\n    -greasePencils 1\\n    -shadows 0\\n    -captureSequenceNumber -1\\n    -width 1749\\n    -height 746\\n    -sceneRenderFilter 0\\n    $editorName;\\nmodelEditor -e -viewSelected 0 $editorName;\\nmodelEditor -e \\n    -pluginObjects \\\"gpuCacheDisplayFilter\\\" 1 \\n    $editorName\"\n"
		+ "\t\t\t\t$configName;\n\n            setNamedPanelLayout (localizedPanelLabel(\"Current Layout\"));\n        }\n\n        panelHistory -e -clear mainPanelHistory;\n        sceneUIReplacement -clear;\n\t}\n\n\ngrid -spacing 5 -size 12 -divisions 5 -displayAxes yes -displayGridLines yes -displayDivisionLines yes -displayPerspectiveLabels no -displayOrthographicLabels no -displayAxesBold yes -perspectiveLabelPosition axis -orthographicLabelPosition edge;\nviewManip -drawCompass 0 -compassAngle 0 -frontParameters \"\" -homeParameters \"\" -selectionLockParameters \"\";\n}\n");
	setAttr ".st" 3;
createNode script -n "sceneConfigurationScriptNode";
	rename -uid "2DA790BD-4A6C-685B-22F7-ECB421E47F60";
	setAttr ".b" -type "string" "playbackOptions -min 1 -max 120 -ast 1 -aet 200 ";
	setAttr ".st" 6;
createNode nodeGraphEditorInfo -n "MayaNodeEditorSavedTabsInfo";
	rename -uid "5FCB7EB1-4F4F-FDD8-32BD-02B7FE105689";
	setAttr -s 2 ".tgi";
	setAttr ".tgi[0].tn" -type "string" "old matrix";
	setAttr ".tgi[0].vl" -type "double2" -550.47881837568514 -567.97863122752767 ;
	setAttr ".tgi[0].vh" -type "double2" 1311.578095564322 890.45924214894728 ;
	setAttr -s 10 ".tgi[0].ni";
	setAttr ".tgi[0].ni[0].x" 565.87469482421875;
	setAttr ".tgi[0].ni[0].y" 243.25993347167969;
	setAttr ".tgi[0].ni[0].nvs" 1923;
	setAttr ".tgi[0].ni[1].x" 1095.9169921875;
	setAttr ".tgi[0].ni[1].y" 55.638324737548828;
	setAttr ".tgi[0].ni[1].nvs" 18306;
	setAttr ".tgi[0].ni[2].x" -378.69915771484375;
	setAttr ".tgi[0].ni[2].y" 451.5040283203125;
	setAttr ".tgi[0].ni[2].nvs" 18306;
	setAttr ".tgi[0].ni[3].x" 1356.1805419921875;
	setAttr ".tgi[0].ni[3].y" 225.97889709472656;
	setAttr ".tgi[0].ni[3].nvs" 18306;
	setAttr ".tgi[0].ni[4].x" 776.5501708984375;
	setAttr ".tgi[0].ni[4].y" 716.408935546875;
	setAttr ".tgi[0].ni[4].nvs" 18306;
	setAttr ".tgi[0].ni[5].x" 558.62835693359375;
	setAttr ".tgi[0].ni[5].y" -127.37457275390625;
	setAttr ".tgi[0].ni[5].nvs" 18306;
	setAttr ".tgi[0].ni[6].x" 391.767578125;
	setAttr ".tgi[0].ni[6].y" 672.245361328125;
	setAttr ".tgi[0].ni[6].nvs" 1923;
	setAttr ".tgi[0].ni[7].x" 262.18759155273438;
	setAttr ".tgi[0].ni[7].y" 345.61572265625;
	setAttr ".tgi[0].ni[7].nvs" 18306;
	setAttr ".tgi[0].ni[8].x" -69.357086181640625;
	setAttr ".tgi[0].ni[8].y" 170.76194763183594;
	setAttr ".tgi[0].ni[8].nvs" 18306;
	setAttr ".tgi[0].ni[9].x" -87.01080322265625;
	setAttr ".tgi[0].ni[9].y" 724.451171875;
	setAttr ".tgi[0].ni[9].nvs" 18306;
	setAttr ".tgi[1].tn" -type "string" "Untitled_1";
	setAttr ".tgi[1].vl" -type "double2" -1569.4625034945557 -934.24487653964991 ;
	setAttr ".tgi[1].vh" -type "double2" 1636.0881105073227 698.83500559365984 ;
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
	setAttr -s 8 ".st";
select -ne :renderGlobalsList1;
select -ne :defaultShaderList1;
	setAttr -s 11 ".s";
select -ne :postProcessList1;
	setAttr -s 2 ".p";
select -ne :defaultRenderUtilityList1;
select -ne :defaultRenderingList1;
select -ne :lambert1;
	setAttr ".c" -type "float3" 1 1 1 ;
select -ne :initialShadingGroup;
	setAttr -s 53 ".dsm";
	setAttr ".ro" yes;
	setAttr -s 52 ".gn";
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
connectAttr "mama.or" "l.r";
connectAttr "mama.os" "l.s";
connectAttr "mama.ot" "l.t";
connectAttr "mama1.ot" "gg.t";
connectAttr "mama1.or" "gg.r";
connectAttr "groupId96.id" "rbgShape1.iog.og[0].gid";
connectAttr ":initialShadingGroup.mwc" "rbgShape1.iog.og[0].gco";
connectAttr "groupId102.id" "rbgShape1.iog.og[1].gid";
connectAttr "lambert7SG.mwc" "rbgShape1.iog.og[1].gco";
connectAttr "groupId97.id" "rbgShape1.ciog.cog[0].cgid";
connectAttr "groupId51.id" "rbgShape2.iog.og[0].gid";
connectAttr ":initialShadingGroup.mwc" "rbgShape2.iog.og[0].gco";
connectAttr "groupId58.id" "rbgShape2.iog.og[1].gid";
connectAttr "lambert4SG.mwc" "rbgShape2.iog.og[1].gco";
connectAttr "groupId98.id" "rbgShape2.iog.og[2].gid";
connectAttr "lambert7SG.mwc" "rbgShape2.iog.og[2].gco";
connectAttr "groupId52.id" "rbgShape2.ciog.cog[0].cgid";
connectAttr "groupId83.id" "rbgShape3.iog.og[0].gid";
connectAttr ":initialShadingGroup.mwc" "rbgShape3.iog.og[0].gco";
connectAttr "groupId88.id" "rbgShape3.iog.og[1].gid";
connectAttr "lambert6SG.mwc" "rbgShape3.iog.og[1].gco";
connectAttr "groupId103.id" "rbgShape3.iog.og[2].gid";
connectAttr "lambert7SG.mwc" "rbgShape3.iog.og[2].gco";
connectAttr "groupId84.id" "rbgShape3.ciog.cog[0].cgid";
connectAttr "groupId1.id" "rbgShape4.iog.og[0].gid";
connectAttr ":initialShadingGroup.mwc" "rbgShape4.iog.og[0].gco";
connectAttr "groupId19.id" "rbgShape4.iog.og[1].gid";
connectAttr "lambert2SG.mwc" "rbgShape4.iog.og[1].gco";
connectAttr "groupId87.id" "rbgShape4.iog.og[2].gid";
connectAttr "lambert6SG.mwc" "rbgShape4.iog.og[2].gco";
connectAttr "groupId100.id" "rbgShape4.iog.og[3].gid";
connectAttr "lambert7SG.mwc" "rbgShape4.iog.og[3].gco";
connectAttr "groupId2.id" "rbgShape4.ciog.cog[0].cgid";
connectAttr "groupId3.id" "rbgShape5.iog.og[0].gid";
connectAttr ":initialShadingGroup.mwc" "rbgShape5.iog.og[0].gco";
connectAttr "groupId20.id" "rbgShape5.iog.og[1].gid";
connectAttr "lambert2SG.mwc" "rbgShape5.iog.og[1].gco";
connectAttr "groupId101.id" "rbgShape5.iog.og[2].gid";
connectAttr "lambert7SG.mwc" "rbgShape5.iog.og[2].gco";
connectAttr "groupId4.id" "rbgShape5.ciog.cog[0].cgid";
connectAttr "groupId5.id" "rbgShape6.iog.og[0].gid";
connectAttr ":initialShadingGroup.mwc" "rbgShape6.iog.og[0].gco";
connectAttr "groupId21.id" "rbgShape6.iog.og[1].gid";
connectAttr "lambert2SG.mwc" "rbgShape6.iog.og[1].gco";
connectAttr "groupId59.id" "rbgShape6.iog.og[2].gid";
connectAttr "lambert4SG.mwc" "rbgShape6.iog.og[2].gco";
connectAttr "groupId99.id" "rbgShape6.iog.og[3].gid";
connectAttr "lambert7SG.mwc" "rbgShape6.iog.og[3].gco";
connectAttr "groupId6.id" "rbgShape6.ciog.cog[0].cgid";
connectAttr "groupId68.id" "rbgShape7.iog.og[0].gid";
connectAttr ":initialShadingGroup.mwc" "rbgShape7.iog.og[0].gco";
connectAttr "groupId76.id" "rbgShape7.iog.og[1].gid";
connectAttr "lambert5SG.mwc" "rbgShape7.iog.og[1].gco";
connectAttr "groupId89.id" "rbgShape7.iog.og[2].gid";
connectAttr "lambert6SG.mwc" "rbgShape7.iog.og[2].gco";
connectAttr "groupId104.id" "rbgShape7.iog.og[3].gid";
connectAttr "lambert7SG.mwc" "rbgShape7.iog.og[3].gco";
connectAttr "groupId69.id" "rbgShape7.ciog.cog[0].cgid";
connectAttr "groupId70.id" "rbgShape8.iog.og[0].gid";
connectAttr ":initialShadingGroup.mwc" "rbgShape8.iog.og[0].gco";
connectAttr "groupId77.id" "rbgShape8.iog.og[1].gid";
connectAttr "lambert5SG.mwc" "rbgShape8.iog.og[1].gco";
connectAttr "groupId105.id" "rbgShape8.iog.og[2].gid";
connectAttr "lambert7SG.mwc" "rbgShape8.iog.og[2].gco";
connectAttr "groupId71.id" "rbgShape8.ciog.cog[0].cgid";
connectAttr "groupId49.id" "rbgShape9.iog.og[0].gid";
connectAttr ":initialShadingGroup.mwc" "rbgShape9.iog.og[0].gco";
connectAttr "groupId57.id" "rbgShape9.iog.og[1].gid";
connectAttr "lambert4SG.mwc" "rbgShape9.iog.og[1].gco";
connectAttr "groupId82.id" "rbgShape9.iog.og[2].gid";
connectAttr "lambert5SG.mwc" "rbgShape9.iog.og[2].gco";
connectAttr "groupId106.id" "rbgShape9.iog.og[3].gid";
connectAttr "lambert7SG.mwc" "rbgShape9.iog.og[3].gco";
connectAttr "groupId50.id" "rbgShape9.ciog.cog[0].cgid";
connectAttr "groupId55.id" "rbgShape10.iog.og[0].gid";
connectAttr ":initialShadingGroup.mwc" "rbgShape10.iog.og[0].gco";
connectAttr "groupId62.id" "rbgShape10.iog.og[1].gid";
connectAttr "lambert4SG.mwc" "rbgShape10.iog.og[1].gco";
connectAttr "groupId81.id" "rbgShape10.iog.og[2].gid";
connectAttr "lambert5SG.mwc" "rbgShape10.iog.og[2].gco";
connectAttr "groupId56.id" "rbgShape10.ciog.cog[0].cgid";
connectAttr "groupId72.id" "rbgShape11.iog.og[0].gid";
connectAttr ":initialShadingGroup.mwc" "rbgShape11.iog.og[0].gco";
connectAttr "groupId78.id" "rbgShape11.iog.og[1].gid";
connectAttr "lambert5SG.mwc" "rbgShape11.iog.og[1].gco";
connectAttr "groupId73.id" "rbgShape11.ciog.cog[0].cgid";
connectAttr "groupId66.id" "rbgShape12.iog.og[0].gid";
connectAttr ":initialShadingGroup.mwc" "rbgShape12.iog.og[0].gco";
connectAttr "groupId75.id" "rbgShape12.iog.og[1].gid";
connectAttr "lambert5SG.mwc" "rbgShape12.iog.og[1].gco";
connectAttr "groupId90.id" "rbgShape12.iog.og[2].gid";
connectAttr "lambert6SG.mwc" "rbgShape12.iog.og[2].gco";
connectAttr "groupId67.id" "rbgShape12.ciog.cog[0].cgid";
connectAttr "groupId7.id" "rbgShape13.iog.og[0].gid";
connectAttr ":initialShadingGroup.mwc" "rbgShape13.iog.og[0].gco";
connectAttr "groupId22.id" "rbgShape13.iog.og[1].gid";
connectAttr "lambert2SG.mwc" "rbgShape13.iog.og[1].gco";
connectAttr "groupId60.id" "rbgShape13.iog.og[2].gid";
connectAttr "lambert4SG.mwc" "rbgShape13.iog.og[2].gco";
connectAttr "groupId8.id" "rbgShape13.ciog.cog[0].cgid";
connectAttr "groupId9.id" "rbgShape14.iog.og[0].gid";
connectAttr ":initialShadingGroup.mwc" "rbgShape14.iog.og[0].gco";
connectAttr "groupId23.id" "rbgShape14.iog.og[1].gid";
connectAttr "lambert2SG.mwc" "rbgShape14.iog.og[1].gco";
connectAttr "groupId10.id" "rbgShape14.ciog.cog[0].cgid";
connectAttr "groupId11.id" "rbgShape15.iog.og[0].gid";
connectAttr ":initialShadingGroup.mwc" "rbgShape15.iog.og[0].gco";
connectAttr "groupId24.id" "rbgShape15.iog.og[1].gid";
connectAttr "lambert2SG.mwc" "rbgShape15.iog.og[1].gco";
connectAttr "groupId92.id" "rbgShape15.iog.og[2].gid";
connectAttr "lambert6SG.mwc" "rbgShape15.iog.og[2].gco";
connectAttr "groupId12.id" "rbgShape15.ciog.cog[0].cgid";
connectAttr "groupId85.id" "rbgShape16.iog.og[0].gid";
connectAttr ":initialShadingGroup.mwc" "rbgShape16.iog.og[0].gco";
connectAttr "groupId91.id" "rbgShape16.iog.og[1].gid";
connectAttr "lambert6SG.mwc" "rbgShape16.iog.og[1].gco";
connectAttr "groupId86.id" "rbgShape16.ciog.cog[0].cgid";
connectAttr "groupId53.id" "rbgShape17.iog.og[0].gid";
connectAttr ":initialShadingGroup.mwc" "rbgShape17.iog.og[0].gco";
connectAttr "groupId61.id" "rbgShape17.iog.og[1].gid";
connectAttr "lambert4SG.mwc" "rbgShape17.iog.og[1].gco";
connectAttr "groupId54.id" "rbgShape17.ciog.cog[0].cgid";
connectAttr "groupId28.id" "rbgShape18.iog.og[0].gid";
connectAttr ":initialShadingGroup.mwc" "rbgShape18.iog.og[0].gco";
connectAttr "groupId40.id" "rbgShape18.iog.og[1].gid";
connectAttr "lambert3SG.mwc" "rbgShape18.iog.og[1].gco";
connectAttr "groupId63.id" "rbgShape18.iog.og[2].gid";
connectAttr "lambert4SG.mwc" "rbgShape18.iog.og[2].gco";
connectAttr "groupId80.id" "rbgShape18.iog.og[3].gid";
connectAttr "lambert5SG.mwc" "rbgShape18.iog.og[3].gco";
connectAttr "groupId29.id" "rbgShape18.ciog.cog[0].cgid";
connectAttr "groupId34.id" "rbgShape19.iog.og[0].gid";
connectAttr ":initialShadingGroup.mwc" "rbgShape19.iog.og[0].gco";
connectAttr "groupId45.id" "rbgShape19.iog.og[1].gid";
connectAttr "lambert3SG.mwc" "rbgShape19.iog.og[1].gco";
connectAttr "groupId79.id" "rbgShape19.iog.og[2].gid";
connectAttr "lambert5SG.mwc" "rbgShape19.iog.og[2].gco";
connectAttr "groupId35.id" "rbgShape19.ciog.cog[0].cgid";
connectAttr "groupId36.id" "rbgShape20.iog.og[0].gid";
connectAttr ":initialShadingGroup.mwc" "rbgShape20.iog.og[0].gco";
connectAttr "groupId46.id" "rbgShape20.iog.og[1].gid";
connectAttr "lambert3SG.mwc" "rbgShape20.iog.og[1].gco";
connectAttr "groupId74.id" "rbgShape20.iog.og[2].gid";
connectAttr "lambert5SG.mwc" "rbgShape20.iog.og[2].gco";
connectAttr "groupId95.id" "rbgShape20.iog.og[3].gid";
connectAttr "lambert6SG.mwc" "rbgShape20.iog.og[3].gco";
connectAttr "groupId37.id" "rbgShape20.ciog.cog[0].cgid";
connectAttr "groupId17.id" "rbgShape21.iog.og[0].gid";
connectAttr ":initialShadingGroup.mwc" "rbgShape21.iog.og[0].gco";
connectAttr "groupId27.id" "rbgShape21.iog.og[1].gid";
connectAttr "lambert2SG.mwc" "rbgShape21.iog.og[1].gco";
connectAttr "groupId42.id" "rbgShape21.iog.og[2].gid";
connectAttr "lambert3SG.mwc" "rbgShape21.iog.og[2].gco";
connectAttr "groupId65.id" "rbgShape21.iog.og[3].gid";
connectAttr "lambert4SG.mwc" "rbgShape21.iog.og[3].gco";
connectAttr "groupId18.id" "rbgShape21.ciog.cog[0].cgid";
connectAttr "groupId15.id" "rbgShape22.iog.og[0].gid";
connectAttr ":initialShadingGroup.mwc" "rbgShape22.iog.og[0].gco";
connectAttr "groupId26.id" "rbgShape22.iog.og[1].gid";
connectAttr "lambert2SG.mwc" "rbgShape22.iog.og[1].gco";
connectAttr "groupId43.id" "rbgShape22.iog.og[2].gid";
connectAttr "lambert3SG.mwc" "rbgShape22.iog.og[2].gco";
connectAttr "groupId16.id" "rbgShape22.ciog.cog[0].cgid";
connectAttr "groupId13.id" "rbgShape23.iog.og[0].gid";
connectAttr ":initialShadingGroup.mwc" "rbgShape23.iog.og[0].gco";
connectAttr "groupId25.id" "rbgShape23.iog.og[1].gid";
connectAttr "lambert2SG.mwc" "rbgShape23.iog.og[1].gco";
connectAttr "groupId48.id" "rbgShape23.iog.og[2].gid";
connectAttr "lambert3SG.mwc" "rbgShape23.iog.og[2].gco";
connectAttr "groupId93.id" "rbgShape23.iog.og[3].gid";
connectAttr "lambert6SG.mwc" "rbgShape23.iog.og[3].gco";
connectAttr "groupId14.id" "rbgShape23.ciog.cog[0].cgid";
connectAttr "groupId38.id" "rbgShape24.iog.og[0].gid";
connectAttr ":initialShadingGroup.mwc" "rbgShape24.iog.og[0].gco";
connectAttr "groupId47.id" "rbgShape24.iog.og[1].gid";
connectAttr "lambert3SG.mwc" "rbgShape24.iog.og[1].gco";
connectAttr "groupId94.id" "rbgShape24.iog.og[2].gid";
connectAttr "lambert6SG.mwc" "rbgShape24.iog.og[2].gco";
connectAttr "groupId39.id" "rbgShape24.ciog.cog[0].cgid";
connectAttr "groupId32.id" "rbgShape25.iog.og[0].gid";
connectAttr ":initialShadingGroup.mwc" "rbgShape25.iog.og[0].gco";
connectAttr "groupId44.id" "rbgShape25.iog.og[1].gid";
connectAttr "lambert3SG.mwc" "rbgShape25.iog.og[1].gco";
connectAttr "groupId33.id" "rbgShape25.ciog.cog[0].cgid";
connectAttr "groupId30.id" "rbgShape26.iog.og[0].gid";
connectAttr ":initialShadingGroup.mwc" "rbgShape26.iog.og[0].gco";
connectAttr "groupId41.id" "rbgShape26.iog.og[1].gid";
connectAttr "lambert3SG.mwc" "rbgShape26.iog.og[1].gco";
connectAttr "groupId64.id" "rbgShape26.iog.og[2].gid";
connectAttr "lambert4SG.mwc" "rbgShape26.iog.og[2].gco";
connectAttr "groupId31.id" "rbgShape26.ciog.cog[0].cgid";
relationship "link" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "lambert2SG.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "lambert3SG.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "lambert4SG.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "lambert5SG.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "lambert6SG.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "lambert7SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "lambert2SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "lambert3SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "lambert4SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "lambert5SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "lambert6SG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "lambert7SG.message" ":defaultLightSet.message";
connectAttr "layerManager.dli[0]" "defaultLayer.id";
connectAttr "renderLayerManager.rlmi[0]" "defaultRenderLayer.rlid";
connectAttr "tc.wim" "mamamama.i[0]";
connectAttr "tc1.m" "mamamama.i[1]";
connectAttr "tc.wm" "mamamama.i[2]";
connectAttr "tc.wim" "mama.imat";
connectAttr "mamamama.o" "mama1.imat";
connectAttr "red.oc" "lambert2SG.ss";
connectAttr "groupId19.msg" "lambert2SG.gn" -na;
connectAttr "groupId20.msg" "lambert2SG.gn" -na;
connectAttr "groupId21.msg" "lambert2SG.gn" -na;
connectAttr "groupId22.msg" "lambert2SG.gn" -na;
connectAttr "groupId23.msg" "lambert2SG.gn" -na;
connectAttr "groupId24.msg" "lambert2SG.gn" -na;
connectAttr "groupId25.msg" "lambert2SG.gn" -na;
connectAttr "groupId26.msg" "lambert2SG.gn" -na;
connectAttr "groupId27.msg" "lambert2SG.gn" -na;
connectAttr "rbgShape4.iog.og[1]" "lambert2SG.dsm" -na;
connectAttr "rbgShape5.iog.og[1]" "lambert2SG.dsm" -na;
connectAttr "rbgShape6.iog.og[1]" "lambert2SG.dsm" -na;
connectAttr "rbgShape13.iog.og[1]" "lambert2SG.dsm" -na;
connectAttr "rbgShape14.iog.og[1]" "lambert2SG.dsm" -na;
connectAttr "rbgShape15.iog.og[1]" "lambert2SG.dsm" -na;
connectAttr "rbgShape23.iog.og[1]" "lambert2SG.dsm" -na;
connectAttr "rbgShape22.iog.og[1]" "lambert2SG.dsm" -na;
connectAttr "rbgShape21.iog.og[1]" "lambert2SG.dsm" -na;
connectAttr "lambert2SG.msg" "materialInfo1.sg";
connectAttr "red.msg" "materialInfo1.m";
connectAttr "green.oc" "lambert3SG.ss";
connectAttr "groupId40.msg" "lambert3SG.gn" -na;
connectAttr "groupId41.msg" "lambert3SG.gn" -na;
connectAttr "groupId42.msg" "lambert3SG.gn" -na;
connectAttr "groupId43.msg" "lambert3SG.gn" -na;
connectAttr "groupId44.msg" "lambert3SG.gn" -na;
connectAttr "groupId45.msg" "lambert3SG.gn" -na;
connectAttr "groupId46.msg" "lambert3SG.gn" -na;
connectAttr "groupId47.msg" "lambert3SG.gn" -na;
connectAttr "groupId48.msg" "lambert3SG.gn" -na;
connectAttr "rbgShape18.iog.og[1]" "lambert3SG.dsm" -na;
connectAttr "rbgShape26.iog.og[1]" "lambert3SG.dsm" -na;
connectAttr "rbgShape21.iog.og[2]" "lambert3SG.dsm" -na;
connectAttr "rbgShape22.iog.og[2]" "lambert3SG.dsm" -na;
connectAttr "rbgShape25.iog.og[1]" "lambert3SG.dsm" -na;
connectAttr "rbgShape19.iog.og[1]" "lambert3SG.dsm" -na;
connectAttr "rbgShape20.iog.og[1]" "lambert3SG.dsm" -na;
connectAttr "rbgShape24.iog.og[1]" "lambert3SG.dsm" -na;
connectAttr "rbgShape23.iog.og[2]" "lambert3SG.dsm" -na;
connectAttr "lambert3SG.msg" "materialInfo2.sg";
connectAttr "green.msg" "materialInfo2.m";
connectAttr "white.oc" "lambert4SG.ss";
connectAttr "groupId57.msg" "lambert4SG.gn" -na;
connectAttr "groupId58.msg" "lambert4SG.gn" -na;
connectAttr "groupId59.msg" "lambert4SG.gn" -na;
connectAttr "groupId60.msg" "lambert4SG.gn" -na;
connectAttr "groupId61.msg" "lambert4SG.gn" -na;
connectAttr "groupId62.msg" "lambert4SG.gn" -na;
connectAttr "groupId63.msg" "lambert4SG.gn" -na;
connectAttr "groupId64.msg" "lambert4SG.gn" -na;
connectAttr "groupId65.msg" "lambert4SG.gn" -na;
connectAttr "rbgShape9.iog.og[1]" "lambert4SG.dsm" -na;
connectAttr "rbgShape2.iog.og[1]" "lambert4SG.dsm" -na;
connectAttr "rbgShape6.iog.og[2]" "lambert4SG.dsm" -na;
connectAttr "rbgShape13.iog.og[2]" "lambert4SG.dsm" -na;
connectAttr "rbgShape17.iog.og[1]" "lambert4SG.dsm" -na;
connectAttr "rbgShape10.iog.og[1]" "lambert4SG.dsm" -na;
connectAttr "rbgShape18.iog.og[2]" "lambert4SG.dsm" -na;
connectAttr "rbgShape26.iog.og[2]" "lambert4SG.dsm" -na;
connectAttr "rbgShape21.iog.og[3]" "lambert4SG.dsm" -na;
connectAttr "lambert4SG.msg" "materialInfo3.sg";
connectAttr "white.msg" "materialInfo3.m";
connectAttr "blue.oc" "lambert5SG.ss";
connectAttr "groupId74.msg" "lambert5SG.gn" -na;
connectAttr "groupId75.msg" "lambert5SG.gn" -na;
connectAttr "groupId76.msg" "lambert5SG.gn" -na;
connectAttr "groupId77.msg" "lambert5SG.gn" -na;
connectAttr "groupId78.msg" "lambert5SG.gn" -na;
connectAttr "groupId79.msg" "lambert5SG.gn" -na;
connectAttr "groupId80.msg" "lambert5SG.gn" -na;
connectAttr "groupId81.msg" "lambert5SG.gn" -na;
connectAttr "groupId82.msg" "lambert5SG.gn" -na;
connectAttr "rbgShape20.iog.og[2]" "lambert5SG.dsm" -na;
connectAttr "rbgShape12.iog.og[1]" "lambert5SG.dsm" -na;
connectAttr "rbgShape7.iog.og[1]" "lambert5SG.dsm" -na;
connectAttr "rbgShape8.iog.og[1]" "lambert5SG.dsm" -na;
connectAttr "rbgShape11.iog.og[1]" "lambert5SG.dsm" -na;
connectAttr "rbgShape19.iog.og[2]" "lambert5SG.dsm" -na;
connectAttr "rbgShape18.iog.og[3]" "lambert5SG.dsm" -na;
connectAttr "rbgShape10.iog.og[2]" "lambert5SG.dsm" -na;
connectAttr "rbgShape9.iog.og[2]" "lambert5SG.dsm" -na;
connectAttr "lambert5SG.msg" "materialInfo4.sg";
connectAttr "blue.msg" "materialInfo4.m";
connectAttr "yellow.oc" "lambert6SG.ss";
connectAttr "groupId87.msg" "lambert6SG.gn" -na;
connectAttr "groupId88.msg" "lambert6SG.gn" -na;
connectAttr "groupId89.msg" "lambert6SG.gn" -na;
connectAttr "groupId90.msg" "lambert6SG.gn" -na;
connectAttr "groupId91.msg" "lambert6SG.gn" -na;
connectAttr "groupId92.msg" "lambert6SG.gn" -na;
connectAttr "groupId93.msg" "lambert6SG.gn" -na;
connectAttr "groupId94.msg" "lambert6SG.gn" -na;
connectAttr "groupId95.msg" "lambert6SG.gn" -na;
connectAttr "rbgShape4.iog.og[2]" "lambert6SG.dsm" -na;
connectAttr "rbgShape3.iog.og[1]" "lambert6SG.dsm" -na;
connectAttr "rbgShape7.iog.og[2]" "lambert6SG.dsm" -na;
connectAttr "rbgShape12.iog.og[2]" "lambert6SG.dsm" -na;
connectAttr "rbgShape16.iog.og[1]" "lambert6SG.dsm" -na;
connectAttr "rbgShape15.iog.og[2]" "lambert6SG.dsm" -na;
connectAttr "rbgShape23.iog.og[3]" "lambert6SG.dsm" -na;
connectAttr "rbgShape24.iog.og[2]" "lambert6SG.dsm" -na;
connectAttr "rbgShape20.iog.og[3]" "lambert6SG.dsm" -na;
connectAttr "lambert6SG.msg" "materialInfo5.sg";
connectAttr "yellow.msg" "materialInfo5.m";
connectAttr "orange.oc" "lambert7SG.ss";
connectAttr "groupId98.msg" "lambert7SG.gn" -na;
connectAttr "groupId99.msg" "lambert7SG.gn" -na;
connectAttr "groupId100.msg" "lambert7SG.gn" -na;
connectAttr "groupId101.msg" "lambert7SG.gn" -na;
connectAttr "groupId102.msg" "lambert7SG.gn" -na;
connectAttr "groupId103.msg" "lambert7SG.gn" -na;
connectAttr "groupId104.msg" "lambert7SG.gn" -na;
connectAttr "groupId105.msg" "lambert7SG.gn" -na;
connectAttr "groupId106.msg" "lambert7SG.gn" -na;
connectAttr "rbgShape2.iog.og[2]" "lambert7SG.dsm" -na;
connectAttr "rbgShape6.iog.og[3]" "lambert7SG.dsm" -na;
connectAttr "rbgShape4.iog.og[3]" "lambert7SG.dsm" -na;
connectAttr "rbgShape5.iog.og[2]" "lambert7SG.dsm" -na;
connectAttr "rbgShape1.iog.og[1]" "lambert7SG.dsm" -na;
connectAttr "rbgShape3.iog.og[2]" "lambert7SG.dsm" -na;
connectAttr "rbgShape7.iog.og[3]" "lambert7SG.dsm" -na;
connectAttr "rbgShape8.iog.og[2]" "lambert7SG.dsm" -na;
connectAttr "rbgShape9.iog.og[3]" "lambert7SG.dsm" -na;
connectAttr "lambert7SG.msg" "materialInfo6.sg";
connectAttr "orange.msg" "materialInfo6.m";
connectAttr "mama1.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[0].dn";
connectAttr "gg.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[1].dn";
connectAttr "t.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[2].dn";
connectAttr "d.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[3].dn";
connectAttr "l.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[4].dn";
connectAttr "old.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[5].dn";
connectAttr "mama.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[6].dn";
connectAttr "mamamama.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[7].dn";
connectAttr "tc1.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[8].dn";
connectAttr "tc.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[9].dn";
connectAttr "lambert2SG.pa" ":renderPartition.st" -na;
connectAttr "lambert3SG.pa" ":renderPartition.st" -na;
connectAttr "lambert4SG.pa" ":renderPartition.st" -na;
connectAttr "lambert5SG.pa" ":renderPartition.st" -na;
connectAttr "lambert6SG.pa" ":renderPartition.st" -na;
connectAttr "lambert7SG.pa" ":renderPartition.st" -na;
connectAttr "red.msg" ":defaultShaderList1.s" -na;
connectAttr "green.msg" ":defaultShaderList1.s" -na;
connectAttr "white.msg" ":defaultShaderList1.s" -na;
connectAttr "blue.msg" ":defaultShaderList1.s" -na;
connectAttr "yellow.msg" ":defaultShaderList1.s" -na;
connectAttr "orange.msg" ":defaultShaderList1.s" -na;
connectAttr "mamamama.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "defaultRenderLayer.msg" ":defaultRenderingList1.r" -na;
connectAttr "dShape.iog" ":initialShadingGroup.dsm" -na;
connectAttr "rbgShape4.iog.og[0]" ":initialShadingGroup.dsm" -na;
connectAttr "rbgShape4.ciog.cog[0]" ":initialShadingGroup.dsm" -na;
connectAttr "rbgShape5.iog.og[0]" ":initialShadingGroup.dsm" -na;
connectAttr "rbgShape5.ciog.cog[0]" ":initialShadingGroup.dsm" -na;
connectAttr "rbgShape6.iog.og[0]" ":initialShadingGroup.dsm" -na;
connectAttr "rbgShape6.ciog.cog[0]" ":initialShadingGroup.dsm" -na;
connectAttr "rbgShape13.iog.og[0]" ":initialShadingGroup.dsm" -na;
connectAttr "rbgShape13.ciog.cog[0]" ":initialShadingGroup.dsm" -na;
connectAttr "rbgShape14.iog.og[0]" ":initialShadingGroup.dsm" -na;
connectAttr "rbgShape14.ciog.cog[0]" ":initialShadingGroup.dsm" -na;
connectAttr "rbgShape15.iog.og[0]" ":initialShadingGroup.dsm" -na;
connectAttr "rbgShape15.ciog.cog[0]" ":initialShadingGroup.dsm" -na;
connectAttr "rbgShape23.iog.og[0]" ":initialShadingGroup.dsm" -na;
connectAttr "rbgShape23.ciog.cog[0]" ":initialShadingGroup.dsm" -na;
connectAttr "rbgShape22.iog.og[0]" ":initialShadingGroup.dsm" -na;
connectAttr "rbgShape22.ciog.cog[0]" ":initialShadingGroup.dsm" -na;
connectAttr "rbgShape21.iog.og[0]" ":initialShadingGroup.dsm" -na;
connectAttr "rbgShape21.ciog.cog[0]" ":initialShadingGroup.dsm" -na;
connectAttr "rbgShape18.iog.og[0]" ":initialShadingGroup.dsm" -na;
connectAttr "rbgShape18.ciog.cog[0]" ":initialShadingGroup.dsm" -na;
connectAttr "rbgShape26.iog.og[0]" ":initialShadingGroup.dsm" -na;
connectAttr "rbgShape26.ciog.cog[0]" ":initialShadingGroup.dsm" -na;
connectAttr "rbgShape25.iog.og[0]" ":initialShadingGroup.dsm" -na;
connectAttr "rbgShape25.ciog.cog[0]" ":initialShadingGroup.dsm" -na;
connectAttr "rbgShape19.iog.og[0]" ":initialShadingGroup.dsm" -na;
connectAttr "rbgShape19.ciog.cog[0]" ":initialShadingGroup.dsm" -na;
connectAttr "rbgShape20.iog.og[0]" ":initialShadingGroup.dsm" -na;
connectAttr "rbgShape20.ciog.cog[0]" ":initialShadingGroup.dsm" -na;
connectAttr "rbgShape24.iog.og[0]" ":initialShadingGroup.dsm" -na;
connectAttr "rbgShape24.ciog.cog[0]" ":initialShadingGroup.dsm" -na;
connectAttr "rbgShape9.iog.og[0]" ":initialShadingGroup.dsm" -na;
connectAttr "rbgShape9.ciog.cog[0]" ":initialShadingGroup.dsm" -na;
connectAttr "rbgShape2.iog.og[0]" ":initialShadingGroup.dsm" -na;
connectAttr "rbgShape2.ciog.cog[0]" ":initialShadingGroup.dsm" -na;
connectAttr "rbgShape17.iog.og[0]" ":initialShadingGroup.dsm" -na;
connectAttr "rbgShape17.ciog.cog[0]" ":initialShadingGroup.dsm" -na;
connectAttr "rbgShape10.iog.og[0]" ":initialShadingGroup.dsm" -na;
connectAttr "rbgShape10.ciog.cog[0]" ":initialShadingGroup.dsm" -na;
connectAttr "rbgShape12.iog.og[0]" ":initialShadingGroup.dsm" -na;
connectAttr "rbgShape12.ciog.cog[0]" ":initialShadingGroup.dsm" -na;
connectAttr "rbgShape7.iog.og[0]" ":initialShadingGroup.dsm" -na;
connectAttr "rbgShape7.ciog.cog[0]" ":initialShadingGroup.dsm" -na;
connectAttr "rbgShape8.iog.og[0]" ":initialShadingGroup.dsm" -na;
connectAttr "rbgShape8.ciog.cog[0]" ":initialShadingGroup.dsm" -na;
connectAttr "rbgShape11.iog.og[0]" ":initialShadingGroup.dsm" -na;
connectAttr "rbgShape11.ciog.cog[0]" ":initialShadingGroup.dsm" -na;
connectAttr "rbgShape3.iog.og[0]" ":initialShadingGroup.dsm" -na;
connectAttr "rbgShape3.ciog.cog[0]" ":initialShadingGroup.dsm" -na;
connectAttr "rbgShape16.iog.og[0]" ":initialShadingGroup.dsm" -na;
connectAttr "rbgShape16.ciog.cog[0]" ":initialShadingGroup.dsm" -na;
connectAttr "rbgShape1.iog.og[0]" ":initialShadingGroup.dsm" -na;
connectAttr "rbgShape1.ciog.cog[0]" ":initialShadingGroup.dsm" -na;
connectAttr "groupId1.msg" ":initialShadingGroup.gn" -na;
connectAttr "groupId2.msg" ":initialShadingGroup.gn" -na;
connectAttr "groupId3.msg" ":initialShadingGroup.gn" -na;
connectAttr "groupId4.msg" ":initialShadingGroup.gn" -na;
connectAttr "groupId5.msg" ":initialShadingGroup.gn" -na;
connectAttr "groupId6.msg" ":initialShadingGroup.gn" -na;
connectAttr "groupId7.msg" ":initialShadingGroup.gn" -na;
connectAttr "groupId8.msg" ":initialShadingGroup.gn" -na;
connectAttr "groupId9.msg" ":initialShadingGroup.gn" -na;
connectAttr "groupId10.msg" ":initialShadingGroup.gn" -na;
connectAttr "groupId11.msg" ":initialShadingGroup.gn" -na;
connectAttr "groupId12.msg" ":initialShadingGroup.gn" -na;
connectAttr "groupId13.msg" ":initialShadingGroup.gn" -na;
connectAttr "groupId14.msg" ":initialShadingGroup.gn" -na;
connectAttr "groupId15.msg" ":initialShadingGroup.gn" -na;
connectAttr "groupId16.msg" ":initialShadingGroup.gn" -na;
connectAttr "groupId17.msg" ":initialShadingGroup.gn" -na;
connectAttr "groupId18.msg" ":initialShadingGroup.gn" -na;
connectAttr "groupId28.msg" ":initialShadingGroup.gn" -na;
connectAttr "groupId29.msg" ":initialShadingGroup.gn" -na;
connectAttr "groupId30.msg" ":initialShadingGroup.gn" -na;
connectAttr "groupId31.msg" ":initialShadingGroup.gn" -na;
connectAttr "groupId32.msg" ":initialShadingGroup.gn" -na;
connectAttr "groupId33.msg" ":initialShadingGroup.gn" -na;
connectAttr "groupId34.msg" ":initialShadingGroup.gn" -na;
connectAttr "groupId35.msg" ":initialShadingGroup.gn" -na;
connectAttr "groupId36.msg" ":initialShadingGroup.gn" -na;
connectAttr "groupId37.msg" ":initialShadingGroup.gn" -na;
connectAttr "groupId38.msg" ":initialShadingGroup.gn" -na;
connectAttr "groupId39.msg" ":initialShadingGroup.gn" -na;
connectAttr "groupId49.msg" ":initialShadingGroup.gn" -na;
connectAttr "groupId50.msg" ":initialShadingGroup.gn" -na;
connectAttr "groupId51.msg" ":initialShadingGroup.gn" -na;
connectAttr "groupId52.msg" ":initialShadingGroup.gn" -na;
connectAttr "groupId53.msg" ":initialShadingGroup.gn" -na;
connectAttr "groupId54.msg" ":initialShadingGroup.gn" -na;
connectAttr "groupId55.msg" ":initialShadingGroup.gn" -na;
connectAttr "groupId56.msg" ":initialShadingGroup.gn" -na;
connectAttr "groupId66.msg" ":initialShadingGroup.gn" -na;
connectAttr "groupId67.msg" ":initialShadingGroup.gn" -na;
connectAttr "groupId68.msg" ":initialShadingGroup.gn" -na;
connectAttr "groupId69.msg" ":initialShadingGroup.gn" -na;
connectAttr "groupId70.msg" ":initialShadingGroup.gn" -na;
connectAttr "groupId71.msg" ":initialShadingGroup.gn" -na;
connectAttr "groupId72.msg" ":initialShadingGroup.gn" -na;
connectAttr "groupId73.msg" ":initialShadingGroup.gn" -na;
connectAttr "groupId83.msg" ":initialShadingGroup.gn" -na;
connectAttr "groupId84.msg" ":initialShadingGroup.gn" -na;
connectAttr "groupId85.msg" ":initialShadingGroup.gn" -na;
connectAttr "groupId86.msg" ":initialShadingGroup.gn" -na;
connectAttr "groupId96.msg" ":initialShadingGroup.gn" -na;
connectAttr "groupId97.msg" ":initialShadingGroup.gn" -na;
// End of rubic.ma
