#				|||||||||||||||||||||||||||||||||||||||||||
#				||||||||||		Qt UI Notes		|||||||||||
#				!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!






QtCore		# core non-graphical classes used by other modules
QtGui		# base classes for UI components
QtWidgets	# classes to extend qt GUI with c++ widgets
QObject		# basic non-visual building block. signals, events,
#Additional: QtCharts, QtMultimedia, QtNetwork, QtQuick, QtTest,













'Widgets: '#------------------------------------------------------------------



#QApplication:
#The difference between QtWidgets.QApplication.instance() and QtWidgets.qApp is that the latter is a static module variable that must be created when the module is first imported. 
#This results in the following initially baffling behaviour:
inst = QtWidgets.QApplication.instance()
qapp = QtWidgets.qApp #qApp is initially just an empty wrapper. #Once the QApplication is created, though, they will both point to the same thing:
>>> (inst, qapp)
(None, <PyQt5.QtWidgets.QApplication object at 0x7ff3c8bd3948>)
#So even though no QApplication object has been created yet, the qApp variable still points to a QApplication instance. 
#If modules were more like classes, so that they could have dynamic properties, it would be possible for qApp to work exactly like QApplication.instance() does and initially return None. 
#But because it is static, it must always return an object of the correct type, so that it can later refer to the same underlying C++ object as QApplication.instance().



# Find item in QApplication by only the objectname:
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





#get main window instance
#3ds max:
#mainWindow = GetQMaxWindow() --old
GetQmaxMainWindow()

#mayaDockableMixin





#get object name
name = w.objectName()


#get widget type:
w.__class__.__name__ #returns class name as a string
#alt using QMetaObject:
w.metaObject().className()
#alt using type():
type(widget)
type(widget).__name__ #same as: w.__class__



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

w.isEnabled	#bool

w.isVisible	#bool
w.isHidden	#bool
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

w.clearFocus()
w.hasFocus()
w.setFocus()
w.clearFocus()

w.activateWindow() #Sets the top-level widget containing this widget to be a top-level window that has keyboard input focus.


#shedule refresh 
w.update()









#Remove widget
for i in reversed(range(self.layout.count())): 
	widgetToRemove = self.layout.itemAt(i).widget()
	# remove it from the layout list
	self.layout.removeWidget(widgetToRemove)
	# remove it from the gui
	widgetToRemove.setParent(None)





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
w.setAttribute(WA_WState_Created)
w.setAttribute(WA_WState_Hidden)
w.setAttribute(WA_WState_Visible)
w.setAttribute(WA_WState_ExplicitShowHide)

#disable/close events
w.setAttribute(WA_DeleteOnClose) #Makes Qt delete this widget when the widget has accepted the close event
w.setAttribute(WA_Disabled) #Indicates that the widget is disabled
w.setAttribute(WA_ForceDisabled) #Indicates that the widget is explicitly disabled
w.setAttribute(WA_QuitOnClose) #Makes Qt quit the application when the last widget with the attribute set has accepted closeEvent().
#
w.setAttribute(WA_DontShowOnScreen)
w.setAttribute(WA_ShowWithoutActivating) #Show the widget without making it active.

#add/remove events
w.setAttribute(WA_NoChildEventsForParent) #Indicates that the widget does not want ChildAdded or ChildRemoved events sent to its parent.
w.setAttribute(WA_NoChildEventsFromChildren) #Indicates that the widget does not want to receive ChildAdded or ChildRemoved events sent from its children.


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




# Visual style



# QPushButton signals.  QtUi QPushButton signal in
#Qt signals:
clicked()
pressed()
released()
toggled()
setText()
setIcon()
#public slots: setChecked(bool), toggle()

#connect to multiple slots:
map(self.dial.valueChanged.connect, [self.spinbox.setValue, self.getValue_dial])
#or
[self.dial.valueChanged.connect(x) for x in [self.spinbox.setValue, self.getValue_dial]]
#alternatively you could connect to one method and use that to call various others.


#enable/ disable button objects
b.setEnabled(False) #either method serves both functions. must be used with an argument
b.setDisabled(True)

b.setDefault #QPushButton.setDefault() #Sets the button as default

#hide/ unhide objects
b.setVisible(False)
#query visible state
b.isHidden()


b.click() #emits clicked signal

