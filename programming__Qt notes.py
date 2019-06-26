set#				|||||||||||||||||||||||||||||||||||||||||||







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
rect.setRect(x, y, w, h) ##Sets the coordinates of the rectangle’s top-left corner to (x , y ), and its size to the given width and height .
rect.getCoords() #Extracts the position of the rectangle’s top-left corner to *``x1`` and *``y1`` , and the position of the bottom-right corner to *``x2`` and *``y2`` .
rect.setCoords(x1, y1, x2, y2) #Sets the coordinates of the rectangle’s top-left corner to (x1 , y1 ), and the coordinates of its bottom-right corner to (x2 , y2 ).
rect.contains(x, y) #or QPoint. Returns true if the point (x , y ) is inside or on the edge of the rectangle
rect.intersects() #Returns true if this rectangle intersects with the given rectangle.
rect.intersect() #Use intersected(rectangle ) instead.
rect.intersected() #Returns the intersection of this rectangle and the given rectangle . Note that r.intersected(s) is equivalent to r & s .
rect.adjust(x1, y1, x2, y2) #Adds dx1 , dy1 , dx2 and dy2 respectively to the existing coordinates of the rectangle.
rect.translate(dx, dy) #Moves the rectangle dx along the x axis and dy along the y axis, relative to the current position. Positive values move the rectangle to the right and down.
rect.moveTo(x, t) #Moves the rectangle, leaving the top-left corner at the given position (x , y ). The rectangle’s size is unchanged.
rect.isEmpty() #Returns true if the rectangle is empty.








'Widgets: general'#------------------------------------------------------------------



QtGui.QApplication.allWidgets()

QtGui.QApplication..topLevelWidgets()
ex. widgets = dict((w.objectName(), w) for w in QtGui.QApplication.topLevelWidgets())
	window = widgets['MayaWindow']










act = QtGui.QAction("Action", self, triggered=self.on_triggered)

act = QtGui.QAction("Action", self)


































































.pressed #bool #QPushButton.pressed()


btn.click() #emits clicked signal

.clicked #bool #QPushButton.clicked()
self.ui.button.clicked.connect(self.methodToConnectTo)


.released #bool #QPushButton.released()

w.toggled() #bool. query pushbutton toggle state.

w.toggle() #Toggles the state of a checkable button.



















# Retrieves buttons’ caption or textfield value


# Programmatically sets buttons’ caption or textfield value







#get list contents:
#set contents
cmb.addItem(string, userData=None) #string/data
cmb.addItems(list_) #string/data
cmb.insertItem(index, string, userData=None) #at index
cmb.insertItems(index, list_)
cmb.setItemData(index, value) #data
#get contents
cmb.findText(text) #using string
#get index
cmb.currentText() #current text
#set index
cmb.setCurrentIndex(0)
cmb.itemText(index) #text using index
cmb.itemData(index) #data
cmb.findData(data) #data
# remove
cmb.removeItem (index)

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



QComboBox.itemText(index) #Returns the text for the given index in the combobox.



















box = QtGui.QMessageBox()






  


































minimumSizeHint ()
sizeHint ()


self.setAttribute(QtCore.Qt.WA_NoChildEventsForParent)







self.ui.b010.focusInEvent = self.max_b010()







if event.type() == QtCore.QEvent.HoverEnter:
if event.type() == QtCore.QEvent.Type.Enter:





















#mouse move
event.type() == QtCore.QEvent.MouseMove







.setMouseTracking(True) #triggers the mouseMove event for all mouse movements rather then only when button is pressed.
















# Cursor position
self.mousePosition = event.pos() #relative position to mouseEvent
self.mousePosition = QtGui.QCursor.pos() #global position

w.pos() #widget positon
w.mapFromGlobal(point)
w.mapFrom(widget, point)
w.mapTo(widget, point)
w.mapFromParent(point)
w.mapToParent(point)

#check if cursor is inside widget
w.rect().contains(w.mapFromGlobal(QtGui.QCursor.pos()))

#
w.hitButton(pos) #Returns: bool. Returns true if pos is inside the clickable button rectangle; otherwise returns false.




	










self.setAttribute(QtCore.Qt.WA_Hover) #Forces Qt to generate paint events when the mouse enters or leaves the widget.
self.setAttribute(QtCore.Qt.WA_UnderMouse) #Indicates that the widget is under the mouse cursor.
self.setAttribute(QtCore.Qt.WA_NoMouseReplay) #Used for pop-up widgets. Indicates that the most recent mouse press event should not be replayed when the pop-up widget closes.
self.setAttribute(QtCore.Qt.WA_MouseTracking) #Indicates that the widget has mouse tracking enabled.
self.setAttribute(QtCore.Qt.WA_NoMousePropagation)
self.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents) #disables the delivery of mouse events to the widget and its children


#mask mouse events
def settingMask(self):
    region = qg.QRegion(self._mainWidget.frameGeometry())
    region -= qg.QRegion(self._mainWidget.geometry())
    region += self._mainWidget.childrenRegion()
    self._mainWidget.setMask(region)
# Also, on my system (Linux), I found I had to call this after the window is shown:
    ...
    myWinPos.show()
    myWinPos.settingMask()
    sys.exit(qtApp.exec_())



#QtTest simulated keyboard/mouse events
from PySide2.QtTest import QTest
QTest.mouseRelease(self, QtCore.Qt.RightButton)
self.blockSignals(True)
QTest.mousePress(self, QtCore.Qt.RightButton)
self.blockSignals(False)















