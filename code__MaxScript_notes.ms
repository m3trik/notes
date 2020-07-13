---------------------- 3ds Max notes-
-------------------------------------


--"GENERAL_SYNTAX: //------------------------------------------------------"







"COMMENTING: //------------------------------------------------------------" 

-- single line 

/* 
multiple 
lines 
*/


"VARIABLES: //-------------------------------------------------------------"

mystring = "This is my string."


"Scope"
-- define local
local variable

-- define global
global variable


-- to python:
maxEval("texture_path = getDir #MaxData +#image_dir")
print rt.texture_path






"Conversion To: //----------------------------------------------------------"

-- int__________float___________string__________vector__________matrix
int ($i)		perfect 		perfect 		perfect 		<<$i, $i, $i>> 			none

float ($f)		without			perfect			perfect			<<$f, $f, $f>>			none

string 			without 		perfect if 		perfect			perfect if 				none
				fraction		starts with 					starts with
				if starts		number,							vector or floats	
				with number,	else 0							with remaining
 				else 0																	elements 0

vector 			length of 		length of 		3 floats		perfect					perfect for
				vector 			vector 			separated								[1][3] matrix,
				without											by a space 				else none
				fraction
------------------------------------------------------------------

matrix			for [1][3] 		for [1][3]		none 			for [1][3] 				perfect
				matrix or 		matrix or 						matrix or 
				smaller, 			smaller,length 				smaller, perfect
				length of 		of matrix 						with remaining
				matrix without 									elements 0
				fraction

  


   

 



 





"STRINGS: //---------------------------------------------------------------"


\"	--	double quote

\		--	Line Continuation

;		--	Command Separation

\n 	--	new line (or: \r\n)

\r 	--	carriage return

\t 	--	TAB

\*	--	asterisk

\?	--	question mark

\\	--	single \

\%	--	percent

\x{d}	--hexadecimal


-- [string operators:]
"string" + "string"
-- Returns a new string that is the concatenation of two strings.
"string" == "string"
"string" != "string"
"string" > "string"
"string" < "string"
"string" >= "string"
"string" <= "string"
-- Standard lexical string comparisons (case sensitive).
-- To perform a case insensitive equality comparison, please use the stricmp() method that performs a lower-case comparison.
"string"[<index_number>]
-- Returns the indexed character as a single-character string, index starts at 1.
"string"[<index_number>]= <single_character_string>
-- Sets the indexed character to the given character.
"string"as<class>


-- [string methods]


--concatenation
s1 = "aa"
s2 = s1
append s1 "bb"
s1-- returns "aabb"
s2-- returns "aabb"and not "aa" 


--find index of substring
rt.findString(obj.name, search_string='') -- Returns the index of search_string in string or undefined if not found.





--Compiles and evaluates the contents of the string as a MAXScript expression 
--and returns the result of the evaluation.
execute <string>


--check for white space:
--at first char
isSpace " MAXScript" --returns 'true'
isSpace "\nMAXScript" --first character is new line. returns 'true'



--search string for text
<integer>findString<string> <search_string> 
--Returns the index of search_string in string or undefined if not found.
findString "Thanks for all the fish!" "all" -- returns 12 


--tokenize
-- <array of strings>filterString "string" <token_string> [splitEmptyTokens:<boolean>]
--filterString splits the input string into substrings based on the characters given 
--in token_string , and returns each substring as a member of the array.
filterString "MAX Script, is-dead-funky" ", -"
-- WOULD RETURN
#("MAX","Script","is","dead","funky")




--If splitEmptyTokens is false or not specified, sequential tokens are handled as a 
--single token, and tokens at the beginning or end of the string are ignored. If 
--splitEmptyTokens is true , each token found will result in string element in the output, 
--with the string element in the cases ignored above being empty strings.
s = "One\t\tThree\tFour"
--> #("One", "", "Three", "Four")
s ="\t\t\tOne\t\t\tThree\tFour\t\t\t"
tokens = filterString s "\t"
--> #("One", "Three", "Four")
tokens = filterString s "\t" splitEmptyTokens:true
--> #("", "", "", "One", "", "", "Three", "Four", "", "", "")


ex. path_ = trimleft "C:\\startup\\userSetup.ms" "C:\\startup" --returns "userSetup.ms"
ex. path_ = trimright "C:\\startup\\userSetup.ms" "userSetup.ms" --returns "C:\startup"



--replace
--Returns a new string where the substring in string starting at index from_integer , 
--and of length length_integer , is replaced with the new_string.new_string can be any 
--length. 
s="1234567890"
s1=replace s 5 3 "inserted string"
-- RETURNS:
"1234inserted string890"


--filter substring
s ="Balerofon"
ss = substring s 5 3-- returns "rof"
ss = substring s 5 -1-- returns "rofon"
ss = substring s 5 100-- returns "rofon" 


--string contains
s="text1"
matchPattern s pattern:"text?"-- returns true
matchPattern s pattern:"T*"-- returns true
matchPattern s pattern:"T*"ignoreCase:false-- returns false
matchPattern s pattern:"s*"-- returns false 






--Case comparison
<integer>stricmp <string1> <string2>
-- In 3ds Max6 and higher, this method performs a lower case comparison of string1 
-- and string2. Returns an integer value < 0 if string1 is less than string 2, = 0 
--if string1 is identical to string 2, and > 1 if string1 is greater than string 2.


--Case conversion
toLower
toUpper "so long and thanks for all the scripts"
"SO LONG AND THANKS FOR ALL THE SCRIPTS"


--Substitute
--Returns a new string with all occurrences of <from_string> in <source_string> replaced 
--with <to_string>. Available in 3ds Max 2008 and higher. Previously available in the 
--Avguard Extensions .
s1 = "Truth, Justice And The American Way"
s2 = "The American Way"
s3 = "All That Stuff"
s4 = substituteString s1 s2 s3
"Truth, Justice And All That Stuff"







-- Convert string
--convert to class
"Foo" as name-- returns #foo

--convert to float
"123.4" as float-- returns 123.4 

--convert to stringstream
--Converting a string to a StringStream value allows you to read through a string using 
--the MAXScript's text file I/O operations.
"$box01" as stringstream-- returns the string as a stringstream 


--copy string
-- The new value contains a copy of the text contents of the copied 
--string and is independent of the copied string.
newstr = copy oldstr


--delete string
free <string>	--Frees the memory used by the string value without waiting for garbage collection.






"OPERATORS: //-------------------------------------------------------------"

+
-
*
/

-- There are assignment operators corresponding to the four math operations (+,-,*, and /) that apply the operation to the assignment’s destination with the result. Their syntax is:
<destination> += <expr> -- add <expr> to destination
<destination> -= <expr> -- subtract <expr> from destination
<destination> *= <expr> -- multiply destination by <expr>
<destination> /= <expr> -- divide destination by <expr>
ex. x = x + 1
-- Using this shorthand form of assignment can be written as
		x += 1

random		ex. random 1.0 100 -- return value type (Float or Integer) is the same as the type of the first argument 




"ITERATORS: //-------------------------------------------------------------"





"COMPARATORS //------------------------------------------------------------"

== -- equal
!= -- not equal 
> -- greater than
< -- less than
>= -- greater than or equal
<= -- less than or equal

-- where <compare_operand> can be one of:
<math_expr>
<operand>
<function_call>


not
and
or




"CONDITIONALS_&_LOOPS: //--------------------------------------------------"


--	CONDITIONALS
--basic if
ex.	if a > b do 
			print d; 
			print e;
--basic if/else
ex.	if a > b then
		( 
			print c
		) 
		else 
			print d

ex.	if ($pos.z < 0) then	--if object is below 0
			$.wirecolor=red
			$.wirecolor=green




a = (if d == 0 then 0 else a / d)






--	TOGGLE
--set to 'not current state'
--toggle for single object
if ($ != undefined) then
	toggle = not $.xray;
	$.xray = toggle;

--toggle for all geometry
toggle = not $.backfacecull;

for obj in Geometry do
	obj.backfacecull = toggle;




--	LOOPS

for i = 1 to snapmode.numOSnaps do
-- 	expression


--for a specified range
for i in 1 to 100 do 
	sphere

for i 1 to 10 do
	Box pos: [i*30, 0, 0]	--create 10 boxes at different x positions




--for 'obj in array' do
for obj in (selection as array)
where classOf obj == Cylinder do
	obj.scale.z = 2	--set scale value for cylinders in current selection






--	SWITCH/CASE
case (superClass) of --in case of variable superClass == shape, light, or camera, perform one of the following  
			shape: superClassString = "shape"
			light: superClassString = "light"
			camera: superClassString = "camera"







"PROCEDURES: //------------------------------------------------------------"
-- functions

-- syntax:
mapped fn functionName argument:optDefaultValue = 
	expression

-- The parameters/arguments for a function are either positional or keyword.
-- 	Positional parameters are defined with a simple <name> and must be placed 
-- before any keyword parameters.
-- 	Keyword parameters have a ':' (colon) after the name and an optional default value. 
-- The caller of the function can optionally supply keyword arguments in any order. 
-- Those not supplied will be set to the default value given, or 
-- the special value unsupplied if a default value is not given.

--function call
functionToCall(arg1 arg2)

--keyword arguments
functionToCall keyword:arg1  keyword:arg2




"ARRAYS/LISTS_&_DICTIONARYS //---------------------------------------------"

-- maxscript collection types
-- https://help.autodesk.com/view/3DSMAX/2018/ENU/?guid=__files_GUID_DAABD302_FB6A_40BB_882A_888631488FB7_htm



--create a MaxScript Array (import pymxs; rt = pymxs.runtime):
rt.execute(" gma = #(1,2,3)") --#output: #(1,2,3)
--add value at index:
rt.gma[1] = 999 --#output: 999

l = list(rt.gma) #[1,999,3]
--add value at index:
l[2] = 888 --#output: [1, 888, 3]


--# create a MaxScript Array via python sequence
ma = rt.Array(*(1, 2, 3)) --#output: #(1,2,3)



--Arrays/Lists
--create array
ex. #()
ex. a = #($Box01, $Box02, $Box03)


--Size of array
--Get/Set the number of elements in the array. 
-- <array>.count : Integer
ex. a.showConstructors


--perform an operation on an array element
a[1].renderable = false


--Get element
ex. array[1] --Indexes start at 1.


--Set element of array to value, growing array as necessary.
ex. array[1] = "element"


--New array is constructed containing all the elements of the first and second operands
<array> + <collection>

ex. a = #(1,2,3,4)
	join a #(5,6,7,8)
	(cameras as array) + lights
	props = getPropNames Node
	join props getPropNames (classOf $foo)
	join props getPropNames $foo #dynamicOnly
	sort props


--create new array with only unique members of source array.
ex. makeUniqueArray #(1, 2, 3, 4, 3, 2, 1)
-- # (1, 2, 3, 4)


--Append value to array, growing it as necessary. 
append <array> <value>	--Returns the resulting array.