b.clicked() #bool checked=False #QPushButton.clicked()
b.clicked.connect(method)
#or with arguments
b.clicked.connect(lambda x=arg: method(x))
b.clicked.connect(lambda: method(x))

b.pressed() #bool #QPushButton.pressed()
b.released() #bool #QPushButton.released()

b.toggled() #bool. query pushbutton toggle state.
b.toggle() #Toggles the state of a checkable button.




#check state
#		QtUi checkable button signal input
#		self.ui.connect(HandleSelection, SIGNAL(toggled(bool)),MEL_HandleSelection,SLOT(setVisible(bool)));
#		QObject::connect(moreButton, SIGNAL(toggled(bool)), tertiarypb7Box, SLOT(setVisible(bool)));

b.stateChanged() #QCheckBox.stateChanged()
b.stateChanged.connect(method)



b.setCheckable(True) #Recognizes pressed and released states of button if set to true

b.isChecked() #QPushButton.isChecked()
# Returns Boolean state of button
b.isChecked()
#setChecked
b.setChecked(True)


#button text
b.text #QPushButton.text() #Retrieves buttons’ caption or textfields value
b.setText #QPushButton.setText() #Programmatically sets buttons’ caption or textfields value
b.setText(0, 'text '+str(num)) #append integer
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
s.setMinimum(-5) #Sets the lower bound of counter
s.setMaximum(5) #Sets the upper bound of counter
s.setRange(0,10) #Sets the minimum, maximum and step value
s.setWrapping(s) #Set whether spin box is circular. Both bounds must be set for this to have an effect.
s.singleStep() #gets the step value of counter
s.setSingleStep(1) #Sets the step value.
s.setValue(2) #set value
s.value() #Get the current value
s.cleanText() #get the current value excluding any prefix or suffix
s.setPrefix("") #Set a string prefix.
s.setSuffix("") #Set the string suffix appended to the spinbox text.
s.text() #gets prefix/suffix string value

QSpinbox.valueChanged.connect(method)




#QComboBox
#get list contents:
#set contents
cmb.addItem(string, userData=None) #string/data
cmb.addItems(list_) #string/data
cmb.insertItem(index, string, userData=None) #at index
cmb.insertItems(index, list_)
cmb.setItemData(index, value) #data
#get contents
cmb.findText(text) #get index using string
cmb.itemText(index) #get string using index
cmb.itemData(index) #data
cmb.findData(data) #data
#set index
cmb.setCurrentIndex(0)
#get index
cmb.currentText() #get current text


# remove
cmb.removeItem(index)

#edit line
cmb.lineEdit(): #Returns the line edit used to edit items in the combobox, or 0 if there is no line edit.
cmb.setLineEdit(edit) #Sets the line edit to use instead of the current line edit widget.

#block signals

#separator
cmb.insertSeparator(index)

#expand/collapse
cmb.hidePopup()
cmb.showPopup()

#remove contents
cmb.clear()

# get list contents:
list_ = [cmb.itemText(i) for i in range(cmb.count())]
components = pm.ls(selection=1, flatten=1)
cmb.addItems(components)

# add string
cmb.addItem(component)

# add signals:
comboboxes = ['cmb000']
for cmb in comboboxes:
	method = getattr(class_, cmb)
	ui = getattr(ui, cmb)
	ui.currentIndexChanged.connect(method)
	ui.activated.connect(method)
	method() #init comboboxes

#additional signals:
cmb.activated.connect(method)
QComboBox.activated(int).connect() #index of the selected item
QComboBox.activated(unicode).connect() #[str] text of selected item
highlighted() #index of the selected item
highlighted(index) #[str] text of selected item
currentIndexChanged()
currentIndexChanged(index)
editTextChanged()

#eventFilter for button press #see also eventFilter for view event
QComboBox.installEventFilter(self)
def eventFilter(self,target,event):
	if target==self.cmb and event.type()==QtCore.QEvent.MouseButtonPress:
		print "Button press"

#get/set data
cmb = QtGui.QComboBox()
cmb.addItem( 'description', my_data ) # set description, set data
print cmb.currentText() # get description
print cmb.itemData( cmb.currentIndex() ) # get data






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
print item.text() # get description
print item.data( QtCore.Qt.UserRole ) # get data






