#				|||||||||||||||||||||||||||||||||||||||||||
#				||||||||||		Qt UI Notes		|||||||||||
#				!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!






QtCore							# core non-graphical classes used by other modules
QtGui							# base classes for UI components
QtWidgets						# classes to extend qt GUI with c++ widgets
QObject							# basic non-visual building block. signals, events,
#QtCharts
#QtMultimedia
#QtNetwork
#QtQuick
#QtTest













'Widgets: '#------------------------------------------------------------------



#QApplication:
#The difference between QtWidgets.QApplication.instance() and QtWidgets.qApp is that the latter is a static module variable that must be created when the module is first imported. 
inst = QtWidgets.QApplication.instance()
qapp = QtWidgets.qApp #qApp is initially just an empty wrapper. #Once the QApplication is created, though, they will both point to the same thing:
#So even though no QApplication object has been created yet, the qApp variable still points to a QApplication instance.

#current application instance
QtCore.QCoreApplication.instance()


# Find item in QApplication by only the objectname:
QtWidgets.QApplication.topLevelWindows()
#top level widgets
widgets = {w.objectName():w for w in QtWidgets.QApplication.topLevelWidgets()}
#windows
windows = {w.objectName():w for w in QtWidgets.QApplication.allWindows()}
#all
widgets = {w.objectName():w for w in QtWidgets.QApplication.allWidgets()}
widget = widgets['MainAttributeEditorLayout']



#get a list of all QObject instances either by class-name or object-name:
#This is only really a debugging tool, as for a large application, there could easily be several hundred thousand objects to check.
def getObjects(name, cls=True):
	objects = []
	for obj in gc.get_objects():
		if(isinstance(obj, QtCore.QObject) and
			((cls and obj.inherits(name)) or
			 (not cls and obj.objectName() == name))):
			objects.append(obj)
	return objects

#If you only need objects which are subclasses of QWidget, use this function:
def getWidgets(name, cls=True):
	widgets = []
	for widget in QtGui.QApplication.allWidgets():
		if ((cls and w.inherits(name)) or
			(not cls and w.objectName() == name)):
			widgets.append(widget)
	return widgets




#get object name
name = w.objectName()


#get widget type:
w.__class__.__name__ 			#returns class name as a string
#alt using QMetaObject:
w.metaObject().className()
#alt using type():
type(widget)
type(widget).__name__ 			#same as: w.__class__

#
w.inherits('classname')			#Returns true if this object is an instance of a class that inherits className or a PySide.QtCore.QObject subclass that inherits className
qobject_cast<Type *>(object)	#determine whether an object is an instance of a particular class for the purpose of casting it


#Toggle
w.setVisible(not w.isVisible()) 



#QAction
#the following three fragments are equivalent:
act = QtGui.QAction("Action", self)
act.triggered.connect(self.on_triggered)
#
act = QtGui.QAction("Action", self, triggered=self.on_triggered)
#
act = QtGui.QAction("Action", self)
act.pyqtConfigure(triggered=self.on_triggered)











#visibility

#toggle visibility
w.setVisible(not w.isVisible()) 

w.isEnabled						#Returns Bool - 

w.isVisible						#Returns Bool - 
w.isHidden						#Returns Bool - 
w.setHidden(True)

w.show()
w.hide()
w.close()




#bring to front
w.raise_()
#send to back
w.lower()



#Focus
w.setFocusPolicy() Keyboard Focus #w.setFocusPolicy(QtCore.Qt.StrongFocus)

w.hasFocus()
w.setFocus()
w.clearFocus()

isActiveWindow()
w.activateWindow() 				#Sets the top-level widget containing this widget to be a top-level window that has keyboard input focus.


#shedule refresh 
w.update()









#Remove widget
for i in reversed(range(self.layout.count())): 
	widgetToRemove = self.layout.itemAt(i).widget()
	self.layout.removeWidget(widgetToRemove) #remove it from the layout list
	widgetToRemove.setParent(None) #remove it from the gui





#Layouts

QFormLayout
QGridLayout
QBoxLayout
QVBoxLayout

#stacking multiple widgets
#setting up a stacked layout
QStackedLayout

#build list of all widget names to be stacked
uiList = ["init", "main", "viewport", "mainOptions", "viewportOptions", "normals", "create", "edit", "transform", "selection", "polygons", "nurbs", "texturing", "animation"]
#use index to get ui name or set stack index
self.name = uiList[index]

if(self.layout() == None):
	self.stackedLayout = QtWidgets.QStackedLayout()

	for ui in uiList:
		ui = getQtui(ui)
		self.stackedLayout.addWidget(ui)

	self.setLayout(self.stackedLayout)

#set ui from stack
self.stackedLayout.setCurrentIndex(index)

#get ui from stack
# self.ui = self.stackedLayout.currentWidget()
self.ui = self.stackedLayout.widget(index)




#WA - Widget attribute
#https://doc.qt.io/archives/qtjambi-4.5.2_01/com/trolltech/qt/core/Qt.WidgetAttribute.html

#change of state events
w.setAttribute(QtCore.Qt.WA_WState_Created)
w.setAttribute(QtCore.Qt.WA_WState_Hidden)
w.setAttribute(QtCore.Qt.WA_WState_Visible)
w.setAttribute(QtCore.Qt.WA_WState_ExplicitShowHide)

#disable/close events
w.setAttribute(QtCore.Qt.WA_DeleteOnClose) #Makes Qt delete this widget when the widget has accepted the close event #w.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)
w.setAttribute(QtCore.Qt.WA_Disabled) #Indicates that the widget is disabled
w.setAttribute(QtCore.Qt.WA_ForceDisabled) #Indicates that the widget is explicitly disabled
w.setAttribute(QtCore.Qt.WA_QuitOnClose) #Makes Qt quit the application when the last widget with the attribute set has accepted closeEvent().

#visibility
w.setAttribute(QtCore.Qt.WA_DontShowOnScreen)
w.setAttribute(QtCore.Qt.WA_ShowWithoutActivating) #Show the widget without making it active.

#add/remove events
w.setAttribute(QtCore.Qt.WA_NoChildEventsForParent) #Indicates that the widget does not want ChildAdded or ChildRemoved events sent to its parent.
w.setAttribute(QtCore.Qt.WA_NoChildEventsFromChildren) #Indicates that the widget does not want to receive ChildAdded or ChildRemoved events sent from its children.


# Remove layout
#recursively remove and delete all the objects from a layout.
def clearLayout(self, layout):
	if layout is not None:
		while layout.count():
		item = layout.takeAt(0)
		widget = item.widget()
		if widget is not None:
			w.deleteLater()
		else:
			self.clearLayout(item.layout())






# Widget types:

#Stacked Widget
stackedWidget = QtWidgets.QStackedWidget()
for w in widgetList:
	stackedWidget.addWidget(w)
window.setCentralWidget(stackedWidget)




#QPushButton (QAbstractButton, QRadiobutton, QCheckBox)
b = QtWidgets.QPushButton()

#signals. (signal in)
#Qt signals:
b.clicked()
b.pressed()
b.released()
b.toggled()
b.setText()
b.setIcon()

b.click() 						#emits clicked signal


b.clicked.connect(method)
#or with arguments
b.clicked.connect(lambda x=arg: method(x))
b.clicked.connect(lambda: method(x))

#public slots: setChecked(bool), toggle()

#connect to multiple slots:
map(self.dial.valueChanged.connect, [self.spinbox.setValue, self.getValue_dial])
#or
[self.dial.valueChanged.connect(x) for x in [self.spinbox.setValue, self.getValue_dial]]
#alternatively you could connect to one method and use that to call various others.


#enable/ disable button objects
b.setEnabled(False) 			#either method serves both functions. must be used with an argument
b.setDisabled(True)

b.setDefault() 					#QPushButton.setDefault() #Sets the button as default

b.pressed() 					#bool #QPushButton.pressed()
b.released() 					#bool #QPushButton.released()

b.toggled() 					#bool. query pushbutton toggle state.
b.toggle() 						#Toggles the state of a checkable button.




#check state
#		QtUi checkable button signal input
#		self.ui.connect(HandleSelection, SIGNAL(toggled(bool)),MEL_HandleSelection,SLOT(setVisible(bool)));
#		QObject::connect(moreButton, SIGNAL(toggled(bool)), tertiarypb7Box, SLOT(setVisible(bool)));

b.stateChanged() 				#QCheckBox.stateChanged()
b.stateChanged.connect(method)
#
b.setCheckable(True) 			#Recognizes pressed and released states of button if set to true
b.isChecked()					#Returns Bool - state of button
#setChecked
b.setChecked(True)				#Bool
b.setChecked(not b.isChecked())	#toggle


#button text
b.text 							#QPushButton.text() #Retrieves buttons’ caption or textfields value
b.setText 						#QPushButton.setText() #Programmatically sets buttons’ caption or textfields value
b.setText(0, 'text '+str(num))	#append integer
b.setText(0, "Parent {}".format(num)) #alt


