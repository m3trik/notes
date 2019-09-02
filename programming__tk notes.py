## tk_hotBox
###### *PySide marking menu style layered ui and toolkit for maya and max.


![alt text](https://raw.githubusercontent.com/m3trik/tk_hotBox/master/docs/Screenshot-Camera_navigation.jpg)
*Example of camera navigation.

![alt text](https://raw.githubusercontent.com/m3trik/tk_hotBox/master/docs/Screenshot-Menu.jpg)
*Menu set.


## Design:
######
*This is a cross-platform, app agnostic, modular, marking menu style ui to house user tools. Each piece is constructed dynamically
to allow for as little overhead as possible in construction and maintainence. Literally all you have to do to have 
a new ui up and running, is to drop a qt designer ui file into the ui folder, create a module and class of the 
same name. Naming convention allows for a stacked ui to be built, signals added/removed, and a master dictionary 
(stored within the switchboard module) to be created that allows getting/setting of relevant data across modules from one 
easy, and reliable location.*

*continual work in progress..*

##
-----------------------------------------------
 Structure:
-----------------------------------------------

## tk_main: 
######
*handles main gui construction.*

* get dynamic ui files relative to folder location.

* handle coordinates to populate ui at cursor position.

* add each ui to a layout stack.

* set window flags and attributes.

* set event filters and overrides.

* construct paint events.


## tk_signals: 
######
*constructs signal connections.*

* build connection dict in switchboard for each class with corresponding signals and slots.

* add/remove signals using the switchboard dict each time the stacked layout index is changed.



## tk_slots: 
######
*master class holding methods that are inherited across all app specific slot class modules.*



## tk_switchboard: 
######
*the following is an example of some of the imformation held for each tool class instance. From this information, you can call switchboard methods to 
get most relevent information easily wherever you need it.*
*for a full up-to-date list, check the tk_switchboard module's docstring.*

* class name as string

* class object

* widget size

* widget name/method name as string

* widget Object

* widget Object with Signal

* method Object

* method docString

* uiList : *string list of all ui filenames in the ui folder*

* previousName : *list of last called relevant ui*

* previousView: *index of the last valid previously opened ui name.*

* prevCommand : *history of commands. uses the method docstring to generate a user friendly name from the dynamic element and stores it along side the command method.*



##
-----------------------------------------------
 Naming convention:
-----------------------------------------------

######
* ui files:     \<name\>.ui
 
* tools module: tk_slots_\<app\>_\<name\>.py
 
* class name:   \<Name\>

*widget/corresponding class methods share the same naming convention across all modules: ie. widget b021 connects to method b021.
the docstring of each method houses a user friendly name that is stored with all other widget info in the switchboard dict when an
instance is populated. Any of the buttons will also connect to a corresponding class method should it exist.*

* QPushButton   b000    (b000-b999) can contain 1000 buttons of one type max per class using this convention.

* QPushButton   i000    these buttons are attached an event filter to change the ui index.

* QComboBox     cmb000  ""

* QCheckBox     chk000  ""

* QSpinBox      s000    ""

* QtextField    t000    ""

any additional widget types can be easily added when needed using this same convention.


##
-----------------------------------------------
 Basic use:
-----------------------------------------------

######
* pressed hotkey shows instance. release hides;

* mouse not pressed: heads up info

* right mouse down: shows main navigation window.

* left mouse down: shows viewport navigation and camera settings.

* middle mouse down: shows mesh display options.

* releasing the mouse over any of the buttons in those windows takes you to the corresponding sub-menu.

* double left mouseclick: produces last used orthographic view.

* double right mouseclick: produces last sub-menu.

* double middle mouseclick: repeats last command.

* dragging on an empty area of the widget moves the window and pins it open.

* holding ctrl while using Spinboxes increments/decrements by an extra decimal place.

* mouse over buttons while window pinned to get an explanation of its function.



##
-----------------------------------------------
 Installation:
-----------------------------------------------
######
(Assuming the directory structure is left intact).

In maya:
* add \maya\tk_slots_maya directory to maya.env
 (MAYA_SCRIPT_PATH=<dir>)
 
In 3ds Max
* add \max\startup directory to system path by navigating in app to:
 main menu> customize> additional startup scripts
 
The default hotkey for launching the menu set is f12. This is because I usually remap f12 to the windows key. This can be changed in the tk_main module.




#times
'''
tk_signals
time: 0.11471084274
tk_slots_max_viewport
time: 0.0632666986347
tk_slots_max_polygons
time: 0.0816165578988
'''





# Re-load Ui:
# import sys
# import os.path as os

# path = os.expandvars("%CLOUD%/__portable/_scripts/")
# sys.path.append(path)

# reload(tk_main)










# BUGS:
# -----------------------------------------------
'''



fix maya's delete shortcut.  reg delete button works.





init heads up display contents not current. require refresh


fix create> circle>  attributes


scene> rename;  with selection, and find field empty, nothing is renamed. (an * in the find field returns correct result) 


set normal by angle not working with no error.


assign scene material cmb does nothing. ui list doesnt expand to fit contents.


fix repeat last command


bug: transform negative '-' sets spinbox value to 0.  







'''





# THINGS TO DO NOW:
# -----------------------------------------------
'''

#combine bridge and tri-fill buttons in polygons.  remove reverse normals and instead check for surrounding normal direction.


#use the maxplus method to parent the widget to the app. remove disable keyboard from show/hide events, and import maxplus when creating instance.



#texturing> materials combobox> id map checkbox not toggling back to regular materials list from id map.



#normals> by angle> add progress bar.  fix progress bar not hiding/resetting on completion.



#file> save> separate save and save & close. add wifeframe flag to close only.




component path tool
	supporting
	nth component
	loop
	ring
	contigious
	shortest path
	
#nth edge
-------------
polySelect(*args, **kwargs)
    This command makes different types of poly component selections.  The return value is an integer array containing the
    id's of the components in the selection in order. If a given type of selection loops back on itself then this is
    indicated by the start id appearing twice, once at the start and once at the end.
    
    Flags:
      - add : add                      (bool)          [create,query]
          Indicates that the specified items should be added to the active list without removing existing items from the active
          list.
    
      - addFirst : af                  (bool)          [create,query]
          Indicates that the specified items should be added to the front of the active list without removing existing items from
          the active list.
    
      - asSelectString : ass           (bool)          [create,query]
          Changes the return type from an integer array to a string array which can be used as a selection string.
    
      - deselect : d                   (bool)          [create,query]
          Indicates that the specified items should be removed from the active list if they are on the active list.
    
      - edgeBorder : eb                (int)           [create,query]
          Select all conected border edges starting at the given edge.
    
      - edgeBorderPath : ebp           (int, int)      [create,query]
          Given two edges on the same border, this will select the edges on the border in the path between them.
    
      - edgeBorderPattern : bpt        (int, int)      [create,query]
          Given two edges on the same border, this will check how many edges there are between the given edges and then continue
          that pattern of selection around the border.
    
      - edgeLoop : el                  (int)           [create,query]
          Select an edge loop starting at the given edge.
    
      - edgeLoopOrBorder : elb         (int)           [create,query]
          Select an edge loop or all conected border edges, depending on whether the edge is on a border or not, starting at the
          given edge.
    
      - edgeLoopOrBorderPattern : lbp  (int, int)      [create,query]
          Given two edges either on the same edge loop or on the same edge border, this will check how many edges there are
          between the given edges and then continue that pattern of selection around the edge loop or edge border.
    
      - edgeLoopPath : elp             (int, int)      [create,query]
          Given two edges that are on the same edge loop, this will select the shortest path between them on the loop.
    
      - edgeLoopPattern : lpt          (int, int)      [create,query]
          Given two edges on the same edge loop, this will check how many edges there are between the given edges and then
          continue that pattern of selection around the edge loop.
    
      - edgeRing : er                  (int)           [create,query]
          Select an edge ring starting at the given edge.
    
      - edgeRingPath : erp             (int, int)      [create,query]
          Given two edges that are on the same edge ring, this will select the shortest path between them on the ring.
    
      - edgeRingPattern : rpt          (int, int)      [create,query]
          Given two edges on the same edge ring, this will check how many edges there are between the given edges and then
          continue that pattern of selection around the edge ring.
    
      - edgeUVLoopOrBorder : euv       (int)           [create,query]
          Select an edge loop or border, terminating at UV borders.
    
      - everyN : en                    (int)           [create]
          Number of elements to stride over. If less than 1 then use 1, meaning every element. 2 means every second one, etc.
    
      - extendToShell : ets            (int)           [create,query]
          Select the poly shell given a face id.
    
      - noSelection : ns               (bool)          [create,query]
          If this flag is used then the selection is not changed at all.
    
      - replace : r                    (bool)          [create,query]
          Indicates that the specified items should replace the existing items on the active list.
    
      - shortestEdgePath : sep         (int, int)      [create,query]
          Given two vertices, this will select the shortest path between them in the 3d object space.
    
      - shortestEdgePathUV : spu       (int, int)      [create,query]
          Given two UVs, this will select the shortest path between them in the 2d texture space.
    
      - shortestFacePath : sfp         (int, int)      [create,query]
          Given two faces, this will select the shortest path between them in the 3d object space.
--------------




#center pivot shortcut


#transfer module.  possibly keep this in 'edit' module


#scene> save> autosave + intervals & amount.  undo amount & slider


#attach/detach/combine/separate/detach curve/etc


#mirror tool> options:
	# copy / instance / flip
	# mirror axis position (world, object, bounding box)
	# add combine with original chk box


# measure geometry tool


# scale selected tool (using null object and checking heirarchy)



# explore use of orderedDict module for init contents



# treeview> construct folder heirarchy and parent objects
null = pm.group(empty=1, name='')
pm.group(empty=1, parent=null, name='')
pm.parent('joint_root_0', 'Joints')



#freeze joint transforms
pm.makeIdentity('joint11', apply=1, translate=1, rotate=1, scale=1, jointOrient=1)


mel.eval('AddAttribute;')
#dynAddAttrWin( {} );

mel.eval('RenameAttribute;')
#dynRenameAttrWin( {} );








#while in heads up display; holding any additional key shows keyboard shortcuts mapped to that key. similar to substance





select by edge angle function





mesh clean-up



	

edit> delete menu
with delete, delete loop, delete history
for edge in rt.selection:
	edge.SelectEdgeLoop()
	edge.EditablePoly.Remove()





set crease amount 	obj.EditablePoly.setEdgeData(1, 0.5)






display> toggle material override


editors:
scene> editors cmb> Asset Tracking System		ATSOps.visible = true
selection> editors> Named Selection Sets 	 macros.run "Edit" "namedSelSets"
editors> Crease Explorer	CreaseExplorerManager.OpenCreaseExplorer ()

selection>  select similar



override materials with fast shader
	actionMan.executeAction 0 "63574"  -- Views: Override Off





search field returns related commands.



framework for interactive tools
# method for storing values


radial array: add interactive update on pivot change
set pivot;  move -r -0.829437 0 0 pCylinder27.scalePivot pCylinder27.rotatePivot


create> cmb001> keep window open on indexChanged.  closing and re-opening hides spinboxes.






move polygon collapse to merge area

 
create camera from view
look through [camera from drop down list]
 

create; creating a primitive doesnt align to set axis
spinboxes visible on set point
wrap setattributes call in an undoinfo chunk

duplicate w/transform spinboxes; convert to being interactive.
add center pivot option



create; angled pipe.  creates a basic pipe section and allows to interactively add angles/fittings/ etc.
create; stairs.  step, rise, amount
create; railing
create; saved asset. store points to building block items etc ascii


move ui path variable to a config file

scene: set unreal/unity project. GamePipeline -sp "Unreal";
scene: re-export last

display; build a layer editor

fix recent autosave;  %userprofile%/AppData/Local/Temp  get dir file list,  sort by date modified

add try/except to delete history function

fix in-view message alpha transparency

use grow/shrink selection buttons to scroll through 'select by name' results.
commands change the textfielchrome-extension://mpognobbkildjkofajifpdfhcoklimli/components/startpage/startpage.htmld text and call t001 function to select that node.
possibly use the toggle function to keep tabs on list place
prevent focus initially.  when focused chkpin down



edit; delete (component) not working
  File "O:\Cloud/____Graphics/Maya/scripts/_Python/_Python_startup\tk_maya_buttons.py", line 1420, in b032
    faces = func.getAllFacesOnAxis (axis)
  File "O:\Cloud/____Graphics/Maya/scripts/_Python/_Python_startup\tk_maya_functions.py", line 45, in getAllFacesOnAxis
    if pm.exactWorldBoundingBox (attr)[index] < -0.00001:
  File "C:\Program Files\Autodesk\Maya2018\Python\lib\site-packages\pymel\internal\pmcmds.py", line 140, in exactWorldBoundingBox_wrapped
pymel.core.general.MayaAttributeError: Maya Attribute does not exist (or is not unique):: u'|brake_disc|brake_disc|brake_discShape.e[261:262].f[0]'


better clean up menu. with checkboxes for options

better center pivot; check component or object mode and apply interactive transforms accordingly.
possibly merge with main transform menu. and add separate spinboxes for x, y, and z. with the option to chain values to each other. 


save; could not delete: elise_mid.009 find a way to delete file regardless of extension. possibly for filename in filenames: if filename.startswith('elise_mid.009'): remove file. maybe best to just get project root and search recursively.
change default iterations to 5; save iteration amount to settings text file.


undo queue combobox (command start with capital letters and functions start with lower case).
scripting; recent commands combobox
 
add maya uv workflow to uv notes https://www.youtube.com/watch?v=cy1vqLw-agk


consolidate all in edit> transfer.  batch transfer is missing. batch translate is being called instead.

start a store settings text file

in the functions module build a list and function that can track selection order
later use it to create a tool instance

align pivot; face normal

create menu creates object on combobox index changed. adjusting settings edits the created objects inputs
pm.plane = polyPlane[]   plane[0] points to pPlane1 (transform node), and plane[1] points to polyPlane1 (history node).

tooltip for polygons>split vertex

display> wireframe inactive; set to query current mode and if wireframe: set to shaded then apply.  otherwise doesn't work

create function for populating new window/message window

add custom keyboard shortcuts via python script instead of manually

pinned windows re-open as separate instance

radial array 
['VRayLightRect1', 'VRayLightRect1_ins1', 'VRayLightRect1_ins2', 'VRayLightRect1_ins3', 'VRayLightRect1_ins4', 'VRayLightRect1_ins5', 'VRayLightRect1_ins6', 'VRayLightRect1_ins7', 'VRayLightRect1_ins8', 'VRayLightRect1_ins9', 'VRayLightRect1_ins10', 'VRayLightRect1_ins11', 'VRayLightRect1_ins12', 'VRayLightRect1_ins13', 'VRayLightRect1_ins14', 'VRayLightRect1_ins15', 'VRayLightRect1_ins16', 'VRayLightRect1_ins17', 'VRayLightRect1_ins18', 'VRayLightRect1_ins19', 'VRayLightRect1_ins19', 'VRayLightRect1_ins19_ins1', 'VRayLightRect1_ins19_ins2', 'VRayLightRect1_ins19_ins3', 'VRayLightRect1_ins19_ins4', 'VRayLightRect1_ins19_ins5', 'VRayLightRect1_ins19_ins6', 'VRayLightRect1_ins19_ins7', 'VRayLightRect1_ins19_ins8', 'VRayLightRect1_ins19_ins9', 'VRayLightRect1_ins19_ins10', 'VRayLightRect1_ins19_ins11', 'VRayLightRect1_ins19_ins12', 'VRayLightRect1_ins19_ins13', 'VRayLightRect1_ins19_ins14', 'VRayLightRect1_ins19_ins15', 'VRayLightRect1_ins19_ins16', 'VRayLightRect1_ins19_ins17', 'VRayLightRect1_ins19_ins18', 'VRayLightRect1_ins19_ins19', 'VRayLightRect1', 'VRayLightRect1_dup1', 'VRayLightRect1_dup2', 'VRayLightRect1_dup3', 'VRayLightRect1_dup4', 'VRayLightRect1_dup5', 'VRayLightRect1_dup6', 'VRayLightRect1_dup7', 'VRayLightRect1_dup8', 'VRayLightRect1_dup9', 'VRayLightRect1_dup10', 'VRayLightRect1_dup11', 'VRayLightRect1_dup12', 'VRayLightRect1_dup13', 'VRayLightRect1_dup14', 'VRayLightRect1_dup15', 'VRayLightRect1_dup16', 'VRayLightRect1_dup17', 'VRayLightRect1_dup18', 'VRayLightRect1_dup19', 'VRayLightRect1_dup19', 'VRayLightRect1_dup19_dup1', 'VRayLightRect1_dup19_dup2', 'VRayLightRect1_dup19_dup3', 'VRayLightRect1_dup19_dup4', 'VRayLightRect1_dup19_dup5', 'VRayLightRect1_dup19_dup6', 'VRayLightRect1_dup19_dup7', 'VRayLightRect1_dup19_dup8', 'VRayLightRect1_dup19_dup9', 'VRayLightRect1_dup19_dup10', 'VRayLightRect1_dup19_dup11', 'VRayLightRect1_dup19_dup12', 'VRayLightRect1_dup19_dup13', 'VRayLightRect1_dup19_dup14', 'VRayLightRect1_dup19_dup15', 'VRayLightRect1_dup19_dup16', 'VRayLightRect1_dup19_dup17', 'VRayLightRect1_dup19_dup18', 'VRayLightRect1_dup19_dup19', 'VRayLightRect1', 'VRayLightRect1_ins1', 'VRayLightRect1_ins2', 'VRayLightRect1_ins3', 'VRayLightRect1_ins4', 'VRayLightRect1_ins5', 'VRayLightRect1_ins6', 'VRayLightRect1_ins7', 'VRayLightRect1_ins8', 'VRayLightRect1_ins9', 'VRayLightRect1_ins10', 'VRayLightRect1_ins11', 'VRayLightRect1_ins12', 'VRayLightRect1_ins13', 'VRayLightRect1_ins14', 'VRayLightRect1_ins15', 'VRayLightRect1_ins16', 'VRayLightRect1_ins17', 'VRayLightRect1_ins18', 'VRayLightRect1_ins19'] #
Traceback (most recent call last):
  File "O:\Cloud/____Graphics/Maya/scripts/_Python/_Python_startup\tk_maya_func.py", line 1836, in b038
    self.b001(create=True)
  File "O:\Cloud/____Graphics/Maya/scripts/_Python/_Python_startup\tk_maya_func.py", line 1554, in b001
    pm.polyUnite (radialArrayObjList, name=objectName)
  File "C:\Program Files\Autodesk\Maya2018\Python\lib\site-packages\pymel\internal\factories.py", line 957, in newFuncWithReturnFunc
    res = beforeReturnFunc(*args, **kwargs)
  File "C:\Program Files\Autodesk\Maya2018\Python\lib\site-packages\pymel\internal\pmcmds.py", line 140, in polyUnite_wrapped
    raise pymel.core.general._objectError(obj)
pymel.core.general.MayaNodeError: Maya Node does not exist (or is not unique):: u'VRayLightRect1_ins1'

add all relevant options for smooth preview located in poly display properties.

image plane setup; get size of selected image and construct plane at camera
look at maya/workflow notes for proper workflow to automate
lock; aspect ratio on plane.  backface culling.

default xyz values for transform move and rotate. 
	add rotate (scale, move) 'by camera' option to transform
	center pivot (object seems to work best) option (on by default)
transform:
	add tweak mode checkbox. strsTweakMode true; click and drag mode for adjusting components
	add step snap relative. manipMoveSetSnapMode 1; toggle off 0 checkable transform an object or component in incriments
	add step snap absolute. manipMoveSetSnapMode 2; toggle off 0 checkable ""
	for both; textfield defalt float 1.00. manipMoveContext -edit -snapValue value Move;

add button for soften/ harden edge procedure. I think it is in a tab here or in python startup.
in normals: create procedure for: if creased; edge harden else; soften. crease transfer algorithm my have useful parts.
fix crease transfer algorithm 
	note future features such as bevel all creased edge by crease value
	explore idea of working with hard/soft edges and transforming them to creased edges

create> text
import maya.app.type.typeToolSetup
maya.app.type.typeToolSetup.createTypeTool()

create init button.  rehash functions module

Cannot find procedure "bt_snapAlignObjectToComponentOptions".
	Start of trace: (command window: line 1).

add toggle polyVertex Face to display menu. or look into face draw size option. doMenuComponentSelection("elise_bodyShell_mid_001", "pvf");
	$mode = `selectMode -query -component`;
	if ($mode==0)
	changeSelectMode -component;
	$maskVertex = `selectType -query -vertex`;
	
add grease pencil window to grease pencil tool as option
GreasePencilTool;
createGreasePencilWindow();

add clipping planes to display
could query current camera and getAttr and change perspShape to "current camera"+Shape
or just have a camera settings button that shows the settings in the attribute editor. 
pm.setAttr ("perspShape.nearClipPlane", 0.001)
pm.setAttr ("perspShape.farClipPlane", 10000)

dR_selConstraintAngle; #alternate command syntax. use regex
dR_DoCmd("selConstraintAngle"); #takes an angle value
dR_DoCmd("selConstraintBorder");
dR_DoCmd("selConstraintElement");
dR_DoCmd("selConstraintOff");



EXTEND FUNCTIONALITY:

modify'frame selected' to query symmetry state (because when more than 1 vertex is selected, they are generally far apart) edit: $state = `symmetricModelling -query -symmetry`;



UI FUNCTIONALITY:

transparent shortcut buttons reveal text name when moused over
transparent shortcut groups can be changed in preferences. ie. modeling shortcuts, rendering shortcuts

tk_maya init; ui in sub-folder with tk_main instead of path (just copy code from test.py)
importing tk_maya_buttons as buttons instead of * would be pointless if splitting up the button module later 

outputwindow text color for help messages

push text from a helpline to a textfield

finish ui stylesheet
simply the way signals and slots are built based on the way the stylesheet builds styles
move all 

spinboxes increment an extra decimal place while holding shift key (pyside key modifiers)






MORE INVOLVED:


framework for interactive tool settings, using polygons> bevel as model.

create optionBox method. create new button beside given button, resizing to compensate.    

keyword app/local command search (using namespace)

add framework for interactive tools (use radial array as a model)

build layer editor.

build a selection function that returns different the current selection
	filter by type:
	as string:
		main object from component
	as object
	converted to:
		vertices
		faces
		edges
	various ls flags:
	all objects

radial symmetry

straighten circle tool. (third party script in maya projects folder)
average curve tool.


script command popup elf window commands like mel2py won't accept multiple lines of code. tried to fix and now completely broken. possibly have a look and see if its not better to just convert it and 'scene options' elf windows into qt ui and add them to layout stack.


play with contrain edge options to build useful selection constraints

better insert edge tool
polySplitRing -constructionHistory off -smoothingAngle 30 -weight 0.9 -fixQuads 1;

collapse edge/
	pm.selectPref (preSelectClosest=True) #definitely want this setting off when not used
	selectPref -preSelectSize 15; #this sets the preselect area tolerance (i think)
	closestVert = pm.ls (selection=True)
	print closestVert
stitch tool
	selectPref(trackSelectionOrder=True)

build heads up display:
	symmetry state
	any active selection constraits
	polycount
	pm.helpLine(width=20, height=8)
	progress bar

select island doesnt work with symmetry also needs the abiltiy for multiple selections







OLD:

functionality to add:

quick rotate menu set. rotate by textedit amount + or - (default 45).

marking menu normals 'set to face' add command average normals before calling
add button edit> Optimize Scene mel; OptimizeScene;
modify Un crease edge so that it works both in object mode for all edges and component mode on just selected edges
add crease 'sets' button; python code: from maya.app.general import creaseSetEditor creaseSetEditor.showCreaseSetEditor()
add toggle crease edge visibility mel; polyOptions -displayCreaseEdge true; polyOptions -displayCreaseEdge false; modify to iterate through and toggle crease display for all objects in the scene. this is a good candidate for a checkbox
modify script; if nothing selected export visible geometry
understand symmetry and getting the align edge loop tool to work with it
functionality for hotkey g repeat last to be used on custom tools
add button toggle script editor output window size
fix sets in toolkit. add buttons from create> sets; set partition, quick select set and options
add buttons; edit mesh> vertex> average vertices, chamfer vertices, reorder vertices
uv tool popup mel window
add button 'Transfer Maps' (no options) mel: performSurfaceSampling 1; 
hotkey hide other objects f2; check for how many objects visible before executing if <2 inView error message
query poly clean up to get current flag state
building on top of existing straighten edgeloop script:use selection order to build an array and iterate through multiple edgeloops
check box support
create instance toggle for all duplicate actions
mod toolkit selection contraints; create drop down menu to select contraint and user input for contraint angle
change minimum size for tool settings, channel/layers
UV display put current display settings in array and toggle off/on 
heads up display for current selection count
toggle (black) silhouette of geometry  (to see low poly curvature ect)





batch export FBX and OBJ
proc batchExport (string $fileType)
	{
	$selection = createArrayFromSelection();
	$exportPath = sourceDirectory($fileType);

	for ($node in $selection)
		{
		$finalExportPath = ($exportPath+"/"+$node);

		if ($fileType == "obj")
			// select -replace $node;
			file -force
						-exportSelected
						-preserveReferences 
						-type "OBJexport"
						-options "-groups 0 \
											-ptgroups 0 \
											-materials 0 \
											-smoothing 1 \
											-normals 1"
						// ($node+".obj");
						($finalExportPath+".obj");
						print ($finalExportPath+".obj"+"\n");

		if ($fileType == "fbx")
			{
			// // Uncomment for export options
			// // Geometry
			// FBXExportSmoothingGroups -v true;
			// FBXExportHardEdges -v false;
			// FBXExportTangents -v false;
			// FBXExportSmoothMesh -v true;
			// FBXExportInstances -v false;
			// FBXExportReferencedContainersContent -v false;
			// // Animation
			// FBXExportBakeComplexAnimation -v false;
			// // FBXExportBakeComplexStart -v "";
			// // FBXExportBakeComplexEnd -v "";
			// FBXExportBakeComplexStep -v 1;
			// // FBXExportBakeResampleAll -v true;
			// FBXExportUseSceneName -v false;
			// // FBXExportQuaternion -v euler;
			// FBXExportShapes -v true;
			// FBXExportSkins -v true;
			// // Constraints
			// FBXExportConstraints -v false;
			// // Cameras
			// FBXExportCameras -v false;
			// // Lights
			// FBXExportLights -v false;
			// // Embed Media
			// FBXExportEmbeddedTextures -v false;
			// // Connections
			// FBXExportInputConnections -v false;
			// // Axis Conversion
			// FBXExportUpAxis y;

			// print ($finalExportPath+"\n");
			FBXExport -selected -file ($finalExportPath+".fbx");
			print ($finalExportPath+".fbx"+"\n");
			}
		}
	}







- da_intPlay: this script add the interactive play button directly to Time Slider
- da_curveToPoly: this script make possible the conversion of curves in polygons
- da_interactiveBooleans: this script make the Polygonal Boolean process more interactive
- da_BooleanFullIntersect: this script make a full intersect, so this execute a mesh subtraction but maintain subtracted part as separate object
- da_PlaneCutter: this script cut a mesh by using a flat mesh, this can be useful for simulate surface cracks
- da_AutoBevel: this script analyse the angle between faces and try to add a Bevel node only on needed edges
- da_ClothAsDeformer: this script set up the current mesh to be deformed by nCloth solver, this can be useful for simulate character selfcollision skin or muscle dynamics
- da_nParticleConverter: this script add the ability to convert particle to a specific type after their creation
- da_perspToggle: this script convert the current persp view to the closest ortho, and vice versa
- da_shell: this script emulates Shell deformer of Autodesk 3D Studio Max, by adding a thickness to flat polygons
- da_ConvertToMetaballs: this script convert particles to polygonal Metaballs
- da_MashVoxelizer: this script use MASH to voxelize an arbitrary mesh inside of another mesh
- da_RivetMash: this script constraint the pivot of a polygon to a component of another polygon
- da_CurveDistributionMash: this script scatter and constrain a polygonal object along a curve
- da_EdgeToLoopToCurve: this script convert edge selection to loop and then make a batch conversion to curves, this is useful for converting polygonal hair to curve hair 
- da_SurfaceScatterMash: this script scatter and constrain a polygonal object on a mesh
- da_CurveLength: this script returns the length of a curve in Maya unit
- da_MouseTrack: this script tracks the mouse movement and create an animation
- da_FacesFollicles: this script creates a follicle in the centre of selected faces
- da_Compass: this script converts Euler angle into a XYZ vector, for drive wind direction in Nucleus and Air Filed
- da_CombineCurves: this script combines curves in a single transform
- da_SepareCurves: this script separate combined curves
- da_MapFacesUV: this script maps any single faces of a mesh as separate planar UV shell
- da_KeyKeyedOnly: this script creates animation keys only on already animated channels
- Control Constraint: this set of scripts constraint a controller to a single or multiple controlled object(s)





'''














# deprecated



  # def initWidgets(self):
  #   '''
  #   Set initial states for dynamic ui widgets. 
  #   '''
  #   for widget in self.sb.getWidget(self.name): #constructs connections for, and returns, all widgets for the given ui name.
  #     # widget.installEventFilter(self)
  #     # widget.setMouseTracking(True)

  #     widgetName = widget.objectName()
  #     widgetType = widget.__class__.__name__ # self.sb.getWidgetType(widget)

  #     widget.setStyleSheet(StyleSheet.css) #add StyleSheet

  #     if self.name=='init' and widgetName=='t000':
  #       widget.viewport().setAutoFillBackground(False)
  #       widget.setTextBackgroundColor(QtGui.QColor(50, 50, 50))

  #     if self.name=='main' or self.name=='viewport':
  #       if widgetName.startswith('r'):
  #         widget.setVisible(False)

  #     if self.name=='create':
  #       if widgetName.startswith('s'):
  #         widget.setVisible(False)



  # def eventFilter(self, widget, event):
  #   '''
  #   Event filter for dynamic ui widgets.
  #   args:
  #     widget=<object> - the widget for which the event occurred.
  #     event=<QEvent>
  #   '''
  #   for widget in self.sb.getWidget(self.name): #constructs connections for, and returns, all widgets for the given ui name.

  #     widgetName = widget.objectName()
  #     widgetType = widget.__class__.__name__ # self.sb.getWidgetType(widget)


  #     #___MouseButtonPress Event
  #     if event.type()==QtCore.QEvent.MouseButtonPress:
  #       self.__mousePressPos = event.globalPos()


  #     #___MouseMove Event
  #     if event.type()==QtCore.QEvent.MouseMove:
  #       if widgetType=='QPushButton':
  #         if widgetName.startswith('i') or widgetName.startswith('v'): #set down
  #           widget.setDown(widget.rect().contains(widget.mapFromGlobal(QtGui.QCursor.pos())))

  #         elif widgetName=='pin': #move window on left mouse drag.
  #           self.moveToMousePosition(self, -self.point.x(), -self.point.y()*.1)

  #       elif widgetType=='QWidget':
  #         if widgetName.startswith('r'): #set visibility
  #           widget.setVisible(widget.geometry().contains(event.pos()))

  #       elif widgetType=='QComboBox':
  #         if widget.rect().contains(widget.mapFromGlobal(QtGui.QCursor.pos())):
  #           #switch the index before opening to initialize the contents of the comboBox
  #           widget.setStyleSheet(StyleSheet.comboBox_alt)
  #           index = widget.currentIndex()
  #           widget.blockSignals(True)
  #           widget.setCurrentIndex(-1)
  #           widget.blockSignals(False)
  #           widget.setCurrentIndex(index) #change index back to refresh contents
  #         else:
  #           widget.setStyleSheet(StyleSheet.comboBox)


  #     #___MouseButtonRelease Event
  #     if event.type()==QtCore.QEvent.MouseButtonRelease:
  #       print widgetName
  #       if widgetType=='QPushButton':
  #         if widget.rect().contains(widget.mapFromGlobal(QtGui.QCursor.pos())):
  #           if widgetName.startswith('i'): #connect to layoutStack and pass in an index as int or string 'name'.
  #             index = widget.whatsThis()
  #             self.layoutStack(index) #switch the stacked layout to the given ui.

  #           elif widgetName.startswith('v'): #ie. 'v012'
  #             self.sb.previousView(as_list=1).append(self.sb.getMethod(self.name, widgetName)) #store the camera view
  #             widget.click()

  #           elif widgetName.startswith('b'): #ie. 'b012'
  #             self.sb.prevCommand(as_list=1).append([self.sb.getMethod(self.name, widgetName), self.sb.getDocString(widgetName)]) #store the command method object and it's docString (ie. 'Multi-cut tool')

  #           elif widgetName=='pin': #Override pushbutton to move the main window on left mouse drag event. When checked, prevents hide event on main window.
  #             print 'pin_mouseReleaseEvent', widgetName
  #             moveAmount = event.globalPos() - self.__mousePressPos
  #             if moveAmount.manhattanLength() > 5: #if widget moved:
  #               widget.setChecked(True) #setChecked to prevent window from closing.
  #               event.ignore()
  #             else:
  #               widget.setChecked(not widget.isChecked()) #toggle check state
  #               self.hide_()

  #       elif widgetType=='QComboBox':
  #         if widget.rect().contains(widget.mapFromGlobal(QtGui.QCursor.pos())):
  #           widget.setStyleSheet(StyleSheet.comboBox_popup)
  #           widget.showPopup()


  #     #___Enter Event
  #     if event.type()==QtCore.QEvent.Type.Enter:
  #       self.__mouseHover.emit(True)


  #     #___HoverLeave Event
  #     if event.type()==QtCore.QEvent.Type.HoverLeave:
  #       self.__mouseHover.emit(False)

  #   # return super(HotBox, self).eventFilter(widget, event)
  #   return QtWidgets.QWidget.eventFilter(self, widget, event)






# def keyPressEvent(self, event):
#     '''
#     args:
#       event=<QEvent>
#     '''
#     if event.key()==QtCore.Qt.Key_F12 and not event.isAutoRepeat(): #Key_Meta or Key_Menu =windows key
#       pass


  # def setWidget(self, w):
  #   '''
  #   args:
  #     w=<QWidget>
  #   '''
  #   w.installEventFilter(self)
  #   if self.overlay is None:
  #     self.overlay = Overlay()
  #   self.overlay.setParent(w)



  # def mouseMoveEvent(self, event):
  #   '''
  #   args:
  #     event=<QEvent>
  #   '''




  # def mouseReleaseEvent(self, event):
  #   '''
  #   args:
  #     event=<QEvent>
  #   '''





# # ------------------------------------------------
#   # Event overrides
#   # ------------------------------------------------
#   def eventFilter(self, widget, event):
#     '''
#     Event filter for dynamic ui objects.
#     args:
#       widget=<object> - the widget for which the event occurred.
#       event=<QEvent>
#     '''
#     widgetName = widget.objectName()
#     widgetType = widget.__class__.__name__ # self.sb.getWidgetType(widget)

#     #___MouseButtonPress Event_____________________
#     if event.type()==QtCore.QEvent.MouseButtonPress:
#       print 'MouseButtonPress',widgetName
#       if widgetName=='pin':
#         self.__mousePressPos = event.globalPos()

#     #___MouseMove Event_____________________
#     if event.type()==QtCore.QEvent.MouseMove:
#       print 'MouseMove-', widgetName
#       if widgetName=='pin':
#         self.moveToMousePosition(self, -self.point.x(), -self.point.y()*.1) #move window on left mouse drag.

#       if any([self.name=='main', self.name=='editors', self.name=='viewport']):
#         print 'MouseMove:',self.name,widgetName
#         if widgetName.startswith('r'):
#           print '- - -'
#           if widget.geometry().contains(event.pos()):
#             print '- - - -'
#             widget.setVisible(True)
#           else:
#             widget.setVisible(False)

#         if widgetName.startswith('i') or widgetName.startswith('v'):
#           if widget.rect().contains(widget.mapFromGlobal(QtGui.QCursor.pos())):
#             widget.setDown(True)
#           else:
#             widget.setDown(False)

#         if widgetName.startswith('cmb'):
#           if widget.rect().contains(widget.mapFromGlobal(QtGui.QCursor.pos())):
#             widget.setStyleSheet(StyleSheet.comboBox_alt)
#           else:
#             widget.setStyleSheet(StyleSheet.comboBox_popup)


#     #___MouseButtonRelease Event_____________________
#     if event.type()==QtCore.QEvent.MouseButtonRelease:
#       print 'MouseButtonRelease:',self.name,widgetName
#       if widgetName=='pin': #Override pushbutton to move the main window on left mouse drag event. When checked, prevents hide event on main window.
#         moveAmount = event.globalPos() - self.__mousePressPos
#         if moveAmount.manhattanLength() > 5: #if widget moved:
#           widget.setChecked(True) #setChecked to prevent window from closing.
#           event.ignore()
#         else:
#           widget.setChecked(not widget.isChecked()) #toggle check state
#           self.hide_()

#       if widgetName.startswith('i'): #connect to layoutStack and pass in an index as int or string 'name'.
#         index = widget.whatsThis()
#         self.layoutStack(index) #switch the stacked layout to the given ui.

#       if widgetName.startswith('v'): #ie. 'v012'
#         self.sb.previousView(as_list=1).append(self.sb.getMethod(widgetName)) #store the camera view

#       if widgetName.startswith('b'): #ie. 'b012'
#         self.sb.prevCommand(as_list=1).append([self.sb.getMethod(widgetName), self.sb.getDocString(widgetName)]) #store the command method object and it's docString (ie. 'Multi-cut tool')


#     #___Enter Event__________________________
#     if event.type()==QtCore.QEvent.Type.Enter:
#       print 'Enter', widgetName
#       self.mouseHover.emit(True)
#       if widgetType=='QComboBox':
#         #switch the index before opening to initialize the contents of the comboBox
#         index = widget.currentIndex()
#         widget.blockSignals(True); widget.setCurrentIndex(-1); widget.blockSignals(False)
#         widget.setCurrentIndex(index) #change index back to refresh contents
#         widget.setStyleSheet(StyleSheet.comboBox_popup)

#       if any([self.name=='main', self.name=='editors', self.name=='viewport']): #layoutStack index and viewport signals
#         if widgetType=='QComboBox':
#           widget.showPopup()
#         elif widgetType=='QPushButton':
#           widget.click()

#       if self.name=='init' and widgetType=='QTextEdit':
#         # self.sb.getMethod('t000')()
#         pass


#     #___HoverLeave Event__________________________
#     if event.type()==QtCore.QEvent.Type.HoverLeave:
#       self.mouseHover.emit(False)
#       if widgetType=='QComboBox':
#         widget.setStyleSheet(StyleSheet.comboBox)
  


#     return QtWidgets.QWidget.eventFilter(self, widget, event)



    # # if not self.name=='init': #remove old and add new signals for current ui from connectionDict
    # if self.name!=self.sb.previousName(allowDuplicates=1):
    #   if self.sb.previousName():
    #     self.sb.removeSignal(self.sb.previousName())
    #     self.sb.addSignal(self.name)
    #   else: #if no previous ui exists
    #     self.sb.addSignal(self.name)


  # def mouseMoveEvent(self, event):
  #   '''
  #   args:
  #     event=<QEvent>
  #   '''
  #   if self.name=='main':
  #     self.setVisibilityOnHover(event.pos(), 'r000-9')
  #     self.setDown_(event.pos(), 'i003-32, v000-37')
  #     self.showPopup_(event.pos(), 'cmb000-2')

  #   if self.name=='editors':
  #     self.setVisibilityOnHover(event.pos(), 'r000-9')
  #     self.setDown_(event.pos(), 'v000-4')
  #     # self.showPopup_(event.pos(), 'cmb000-2')

  #   elif self.name=='viewport':
  #     self.setVisibilityOnHover(event.pos(), 'r000-8')
  #     self.setDown_(event.pos(), 'v000-29')
  #     self.showPopup_(event.pos(), 'cmb000-3')



  # def unpackNames(self, nameString):
  #   '''
  #   Get a list of individual names from a single name string.
  #   args:
  #     nameString=string consisting of widget names separated by commas. ie. 'v000, b004-6'
  #   returns:
  #     unpacked names. ie. ['v000','b004','b005','b006']
  #   '''
  #   packed_names = [n.strip() for n in nameString.split(',') if '-' in n] #build list of all widgets passed in containing '-'

  #   unpacked_names=[]
  #   for name in packed_names:
  #     name=name.split('-') #ex. split 'b000-8'
  #     prefix = name[0].strip('0123456789') #ex. split 'b' from 'b000'
  #     start = int(name[0].strip('abcdefghijklmnopqrstuvwxyz') or 0) #start range. #ex. '000' #converting int('000') returns None, if case; assign 0.
  #     stop = int(name[1])+1 #end range. #ex. '9' from 'b000-8' for range up to 9 but not including 9.
  #     unpacked_names.extend([str(prefix)+'000'[:-len(str(num))]+str(num) for num in range(start,stop)]) #build list of name strings within given range

  #   names = [n.strip() for n in nameString.split(',') if '-' not in n] #all widgets passed in not containing '-'

  #   return names+unpacked_names



  # def getUiObject(self, widgets):
  #   '''
  #   Get ui objects from name strings.
  #   args:
  #     widgets='string' - ui object names
  #   returns:
  #     list of corresponding ui objects  
  #   '''
  #   objects=[]
  #   for name in self.unpackNames(widgets):
  #     try:
  #       w = getattr(self.ui, name)
  #       objects.append(w)
  #     except: pass
  #   return objects



  # def setVisibilityOnHover(self, mousePosition, widgets):
  #   '''
  #   Show/hide widgets on mouseover event.
  #   args:
  #     mousePosition=QPoint
  #     widgets=string consisting of widget names separated by commas. ie. 'r000, r001, v000-13, i020-23'
  #   '''
  #   for w in self.getUiObject(widgets):
  #     if w.geometry().contains(mousePosition):
  #       w.show()
  #     else:
  #       w.hide()



  # def setDown_(self, mousePosition, widgets):
  #   '''
  #   Set pushbutton down state.
  #   args:
  #     mousePosition=QPoint
  #     widgets=string consisting of widget names separated by commas. ie. 'r000, r001, v000-13, i020-23'
  #   '''
  #   for w in self.getUiObject(widgets):
  #     if w.rect().contains(w.mapFromGlobal(QtGui.QCursor.pos())):
  #       w.setDown(True)
  #     else:
  #       w.setDown(False)



  # def showPopup_(self, mousePosition, widgets):
  #   '''
  #   Set comboBox popup state.
  #   args:
  #     mousePosition=QPoint
  #     widgets=string 
  #   '''
  #   for w in self.getUiObject(widgets):
  #     if w.rect().contains(w.mapFromGlobal(QtGui.QCursor.pos())):
  #       # w.showPopup()
  #       w.setStyleSheet('''
  #         QComboBox {
  #         background-color: rgba(82,133,166,200);
  #         color: white;
  #         }
  #         ''')
  #     else:
  #       # w.hidePopup()
  #       w.setStyleSheet('''
  #         background-color: rgba(100,100,100,200);
  #         color: white;
  #         }
  #         ''')



# def hoverEvent(self, event):
#     '''
#     args:
#       event=<QEvent>
#     '''
#     print "hover"


# def onSignalEvent(self, widgetName):
#   '''
#   Called on any ui widget before it's signal is triggered.
#   args:
#     widgetName='string' - objectName of button
#   '''
#   widget = self.getWidget(widgetName)

#   if widgetName.startswith('i'): #connect to layoutStack and pass in an index as int or string 'name'.
#     index = widget.whatsThis() #widget.text()
#     self.layoutStack(index) #switch the stacked layout to the given ui.

#   if widgetName.startswith('b'): #ie. 'b012'
#     self.sb.prevCommand(as_list=1).append([self.sb.getMethod(widgetName), self.sb.getDocString(widgetName)]) #store the command method object and it's docString (ie. 'Multi-cut tool')

#   if widgetName.startswith('v'): #ie. 'v012'
#     self.sb.previousView(as_list=1).append(self.sb.getMethod(widgetName)) #store the camera view



# # ------------------------------------------------
# # Popup Window
# # ------------------------------------------------
# class Popup(QtWidgets.QWidget):
#   def __init__(self, ui, parent=None):
#     QtWidgets.QWidget.__init__(self, parent)

#     layout = QtWidgets.QGridLayout(self)
#     layout.addWidget(ui)
#     layout.setContentsMargins(0,0,0,0) #adjust the margins or you will get an invisible, unintended border

#     self.setLayout(layout)
#     self.adjustSize()

#     self.setWindowFlags(QtCore.Qt.Popup | QtCore.Qt.Tool | QtCore.Qt.FramelessWindowHint) #tag this widget as a popup



# # ------------------------------------------------
# # Grid
# # ------------------------------------------------
# class Grid(QtWidgets.QWidget):
#   def __init__(self, hotBox, parent=None):
#     super(Grid, self).__init__(parent)


#     # layout = QtWidgets.QHBoxLayout(self)
#     # layout.setSpacing(0)
#     # layout.setContentsMargins(0,0,0,0)

#     # self.pin = Pin(hotBox)
#     # layout.addWidget(self.pin)

#     # self.cmb = QtWidgets.QComboBox()
#     # self.cmb.setMaximumSize(18,18)
#     # layout.addWidget(self.cmb)

#     self.hotBox = hotBox

#     self.hotBox.signal.buildConnectionDict('grid') #construct the signals and slots for the ui
#     self.ui = self.hotBox.sb.getUi('grid')

#     self.ui.pin.installEventFilter(self)



#   def eventFilter(self, obj, event):
#     # if event.buttons()==QtCore.Qt.LeftButton:
#     if event.type()==QtCore.QEvent.MouseButtonPress:
#       self.__mousePressPos = event.globalPos()
#       return True

#     if event.type()==QtCore.QEvent.MouseMove:
#       self.hotBox.moveToMousePosition(self.hotBox, -self.hotBox.point.x(), -self.hotBox.point.y()*.1) #move window on left mouse drag.
#       return True

#     if event.type()==QtCore.QEvent.MouseButtonRelease:
#       moveAmount = event.globalPos() - self.__mousePressPos
#       if moveAmount.manhattanLength() > 5: #if button moved:
#         self.setChecked(True) #setChecked to prevent window from closing.
#         event.ignore()
#       else:
#         self.setChecked(not self.isChecked()) #toggle check state
#         self.hotBox.hide_()
#       return True
#     return False #return False for other event types




# class Pin(QtWidgets.QPushButton):
#   '''
#   Pushbutton overridden to move the main window on left mouse drag event.
#   When checked, prevents hide event on main window.
#   '''
#   def __init__(self, hotBox, parent=None):
#     super(Pin, self).__init__(parent)

#     self.hotBox = hotBox
#     self.setCheckable(True)


#   def mousePressEvent(self, event):
#     '''
#     args:
#       event=<QEvent>
#     '''
#     if event.button()==QtCore.Qt.LeftButton:
#       self.__mousePressPos = event.globalPos()


#   def mouseMoveEvent(self, event):
#     '''
#     args:
#       event=<QEvent>
#     '''
#     if event.buttons()==QtCore.Qt.LeftButton:
#       self.hotBox.moveToMousePosition(self.hotBox, -self.hotBox.point.x(), -self.hotBox.point.y()*.1) #move window on left mouse drag.


#   def mouseReleaseEvent(self, event):
#     '''
#     args:
#       event=<QEvent>
#     '''
#     if event.button()==QtCore.Qt.LeftButton:
#       moveAmount = event.globalPos() - self.__mousePressPos
#       if moveAmount.manhattanLength() > 5: #if button moved:
#         self.setChecked(True) #setChecked to prevent window from closing.
#         event.ignore()
#       else:
#         self.setChecked(not self.isChecked()) #toggle check state
#         self.hotBox.hide_()