# QTreeWidget
#get/set data
tree_widget = QtGui.QTreeWidget()
item = QtGui.QTreeWidgetItem( tree_widget, ['description'] ) # set description
item.setData(1, QtCore.Qt.EditRole, my_data) # set data
item.setData(2, QtCore.Qt.EditRole, my_data) # set data
item.setData(3, QtCore.Qt.EditRole, my_data) # set data
print item.text(0) # get description
print item.text(1) # get data
print item.text(2) # get data
print item.text(3) # get data





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
t.append('string') #append text as new line
#
t.insertHtml(text)
#
t.insertPlainText(text) #add text

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
t.append(key) #t.append(key+str(value))
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


# get size:
w..width = self.ui.frameGeometry().width()
w..height = self.ui.frameGeometry().height()

#for widget:
mainWindow = QtGui.QWidget()
width = w.frameGeometry().width()
height = w.frameGeometry().height()
#for screen:
mainWindow = QtGui.QWidget()
screenShape = QtGui.QDesktopWidget().screenGeometry()


# set size:
QtCore.QSize.setWidth() 
QtCore.QSize.setHeight()

#resize
w.resize(100,30)
w.resize(w*2,h*2)
w.resize(w//2,h//2)
w.resize(width, height) #window size

#shrink the window to minimum size.
w.resize(minimumSizeHint())
w.setFixedSize(w.sizeHint())

# If you want to only shrink in height, then you can do something like:
w.resize(w.width(), w.minimumSizeHint().height())

#automaticly resize to fit content
w.adjustSize()

#resize to fit screen
w.resize(w.screenShape.width(), w.screenShape.height())

# get recommended widget size
w.sizeHint
w.setMinimumSize(w.layout.sizeHint())


ui.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)		


# overload sizeHint:
def sizeHint(self):
	return QtCore.QSize(15, 15)



w.geometry()

#holds the geometry of the widget as it will appear when shown as a normal(not maximized or full screen) top-level widget.
#Note, the widget must be first shown for this to return something other than(0,0)
w.normalGeometry(). 



















'Position'#-----------------------------------------------------------------

# Position
.offsetPos
w.offsetPos(offset)


#move
w.move(<QPoint>)
w.move(15,15)
w.move.y(15)


#center of widget
w.rect().center()
#relative to its parent
w.mapToParent(c)
#relative to the screen
w.mapToGlobal(c)


#x coord of parents center
w.parentWidget().rect().center().x()

#QPoint
point.isNull() #Returns true if both the x and y coordinates are set to 0
point.manhattanLength() #Returns the sum of the absolute values of QPoint.x() & QPoint.y()
point.setX(x)
point.setY(y)
point.toTuple()
point.x() #Returns the x coordinate of this point.
point.y() #Returns the y coordinate of this point.


#QRect
rect.x() #Returns the x-coordinate of the rectangle’s left edge. Equivalent to left()
rect.y() #Returns the y-coordinate of the rectangle’s top edge. Equivalent to top()
rect.setX(x) #Sets the left edge of the rectangle to the given x coordinate. May change the width, but will never change the right edge of the rectangle.
rect.setY(y) #Sets the top edge of the rectangle to the given y coordinate. May change the height, but will never change the bottom edge of the rectangle.
rect.size() #Returns the size of the rectangle.
rect.setSize(s) #Sets the size of the rectangle to the given size . The top-left corner is not moved.
rect.width() #Returns the width of the rectangle.
rect.setWidth(w) #Sets the width of the rectangle to the given width . The right edge is changed, but not the left one.
rect.height() #Returns the height of the rectangle.
rect.setHeight(h) #Sets the height of the rectangle to the given height . The bottom edge is changed, but not the top one.
rect.top() #Returns the y-coordinate of the rectangle’s top edge.
rect.topLeft() #Returns the position of the rectangle’s top-left corner.
rect.topRight() #Returns the position of the rectangle’s top-right corner.
rect.bottom() #Returns the y-coordinate of the rectangle’s bottom edge.
rect.bottomLeft() #Returns the position of the rectangle’s bottom-left corner.
rect.bottomRight() #Returns the position of the rectangle’s bottom-right corner.
rect.left() #Returns the x-coordinate of the rectangle’s left edge. Equivalent to x().
rect.right() #Returns the x-coordinate of the rectangle’s right edge.
rect.center() #Returns the center point of the rectangle.
rect.getRect() #Extracts the position of the rectangle’s top-left corner to *``x`` and *``y`` , and its dimensions to *``width`` and *``height`` .
rect.setRect(x, y, w, h) ##Sets the coordinates of the rectangle’s top-left corner to(x , y ), and its size to the given width and height .
rect.getCoords() #Extracts the position of the rectangle’s top-left corner to *``x1`` and *``y1`` , and the position of the bottom-right corner to *``x2`` and *``y2`` .
rect.setCoords(x1, y1, x2, y2) #Sets the coordinates of the rectangle’s top-left corner to(x1 , y1 ), and the coordinates of its bottom-right corner to(x2 , y2 ).
rect.contains(x, y) #or QPoint. Returns true if the point(x , y ) is inside or on the edge of the rectangle
rect.intersects() #Returns true if this rectangle intersects with the given rectangle.
rect.intersect() #Use intersected(rectangle ) instead.
rect.intersected() #Returns the intersection of this rectangle and the given rectangle . Note that r.intersected(s) is equivalent to r & s .
rect.adjust(x1, y1, x2, y2) #Adds dx1 , dy1 , dx2 and dy2 respectively to the existing coordinates of the rectangle.
rect.translate(dx, dy) #Moves the rectangle dx along the x axis and dy along the y axis, relative to the current position. Positive values move the rectangle to the right and down.
rect.moveTo(x, t) #Moves the rectangle, leaving the top-left corner at the given position(x , y ). The rectangle’s size is unchanged.
rect.isEmpty() #Returns true if the rectangle is empty.