self.setAttribute(QtCore.Qt.WA_InputMethodTransparent)
self.setAttribute(QtCore.Qt.WA_KeyboardFocusChange) #Set on a toplevel window when the users changes focus with the keyboard (tab, backtab, or shortcut).


































# install event filter ----------------------------------------------







	if e.type() == QEvent.DragEnter: #remember to accept the enter event
self.ui.tree_widget_of_items.installEventFilter(self)



	    self.textEdit = QTextEdit()

	    if obj == textEdit:
























# Remove event filter ------------------------------------------------------

self.ui.cmb002.removeEventFilter() #Removes an event filter object obj from this object. 
#The request is ignored if such an event filter has not been installed.
#All event filters for this object are automatically removed when this object is destroyed.
#It is always safe to remove an event filter.



















	self.enterEvent.emit(True)

	self.enterEvent.emit(False)






 
        # Initialize the PunchingBag as a QObject
 



    

    
        super(Example, self).__init__()
        
        

        
        
        
        
    


    main()









class FileEdit(QLineEdit):













        self._rcwin.show()

class MainWindow(QMainWindow):

        if self._rcwin is None:










parent = QtCore.QObject()





button = QtGui.QPushButton("ButtonName", parent=widget)












#set interval
timer = QtCore.QTimer()
timer.setInterval(1000.0 / 25)  #25 times per second
timer.timeout.connect(<function>)
timer.start()
# timer.stop()  # Call this to stop printing































def getQtui(name):






































maya qt menus





menu3

















menuItem228

























#				|||||||||||||||||||||||||||||||||||||||||||
#				||||||||||		Qt UI Notes		|||||||||||
#				!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!



QtCore		#core non-graphical classes used by other modules
QtGui			#base classes for UI components
QtWidgets #classes to extend qt GUI with c++ widgets

#Additional: QtCharts, QtMultimedia, QtNetwork, QtQuick, QtTest,

QObject		#basic non-visual building block. ex. signals, events, 







QtGui.QColor(122, 163, 39)

QtGui.QColor.alpha #get alpha int value


widget.setForeground(0,QtGui.QBrush(QtGui.QColor("red")))







setWindowOpacity(0.5)

setAutoFillBackground(False)










buttonObject.setStyleSheet("") ##set style sheet to default. also (styleSheet())


button.setStyleSheet('''QPushButton {
}''')


.setStyleSheet("QToolTip { color: #ffffff; background-color: #2a82da; border: 1px solid white; }");

	QTreeWidget {border:none;} 
	QTreeWidget::item {height: 20px;}
	QTreeView {
  }

STYLESHEET = '''
	    background-color: #ABABAB; /* sets background of the menu */
	    border: 1px solid black;

	    /* sets background of menu item. set this to something non-transparent
	        if you want menu color and menu item color to be different */
	    background-color: transparent;

	QMenu::item:selected { /* when user selects item using mouse or keyboard */
	    background-color: #654321;
	For a more advanced customization, use a style sheet as follows:

	QMenu {
	    background-color: white;
	    margin: 2px; /* some spacing around the menu */

	QMenu::item {
	    padding: 2px 25px 2px 20px;
	    border: 1px solid transparent; /* reserve space for selection border */

	QMenu::item:selected {
	    border-color: darkblue;
	    background: rgba(100, 100, 100, 150);
	}

	QMenu::icon:checked { /* appearance of a 'checked' icon */
	    background: gray;
	    border: 1px inset gray;
	    position: absolute;
	    top: 1px;
	    right: 1px;
	    bottom: 1px;
	    left: 1px;
	}'''



'Size'#---------------------------------------------------------------------

# Size

QWidget.adjustSize()

QtCore.QSize.setWidth() 
QtCore.QSize.setHeight()



# get size
self.width = self.ui.frameGeometry().width()
self.height = self.ui.frameGeometry().height()

#for widget:
mainWindow = QtGui.QWidget()
width = mainWindow.frameGeometry().width()
height = mainWindow.frameGeometry().height()
#for screen:
mainWindow = QtGui.QWidget()
screenShape = QtGui.QDesktopWidget().screenGeometry()



#shrink the window to minimum size.
self.resize(minimumSizeHint())

# If you want to only shrink in height, then you can do something like:
self.resize(width(), minimumSizeHint().height())

#automaticly resize to fit content
self.adjustSize()

#resize to fit screen
mainWindow.resize(self.screenShape.width(), self.screenShape.height())

# get recommended widget size
QWidget.sizeHint
self.setMinimumSize(self.layout.sizeHint())


