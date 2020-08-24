// QML notes



/* Auto-Completion
>	ctrl+space
*/




// PROPERTIES ---------------------------------------

//set new property <var> <name>: <value>
property bool propertyName: false	//
//set existing:
<property> = <value>	//ex. onClicked: parent.running = true

//get
<id>.<property>			//ex. running: parent.running







// SHAPE --------------------------------------------


//circle from rectangle
radius = 100			// 100 = full circle, or width*.5







// IMAGE --------------------------------------------

Image {
	id: <id>
	source: ""
	opacity: 0.5
}


AnimatedImage {
	id: <id>
	source: ""
	opacity: 0.5
}




// TEXT ---------------------------------------------

Text {
	id: <id>
	anchors.centerIn: parent
	font: <font>		//parent.font
	color: <color>		//parent.color
	text: ""			
}


//TextInput
TextInput {
	id: txtPlain
	anchors.fill: parent
	anchors.margins: 4
}


//TextField
TextField {
	id: txtText
	text: ""
	width: 300
}


//TextArea
Rectangle {
	id: textFrame
	width: parent.width
	height: parent.height// - (<frame>.height + <column>.spacing)

	TextArea {
		id: txtEncoded
		anchors.fill: parent
	}
}






// COLOR --------------------------------------------

color: "green"
color: "#00FF00"


//alpha

opacity: 0.6			//(float)





// SIZE ---------------------------------------------

width: 150				//(int)
height: 150				//(int)






// POSITION -----------------------------------------
/*
Do's:
>	Choose appropriate method for each specific case:
>	Absolute position to set static 'x' and 'y' values.
>	Anchors to set relative position.
>	Positioners to arrange set of items with fixed size into a row, a column, or a grid.
>	Layouts to arrange set of items into a row, a column, or a grid, and resize them.

Don't:
>	Use bindings on 'x', 'y', 'width', and 'height' properties.
>	Set 'x' and left/right/horizontalCenter anchors at the same time.
>	Set 'y' and top/bottom/verticalCenter anchors at the same time.
>	Use left/right/horizontalCenter anchors for items in Row/RowLayout/Grid/GridLayout
>	Use top/bottom/horizontalCenter anchors for items in Column/ColumnLayout/Grid/GridLayout
*/


//absolute (global)
x: 50					//(int)
y: 50					//(int)
z: 0					//(int) raise object by setting a value from '1' to the number of layers in the scene. 


//anchoring:

anchors.fill: parent	//set to the size of a given object
anchors.margin: 50		//set margins. anchors.leftMargin: 50
anchors.centerIn: parent	//center object
anchors.horizontalCenter: parent.horizontalCenter
anchors.verticalCenter: parent.verticalCenter





// Transform ---------------------------------------

//move relative
transform: Translate {
	x: 50
	y: 50
}






// WINDOW ------------------------------------------

Window {
	id: <id>
	visible: true
	width: 640
	height: 380

	Column {
		Row {
			id: row1
			Button {
				text: ""
			}
		}
	}
}



// HIERARCHY ---------------------------------------

parent




// FOCUS -------------------------------------------


focus
activeFocus ?		//ex. color: activeFocus ? "gray" : "lightgray"

parent.forceActiveFocus()	//generally use keyNavigation rather than explicitly call forceActiveFocus()




// CONTROLS ---------------------------------------
//Qt Quick Controls provides a set of controls that can be used to build complete interfaces in Qt Quick.
import QtQuick.Controls 2.15


Button {
	text: ""
	onClicked {

	}
}


Slider {
	width: parent.width
	maximumValue: 360
	minimumValue: 0
	value: 0

	onValueChanged: {

	}
}



// DIALOGS ----------------------------------------


ColorDialog {
	id: colorDialog
	modality: Qt.WindowModal
	title: "Choose a Color."
	color: "black"
	onAccepted: {console.log("Accepted: "+color)}
	onRejected: {console.log("Rejected!")}
}

FontDialog {
	id: fontDialog
	modality: Qt.WindowModal
	title: "Choose a Font."
	onAccepted: {console.log("Accepted: "+font)}
	onRejected: {console.log("Rejected!")}
}




// SIGNALS ----------------------------------------


signal send(string value)
onTargetChanged: send.connect(target.<function_name>)






// SLOTS ------------------------------------------


function <function_name>(value) {
        displayText = value
        clicknotify.running = true
    }





// EVENTS -----------------------------------------


onValueChanged {}



// ANIMATION -------------------------------------

PropertyAnimation {

}

ColorAnimation {

}

//rotation (animate the rotation property)
NumberAnimation on rotation {
	from: 0
	to: 360
	duration: 3000
	loops: NumberAnimation.Infinite
	running. true
}

RotationAnimation {

}

SequentialAnimation on buttonColor {
	id: clicknotify
	running: false

	ColorAnimation {
		from: "white"
		to: "black"
		duration: 100
	}

	ColorAnimation {
		from: "black"
		to: "white"
		duration: 100
	}
}





// APPLICATION -----------------------------------
/* To execute and display a QtQuick application:
>	instance of QQmlEngine class
>	""			QQuickWindow
>	""			QQuickItem
*/

/*
>	Create QQmlEngine and QQuickWindow manually if you prefer to have full control over your app.
>	Use QQuickView if you prefer to create the root window in the C++ side.
>	Use QQmlApplicationEngine if your root QML component is a Window.
>	Use QQuickWidget if your application is widgets-based.
*/

//load an external application
QGuiApplication app(int argc, char *argv[])

QQmlEngine engine;
QQmlComponent component(&engine, QUrl(QStringLiteral("qrc:/main.qml")));
component.create()

return app.exec()





// PROJECT --------------------------------------

//modify project
//right click context menu in project hierarchy.




// ERRORS ---------------------------------------

/*
In Creator: Check the application output tab (versus to compile output), for any error messages.
*/