#event position
event.pos() #relative position to mouseEvent
event.x()
event.y()
event.globalPos()
event.globalX()
event.globalY()
event.localPos()
event.screenPos()
event.setLocalPos(localPosition)
event.windowPos()


#cursor
QtGui.QCursor.pos() #global position

w.pos()
w.mapFromGlobal(point)
w.mapFrom(widget, point)
w.mapTo(widget, point)
w.mapFromParent(point)
w.mapToParent(point)

#check if cursor is inside widget
w.rect().contains(w.mapFromGlobal(QtGui.QCursor.pos()))
w.geometry().contains(event.pos())
w.underMouse() #Returns True if the widget is under the mouse cursor; else False.



#
w.hitButton(pos) #Returns: bool. Returns true if pos is inside the clickable button rectangle; otherwise returns false.
















'Events'#--------------------------------------------------------------------



QtCore.QEvent.accept() #indicates whether the receiver wants the event.
QtCore.QEvent.isAccepted() #returns bool
QtCore.QEvent.setAccepted(True) #bool
QtCore.QEvent.ignore() #event is propagated up the parent widget chain until a widget accepts it. (or an event filter consumes it)


w.setAttribute(QtCore.Qt.WA_NoMousePropagation) #event will not be propagated further up the parent widget chain.



event.source()
event.button()
event.buttons()
event.flags()


actionEvent(event)
changeEvent(event)


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


#Focus
focusInEvent(event)
focusNextPrevChild(next)
focusOutEvent(event)

QtGui.QFocusEvent #PySide.QtGui.QFocusEvent.gotFocus() #Return type: PySide.QtCore.bool

.focusInEvent #w.focusInEvent()
.focusOutEvent #w.focusOutEvent

w.focusInEvent = self.max_b010()
w.focusOutEvent(MaxPlus.CUI.EnableAccelerators())


setVisible(visible)

showEvent(event)
self.showEvent(offsetPos(self, offset))


QtCore.QEvent.HoverMove

ex.
if event.type() == QtCore.QEvent.HoverEnter:
ex.
if event.type() == QtCore.QEvent.Type.Enter:


enterEvent(event)
.enterEvent
.leaveEvent


hideEvent(event)

leaveEvent(event)

closeEvent(event)


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
drag.setHotSpot(event.pos()) # drag.setHotSpot(event.pos() - self.rect().topLeft())
drag.setDragCursor(QtGui.QCursor(QtCore.Qt.CrossCursor).pixmap(), QtCore.Qt.MoveAction) #Sets the position of the hot spot relative to the top-left corner of the pixmap used to the point specified by hotspot.
dropAction = drag.exec_(QtCore.Qt.MoveAction) #drag.start(QtCore.Qt.MoveAction)
target = drag.target() #the widget where the drag object was dropped. (needs to be placed after drag.exec_/drag.start)