#resize a specific amount
.resize
button.resize(100,30)
button.resize(w*2,h*2)
button.resize(w//2,h//2)
self.resize(self.width, self.height) #window size


# overload sizeHint:
def sizeHint(self):
	return QtCore.QSize(15, 15)



.geometry

#holds the geometry of the widget as it will appear when shown as a normal (not maximized or full screen) top-level widget.
#Note, the widget must be first shown for this to return something other than (0,0)
QWidget.normalGeometry(). 




'Position'#-----------------------------------------------------------------

# Position

.offsetPos
self.offsetPos(offset)


# bring front - send back
self.ui.raise_
self.ui.lower()




'Widget general'#------------------------------------------------------------------



# get object name
ex. name = button.objectName()


#get widget type:
ex. widget.__class__.__name__ #returns class name as a string
#alt using QMetaObject:
ex. widget.metaObject().className()
#alt using type():
ex. type(widget)
ex. type(widget).__name__ #same as: widget.__class__



# Toggle
widget.setVisible(not widget.isVisible()) 




#the following three fragments are equivalent:
act = QtGui.QAction("Action", self)
act.triggered.connect(self.on_triggered)

act = QtGui.QAction("Action", self, triggered=self.on_triggered)

act = QtGui.QAction("Action", self)
act.pyqtConfigure(triggered=self.on_triggered)



#get main window instance
#3ds max:
#mainWindow = GetQMaxWindow() --old
GetQmaxMainWindow()

#mayaDockableMixin





# visibility

# toggle visibility
widget.setVisible(not widget.isVisible()) 

.isEnabled	#bool

.isVisible	#bool
.isHidden	#bool
.setHidden(True)

self.show()
self.hide()
.close




#bring to front
self.ui.raise_
#send to back
self.ui.lower()



#	Focus
QWidget.setFocusPolicy() Keyboard Focus #self.setFocusPolicy(QtCore.Qt.StrongFocus)

w.clearFocus()
w.hasFocus()
w.setFocus()
w.clearFocus()


#shedule refresh 
self.update()




# Remove widget
for i in reversed(range(self.layout.count())): 
	widgetToRemove = self.layout.itemAt(i).widget()
	# remove it from the layout list
	self.layout.removeWidget(widgetToRemove)
	# remove it from the gui
	widgetToRemove.setParent(None)




# Layouts

QFormLayout
QGridLayout
QBoxLayout
QVBoxLayout

# stacking multiple widgets
#setting up a stacked layout
QStackedLayout
eg.
#build list of all widget names to be stacked
uiList = ["init", "main", "viewport", "mainOptions", "viewportOptions", "normals", "create", "edit", "transform", "selection", "polygons", "nurbs", "texturing", "animation"]
#use index to get ui name or set stack index
self.name = uiList[index]

if (self.layout() == None):
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




# WA - Widget attribute
#https://doc.qt.io/archives/qtjambi-4.5.2_01/com/trolltech/qt/core/Qt.WidgetAttribute.html
widget.setAttribute(QtCore.Qt.WA_DeleteOnClose) #separated by |

#state
WA_WState_Created
WA_WState_Hidden
WA_WState_Visible
WA_WState_ExplicitShowHide

#close/disable
WA_DeleteOnClose #Makes Qt delete this widget when the widget has accepted the close event
WA_Disabled #Indicates that the widget is disabled
WA_ForceDisabled #Indicates that the widget is explicitly disabled
WA_QuitOnClose #Makes Qt quit the application when the last widget with the attribute set has accepted closeEvent().
#
WA_DontShowOnScreen
WA_ShowWithoutActivating #Show the widget without making it active.

#parent/child
WA_NoChildEventsForParent #Indicates that the widget does not want ChildAdded or ChildRemoved events sent to its parent.
WA_NoChildEventsFromChildren #Indicates that the widget does not want to receive ChildAdded or ChildRemoved events sent from its children.









'Widget types'#------------------------------------------------------------------


# Visual style



# QPushButton signals.  QtUi QPushButton signal in
#Qt signals: clicked(), pressed(), released(), toggled(), setText(), setIcon()
#public slots: setChecked(bool), toggle()

#connect to multiple slots:
map(self.dial.valueChanged.connect, [self.spinbox.setValue, self.getValue_dial])
#or
[self.dial.valueChanged.connect(x) for x in [self.spinbox.setValue, self.getValue_dial]]
#alternatively you could connect to one method and use that to call various others.


#enable/ disable button objects
ex. button.setEnabled(False) #either method serves both functions. must be used with an argument
ex. button.setDisabled(True)

#hide/ unhide objects
ex. button.setVisible(False)
#query visible state
ex. button.isHidden()


.pressed #QPushButton.pressed()


btn.click() #emits clicked signal

.clicked #bool checked=False #QPushButton.clicked()
self.ui.button.clicked.connect(self.methodToConnectTo)
#or with arguments
self.ui.button.clicked.connect(lambda ans=passedArg: self.methodToConnectTo(passedArg))
#
b4.clicked.connect(lambda:self.whichbtn(self.b4))


.released #QPushButton.released()

.toggled #bool checked


.toggle #QPushButton.toggle()
# Toggles between checkable states
self.b1.toggle()
	


# QCheckBox

#		QtUi checkable button signal input
#		self.ui.connect(HandleSelection, SIGNAL(toggled(bool)),MEL_HandleSelection,SLOT(setVisible(bool)));
#		QObject::connect(moreButton, SIGNAL(toggled(bool)), tertiarypb7Box, SLOT(setVisible(bool)));

.stateChanged #QCheckBox.stateChanged()
self.ui.c000.stateChanged.connect(self.max_c000)


.setCheckable #QPushButton.setCheckable()
# Recognizes pressed and released states of button if set to true
self.b1.setCheckable(True)


.isChecked #QPushButton.isChecked()
# Returns Boolean state of button
self.b1.isChecked()
#setChecked
self.ui.chkpin.setChecked(True)



.setEnabled(False) #QPushButton.setEnabled()
# When set to false, the button becomes disabled, hence clicking it doesn’t emit a signal
b3.setEnabled(False)




.setDefault #QPushButton.setDefault()
# Sets the button as default




.text #QPushButton.text()
# Retrieves buttons’ caption or textfields value


# modify button text
.setText #QPushButton.setText()
# Programmatically sets buttons’ caption or textfields value


# icon
.setIcon #QPushButton.setIcon()
# Shows an icon formed out of pixmap of an image file
ex.
b2.setIcon(QIcon(QPixmap("python.gif")))


#set icon to rgb value:
pixmap = QtGui.QPixmap(100,100)
pixmap.fill(QtGui.QColor.fromRgb(r, g, b))
cmb.setItemIcon(index, QtGui.QIcon(pixmap))



#QSpinBox. for a double value use QDoubleSpinBox
.setMinimum(-5) #Sets the lower bound of counter
.setMaximum(5) #Sets the upper bound of counter
.setRange(0,10) #Sets the minimum, maximum and step value
.setWrapping(s) #Set whether spin box is circular. Both bounds must be set for this to have an effect.
.singleStep() #gets the step value of counter
.setSingleStep(1) #Sets the step value.
.setValue(2) #set value
.value() #Get the current value
.cleanText() #get the current value excluding any prefix or suffix
.setPrefix("") #Set a string prefix.
.setSuffix("") #Set the string suffix appended to the spinbox text.
.text() #gets prefix/suffix string value

self.ui.spinbox.valueChanged.connect(self.b000)


#QComboBox
# get list contents:
list_ = [cmb.itemText(i) for i in range(cmb.count())]
components = pm.ls (selection=1, flatten=1)
cmb.addItems(components)
# add string
cmb.addItem(component)
# add signals:
comboboxes = ["cmb000"]
for combobox in comboboxes:
	method = getattr (self, combobox)
	ui = getattr (self.ui, combobox)
	ui.currentIndexChanged.connect(method)
	ui.activated.connect(method)
	method() #init comboboxes
#additional signals:
cmb.activated.connect(self.b034)
QComboBox.activated(int).connect() #index of the selected item
QComboBox.activated(unicode).connect() #[str] text of selected item
highlighted () #index of the selected item
highlighted (index) #[str] text of selected item
currentIndexChanged ()
currentIndexChanged (index)
editTextChanged ()
#eventFilter for button press #see also eventFilter for view event
self.combo.installEventFilter(self)
def eventFilter(self,target,event):
	if target == self.combo and event.type() == QtCore.QEvent.MouseButtonPress:
		print "Button press"
		self.b034()


# QListWidget
#add key (or value) from a dictionary to a list 
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
ex.
if lineEdit.text() == default_text:
	lineEdit.setText("")
	set_focus_in_color()
	QtGui.QLineEdit.focusInEvent(lineEdit, QtGui.QFocusEvent(QtCore.QEvent.FocusIn))
  
lineEdit.focusInEvent = focus_in

#		QLineEdit signal in
#		Qt signals: editingFinished(), returnPressed(), selectionChanged(), textChanged(const QString &text), textEdited(const QString &text)
#		Qt slots: clear(), copy() const, cut(), paste(), redo(), selectAll(), setText(const QString &), undo()  
ex.
self.ui.t001.returnPressed.connect(self.mel_b019) #qpushbutton b019


# .maxLength (int)  By default, this property contains a value of 32767
ex.
QLineEdit.maxLength()
ex.
QLineEdit.setMaxLength(8)


#increment/ decrement a QLineEdit
ex.
def b001(self): #decrement t000
	textfield = int(self.ui.t000.text()) #get current value
	newText = str(textfield -1) #decrement amount
	self.ui.t000.setText(newText) #set new value


# .setInputMask
#allows the user to type only one digit ranging from 0 to 9. 
#Use multiple 9's to allow the user to enter multiple numbers
ex.
QLineEdit.setInputMask("9")

#list of char arguments for setInputMask
#Use \ to escape the special characters listed above to use them as separators.
A	#ASCII alphabetic character required. A-Z, a-z.
a	#ASCII alphabetic character permitted but not required.

N	#ASCII alphanumeric character required. A-Z, a-z, 0-9.
n	#ASCII alphanumeric character permitted but not required.

9	#ASCII digit required. 0-9.
0	#ASCII digit permitted but not required.
D	#ASCII digit required. 1-9.
d	#ASCII digit permitted but not required (1-9).

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
ex.
QLineEdit.setValidator(QtGui.QIntValidator(0, 100))
ex.
QLineEdit.setValidator(QtGui.QDoubleValidator(0, 100, 2))





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
ex. def groupButtons(self, groupName, group):
			#args: [string], [stringArray])
			#returns: 
			buttonGroup = QtWidgets.QButtonGroup(self.hb.ui)
			buttonGroup.setObjectName(groupName)

			for button in group:
				buttonGroup.addButton(button)
			return buttonGroup

ex. def groupButtons(objectName, ui, prefix, range_):
			#([string], [object], [string], [int])
			buttonGroup = QtWidgets.QButtonGroup(ui)
			buttonGroup.setObjectName(objectName)

			for num in range (range_):
				numString = '000'[:-len(str(num))]+str(num) #remove zeros from string according to the length of the number

				button = getattr(ui, prefix+numString) #equivilent to: (self.ui.m000)
				# print button
				buttonGroup.addButton(button)
			# print buttonGroup
			return buttonGroup

#call
self.buttonGroup = groupButtons("main_buttonGroup", self.ui, "m", 10)




'Events'#--------------------------------------------------------------------

actionEvent (event)
changeEvent (event)
closeEvent (event)
contextMenuEvent (event)
dragEnterEvent (event)
dragLeaveEvent (event)
dragMoveEvent (event)
dropEvent (event)
enterEvent (event)
focusInEvent (event)
focusNextPrevChild (next)
focusOutEvent (event)
heightForWidth (arg__1)
hideEvent (event)
inputMethodEvent (event)
inputMethodQuery (arg__1)
keyPressEvent (event)
keyReleaseEvent (event)
languageChange ()
leaveEvent (event)
minimumSizeHint ()
mouseDoubleClickEvent (event)
mouseMoveEvent (event)
mousePressEvent (event)
mouseReleaseEvent (event)
moveEvent (event)
paintEvent (event)
resizeEvent (event)
setVisible (visible)
showEvent (event)
sizeHint ()
tabletEvent (event)
wheelEvent (event)





.moveEvent
.resizeEvent


#Focus
PySide.QtGui.QFocusEvent #PySide.QtGui.QFocusEvent.gotFocus() #Return type:	PySide.QtCore.bool


.focusInEvent #QWidget.focusInEvent()
.focusInEvent #QPushButton.focusInEvent
.focusOutEvent #QPushButton.focusOutEvent

ex.
self.ui.b010.focusInEvent = self.max_b010()

.focusOutEvent #QWidget.focusOutEvent()
ex.
self.focusOutEvent(MaxPlus.CUI.EnableAccelerators())



self.showEvent(offsetPos(self, offset))


QtCore.QEvent.HoverMove

ex.
if event.type() == QtCore.QEvent.HoverEnter:
ex.
if event.type() == QtCore.QEvent.Type.Enter:


.enterEvent
ex.
	print "enterEvent"
	self.show()
	self.setFocus()

.leaveEvent
ex.
	print "leaveEvent"
	self.hide()


QtGui.QDragEnterEvent(pos, actions, data, buttons, modifiers)
# Parameters:
# pos – PySide.QtCore.QPoint
# actions – PySide.QtCore.Qt.DropActions
# data – PySide.QtCore.QMimeData
# buttons – PySide.QtCore.Qt.MouseButtons
# modifiers – PySide.QtCore.Qt.KeyboardModifiers




#custom event filter:

# install filter
ex. QtGui.qApp.installEventFilter(self)
ex. buttonObject.installEventFilter(self.hotBox) 

# return value
ex. return QtWidgets.QWidget.eventFilter(self, button, event)
ex. return super(HotBox, self).eventFilter(self, event) #returns the event that occurred






'Mouse Event'#--------------------------------------------------------------


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
if (QtGui.QMouseEvent.button == QtCore.Qt.RightButton):
# QtCore.Qt.MiddleButton
# QtCore.Qt.LeftButton

# middle mouse button event
ex.
if event.buttons() & QtCore.Qt.MiddleButton:
# Left Button event with control key
ex.
if event.buttons() & QtCore.Qt.LeftButton and event.modifiers() & QtCore.Qt.ControlModifier:




mouseTracking::#bool, default: distabled,
# Access functions:
.hasMouseTracking
.setMouseTracking(True)


QWidget.underMouse() #Returns true if the widget is under the mouse cursor; otherwise returns false.


QEvent::HoverEnter	#The mouse cursor enters a hover widget (QHoverEvent).
QEvent::HoverLeave	#The mouse cursor leaves a hover widget (QHoverEvent).
#setMouseTracking(True) for mouse event
.enterEvent #An event is sent to the widget when the mouse cursor enters the widget.
.leaveEvent	#A leave event is sent to the widget when the mouse cursor leaves the widget.
.onEnter
.onLeave

QEvent::MouseButtonDblClick 	#Mouse press again (QMouseEvent).

.mouseDoubleClickEvent
ex.
def mouseDoubleClickEvent(self, event):
	print "mouseDoubleClickEvent"

QEvent::MouseMove 	#Mouse move (QMouseEvent).
.mouseMoveEvent

QEvent::MouseButtonPress 	#Mouse press (QMouseEvent).
.mousePressEvent

QEvent::MouseButtonRelease 	#Mouse release (QMouseEvent).
.mouseReleaseEvent
ex.
mouseReleaseEvent = QtGui.QMouseEvent(
											QtCore.QEvent.MouseButtonRelease,
											self.cursor().pos(),
											QtCore.Qt.LeftButton,
											QtCore.Qt.LeftButton,
											QtCore.Qt.NoModifier,
										)
#QtCore.QEvent.Type
if event.type() == QtCore.QEvent.Type.MouseButtonRelease:


QtCore.QEvent.Type.MouseButtonRelease
QtCore.QEvent.Type.UngrabMouse


QEvent::wheel 	#Mouse wheel rolled (QWheelEvent).




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
ex. widget.setWindowFlags(QtCore.Qt.flag1|QtCore.Qt.flag2)

WA_Hover #Forces Qt to generate paint events when the mouse enters or leaves the widget.

WA_UnderMouse #Indicates that the widget is under the mouse cursor.

WA_NoMouseReplay #Used for pop-up widgets. Indicates that the most recent mouse press event should not be replayed when the pop-up widget closes.

WA_MouseTracking #Indicates that the widget has mouse tracking enabled.
WA_TransparentForMouseEvents #disables the delivery of mouse events to the widget and its children


PySide.QtGui.QWidget.grabMouse()
PySide.QtGui.QWidget.releaseMouse()





'Keyboard Event'#-----------------------------------------------------------


WindowTransparentForInput
WA_InputMethodTransparent
WA_KeyboardFocusChange #Set on a toplevel window when the users changes focus with the keyboard (tab, backtab, or shortcut).


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



#repainting (key auto repeating)
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



QWidget.keyPressEvent() #key press event under a window class
ex.
def keyPressEvent(self, event):
	if event.key() == QtCore.Qt.Key_X:
		self.X_dn()
	if event.key() == QtCore.Qt.Key_Y:
		self.Y_dn()

def X_dn (self):
	print "x Down"
#or possibly:
self.keyPressEvent(self.X_dn, QtCore.Qt.Key_X) #(command/function, event)



QWidget.keyReleaseEvent()
ex.
def keyReleaseEvent(self, event):
	if event.key() == QtCore.Qt.Key_X:
		self.X_up()
	if event.key() == QtCore.Qt.Key_Y:
		self.Y_up()

def X_up (self):
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
	if (obj.objectName() == "group_of_widgets"):
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
if (o.objectName() == "tree_widget_of_items"):
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

#or possibly
ex.
keyPressEater = KeyPressEater(self)
self.QPushButton.installEventFilter(keyPressEater)
self.QListView.installEventFilter(keyPressEater)

#working example
ex.
self.ui.b010.installEventFilter(self)

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

self.ui.b011.installEventFilter(HoverEnterFilter(self))


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

HoverArea(self.ui.v000).mouseHover.connect(self.mel_v000)



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


# assign signal a value. must be defined as class variable (before class init)
ex. updated = Signal(int)
ex. updated = Signal(str)
ex. updated = Signal(object)


# create a signal
ex. enterEvent = QtCore.Signal(bool)


def enterEvent(self, event):
	self.enterEvent.emit(True)

def leaveEvent(self, event):
	self.enterEvent.emit(False)


#call function with argument from signal
#using lambda function
ex. self.button.clicked.connect (lambda: self.overlay.setVisible(False) if self.overlay.isVisible() else self.overlay.setVisible(True))
#using functools.partial
#from functools import partial
ex. button.clicked.connect (partial(function, arg))
#
ex. button.clicked.connect(partial(self.function, arg=arg['name']))



# emit a simple signal
ex. #from PySide.QtCore import QObject, Signal, Slot

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
ex. #from PySide import QtGui, QtCore

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

ex.
parent = QtCore.QObject()
parent.setObjectName("parent")

child = QtCore.QObject()
child.setObjectName("child")

child.setParent(parent)

#calling:
parent.children()
#returns [QtCore.Qbject at 0x10xxxxxx]


ex.
button = QtGui.QPushButton("ButtonName", parent=widget)


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

_timer = QtCore.QTimer(





'Populating Ui with Elements'#-----------------------------------------------

#populate a grid layout with buttons
class ButtonBlock(QtGui.QWidget):

	def __init__(self, *args):
		super(QtGui.QWidget, self).__init__()
		grid = QtGui.QGridLayout()
		names = ('One', 'Two', 'Three', 'Four', 'Five',
						'Six', 'Seven', 'Eight', 'Nine', 'Ten')
		for i, name in enumerate(names):
			button = QtGui.QPushButton(name, self)
			button.clicked.connect(self.make_calluser(name))
			row, col = divmod(i, 5)
			grid.addWidget(button, row, col)
		self.setLayout(grid)

	def make_calluser(self, name):
		def calluser():
			print(name)
		return calluser

app = QtGui.QApplication(sys.argv)
tb = ButtonBlock()
tb.show()






'Dynamic Ui'#----------------------------------------------------------------


# sorting through the ui
#put the widgets into a generator. identify widget types so they can be handled accordingly
ex. QObject.findChildren()

ex. widgets = (layout.itemAt(i).widget() for i in range(layout.count()))
	for w in widgets:
		if isinstance(widget, QLineEdit):
			print "linedit: %s  - %s" %(widget.objectName(),widget.text())
			print "checkBox: %s  - %s" %(widget.objectName(),widget.checkState())
#alt
ex.	for widget in centralwidget.children():
		if isinstance(widget, QLineEdit):
			print "linedit: %s  - %s" %(widget.objectName(),widget.text())

		if isinstance(widget, QCheckBox):
			print "checkBox: %s  - %s" %(widget.objectName(),widget.checkState())

ex. self.ui.findChildren(QtWidgets.QPushButton) #pass a type (or tuple of types) as the first argument, and an optional string as the second argument (for matching the objectName).


layout.count()
layout.rowCount()
layout.columnCount()




	    







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


#DEBUG
class MainWindow(QtWidgets.QMainWindow):
	testSignal = QtCore.Signal()

def __init__(self, parent=None, **kwargs):
	super(MainWindow, self).__init__(parent, **kwargs)
	self.testSignal.connect(self.debug)

def debug(self, *args, **kwargs):
	print("got", args, "and", kwargs)




#RuntimeError: '__init__' method of objects base class (MyObject) not called.
#Python wrapper is created but C++ object isn’t
ex.
from PyQt4.QtCore import QObject

	def __init__(self):
	self.field = 7

obj = MyObject()
print(obj.field)
obj.setObjectName("New object")

# MyObject constructor doesn’t call the constructor of the base class. MyObject is successfully created and can be used. But when the C++ method is called, a RuntimeError is issued. The exception explains what is wrong.
# Fixed code:
ex.
class MyObject(QObject):
	def __init__(self):
		QObject.__init__(self)


#garbage collection management:
ex.
def createLabel():
    label = QLabel("Hello, world!")
    label.show()
    return label #add return. References to all created objects must be saved even if you are not going to use them

app = QApplication([])
label = createLabel()

app.exec_()


# RuntimeError: A QApplication instance already exists.
#there is already a PySide application running, so get a handle for that object like this:
app = QtGui.QApplication.instance()


## AttributeError: 'PySide2.QtCore.Signal' object has no attribute 'emit'
#define signal as a class variable before init
ex.
class Button(QtCore.QObject):
	mouseHover = QtCore.Signal(bool)
#now in can be referenced in later methods as self.mousHover.emit(True/False)



'installation'


#python wheels: (download and install locally to make sure the correct wheel gets installed)
http://download.qt.io/snapshots/ci/pyside/






'Style'#--------------------------------------------------------------------


#19 predefined QColor objects accessible as members of the Qt namespace (ie. Qt::red).: 
#white, black, red, darkRed, green, darkGreen, blue, darkBlue, 
#cyan, darkCyan, magenta, darkMagenta, yellow, darkYellow, gray, 
#darkGray, lightGray, color0 and color1
ex.
QtGui.QColor.magenta()

ex.
QtGui.QColor(122, 163, 39)

ex.
QtGui.QColor.alpha #get alpha int value
QtGui.QColor.setAlpha(2)


ex.
widget.setForeground(0,QtGui.QBrush(QtGui.QColor("red")))

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
WA_SetCursor #Indicates that the widget has a cursor of its own.
WA_SetFont #Indicates that the widget has a font of its own.


ex.
setWindowOpacity(0.5)

ex.
setAutoFillBackground(False)
QWidget.autoFillBackground(True)


#erase area \fill with background
fillRect(rectangle, background())




# styleSheet
# docs: http://doc.qt.io/archives/qt-4.8/stylesheet-examples.html
#print the stylesheet if there is one:
print self.pushButton.styleSheet()

#QWidget.styleSheet
pushButton.styleSheet #query the widgets style sheet.

#If you would prefer that the font and palette propagate to child widgets, you can set the Qt::AA_UseStyleSheetPropagationInWidgetStyles flag, like this:
QCoreApplication::setAttribute(Qt::AA_UseStyleSheetPropagationInWidgetStyles, true);


ex.
buttonObject.setStyleSheet("") ##set style sheet to default. also (styleSheet())
self.setStyleSheet("background: transparent;") #doesn't need the style sheet itself but child widgets contained in the widget that have autoFillBackground()==True by default should have it unset or should have set QtCore.Qt.WA_TranslucentBackground or have a transparent background color set by a style sheet which is then inherited
pushButton.setStyleSheet("background-color: transparent") #white, black, grey, magenta, etc
setStyleSheet("background-color: rgba(227, 227, 227, 2)") #rgb + alpha. alpha value of 1 sometimes doesnt work.


ex.
.setStyleSheet("QToolTip { color: #ffffff; background-color: #2a82da; border: 1px solid white; }");
.setStyleSheet("QLabel {font-size: 100px; opacity:0.5}")

#comment css
/* css multi-line comment */


ex.
button.setStyleSheet('''
QPushButton {
	background:rgba(127,127,127,2);
	background-color: red;
	color: white;
	border-width: 2px;
	border-radius: 10px;
	border-color: beige;
	border-style: outset;
	font: bold 14px;
	min-width: 10em;
	padding: 5px;
QPushButton:hover {   
	border: 1px solid black;
	border-radius: 5px;   
	background-color:#66c0ff;
QPushButton:pressed {
	background-color: rgb(224, 0, 0);
	border-style: inset;
QPushButton:enabled {
	color: red
QComboBox {
	image: url(:/none);}
QComboBox::drop-down {
	border-width: 0px; 
	color: transparent
QComboBox::down-arrow {
	border: 0px solid transparent; 
	border-width: 0px; left: 0px; top: 0px; width: 0px; height: 0px; 
	background-color: transparent; 
	color: transparent; 
	image: url(:/none);
QTreeWidget {
	border:none;
} 
QTreeWidget::item {
	height: 20px;
QTreeView {
  alternate-background-color: rgba(35,35,35,255);
  background: rgba(45,45,45,255);
}
QMenu {
	background-color: white; /* background-color: #ABABAB; sets background of the menu */
	margin: 2px; /* some spacing around the menu */
	border: 1px solid black;
}
QMenu::item {
	/* sets background of menu item. set this to something non-transparent
	if you want menu color and menu item color to be different */
	background-color: transparent;
	padding: 2px 25px 2px 20px;
	border: 1px solid transparent; /* reserve space for selection border */
}
QMenu::item:selected { 
	/* when user selects item using mouse or keyboard */
	background-color: #654321;
	border-color: darkblue;
	background: rgba(100, 100, 100, 150);
}
QMenu::icon:checked { /* appearance of a 'checked' icon */
	background: gray;
	border: 1px inset gray;
	position: absolute;
	top: 1px;
	right: 1px;
	bottom: 1px;
	left: 1px;
}
''')









maya qt menus

popupMenu77
LayerEditor
menu8
objDeformerPopup
popupMenu98
HotboxCenter2
menuItem1045
bifCacheMenu
mainDynEffectsMenu
objectMaskPopup
listMenu
menuItem882
menuCreateSceneAssembly
menuItem747

menu28
mainDisplayMenu
popupMenu114
popupMenu9
menuItem1050
HotboxWest3
vrayAEMenu
menu
popupMenu8
OptionMenu
FilterUIAttributeFilterSubMenu
popupMenu128
mainWindowMenu
modelPanel3ToolOptionsPop
menu24

outlinerPanel1Popup

mainEditMeshMenu
modelPanel2ToolOptionsPop
Outliner
FilterUIAttributeFilterSubMenu
menuItem839
popupMenu91
menuItem521
popupMenu138
CommandLine
Panels
HotboxEast3
compPivotPopup
menuItem893
mainNClothMenu
HotboxNorth3
mainParticlesMenu
popupMenu62
modelPanel3CommandPop
popupMenu52
mainConstraintsMenu
objOtherPopup
menu18
popupMenu5
mainPipelineCacheMenu
menuItem852
AEdynamicsSubMenu
menuItem422
HotboxNorth2
menu4
menu26
Panels
popupMenu103
HotboxSouth1
popupMenu81
HotboxEast2
compOtherPopup
menuItem1001
HotboxSouth3
menuItem226
popupMenu109
menuItem225
popupMenu110

menu3
modelPanel2ConvertPop
menu13
popupMenu83
menuItem318
popupMenu134
popupMenu125
NEXDockControl
modelPanel3ObjectPop
Panels
geometryCacheMenu
View
vrayMenuCreateItem
View
menuItem510
menuItem156
popupMenu121


bonusToolsMenu
popupMenu108
popupMenu54
popupMenu132
menuItem420
popupMenu89
View
popupMenu82
popupMenu78
popupMenu80
objSurfacePopup
transHierItem
HotboxCenter3


HotBoxControlsMenu
menu20
menu23
menuItem157
mainNCacheMenu
menu1
modelEditorTransformSelOptionMenu
objMarkerPopup
popupMenu12
FilterUIObjectFilterSubMenu
AEshadingSubMenu
popupMenu50
popupMenu126
popupMenu66
menu25
popupMenu79
popupMenu117
popupMenu113
objRenderingPopup
menu16
StatusLine
popupMenu90
mainNConstraintMenu
objectMenu
menuItem1052
menu5



compMarkerPopup
popupMenu97
menuItem887
popupMenu15
popupMenu13
mainSelectMenu
HotboxSouth2
focusMenu
popupMenu1
Shelf
menuItem733
addMenu

popupMenu75
polyPrimitivesItem
mainBifrostFluidsMenu

popupMenu116

popupMenu73
matchTransformsItem
popupMenu67
HelpMenu
mainCartoonMenu
popupMenu93
popupMenu140
mainEditMenu

popupMenu131
modelEditorTransformSelOptionMenu
assetItem
mainRigDeformationsMenu
mainOptionsMenu
objCurvePopup
popupMenu136
mainPlaybackMenu
HelpMenu
mainRigSkinningMenu
popupMenu139
menuItem224

mainUVMenu

mainRigSkeletonsMenu
MayaWindow

HotboxEast1


menu21
RangeSlider
compHullPopup
menu14
historyPopup

FilterUIObjectFilterSubMenu
menuItem228
modelPanel1ConvertPop
mainRenTexturingMenu
popupMenu86
menuItem1057
workspaceSelectorMenu
compPointPopup
menu17
measureItem

popupMenu92
menuItem329
View
popupMenu141
menuItem230
popupMenu107
menu15
popupMenu65
menuItem152
menuItem741
mainRenderMenu
dash_contextual
modelEditorTransformSelOptionMenu
mainSurfacesMenu
popupMenu104
menuItem1054
popupMenu7
mainMeshToolsMenu
compParmPointPopup
surfConvItem

popupMenu11
menu12
AEhelpMenu
menuItem712
popupMenu14
outlinerPanel4Popup
objJointPopup
popupMenu94
menuItem1055
Panels

popupMenu135
ToolBox
Show
modelPanel1ToolOptionsPop
menuItem734
popupMenu63

menu22
mainMashMenu

mainKeysMenu
popupMenu123
popupMenu105
popupMenu6
modelPanel1CommandPop
menu6
popupMenu120

popupMenu87
popupMenu2

popupMenu133
menu30
mainGenerateMenu
FilterUIAttributeFilterSubMenu
mainVisualizeMenu
mainRigConstraintsMenu
TimeSlider
ChannelBox
popupMenu122

modelPanel2ObjectPop
mainCreateMenu
mainBossMenu
menuItem65
popupMenu102
menu27
mainCurvesMenu
modelPanel2CommandPop

modelPanel3ConvertPop
menuItem174
popupMenu95
graspItem

popupMenu70
objectsCompItem
popupMenu3
objDynamicPopup
FilterUIAttributeFilterSubMenu
menuItem876
init
popupMenu85
menu2
popupMenu99

popupMenu96
OpenSceneButtonRecentFileItems

menuItem162
menuItem1053
menu31
cbShowMenu

menuItem699
popupMenu115
mainModifyMenu
menuItem899
HelpLine
popupMenu58
mainMeshDisplayMenu
popupMenu100
LightsItem

menuItem1056
menuItem1026
popupMenu49
popupMenu72
menuMode
menuItem418
menuItem627
mainMeshMenu
popupMenu59
popupMenu127
menuItem160
popupMenu51
popupMenu10
modelPanel1ObjectPop
mainDeformMenu
modelPanel4ConvertPop
menu
popupMenu130
modelPanel4ObjectPop
popupMenu61
compFacetPopup
popupMenu142
menu10
mainDeformationMenu
mainStereoMenu
popupMenu56
popupMenu112
menuItem870
menu11
mainShadingMenu

menu29
mainRigControlMenu
FilterUIObjectFilterSubMenu
HotboxWest1
componentMaskPopup
TimeSliderMenu
modelEditorTransformSelOptionMenu
popupMenu137
gpuCacheMenu
popupMenu129
menu9
popupMenu84
defManipItem

popupMenu53



popupMenu69
mainFieldsSolverMenu
mainFileMenu
HotBoxRecentCommandsMenu
futurePopup
popupMenu60
AEkinematicsSubMenu

popupMenu71
alembicCacheMenu
popupMenu74
menu19
popupMenu57
menu

popupMenu64
popupMenu106
modelPanel4CommandPop
modelPanel4ToolOptionsPop
mainFluidsMenu
AEdeformersSubMenu
popupMenu68

createCurveTools
setCurrentContainerItem
mainHairMenu
MainHelpMenu

AElightSubMenu
compLinePopup
volumePrimitivesItem
HotboxNorth1
menu7
menuItem416
popupMenu55
HotboxWest2
menuItem172


popupMenu88
HotboxCenter1
popupMenu4
menuItem175
popupMenu111
popupMenu118
menuItem811
popupMenu119
CommandWindow
popupMenu124
menuItem417
menuItem173
nexSoftSelectionDistanceType
popupMenu101
'''