# icon
b.setIcon #QPushButton.setIcon()
# Shows an icon formed out of pixmap of an image file
b.setIcon(QIcon(QPixmap("python.gif")))

#set icon to rgb value:
pixmap = QtGui.QPixmap(100,100)
pixmap.fill(QtGui.QColor.fromRgb(r, g, b))
cmb.setItemIcon(index, QtGui.QIcon(pixmap))






#QSpinBox. (for a double value use QDoubleSpinBox)
s = QtWidgets.QSpinbox()

#signals:
s.valueChanged(arg)				#optional arg=unicode or int of specific value that has been modified. ie. s.valueChanged[unicode].connect(callback_unicode)


#get
s.text() 						#Returns Unicode - gets prefix/suffix string value
s.value() 						#Returns  - Get the current value
s.cleanText() 					#get the current value excluding any prefix or suffix
s.singleStep() 					#gets the step value of counter
#set
s.setMinimum(-5) 				#Sets the lower bound of counter
s.setMaximum(5) 				#Sets the upper bound of counter
s.setRange(0,10) 				#Sets the minimum, maximum and step value
s.setWrapping(s) 				#Set whether spin box is circular. Both bounds must be set for this to have an effect.
s.setSingleStep(1) 				#Sets the step value.
s.setValue(2) 					#set value
s.setPrefix("") 				#Set a string prefix.
s.setSuffix("") 				#Set the string suffix appended to the spinbox text.



s.valueChanged.connect(method)




#QComboBox
cmb = QtWidgets.QComboBox()

#signals:
cmb.activated.connect(method)
cmb.activated[str].connect(method)
cmb.activated(int).connect() 	#index of the selected item
cmb.activated(unicode).connect(method) #[str] text of selected item

cmb.highlighted().connect(method) #index of the selected item
cmb.highlighted(index).connect(method) #[str] text of selected item

cmb.currentIndexChanged.connect(method)
cmb.currentIndexChanged(index).connect(method)

cmb.editTextChanged.connect(method)



#set items:
cmb.addItem(string, userData=None) #string/data
cmb.addItems(list_) 			#string/data
cmb.insertItem(index, string, userData=None) #at index
cmb.insertItems(index, list_)
#get all items:
items = [cmb.itemText(i) for i in range(cmb.count())]
#get items:
cmb.findText(text) 				#get index using string
cmb.itemText(index) 			#get string using index
cmb.itemData(index) 			#data
cmb.findData(data) 				#data
#set index
cmb.setCurrentIndex(0)
cmb.setCurrentIndex(cmb.findText('')) #using string
#get index
cmb.currentIndex()
#get text
cmb.currentText() 				#get current text
#set text
cmb.setItemText(cmb.currentIndex(), text) #set current text



# remove
cmb.removeItem(index)


#block signals

#separator
cmb.insertSeparator(index)


#get combobox contents:
list_ = [cmb.itemText(i) for i in range(cmb.count())]

#remove contents
cmb.clear()


#get/set data
cmb.addItem('string', data) 	#set string, set data
cmb.itemData(cmb.currentIndex()) #get current data
cmb.setItemData(index, value) 	#data

#expand/collapse
cmb.hidePopup()
cmb.showPopup()



#edit line
#get
cmb.lineEdit(): 				#Returns the line edit used to edit items in the combobox, or 0 if there is no line edit. QtGui.QLineEdit widget is a one-line text editor.
#set
cmb.setLineEdit(edit) 			#Sets the line edit to use instead of the current line edit widget.


#combobox model (QtCore.QAbstractItemModel, QtGui.QStandardItemModel)
#get
cmb.model()						#Returns QStandardItemModel - of the combobox. The model class provides a generic model for storing custom data.
cmb.modelColumn()				#the column in the model that is visible. If set prior to populating the combo box, the pop-up view will not be affected and will show the first column (using this property’s default value).
cmb.rootModelIndex()			#Returns the root model item index for the items in the combobox.
#set
cmb.setModal(model) 			#Sets the model. model must not be 0. If you want to clear the contents of a model, call QtWidgets.QComboBox.clear().


#combobox view (QtGui.QAbstractItemView, QtWidgets.QListView)
#get
cmb.view()						#Returns QListView - of the combobox popup. The view class provides a list or icon view onto a model.
#set
cmb.setView(itemView)			#Sets the view to be used in the combobox popup to the given itemView . The combobox takes ownership of the view. Note: If you want to use the convenience views (like QtWidgets.QListWidget , QtWidgets.QTableWidget or QtWidgets.QTreeWidget), make sure to call QtWidgets.QComboBox.setModel() on the combobox with the convenience widgets model before calling this function.
cmb.view().setMinimumWidth(cmb.minimumSizeHint().width()) #set view width to fit contents.


#comboBox frame
#get
frame = cmb.findChild(QtWidgets.QFrame) #Returns QFrame(or None) - of the comboBox.
frame.frameStyle() 				#get frame style

#set
cmb.setFrame(False) 			#Bool - popup frame visability.
frame.setFrameStyle(QtGui.QFrame.Panel|QtGui.QFrame.Raised) #QFrame.NoFrame, Box, Panel, StyledPanel, HLine and VLine; the shadow styles are Plain, Raised and Sunken
frame.move(frame.x()+70, frame.y()-20)
frame.setModal(True) 			#




# QTableWidget
#get/set data
table_widget = QTableWidget()
table_widget.setRowCount(1) # add one row
item = QtGui.QTableWidgetItem()
item.setText( 'description') # set description
item.setData( QtCore.Qt.UserRole, my_data ) # set data
table_widget.setItem( 0, 0, item ) # add item to table on row 0, colum 0
current_row = table_widget.currentRow() # selected row
item = table_widget.item( 0, 0 )
print item.text() 				#get description
print item.data( QtCore.Qt.UserRole ) # get data






# QTreeWidget
#get/set data
tree_widget = QtWidgets.QTreeWidget()
item = QtWidgets.QTreeWidgetItem(tree_widget, ['description']) # set description
item.setData(1, QtCore.Qt.EditRole, my_data) #set data
print item.text(0) 				#get description
print item.text(1) 				#get data

#item widget
#get
self.itemWidget(wItem, column): #(bool) query: widget in column
wItem = self.itemBelow(wItem) 	#return the wItem below
#set
wItem = QtWidgets.QTreeWidgetItem(self) #create a new widgetItem row

#set widgetItem child
self.setItemWidget(wItem, column, widget)

#columns
self.setColumnCount(int)

#remove widgetItem
[self.takeTopLevelItem(self.indexOfTopLevelItem(i)) for i in items]

#remove widgetItem Child
wItem.takeChild(column) #indexOfTopLevelItem #indexOfChild
self.removeItemWidget(wItem, column)



def get_subtree_nodes(tree_widget_item):
	"""Returns all QTreeWidgetItems in the subtree rooted at the given node."""
	nodes = []
	nodes.append(tree_widget_item)
	for i in range(tree_widget_item.childCount()):
		nodes.extend(get_subtree_nodes(tree_widget_item.child(i)))
	return nodes

def get_all_items(tree_widget):
	"""Returns all QTreeWidgetItems in the given QTreeWidget."""
	all_items = []
	for i in range(tree_widget.topLevelItemCount()):
		top_item = tree_widget.topLevelItem(i)
		all_items.extend(get_subtree_nodes(top_item))
	return all_items #return [self.getSubtreeNodes(self.topLevelItem(i)) for i in range(self.topLevelItemCount())]






# QListWidget
#add key(or value) from a dictionary to a list 
listContents=[]
for key in seqDict:
	listContents.append(key)
# add list contents
l = self.ui.listWidget
l.clear()
if listContents:
	l.addItems(sorted(listContents))
	# resize listWidget to fit contents
	l.sizeHintForColumn(0) + 2 * l.frameWidth()
	l.sizeHintForRow(0) * l.count() + 2 * l.frameWidth()
	l.setFixedSize(l.sizeHintForColumn(0) + 2 * l.frameWidth(), l.sizeHintForRow(0) * l.count() + 2 * l.frameWidth())

#get list string value
files = self.ui.listWidget.selectedItems()
for f in files:
	print f.text()





# QRadioBox





# QMessageBox
box = QtGui.QMessageBox()
ex.
msgBox = QtWidgets.QMessageBox()
		msgBox.setText('message')
		msgBox.exec_()

ex.
box = QtGui.QMessageBox()
box.setIcon(QtGui.QMessageBox.Question)
box.setWindowTitle('Kaydet!')
box.setText('Kaydetmek İstediğinize Emin Misiniz?')
box.setStandardButtons(QtGui.QMessageBox.Yes|QtGui.QMessageBox.No)
buttonY = box.button(QtGui.QMessageBox.Yes)
buttonY.setText('Evet')
buttonN = box.button(QtGui.QMessageBox.No)
buttonN.setText('Iptal')
box.exec_()