QtCore.Qt.MoveAction
QtCore.Qt.CopyAction
QtCore.Qt.DropAction



contextMenuEvent(event)


paintEvent(event)


tabletEvent(event)





#custom event filter:

# install filter
QtGui.qApp.installEventFilter(self)
buttonObject.installEventFilter(self.hotBox) 

# return value
return QtWidgets.w.eventFilter(self, button, event)
return super(HotBox, self).eventFilter(self, event) #returns the event that occurred




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




#custom event type:
#Parameters: hint=int
#Registers and returns a custom event type.
#The hint provided will be used if it is available, 
#otherwise it will return a value between QEvent.User and QEvent.MaxUser that has not yet been registered. 
#The hint is ignored if its value is not between QEvent.User and QEvent.MaxUser .
QtCore.QEvent.registerEventType([hint=-1]) #returns: int


#Send event directly to receiver widget;
event = QtGui.QEnterEvent(pos, pos, pos)
QtWidgets.QApplication.sendEvent(widget, event) #Returns the value that was returned from the event handler.

#
event = QtCore.QEvent(QtCore.QEvent.Leave)
QtWidgets.QApplication.sendEvent(widget, event)







'Mouse Event'#--------------------------------------------------------------

#mouse move
event.type() == QtCore.QEvent.MouseMove


# Mouse button
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




w.mouseTracking #bool, default: distabled,
# Access functions:
w.hasMouseTracking
w.setMouseTracking(True) #triggers the mouseMove event for all mouse movements rather then only when button is pressed.

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

			
	



QtCore.QEvent.HoverEnter	#The mouse cursor enters a hover widget(QHoverEvent).
QtCore.QEvent.HoverLeave	#The mouse cursor leaves a hover widget(QHoverEvent).
#setMouseTracking(True) for mouse event
w.enterEvent #An event is sent to the widget when the mouse cursor enters the widget.
w.leaveEvent	#A leave event is sent to the widget when the mouse cursor leaves the widget.
w.onEnter
w.onLeave

QtCore.QEvent.MouseButtonDblClick 	#Mouse press again(QMouseEvent).

.mouseDoubleClickEvent
ex.
def mouseDoubleClickEvent(self, event):
	print "mouseDoubleClickEvent"

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

QtCore.QEvent.Type.MouseButtonRelease
QtCore.QEvent.Type.UngrabMouse
QtCore.QEvent.wheel 	#Mouse wheel rolled(QWheelEvent).




# Call grabMouse on a widget and only that widget will receive mouse events(mouseMoves etc.), 
# the same applies for grabKeyboard. This means that the other widgets from your application will 
# not get any mouse/keyboard event until you call the corresponding release function.
QWidget.grabKeyBoard() #http://qt-project.org/doc/qt-5/qwidget.html#grabKeyboard
QWidget.releaseKeyBoard() #http://qt-project.org/doc/qt-5/qwidget.html#releaseKeyboard
QWidget.mouseGrabber() #Returns the widget that is currently grabbing the mouse input. else: None 
QWidget.releaseMouse() #Releases the mouse grab.






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



#mouse/keyboard
w.setWindowFlags(QtCore.Qt.flag1|QtCore.Qt.flag2)

w.setAttribute(QtCore.Qt.WA_Hover) #Forces Qt to generate paint events when the mouse enters or leaves the widget.
w.setAttribute(QtCore.Qt.WA_UnderMouse) #Indicates that the widget is under the mouse cursor.
w.setAttribute(QtCore.Qt.WA_NoMouseReplay) #Used for pop-up widgets. Indicates that the most recent mouse press event should not be replayed when the pop-up widget closes.
w.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents) #disables the delivery of mouse events to the widget and its children

#get state of attribute:
w.testAttribute(QtCore.Qt.WA_MouseTracking) #returns bool #Indicates if the widget has mouse tracking enabled.



#mask mouse events
def settingMask(self):
    region = qg.QRegion(self._mainWidget.frameGeometry())
    region -= qg.QRegion(self._mainWidget.geometry())
    region += self._mainWidget.childrenRegion()
    self._mainWidget.setMask(region)