--Appends the value to the array if the value is not already in the array.
appendIfUnique <array> <value>  --boolean
ex. (
	local h = #(1,2,3,4)
	appendIfUnique h 60 -- should work
	appendIfUnique h 4 -- shouldn't work
	if ((h.count != 5) or (h[5] != 60)) do
	throw "Entry 5 in the array is incorrect"
	format "%\n" h
-- RESULT:
-- #(1, 2, 3, 4, 60)
-- OK


--Convert collection to an array.
<collection> as array 



--creates a copy of all the elements in the array.
-- If #noMap is specified, the copy made is what is called a shallow copy 
-- - only a copy of the upper-level value itself (that is, the array value) is created. 
-- Copies aren't made of values stored in the array, rather a reference to the same value 
-- is stored in both array values.
copy <array> [#noMap] -- mapped 
-- Returns a value of OK .


--creates a copy of all elements in the array, including nested sub-arrays
deepCopy <array> --returns the new array


-- Delete element indexed by number from array, shrinking it in size by 1.
deleteItem <array> <number> --Returns the resulting array.



--Appends all the elements of the second argument to the array (first) argument.
join <array> <collection> 


--Inserts the value at the specified index in the array, growing the array if necessary.
insertItem <value> <array> <integer> --Returns OK.


--compare elements
-- performs a MAXScript '==' comparison between elements in the array and 
-- the target object and then returns the index of the first occurrence of 
-- the given value in the array or 0 (zero) if the value is not in the array.
-- Values such as Point3s and Strings match if they have the same contents.
findItem <array> <value> 


--Sorts the elements of the array into ascending order. All the elements must be comparable.
sort <array> 


--Sort and compare elements
-- Sorts the array using the specified function for element-by-element comparison. 
-- The comparison function must take 2 values as arguments, and return an integer number < 0 
-- if the first value is less than the second value, 0 if the values are equivalent, and 
-- an integer number > 0 if the first value is greater than the second value. The entire array is sorted 
-- unless a start or end value is specified.
qsort <array> <function> [start:<integer>] [end:<integer>] [user-defined key args passed to function] 
-- The following script generates 10 random positions, and then sorts 
-- the positions based on their distance from [0,0,0]:
-- positions =for i = 1 to 10 collect (random [0,0,0] [100,100,0])
fn compareFN v1 v2 =
local d = (length v1)-(length v2)
case of
(d < 0.): -1
(d > 0.): 1
default: 0
 
qsort positions compareFN
for p in positions do print p

-- All key arguments are passed to the comparison function. 
--This allows you to do things like an indexed sort:
fn compareFN v1 v2 valArray: =
	local v1i = valArray[v1]
	local v2i = valArray[v2]
	local d = (length v1i) - (length v2i)
	case of
		(d < 0.): -1
		(d > 0.): 1
		default: 0
positions = for i = 1 to 10 collect (random [0,0,0] [100,100,0] )
indexArray = for i = 1 to positions.count collect i
qsort indexArray compareFN valArray:positions
 
for i = 1 to positions.count do print positions [indexArray[i] ]


--Binary search in a sorted list of arrays
bsearch <key> <array> <function> [start:<integer>] [end:<integer>] [user-defined key args passed to function] 


--Returns minimum value of items in the array or of the argument values. 
amin ( <array> | {value} ) 
myMin1 = amin #(5,1,4,2,8)
myMin2 = amin 5 1 4 2 8


--Returns maximum value of items in the array or of the argument values. 
-- If the array size is zero or no arguments are specified, the value undefined is returned.
-- the elements in an array are stored by reference rather than by value. 
-- When you operate directly on array elements, and the reference to the array is stored in 
-- more than one place, unexpected results may occur.
amax ( <array> | {value} ) 
RandomSets=#() -- create array
RandomSet=#() -- create array
for i = 1 to 3 do -- loop i
(for j=1 to 3 do -- for each i loop j
RandomSet[j] = random 1 100 -- set array element to random value
print RandomSet #nomap -- print array of random values
RandomSets[i] = RandomSet -- store random value array in array
print RandomSets -- print array of arrays of random values 
-- OUTPUT:
-- #() -- result of line 1
-- #() -- result of line 2
-- #(33, 47, 31) -- output from line 6, i =1
-- #(4, 52, 39) -- output from line 6, i =2
-- #(52, 36, 23) -- output from line 6, i =3
-- OK -- result of for loop, lines 3 to 8
-- #(52, 36, 23) -- 3 lines of output from line 7
-- #(52, 36, 23)
-- OK -- result of line 9 


--Frees the memory used by the array value without waiting for garbage collection.
free <array>





-- Dictionarys
d = Dictionary #(#ss, 1) #(#tt, 2)
for i in d do print i
-- RESULTS
-- Dictionary #name ss:1 tt:2 
-- (DataPair key:#ss value:1)
-- (DataPair key:#tt value:2)


Dictionary() -- empty dictionary of type #name
Dictionary (#integer | #name | #string) -- empty dictionary of the specified type
Dictionary {#(key, value)}+ -- one or more two-value arrays
Dictionary {key:value}+ -- one or more explicit key:value pairs
Dictionary {(DataPair key value)} -- one or more DataPair objects


-- A count of items in the dictionary
<dictionary>.count : Integer, read-only

-- The type of the dictionary, which can be #name, #string, #integer.
<dictionary>.type read-only 

-- An array of the dictionary's keys. Note: changing this array does not affect the dictionary.
<dictionary>.keys : Array, read-only

-- Gets the value for key. If there is not an entry for the key, the value undefined is returned.
<dictionary>[key] 

-- Sets the value for key. An existing entry does not need to exist for the key.
<dictionary>[key] = <value>

-- Gets a value from the dictionary based on key. If there is no entry for the key, a value of undefined is returned.
GetDictValue <dictionary> <key >

-- Sets the value for an existing entry in dictionary based on key. If there is no entry for the key, nothing happens.
SetDictValue <dictionary> <key > <value>

-- Puts a value in dictionary based on key.
-- If putOnlyIfNew is true, the value is added only if there is no existing entry for the key.
PutDictValue <dictionary> <key > <value> putOnlyIfNew:<bool> -- defaults false

-- Removes the existing entry in the dictionary based on key
RemoveDictValue <dictionary> <key >

-- Returns whether there is an existing entry in the dictionary for the given key
HasDictValue <dictionary> <key >

-- Returns an array of key values in the dictionary.
GetDictKeys <dictionary>

-- Returns the key type of the dictionary - #name, #string, or #integer.
GetDictKeyType <dictionary>

-- creates a shallow copy of the dictionary. 
copy <dictionary> [#nomap]

-- Frees the internal memory associated with the dictionary.
free <dictionary>




--convert bit array to array
--You can convert a bitArray to an Array, and an Array containing only true and false values to bitArray.
--A bit in a BitArray can be either set (1, true) or not set (0, false).
ex. MaxPlus.Core.EvalMAXScript("fn bitArrayToArray b = (return b as Array)")
	rt.bitArrayToArray(bitArray)









"TRANSFORM: //-------------------------------------------------------------"



--query position
INode.Position
ex. $.position


--move
--absolute
$.position = [10,10,0] --same as $.pos
--adds x,y,z to the positions of all objects whose names contain "_left"
$*_left*.position += [50,20,10]
--relative
move $ [10,0,0]	--xyz
rt.move(obj, rt.point3(0,0,0))
rt.selection.move(rt.point3(0,0,0)) -- mapped
rt.selection.pos.z = 0
rt.selection.position.z = rt.selection.position.z + 10 --move relative


--scale
scale <node> <point3> -- mapped
--absolute
INode.Scaling
scale $ [2,2,1]		--scale 2x in xy.  z is 1:1 unchanged
$.scale = [1,1,2] --scale 2x in z

--
MaxPlus.Point3(ScaleAmount, ScaleAmount, ScaleAmount)

box = MaxPlus.Factory.CreateGeomObject(MaxPlus.ClassIds.Box)
box.ParameterBlock.Length.Value = 10.0
box.ParameterBlock.Height.Value = 10.0
box.ParameterBlock.Width.Value = 10.0


--rotate
--absolute
obj.Rotation
rt.rotate(node, rt.angleaxis(90, [0,1,0])) --rotate 90 on Y axis
--using transform matrix
currentMatrix = obj.transform
rt.preRotate(currentMatrix, rt.eulertoquat(rt.eulerAngles(0, 90, 0)))
obj.transform = currentMatrix

--rotate relative
obj.rotation = rt.eulerangles(0, 0, 90)
euler = rt.eulerangles(0, 0, 90)
rt.rotate(self.node, euler)

$*_left*.position += [50,20,10] -- adds 50,20,10 units (x,y,z order) to the positions
                                  -- of all objects whose names contain "_left"
--
rotate <node> <angle> <axis_point3> -- mapped -- angle in degrees 
rotate <node> <quat> -- mapped 
rotate <node> <eulerangles> -- mapped 

--
--queries the transform axis of the indexed axis system of the node 
getTransformAxis (<node>|undefined) <index> --returns as a matrix3 value

--queries the transformation matrix of the givennode or rootnode
getNodeTM {<node> | <rootnode>} --returnsas a matrix3 value

--Returns the transform controller for the node
getTMController <node>

--Computes the distance between the pivot points of the two specified nodes.
distance <node> <node>




--Snap
--Get/Set snap mode state
snapMode.active --boolean
state = snapMode.active
snapMode.active = not state

--Get/Set the current snap type as a name. Possible names are #2D , #2_5D , #3D
snapMode.type
snapMode.toFrozen
snapMode.axisConstraint
snapMode.useAxisCenterAsStartSnapPoint
snapMode.strength
snapMode.snapRadius

--System Global which contains true if the Marker is currently snapped to something
snapMode.hit --undefined if Snaps are not active

--System Global which contains the node currently being snapped to
snapMode.node --undefined if not snapped to a node or if Snaps are not active

--System Global which contains the Snap System Flags as an integer
snapMode.flags --undefined if Snaps not active

--System Global which contains the last Snap Point as Point3 coordinate in local coordinates of the node snapped to.
snapMode.hitPoint --undefined if Snaps are not active.

--System Global which contains the last Snap Point as Point3 world coordinate.
snapMode.worldHitpoint --undefined if Snaps are not active.

--System Global which contains the last Snap Point as a Point3 screen coordinate.
snapMode.screenHitPoint --undefined if Snaps are not active.

--System Global which contains the last Snap Point as point3 world coordinate.
snapMode.refPoint --undefined if Snaps are not active.

--System Global which contains the first snap point as point3 world coordinate.
snapMode.topRefPoint --undefined if Snaps are not active.

--System Global which contains the number of OSnaps as an integer.
snapMode.numOSnaps --1"Body", 2"NURBS", 3"Standard", 4"Standard", 5"Standard", 6"Standard"

--Returns true if the indexed OSnap item in the indexed OSnap is active
snapMode.getOSnapItemActive <int osnap_index> <int osnap_item_index> 
-- snapMode.active  --set snapmode active
state = snapmode.getOSnapItemActive 4 1
snapmode.getOSnapItemActive 4 1 (not state)

--Returns the name of the indexed OSnap item in the indexed OSnap as string.
snapMode.getOSnapItemName <int osnap_index> <int osnap_item_index> 
snapMode.getOSnapItemName <int osnap_index> <int osnap_item_index>
-- Returns the name of the indexed OSnap item in the indexed OSnap as string.

-- http://www.cgplusplus.com/online-reference/maxscript-reference/source/snapmode.htm

-- 1: name: "Body Snaps"
--  2: name: "End Edge"; tooltip: ""; state: false
--  3: name: "Edge"; tooltip: ""; state: false
--  4: name: "Edge Midpoint"; tooltip: ""; state: false
-- 2: name: "NURBS"
--  1: name: "CV"; tooltip: ""; state: false
--  2: name: "Point"; tooltip: ""; state: false
--  3: name: "Curve Center"; tooltip: ""; state: false
--  4: name: "Curve Normal"; tooltip: ""; state: false
--  5: name: "Curve Tangent"; tooltip: ""; state: false
--  6: name: "Curve Edge"; tooltip: ""; state: false
--  7: name: "Curve End"; tooltip: ""; state: false
--  8: name: "Surf Center"; tooltip: ""; state: false
--  9: name: "Surf Normal"; tooltip: ""; state: false
--  10: name: "Surf Edge"; tooltip: ""; state: false
-- 3: name: "Point Cloud Objects"
--  1: name: "Point Cloud Vertex"; tooltip: ""; state: true
-- 4: name: "Standard"
--  1: name: "Grid Points"; tooltip: ""; state: false
--  2: name: "Grid Lines"; tooltip: ""; state: false
-- 5: name: "Standard"
--  1: name: "Pivot"; tooltip: ""; state: false
--  2: name: "Bounding Box"; tooltip: ""; state: false
-- 6: name: "Standard"
--  1: name: "Perpendicular"; tooltip: ""; state: false
--  2: name: "Tangent"; tooltip: ""; state: true
-- 7: name: "Standard"
--  1: name: "Vertex"; tooltip: ""; state: false
--  2: name: "Endpoint"; tooltip: ""; state: false
--  3: name: "Edge/Segment"; tooltip: ""; state: false
--  4: name: "Midpoint"; tooltip: ""; state: false
--  5: name: "Face"; tooltip: ""; state: false
--  6: name: "Center Face"; tooltip: ""; state: false







-- pivot
--mapped functions
rt.ResetXForm(rt.selection) --#Same as the Reset XForm utility in the Utilities tab - applies XForm modifier to node, stores the current transformations in the gizmo and resets the object transformations.
rt.ResetPivot(rt.selection) --#Same as Hierarchy/Pivot/Reset Pivot.
rt.ResetScale(rt.selection) --#Same as Hierarchy/Pivot/Reset Scale.
rt.ResetTransform(rt.selection) --#Same as Hierarchy/Pivot/Reset Transform.

rt.CenterObject(rt.selection) --#Same as Hierarchy/Pivot/Affect Object Only - Center to Pivot.
rt.CenterPivot(rt.selection) --#Same as Hierarchy/Pivot/Affect Pivot Only - Center to Object.

rt.AlignToParent(rt.selection) --#Aligns the pivot to the node's parent's pivot, or to world if no parent.
rt.AlignObject(rt.selection) --#Same as Hierarchy/Pivot/Affect Object Only - Align to Pivot.
rt.AlignPivot(rt.selection) --#Same as Hierarchy/Pivot/Affect Pivot Only - Align to Object.
rt.WorldAlignObject(rt.selection) --#Same as Hierarchy/Pivot/Affect Object Only - Align to World.
rt.WorldAlignPivot(rt.selection) --#Same as Hierarchy/Pivot/Affect Pivot Only - Align to World.





--place instances of object at pivots of selected objects
for obj in selection do instance $Downlight001 pos:obj.pos











"VECTORS: //---------------------------------------------------------------"











"MATRICES: //--------------------------------------------------------------"












"CREATE: //----------------------------------------------------------------"


--[Primitives]
--http://docs.autodesk.com/3DSMAX/16/ENU/MAXScript-Help/index.html?url=files/GUID-BD5ADFE5-379A-40D5-8FA2-3EB9649F088B.htm,topicNumber=d30e280686
--universal attributes
name=''
pos=rt.point3(0,0,0) --position
wireColor=rt.color('red') --wireframe color
isSelected=True --bool

--cube
rt.Box(width=25, length=25, height=25, lengthsegs=1, widthsegs=1, heightsegs=1)
--sphere
rt.Sphere(radius=15, segs=1, smooth=True, hemisphere=0, chop=0, recenter=False, slice=False, sliceFrom=0, sliceTo=0) --#slice=slicing state on or off with sliceFrom and sliceTo values 0.0 - 1.0
--cylinder
rt.Cylinder(radius=10, height=25, heightsegs=1, capsegs=1, sides=12, smooth=True, slice=False, sliceFrom=0, sliceTo=0) --#slice=slicing state on or off with sliceFrom and sliceTo values 0.0 - 1.0
--pipe
rt.Tube(radius1=5, radius2=8, height=25, sides=12, capSegs=1, hightSegs=1)
--plane
rt.Plane(length=25, width=25, lengthsegs=1, widthsegs=1)
--cone
rt.Cone(radius1=15, radius2=1, height=25, heightsegs=1, capsegs=1, sides=12, smooth=True, slice=False, sliceFrom=0, sliceTo=0) --#slice=slicing state on or off with sliceFrom and sliceTo values 0.0 - 1.0
--pyramid
rt.Pyramid(width=25, depth=25, height=25, widthsegs=1, depthSegs=1, heightsegs=1)
--torus
rt.Torus(radius1=20, radius2=5, segs=12, tubeRotation=0, tubeTwist=0, sidesInteger=6, smoothInteger=0) --#smoothinteger: #0-None (Turns off smoothing entirely, producing prism-like facets on the torus.), 1-Sides (Smoothes the edges between adjacent segments, producing smooth bands running around the torus.), 2-All (Produces complete smoothing on all surfaces of the torus.), 3-Segments (Smoothes each segment individually, producing ring-like segments along the torus.)
--geosphere
rt.GeoSphere(radius=15, segs=4, smooth=True, hemisphere=False, baseToPivot=False, baseType=2) --#baseType: #0-Tetra (Based on a four-sided tetrahedron. The triangular facets can vary in shape and size. The sphere can be divided into four equal segments.), 1-Octa (Based on an eight-sided octahedron. The triangular facets can vary in shape and size. The sphere can be divided into eight equal segments.), 2-Icosa (Based on a 20-sided icosahedron. The facets are all equally sized equilateral triangles. The sphere can be divided into any number of equal segments, based on multiples and divisions of 20 faces.)
--textplus
rt.TextPlus(layouttype=0, width=100, length=100)








-- test whether a given node is convertible into a given class
--[ Mesh, SplineShape, NURBSCurve, NURBSSurface, etc.]
canConvertTo <node> <class>
if canConvertTo $foo NURBSSurface then...

--general form of the existing specific conversion functions such as convertToMesh()
ex. rt.convertTo(obj, rt.<class>) -- mapped
ex. convertTo $circle01 SplineShape --If the conversion is not supported, returns undefined.

--Convert an object to an editable mesh
--it will remove all modifiers present
convertToMesh <node> -- mapped
convertToMesh()

--These functions work on those primitive geometry and shape classes that support 
--conversion to NURBS (such as boxes, spheres, circles, lines, etc.)
--Convert to a SplineShape object.
convertToSplineShape <node> -- mapped 
--Convert to a NURBSSurface
convertToNURBSSurface <node> -- mapped 
--Convert to a NURBSCurve
convertToNURBSCurve <node> -- mapped 








"MODIFIERS: //-------------------------------------------------------------"



--open modifier panel.
ex. maxEval ('max modify mode')
ex. if getCommandPanelTaskMode() != #modify do (max modify mode)

--get selected modifier
ex. rt.modPanel.getCurrentObject()

--get modifier by name:
ex. rt.selection[0].modifiers['TurboSmooth']
--set modifier by name
ex. rt.modPanel.setCurrentObject(obj)

--get modifier by index:
ex. rt.selection.modifiers[-1].renderIterations
--set modifier by index
ex. rt.modPanel.setCurrentObject(obj.modifiers[0])

--get index
ex. index = rt.modPanel.getModifierIndex(obj, m)
ex. index = [m for m in obj.modifiers].index(m)+1 --add one to convert index from python to maxscript

--set index


--get modifier class id:
ex. print sel.modifiers[0].classID
--create with class id:
MaxPlus.Factory.CreateWorldSpaceModifier(MaxPlus.Class_ID(0x000110b4, 0x00007f9e))


--add modifier to top of stack:
--addModifier $ (Bend())	--add bend modifier to selected
ex. obj.AddModifier(rt.Taper(amount=1, primaryAxis=1)) --rt.addModifier(obj, mod, before=index)
ex. addModifier $ (Taper amount:1 primaryAxis:1)


--create modifier
m = rt.Smooth()
m.autoSmooth = True --set attributes
m.threshold = angle


--if not exists; create, else; modify.
obj = rt.selection[0]
m = obj.modifiers[rt.Symmetry] --or string 'Symmetry'
if not m:
	m = rt.symmetry()
	index = len(obj.modifiers) --add to bottom of stack (or before a specific modifier).
	rt.addModifier(obj, uv, before=index) --optional index.

m.axis = 0 #0(x), 1,(y), 2(z) --set attributes
m.flip = True #negative axis



--add to selection:
--Used in place of 'addModifier()' Applies a modifier above current stack index.
ex. rt.modpanel.addModToSelection(m)


--add modifier to components:
max modify mode-- open mod panel
select $box01-- select box01 into mod panel
subObjectLevel = 3-- subobject level to Face
addModifier $box01 (ffd_2x2x2())-- add FFD mod to those faces





--Tests whether a particular modifier or modifier class may be added the given <node> or 
--to all of the objects in the objectset or group.
validModifier [<node> | <objectset> | <group> ] <modifier |modifier_class> 

--enable/disable modifier
ex. obj.modifiers[2].enabled = False --turn off 2nd modifier
--sets the state of all modifiers of selected object to "Off in Viewport"
obj.modifiers.enabledInViews = off
--turn all the TurboSmooth modifiers off in viewport (stays on in render)
(getClassInstances TurboSmooth).enabledInViews = off
--all modifiers of a given class
ex. (getClassInstances turboSmooth).enabled=False


--Collapses the modifiers out of a stack
--collapse all:
collapseStack <node> -- mapped
--collapse to:
--maxOps.CollapseNodeTo <node>node <index>modIndex <boolean>noWarning
ex. rt.maxOps.CollapseNodeTo(obj, index, False)






--Takes either a modifier value which is present on the <node> stack, or an index 
--specifying the index of the modifier to delete, counting from the top of the stack.
deleteModifier <node> <modifier_or_index> -- mapped


--Prints a representation of the current modifier stack for the given node.
printStack <node>




enableShowEndRes <boolean> 

showEndResult 












"SELECTION: //-------------------------------------------------------------"


--select All
$*	

--get current selection
$ --returns 'undefined' if nothing selected

rt.selection

rt.getCurrentSelection() --returns the current selection as an array


--get only top-level nodes from selection
maxEval("select $/selection/*")

--add all children of currently selected nodes to the selection
for obj in selection do selectMore obj.children

--select instances and references of the selected node
select (refs.dependentNodes $.baseObject)


--select (for each geometry object, where the object doesn't have any texture vertices collect that object). i.e., this selects all objects without proper mapping coordinates
select (for obj in geometry where getNumTVerts obj == 0 collect obj)



--current mod panel object:
max modify mode --switch to Modify panel
rt.Modpanel.getcurrentObject()

rt.Filters.GetModOrObj()



SelectionManager.Nodes --provides an iterator for the selection list.
--You can now do the following:
def applyMaterialToNodes(m):
	for n in MaxPlus.SelectionManager.Nodes:
		n.Material = m


--select by name
--select object woth the name Box01
select <node> -- mapped
select $Box01		

--objects whose names start with 'Tile'
$Tile*					
--enclose in single quotes for searches containing whitespaces
$'Tile A'*			


--objects whose names contain either '_right' or '_left'
select ($*_right* as array + $*_left* as array)
--objects starting with 'Box' with height (in system units) bigger than 100
select (for obj in $box* where obj.height > 100 collect obj)
 


--Add a node to the set of selected objects.
selectMore <node> -- mapped

--query if the specified point is selected. NURBS, poly and spline objects.
isPointSelected <node> <point_index> 

--Returns a floating point weighted point selection if the object supports soft selections.
--Most object types just return 1.0 if the point is selected and 0.0 if not.
pointSelection <node> <point_index>



--number of selected objects
selection.count
--output to the script listener window
format "% objects selected." selection.count






--get component level
rt.getSelectionLevel(obj)

--set component level
--by index:
rt.subObjectLevel = 2
--'Object', 'Vertex', 'Edge', 'Face'
rt.setSelectionLevel(obj, 'Edge') --not working in python



numSubObjectLevels

IsSubSelEnabled()


--multi-component selection
obj.selectMode = 0 --off
obj.selectMode = 1 --sub-object selection preview
obj.selectMode = 2 --multi-component selection preview







-- convert component selection type
--'Object', 'Vertex', 'Edge', 'Border', 'Face', 'Element', 'CurrentLevel'
rt.selection[0].ConvertSelection('CurrentLevel', 'Face')



-- component selection
-- vertices
ex. rt.select(vertices)
ex. rt.polyop.setVertSelection(obj, verts) --select the vertices
ex. obj.EditablePoly.SetSelection('Vertex', rt.BitArray(10)) --bitarray value 9
-- edges
ex. rt.select(edges)
ex. rt.polyop.setEdgeSelection(obj, edges) --select the edges
ex. obj.EditablePoly.SetSelection('Edge', rt.BitArray(*range(10))) --bitarray range 0-9
-- faces
ex. rt.select(faces)
ex. rt.polyop.setFaceSelection(obj, faces)  --select the faces
ex. obj.EditablePoly.SetSelection('Face', rt.BitArray(*range(10, 20))) --bitarray range 10-19


vertices = rt.getVertSelection(obj) --get selected Vertices
edges = rt.getEdgeSelection(obj) --get selected edges
--using vertices
edges = rt.polyop.getEdgesUsingVert(obj, vertices)
faces = rt.getFaceSelection(obj) --get selected faces




--Deselect all.  Scene is redrawn unless redraw:false is specified.
clearSelection() clearNodeSelection [redraw:<boolean>] 
ex. rt.clearSelection()	--clears the current scene node selection


--Deselects the given node(s).
ex. rt.deselect(node) --deselects the given nodes
ex. deselect $box* --deselects all items whose names start with "box".

--Deselect a single node
ex. rt.deselectNode(node)

--substracts from selected objects named Dummy__ each ? substituting one character
deselect $Dummy??






-- selection sets
--object level
--get set by name
set_[name] --name can be either a String or Name value.
--get set by index
set_[int] --Indexes start at 1.
--
set_.count --returns the number of named selection sets as an int.
--create\replace a set
rt.selectionSets[name] = sel --creates or replaces a set by the given name
--create a set from objects starting with 'Box'
selectionSets["Boxes"] = $Box*
--
getNumNamedSelSets() --Returns the number of named selection sets as an integer.
--
getNamedSelSetName(int) --<set_index > Returns the name of the indexed named selection set as a string. <set_index> is 1 based.
--
getNamedSelSetItemCount(int) --<set_index > Returns the number of nodes in the indexed named selection set as an integer. <set_index > is 1 based.
--
getNamedSelSetItem(int, int) --<set_index> <node_index> Returns the indexed node in the indexed named selection set as a node. <set_index> and <node_index> are 1 based.
--get set by object
sets = {s.name:s for n,s in enumerate(rt.selectionSets, 1) for i in range(1, rt.getNamedSelSetItemCount(n)+1) if rt.getNamedSelSetItem(n, i)==obj}
--delete
rt.deleteItem(obj.faces, set) --the second argument can be the set name or set object.
--get empty sets
[s for s in rt.selectionSets if len(s)==0]



--component level
obj.faces[name] = rt.getFaceSelection(obj)
--get component level set from an object
sets = {s:set_array[s] for s in obj.faces.selSetNames}
[rt.bitarray(obj.edges[n]) for n in obj.edges.selSetNames] --for n in selection[1].edges.selSetNames do print (selection[1].edges[n] as bitarray)
--copy set
namedSelCopy()
--paste set
namedSelPaste()












"OBJECTS_&_ATTRIBUTES: //--------------------------------------------------"




-- naming
--set
obj.name = rt.uniqueName('')
rt.sphere(prefix="baz")

--get
--using wildcards:
ex. rt.matchPattern(obj.name, pattern='', ignoreCase=0)

--list containing Box001 and all its children (complete hierarchy)
$Box001*...* as array

--get object by name (get object from string):
ex. rt.getNodeByName('name_', ignoreCase=True, all=True) --Returns: the first node with the specified name. If all is True, an array of nodes with the specified name is returned.

--all objects that start with x
$Tile*

--If exact is false(default), the normal MAXScript node name comparisons are performed.
--If all is true, an array of nodes with the specified name is returned.
getNodeByName <string> exact:<bool> ignoreCase:<bool> all:<bool> --Returns first node with the specified name.
--[   Defaults:				 exact:false	ignoreCase:true 	all:false]
getnodebyname "AA" all:true
--($Teapot:aa @ [...], $Box:AA @ [...]) --returns all nodes named aa

--Access the base object in a scene node. This has relevance in nodes that have modifiers
--present that change the node type as it is processed up the stack. For example, a line 
--with an extrude modifier starts out as a Shape and turns into an Editable Mesh at the 
--top of the stack, its so-called world state. The baseObject property gives you access 
--to the base object in the modifier stack.
<node>.baseObject  A subclass of Node  default: varies
baseClass = classOf(obj.baseObject)


--store information about the geometry
INode.BaseObject.ParameterBlock


--check if obj is a node
ex. rt.IsValidNode(obj) --returns: boolean.

--check for existence
ex. [o for o in rt.objects if o.name=='name_']
--
ex. obj != undefined 



--get object type
--editable poly
ex. rt.Ribbon_Modeling.IsEditablePoly()
ex. rt.isKindOf(obj, rt.Editable_Poly)
ex. rt.isKindOf(obj, "Edit_Poly")



--check if shape object
isShapeObject <node>	--boolean

--query if the node's object is deformable. 
--A deformable object is an object with points that can be modified.
--isDeformable might return true for some nodes, 
--this does not necessarily mean that they can be deformed.
--while all geometry primitives return false but can be deformed.
isDeformable <node>

--Returns the number of deformable points for the node's object.
numPoints <node>

--Returns the position of the indexed point for the node's object.
getPointPos <node> <index> 

--Returns a 2 element array containing the min and max points of 
--the node's bounding box in coordinate system matrix3 as point3 values.
nodeGetBoundingBox <node> <matrix3>

--Returns a 2 element array containing the min and max points of the node's local bounding box
nodeLocalBoundingBox <node> 






--Object properties
showProperties $
--explicitly
showProperties ( VRayLight() )

--Retrieves the node's user property with the given key as a string. 
--<key_string> is either a String or a Name value.
getUserProp <node> <key_string>
--get property
eg. obj.getmxsprop('SelectByAngle')

--Sets the node's user property with the given key to the given value.
setUserProp <node> <key_string> <value>


--set property on selected object
$.<property> = value
ex. $.renderable = false
-- toggle
ex. $renderable = not $.renderable
--
obj.setmxsprop('SelectByAngle', True)


--This is effectively the contents of the User Defined Properties box in 
--the Object Properties dialog
getUserPropBuffer <node>

--Sets the user property buffer to the given string.
setUserPropBuffer <node> <string>



--Returns the rotation binding weight for the node.
getRotTaskWeight <node>

--Sets the rotation binding weight for the node.
setRotTaskWeight <node> <float> 

--Returns the position binding weight for the node.
getPosTaskWeight <node>

--Sets the position binding weight for the node.
setPosTaskWeight <node> <float> 

--query if the specified axis is turned on for position or rotation binding. 
--If an axis is turned off, the specified axis is no longer influenced by the 
--follow object or the IK Controller Position end effector . <pos_or_rot_integer> 
--sets whether the method returns the position state or the rotation state: 
--0 specifies position; 1 specifies rotation. 
--<axis_integer> sets the axis to check: 0 specifies X, 1 specifies Y, 2 specifies Z.
getTaskAxisState <node> <pos_or_rot_integer> <axis_integer> 

--Sets the axis state for position or rotation binding to the specified boolean value. 
--See getTaskAxisState() for a description of the parameters.
setTaskAxisState <node> <pos_or_rot_integer> <axis_integer> <boolean>

--Mirrors the specified IK constraints on the specified node's transform controller 
--about the specified axis . <axis_integer> specifies the axis of reflection: 
--0 for X, 1 for Y, 2 for Z . <pos_or_rot_integer> specifies which type of 
--constraints are being mirrored: 0 for position, 1 for rotation.
mirrorIKConstraints <node> <axis_integer> <pos_or_rot_integer>

--Call this method when one of the node level IK parameters has been changed.
nodeIKParamsChanged <node>

--query if the <ik_node> can be bound to the <node> as a follow object.
OKToBindToNode <ik_node> <node> --boolean





--query number of surfaces (loft objects)
numSurfaces <node>

--query if the node's showLinksOnly property is true .
isBoneOnly <node>





-- <node_constructor> [name: <string> ]
[ prefix: <string> ] 
[ material: <material> ] 
[ target: <node> ] 
[ pos: <point3> ] -- default [0,0,0] 
[ position: <point3> ] -- synonym for pos 
[ rotation: <quat> ] -- default 0 rotation 
[ scale: <point3> ] -- default 100% scale 
[ pivot: <point3> ] -- default normal node pivot location 
[ transform: <matrix3> ] -- default identity 
[ isSelected: <boolean> ] -- default false 
[ dir: <point3> ]-- set local z direction   

b = box name:"foo" position:[10,10,10] height:20

for i in 1 to 100 do sphere prefix:"baz"
--creates 100 spheres, giving each a unique name
--beginning with "baz", such as $baz01, $baz02, $baz03, etc.



--Computes the closest intersection of the ray and the surface of the given node. 
--Returns another Ray which defines the position of intersection in 3D space and the 
--surface normal direction vector at that point. The intersection test respects the 
--face normals of the node, i.e. if a face's normal points away from the ray's source, 
--an intersection test is not performed on that face.
intersectRay <node> <ray> 

--Takes a ray and computes the closest intersection to the surface of the given node.
--It returns an array with the following three elements.
--1) A Ray defining the position of intersection in 3-space and the surface normal 
--	 direction vector at the point.
--2) The index of the face the ray intersects with
--3) The barycentric coordinates of the face that was hit.
intersectRayEx <node> <ray>

--Performs intersectRay on all nodes in the scene.
--Returns an array of results, one entry per node hit, where each entry is a 2 element 
--array containing the node and the intersectRay result for that node.
intersectRayScene <ray>

--query if the bounding boxes of the two specified nodes overlap.
intersects <node> <node>	--boolean




--clone
-- All the clone operations can take any of the standard node creation optional keyword 
-- arguments which are applied after the node has been copied.
copy <node> -- mapped 
reference<node> -- mapped 
instance<node> -- mapped 

--query instance
areNodesInstances <node> <node>
InstanceMgr.GetInstances $ &rptInstances
trueInstances = for n in rptInstances where\
(areNodesInstances $ n) collect n

--http://docs.autodesk.com/3DSMAX/15/ENU/MAXScript-Help/files/GUID-48C5E2F2-DE34-4EA3-A84C-4DBD463DBF90.htm#WS73099CC142F487553098682E12AC2FC2BC7-58BD
maxOps.cloneNodes 

--generates a new node that contains a copy of the world-state mesh of the source
snapshot <node> -- mapped

--Returns world state of node as a <mesh> value.
snapshotAsMesh <node>

--Lets you turn existing nodes into instances and references to other nodes. 
--You can use these, for example, to replace the geometry of one node with another
instanceReplace <dest_node> <src_node> -- mapped 
referenceReplace <dest_node> <src_node> -- mapped 
ex. rt.instanceReplace('foo*', 'baz') --makes all the foo* objects be instances of baz's geometry & modifier stack.
--replace objects in selection with specified object (respecting the transforms)
instanceReplace selection $LampPost01




--Heirarchies
-- Makes <node2> a child of <node1> . Resets the current location of <node2> to 
-- the location of <node1> unless move:false is specified.
attachObjects <node1> <node2> [move:<boolean> ]

ex. rt.polyop.attach(obj, <source>) --Attaches <source>, converted to a polymesh if necessary, to <poly>.


-- Detach
--delete - delete faces after being detached.
--asNode True- the faces are detached as a separate node.
	--If asNode is True , <name> specifies the name of the new node.
	--If asNode is True and is an Editable Poly (not a node), <node> must be specified.
--asNode False - the faces are detached as an element.
--detach faces used by verts:
ex. rt.polyop.detachVerts(obj, <vertlist>, delete=True, asNode=False, name="Object01") --Returns true if the operation is successful.
--detach faces used by edges:
ex. rt.polyop.detachEdges(obj, <edgelist>, delete=True, asNode=False, name="Object01")
--detach faces:
ex. facelist = rt.polyop.getelementsusingface(obj, 1) --use element or face
	rt.polyop.detachFaces(obj, <facelist>, delete=True, asNode=True, name="Object01")



--Group nodes. 
--You can optionally specify the group name or group name prefix. 
--Specifying select:true selects the group after it is made.
group <node_collection> [name:<string> ] [prefix:<string> ] [select:<boolean> ] --returns the group node.
group $box* name:"boxes"--makes a group of all box*'s named "boxes".
group selection--groups current selection. 

--Attaches a node collection to an existing group. 
--Nodes that are already members of a group cannot be attached to another group.
attachNodesToGroup <node_collection> <targetNode> 


--set the group open
--for each object, where the object is a Head of a group.
for obj in objects where isGroupHead obj do setGroupOpen obj on


--Detaches the specified nodes from the groups they belong to.
detachNodesFromGroup <node_collection>

--Ungroups one level of a group node.
ungroup <group_head_node> -- mapped 
ungroup $group01--ungroups group $group01 

--Ungroups all levels in a group node.
explodeGroup <group_head_node> -- mapped 




--Viewport Display
--show/hide
ex. rt.hide(obj) -- mapped --Hides the specified node or node collection.
--If the optional doLayer keyword is set to true and the node is in a layer that is hidden,
--the entire layer is unhidden. When false (the default), just the node is unhidden.
unhide <node> [doLayer:<boolean>] -- mapped 

--hide all children in scene (leave only top-level nodes)
maxEval("hide $*/*")

--query visability
ex. obj.isHiddenInVpt
ex. obj.isHidden = True

--xray
ex. g.xray = True


--freeze
ex. freeze(obj) -- mapped --Freezes the specified node or node collection.
--If the optional doLayer keyword is set to true and the node is in a layer that is frozen, 
--the entire layer is unfrozen. When false (the default), just the node is unfrozen.
unfreeze <node> [doLayer:<boolean>] -- mapped

ex. obj.isFrozen == True



--Sets whether the node is renderable.
setRenderable <node> <boolean>


--query if node is displayed using vertex colors in shaded viewports, false otherwise.
getCVertMode <node> 

--Sets whether to display the effect of assigned vertex colors for the node in shaded viewports.
setCVertMode <node> <boolean>

--query if the vertex color display for the node is shaded in the viewports
getShadeCVerts <node> 

--Sets whether the vertex color display for the node is shaded in the viewports. 
--When true , the colors are unshaded and appear in their pure RGB values. 
--When false , the colors appear like any other assigned color in the viewports.
setShadeCVerts <node> <boolean>




--instance object:
--http://help.autodesk.com/view/3DSMAX/2018/ENU/?guid=__files_GUID_EB69A035_7FF4_4A0A_8A82_409C4145B9DF_htm
--uninstance:
i=rt.instancemgr
for obj in rt.selection:
	if i.CanMakeObjectsUnique(obj):
		i.MakeObjectsUnique(obj, 'prompt') --#uninstance obj




--filter geometry Objects
ex.	for obj in objects where classof obj == VRayLight do
		print obj;

-- alternative method
-- performs the loop through all objects in MAXScript, but instead of calling SuperClassOf 
-- o == GeometryClass it checks whether the class of the object is part of the list of valid 
-- geometryClass class objects
ex. for obj in objects where findItem geometryClass.classes (classof obj) > 0 collect obj
--
ex. [[o for o in rt.objects if rt.matchPattern(o.name, pattern=f, ignoreCase=0)] for f in list_] --#all objects that match criteria


--[Object Sets]
--ObjectSets are collections of the current scene objects divided into the main 3ds max 
--object type categories/classes

objects 	--allobjects in the scene
geometry	--primitives, meshes, other geometry types
lights		--including VRay and third party
cameras		--
helpers		--
shapes		--lines, circles, rectangles, splines
systems		--eg. bones
spacewarps--forces, spacewarps, deflectors, etc
selection --current selection. interchangable with $


--convert objectSet to array
ex. <objectSet> as array
ex. rt.array(*list_)



--delete node
rt.delete(obj) -- mapped

-- When a node has been deleted,
obj == undefined --returns false
obj != undefined --returns true

--query if object still exists in the scene, as in variables or arrays.
rt.isDeleted(<MAXWrapper_object>) --returns boolean


--delete object with specified name from scene. 
--handling special characters in objects' names using single quotes
delete $'car.wheel.*'









"COMPONENTS: //------------------------------------------------------------"




--create
ex. rt.polyop.createVert(obj, <point3 pos>) --creates a vertex as the specified position.
ex. rt.polyop.createEdge(obj, <int vert1>, <int vert2>) --Returns the index of the created edge or undefined if no edge was created.
ex. rt.polyop.createPolygon(obj, <vertex array>) --creates a face using the specified vertices.


ex. vertices = list(range(1, rt.polyop.getNumVerts(obj)))
ex. vertices = list(range(1, obj.verts.count))
ex. edges = list(range(1, rt.polyop.getNumEdges(obj)))
ex. edges = list(range(1, obj.edges.count))
ex. faces = list(range(1, rt.polyop.getNumFaces(obj)))
ex. faces = list(range(1, obj.faces.count))


--get position
ex. rt.polyop.getVert(obj, <int vertex>) --Returns the position of the specified vertex.

--set position
ex. rt.polyop.setVert(obj, <vertlist>, {<point3 pos>|<point3 pos_array>}) --Sets the position of the specified vertices.




--get selection
ex. rt.polyop.getVertSelection(obj) --Returns the current vertex selection as a bitarray.
ex. vertices = [i.index for i in obj.selectedVerts] --Returns list
--alt
ex. obj.selectedVerts()
ex. rt.polyop.getEdgeSelection(obj) --Returns BitArray
ex. edges = [i.index for i in obj.selectedEdges] --Returns list
ex. rt.polyop.getFaceSelection(obj) --Returns BitArray
ex. faces = [i.index for i in obj.selectedFaces] --Returns list


--set selection
ex. rt.polyop.setVertSelection(obj, <vertlist>) --Sets the current vertex selection based on <vertlist>.
ex. rt.polyop.setEdgeSelection(obj, <edgelist>)
ex. rt.polyop.setFaceSelection(obj, <facelist>)


--hidden
ex. rt.polyop.getHiddenVerts(obj) --Bits in the result bitarray are set if the corresponding vertex is hidden.
ex. rt.polyop.setHiddenFaces(obj, <facelist>) --Hides the corresponding faces in the poly
ex. rt.polyop.setHiddenVerts(obj, <vertlist>) --Hides the corresponding vertices in the poly.
ex. rt.polyop.getHiddenFaces(obj) --Bits in the result bitarray are set if the corresponding face is hidden.
--unhide
ex. rt.polyop.unHideAllFaces(obj) --Unhides all faces in the poly.
ex. rt.polyop.unHideAllVerts(obj) --Unhides all vertices in the poly.

--visibility
--get
ex. rt.polyop.getEdgeVis(obj, <int edge>) --Returns true if the specified edge is visible, false otherwise.
--set
ex. rt.polyop.setEdgeVis(obj, <edgelist>, <boolean>) --Sets the visibility of the specified edges.



--get number of
ex. rt.polyop.getNumVerts(obj) --Returns the number of vertices in the poly. Includes any dead vertices.
ex. obj.selectedVerts.count --Returns number of selected vertices
--vertices from face
ex. rt.polyop.getFaceDeg(obj, <int face>) --Returns the number of vertices in the specified face.
--vertices and faces
ex. rt.getPolygonCount(obj)	--Returns a 2 element array [#of faces, #of vertices]
ex. rt.polyop.getNumEdges(obj)
ex. rt.polyop.getNumFaces(obj)
--face: get number corners
ex. obj.GetFaceDegree(<face index>) --Returns the number of corners of the specified polygon. 3 means triangle, 4 means quad, and so on.




--get one component type from another
--from vert:
ex. rt.polyop.getEdgesUsingVert(obj, <vertlist>) --Bits in the result bitarray are set if the corresponding edge uses one of the vertices in <vertlist>
ex. rt.polyop.getFacesUsingVert(obj, <vertlist>) --Bits in the result bitarray are set if the corresponding face uses one of the vertices in <vertlist> .


--from edge:
ex. rt.polyop.getEdgeVerts(obj, <int edge>) --Returns the edge's vertices as a 2 element array
ex. rt.polyop.getVertsUsingEdge(obj, <edgelist>) --Bits in the result bitarray are set if the corresponding vertex uses one of the edges in <edgelist> .
--get faces
ex. rt.polyop.getEdgeFaces(obj, <int edge>) --Returns the faces using the specified edge. Normally a 1 element (open edge) or 2 element array.
ex. rt.polyop.getFacesUsingEdge(obj, <edgelist>) --Bits in the result bitarray are set if the corresponding face uses one of the edges in <edgelist> .

--from face:
--get verts
ex. rt.polyop.getFaceVerts(obj, <int face>) --Returns the face's vertices as an array
ex. rt.polyop.getVertsUsingFace(obj, <facelist>) --Bits in the result bitarray are set if the corresponding vertex uses one of the faces in <facelist> .
ex. rt.polyop.getVertsUsedOnlyByFaces(obj, <facelist>) --Bits in the result bitarray are set if the corresponding vertex is only used by faces in <edgelist>.
--get edges
ex. rt.polyop.getFaceEdges(obj, <int face>) --Returns the face's edges as an array
ex. rt.polyop.getEdgesUsingFace(obj, <facelist>) --Bits in the result bitarray are set if the corresponding edge uses one of the faces in <facelist> .
--get edges/verts from multiple faces  --and construct dict ie. {<face index>:[list of components]}
ex. faces = [i.index for i in obj.selectedFaces]
	vertices = {face:rt.polyop.getFaceVerts(obj, face) for face in faces}
--get elements
ex. rt.polyop.getElementsUsingFace(obj, <facelist>) --Bits in the result bitarray are set for all faces in the same "element" or connected component with faces in <facelist>.


--Returns the vertex index of the Nth vertex used by the specified face (where, N is between 1 and the number of face corners).
ex. obj.GetFaceVertex(1, 1) --ie. Returns face 6. args=(vertex, corner)
ex. obj.GetFaceEdge(1, 1) --ie. Returns edge 1. args=(faceID, side)



--get component point coordinates
ex. target = rt.polyOp.getVert(obj, index[-1])
--group of vertices averaged:
ex. averageSelVertCenter <node> --Returns the average position (center) of the selected vertices in the given mesh as a Point3.
ex. target = rt.polyOp.getEdge(obj, index[-1])
ex. target = rt.polyOp.getFace(obj, index[-1])



--move 
--vertex
ex. rt.polyop.moveVert(obj, <vertlist>, {<point3 offset>|<point3 offset_array>})
--gets or sets the position of the selected element in the mesh
--<vertexselection>.pos : Point3 
$foo.verts[i].pos = $bar.verts[j].pos + [10,0,0]


--get length/area
--face area
ex. rt.polyop.getFaceArea(obj, <int face>)


--get center
--of face
ex. rt.polyop.getFaceCenter(obj, <int face>)--Returns the center of the face by taking the average of all its vertices.
ex. rt.polyop.getSafeFaceCenter(obj, <int face>) --Returns the "safe" center of the face, if possible. For non-convex faces, the average point found using getFaceCenter is unsuitable for some applications because it can lie outside the face. If a safe center cannot be found, a value of undefined is returned. 







--divide
--edge middle:
ex. rt.polyop.splitEdges(obj, <edgelist>)
--fraction
ex. obj.EditablePoly.divideEdge(edge, position) --position is a float value between 0-1 
ex. rt.polyop.divideEdge(obj, <int edge>, <float fraction>) --Divides the specified edge at the specified fractional distance along the edge. The return value is the index of the new vertex or undefined if no vertex was created.
--divide face
ex. rt.polyop.divideFace(obj, <int face>, <point3 pos>) --Divides the specified face, with the new vertex being created at the closest point on the face to the specified position. If the specified position is outside the face, the vertex will be created at the center of the face.



--merge /weld
--vertices
--selected
ex. obj.EditablePoly.SetSelection(#Vertex, #{1..1352})
	obj.EditablePoly.weldFlaggedVertices()
--to target
ex. rt.polyop.weldVerts (obj, <vertex1 index as int>, <vertex2 index as int>, <target as point3>) --Welds the two specified vertices with the resulting vertex positioned at the specified location.
ex. rt.polyop.weldVertsByThreshold(obj, <vertlist>)
ex. rt.polyop.collapseVerts(obj, <vertlist>)
--weld edge vertices 
ex. rt.polyop.weldEdges(obj, <int edge1>, <int edge2>) --Only vertices on a border can be welded.
--by threshold
ex. rt.polyop.weldEdgesByThreshold(obj, <edgelist>)



--collapse
--edges
ex. rt.polyop.collapseEdges(obj, <edgelist>)
--faces
ex. rt.polyop.collapseFaces(obj, <facelist>)



--open edges
ex. rt.polyop.getOpenEdges(obj) --Bits in the result bitarray are set if the corresponding edge is open (used by only 1 ace).
ex. rt.polyop.getBorderFromEdge(obj, <int edge>) --Bits in the result bitarray are set for open edges in the poly that are connected using open edges to the specified edge.




--remove
--vertex
ex. obj.EditablePoly.remove(selLevel='Vertex', flag=1) --flag 1 = currently selected
ex. obj.EditablePoly.remove(selLevel='Edge', flag=1)
ex. obj.EditablePoly.remove(selLevel='Edge', flag=1)


--delete (all sub-object elements that use the deleted elements are also deleted.)
--vertex
ex. rt.polyop.deleteVerts(obj, <vertlist>) --Deletes the specified vertices.
ex. rt.polyop.deleteIsoVerts(obj) --Deletes any vertices not used by any faces.
--edge
ex. rt.polyop.deleteEdges(obj, edges, delIsoVerts=1) --Deletes the specified edges. If <delIsoVerts> is true , any vertices that are no longer used by edges are also deleted.
--face
ex. rt.polyop.deleteEdges(obj, faces, delIsoVerts=1) --Deletes the specified faces. If <delIsoVerts> is true , any vertices that are no longer used by faces are also deleted.








--edge crease
--get
obj.EditablePoly.getEdgeData(1)
--set
obj.EditablePoly.setEdgeData(1, creaseAmount) --#crease edge




--get
obj.EditablePoly.setVertexData(1) --#Get the vertex data stored in the specified vertexDataChannel. The number of vertices with stored values in this channel will be written to the passed by reference variable numberSelected
--set
obj.EditablePoly.setVertexData(1, <int>)






"SYMMETRY: //--------------------------------------------------------------"



--get symmetry state on object
symmetry = obj.modifiers[rt.Symmetry] --returns None if no symmetry modifier present

--get/set axis
symmetry.axis --int. 0=X Axis, 1=Y Axis, 2=Z Axis

--flip source axis
symmetry.flip --bool. When set to true, uses the other half of the object as the source for symmetry.

--delete/slice opposing axis
symmetry.slice --int. When set to 1, slices the source geometry along the mirror plane and deletes the one half.

--weld seam
symmetry.weld -- int. When set to 1, welds the vertices of the source and mirrored halves together.

--welding threshold (animatable)
symmetry.threshold Float default: 0.1 --float vertices closer than the threshold value will be welded.

--Mirror gizmo transforms (animatable)
m = symmetry.mirror(SubAnim=Mirror) --transform; SubAnim. Controls the transformation of the Mirror gizmo
m.position(rt.Point3([0,0,0])) --Point3. The position of the Mirror gizmo.
m.rotation(rt.Quat([0,0,0,1])) --Quat. The rotation of the Mirror gizmo.
m.scale(rt.Point3([1,1,1])) --Point3. The scale of the Mirror gizmo.
m.value(rt.Matrix3([1,0,0] [0,1,0] [0,0,1] [0,0,0])) --Matrix3. The complete matrix3 transformation value of the Mirror gizmo.







"RIGGING: //---------------------------------------------------------------"














"NORMALS: //---------------------------------------------------------------"


--get vertex normals

--average vertex normals
ex. normal = rt.averageSelVertNormal(obj) --Returns the normalized average of the normals of the selected vertices in the given mesh as a Point3


--get face normal
ex. rt.getNormal(obj, <vert_index_integer>) --Returns the normal at the indexed vertex's position as a point3
ex. rt.polyop.getFaceNormal(obj, <int face>)

--set face normal
--Sets the indexed vertex's normal vector. setNormal(obj, <vert_index_integer> <point3>)
ex. rt.setNormal(obj, vertex, normal) --Returns the face normal of the face.


--get face smoothing groups
ex. obj.GetFaceSmoothingGroups(<index faceID>) --Returns the Smoothing Groups of the specified face.

--edge hardness
ex. obj.makeHardEdges(<DWORD>flag) --Sets the edges specified by the flag to Hard.
ex. obj.makeSmoothEdges(<DWORD>flag) --Sets the edges specified by the flag to Smooth.
ex. obj.selectHardEdges() --Selects all Hard Edges.
ex. obj.selectSmoothEdges() --Selects all Smooth Edges.


--auto smooth mesh
ex. rt.polyop.autoSmooth(obj) --The face smoothing threshold angle is a property (autoSmoothThreshold) of the editable poly.





--reverse face normal
ex. rt.polyop.flipNormals(obj, <facelist>) --Flips the normal of the specified faces.















"UV: //--------------------------------------------------------------------"


--Unwrap_UVW modifier:
uv = rt.selection[0].modifiers['Unwrap_UVW']


--cut:
uv.breakSelected()		--Presses the Break icon in the edit floater.
uv.detachEdgeVertices()	--Detaches any vertex that is not completely surrounded by selected vertices.


--sew:
uv.weld()				--Presses the Target Weld icon in the edit floater.
uv.weldSelected()		--Presses the Weld Selected button in the edit floater.
uv.weldOnlyShared(True) --only selected vertices will be welded. default: True
uv.WeldAllShared()		--Welds all shared vertices.
uv.WeldSelectedShared() --Welds the shared selected vertices.
uv.FlattenBySmoothingGroup(rescale=False, rotate=False, padding=0.2) --keyword args not working in pymxs
uv.FlattenByMaterialID(rescale=False, rotate=False, padding=0.2)
uv.stitchVerts(align=True, bias=1.0) --Bias of 0.0 the vertices will move to the source and 1.0 they will move to the target. 
uv.stitchVertsNoParams() --Execute the Stitch function using the current defaults.
--
uv.stitchVertsDialog()	--Open the Stitch dialog.
--get:
uv.getWeldThreshold()	--Returns the weld threshold.
--set:
uv.setWeldThreshold(height=0.1) --Sets the threshold values for welds.


--pack:
uv.packNoParams()		--Executes the Pack function using the current default settings.
uv.pack(method=1, spacing=0.01, normalize=True, rotate=False, fillholes=True) --Lets you pack the texture vertex elements so that they fit within a square space.
	--method - 0 is a linear packing algorithm fast but not that efficient, 1 is a recursive algorithm slower but more efficient.
	--spacing - the gap between cluster in percentage of the edge distance of the square
	--normalize - determines whether the clusters will be fit to 0 to 1 space.
	--rotate - determines whether a cluster will be rotated so it takes up less space.
	--fillholes - determines whether smaller clusters will be put in the holes of the larger cluster.
--
uv.packDialog()			--Opens the Pack UVs dialog.


--rescale:
uv.RescaleCluster(obj, facesel=[bitArray])
--get:
uv.GetPackRescaleCluster()
--set:
uv.SetPackRescaleCluster(rescale=True)


--sketch:
uv.sketchNoParams()		--Executes the Sketch function using the current defaults.
uv.sketch(indexList=[int array], positionList=[point3 array] --Sketches UV coordinates using the supplied index list array and the position list array.
uv.sketchReverse()		--Reverses the order of the select vertices that are being used for sketch when you use the Use Current Selection option.
--
uv.sketchDialog()		--Opens the Sketch Vertices dialog.


--straighten:
uv.straighten()


--relax:
uv.relax(1, 0.01, True, True)


uv.MirrorGeomSelection = False

uv.renderuv_seamedges = not uv.renderuv_seamedges
uv.renderuv_visibleedges = not uv.renderuv_visibleedges

--additional Unwrap_UVW:
['DisplayPixelUnits', 
'MirrorGeomSelection', 'MirrorSelectionAxis', 'MirrorSelectionThreshold', 
'PaintFallOff', 'PaintFallOffType', 'PaintFullStrength', 'PaintMoveBrush', 
'RelaxMoveBrush', 
'SelectionPreview',  
'TypeInLinkUV', 
'autoPin', 'filterPin',
'baseMaterial', 'baseMaterial_list', 'checkerMaterial', 'TextureCheckerMaterial',
'buttonpanel_height1', 'buttonpanel_height2', 'buttonpanel_visible', 'buttonpanel_width', 
'edgeSnap', 'vertexSnap', 'gridSnap', 
'editorHWnd', 'editorViewHWnd', 
'groupDensity', 'groupDisplay', 'groupName', 
'localDistortion', 
'peelAutoEdit', 
'quick_map_align', 'quick_map_preview', 
'renderuv_edgeColor', 'renderuv_edgealpha', 'renderuv_fillColor', 'renderuv_fillalpha', 'renderuv_fillmode', 'renderuv_force2sided', 'renderuv_height', 'renderuv_invisibleedges', 'renderuv_overlapColor', 'renderuv_seamColor', 'renderuv_seamedges', 'renderuv_showframebuffer', 'renderuv_showoverlap', 'renderuv_visibleedges', 'renderuv_width',  
'showImageAlpha', 'showTileGridlines', 
'splinemap_advanceMethod', 'splinemap_display', 'splinemap_iterations', 'splinemap_manualseams', 'splinemap_node', 'splinemap_projectiontype', 'splinemap_resampleCount', 'splinemap_uoffset', 'splinemap_uscale', 'splinemap_voffset', 'splinemap_vscale', 
'texMapIDList', 'texMapList', 
'toolBarVisible']



--UVW_Xform modifier:
uv = rt.selection[0].modifiers['Unwrap_UVW']


--additional UVW_Xform:
['Map_or_Vertex_Color', 
'Rotation_Angle', 'Rotation_Center', 
'U_Flip', 'V_Flip', 'W_Flip',
'U_Offset', 'V_Offset', 'W_Offset',
'U_Tile', 'V_Tile', 'W_Tile',
'map_channel']









"Materials: //-------------------------------------------------------------"





--create a new default material as follows:
m = MaxPlus.Factory.CreateDefaultStdMat()


--get currently selected material
ex. rt.medit.getCurMtl()
--get material by name
ex. rt.sceneMaterials['name']
--get all scene materials
ex. rt.sceneMaterials
ex. [m for m in rt.sceneMaterials]
--get material from face
ex. obj.GetFaceMaterial(face) --#Returns the material of the specified face.
--get all materials including submaterials
mats=[]
for mat in rt.sceneMaterials:
	if rt.getNumSubMtls(mat): --#if material is a submaterial; search submaterials
		for i in range(1, rt.getNumSubMtls(mat)+1):
			subMat = rt.getSubMtl(mat, i)
			mats.append(subMat)
	elif:
		mats.append(mat)
--get subMaterials
ex. [m for m in mat[0]]
ex. mat.materialList
--get subMaterial from face
ex. subMaterial = rt.getSubMtl(mat, rt.GetFaceMatID(obj, face)) --#get the submaterial using the matID index
--get all subMaterials from material
ex. subMaterials = [rt.getSubMtl(mat, id) for id in range(1, rt.getNumSubMtls(mat)+1)] --#get the material using the matID index. modify index range for index starting at 1.
	subMatNames = [s.name for s in subMaterials if s is not None]
--get number of subMaterials
ex. len([mat[0])
ex. rt.getNumSubMtls(mat)
ex. mat.materialList.count
ex. mat.numsubs --#total number of indices. includes undefined material slots. ie. material at ID index 1 and another at index 20, returns 20 with 18 undefined indices.

--get subMaterial ID's
ex. mat.materialIDList
--get subMaterial ID from face
ex. id = rt.polyop.getFaceMatID(obj, face) --Returns the material ID assigned to the face #ex. rt.GetFaceMatID(obj, f)
--get face from subMaterial ID
ex. [i for i in range(1, obj.numFaces+1) if rt.getFaceMatID(obj, i)==id]



--set material to object
ex. obj.material = mat
	mat.materialList.count = mat.numsubs+1 --#add slot to multimaterial
	mat.mapEnabled[3] = True
	mat.materialIDList[3] = 2
	mat.names[3] = ''
	mat.materialList[-1] = material --#assign material to the newly created slot 
--set subMaterial
ex. rt.setSubMtl(mat, id, newMat) --#sets the indexed sub material to the specified material.
--set material id to face
ex. rt.polyop.setFaceMatID(obj, face, <int MatID>) --Assigns the material ID to the face
--set material id to a list of faces
ex. [rt.setFaceMatID(obj, f, <int MatID>) for f in faces] --#Assigns the material ID to a list of faces



--create standard material
material = rt.StandardMaterial(name='')
--create multimaterial
material = multiMaterial()
material = rt.VRayMtl()



--assign attributes:
material.diffuse = color 255 0 0
--vray
material = VRayMtl diffuse:green reflection:grey reflection_glossiness:0.7




--set attributes
m.Diffuse = rt.color(r, g, b) --MaxPlus.Color(0, 0, 1)
m.name = ''



mat.effectsChannel --All the material subclasses can access the effectsChannel property and specify it as a constructor parameter.
mat.showInViewport --Accesses the material-level show-in-viewport state, which can also be set on a material constructor call using the showInViewport : parameter.


--rename
ex. material.name = "name"
ex. obj.name = rt.uniqueName()
assignNewName <material> --Modifies the name of the specified material to make it unique. The name is of the form "Material #1" where the number is incremented as required to make ensure it’s unique.


--delete material
material = undefined
--delete materials from all objects
rt.objects.mat = undefined




--Slate Material Editor

--open/close
ex. if not rt.SME.isOpen(): rt.SME.open()
ex. rt.SME.Close()
ex. rt.SME.OpenMtlBrowseDlg() --material browser submenu


--create new view
ex. rt.SME.CreateView('name') --creates a new Node View with the given name and returns its index.
--create temp view
ex. if rt.SME.GetViewByName('temp'):
		rt.SME.DeleteView(rt.SME.GetViewByName('temp'), False)
	index = rt.SME.CreateView('temp')
	view = rt.SME.GetView(index)


--get active view
ex. rt.SME.activeView --returns index. not callable ie. activeView()
--set active view
ex. rt.SME.activeView(index) --set index


--get view index by name
ex. rt.SME.GetViewByName('name') --Returns the index of the named Node View
--get view object by index
ex. rt.SME.GetView(index) --Returns an IObject:IFP_NodeViewImp object representing the indexed Node View.
--get view index by view object
ex. rt.SME.GetViewIndex(view) --Returns the index of the given Node View


--get/set view properties:
view = rt.SME.GetView(rt.SME.activeView)
--get view name
ex. view.name
--set view name
ex. view.name('name')
--number of nodes in view
ex. view.GetNumNodes() --Returns the number of nodes in the View.
--get node interface
ex. view.GetNode(index) --Returns the Node Interface of the indexed node from the View.
--get node interface by reference
ex. view.GetNodeByRef(<ref object>) --Returns the Node Interface to the given Material or Map object reference, or undefined if the reference does not exist.

--create/show node in graph
ex. node = view.CreateNode(mat, rt.point2(0, 0))
--show material parameters rollout


--delete view
ex. rt.SME.DeleteView(index, True) --Deletes the indexed Slate Material Editor view. ask_user=bool


--opens the Parameter Editor rollout for the specified material.
ex. rt.SME.SetMtlInParamEditor(mat)

--edit material properties
ex. rt.rootScene[rt.name('SME')][rt.name('View1')][rt.name('door_handle____VRayMtl')].Properties.reference.anisotropy_channel = 3










"Cameras: //---------------------------------------------------------------"


-- create camera
cam = freecamera()

-- get camera
--current camera
activeCam = rt.getActiveCamera()

--get camera name
activeCamName = activeCam.name

-- get camera type
cam.type Name default: #free --#free- Free Camera (Target view can be set in any direction) --#target- Target Camera (Camera will always align view with target object)


--set FOV (field of view)
cam.fov = 0 --set the camera's fov to the new fov value
cam.fovType = 1 --int (default: 1) --sets the current Field Of View type. valid values: 1 -Horizontal, 2 -Vertical, 3 -Diagonal
--get FOV
cam.curFOV --float (default: 45.0)

-- orthographic camera
cam.orthoProjection --boolean (default: false) 

-- cone
cam.showCone --boolean (default: false) --Displays the cone (actually a pyramid) defined by a camera's field of view. The cone appears in the other viewports, but does not appear in a camera viewport.

-- horizon line
cam.showHorizon --boolean (default: false) --Displays the horizon line. A dark gray line appears at the level of the horizon in the camera's viewport.

-- atmospheric effects
cam.nearrange = 0.0 --float (default: 0.0) -- animatable; alias: Near_Env_Range. The near range for atmospheric effects.
cam.farrange = 1000.0 --Float (default: 1000.0) -- animatable; alias: Far_Env_Range. The far range for atmospheric effects.








"Lighting: //--------------------------------------------------------------"




--turn on all lights whose names start with "Key"
lights/Key*.enabled = on


--set attributes
--for all lights
rt.lights.value *= 0.5 --set the intensity of all lights

--for each light that has the property intensity
for eachLight in lights where isProperty eachLight #intensity do eachLight.intensity = 1000 --make that property value 1000







"SUBDIVISION: //-----------------------------------------------------------"


--smooth by face
--rt.polyop.meshSmoothByFace(obj, <facelist>)
faceSelection = rt.polyop.getFaceSelection(obj)
rt.polyop.meshSmoothByFace(obj, faceSelection)

--smooth faces by vertex
ex. rt.polyop.meshSmoothByVert(obj, <vertlist>) --Smooths the faces associated with the specified vertices.












"CLASSES: //---------------------------------------------------------------"

--determine class
ex. rt.classOf(obj) 
--superclass
ex. rt.superClassOf(obj)

--superclasses
rt.GeometryClass
rt.light
rt.camera
rt.helper
rt.SpacewarpObject


--Query class and parent class
obj = selection
print("ClassOf:"+(ClassOf obj) as string)
print("SuperClassOf:"+(SuperClassOf obj) as string)

--alternative method
for obj in selection do 
	case (superClassOf obj ) of 
		(GeometryClass)	: (format "object : % | superclass : %\n" (obj.name) "this is GeometryClass")
		(light) : (format "object : % | superclass : %\n" (obj.name) "this is light")
		(camera)	: (format "object : % | superclass : %\n" (obj.name) "this is camera")
		(helper)	: (format "object : % | superclass : %\n" (obj.name) "this is helper")
		(SpacewarpObject)	: (format "object : % | superclass : %\n" (obj.name) "this is SpacewarpObject")





struct
struct person (name, height, age, sex)

bill = person name: "Bill" height:72 age:34 sex:#male
joe = person name: "Joseph" sex:#male

bill.age  --returns 34
joe.age  --returns undefined
joe.age = bill.age-4 --assigns Bill's age less 4 to Joe's age.


ex. --expressions and procedures separated by commas
struct structName
	---,
	
	fn functionOne=
	---
	---
	),
	
	fn functionTwo=
		if something then
		---
		else
		---
	

Struct=structName()
Struct.functionTwo()











"HIERARCHIES: //-----------------------------------------------------------"



-- INode.Parent
$Tile.parent = $Wall						--link tile to wall object

-- INode.Children
$.children[1].name = "Tile_01"	--set name of first child object



--query
--for each selected helper which is not parented to anything print out its name
for obj in selection where isKindOf obj Helper AND obj.parent == undefined do print obj.name








"ANIMATION: //-------------------------------------------------------------"


animate on (at time 50f (move$ [0,0,5]))	--with AutoKey on, move object at frame 50

animate on (at time 100f ($.radius = 10))	--with AutoKey on, set radius at frame 100



-- import pymxs
at = pymxs.attime; t = rt.Teapot()

--animate it
with pymxs.animate(True):
	with at(1):
		t.pos = rt.Point3(2,2,2)
	with at(12):
		t.pos = rt.Point3(10, 10, 10)
	with at(21):
		t.pos = rt.Point3(20,20,20)








--Out-of-Range Functions
--Gets the Out-of-Range type (ORT) for the controller for the time before the first key.
getBeforeORT <controller>
-- Returns one of the following name values:

-- Gets the Out-of-Range (ORT) type for the controller for the time after the last key.
getAfterORT <controller>
--Returns one of the name values as for getBeforeORT() shown above.

-- Sets the Out-of-Range (ORT) type for the controller for the time before the first key.
-- The <ORT_type_name> must be one of the following name values:
-- #constant #cycle #loop #pingPong #linear #relativeRepeat
setBeforeORT <controller> <ORT_type_name>

-- Sets the Out-of-Range (ORT) type for the controller for the time after the last key. 
-- The <ORT_type_name> must be one of the symbolic values shown in setBeforeORT() above. 
-- No testing done on the validity of <ORT_type_name> is performed.
setAfterORT <controller> <ORT_type_name>

-- Enables or disables the Out-of-Range processing for the controller. 
-- If set to disabled with false , the controller effectively employs a constant ORT.
enableORTs <controller> <boolean>








"Render: //----------------------------------------------------------------"

max quick render 	--equivalent to pushing the 'render' button

--additional function to kick off renders independant of the current render dialog settings
render camera:$Camera01 frame:100 outputfile:"%currentuser%\\desktop\\.filename.exr"

--set render type
rendTimeType = 1	--( 1= single frame
-- 										2= active frame
-- 										3= user range
-- 										4= frame string )

--set render start frame
rendStart = 100

--set render end frame
rendEnd = 250

--set render size
renderWidth = 1920
renderHight	= 1080

--render to disk
rendSaveFile = true

rendOutputFilename = "%currentuser%\\desktop\\.filename.exr"


--[VRay Specific]

--set current renderer to VRay
renderers.current = VRay()

--set adaptive sampling min rate
renderers.current.adaptiveSubdivision_minRate = 1

--turn on VRays GI calculation
renderers.current.gi_on = true







"ENVIRONMENT: //-----------------------------------------------------------"

backgroundColor = color 0 0 0	--set environment background color

useEnvironmentMap = false	--turn environment map off

environmentMap = Checker()	--apply environment map. in this case checker



--Get/Set Vertex Color, Illumination and Alpha
ex. obj.SetVertexColor(<color>, #VertexColor|#Illumination|#Alpha) --Sets the Vertex Color, Illumination or Alpha value of the selected vertices to the specified color value.
ex. obj.vertexColorType(#color|#illum|#alpha|#color_plus_illum) --Get/set the vertex color display type.
ex. obj.showVertexColors(True) --default: false
--This affects all vertices used by the selected polygons.
--Corresponds to using the color picker in the Edit Vertex Colors rollout of the Editable Poly UI.
ex. obj.SetFaceColor(<color>, #VertexColor|#Illumination|#Alpha) --Sets the Vertex Color, Illumination or Alpha value of the selected polygons to the specified color value.

ex. obj.GetVertexColor(#VertexColor|#Illumination|#Alpha) --Gets the Vertex Color, Illumination or Alpha value of the selected vertices
ex. obj.GetFaceColor(#VertexColor|#Illumination|#Alpha) --Gets the Vertex Color, Illumination or Alpha value of the selected polygons


--wireframe color
ex. obj.wireColor(color) --default: random color
--modify wirecolor of direct children of a node
ex. obj.children.wirecolor = red



--[In-View Messages]
ex. rt.messageBox('message', title='window_title') --Displays a modal message box containing the message string and an OK button. The message box window title an be set with the title: keyword parameter. You can control whether a beep is made with the beep: keyword parameter, which defaults to true .
ex. rt.queryBox('message', title='window_title') --Displays a modal message box similar to the one that the messageBox() function creates, except it contains Yes and No buttons. The queryBox() function returns true if the user clicks Yes and false if the user clicks No.
--
ex. rt.yesNoCancelBox('message', title='window_title') --Displays a modal message box similar to the one that the messageBox() function creates, except it contains a Yes, a No, and a Cancel button. The yesNoCancelBox() function returns #yes , #no or #cancel depending on which button the user clicked to dismiss the message box.





--[Ui]

-- get main window instance
window = QtGui.QWidget(MaxPlus.GetQMaxWindow())
_GCProtector.widgets.append(window)



-- attach the QWidget to the 3dsmax mainwindow. (Attach a given parentless QWidget by its Qt winId to the win32 3ds max main window)
MaxPlus.AttachQWidgetToMax(w)




-- basic rollout floater framework
	global rofTool	--start a new local variable scope here and declare a global variable for 
									--the rollout floater
	Rollout roTool "Tool"	--start a new rollout definition
		spinner spSpinner "Value:"	--add a spinner and a button control to the rollout
		button btnButton "button text"

		on btnButton pressed do --event handler for the button
			format "value: %\n" spSpinner.value --output current spinner value

	try	--mechanism to prevent opening more than one floater window.
		closeRolloutFloater rofTool
	catch()

	rofTool = newRolloutFloater "Tool Floater" 300 100

	addRollout roTool rofTool	--add rollout to the floater




-- Undo
--syntax
--["undo_item_label" | label:<string_operand> | variable_name ] <bool_expr> <expr>

--syntax description
--"undo_item_label" must be a string literal,
--<string_operand> evaluates to a string at runtime,
--variable_name is a global or local variable containing a string value.


undo on (
    -- Do something.
)--end undo


createdialog test
undo "add background" on
...


my_context_name = "An Undo Context"
undo my_context_name on
...



-- Viewport:

--redraw
ex. rt.redrawViews() --Causes the 3ds Max viewports to be immediately redrawn in an optimal way, such that only those parts of the view that have changed are redrawn.

--enable/disable edged faces
viewportSetting = rt.NitrousGraphicsManager.GetViewportSetting(1)
state = viewportSetting.SelectedEdgedFacesEnabled
viewportSetting.SelectedEdgedFacesEnabled = not state --toggle


--show end result
--query/set
ex. rt.showEndResult = True
--enable/disable
ex. rt.enableShowEndRes(True)






"TIME: //------------------------------------------------------------------"

-- sleep
--interrupt sleep with ESC key; halts execution. SPACE bar to halt sleep & continue executing
--argument is a floating point number of seconds.
sleep 20 --pause a script in seconds



--delay commands:

-- dotNetObject:System.Windows.Forms.Timer
-- alternative to the MAXScript rollout Timer control.
-- The main advantage of the DotNet version is the ability to call MAXScript functions at given intervals without the need for a rollout.
function PerformDelayedTasks sender evt=
	sender.enabled = false 	--important: don't repeat this timer event
	dotnet.RemoveEventHandler sender "Elapsed" PerformDelayedTasks --for sanity and cleanup

	-- put all your delayed tasks below --
delayTimer= dotnetobject "Windows.Forms.Timer"
delayTimer.Interval=5000
dotnet.AddEventHandler delayTimer "Tick" PerformDelayedTasks
delayTimer.enabled = truee


-- another dotNet example
theTimer = dotNetObject "System.Windows.Forms.Timer" --create a Timer
fn printTime = 
	print localTime --define a MAXScript function to be called by the Timer.
) 
dotnet.addEventHandler theTimer "tick" printTime --add ON TICK event hander to call the function
theTimer.interval = 1000 --set the tick interval to 1 second (1000 milliseconds)
theTimer.start() --start the Timer
--theTimer.stop() --use this method to stop the Timer.












"RANDOMIZE: //-------------------------------------------------------------"

random

$.pos.x = random 0 10		--integer or float. randomize between first and second value.

$material.diffuseColor = color 0 0 (random 0 360) --randomize rgb 'b' value



--deselect random objects until only 50 are left selected
while selection.count > 50 do deselect selection[random 1 selection.count]











"PYTHON(in maxscript): //--------------------------------------------------"


--print list of available python methods to output window
showinterface python


Init(): --Loads Python if it is not loaded already.

-- [run python]
--run python code
ex. python.Execute "print 'hello'"

--run python file from maxscript
ex. python.ExecuteFile "tk_setup.py"
--full path
ex. python.ExecuteFile @"C:\Program Files\Autodesk\3ds Max 2015\scripts\Python\demoBentCylinder.py"



--python modules in maxscript:
--import a module
--assign value to a variable when importing
--module sub class
ex. init = (python.Import "module").Init
ex. module = python.Import "module"
	init = module.Init


--Documentation: https://knowledge.autodesk.com/search-result/caas/CloudHelp/cloudhelp/2017/ENU/Max-Python-API/developer/executing-python-from-maxscript-html.html
-- Python libraries can be imported and used in MAXScript, using Python.Import(). 
--In this example, we import the Python built-in methods and constants, 
--and use the pow() function:
builtIn = python.Import "__builtin__"
builtIn.pow 2 3
-- 8

ex. QtCore = python.Import "PySide2.QtCore"


--Reloads a Python module
--for example, a keyword gets re-defined 
Reload()
ex. python.reload theModule
-- <module '__builtin__' (built-in)>


--Errors
--Returns, as a string, the error message associated with the last error encountered 
--while running the Init(), Execute(), or ExecuteFile() methods.
GetLastError(): 






-- MaxPlus
-- set a variable for a maxscript command in maxplus
MaxPlus.Core.EvalMAXScript("variable = $")

--retrieve the value from a FP wrapped variable
pymxs.runtime.variable









--Core:
--variable
GetRootNode () 
for node in MaxPlus.Core.GetRootNode().Children:

IsGlobalVariableNameSettable (args)

IsVariableNameValid (args)

--script
EditMAXScriptFile (args)

EvalMAXScript (args) 

ExecuteMAXScript (args) 

Print (args) 

Write (args) 

WriteLine (args) 

--time
ResetCurrentTimeContext () 

GetCurrentTime () 

GetCurrentTimeContext () 

SetCurrentTime (args) 

SetCurrentTimeContext (args) 

UseCurrentTimeContext () 

--interface
GetCOREInterface (args) 

GetCOREInterfaceAt (args) 

GetFPInterface (args) 

GetFPInterfaceDesc (args) 

GetInterface (args) 

GetWindowHandle () 


-- FPValvue --Function Publishing (Interface)
--Assign FPValue
--execute a MAXScript expression using Core.EvalMAXScript() and obtain a return value via FPValue 
--using either:
commandString1 = "MaxPlus.Core.EvalMAXScript(\"print #aaa\")"
--RETURNS FPValue which is held in the commandString1 variable
--python.execute commandString1

--or:
fpValue = MaxPlus.FPValue()
evaluation_success = MaxPlus.Core.EvalMAXScript(<string>, fpValue)


--Get FPValue
--An FPValue wraps various types of values, for example, int, float, object, mesh, and so forth.

--obtain the value stored in the FPValue
<FPValue>.Get()
MaxPlus.FPValue.Get(<FPValue>)


--Get Type
<FPValue>.GetType()
--or
MaxPlus.FPValue.GetType(<FPValue>)

--Get Type string
--return a string corresponding to the supplied type value
MaxPlus.FPTypeGetName(<FPValue>.GetType())


--help
--print to listener output a list of FPValue type names and their corresponding constants:
import MaxPlus
help(MaxPlus.FPTypeConstants)
--
FPValue_types = {"AngAxis":48, "AngAxisTab":2096, "Angle":5, "AngleTab":2053, "BOOL":4, "BOOLTab":2052, "BezierShape":71, "BezierShapeTab":2119, "BitArray":51, "BitArrayTab":2099, "Bitmap":16, 
	"BitmapTab":2064, "Bool":66, "BoolTab":2114, "Box3":70, "Box3Tab":2118, "ClassDesc":52, "ClassDescTab":2100, "Color":62, "ColorChannel":11, "ColorChannelTab":2059, "ColorTab":2110, 
	"Control":55, "ControlTab":2103, "DWORD":65, "DWORDTab":2113, "Double":69, "DoubleTab":2117, "Enum":45, "EnumTab":2093, "FPInterface":59, "FPInterfaceTab":2107, "FPValue":63, "FPValueTab":2111, 
	"FRgb":23, "FRgbTab":2071, "FileName":9, "FileNameTab":2057, "Float":0, "FloatTab":2048, "HWND":60, "HWNDTab":2108, "Hsv":10, "HsvTab":2058, "IObject":58, "IObjectTab":2106, "Index":19, 
	"IndexTab":2067, "Int":1, "Int64":68, "Int64Tab":2116, "IntPtr":67, "IntPtrTab":2115, "IntTab":2049, "Interval":47, "IntervalTab":2095, "MSFloat":254, "Matrix3":20, "Matrix3Tab":2068, "Mesh":53, 
	"MeshTab":2101, "Mtl":14, "MtlTab":2062, "Name":61, "NameTab":2109, "Node":17, "NodeTab":2065, "Object":54, "ObjectTab":2102, "PBlock2":21, "PBlock2Tab":2069, "PercentFraction":6, 
	"PercentFractionTab":2054, "Point":56, "Point2":30, "Point2Tab":2078, "Point3":3, "Point3Tab":2051, "Point4":22, "Point4Tab":2070, "PointTab":2104, "Quat":49, "QuatTab":2097, 
	"RadioButtonIndex":13, "RadioButtonIndexTab":2061, "Ray":50, "RayTab":2098, "RefTarg":18, "RefTargTab":2066, "Rgb":2, "RgbTab":2050, "Str":57, "StrTab":2105, "String":8, "StringTab":2056, 
	"Texmap":15, "TexmapTab":2063, "TimeValue":12, "TimeValueTab":2060, "Value":64, "ValueTab":2112, "Void":46, "VoidTab":2094, "World":7, "WorldTab":2055}



--Get the INDEX inside the Parent Anim Object
getParameterSubAnimNum
(ParamCollectorOps.getParameterParentAnim 1)[ParamCollectorOps.getParameterSubAnimNum 1].value
--RETURNS the value of the Length sub-animation track.
(ParamCollectorOps.getParameterParentAnim 1)[ParamCollectorOps.getParameterSubAnimNum 1].value = 10
--will set the value of the Box's length to 10 units and so on...

--"1" is the index of the parameter. You can get the index of a parameter by using 
ParamCollectorOps.getParameterIndex 1 1 1
--where the first argument is the collection index, the second is the rollout index in the collection, 
--the third is the parameter index inside the rollout. In the above case, the result would be 1 
--(first parameter in first rollout of the first collection)...






-- pymxs
--wrapper for the MAXScript engine, exposes virtually all the Interfaces, globals, and classes available in MAXScript
--see demoPyMXSTypeInterop.py example file in cloud 3ds scripts pymxs directory.

--print in pymxs
pymxs.print_()










"DIRECTORIES: //--------------------------------------------------------"

-- Returns the filename path of the source file the function has been called from.
<filename>getSourceFileName() 


-- [run maxscript]
--fileIn will do the same as "run script" or evaluate all in the editor. 
--It can make a function available if it's globally declared
FileIn
fullPath = "O:\\Cloud\\__Graphics\\3ds Max\\Scripts\\macros\\tk_macroScript.ms"
FileIn fullPath


Include
-- Include actually takes the code from that file and injects it at that point. 
-- So if you have a large script and you want to organize things a bit better you can write 
-- certain functions in a separate file and include that function when the script get executed,
-- so that function would always accessible because it is included in that scope.




-- Set 3rd Party Plug-Ins paths
baseDir = pathConfig.removePathLeaf (getDir #temp)
iniFile = baseDir + "\\Plugin.UserSettings.ini"
setIniSetting iniFile "Directories" "Your Plugin Name" "Your Plugin Directory"



-- full path. (may be neccesarry to initialize python python.Init() )
fullPath = "%CLOUD%/__Graphics/3ds Max/Scripts/___Python_path/tk_setup.py"
python.ExecuteFile @fullPath





-- Check if path or file exists
ex. doesFileExist file
ex. getfileattribute file #directory
--or using dotNet
ex. ((dotnetclass "System.IO.Directory").exists "D:\	emp")
ex. ((dotnetclass "System.IO.File").exists "D:\	emp\\Wow.ms")




--access 3ds Max system directories:
--get directory
GetDir <filetype_name> --Returns as a string the directory specified in the Customize > Configure Paths dialog for the specified file type.
--set directory
SetDir <filetype_name> <string> --Returns true if successful, false if not. 



-- Project Folder: ---------------------------------------------------------------------
pathConfig.doProjectSetupSteps()
-- Performs all steps necessary to set up a new Project, including browsing for project folder and creating all sub-folders. Returns true on success, false if cancelled.

pathConfig.doProjectSetupStepsUsingDirectory <ProjectPath> 	 
-- Performs all steps necessary to set up a new Project using the supplied Project Path as the Root. Returns true on success, false if cancelled.

pathConfig.getCurrentProjectFolder() 
-- Returns the current Project Folder.

pathConfig.getCurrentProjectFolderPath() 
-- Returns the current Project Folder definition file (*.MXP).

pathConfig.getProjectFolderPath <ProjectPath> 
-- Returns the Project Definition filename (<ProjectPath>\<ProjectName>.mxp) for the specified Project Folder.

pathConfig.getProjectSubDirectory <subdir_index> 
-- Returns the indexed Project sub-directory.
ex. for i = 1 to pathConfig.getProjectSubDirectoryCount() do
		format "%: %\n" i (pathConfig.getProjectSubDirectoryi) --Print all Project Sub-Directories:

pathConfig.getProjectSubDirectoryCount() 
-- Returns the number of Project sub-directories. See above example.

pathConfig.addProjectDirectoryCreateFilter <#directory_type> 
-- Adds Project Directory Filter where <directory_type> is one of the following:
-- #font | #Scene | #export | #import | #help | #expression | #preview | #image | #Sound | #plugcfg | #maxstart | #vpost | #drivers | #autoback | #matlib | #scripts | #startupScripts | #defaults | #renderPresets | #ui | #maxroot | #renderoutput | #animations | #archives | #Photometric | #renderassets | #userScripts | #userMacros | #userStartupScripts | #temp | #userIcons | #maxData | #downloads | #proxies 

pathConfig.removeAllProjectDirectoryCreateFilters() 
-- Removes all filters added using pathConfig.addProjectDirectoryCreateFilter()

pathConfig.setCurrentProjectFolder <ProjectPath> 
-- Sets the current project folder to the given path. The Project Folder is displayed in the title bar of 3ds Max and will be updated instantly.




-- Path Manipulation, Conversion and Resolving: -----------------------------------------
pathConfig.appendPath <path1> <path2> -- Appends the second argument filename to the first argument path, adding backslash if necessary.
ex. pathConfig.appendPath "c:\\temp" "test.txt"
	"c:\temp\test.txt"
	pathConfig.appendPath "c:\\temp\\" "test"
	"c:\temp\test"

pathConfig.convertPathToAbsolute <relative_path> -- Converts the relative path argument to absolute project path using the Project Directory.
ex.	pathConfig.convertPathToAbsolute "meshes"
	"C:\Documents and Settings\username\My Documents\3dsmax\meshes"

pathConfig.convertPathToLowerCase <path> -- Converts the path argument to lower case and unifies the backslashes.
ex.	pathConfig.convertPathToLowerCase "C:\\Temp\Test/pATH"
	"c:\temp\test\path"

pathConfig.convertPathToRelativeTo <path1> <path2> -- Converts the first path argument to a relative path with respect to the second path argument.
ex.	pathConfig.convertPathToRelativeTo "C:\\Temp\\Test" "c:\\Program Files\\"
	"..\Temp\Test"

pathConfig.convertPathToUnc <path> -- Returns the UNC path from a mapped drive path.
ex. pathConfig.convertPathToUnc "t:\\project" --If drive letter T: is mapped to a server called MyServer, then
	"\\MyServer\projects"

mapPaths.getFullFilePath <filename> -- Resolves the filename using map paths, returns fully qualified filename if the file is found.

pathConfig.normalizePath <path> -- Returns a normalized path name.
ex. pathConfig.normalizePath "scenes/test.txt"
	".\scenes\test.txt"

pathConfig.pathsResolveEquivalent <path1> <path2> -- Returns true if the two paths resolve to the same location (in other words the two paths are equivalent), false if they are not equivalent.
ex. pathConfig.pathsResolveEquivalent "scenes\\test.txt" "./scenes/test.txt"
	true

pathConfig.resolvePathSymbols <path> -- Resolves the path symbols.

pathConfig.resolveUNC SystemGlobal:resolveUNC false -- This is the property toggle found in Preferences>Files which controls whether max automatically converts absolute paths to their UNC equivalents. (i.e. M:\file.txt to server1\\file.txt if M: is mapped to server1\\)

pathConfig.removePathLeaf <path> -- Removes a leaf from the given path.
ex.	pathConfig.removePathLeaf "c:\\temp\\test"
	"c:\temp"

pathConfig.removePathTopParent <path> -- Removes the top parent from the given path.
ex. pathConfig.removePathTopParent "c:\\temp\\test"
	"temp\test"

pathConfig.stripPathToLeaf <path_or_filename> -- Returns the last sub-directory name from the given path. If the path is a full file name, returns the file name. Equivalent to filename from path.
ex.	pathConfig.stripPathToLeaf "C:\\temp\\test"
	"test"
	pathConfig.stripPathToLeaf "C:\\temp\\test\\"
	""
	pathConfig.stripPathToLeaf "C:\\temp\\test\\somefile.tga"
	"somefile.tga"
	--COMPARE:
	filenamefrompath "C:\\temp\\test"
	"test"
	filenamefrompath "C:\\temp\\test\\"
	""
	filenamefrompath "C:\\temp\\test\\somefile.tga"
	"somefile.tga"
   
pathConfig.stripPathToTopParent -- Returns the root of the given path.
ex.	pathConfig.stripPathToTopParent "C:\\temp\\test\\test.tga"
	"C:\\"
	pathConfig.stripPathToTopParent "\\\\SomeServer\\Projects\\Test"
	"\\SomeServer"
	pathConfig.isAbsolutePath <path_string> --Is... Query Methods --Returns true if the argument is an absolute path, false if it is a relative path. The path does not have to exist for this method to operate on it.

pathConfig.isLegalPath <path_string> -- Returns true if the argument is a legal path definition, false if it is an illegal path. The path does not have to exist for this method to operate on it, it is only being parsed for correctness.
ex. pathConfig.isLegalPath "c:\\" --legal path, existing
	true
	pathConfig.isLegalPath "z:\\path" --legal path, not existing
	true
	pathConfig.isLegalPath "zz:\\path" --illegal double drive letter!
	false

pathConfig.isPathRootedAtBackslash <path> -- Returns true if the argument starts with a backslash, false if it does not.
ex. pathConfig.isPathRootedAtBackslash "\\machine\\c$" --starts with backslash:
	true
	pathConfig.isPathRootedAtBackslash "c:\\temp" --does not start with backslash:
	false

pathConfig.isPathRootedAtDriveLetter <path> -- Returns false if the argument starts with a backslash, true if it starts with a drive letter. The inverse of pathConfig.isPathRootedAtBackslash()

pathConfig.isProjectFolder<path> -- Returns true if the argument path is a valid Project Folder root, false otherwise.

pathConfig.isRootPath <path> -- Returns true if the argument path is a Root path, false otherwise
ex.	pathConfig.isRootPath "C:\\"
	true
	pathConfig.isRootPath "C:\\temp"
	false

pathConfig.isUncPath <path> -- Returns true if the argument path is a UNC path, false otherwise
ex. pathConfig.isUncPath "T:\\Projects" --mapped drive, not UNC
	false
	pathConfig.isUncPath "\\\\MyServer\\Projects" --UNC path
	true

pathConfig.isUncSharePath <path> -- Returns true if the argument path is a UNC share path, false otherwise.

pathConfig.isUsingProfileDirectories() -- Returns true if the system is using Profile directories, false otherwise.

pathConfig.isUsingRoamingProfiles() -- Returns true if the system is using Roaming Profiles, false otherwise. When using roaming profiles on somebody else's machine, your profile is being accessed over the network from your own machine. This mode is not officially supported.





-- Other Path-Related Methods and Structs: ----------------------------------------------
pathConfig.GetDir <#directory_type> -- Points at the GetDir() method documented here. -- Returns the system directory where directory_type is one of the following: -- #font | #Scene | #export | #import | #help | #expression | #preview | #image | #Sound | #plugcfg | #maxstart | #vpost | #drivers | #autoback | #matlib | #scripts | #startupScripts | #defaults | #renderPresets | #ui | #maxroot | #renderoutput | #animations | #archives | #Photometric | #renderassets | #userScripts | #userMacros | #userStartupScripts | #temp | #userIcons | #maxData | #downloads | #proxies | #pageFile 

pathConfig.SetDir -- Points at the SetDir() method documented here.

pathConfig.mapPaths #Struct:mapPaths -- Points at the mapPaths struct definition.
ex. --the two method calls are equivalent:
	mapPaths.getFullFilePath "fir.tga"
	pathConfig.mapPaths.getFullFilePath "fir.tga"

pathConfig.pluginPaths #Struct:pluginPaths -- Points at the pluginPaths struct.
ex. count = pathConfig.pluginPaths.count()
	for j = 1 to count do
		format " % : %\n" j (pathConfig.pluginPaths.get j)

pathConfig.sessionPaths #Struct:sessionPaths -- Points at the sessionPaths struct.

pathConfig.xrefPaths #Struct:xrefPaths -- Points at theXRefPath struct
ex. --the two method calls are equivalent:
	xrefPaths.getFullFilePath "delme.max"
	pathConfig.xrefPaths.getFullFilePath "delme.max"
	Configurate User Paths Dialog - Path Settings Loading, Saving and Merging
	pathConfig.SaveTo <filename> 
	Saves the path configuration to the given filename.Returns true on success, false otherwise.Corresponds to the Save To... button in the Customize>Configure User Paths dialog.

pathConfig.load <filename> -- Loads the path configuration from the specified path configuration file. Returns true on success, false otherwise.Corresponds to the Load button in the Customize>Configure User Paths dialog.

pathConfig.merge <filename> -- Merges the settings from the given path configuration file. Returns true on success, false otherwise. Loads the path configuration from the specified path configuration file. Returns true on success, false otherwise. Corresponds to the Merge button in the Customize>Configure User Paths dialog.




--built-in environment paths
#animations	--"C:\Users\<UserName>\Documents\3dsMax\sceneassets\animations"
#archives	--"C:\Users\<UserName>\Documents\3dsMax\archives"
#autoback	--"C:\Users\<UserName>\Documents\3dsMax\autoback"
#autodeskCloud --"C:\Users\<UserName>\AppData\Local\Autodesk\Autodesk Sync\Cloud\<LoginName>" Returns empty string "" if the user is not logged in Autodesk 360.
#defaults	--"C:\Program Files\Autodesk\3ds Max <ReleaseNumber>\en-US\defaults\MAX"
#downloads	--"C:\Users\<UserName>\Documents\3dsMax\downloads"
#drivers	--"C:\Program Files\Autodesk\3ds Max <ReleaseNumber>\drivers"
#export		--"C:\Users\<UserName>\Documents\3dsMax\export"
#font		--"C:\Program Files\Autodesk\3ds Max <ReleaseNumber>\fonts"
#help		--"C:\Program Files\Autodesk\3ds Max <ReleaseNumber>\help"
#image		--"C:\Users\<UserName>\Documents\3dsMax\sceneassets\images"
#import		--"C:\Users\<UserName>\Documents\3dsMax\import"
#matlib		--"C:\Users\<UserName>\Documents\3dsMax\materiallibraries"
#maxData	--"C:\Users\<UserName>\AppData\Local\Autodesk\3dsMax\<ReleaseNumber> - 64bit\ENU\"
#maxroot	--"C:\Program Files\Autodesk\3ds Max <ReleaseNumber>\"
#maxstart	--"C:\Users\<UserName>\Documents\3dsMax\scenes"
#pageFile	--"C:\Users\<UserName>\AppData\Local\Autodesk\3dsMax\<ReleaseNumber> - 64bit\ENU\temp"
#photometric --"C:\Users\<UserName>\Documents\3dsMax\sceneassets\photometric"
#plugcfg	--"C:\Users\<UserName>\AppData\Local\Autodesk\3dsMax\<ReleaseNumber> - 64bit\ENU\en-US\plugcfg"
#preview	--"C:\Users\<UserName>\Documents\3dsMax\previews"
#proxies	--"C:\Users\<UserName>\Documents\3dsMax\proxies"
#renderassets	--	"C:\Users\<UserName>\Documents\3dsMax\sceneassets\renderassets"
#renderPresets	--	"C:\Users\<UserName>\Documents\3dsMax\renderpresets"
#renderoutput	--	"C:\Users\<UserName>\Documents\3dsMax\renderoutput"
#scene	--	"C:\Users\<UserName>\Documents\3dsMax\scenes"
#scripts	--	"C:\Program Files\Autodesk\3ds Max <ReleaseNumber>\scripts"
#sound	--	"C:\Users\<UserName>\Documents\3dsMax\sceneassets\sounds"
#startupScripts	--	"C:\Program Files\Autodesk\3ds Max <ReleaseNumber>\scripts\startup"
#temp	--"C:\Users\<UserName>\AppData\Local\Autodesk\3dsMax\<ReleaseNumber> - 64bit\ENU\temp"
#ui	--"C:\Program Files\Autodesk\3ds Max <ReleaseNumber>\en-US\UI\"
#userMacros	--"C:\Users\<UserName>\AppData\Local\Autodesk\3dsMax\<ReleaseNumber> - 64bit\ENU\usermacros"
#userScripts	--"C:\Users\<UserName>\AppData\Local\Autodesk\3dsMax\<ReleaseNumber> - 64bit\ENU\scripts"
#userStartupScripts	--"C:\Users\<UserName>\AppData\Local\Autodesk\3dsMax\<ReleaseNumber> - 64bit\ENU\scripts\startup"
#userIcons	--"C:\Users\<UserName>\AppData\Local\Autodesk\3dsMax\<ReleaseNumber> - 64bit\ENU\usericons"
#vpost	--



-- get WINDOWS env variable
fn getEnvVar var = (
	var = var as string
	dotNet.loadAssembly "System"   
	local env = dotNetClass "system.Environment"
	env.GetEnvironmentVariable var
)








"USER_INPUT: //------------------------------------------------------------"

-- [hotkeys]



-- Using dotNet:

-- [.net System.Windows.Forms.Control]
-- Documentation
-- https://msdn.microsoft.com/en-us/library/system.windows.forms.control%28v=vs.110%29.aspx?f=255&MSPPError=-2147217396


-- Operators:
== != 

sender


--query properties or events
ctrl = dotNetClass "System.Windows.Forms.Control"
showProperties ctrl
showEvents ctrl
showMethods ctrl
dotNet.showConstructors ctrl

dotNet.addEventHandler
-- takes 3 arguments:
-- a dotnetobject with a public event,
-- a string that is the name of the event,
-- and an maxscript function

ctrl = dotNetClass "System.Windows.Forms.Control"
dotnet.addeventhandler ctrl "KeyDown" keyDownFunction




#--getKeyState---------------------------------------------------------------------------

#The state will either be 0 or 1 when not pressed, and increase to something like 60000 when 
#pressed, so to get a True/False result, checking for > 1
#key = virtual-key code #https://msdn.microsoft.com/en-us/library/windows/desktop/dd375731(v=vs.85).aspx
#microsoft docs: https://msdn.microsoft.com/en-us/library/windows/desktop/ff468859(v=vs.85).aspx
def getKeyState(key):
	if (key == "shift"): #VK_LSHIFT #left
		key = 0xA0
	if (key == "ctrl"): #VK_CONTR
		key = 0x11
	if (key == "alt"): #VK_MENU
		key = 0x12
	if (key == "del"): #VK_DELETE
		key = 0x2E
	if (key == "esc"): #VK_ESCAPE
		key = 0x1B
	if (key == "enter"): #VK_RETURN
		key = 0x0D
	value = windll.user32.GetKeyState(key)
	if (value > 1):
		return True #key down
	else:
		return False #key up



control = dotNetClass "system.windows.forms.control"
showProperties control
showProperties control.keyDown
showProperties control.keyUp

on control.keyDown.x do
	snapmode.setOSnapItemActive 4 1 (true);
	snapmode.setOSnapItemActive 4 2 (true);
	)
on control.keyUp.x do
	(
	snapmode.setOSnapItemActive 4 1 (false);
	snapmode.setOSnapItemActive 4 2 (false);
	)

-- if statement for above
if control.keyUp == control.keyUp.x do
		(
		---
		)

-- actions
KeyDown		--Occurs when a key is pressed while the control has focus.
KeyPress	--Occurs when a character. space or backspace key is pressed while the control has focus.
KeyUp			--Occurs when a key is released while the control has focus.
KeyEventArgs --Provides query data for the KeyDown or KeyUp event.
KeyPressEventArgs	--Provides query data for the KeyPress event.
ModifierKeys --Gets a value indicating which of the modifier keys (SHIFT, CTRL, and ALT) is in a pressed state.


MouseButtons --Gets a value indicating which of the mouse buttons is in a pressed state.
MousePosition	--Gets the position of the mouse cursor in screen coordinates.
MouseDown	--Occurs when the mouse pointer is over the control and a mouse button is pressed.
MouseEnter --Occurs when the mouse pointer enters the control.
MouseHover --Occurs when the mouse pointer rests on the control.
MouseLeave --Occurs when the mouse pointer leaves the control.
MouseMove --Occurs when the mouse pointer is moved over the control.
MouseUp		--Occurs when the mouse pointer is over the control and a mouse button is released.

-- microsoft keyboard key names:
-- https://msdn.microsoft.com/en-us/library/system.windows.forms.keys(v=vs.110).aspx


-- create a DotNet TextBox
ex.
hTextBox = dotNetObject "System.Windows.Forms.TextBox"
hTextBox.size = dotNetObject "System.Drawing.Size" 160 25
hTextBox.location = dotNetObject "System.Drawing.Point" 20 20
-- create a DotNet Form
hForm = dotNetObject "System.Windows.Forms.Form"
hForm.size = dotNetObject "System.Drawing.Size" 200 100
hForm.controls.add hTextBox
hForm.topmost = true
-- create a DotNet Application to run the form
hApp = dotNetClass "System.Windows.Forms.Application"
hApp.run hForm







"SCRIPT_EDITOR: //---------------------------------------------------------"

--MAXScript Editor Properties File - Quick Navigation:
--https://help.autodesk.com/view/3DSMAX/2018/ENU/?guid=__files_GUID_8588CAB1_7F4E_4A5E_9CD8_7F11F4DF9755_htm

--[defining keyboard shortcuts]

-- Tools > Open Global Options File menu item
-- Scroll down and locate the section remarked as

--  # User defined key commands
--	syntax: <shortcut>|<command>|\
--add a '\' at the end of each line except the last.
--The modifier keys are Ctrl, Shift, and Alt

-- The named keys are Left, Right, Up, Down, Insert, End, Home, Enter, Space, Tab, 
-- KeypadPlus, KeypadMinus, KeypadMultiply, KeypadDivide, Escape, Delete, PageUp, 
-- PageDown, Slash, Question, Equal, Win.

--Documentation: https://knowledge.autodesk.com/search-result/caas/CloudHelp/cloudhelp/2015/ENU/MAXScript-Help/files/GUID-BC77ED4A-66B5-4958-876D-DBBBBD486A52-htm.html
--Changes active after restart





-- [External Editor]

-- Sublime text: send to 3ds Max
-- file: Key Bindings - User file 

-- default MAXScript Listener keys:
{ "keys": ["ctrl+e"], "command": "send_file_to_max" },
{ "keys": ["shift+enter"], "command": "send_selection_to_max"},
{ "keys": ["ctrl+shift+e"], "command": "select_max_instance" },
{ "keys": ["f1"], "command" : "open_max_help"}


--MAXScript Editor - Defining Custom Keywords
-- https://knowledge.autodesk.com/search-result/caas/CloudHelp/cloudhelp/2015/ENU/MAXScript-Help/files/GUID-85AD190F-1A65-4BF2-8AE8-9688960B1ACC-htm.html

"Abbreviations files"
-- Abbreviations in Maxscript is one of the powerful tools in scripting, yet not all artists know about. 
-- Frankly it was found to make our scripting life much easier, have you ever thought of a short cut to 
-- your codes instead of writing them over and over again or at best case you would copy and paste from 
-- your collected library of codes.
-- Well the good news is that abbreviations in Maxscript was found for this exact reason, so instead of 
-- defining a Functions the old way why don't we just type fn and then hit Ctrl+Shift+A and it will throw 
-- us a full code:

FN _NAME =
 "Your code"
)

-- We can do it for loops or rollout templates etc.....
-- And to know how this magic works we are going to follow those simple steps:
 
-- 1- create a new script and in Tools > Open abbreviations file, this will open an empty script for you 
-- (in case you didn't edit it before) were you can define your abbreviations.
 
-- 2- An abbreviation is defined in the form:
-- <AbbrevName>=<Expanded Form>
-- for example let's define a for loop

fordo=for i in 1 to 10 do ()
save it. Now open a new script and type fordo and hit Ctrl+Shift+A or go to Edit > Expand abbreviations. 

-- Voila! a for loop appeared.
 
-- 3- There are some rules you should follow here, AbbrevName is case sensitive and it detects spaces. So if 
-- you define it like:
-- For do =, when you want to call it the F should be capital and there is a space inbetween and after do.
 
-- 4- If you want to arrange the expanded forms to have tabs and on different lines then we have to use (\n) 
-- to move the following into another line and (\t) to add a tab, our loop example would change to be:
-- fordo=for i in 1 to 10 do \n(\n\t "your code" \n)
-- As simple as this. So when we call fordo it's gonna give us:

for i in 1 to 10 do 
(
  "your code" 
)

-- And here a couple of abbreviations you can add to your library:
fordo=for i in 1 to 10 do \n(\n\t "your code" \n)
rol=rollout _name "name" \n(\n \n)\n createdialog _name     
fn=fn NAME arg_a arg_b =\n(\n\tfnBody\n)
if=if ARG then\n(\n\tState\n)\nelse\n(\n\tState2\n)
sh=shellLaunch @"your file" ""
mfn=maxfilename
mfp=maxfilepath


-- [Abbreviations file]
/* COMMENTS */
header=/*HeaderStart***********\n:created By:\t\t\tName:\n:Company:\t\t\t\t***********HeaderEnd*/
fnHeader=/*FnStart***********\n:Function: |\n:Usage: \n:Returns: \n:Todo: \n:Notes: \n***********FnEnd*/
fn=/*FnStart***********\n:Function |\n:Usage: \n:Returns: \n:Todo: \n:Notes: \n***********FnEnd*/
comment=/*CommentStart***********\n|\n***********CommentEnd*/

/* CODE STRUCTURES */
struct=struct |\n(\n\tfn,\n\t\n\tfn\n)\nNAME = NAME()
attributes=def = attributes NAME_D\n--redefine:def\n(\n\tlocal VAR = undefined\n\t\n\tparameters\n\n\trollout\n)
parameters=parameters NAME_Prm\n(\n\tPARAM type:#VAL\n)
for x=for x in ARRAY where ARG do\n(\n\tEXPR\n)
for i=for i = 1 to INTEGER where ARG do\n(\n\tEXPR\n)
if=if EXPR then\n(\n\tEXPR\n)\nelse\n(\n\tEXPR\n)
case=case EXPR of =\n(\n\tFACTOR: EXPR\n\tdefault: EXPR\n)

/* UI CONTROLS */
spinner=spinner NAME_Spin *CAPTION* range:[0,100,0] type:#float fieldWidth:spnW1 align:#right
slider=slider NAME_Sld *CAPTION* range:[0,100,0] type:#float ticks:2 align:#center
button=button NAME_Bt *CAPTION* width:w1 align:#center
checkbutton=checkbutton NAME_Cbt *CAPTION* align:#center
edittext=edittext NAME_Et *CAPTION* fieldWidth:w1 labelOnTop:true align:#left
checkbox=checkbox NAME_Cbx *CAPTION* align:#left
label=label NAME_Lbl *CAPTION* align:#center
group=group *CAPTION*\n(\n\tCONTROLS\n)

/* MAX WRAPPERS */
nodeTransformMonitor=nodeTransformMonitor node:| forwardTransformChangeMsgs:false

/* GENERAL */



-- MAXScript Editor - Defining And Using Abbreviations:
-- https://knowledge.autodesk.com/search-result/caas/CloudHelp/cloudhelp/2015/ENU/MAXScript-Help/files/GUID-7358FB2E-182A-4BB8-8208-3E74D28FC205-htm.html



-- query






"COMMAND LINE/BATCH: //----------------------------------------------------"


-- run python file FROM WINDOWS COMMAND LINE or batch file
3dsmax -U PythonHost "tk_setup.py" 
-- run maxscript
"%ADSK_3DSMAX_x64_2018%\3dsmax.exe" -U MAXScript doit.ms




-- Enter the following from a command prompt: “c:\program files\autodesk\3dsmaxXXX\3dsmaxcmd” -x and press Enter.

-- All control characters map to the Windows Regional settings standards.
-- Date format control chars:
  d       --Day of month as digits with no leading zero for single-digit days.
  dd      --Day of month as digits with leading zero for single-digit days.
  ddd     --Day of week as a three-letter abbreviation. The function uses the
          --LOCALE_SABBREVDAYNAME value associated with the specified locale.
  dddd    --Day of week as its full name. The function uses the LOCALE_SDAYNAME

  M       --Month as digits with no leading zero for single-digit months.
  MM      --Month as digits with leading zero for single-digit months.
  MMM     --Month as a three-letter abbreviation. The function uses the
          --LOCALE_SABBREVMONTHNAME value associated with the specified locale.
  MMMM    --Month as its full name. The function uses the LOCALE_SMONTHNAME
          --value associated with the specified locale.
  y       --Year as last two digits, but with no leading zero for years less than 10.
  yy      --Year as last two digits, but with leading zero for years less than 10.
  yyyy    --Year represented by full four digits.

--Time format control chars:
  h       --Hours with no leading zero for single-digit hours; 12-hour clock.
  hh      --Hours with leading zero for single-digit hours; 12-hour clock.
  H       --Hours with no leading zero for single-digit hours; 24-hour clock.
  HH      --Hours with leading zero for single-digit hours; 24-hour clock.
  m       --Minutes with no leading zero for single-digit minutes.
  mm      --Minutes with leading zero for single-digit minutes.
  s       --Seconds with no leading zero for single-digit seconds.
  ss      --Seconds with leading zero for single-digit seconds.
  t       --One character time-marker string, such as A or P.
  tt      --Multicharacter time-marker string, such as AM or PM.


          -- BACKBURNER JOB SUBMISSION-

--you want to submit a job to backburner, you can optionally give a manager
--me, otherwise it will perform a default search for the manager.  You can
--tionally specify the manager's port number and, for searches, a netmask.
--suming the manager's network name is mgr_machine:

3dsmaxcmd scene.max -submit
3dsmaxcmd scene.max -submit -netmask:255.255.0.0
3dsmaxcmd scene.max -submit:mgr_machine
3dsmaxcmd scene.max -submit:mgr_machine -port:1234

 --you want to change the job name and submit it to the network queue
 --initially suspended:

3dsmaxcmd scene.max -submit -jobName:"My Job" -suspended

 --default, a 32-bit 3dsmaxcmd.exe will submit jobs to 32-bit servers, and
--64-bit 3dsmaxcmd.exe will submit jobs to 64-bit servers. You can optionally
--bmit a job to a platform other than the default. To submit a job to 64-bit
--rvers from a 32-bit 3dsmaxcmd.exe:

3dsmaxcmd scene.max -submit -platform:64

--submit a strip render job to the network. Job uses 4 strips, and an overlap

3dsmaxcmd scene.max -submit -split:4,10

--under a single strip locally. Render strip number 2 of 4, using an overlap
--10 pixels between each strip:

3dsmaxcmd scene.max -strip:4,10,2

--stitch together a set of strips rendered locally. Stitch a frame rendered
--ing 4 strips and an overlap of 10 pixels between each strip:

3dsmaxcmd scene.max -stitch:4,10

--default, timeout values for waiting for max to load, render, and unload
--e the same as those found in the Advanced settings of the Network Job
--signment dialog in max. To specify timeout values (minutes) when submitting job:

3dsmaxcmd scene.max -submit -waitLoad:20 -waitRender:300 -waitUnload:10

--you want to generate a job description xml file so you can edit it:
--ny command line options specified will be included in the job file)

3dsmaxcmd scene.max -writeJobFile

--ad a pre-existing job description file and render it:

3dsmaxcmd scene.max -readJobFile:scene.xml


--3dsmaxcmd [options] scene_file

--BASIC OPTIONS-

 -?                                  -- This help
 -x                                  -- Show examples
 -v:<0-5>                            -- Verbose level, 0-5
 @<filename>                         -- Command line options in a file
    OR  -cmdFile:<filename>

 -preset:<filename>                  -- Render preset file
    OR  -rps:<filename>
 -sceneState:<scene-state-name>      -- Load a scene state before rendering
 -batchRender                        -- Render all enabled batch renders
 -batchRender:<batch-render-name>    -- Render batch render named
                                       --batch-render-name
 -preRenderScript:<filename>         -- Pre-render script file
    OR  -script:<filename>
 -postRenderScript:<filename>        -- Post-render script file
 -workPath:<pathname>                -- Work path
                                       --Root location for job data folders
 -pathFile:<filename>                -- A path configuration file (.mxp)
 -workingFolder:<filename>           -- A path to a directory to be used as th

                                      -- Working Folder for the application
                                       --session
 -split:<strips,overlap>             -- Split render;
 -strip:<strips,overlap,strip>       -- Single strip, rendered locally;
                                       --strip count, overlap, and strip number
 -stitch:<strips,overlap>            -- Stitch strips rendered locally;
                                       --strip count and overlap
 -dateFormat:<dateformat>            -- Specify a date format to be used
                                       --defaults to locale-dependent format
 -timeFormat:<timeFormat>            -- Specify a time format to be used
                                       --in message timestamp
                                      -- defaults to locale-dependent format
                                      -- and 24-hour clock


 --RENDER PARAMETERS-

 -outputName:<filename>              -- Render output filename
    OR  -o:<filename>
 -camera:<string>                    -- Render camera
    OR  -cam:<string>
 -width:<integer>                    -- Output width
    OR  -w:<integer>
 -height:<integer>                   -- Output height
    OR  -h:<integer>
 -pixelAspect:<number>               -- Pixel aspect ratio
 -start:<integer>                    -- Sequence start frame
 -end:<integer>                      -- Sequence end frame
 -nthFrame:<integer>                 -- Every nth frame value
 -frames:<string>                    -- Frames list (1,3,5-12), or "all"
 -stillFrame                         -- Indicates that this is a still frame
    OR  -sf                            --render; no frame suffix will be added
                                       --to output filename
 -imageSequenceFile:<0/1/2>          -- Image sequence file creation,
                                       --0=none, 1=.imsq, 2=.ifl
 -gammaCorrection:<1/0>              -- Toggle gamma correction
 -gammaValueIn:<number>              -- Input gamma value
 -gammaValueOut:<number>             -- Output gamma value
 -continueOnError                    -- If an error is encountered, an attempt
                                       --to continue is made
 -videopostJob:<1/0>                 -- Apply Videopost to the scene

 --RENDER FLAGS-

 -showRFW:<0/1>                      -- Show/hide Render Frame Window
    OR  -rfw:<0/1>                    --during render
 -skipRenderedFrames:<1/0>           -- Toggle skip existing images
 -videoColorCheck:<1/0>              -- Toggle video Color Check
 -force2Sided:<1/0>                  -- Toggle force 2 sided
 -renderHidden:<1/0>                 -- Toggle render hidden
 -atmospherics:<1/0>                 -- Toggle atmospherics
 -superBlack:<1/0>                   -- Toggle super black
 -renderFields:<1/0>                 -- Toggle render to fields
 -fieldOrder:<even/odd>              -- Field order
 -displacements:<1/0>                -- Toggle displacement mapping
 -effects:<1/0>                      -- Toggle render effects
 -useAreaLights:<1/0>                -- Toggle area lights/shadows
 -useAdvLight:<1/0>                  -- Toggle use advanced lighting
 -computeAdvLight:<1/0>              -- Toggle compute advanced lighting
 -ditherPaletted:<1/0>               -- Toggle output dithering (paletted)
 -ditherTrueColor:<1/0>              -- Toggle output dithering (true color)
 -renderElements:<1/0>               -- Toggle render elements


 --BACKBURNER JOB SUBMISSION-

 -submit[:manager_name]              -- Submit to Backburner
    OR  -s[:manager_name]
 -port:<integer>                     -- Manager port number
 -netmask:<string>                   -- Network mask other than 255.255.255.0
 -jobName:<string>                   -- Job name
 -priority:<integer>                 -- Job priority
 -suspended                          -- Toggle initially suspended
 -writeJobFile                       -- Write all job settings to xml file
 -readJobFile:<filename>             -- Read all job settings from xml file
 -waitLoad:<integer>                 -- Timeout (minutes) for max to load
 -waitUnload:<integer>               -- Timeout (minutes) for max to unload
 -waitRender:<integer>               -- Timeout (minutes) for max to render
 -platform:<32/64>                   -- Override the job to 32-bit or 64-bit


 --BITMAP PARAMETERS-

 -BMP_TYPE:<2/8>                     -- .BMP type, 2=paletted, 8=true 24

 -JPEG_QUALITY:<1-100>               -- .JPG quality value
 -JPEG_SMOOTHING:<1-100>             -- .JPG smoothing value

 -TARGA_COLORDEPTH:<16/24/32>        -- .TGA color bitdepth
 -TARGA_COMPRESSED:<1/0>             -- .TGA compression on/off
 -TARGA_ALPHASPLIT:<1/0>             -- .TGA alpha split on/off
 -TARGA_PREMULTALPHA:<1/0>           -- .TGA premultiplied alpha on/off

 -TIF_TYPE:<0/1/2/3/4>               -- .TIF type,
                                       -- mono/8-bit color/logl/logluv/
                                        --16-bit color
 -TIF_ALPHA:<1/0>                    -- .TIF alpha on/off
 -TIF_COMPRESSION:<1/0>              -- .TIF compression on/off
 -TIF_DPI:<number>                   -- .TIF dots-per-inch value

-- For each of the following there is a corresponding -RPF_xxx option
 -RLA_COLORDEPTH:<8/16/32>           -- .RLA color bitdepth
 -RLA_ALPHA:<1/0>                    -- .RLA alpha on/off
 -RLA_PREMULTALPHA:<1/0>             -- .RLA premultiplied alpha on/off
 -RLA_DESCRIPTION:<string>           -- .RLA description (in quotes)
 -RLA_AUTHOR:<string>                -- .RLA author name (in quotes)
 -RLA_ZDEPTHCHANNEL:<1/0>            -- .RLA z-depth channel on/off
 -RLA_MTLIDCHANNEL:<1/0>             -- .RLA material ID channel on/off
 -RLA_OBJECTIDCHANNEL:<1/0>          -- .RLA object ID channel on/off
 -RLA_UVCHANNEL:<1/0>                -- .RLA UV coordinates channel on/off
 -RLA_NORMALCHANNEL:<1/0>            -- .RLA surface normals channel on/off
 -RLA_NONCLAMPEDCOLORCHANNEL:<1/0>   -- .RLA non-clamped color channel on/off
 -RLA_COVERAGECHANNEL:<1/0>          -- .RLA coverage channel on/off

 --For each of the RLA options above, there is a corresponding -RPF_xxx option,
 --plus the following which are specific to RPF and unavailable for RLA
 -RPF_NODERENDERIDCHANNEL            -- .RPF node render ID channel on/off
 -RPF_COLORCHANNEL                   -- .RPF color channel on/off
 -RPF_TRANSPCHANNEL                  -- .RPF transparency channel on/off
 -RPF_VELOCCHANNEL                   -- .RPF velocity channel on/off
 -RPF_WEIGHTCHANNEL                  -- .RPF sub-pixel weight channel on/off
 -RPF_MASKCHANNEL                    -- .RPF sub-pixel mask channel on/off

 -EXR_BITDEPTH                       -- .EXR main output layer bit depth
                                       --     0 = float
                                         --   1 = half float
                                           -- 2 = 8bits/channel integer
 -EXR_COMPRESSIONTYPE                -- .EXR compression type
                                       --     0 = no compression
                                         --   1 = run length encoding
                                           -- 2 = zlib compression, one scan li at a time
                                            --3 = zlib compression, in blocks o 6 scan lines
                                            --4 = piz-based wavelet compression
                                            --5 = lossy 24-bit float compressio

                                            --6 = lossy 4-by-4 pixel block compresion, fixed compression rate
                                            --7 = lossy 4-by-4 pixel block compresion, flat fields are compressed more
 -EXR_STORAGETYPE                    -- .EXR storage type
                                       --     0 = Store Image as Scanlines
                                         --   1 = Store Image as Tiles

 -EXR_IMAGETYPE                      -- .EXR main output layer image type
                                       --     0 = rgba
                                         --   1 = rgb
                                           -- 2 = mono

--OBSOLETE PARAMETERS-

--The following flags are deprecated, but supported for backward compatibility

-- These flags are replaced by -pathFile:<filename> - see BASIC OPTIONS
 -bitmapPath:<pathname>              -- Extra bitmap path for rendering
                                      -- multiple path commands are allowed
 -xrefPath:<pathname>                -- Extra xref path for rendering
                                       --multiple path commands are allowed

--These flags are replaced by:
 -RLA/RPF_ZCHANNEL:<1/0>             -- RLA/RPF_ZDEPTHCHANNEL:<1/0>+
 -RLA/RPF_NODEIDCHANNEL:<1/0>        -- RLA/RPF_OBJECTIDCHANNEL:<1/0>+
 -RLA/RPF_REALPIXCHANNEL:<1/0>       -- RLA/RPF_NONCLAMPEDCOLORCHANNEL:<1/0>+

--  The following flags are deprecated and no longer supported
 -EXR_USEEXPONENT                    -- .EXR Use exponent on/off
 -EXR_EXPONENT                       -- .EXR Exponent value (decimal)
 -EXR_PREMULTALPHA                   -- .EXR Pre-multiply alpha on/off
 -EXR_ALPHA                          -- .EXR Save alpha component on/off
 -EXR_RED                            -- .EXR Save red component on/off
 -EXR_GREEN                          -- .EXR Save green component on/off
 -EXR_BLUE                           -- .EXR Save blue component on/off
 -EXR_USEFRAMENUMDIGITS              -- .EXR Use number of frame digits on/off
 -EXR_FRAMENUMDIGITS                 -- .EXR Number of frame digits (integer)
 -EXR_USEREALPIX                     -- .EXR Use RealPix RGB data on/off

--  Options are not case-sensitive
--  MAXScript names for rendering parameters and flags are accepted as alias,
--  where applicable.






"DOCUMENTATION: //---------------------------------------------------------"

--finding the macro for a command:
'customize user interface'> keyboard> Main UI/'All Commands'







"ERRORS: //----------------------------------------------------------------"

--[Error Handling]





--[Debugging: non-descript syntax errors and typos]



















