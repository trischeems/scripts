##### Tri vega #######
########### " Contacts with me : info.tri3d@gmail.com "
########### " Gumroad : https://phamtri.gumroad.com/"
########### " Copyright by Tri 3D "
########### " Thanks for you !!! "
import sys
import imp
import VegaStudio_tools_animation.Functions.Tri3D_Ui as toolsUi

if sys.version_info.major >= 3:
    imp.reload(toolsUi)
else:
    reload(toolsUi)

toolsUi.createUI()