# Also, on my system(Linux), I found I had to call this after the window is shown:
    ...
    myWinPos.show()
    myWinPos.settingMask()
    sys.exit(qtApp.exec_())





















'Keyboard Event'#-----------------------------------------------------------


w.setAttribute(QtCore.Qt.WA_InputMethodTransparent)
w.setAttribute(QtCore.Qt.WA_KeyboardFocusChange) #Set on a toplevel window when the users changes focus with the keyboard(tab, backtab, or shortcut).




setFocusPolicy( Qt::NoFocus );


# keyboard Codes:
# https://doc.qt.io/archives/qtjambi-4.5.2_01/com/trolltech/qt/core/Qt.Key.html
ex.
QtCore.Qt.Key_Z



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

def xkeyisdown:
	print "x key is down"

ex.#old syntax
QtCore.QObject.connect(QtGui.QShortcut(QtGui.QKeySequence(QtCore.Qt.Key_Escape), self.Dialog), QtCore.SIGNAL('activated()'), self.Dialog.close)
ex.#or
self.connect(QtGui.QShortcut(QtGui.QKeySequence(QtCore.Qt.Key_Escape), self), QtCore.SIGNAL('activated()'), self.down)

def down(self): 
	print 'escape key down'



#repainting(key auto repeating)
if event.isAutoRepeat():
	return



Qt::Key
#key names used by Qt
#http://doc.qt.io/archives/qt-4.8/qt.html#Key-enum


QtGui.QKeyEvent
#Return type:	PySide.QtCore.int
#query keyboard event.  Returns the code of the key that was pressed or released.
# Returns the code of the key that was pressed or released.
ex.
if QtGui.QKeyEvent.key == QtCore.Qt.Key_Z:

# Parameters:	key – PySide.QtGui.QKeySequence.StandardKey
# Return type:	PySide.QtCore.bool
ex.
QtGui.QKeyEvent.matches(key)



QtGui.QKeySequence()



w.keyPressEvent() #key press event under a window class
ex.
def keyPressEvent(self, event):
	if event.key() == QtCore.Qt.Key_X:
		self.X_dn()
	if event.key() == QtCore.Qt.Key_Y:
		self.Y_dn()

def X_dn(self):
	print "x Down"
#or possibly:
self.keyPressEvent(self.X_dn, QtCore.Qt.Key_X) #(command/function, event)



w.keyReleaseEvent()
ex.
def keyReleaseEvent(self, event):
	if event.key() == QtCore.Qt.Key_X:
		self.X_up()
	if event.key() == QtCore.Qt.Key_Y:
		self.Y_up()

def X_up(self):
	print "x Up"


# ----------------------------------------------


# eventFilter
#the event-filter should return True to stop any further handling, 
#return False to pass the event on for further handling

# Install EventFilter on component :
self.ui.buttonGroup.installEventFilter(self)      
# NOT self.ui.buttonGroup.installEventFilter(self.ui)

# Define eventFilter():
def eventFilter(self, obj, event):
	if(obj.objectName() == "group_of_widgets"):
		if event.type() == QtCore.QEvent.Type.Enter:
			self.drop_action(event)


ex.
self.ui.tree_widget_of_items.installEventFilter(self)

	if e.type() == QEvent.DragEnter: #remember to accept the enter event
		e.acceptProposedAction()
		return True
	if e.type() == QEvent.Drop:
		# handle the event
		# ...
		return True
	return False #remember to return false for other event types
#or
self.ui.tree_widget_of_items.installEventFilter(self)

def eventFilter(self, o, e):
if(o.objectName() == "tree_widget_of_items"):
    if e.type() == QtCore.QEvent.Type.Enter:
        self.drop_action(e)


ex.
class MainWindow(QMainWindow):
	def __init__(self):
	    self.textEdit = QTextEdit()
	    setCentralWidget(self.textEdit)
	    textEdit.installEventFilter(self)

	    if obj == textEdit:
	        if event.type() == QEvent.KeyPress:
	            keyEvent = event
	            print "Ate key press", keyEvent.key()
	            return true
	        else:
	            return false
	    else:
	        # pass the event on to the parent class
	        return QMainWindow.eventFilter(self, obj, event)