if box.clickedButton() == buttonY:
	# YES pressed
elif box.clickedButton() == buttonN:
	# NO pressed








# QLabel
lbl = QtWidgets.QLabel()

#connect on mousePress
lbl.mousePressEvent = method #method must take event as an arg.







# QLineEdit
ex.	if lineEdit.text() == default_text:
		lineEdit.setText("")
		set_focus_in_color()
		QtGui.QLineEdit.focusInEvent(lineEdit, QtGui.QFocusEvent(QtCore.QEvent.FocusIn))
	  
	lineEdit.focusInEvent = focus_in

#		QLineEdit signal in
#		Qt signals: editingFinished(), returnPressed(), selectionChanged(), textChanged(const QString &text), textEdited(const QString &text)
#		Qt slots: clear(), copy() const, cut(), paste(), redo(), selectAll(), setText(const QString &), undo()  
ex.	QLineEdit.returnPressed.connect(self.mel_b019) #qpushbutton b019


# .maxLength(int)  By default, this property contains a value of 32767
ex.	QLineEdit.maxLength()
ex.	QLineEdit.setMaxLength(8)


#increment/ decrement a QLineEdit
ex.	def b001(self): #decrement t000
		textfield = int(self.ui.t000.text()) #get current value
		newText = str(textfield -1) #decrement amount
		self.ui.t000.setText(newText) #set new value


# .setInputMask
#allows the user to type only one digit ranging from 0 to 9. 
#Use multiple 9's to allow the user to enter multiple numbers
ex.	QLineEdit.setInputMask("9")

#list of char arguments for setInputMask
#Use \ to escape the special characters listed above to use them as separators.
A	#ASCII alphabetic character required. A-Z, a-z.
a	#ASCII alphabetic character permitted but not required.

N	#ASCII alphanumeric character required. A-Z, a-z, 0-9.
n	#ASCII alphanumeric character permitted but not required.

9	#ASCII digit required. 0-9.
0	#ASCII digit permitted but not required.
D	#ASCII digit required. 1-9.
d	#ASCII digit permitted but not required(1-9).

#	#ASCII digit or plus/minus sign permitted but not required.

B	#Binary character required. 0-1.
b	#Binary character permitted but not required.

>	#All following alphabetic characters are uppercased.
<	#All following alphabetic characters are lowercased.
!	#Switch off case conversion.





# .setValidator, QIntValidator, QDoubleValidator
QtGui.QDoubleValidator.setRange() 
QtGui.QDoubleValidator.setBottom() #a lower bound
QtGui.QDoubleValidator.setTop() #upper bound
QtGui.QDoubleValidator.setDecimals() #limit on the number of digits after the decimal point

#QDoubleValidator(bottom, top, decimals, parent)
ex.	QLineEdit.setValidator(QtGui.QIntValidator(0, 100))
ex.	QLineEdit.setValidator(QtGui.QDoubleValidator(0, 100, 2))





# QTextEdit

#add text
text = QString('string')
#
t.append('string') 				#append text as new line
#
t.insertHtml(text)
#
t.insertPlainText(text) 		#add text

#clear text
t.clear()

t.copy()
t.cut()
t.paste()

#get text color
t.textColor()
t.textBackgroundColor()

#set text color
t.setTextColor(color)
t.setTextBackgroundColor(color)

#change text color
highlight = QtGui.QColor(128, 128, 0) #QtGui.QColor.yellow()
baseColor = t.textColor()

t.setTextColor(baseColor)
t.append(key) 					#t.append(key+str(value))
t.setTextColor(highlight)
t.insertPlainText(str(value))


#set font style
t.fontItalic()
t.fontPointSize()
t.fontUnderline()
t.fontWeight()




# QButtonGroup
# create buttonGroup
def groupButtons(self, groupName, group):
			#args: [string], [stringArray])
			#returns: 
			buttonGroup = QtWidgets.QButtonGroup(self.hb.ui)
			buttonGroup.setObjectName(groupName)

			for button in group:
				buttonGroup.addButton(button)
			return buttonGroup

def groupButtons(objectName, ui, prefix, range_):
			#([string], [object], [string], [int])
			buttonGroup = QtWidgets.QButtonGroup(ui)
			buttonGroup.setObjectName(objectName)

			for num in range(range_):
				numString = '000'[:-len(str(num))]+str(num) #remove zeros from string according to the length of the number

				button = getattr(ui, prefix+numString) #equivilent to: (self.ui.m000)
				# print button
				buttonGroup.addButton(button)
			# print buttonGroup
			return buttonGroup

#call
self.buttonGroup = groupButtons("main_buttonGroup", self.ui, "m", 10)

























'Size'#---------------------------------------------------------------------


QtWidgets.QSizePolicy				#The size policy of a widget is an expression of its willingness to be resized in various ways, and affects how the widget is treated by the layout engine.
#set
#Fixed, Minimum, Maximum, Preferred, Expanding, MinimumExpanding, Ignored
w.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding) #policyX, policyY


#get size:
#.width / .height can be derived from anything that returns a QSize
w.size()						#Returns QtCore.QSize
w.size().width()				#Returns int - width
w.size().height()				#Returns int - height
w.geometry()					#Returns QtCore.QSize - geometry of the widget as it will appear when shown as a normal(not maximized or full screen) top-level widget. #Note, the widget must be first shown for this to return something other than(0,0)
w.normalGeometry()				#Returns QtCore.QSize - geometry of the widget as it will appear when shown as a normal (not maximized or full screen) top-level widget.
w.frameSize()					#Returns QtCore.QSize - holds the size of the widget including any window frame.
w.frameGeometry()				#Returns QtCore.QSize - geometry of the widget relative to its parent including any window frame.

#get recommended widget size
w.sizeHint()
w.sizeHint().width()
w.sizeHint()

#set size:
w.resize(width, height) 		#int, int or QSize
w.setBaseSize(width, height)	#int, int or QSize - The base size is used to calculate a proper widget size if the widget defines QtWidgets.QWidget.sizeIncrement().
w.setFixedSize(width, height)	#int, int or QSize


#set in one direction
w.setFixedWidth(width)			#int or QSize
w.setFixedHeight(height)		#int or QSize 		w.setFixedHeight(w.sizeHint().height())
w.resize(w.width(), w.minimumSizeHint().height())

#resize to fit content
w.adjustSize()

#set minimum size to recommended
w.setMinimumSize(w.layout.sizeHint())
w.setMinimumWidth(w.minimumSizeHint().width())
w.setMinimumHeight(w.minimumSizeHint().height())

#set to minimum size.
w.resize(w.minimumSizeHint())
w.setFixedSize(w.sizeHint())


#get screen size
screenShape = QtWidgets.QDesktopWidget().screenGeometry()
#resize to fit screen
w.resize(w.screenShape.width(), w.screenShape.height())



#area
QtCore.QSize					#defines the size of a two-dimensional object using integer point precision.
#get
QtCore.QSize.width() 			#Returns int - width.
QtCore.QSize.height()			#Returns int - height.
#set
QtCore.QSize.setWidth(int) 		#Sets the height.	
QtCore.QSize.setHeight(int)		#Sets the width.
QtCore.QSize.scale()



QtCore.QRect 					#holds the internal geometry of the widget excluding any window frame.
#get
w.rect().size()					#Returns QSize - size of the rectangle.
w.rect().size().width()			#Returns int - rect width
w.rect().size().height()		#Returns int - rect height
w.rect().width() 				#Returns int - the width of the rectangle.
w.rect().height() 				#Returns int - the height of the rectangle.
w.rect().adjusted(x1,y1,x2,y2) 	#Returns QRect - new rectangle with x1, y1, x2, y2 added respectively to the existing coordinates of this rectangle.
w.rect().united(rect)			#Returns QRect - the bounding rectangle of this rectangle and the given rectangle. ex. combinedRect = rect1.united(rect2)
w.rect()intersect(rect) 		#Returns QRect - Use intersected(rectangle) instead.

#set
w.rect().setSize()				#QSize - Sets the size of the rectangle to the given size . The top-left corner is not moved.
w.rect().setWidth(w)			#int - Sets the width of the rectangle to the given width . The right edge is changed, but not the left one.
w.rect().setHeight(h)			#int - Sets the height of the rectangle to the given height . The bottom edge is changed, but not the top one.
w.rect()setWidth(w) 			#Sets the width of the rectangle to the given width . The right edge is changed, but not the left one.
w.rect()setHeight(h) 			#Sets the height of the rectangle to the given height . The bottom edge is changed, but not the top one.
w.rect().adjust(x1,y1,x2,y2) 	#Adds x1, y1, x2, y2 respectively to the existing coordinates of the rectangle.
w.rect()unite(rect)				#Use united(rectangle) instead. rect1.unite(rect2)



