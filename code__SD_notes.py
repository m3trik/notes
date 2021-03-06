#Python in Substance Designer










# ======================================================================
#	GRAPH:
# ======================================================================

#Get the Current Graph and Selection (import sd):
# Get the application and UI manager object.
ctx = sd.getContext()
app = ctx.getSDApplication()
uiMgr = app.getQtForPythonUIMgr()

# Get the current graph.
currentGraph = UIMgr.getCurrentGraph()

#Get the package manager & current package.
pkgMgr = app.getPackageMgr()
currentpackage = pkgMgr.getUserPackages().getItem(0)

# Get the currently selected nodes.
selection = uiMgr.getCurrentGraphSelection()
for node in selection:
	print("Node %s" % node)

# ----------------------------------------------------------------------









# ======================================================================
#	NODES:
# ======================================================================

# Accessing node definitions and properties (import sd, from sd.api.sdproperty import SDPropertyCategory, from sd.api.sdvalueserializer import SDValueSerializer):
# Available node information include:
	#definition;
	#identifier;
	#position;
	#properties (as a list);
	#resources that are being referenced;

def printSelectedNodesInfo(nodes):
	'''Print information regarding the selected nodes.
	'''
	for node in nodes:
		definition = node.getDefinition()
		nodeId = node.getIdentifier()

		print("node %s, id = %s" % (definition.getLabel(), nodeId))

		# Create a list of each property category enumeration item.
		categories = [
			SDPropertyCategory.Annotation,
			SDPropertyCategory.Input,
			SDPropertyCategory.Output
		]

		# Get node properties for each property category.
		for category in categories:
			props = definition.getProperties(category)

			# Get the label and identifier of each property.
			for prop in props:
				label = prop.getLabel()
				propId = prop.getId()

				# Get the connection for the currently accessed property.
				if prop.isConnectable():
					connections = node.getPropertyConnections(prop)

					if connections:
						print("Propery %s is connected!!!" % label)
						continue

				# Get the value for the currently accessed property.
				value = node.getPropertyValue(prop)

				if value:
					print("Property %s, id = %s, value = %s" % (label, propId, SDValueSerializer.sToString(value)))


# Accessing node inputs identifiers and types (import sd, from sd.api import sduimgr, from sd.api.sdproperty import *):
# Access a node in the current graph, and its properties.
graph = uiMgr.getCurrentGraph()
node = graph.getNodeFromId('<Replace this text with the node ID>')
nodeProps = node.getProperties(SDPropertyCategory.Input)

# List node identifiers and types in console.
for i in range(len(nodeProps)):
	print(nodeProps[i].getId())
	print(nodeProps[i].getType())



def getMaterialList(rootpath):
    for i in os.listdir(rootpath):
        path = os.path.join(rootpath, i)
        if path.split('')[-1] == '.autosave' or path.split('')[-1] == 'dependencies':
            continue
        filename = path.split('')[-1]
        if filename.split('.')[-1] == 'sbs' and not os.path.isfile(path + 'ar'):
            print(path)
            MaterialPathList.append(path)
        if os.path.isdir(path):
            getMaterialList(path)



def createPBRRenderNode(app, pkgMgr, currentGraph):
	'''Create PBR Render Node.
	'''
	resourcePath = app.getPath(SDApplicationPath.DefaultResourcesDir)
	package = pkgMgr.loadUserPackage(os.path.join(resourcePath, 'packages', 'pbr_render_ortho.sbs'))
	packageName = 'PBR_render_ortho'
	instanceNode = currentGraph.newInstanceNode(package.findResourceFromUrl(packageName))
	instanceNode.setInputPropertyValueFromId('shape', SDValueInt.sNew(1))
	instanceNode.setInputPropertyValueFromId('envrionment_horizontal_rotation', SDValueFloat.sNew(0.06))
	instanceNode.setInputPropertyValueFromId('background_color', SDValueColorRGBA.sNew(ColorRGBA(0, 0, 0, 0)))
	return instanceNode