#another eventFilter example with mouse events
ex.
def eventFilter(self, source, event):
	if event.type() == QtCore.QEvent.MouseMove:
		if event.buttons() == QtCore.Qt.NoButton:
			print("Simple mouse motion")
		elif event.buttons() == QtCore.Qt.LeftButton:
			print("Left click drag")
		elif event.buttons() == QtCore.Qt.RightButton:
			print("Right click drag")
	elif event.type() == QtCore.QEvent.MouseButtonPress:
		if event.button() == QtCore.Qt.LeftButton:
			print("Press!")
	return super(Window, self).eventFilter(source, event)
#then install filter in widget
self.graphicsView.viewport().installEventFilter(self)


#Here’s a KeyPressEater class that eats the key presses of its monitored objects:
ex.
class KeyPressEater(QObject):
    def eventFilter(self, obj, event):
        if event.type() == QEvent.KeyPress:
            print "Ate key press", event.key()
            return True
        else:
            # standard event processing
            return QObject.eventFilter(self, obj, event)

#And here’s how to install it on two widgets:
keyPressEater = KeyPressEater(self)
pushButton = QPushButton(self)
listView = QListView(self)

pushButton.installEventFilter(keyPressEater)
listView.installEventFilter(keyPressEater)



#working example
ex.
w.installEventFilter(self)

#filter for mouse over event
ex.
# class HoverEnterFilter(QtCore.QObject):
class HoverEnterFilter(QtWidgets.QWidget):
	def eventFilter(self, obj, event):
		if event.type() == QtCore.QEvent.HoverEnter:
			print "-HoverEnter"
			# return QtCore.QObject.eventFilter(self, obj, event)
			return True
		else:
			return False

w.installEventFilter(HoverEnterFilter(self))


#subClass for method overriding
ex.
class HoverArea(QtWidgets.QPushButton):
	mouseHover = QtCore.Signal(bool)

	def __init__(self, parent=None):
		QtWidgets.QPushButton.__init__(self, parent)
		self.setMouseTracking(True)
		self.resize(61,23)

	def enterEvent(self, event):
		self.mouseHover.emit(True)

	def leaveEvent(self, event):
		self.mouseHover.emit(False)

HoverArea(pushButton).mouseHover.connect(method)



#QComboBox view event signal
class ShowEventFilter(QtCore.QObject):
	def eventFilter(self, filteredObj, event):
		if event.type() == QtCore.QEvent.Show:
			print "Popup Showed !"
			# do whatever you want
		return QtCore.QObject.eventFilter(self, filteredObj, event)

eventFilter = ShowEventFilter()
cb.view().installEventFilter(eventFilter)














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
#findsignals


# assign signal a value. must be defined as class variable(before class init)
updated = Signal(int)
updated = Signal(str)
updated = Signal(object)


# create a signal
enterEvent = QtCore.Signal(bool)


def enterEvent(self, event):
	self.enterEvent.emit(True)

def leaveEvent(self, event):
	self.enterEvent.emit(False)


#call function with argument from signal
#using lambda function
w.clicked.connect(lambda: self.overlay.setVisible(False) if self.overlay.isVisible() else self.overlay.setVisible(True))
#using functools.partial
#from functools import partial
w.clicked.connect(partial(function, arg))
#
w.clicked.connect(partial(self.function, arg=arg['name']))



# emit a simple signal
#from PySide.QtCore import QObject, Signal, Slot

class PunchingBag(QObject):
    ''' Represents a punching bag; when you punch it, it
        emits a signal that indicates that it was punched. '''
    punched = Signal()
 
        # Initialize the PunchingBag as a QObject
        QObject.__init__(self)
 
    def punch(self):
        ''' Punch the bag '''
        self.punched.emit()


#emit a signal
#from PySide import QtGui, QtCore

class Communicate(QtCore.QObject):
    
    closeApp = QtCore.Signal()

class Example(QtGui.QMainWindow):
    
        super(Example, self).__init__()
        
        self.initUI()
        
    def initUI(self):      

        self.c = Communicate()
        self.c.closeApp.connect(self.close)       
        
        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Emit signal')
        self.show()
        
    def mousePressEvent(self, event):
        
        self.c.closeApp.emit()
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


    main()



#block a signal
ex.
cmb.blockSignals(True)
cmb.blockSignals(False)

















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

















'Heirarchy'#-----------------------------------------------------------------


#set parent:
child.setParent(parent)
#
button = QtWidgets.QPushButton('ButtonName', parent=widget)