#screen size
geometry = QtWidgets.QApplication.instance().desktop().screenGeometry() #availableGeometry()
geometry.width()
geometry.height()
self.setGeometry(geometry)
#get
isFullScreen()
isMaximized()
isMinimized()
#set
showFullScreen()
showMaximized()
showMinimized()












'Position'#-----------------------------------------------------------------


QtCore.QPoint()					#Returns QPoint - (int, int) if no args given; Constructs a null point, i.e. with coordinates (0, 0)
QtCore.QPoint.setX()
QtCore.QPoint.setY()


#get
w.pos()							#Returns QPoint
w.pos().y()						#Returns int
w.mapFromParent(point)			#Returns QPoint - Parent coordinate to child coordinate.
w.mapToParent(point)			#Returns QPoint - Child coordinate to parent coordinate.
w.mapFromGlobal(point)			#Returns QPoint - Screen coordinate to widget coordinate.
w.mapToGlobal(point)			#Returns QPoint - Widget coordinate to screen coordinate. ex. mapToGlobal(QPoint(0,0)) returns: the global coordinates of the widget's top-left pixel.
w.mapFrom(widget, point)		#Returns QPoint - Widget coordinate from the coordinate system of parent, to this widget’s coordinate system. Must be a parent of the calling widget.
w.mapTo(widget, point)			#Returns QPoint - Widget coordinate to the coordinate system of parent. Must be a parent of the calling widget.

w.parentWidget().rect().center().x() #Returns int - x coord of parents center


#set
w.move(QPoint)
w.move(x, y)
w.move.y(int)




#QPoint
#get
point.x() 						#Returns the x coordinate of this point.
point.y() 						#Returns the y coordinate of this point.
point.isNull() 					#Returns Bool - True if both the x and y coordinates are set to 0
point.manhattanLength() 		#Returns QPoint - the sum of the absolute values of QPoint.x() & QPoint.y()
#set
point.setX(int)
point.setY(int)
point.toTuple()



#QRect rect()
#get
#x & y
rect.getRect() 					#Extracts the position of the rectangle’s top-left corner to *``x`` and *``y`` , and its dimensions to *``width`` and *``height`` .
rect.topLeft()#.x()				#Returns QPoint - the position of the rectangle’s top-left corner.
rect.topRight()#.y()			#Returns QPoint - the position of the rectangle’s top-right corner.
rect.bottomLeft()#.x()			#Returns QPoint - the position of the rectangle’s bottom-left corner.
rect.bottomRight()#.y()			#Returns QPoint - the position of the rectangle’s bottom-right corner.
rect.center()#.x()				#Returns QPoint - the center point of the rectangle.
rect.getCoords() 				#Extracts the position of the rectangle’s top-left corner to *``x1`` and *``y1`` , and the position of the bottom-right corner to *``x2`` and *``y2`` .
rect.united(r)					#Returns QRect - bounding rectangle of this rectangle and the given rectangle.
rect.intersected() 				#Returns QRect - the intersection of this rectangle and the given rectangle. rect1.intersected(rect2) is equivalent to rect1 & rect2.
#x
rect.x() 						#Returns int - the x-coordinate of the rectangle’s left edge. Equivalent to left()
rect.left() 					#Returns int - the x-coordinate of the rectangle’s left edge. Equivalent to x().
rect.right() 					#Returns int - the x-coordinate of the rectangle’s right edge.
#y
rect.y() 						#Returns int - the y-coordinate of the rectangle’s top edge. Equivalent to top()
rect.top() 						#Returns int - the y-coordinate of the rectangle’s top edge.
rect.bottom() 					#Returns int - the y-coordinate of the rectangle’s bottom edge.
#query
rect.contains(x, y) #or QPoint	#Returns Bool - True if the point(x , y ) is inside or on the edge of the rectangle
rect.intersects() 				#Returns Bool - True if this rectangle intersects with the given rectangle.
rect.isEmpty()					#Returns Bool - True if the rectangle is empty.
#set
rect.setRect(x, y, w, h) 		#Sets the coordinates of the rectangle’s top-left corner to(x , y ), and its size to the given width and height .
rect.setX(x) 					#Sets the left edge of the rectangle to the given x coordinate. May change the width, but will never change the right edge of the rectangle.
rect.setY(y) 					#Sets the top edge of the rectangle to the given y coordinate. May change the height, but will never change the bottom edge of the rectangle.
rect.setCoords(x1, y1, x2, y2) 	#Sets the coordinates of the rectangle’s top-left corner to(x1 , y1 ), and the coordinates of its bottom-right corner to(x2 , y2 ).
rect.translate(dx, dy) 			#Moves the rectangle dx along the x axis and dy along the y axis, relative to the current position. Positive values move the rectangle to the right and down.
rect.moveTo(x, t) 				#Moves the rectangle, leaving the top-left corner at the given position(x , y). The rectangle’s size is unchanged.




#event position
event.pos() 					#relative position to mouseEvent
event.x()
event.y()
event.globalPos()
event.globalX()
event.globalY()
event.localPos()
event.screenPos()
event.setLocalPos(localPosition)
event.windowPos()


#cursor pos
QtGui.QCursor.pos() 			#global position



#check if cursor is inside widget
w.rect().contains(w.mapFromGlobal(QtGui.QCursor.pos()))
w.geometry().contains(event.pos())
w.underMouse() 					#Returns True if the widget is under the mouse cursor; else False.


#
w.hitButton(pos)				#Returns: bool. Returns true if pos is inside the clickable button rectangle; otherwise returns false.



#screen
screenGeometry = QtWidgets.QApplication.desktop().availableGeometry().adjusted(0,0,0,-100)
screenRect = QtWidgets.QDesktopWidget().screen().rect()
screenRect = QtWidgets.QApplication.desktop().rect()












'Events'#--------------------------------------------------------------------


#custom event type
#Registers and returns a custom event type. The hint provided will be used if it is available, 
#otherwise it will return a value between QEvent.User and QEvent.MaxUser that has not yet been registered. 
#The hint is ignored if its value is not between QEvent.User and QEvent.MaxUser .
QtCore.QEvent.registerEventType([hint=-1]) #Returns: int Parameters: hint=int
#
QtWidgets.QApplication.notify(widget, event)


#QtWidgets.QApplication / QtCore.QCoreApplication
#get
QtWidgets.QApplication.hasPendingEvents() #Returns Bool - True if there are pending events. Pending events can be either from the window system or posted events using QtCore.QCoreApplication.postEvent().
QtWidgets.QApplication.postEvent(widget, event) #Adds the event, with the widget as the receiver of the event, to an event queue, and returns immediately.
ex.
focusEvent = QtGui.QFocusEvent(QtCore.QEvent.FocusIn, QtCore.Qt.OtherFocusReason)
QtWidgets.QApplication.postEvent(self.lineEdit(), focusEvent)
#set
QtWidgets.QApplication.sendEvent (widget, event) #Returns Bool(from the event hander) - Sends event event directly to receiver widget, using the PySide.QtCore.QCoreApplication.notify() function. Returns the value that was returned from the event handler.
ex.
event = QtCore.QEvent(QtCore.QEvent.Leave)
QtWidgets.QApplication.sendEvent(widget, event)



#from an event
w.exec_(event.globalPos())


event.__class__
event.__class__.__name__

event.type()
QtCore.QEvent.Show 				#QtCore.QEvent.Type.Show
QtCore.QEvent.Hide
QtCore.QEvent.Enter 			#event = QtGui.QEnterEvent(pos, pos, pos)
QtCore.QEvent.Leave
QtCore.QEvent.MouseButtonPress
QtCore.QEvent.MouseMove
QtCore.QEvent.HoverEnter
QtCore.QEvent.HoverLeave
QtCore.QEvent.Drag
QtCore.QEvent.Drop
QtCore.QEvent.key
QtCore.QEvent.KeyPress

QtGui.QKeyEvent
QtGui.QMouseEvent 				#supports mouse button presses, double-clicks, moves, and other related operations.
QtGui.QWheelEvent
QtGui.QInputEvent 				#base class for events that describe user input.
QtGui.QActionEvent 				#provides an event that is generated when a QAction is added, removed, or changed.
QtGui.QContextMenuEvent 		#contains parameters that describe a context menu event.
QtGui.QWindowStateChangeEvent 	#provides the window state before a window state change.
QtGui.QExposeEvent 				#contains event parameters for expose events.
QtGui.QFileOpenEvent 			#provides an event that will be sent when there is a request to open a file or a URL. 
QtGui.QResizeEvent 				#adds size(), oldSize() to enable widgets to discover how their dimensions have been changed.
QtGui.QFocusEvent 				#PySide.QtGui.QFocusEvent.gotFocus() #Return type: PySide.QtCore.bool




QtCore.QEvent.HoverEnter	#The mouse cursor enters a hover widget(QHoverEvent).
QtCore.QEvent.HoverLeave	#The mouse cursor leaves a hover widget(QHoverEvent).
#setMouseTracking(True) for mouse event
w.enterEvent #An event is sent to the widget when the mouse cursor enters the widget.
w.leaveEvent	#A leave event is sent to the widget when the mouse cursor leaves the widget.
w.onEnter
w.onLeave