def linkEnvironmentMap(app, pbrRenderNode, package, currentGraph):
	'''
	'''
	resourcePath = app.getPath(SDApplicationPath.DefaultResourcesDir)
	envMapPath = resourcePath + '/view3d/maps/glazed_patio.exr'
	envMap = SDResourceBitmap.sNewFromFile(package, envMapPath, EmbedMethod.Linked)
	envMapNode = currentGraph.newInstanceNode(envMap)
	envMapNode.newPropertyConnectionFromId('unique_filter_output', pbrRenderNode, 'environment_map')

# ----------------------------------------------------------------------









# ======================================================================
#	HISTORY:
# ======================================================================

#Undo groups (import sd, from sd.api.sdhistoryutils import *):
#Get the application and package manager objects.
cxt = sd.getContext()
app = cxt.getSDApplication()
pkgMgr = app.getPackageMgr()

#Group one or more changes into an undo group.
with SDHistoryUtils.UndoGroup("My Undo Group"):
	# Create two new packages.
	pkgMgr.newUserPackage()
	pkgMgr.newUserPackage()

# ----------------------------------------------------------------------









# ======================================================================
#	UI:
# ======================================================================

# Get the application.
app = sd.getContext().getSDApplication()


# Get the UI Manager.
uiMgr = app.getQtForPythonUIMgr()


# Get the main window.
mainWindow = uiMgr.getMainWindow()



# Creating Panels (import sd, from PySide2 import QtWidgets):
#Create a new dock widget.
#The dock identifier is used when saving and restoring dock positions and sizes.
#For this reason, it's important that the identifier is unique.
dock = uiMgr.newDockWidget(identifier="sample.test.dock", title="New Dock")

# Create a layout and add some widgets.
layout = QtWidgets.QVBoxLayout()
dock.setLayout(layout)

for i in range(0, 5):
	layout.addWidget(QtWidgets.QPushButton("Button %s" % i))



# Creating Toolbars in the Application Window (import sd, from PySide2 import QtCore, QtWidgets):
#Create our toolbar.
toolbar = QtWidgets.QToolBar()
toolbar.addAction("Tool")
toolbar.addAction("Bar")

# Add our toolbar to Designer's window.
mainWindow.addToolBar(QtCore.Qt.TopToolBarArea, toolbar)



# Creating Toolbars in Graph Views (from functools import partial, import sd, from PySide2 import QtCore, QtGui, QtWidgets):
class MyGraphToolBar(QtWidgets.QToolBar):
	def __init__(self, graphViewID, uiMgr):
		super(MyGraphToolBar, self).__init__(parent=uiMgr.getMainWindow())

		# Save the graphViewID and uiMgr for later use.
		self.__graphViewID = graphViewID
		self.__uiMgr = uiMgr

		# Add actions to our toolbar.
		act = self.addAction("P")
		act.setToolTip("Print the selected nodes to the Python console")
		act.triggered.connect(self.__onPrintNodes)

	def __onPrintNodes(self):
		for node in self.__getSelectedNodes():
			print(node)

	def __getSelectedNodes(self):
		# Use our saved graphViewID to retrieve the graph selection.
		return self.__uiMgr.getCurrentGraphSelectionFromGraphViewID(
			self.__graphViewID)

def onNewGraphViewCreated(graphViewID, uiMgr):
	# Create our toolbar.
	toolbar = MyGraphToolBar(graphViewID, uiMgr)

	# Add our toolbar to the graph widget.
	uiMgr.addToolbarToGraphView(
		graphViewID,
		toolbar,
		icon = None,
		tooltip = "My Graph Toolbar")

# Get the application and UI manager object.
ctx = sd.getContext()
app = ctx.getSDApplication()
uiMgr = app.getQtForPythonUIMgr()

# Register a callback to know when GraphViews are created.
uiMgr.registerGraphViewCreatedCallback(
	partial(onNewGraphViewCreated, uiMgr=uiMgr))

# ----------------------------------------------------------------------









# ======================================================================
#	IMPORT | EXPORT:
# ======================================================================

exporterInstance = SDSBSARExporter(ctx, None)
e = exporterInstance.sNew()
e.exportPackageToSBSAR(package, savepath)

# ----------------------------------------------------------------------








# ======================================================================
#	ERRORS:
# ======================================================================




# ----------------------------------------------------------------------