#get child objects:
parent.children() #returns [QtCore.Qbject at 0x10xxxxxx]
#
centralwidget.children()
#get specific
checkbox = parent.findChild(QtWidgets.QCheckBox, 'checkBoxEnabled')









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













'Time'#----------------------------------------------------------------------

_timer = QtCore.QTimer()



#set interval
timer = QtCore.QTimer()
timer.setInterval(1000.0 / 25)  #25 times per second
timer.timeout.connect(<function>)
timer.start()
# timer.stop()  # Call this to stop printing


















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

#from a list
for widget in ui.children():




# Promote a widget in designer to use a custom class:
#>	In Qt Designer, select all the line-edits you want to replace, then right-click them and select "Promote to...". 
#>	In the dialog, set "Promoted class name" to "LineEdit", and set "Header file" to the python import path for the module that contains this class (e.g. myapp.LineEdit).
#>	Then click "Add", and "Promote", and you will see the class change from "QLineEdit" to "LineEdit" in the Object Inspector pane.

# Now when you re-generate your ui module with pyuic, you should see that it uses your custom LineEdit class and there will be an extra line at the bottom of the file like this:
# from myapp.LineEdit import LineEdit





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






















'External Applications'#-----------------------------------------------------

#maya
pm.lsUI (
numWidgets(nw)	#[boolean,create]  Reports the number of QT widgets used by Maya.
dumpWidgets(dw)	#[boolean,create]  Dump all QT widgets used by Maya.
)


















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
QtCore.Qt.WindowTransparentForInput
QtCore.Qt.WindowStaysOnTopHint

WA_WState_WindowOpacitySet
WA_NoSystemBackground #Indicates that the widget has no background
WA_TranslucentBackground #Indicates that the widget should have a translucent background
WA_TintedBackground
WA_StyledBackground #Indicates the widget should be drawn using a styled background.
WA_StyleSheet #Indicates that the widget is styled using a style sheet.
WA_WindowPropagation #Makes a toplevel window inherit font and palette from its parent.
WA_SetPalette #Indicates that the widget has a palette of its own.
WA_SetStyle #Indicates that the widget has a style of its own.
WA_SetFont #Indicates that the widget has a font of its own.


ex.
w.setWindowOpacity(0.5)

ex.
w.setAutoFillBackground(False)
w.autoFillBackground(True)


#erase area \fill with background
w.fillRect(rectangle, background())



# style
w.setStyle(QtWidgets.QStyleFactory.create("plastique"))



# styleSheet
# docs: http://doc.qt.io/archives/qt-4.8/stylesheet-examples.html
#print the stylesheet if there is one:
print self.pushButton.styleSheet()

#w.styleSheet
pushButton.styleSheet #query the widgets style sheet.

#If you would prefer that the font and palette propagate to child widgets, you can set the Qt::AA_UseStyleSheetPropagationInWidgetStyles flag, like this:
QCoreApplication::setAttribute(Qt::AA_UseStyleSheetPropagationInWidgetStyles, true);


ex.
buttonObject.setStyleSheet("") ##set style sheet to default. also(styleSheet())
self.setStyleSheet("background: transparent;") #doesn't need the style sheet itself but child widgets contained in the widget that have autoFillBackground()==True by default should have it unset or should have set QtCore.Qt.WA_TranslucentBackground or have a transparent background color set by a style sheet which is then inherited
pushButton.setStyleSheet("background-color: transparent") #white, black, grey, magenta, etc
setStyleSheet("background-color: rgba(227, 227, 227, 2)") #rgb + alpha. alpha value of 1 sometimes doesnt work.


ex.
.setStyleSheet("QToolTip { color: #ffffff; background-color: #2a82da; border: 1px solid white; }");
.setStyleSheet("QLabel {font-size: 100px; opacity:0.5}")

#comment css
/* css multi-line comment */





buttonObject.setStyleSheet("") ##set style sheet to default. also(styleSheet())


w.setStyleSheet('''QPushButton {
}''')


.setStyleSheet("QToolTip { color: #ffffff; background-color: #2a82da; border: 1px solid white; }");

	QTreeWidget {border:none;} 
	QTreeWidget::item {height: 20px;}
	QTreeView {
  }






#Cursor
WA_SetCursor #Indicates that the widget has a cursor of its own.

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