QtCore.QEvent.MouseButtonDblClick 	#Mouse press again(QMouseEvent).
w.mouseDoubleClickEvent
ex.
def mouseDoubleClickEvent(self, event): ""

QtCore.QEvent.MouseMove 	#Mouse move(QMouseEvent).
w.mouseMoveEvent

QtCore.QEvent.MouseButtonPress 	#Mouse press(QMouseEvent).
w.mousePressEvent

QtCore.QEvent.MouseButtonRelease 	#Mouse release(QMouseEvent).
w.mouseReleaseEvent = QtGui.QMouseEvent(
							QtCore.QEvent.MouseButtonRelease,
							self.cursor().pos(),
							QtCore.Qt.LeftButton,
							QtCore.Qt.LeftButton,
							QtCore.Qt.NoModifier)

QtCore.QEvent.wheel 	#Mouse wheel rolled(QWheelEvent).




event.button()
event.buttons()
QtCore.Qt.NoButton
QtCore.Qt.LeftButton
QtCore.Qt.RightButton

event.key()
QtCore.Qt.Key_F12


QtCore.QEvent.accept() 			#indicates whether the receiver wants the event.
QtCore.QEvent.isAccepted() 		#returns bool
QtCore.QEvent.setAccepted(True) #bool
QtCore.QEvent.ignore() 			#event is propagated up the parent widget chain until a widget accepts it. (or an event filter consumes it)
QtCore.QEvent.acceptProposedAction()



event.source()
event.button()
event.buttons()
event.flags()


actionEvent(event)
changeEvent(event)

#Focus
focusInEvent(event)
.focusInEvent 					#w.focusInEvent = self.max_b010()

focusOutEvent(event)
.focusOutEvent 					#w.focusOutEvent(MaxPlus.CUI.EnableAccelerators())
focusNextPrevChild(next)


#show
showEvent(event)				#self.showEvent(offsetPos(self, offset))

#enter
enterEvent(event)
.enterEvent
.leaveEvent


#move
moveEvent(event)
.moveEvent


#size
sizeHint()
resizeEvent(event)
.resizeEvent
minimumSizeHint()
heightForWidth(arg__1)


#mouse
mouseDoubleClickEvent(event)
mouseMoveEvent(event)
mousePressEvent(event)
mouseReleaseEvent(event)
wheelEvent(event)
dragEnterEvent(event)
dragLeaveEvent(event)
dragMoveEvent(event)
dropEvent(event)


#keyboard
inputMethodEvent(event)
inputMethodQuery(arg__1)
keyPressEvent(event)
keyReleaseEvent(event)


hideEvent(event)

leaveEvent(event)

closeEvent(event)


#drag and drop
QtGui.QDragEnterEvent(pos, actions, data, buttons, modifiers)
# Parameters:
# pos – PySide.QtCore.QPoint
# actions – PySide.QtCore.Qt.DropActions
# data – PySide.QtCore.QMimeData
# buttons – PySide.QtCore.Qt.MouseButtons
# modifiers – PySide.QtCore.Qt.KeyboardModifiers


#setting MIME data:
itemData = QtCore.QByteArray()
dataStream = QtCore.QDataStream(itemData, QtCore.QIODevice.WriteOnly)
dataStream << QtCore.QByteArray(str(self.labelText)) << QtCore.QPoint(event.pos() - self.rect().topLeft())
mimeData = QtCore.QMimeData()
mimeData.setData('application/x-fridgemagnet', itemData)
mimeData.setText(self.labelText)
drag = QtGui.QDrag(self)
drag.setMimeData(mimeData)


#QDrag(placed in the 'drag' widget's mouseMoveEvent)
drag = QtGui.QDrag(self)
drag.setMimeData(QtCore.QMimeData())
drag.setHotSpot(event.pos())	# drag.setHotSpot(event.pos() - self.rect().topLeft())
drag.setDragCursor(QtGui.QCursor(QtCore.Qt.CrossCursor).pixmap(), QtCore.Qt.MoveAction) #Sets the position of the hot spot relative to the top-left corner of the pixmap used to the point specified by hotspot.
dropAction = drag.exec_(QtCore.Qt.MoveAction) #drag.start(QtCore.Qt.MoveAction)
target = drag.target() 			#the widget where the drag object was dropped. (needs to be placed after drag.exec_/drag.start)


QtCore.Qt.MoveAction
QtCore.Qt.CopyAction
QtCore.Qt.DropAction



contextMenuEvent(event)

paintEvent(event)

tabletEvent(event)





# install event filter
w.installEventFilter(self)
#install filter for widget sub object
w.view().installEventFilter(self) #viewport(), frame()




def eventFilter(self, widget, event):
	if event.type()==QtCore.QEvent.MouseButtonPress:
		pass

	# event filter return value
	#the event-filter should return True to stop any further handling, 
	#return False to pass the event on for further handling
	return Class.eventFilter(self, widget, event) #class itself.
	return QtCore.QObject.eventFilter(self, widget, event) #inherited class.  Class(QtCore.QObject):
	return QtWidgets.QComboBox.mouseMoveEvent(self, event) #inherited class.  Class(QtWidgets.QComboBox):
	return QtWidgets.QToolButton.showMenu(self)
	return super(Class, self).eventFilter(widget, event) #class or inherited class.
	return self.__class__.__base__.setText(self, text)
	super().showPopup() #from builtins import super (python 3's super behavior)
	super(QMenu_, self).hide()
	super(QtWidgets.QToolButton).showMenu()



# Remove event filter ------------------------------------------------------

w.removeEventFilter() #Removes an event filter object obj from this object. 
#The request is ignored if such an event filter has not been installed.
#All event filters for this object are automatically removed when this object is destroyed.
#It is always safe to remove an event filter.






#QtTest simulated keyboard/mouse events
from PySide2.QtTest import QTest
QTest.mouseRelease(self, QtCore.Qt.RightButton)
self.blockSignals(True)
QTest.mousePress(self, QtCore.Qt.RightButton)
self.blockSignals(False)









# Re-implementation of QApplication.notify in Python which would propagate custom events.
class MyApp(QApplication):
	def notify(self, widget, event):
		if event.type() > QtCore.QEvent.User:
			while(widget):
				# Note that this calls `event` method directly thus bypassing
				# calling qApplications and receivers event filters
				res = widget.event(event);
				if res and event.isAccepted():
					return res
				widget = widget.parent()
		return super(MyApp, self).notify(receiver, event)
# And instead of using instance of QApplication we use instance of our subclass.
if __name__=='__main__':
	app = MyApp(sys.argv)









'Mouse Event'#--------------------------------------------------------------

#mouse/keyboard
w.setWindowFlags(QtCore.Qt.<flag1>|QtCore.Qt.<flag2>)

w.setAttribute(QtCore.Qt.WA_Hover) #Forces Qt to generate paint events when the mouse enters or leaves the widget.
w.setAttribute(QtCore.Qt.WA_UnderMouse) #Indicates that the widget is under the mouse cursor.
w.setAttribute(QtCore.Qt.WA_NoMouseReplay) #Used for pop-up widgets. Indicates that the most recent mouse press event should not be replayed when the pop-up widget closes.
w.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents) #disables the delivery of mouse events to the widget and its children.
w.setAttribute(QtCore.Qt.WA_NoMousePropagation) #mouse events will not be propagated further up the parent widget chain.

#get state of attribute:
w.testAttribute(QtCore.Qt.WA_MouseTracking) #returns bool #Indicates if the widget has mouse tracking enabled.


# Mouse tracking
w.mouseTracking() 				#bool, default: disabled,
w.hasMouseTracking()
w.setMouseTracking(True) 		#triggers the mouseMove event for all mouse movements rather then only when button is pressed.

#set mouse tracking for child widgets:
def setMouseTracking(self, flag):
	def recursive_set(parent):
		for child in parent.findChildren(QtCore.QObject):
			try:
				child.setMouseTracking(flag)
			except:
				pass
			recursive_set(child)

	QtWidgets.w.setMouseTracking(self, flag)
	recursive_set(self)
w.setMouseTracking(True) 		#enables the delivery of mouse events to the widget's children. default: False.


# Mouse move
event.type() == QtCore.QEvent.MouseMove


# Mouse button
mouseButtons = QApplication.mouseButtons() #ex. if bool(mouseButtons == QtCore.Qt.LeftButton):

class PySide.QtGui.QMouseEvent(type, pos, globalPos, button, buttons, modifiers)
# Parameters:
# type – PySide.QtCore.QEvent.Type
# pos – PySide.QtCore.QPoint
# globalPos – PySide.QtCore.QPoint
# button – PySide.QtCore.Qt.MouseButton
# buttons – PySide.QtCore.Qt.MouseButtons
# modifiers – PySide.QtCore.Qt.KeyboardModifiers
ex.
if(QtGui.QMouseEvent.button == QtCore.Qt.RightButton):
# QtCore.Qt.MiddleButton
# QtCore.Qt.LeftButton

# middle mouse button event
ex.
if event.buttons() & QtCore.Qt.MiddleButton:
# Left Button event with control key
ex.
if event.buttons() & QtCore.Qt.LeftButton and event.modifiers() & QtCore.Qt.ControlModifier:


QApplication.setDoubleClickInterval(int) #the time limit that distinguishes a double click from two consecutive mouse clicks. default: 400 milliseconds.






# Call grabMouse on a widget and only that widget will receive mouse events(mouseMoves etc.), 
# the same applies for grabKeyboard. This means that the other widgets from your application will 
# not get any mouse/keyboard event until you call the corresponding release function.
QWidget.grabKeyBoard() #http://qt-project.org/doc/qt-5/qwidget.html#grabKeyboard
QWidget.releaseKeyBoard() #http://qt-project.org/doc/qt-5/qwidget.html#releaseKeyboard
QWidget.mouseGrabber() #Returns the widget that is currently grabbing the mouse input. else: None 
QWidget.releaseMouse() #Releases the mouse grab.

QtCore.QEvent.UngrabMouse




# mouseMoveEvent Override:
ex.
def mouseMoveEvent(self, event):
	super(ToolBar, self).mousePressEvent(event) #ToolBar = parent class
	if event.buttons() == QtCore.Qt.NoButton:
		print("Simple mouse motion")
	elif event.buttons() == QtCore.Qt.LeftButton:
		print("Left click drag")
	elif event.buttons() == QtCore.Qt.RightButton:
		print("Right click drag")

# mousePressEvent Override:
ex.
def mousePressEvent(self, event):
	super(ToolBar, self).mousePressEvent(event) #ToolBar = parent class
	if event.button() == QtCore.Qt.LeftButton:
		print("Press!")
	



QtTest.QTest.mouseRelease(widget, button[, stateKey=0[, pos=QPoint()[, delay=-1]]])
# Parameters:	
# widget – PySide.QtGui.QWidget
# button – PySide.QtCore.Qt.MouseButton
# stateKey – PySide.QtCore.Qt.KeyboardModifiers
# pos – PySide.QtCore.QPoint
# delay – PySide.QtCore.int





#mask mouse events
def settingMask(self):
	region = qg.QRegion(self._mainWidget.frameGeometry())
	region -= qg.QRegion(self._mainWidget.geometry())
	region += self._mainWidget.childrenRegion()
	self._mainWidget.setMask(region)





















'Keyboard Event'#-----------------------------------------------------------


w.setAttribute(QtCore.Qt.WA_InputMethodTransparent) #
w.setAttribute(QtCore.Qt.WindowTransparentForInput) #
w.setAttribute(QtCore.Qt.WA_KeyboardFocusChange) #Set on a toplevel window when the users changes focus with the keyboard(tab, backtab, or shortcut).


setFocusPolicy( Qt::NoFocus );


# keyboard Codes:
# https://doc.qt.io/archives/qtjambi-4.5.2_01/com/trolltech/qt/core/Qt.Key.html
ex. QtCore.Qt.Key_Z


#repainting(key auto repeating)
event.isAutoRepeat()
QApplication.setKeyboardInputInterval(int) #the time limit that distinguishes a key press from two consecutive key presses. default: 400 milliseconds.


Qt::Key
#key names used by Qt
#http://doc.qt.io/archives/qt-4.8/qt.html#Key-enum


QtGui.QKeyEvent
#Return type:	PySide.QtCore.int
#query keyboard event.  Returns the code of the key that was pressed or released.
# Returns the code of the key that was pressed or released.
ex. QtGui.QKeyEvent.key == QtCore.Qt.Key_Z

# Parameters:	key – PySide.QtGui.QKeySequence.StandardKey
# Return type:	PySide.QtCore.bool
ex. QtGui.QKeyEvent.matches(key)



QtGui.QKeySequence()



w.keyPressEvent() #key press event under a window class
event.key() == QtCore.Qt.Key_X



w.keyReleaseEvent()
event.key() == QtCore.Qt.Key_X





#modifiers:
modifiers = QApplication.keyboardModifiers() #ex. (bool(modifiers == QtCore.Qt.ControlModifier)):




QShortcut Class
#used to create keyboard shortcuts.
ex.
def shortcutActivated(shortcut):
	shortcut.setEnabled(0)
	e = QtGui.QKeyEvent(QEvent.KeyPress, Qt.Key_H, Qt.CTRL)
	QCoreApplication.postEvent(theMainApplicationQtWindowInstance, e)
	mel.evalDeferred(partial(shortcut.setEnabled, 1)) #functools.partial

def initShortcut():
	shortcut = QtGui.QShortcut(QKeySequence(Qt.CTRL + Qt.Key_H), theMainApplicationQtWindowInstance)
	shortcut.setContext(Qt.ApplicationShortcut)
	shortcut.activated.connect(partial(shortcutActivated, shortcut))

ex.#new syntax
self.s000 = QtWidgets.QShortcut(QtGui.QKeySequence(QtCore.Qt.Key_L), self)
self.s000.activated.connect(self.xkeyisdown)












'Paint Event'#--------------------------------------------------------------

	def paintEvent(self, event):
		#args: [QEvent]
		if any ([self.hotBox.name=="main", self.hotBox.name=="viewport"]):
			self.raise_()
			self.setWindowFlags(QtCore.Qt.WA_TransparentForMouseEvents)

			#Initialize painter
			painter = QtGui.QPainter(self)
			pen = QtGui.QPen(QtGui.QColor(115, 115, 115), 3, QtCore.Qt.SolidLine, QtCore.Qt.RoundCap, QtCore.Qt.RoundJoin)
			painter.setPen(pen)
			painter.setRenderHint(QtGui.QPainter.Antialiasing, True)
			painter.setBrush(QtGui.QColor(115, 115, 115))
			painter.drawEllipse(self.hotBox.point, 5, 5)

			#perform paint
			if self.hotBox.mousePosition:
				mouseX = self.hotBox.mousePosition.x()
				mouseY = self.hotBox.mousePosition.y()
				line = QtCore.QLine(mouseX, mouseY, self.hotBox.point.x(), self.hotBox.point.y())
				painter.drawLine(line)
				painter.drawEllipse(mouseX-5, mouseY-5, 10, 10)



painter = QtGui.QPainter(self)
painter.fillRect(self.rect(), QtGui.QColor(80, 80, 255, 128))





















'Signals'#------------------------------------------------------------------


# *Class Must inherit QObject for signals
signal = QtCore.Signal(bool) 	#create a signal. #The Signal class provides a way to declare and connect Qt signals in a pythonic way.
signal = QtCore.Signal((int,), (str,))
#assign signal a value. must be defined as class variable(before class init)
updated = Signal(int)
updated = Signal(str)
updated = Signal(object)
#emit signal
signal.emit(*args) 				#args is the arguments to pass to any connected slots.

#connect
signal.connect(method)			#Create a connection between this signal and a receiver, the receiver can be a Python callable, a Slot or a Signal.
signal[str].connect(method)		#if ex. 'int' is the default, specify str when connecting the second signal.
#disconnect
signal.disconnect(method)		#Disconnect this signal from a receiver, the receiver can be a Python callable, a Slot or a Signal.
#all
eg. disconnect(w,0,0,0)			#supported args: (QtCore.QMetaObject.Connection)(QtCore.QObject, str, Callable)(str, Callable)(QtCore.QObject, str=None)(QtCore.QObject, QtCore.QMetaMethod, QtCore.QObject, QtCore.QMetaMethod)(QtCore.QObject, str, QtCore.QObject, str)(str, QtCore.QObject, str)
eg. w.disconnect()				#throws a TypeError exception if no signals are present.



#subClass for method overriding
ex.
class HoverArea(QtWidgets.QPushButton):
	mouseHover = QtCore.Signal(bool)

	def __init__(self, parent=None):
		QtWidgets.QPushButton.__init__(self)
		self.setMouseTracking(True)

	def enterEvent(self, event):
		self.mouseHover.emit(True)

	def leaveEvent(self, event):
		self.mouseHover.emit(False)

HoverArea(pushButton).mouseHover.connect(method)




#using lambda function
w.clicked.connect(lambda: overlay.setVisible(not overlay.isVisible()))
#using functools.partial
#from functools import partial
w.clicked.connect(partial(function, arg))
#
w.clicked.connect(partial(self.function, arg=arg['name']))




#emit a signal
signal = QtCore.Signal()
signal.connect(<method>)
signal.emit()


#from PySide.QtCore import QObject, Signal, Slot
class PunchingBag(QObject):
	punched = QtCore.Signal()

	QObject.__init__(self) #Initialize the PunchingBag as a QObject

	def punch(self):
		self.punched.emit()






#block a signal
ex.
w.blockSignals(True)
w.blockSignals(False)

















'Drag and Drop'#------------------------------------------------------------

ex.
class FileEdit(QLineEdit):
def __init__( self, parent ):
	super(FileEdit, self).__init__(parent)

	self.setDragEnabled(True)

def dragEnterEvent( self, event ):
	data = event.mimeData()
	urls = data.urls()
	if ( urls and urls[0].scheme() == 'file' ):
		event.acceptProposedAction()

def dragMoveEvent( self, event ):
	data = event.mimeData()
	urls = data.urls()
	if ( urls and urls[0].scheme() == 'file' ):
		event.acceptProposedAction()

def dropEvent( self, event ):
	data = event.mimeData()
	urls = data.urls()
	if ( urls and urls[0].scheme() == 'file' ):
		# for some reason, this doubles up the intro slash
		filepath = str(urls[0].path())[1:]
		self.setText(filepath)
















'Creating and checking for instances'#--------------------------------------

# Keep a reference to the RigControlWindow instance as a private attribute of 
#the main window.
ex.
class MainWindow(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		self._rcwin = None

		if self._rcwin is None:
			self._rcwin.show()

#or use a property:
ex.
class MainWindow(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		self._rcwin = None

	@property
	def rcwin(self):
		if self._rcwin is None:
			self._rcwin = RigControlWindow()
		return self._rcwin

	def showRigControlWindow(self):
		self.rcwin.show()

# or use a function in a module:
ex.
def startGui():
	if 'myWindows' in globals():
		global myWindows
		myWindows.show()
	else:
		global myWindows
		myWindows = init_gui.MainWindow(parent=init_gui.MyMainWindow())
		myWindows.show()
And then call startGui from a shelf script like this:

if __name__ == '__main__':
	startGui()







'Properties'#----------------------------------------------------------------


#set property
color = QtCore.Property(QtGui.QColor, self.getColor, self.setColor) #gettr /settr
#python equivalent
mainAppWindow = property(getMainAppWindow, setMainAppWindow)








'Heirarchy'#-----------------------------------------------------------------


#set parent:
child.setParent(parent)
#
button = QtWidgets.QPushButton('ButtonName', parent=widget)


#get parent:
child.parent()
#
child.parentWidget()
#parent window
child.window()
#
[w for w in QApplication.topLevelWidgets()]
#
customClassInst = self.parent()
while customClassInst is not None and not isinstance(customClassInst, CustomClass):
	customClassInst = customClassInst.parent()



#get child objects:
parent.children() 				#returns [QtCore.Qbject at 0x10xxxxxx]
#
centralwidget.children()
#get specific
checkbox = parent.findChild(QtWidgets.QCheckBox, 'checkBoxEnabled') #pass a type (or tuple of types) as the first argument, and an optional string as the second argument (for matching the objectName).
#all of type
lineEdits = form.findChildren(QtGui.QLineEdit) #pass a type (or tuple of types) as the first argument, and an optional string as the second argument (for matching the objectName).



#get an attribute from a parent object anywhere in the hierarchy.
p = <widget>.parent()
while not hasattr(p.window(), 'attr'): #p or p.window() depending on the circumstances.
	p = p.parent()
attr = p.window().attr














'Time'#----------------------------------------------------------------------

_timer = QtCore.QTimer()

#call a slot after a specified interval:
QtCore.QTimer.singleShot(0, lambda: self.setFocus()) #QTimer with a timeout of 0 will time out as soon as all the events in the window system's event queue have been processed.


#set interval
timer = QtCore.QTimer()
timer.setInterval(1000.0 / 25)  #25 times per second
timer.timeout.connect(<function>)
timer.start()
# timer.stop()  				#Call this to stop printing


















'Dynamic Ui'#----------------------------------------------------------------


layout.count()
layout.rowCount()
layout.columnCount()




#get widgets from layout:
widgets = (layout.itemAt(i).widget() for i in range(layout.count()))
items = (layout.itemAt(i) for i in range(layout.count()))

#get widgets from dynamic ui:
#from a dict
for widgetName, widgetObject in ui.__dict__.iteritems(): #for each object in the ui:
#
ui.__dict__.items()
#from a list
for widget in ui.children():




# Promoting a widget in designer to use a custom class:
# >	In Qt Designer, select all the widgets you want to replace, 
# 		then right-click them and select 'Promote to...'. 

# >	In the dialog:
# 		Base Class:		Class from which you inherit. ie. QWidget
# 		Promoted Class:	Name of the class. ie. "MyWidget"
# 		Header File:	Path of the file (changing the extension .py to .h)  ie. myfolder.mymodule.mywidget.h

# >	Then click "Add", "Promote", 
# 		and you will see the class change from "QWidget" to "MyWidget" in the Object Inspector pane.

# register the custom widget
# When loading the ui file:
	from myfolder.mymodule import MyWidget
	uiLoader = QUiLoader()
	uiLoader.registerCustomWidget(MyWidget)
	main_window = uiLoader.load(file)
#or:
# dynamically register (assuming module name and class name are identical)
widgetPath = os.path.join(os.path.dirname(__file__), 'widgets')
for m in os.listdir(widgetPath):
	m = m.rstrip('.pyc') #get module name from file name
	c = 'widgets.'+m+'.'+m
	uiLoader.registerCustomWidget(locate(c))
# one liner with list comprehension:
[uiLoader.registerCustomWidget(locate('widgets.'+m +'.'+m)) for m in [file_.rstrip('.py') for file_ in os.listdir(widgetPath) if file_.endswith('.py')]]




#Converting the ui file
#Using compileUi:
ex.
from pyside2uic import compileUi

#Open output .py file for writing
output_path = os.expandvars("%CLOUD%/____Graphics/Maya/scripts/_Python/_Python_startup/Maya_CustomTools_Ui.py")
python_file = open(output_path, 'w')
#Read input .ui file
input_path = os.expandvars("%CLOUD%/____Graphics/Maya/scripts/Qt/Maya_CustomTools_Ui.ui")
compileUi(input_path, python_file, False, 4, False)
python_file.close()



#using QUiLoader:
ex.
def getQtui(name):
		#arg: string
		#returns: dynamic ui object
		uiPath = "ui/"+name+".ui"
		uiFile = os.path.expandvars(uiPath)
		qtui = QUiLoader().load(uiFile)
		return qtui

ex.
def getQtui(name):
	#args: [string]
	#return: [dynamic ui]
	uiPath = os.path.expandvars("%CLOUD%/____Graphics/Maya/Scripts/Qt/tk_maya_ui/tk_"+name+".ui")
	qtui = QUiLoader().load(uiPath)
	print uiPath; return qtui


ex.
uiList=[]
for file_ in os.listdir(path):
	if file_.endswith('.ui'):
		f = QtCore.QFile(path+'/'+file_)
		f.open(QFile.ReadOnly)
		uiList.append([file_.replace('.ui',''), QUiLoader().load(f)])
		f.close()

ex.
#set path to the directory containing the ui files.
path = os.path.join(os.path.dirname(__file__), 'ui') #get absolute path from dir of this module + relative path to directory
#construct the uiList from directory contents. ie. [['polygons', <polygons dynamic ui object>]]
qApp = QApplication(sys.argv)
uiList = [QUiLoader().load(path+'/'+file_) for file_ in os.listdir(path) if file_.endswith('.ui')]








'External Files'#------------------------------------------------------------

#QFileDialog
fileDialog = QtWidgets.QFileDialog()
directory = fileDialog.getExistingDirectory()









'Parent Applications'#-------------------------------------------------------


#get main window instance
#3ds max:
#mainWindow = GetQMaxWindow() --old
GetQmaxMainWindow()

#mayaDockableMixin


#maya
maya.OpenMayaUI.MQtUtil.findControl()
# Parenting to maya main window:
from maya import OpenMayaUI as omui
from shiboken2 import wrapInstance
applicationWindow = omui.MQtUtil.mainWindow()
if applicationWindow is not None:
	applicationWindow = wrapInstance(long(applicationWindow), QtGui.QWidget) #requires wrapertype as a second argument, so you can pass QWidget as a second argument
#or
for obj in QtWidgets.qApp.topLevelWidgets(): #qApp or QApplication
	if obj.objectName() == 'MayaWindow'
		applicationWindow = obj

# Parenting to max main window:
applicationWindow = QtGui.QWidget(MaxPlus.GetQMaxWindow())
_GCProtector.widgets.append(applicationWindow) #append to garbage collector

# docking to maya main window
#http://help.autodesk.com/view/MAYAUL/2015/ENU/?guid=__files_GUID_66ADA1FF_3E0F_469C_84C7_74CEB36D42EC_htm








'Style'#--------------------------------------------------------------------

# Predefined QColor objects (Qt namespace (ie. Qt::red)):
white
black
red
darkRed
green
darkGreen
blue
darkBlue
cyan
darkCyan
magenta
darkMagenta
yellow
darkYellow
gray
darkGray
lightGray
color0 (zero pixel value) (transparent, i.e. background)
color1 (non-zero pixel value) (opaque, i.e. foreground)
transparent


ex.
QtGui.QColor.magenta()

ex.
QtGui.QColor(122, 163, 39)

ex.
QtGui.QColor.alpha #get alpha int value
QtGui.QColor.setAlpha(2)


ex.
w.setForeground(0, QtGui.QBrush(QtGui.QColor("red")))

self.autoFillBackground()


#flags
.setWindowFlags(QtCore.Qt.flag1|QtCore.Qt.flag2) #syntax: QtCore.Qt.<flag> | separated by pipes.

CustomizeWindowHint
QtCore.Qt.Tool
QtCore.Qt.FramelessWindowHint
QtCore.Qt.X11BypassWindowManagerHint
QtCore.Qt.WindowStaysOnTopHint

w.setAttribute(QtCore.Qt.WA_WState_WindowOpacitySet)
w.setAttribute(QtCore.Qt.WA_NoSystemBackground) #Indicates that the widget has no background
w.setAttribute(QtCore.Qt.WA_TranslucentBackground) #Indicates that the widget should have a translucent background
w.setAttribute(QtCore.Qt.WA_TintedBackground)
w.setAttribute(QtCore.Qt.WA_StyledBackground) #Indicates the widget should be drawn using a styled background.
w.setAttribute(QtCore.Qt.WA_StyleSheet) #Indicates that the widget is styled using a style sheet.
w.setAttribute(QtCore.Qt.WA_WindowPropagation) #Makes a toplevel window inherit font and palette from its parent.
w.setAttribute(QtCore.Qt.AA_UseStyleSheetPropagationInWidgetStyles, True) #font and palette propagate to child widgets.
w.setAttribute(QtCore.Qt.WA_SetPalette) #Indicates that the widget has a palette of its own.
w.setAttribute(QtCore.Qt.WA_SetStyle) #Indicates that the widget has a style of its own.
w.setAttribute(QtCore.Qt.WA_SetFont) #Indicates that the widget has a font of its own.


ex.
w.setWindowOpacity(0.5)

ex.
w.setAutoFillBackground(False)
w.autoFillBackground(True)



#get color:
w.palette().color(QtGui.QPalette.Background).name() #returns '#edecec' which is obviously not white. So Background is the wrong color role to query for this widget. Instead, it looks like Base might be more appropriate:
w.palette().color(QtGui.QPalette.Base).name() #returns '#ffffff'

color = w.palette().color(w.backgroundRole())
color = w.palette().color(QtGui.QPalette.Background) #alt method
rgba = color.red(), color.green(), color.blue(), color.alpha()

w.palette().setColor(QtGui.QPalette.Active, QtGui.QPalette.Text, background)



# style
w.setStyle(QtWidgets.QStyleFactory.create("plastique"))

ex. #setting styles from a comboBox
list_ = QtGui.QStyleFactory.keys() #get styles from QStyleFactory
style = cmb.findText(QtGui.qApp.style().objectName(), QtCore.Qt.MatchFixedString)
QtGui.qApp.setStyle(style)


# styleSheet
# docs: http://doc.qt.io/archives/qt-4.8/stylesheet-examples.html
w.styleSheet() #query the widgets style sheet.
print w.styleSheet() #print the stylesheet if there is one:





ex.
w.setStyleSheet('') 			#set style sheet to default. also(styleSheet())
w.setStyleSheet("background: transparent;") #doesn't need the style sheet itself but child widgets contained in the widget that have autoFillBackground()==True by default should have it unset or should have set QtCore.Qt.WA_TranslucentBackground or have a transparent background color set by a style sheet which is then inherited
#comment css/qss
	/* multi-line */

# setting property:
	qApp.setStyleSheet("QLineEdit#name[prop=true] {background-color:transparent;}") #does't effect the lineEdit with objectName 'name' if that buttons property 'styleSheet' is false (c++ lowercase). 
	w.setProperty('prop', True) #set the widget property.

# gradient:
	'background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #E0E0E0, stop: 1 #FFFFFF);'

# multiple widgets:
	'QComboBox:!editable, QComboBox::drop-down:editable { ... }'






#Cursor
w.setAttribute(QtCore.Qt.WA_SetCursor #Indicates that the widget has a cursor of its own.

#Set Cursor:
w.setCursor(QtGui.QCursor(QtCore.Qt.BitmapCursor))

#Cursor Shape:
QtCore.Qt.CursorShape(2) #get cursor using int value

#cursor object 				#value	#name 			#description
QtCore.Qt.BlankCursor		10		''				#typically used when the cursor shape needs to be hidden.
QtCore.Qt.ArrowCursor 		0		'left_ptr'		#The standard arrow cursor.
QtCore.Qt.UpArrowCursor		1		'up_arrow'		#An arrow pointing upwards toward the top of the screen.
QtCore.Qt.CrossCursor		2		'cross'			#typically used to help the user accurately select a point on the screen.
QtCore.Qt.WaitCursor		3		'wait'			#usually shown during operations that prevent the user from interacting with the application.
QtCore.Qt.IBeamCursor		4		'ibeam'			#indicating that a widget can accept and display text input.
QtCore.Qt.SizeVerCursor		5		'size_ver'		#A cursor used for elements that are used to vertically resize top-level windows.
QtCore.Qt.SizeHorCursor		6		'size_hor'		#A cursor used for elements that are used to horizontally resize top-level windows.
QtCore.Qt.SizeBDiagCursor	7		'size_bdiag'	#A cursor used for elements that are used to diagonally resize top-level windows at their top-right and bottom-left corners.
QtCore.Qt.SizeFDiagCursor	8		'size_fdiag'	#A cursor used for elements that are used to diagonally resize top-level windows at their top-left and bottom-right corners.
QtCore.Qt.SizeAllCursor		9		'size_all'		#A cursor used for elements that are used to resize top-level windows in any direction.
QtCore.Qt.SplitVCursor		11		'split_v'		#A cursor used for vertical splitters, indicating that a handle can be dragged horizontally to adjust the use of available space.
QtCore.Qt.SplitHCursor		12		'split_h'		#A cursor used for horizontal splitters, indicating that a handle can be dragged vertically to adjust the use of available space.
QtCore.Qt.PointingHandCursor13		'pointing_hand'	#A pointing hand cursor that is typically used for clickable elements such as hyperlinks.
QtCore.Qt.ForbiddenCursor	14		'forbidden'		#A slashed circle cursor, typicallyusedduringdraganddropoperationstoindicatethatdraggedcontentcannotbedroppedonparticularwidgetsorinsidecertainregions.
QtCore.Qt.OpenHandCursor	17		'openhand'		#A cursor representing an openhand, typicallyusedtoindicatethattheareaunderthecursoristhevisiblepartofacanvasthattheusercanclickanddraginordertoscrollaround.
QtCore.Qt.ClosedHandCursor	18		'closedhand'	#A cursor representing a closed hand, typically used to indicate that a dragging operation is in progress that involves scrolling.
QtCore.Qt.WhatsThisCursor	15		'whats_this'	#An arrow with a question mark, typically used to indicate the presence of 'WhatsThis' help for a widget.
QtCore.Qt.BusyCursor		16		'left_ptr_watch'#An hourglass or watch cursor, usually shown during operations that allow the user to interact with the application while they are performed in the background.
QtCore.Qt.DragMoveCursor	20		'move'			#A cursor that is usually used when dragging an item.
QtCore.Qt.DragCopyCursor	19		'copy'			#A cursor that is usually used when dragging an item to copy it.
QtCore.Qt.DragLinkCursor	21		'link'			#A cursor that is usually used when dragging an item to make a link to it.
QtCore.Qt.BitmapCursor		24









'Exit'#----------------------------------------------------------------------


#terminate the event-loop (if it's running)
QCoreApplication.quit()
QCoreApplication.exit(0)


#terminate the program
sys.exit()



















'Errors'#--------------------------------------------------------------------


QtCore.QDebug('')



#DEBUG
class MainWindow(QtWidgets.QMainWindow):
	testSignal = QtCore.Signal()

def __init__(self, parent=None, **kwargs):
	super(MainWindow, self).__init__(parent, **kwargs)
	self.testSignal.connect(self.debug)

def debug(self, *args, **kwargs):
	print("got", args, "and", kwargs)






# RuntimeError: A QApplication instance already exists.
#there is already a PySide application running, so get a handle for that object like this:
app = QtGui.QApplication.instance()


## AttributeError: 'PySide2.QtCore.Signal' object has no attribute 'emit'
#define signal as a class variable before init
ex.
class Button(QtCore.QObject):
	mouseHover = QtCore.Signal(bool)
#now in can be referenced in later methods as self.mousHover.emit(True/False)





# install
#python wheels: (download and install locally to make sure the correct wheel gets installed)
http://download.qt.io/snapshots/ci/pyside/



