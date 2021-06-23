'PYTHON_notes_______________________________________________________________________________'






#escape sequences
#\        ignore or continuation
#\n       new line
#\t       tab

#multiple commands on a single line:
eg. expression;expression;expression; #does not work with anything requiring an indented block



#print to console
sys.stdout.write('\n')







'Mathmatical Operators______________________________________________________________________'

#division '/'
#to get floating point result in python 2
eg. c = a / float(b) #If the numerator or denominator is a float, then the result will be also
eg. from __future__ import division #Python 3 division behavior.

#floor division. #drops and remainder and rounds down. '//'
//

#Exponentiation. **
eg. 2**3 #equivalent to: 2*2*2 = 8 
#or 
ex. pow(2, 3)


#Modulus %
eg. 26 % 7 is 5 #If 26 / 7, then the division remainder is 5. (since 7+7+7=21 and 26-21=5.) 


#increment/ decrement '+=' '-='
eg. i += 1 #AND assignment operator, eg. x += 5 is equivanent to x = x + 5
eg. i -= 1 #AND assignment operator, eg. x -= 5 is equivanent to x = x - 5


#additonal assignment operators:
*=		#x *= 5	x = x * 5
/=		#x /= 5	x = x / 5
%=		#x %= 5	x = x % 5
//=		#x //= 5	x = x // 5
**=		#x **= 5	x = x ** 5
&=		#x &= 5	x = x & 5
|=		#x |= 5	x = x | 5
^=		#x ^= 5	x = x ^ 5
>>=		#x >>= 5	x = x >> 5
<<=		#x <<= 5	x = x << 5



#numberic:          overriding +-*/% operators
__add__             +  Addition    eg. print (int.__add__(arg1,arg2))#when used with an 
							# '__add__' method. the methods body described in what way they are added.
__sub__             -  Subtraction eg. print (str.__sub__(arg1,arg2))
__mul__             *  Multiplication
__truediv__         /  Division
__floordiv__        // Floor Division. Drops remainder & rounds down.
__mod__             %  Modulus. Remainder
__pow__             ** Power of. Exponent



#reverse the sign of a number. (turn a neg number positive and vice versa):
# by multiplying by -1
eg. -10 * -1
#10
eg. 10 * -1
#-10


#get highest value
eg. max(1,2,3) #returns 3
#lowest  
eg. min(1,2,3) #returns 1

#absolute value. (distance from 0)
eg. abs(-3, 3) #both have a distance of 3
#always return positve value:
eg. abs(number)


#round float value 
eg. round(1.1111) #returns 1.0
eg. round(1.1111, 2) #returns 1.11



#difference (distance) between two numbers:
eg. abs(1-2) #returns 1
#appropriately-signed distance between any two numbers. using math (import math)
def distance(a, b):
	if (a == b):
		return 0
	elif (a < 0) and (b < 0) or (a > 0) and (b > 0):
		if (a < b):
			return (abs(abs(a) - abs(b)))
		else:
			return -(abs(abs(a) - abs(b)))
	else:
		return math.copysign((abs(a) + abs(b)),b)
#alt:
def distance(a, b):
	return (max(a, b) - min(a, b)) * (-1 if a > b else 1)


#differnce (distance) between elements in an array
#using numpy (import numpy as np)
np.diff([1,5,6,8])	#returns: array([4, 1, 2])


#distance between two points
dist = math.hypot(x2 - x1, y2 - y1)
#alt
dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
#
p1 = [4, 0]
p2 = [6, 6]
distance = math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)



#get decimal place:
decimals = str(float_)[::-1].find('.') #get decimal places

#move decimal place
a = 0.01
a * 10. #shifts decimal place right
a / 10. #shifts decimal place left







'Comparators________________________________________________________________________________'
<=      #less than or equal

>=      #greater than or equal

==      #equal to

!=      #not equal

is      #object identity (ie. listA==listB, but not is ListB)

is not  #negated object identity


__lt__              <  Less than
__le__              <= Less than or equal to
__eq__              == Equal to
__ne__              != Not Equal to
__gt__              >  Greater than
__ge__              >= Greater than or equal to




eg. isinstance(var, (str, unicode))
eg. type(var)
eg. type(x) in [str, float]













'Boolean Operations_________________________________________________________________________'
#the Boolean data type is a data type, having two values (usually denoted true and false)
and    x and y     if x is False, then x, else y
or     x or y	     if x is False, then y, else x
not    not x	     if x is False, then True, else False

#order of operation
not #evaluated first
and #evaluated next
or #evaluated last
() #evaluated first regardless


__and__             &  
__xor__             ^
__or__              |


# Toggle
#alternative toggle method
#query value and toggle on/off
state = (query a boolean value)
not state

# For Two values
# boolean
eg. state^=True

#if you are using two arbitrary values, use an inline if:
toggle = 'a' if toggle == 'b' else 'b'

# this supposedly works but not sure how
		toggle = x[toggle] #try [::-1] to reverse the list

# 0 and 1 using bitwise exclusive-or:
eg. x = 1
		x ^= 1 #returns 0

# two integers using xor-by-precomputed-constant:
eg. A = 205
		B = -117
		t = A ^ B # precomputed toggle constant
		x ^= t # toggle

# if the values are hashable you can use a dictionary;
eg. A = 'xyz'
		B = 'pdq'
		d = {A:B, B:A}
		x = A
		x = d[x] # toggle





# For Multiple Values (in this case 4)
eg. x = [1,2,3,0]
		toggle = x[toggle]

eg. toggle = 0
			toggle = 1 if toggle == 0 else 0

eg. x = [1,0]
		toggle = 0
		for i in xrange(0,100):
			toggle = x[toggle]

# using itertools
eg. toggle = itertools.cycle(['red', 'green', 'blue']).next #in Python 3 the next() method was changed to __next__()
		toggle()

# create an itertools function. possibly could be used with multiple values
eg. myfunc = itertools.cycle([0,1]).next
		myfunc()    # -> returns 0
		myfunc()    # -> returns 1

# using a generator
eg. def alternate():
		while True:
			yield 0
			yield 1

alternator = alternate()
print alternator.next()



# toggle function
#any sequence of ints 0-9 for multiple sequences at a time
global g_seqDict
g_seqDict={}
def cycle(id_sequence): #toggle between numbers in a given sequence
	#[args: string id_numberical sequence ie. 'name_123']
	try:
		value = g_seqDict[id_sequence] #ie. value = [1,2,3]
	except KeyError: #else create sequence list for the given key
		id_ = id_sequence.split('_')[0] #ie. name
		sequence = id_sequence.split('_')[1] #ie. 123
		g_seqDict[id_sequence] = [i for i in list(sequence)] #ie. {name_123:[1,2,3]}
	value = g_seqDict[id_sequence][0] #get the next value ie. 1
	g_seqDict[id_sequence] = g_seqDict[id_sequence][1:]+[value] #move the value to the end of the list ie. {name_123:[2,3,1]}
	return value









'Conditionals_______________________________________________________________________________'

if():
elif():

try:      #see error handling
finally:

#try with multiple statements:
for code in (
	lambda: a / b,
	lambda: a / (b + 1),
	lambda: a / (b + 2),
	):
	try: print(code())
	except Exception as ev: continue
	break
else:
	print('it failed: %s' % ev)

#using and/or
	mod = obj.modifiers['TurboSmooth'] or obj.modifiers['TurboSmooth_Pro'] or obj.modifiers['OpenSubDiv']
	mod.iterations = 0 #set subdivision levels to 0.
except: pass



#conditional statement 
eg. x = 'a < b' if (a < b) else 'a >= b'


eg. force=True; force if sceneName else not force


# if/else conditionals in list comprehension:
eg. [(i if True else None) for i in []]



#when comparing types use is instead of ==
# any / all
eg. all((cond1, cond2, cond3))
#
eg. all(i in 'QPushButton <b>Rich Text</b>' for i in ('<','>'))
#generator expression
eg. all(i is '1' for i in ('1','0'))
eg. any((filename is f for f in ('.ma','.ma.swatches','.mb','.mb.swatches')))

#any using list comprehension
eg. [x for x in ['0','2','1'] if x=='1']



# switch/ case:
# The following example is pretty much the exact use-case of a dictionary,
# but is included for its simplicity. Note that you can include statements
# in each suite.
v = 'ten'
for case in switch(v):
	if case('one'):
		print 1
	if case('two'):
		print 2
	if case('ten'):
		print 10
	if case('eleven'):
		print 11
	if case(): # default, could also just omit condition or 'if True'
		print 'default'


# matching multiple cases in a single shot. (import string)
c = 'A'
for case in switch(c):
	if case(*string.lowercase): # note the * for unpacking as arguments
		print 'lowercase'
	if case(*string.uppercase):
		print 'uppercase'
		break
	if case('!', '?', '.'): # normal argument passing style also applies
		print 'terminator'
		break
	if case(): # default
		print 'default'


#switch/case using a dict
def dispatch_dict(operator, x, y):
	return {
		'add': lambda: x + y,
		'sub': lambda: x - y,
		'mul': lambda: x * y,
		'div': lambda: x / y,
	}.get(operator, lambda: None)() #default value of None

#dispatch_dict('mul', 2, 8) Returns: 16
#dispatch_dict('unknown', 2, 8) Returns: None











'Looping___________________________________________________________________________________'


#Control flow: 
return    #returns the result

return elem1, elem2, elem3 #return a tuple of given elements
					#returns ex. [3.0, 'string', [list]]

return notimplemented #used with if statement to return without an error.

continue  #continue the loop #returns to 'for'
yield     #creates a generator
break     #used to break out of a loop statement even if the condition has not been met
pass      #does nothing but can be used if required syntactically.


#Loops:
while   eg. while x <= y:   
for     eg. for i in list_: #i is an index variable used without explicit reference          




#iterating through a list, string, or tuple:
#each item
eg. [print i for i in list_]
#items that satisfy an if condition.
eg. [print i for i in list_ if i <8]
#break if condition met
eg. even = [n for n in numbers[:None if 412 not in numbers else numbers.index(412)] if not n % 2]
#using a function to raise StopIteration and list to catch it:
eg. even = list(next(iter(())) if n == 412 else n for n in numbers if 0 == n % 2)
#using itertools
eg. even = (n for n in numbers if not n % 2)
		list(itertools.takewhile(lambda x: x != 412, even))
#break up until condition
eg. [i for i in iter(lambda x=iter(['init','main','viewport']): next(x), 'viewport')] #returns ['init','main']



#iterating through two or more lists simultaneously
eg. for i, item in enumerate(list1):
			print item, list2[i]
#using zip
for item1, item2 in zip(list1, list2):
#for very large lists :
#from itertools import izip
for item1, item2 in izip(list1, list2):
	print item1, item2



#iterating through a list of lists using comprehension
eg. [[i+1 for i in list2] for list2 in list1]
#alt using map:
eg. [map(lambda i:i+1 ,list2) for list2 in list1]



#using enumerate() with list comprehension:
eg. [index for index, element in enumerate(list_)]



#perform an operation x number of times.
#xrange is more efficient than range for large values
#'num' is redefined each sequence. if you need to modify it during loop. 
eg. [num for num in xrange(10)] #returns [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#between two values: (start, stop)
eg. range(140, 151) #140-150 ie. [140, 141, 142,..]
#(start, stop, step)
eg. range(3, 8, 2) #creates list with a 2 unit interval. in this case [3, 5, 7]
#random integer values.  



#using itertools: #faster than range
# itertools.repeat(object[, times])
# import itertools
for i in itertools.repeat(None, 10): #or itertools.repeat(10)
	pass

#increment by a specific starting point or step:
#using 'while':
i=0 #define a starting point. 
while i < len(xyz):
	x.append(xyz[i]) #perform operation
	y.append(xyz[i+1])
	z.append(xyz[i+2])
	i+=3 #increment











'Variables__________________________________________________________________________________'

# Naming Convention
#class (capitalized)
ClassVariable

#name mangling:
#protected variable. by convention do not modify outside of subclass
_variable
#private variable. prefixed with at least 2 underscores & at most 1 suffix
__variable
#call a private variable from outside its class.
._Test__variable




# Assignment
#assign multiple variables the same value
eg. var1=var2=var3 = None #if 'x=y=z=[]' were used, operations on all three variables would be assigned to the same list.
eg. a, b, *c = [1,2,3,4,5] #returns: 1 2 [3, 4, 5]
#if separate lists are desired, use: 
eg. x=[];y=[];z=[]
eg. a,b,c = (1,2,3)
#starred assignments:
eg. a, *b, c = [1, 2, 3, 4, 5] #result: a=1, b=[2, 3, 4], c=5
#deep unpacking:
eg. color, (r, g, b) = ('red', (250, 23, 10)) #result: color='red', r=250, g=23, b=10



#dynamically assign variables:
#using a dictionary:
eg. vars_={}
	vars_['var1']=value #vars_['var1'] returns: <value>

#adding to globals() or locals():
eg. locals()[key]=value
eg. globals()['var'] = "an object"
#assign variables from **kwargs
eg. kwargs_ = (exec('%s=%s' % (k,v)) for k,v in kwargs.items()) #create variables for any kwargs passed in
#
eg. kwargs_ = ('{}={}'.format(k,v) for k,v in kwargs.items())
#
# unpack an iterables contents to arguments in a function call
#using * to get list or set as *args
eg. *list_ #eq to: list_[0], list_[1], ...
eg. *range(10, 13) #eq to: 10, 11, 12
#using ** to get dictionary keys/values as **kwargs
eg. **dict_ #eq to: key1=value1, key2=value2


#swap variables
eg. a, b = b, a



#check if variable exists. an alternative would be to use try: except:
eg. 'a' in vars() or 'a' in globals()


#get object from string
eg. button = getattr(self.ui, 'self.ui.obj')
#assign default value if no object found:
getattr(class_, 'method', None)




#check object type
#type:
str, unicode, int, float, complex
list, dict, tuple, set, frozenset
bytes, bytearray
object
bool
eg. type(obj) #Returns: <type 'str'>
#
eg. isinstance(obj, (str,unicode)) #Returns: bool
eg. isinstance(obj, type(None)) #check for nonetype
#using types (import types)
# types.LambdaType
# types.MethodType
# types.GeneratorType
type(obj) == types.FunctionType
#using numbers (import numbers)
isinstance(10, numbers.Integral) #Returns: True
isinstance(10.5, numbers.Integral) #Returns: False
#if type==callable
eg. callable(obj)




# convert to another data type using the convert function:
#str() int() float() tuple() set()
eg. float('6.66')



#convert string '0' to int 0: (useful when string is unknown but may be 0)
eg. int('0' or 0) #returns 0  #int('0') returns None.
#check if string is an int
eg. '23.4'.isdigit() #Returns: False




#prompt user to input a value.
eg. variable = input('enter a filename')







#execute a string statement.
eg. exec ('print "x"')

#evaluate an expression. 
eg. eval ('2+2') #returns 4






#global to current module
#global variables cannot be directly assigned a value within a function 
#(unless named in a global statement) although they may be referenced.
eg. global x
eg. global x, y, z 
#define global within a function
eg. def function(arg1, arg2):
			global uiPath1
			global uiPath2
			uiPath1 = arg1
			uiPath2 = arg2
			#or
			global uiPath1, uiPath2
			uiPath1,uiPath2 = (arg1,arg2)
			#now uiPath_pt1 and uiPath_pt2 can be used anywhere in the module

#global to all modules
# create config.py with global variables defined and import config.py to all other modules needing those variables 



#delete a variable
eg. del x










'Iterables__________________________________________________________________________________'


#container:         for emulating lists like classes
__len__             len() Length of.
__getitem__         Index
__setitem__         Assign to Index
__delitem__         Delete item at Index
__iter__            Iteration eg. in for Loops #create an iterator method
__contains__        In









'Strings____________________________________________________________________________________'

''
""        #single line.
""" """   #multi-line.


__str__


#raw string. raw strings don't escape anything.
r'string'
#unicode
u'string'
#convert unicode:
u'string'.encode('utf-8')
#
'string'.decode('utf-8')


#string properties
'string'.punctuation
'string'.digits


#get length of a string.           
eg. len('string') #'6'

#set length with optional fill char.
rjust("str", 20) #returns: '                 str'
ljust("str", 20) #left-justifies a string to a given width. returns: 'str                 '
center("str", 20) #returns: '        str         '
zfill("0.1", 10) #pads a numeric string with leading zeros. returns: '00000000.1'



#repeat string
eg. '.'*10


# String formatting:
#using format()
#'{1} {0}' would reverse the order.
eg. '{0} {1}\n{2}'.format(hello, world, 'new string') #\n char allows sets a new line for 'new string' after printing 'hello world'
eg. '{x} {y}'.format(x='Hello', y='World') #returns: 'Hello World'
#escaping '{' and '}'
eg. '{0} {{excaped curly braces}}'.format('')

#
eg. '%s %s' % (hello, world)
#join strings with other data types
eg. '%i%f%s' %(x,y,z) #adding .x between % & f (ex %.xf) will give you x dec places (%f=%d)

#using +
eg. 'str'+'ing'

#using join()
eg. '_'.join([hello, world]) #join inserting an underscore
eg. ''.join(string1, string2)   eg. print ':'.join('string') #s:t:r:i:n:g
eg. ','.join(['string1', 'string2', 'string3']) #'string1,string2,string3'

#convert from mulit-line to single line. (in this case separated by tab space)
eg. singleLine = '\t'.join([line.strip() for line in my_string])
#alt method
eg. my_string.replace('\r', '\t')
eg. ''.join(my_string.splitlines())




#access characters in a string. 
eg.	'string'[0] #'s'
#slicing. take a subsection.
eg. 'string'[1:-1] #'trin'


#check for single set of chars:
eg. 'char' in 'chars' #returns: bool
eg. 'char' not in 'chars' #returns: bool
#using re
eg. pattern = re.compile(r'\d\$,')
	pattern.findall(string) #returns: bool
#find case-insensitive
eg. 'chars'.lower() in 'chars'.lower()
#using re (import re)
eg. re.search('chars', string, flags=re.IGNORECASE)
#check for multiple sets of chars:
eg. any(char in set('0123456789$,') for char in 'chars') #returns: bool
eg. any(((True if s in 'chars.' else False for s in ('Char', 'char')))) #returns: bool
eg. all(((True if s in 'chars.' else False for s in ('Char', 'char')))) #returns: bool
eg. next((True for s in ('Char', 'char') if s in 'chars.'), False) #returns: bool


#find index 
eg. string.index('chars') #'3'
#find match anywhere in a string.
re.search(r'chars', string)
#using re (import re)
re.search('chars', string).start() #return starting index.
re.search(r"\bchars\b", string).start() #return starting index. \b = whole words only.
re.search('chars', string).end() #return ending index.
#find all instances.
re.findall(r'chars', string)
#find first instance
eg. string.find('chars') #returns index ie. '5'
#find first instance of char(s) from right
eg. string.rfind('chars') #returns index of first instance from right.


#matches beginning of a string.
re.match(r'chars')


#startswith/ endswith (boolean)
#can also supply a tuple of strings to test for or convert list to tuple
eg. string.startswith('chars') #returns bool
eg  string.endswith('chars') #returns bool


#check for numeric characters:
#\d matches a numerical digit, 
#\d+ means match one-or-more digits.
#$ means match the end of the string.
eg. #import re
m = re.search(r'\d+$', string) # if the string ends in digits m will be a Match object, or None otherwise.
if m is not None:
		print m.group()
#get trailing integers
#using re (import re)
m = re.findall(r"\d+\s*$", W)
trailing_digits = m[0] if m else None #returns trailing digits as a string.


#number of occurrences. 
eg. print string.count(' ') #count the #of whitespace '0' 



#tokenize string to elements of a list
eg. list('chars')        #returns: ['c', 'h', 'a', 'r', 's']
#without using a list:
eg. [c for c in 'chars'] #returns: ['c', 'h', 'a', 'r', 's']

#split string.
eg. string.split()#splits on whitespace by default
eg. 'c, h, a,r,s'.split(',') #returns: ['c','h','a','r','s']




#strip from left or right (removes whitespace if no argument is given)
#strip leading characters
eg. 'ABxABBAxBA'.lstrip('AB') #returns 'BA' (Strips ALL 'A' or 'B' from left until encountering another char)
#strip trailing characters
eg. 'ABxABBAxBA'.rstrip('BA') #returns 'AB' (Strips ALL 'A' or 'B' from right until encountering another char)


#removes from both ends. passing no argument results in removing whitespaces
eg. 'ABxABBAxBA'.strip('AB') #returns 'xABBAx' (Strips ALL 'A' or 'B' from both ends until encountering another char)
eg. 'ABxABBAxBA'.strip('A') #returns 'BxABBAxB' #.strip('A') will not work as you must list ALL chars as they appear in the string.

#strip from entire sequence
eg. 'ABBA'.replace('B', '') #returns: 'AA'
eg. 'ABBA'.translate({ord('B'): None}) #returns: 'AA'
#mutiple chars:
eg. 'ABBA'.translate({ord(i): None for i in 'AB'}) #returns: ''
#python 3
eg. text = text.translate(str.maketrans('','','1234567890')) #string.digits can be substituted for '1234567890'.
#substring:  (replace elements of a string.  may work with a tuple of multiple strings or list converted to tuple)
# replace (this, withThis, howMany) 
eg. 'ABBA'.replace('AB', '') #returns 'BA' (Strips ALL 'AB')
#first occurance from beginning
eg. 'string'.replace('in', '', 0) #returns 'strg'
#first occurance from end
eg. 'string'.replace('in', '', -1) #returns 'strg'
#first x occurances of substring:
eg. 'ABBA'.replace('B', '', 2) #returns 'AA'
#first x occurances from right
eg. ''.join('pCylinderShape1.f[0]'.rsplit('Shape', 1)) #replaces the first occurance of 'Shape' from the right with ''. #'pCylinder1.f[0]' from 'pCylinderShape1.f[0]'

#strip numberic characters.  also lstrip/ rstrip.
eg. 'b000'.strip('0123456789') #returns 'b'
#strip alphanumberic characters:
eg. 'b000'.strip('abcdefghijklmnopqrstuvwxyz') #returns '000'

#strip all chars from both ends of first instance of specific chars.
#can use different find and index slice options to tweak results.
eg. string = string[string.lfind('[')+1:string.rfind(']')] #'body_mainShape.vtx[176]' becomes 176
#inverse:
eg. string[:string.rfind('Shape')] + string[string.rfind('Shape')+5:] #'tire_treadShape.e[1410]' becomes 'tire_tread.e[1410]' (also: string.replace('Shape.', '.', -1))
#using index:
eg. string = string[string.index('['):string.index(']')] #'body_mainShape.vtx[176]' becomes 176
#replace case-insensitive:
#using re (import re)
eg. pattern = re.compile('char', re.IGNORECASE)
	pattern.sub('replace', 'char Char CHAR') # 'replace replace replace'


#strip using .join
#indexs can be changed to take a subsection. ie. [2:4] would return '176'
eg. string = ''.join(string.partition('[')[1:]) #'body_mainShape.vtx[176]' becomes [176]


#using re to remove specific chars
eg. re.sub('[^A-Za-z0-9]+', '', 's_t_r_i_n_g') #returns: 'string'
eg. re.sub('^-', '', '-23') # '^' indicates to remove the first '-' only
# strip all characters using re
# many more complex options in the re docs: https://docs.python.org/2/library/re.html
# \W    non-alphanumeric characters
# \w    alphanumeric characters
# \b    beginning or end of a word. r'\bfoo\b' matches 'foo', 'foo.', '(foo)', 'bar foo baz' but not 'foobar' or 'foo3'. the end of a word is indicated by whitespace or a non-alphanumeric, non-underscore character
# \B    not at the beginning or end of a word. r'py\B' matches 'python', 'py3', 'py2', but not 'py', 'py.', or 'py!'. the end of a word is indicated by whitespace or a non-alphanumeric, non-underscore character
# \d    matches any decimal digit; this is equivalent to the set [0-9]
# \D    matches any non-digit character; this is equivalent to the set [^0-9]
# \A    matches only at the start of the string.
# \Z    matches only at the end of the string.
from re import sub
sub(r'[\W_]+', '', string)
#
import re
pattern = re.compile(r'[\W_]+')
pattern.sub('', string)


#replace all instances.
eg. re.sub(pattern,replace,string,max=0)


#remove or replace specific chars from a string
eg. string.translate(None, '!@#$')
eg. string.replace('!@#$','') #optional third argument: integer max num of items to replace
#or with loop
eg. [string.replace(char,'') for char in '!@#$']


#remove trailing characters in a string
	# \d: a digit (0-9)
	# +: one or more of the previous item (ie. \d)
	# $: the end of the input string
eg. n = re.search(r'\d+$', 'string08')
	num = int(n.group()) if n else None




#reverse a string
eg. ''.join(reversed('string'))
eg. 'string'[::-1] #[begin:end:step] - by leaving begin and end off and specifying a step of -1, it reverses a string.


#convert case
#capitalize first char
eg. string[:1].upper()+string[1:]
#capitalize first alphanumberic char. sets other characters in string as lower
eg. string.capitalize() #'1Str ing' from '1str ing' 
#capitalize first alphanumberic char after white space. sets other characters in string as lower
eg. string.title() #'1Str Ing' from '1str ing'
#all UPPER
eg. 'string'.upper() #'STRING'
eg. 'string'.isupper() #returns: bool
#all lower
eg. 'STRING'.lower() #'string'
eg. 'string'.islower() #returns: bool
#swap case
eg. 'String'.swapcase() #'sTRING'
#specific chars
eg. string[:4].upper()+string[2:] #convert specific indices.





#convert string to type integer
int('8') #returns: int


#insert a comma value every 3 digits
#int:
format(num, ',d') #4567987 to 4,567,987
#python 3 using f-strings:
f'{num:,d}'
#float:
'{:,.2f}'.format(num) #4567987.00  to 4,567,987.00










'Lists__(arrays)____________________________________________________________________________'



# create an empty list.
list_=[]          
#also: 
list_=list()

# create a list with contents.
list_ = ['red', 'blue', 'green', 3.5, 3]


# populate a list within a given range:
eg. list(range(9)) #returns [0, 1, 2, 3, 4, 5, 6, 7, 8]
#create a list within a set range: range(start, stop, step) 
eg. list(range(3,8,2)) #creates list with a 2 unit interval. in this case [3, 5, 7]
#between two values:
eg. list(range(140, 151)) #140-150 ie. [140, 141, 142,..]
#between two values with increment amount:
eg. numpy.arange(140, 150, 0.5) #increment by .5 ie. [140, 140.5, 141,..]
#creates a list with random integer values.  
eg. random.randomrange(0, 100)

#initialize with multiples of the same element.
eg. ['init'] * 4 #results in ['init', 'init', 'init', 'init']

list_ = [i*2 for i in range(10)]  #generates a list of even numbers 0 through 18




# work on a copy or subsection of a list:
list_[:] = list_ #or ex. [-2:] for last two elements
#modifying list_[:] won't effect the original.




#length of list (or dictionary)
eg. len(list_)
#length of first second and last index combined
eg. len([0,1,-1])  



#check if object is a list:
isinstance(obj, list):


#check Membership:
eg. 3 in [1, 2, 3] #results in True

#check if index exists:
eg. index < len(List_)
#using try/except
eg. try:
		list_[1]
	except IndexError, e:
		print e #'Index doesn't exist'


#get element from index
eg. e = list_[i] if len(list_) > i else None


#check if list contains type of element:
#contains list:
eg. any(isinstance(i, list) for i in list_)



#'[:]' takes a full slice of a list. useful when modifying a list while still iterating over it.            
eg. [list_.insert(0, i) for i in list_[:] if len(item) > 6]



#get the first and last item
eg. list_[::len(list_)-1]
eg. [list_[0], list_[-1]]


#get subsection:
list_[1:5] #subsection 1-4
#also
list_[:3] #up to 2
list_[3:] #from 3

#get subsection with a step amount
eg. list(2:6:3) #from index 2-5, with a step of 3. so returns indices 2,5


#with negative integers, the search is counted from the end of the list.
eg. list_(-1:1)
eg. list_(::-1)
# get last element of a list. ex. list_[-1]
eg. list_[-1]
# if possibly empty (returns empty list instead of IndexError)
eg. list_[-1:]
# returns None is stead of an empty list
eg. list_[-1] if list_ else None


#get the first occurrence         
eg. list.index('x') #returns index of element

#get the Total number of occurrences
(x, mylist.count(x)) for x in set(mylist)

#get the most occuring element
#using statistics (import statistics)
eg. statistics.mode(list_)


#get every nth element from a list
#list_ [starting index, step amount]
list_ = [1,2,3,1,2,3]
list_[0::3] # 1,1
list_[1::3] # 2,2



#get next item
#using iter()
eg. a_iter = iter(a)
		next(a_iter)


#get index:
#use 'if item in list_' or try/except block that catches valueError when item not present.
eg. list_.index('') #returns index 
eg. reverse(list_).index('')


#get index based on partial string
eg. l = [mylist.index(i) for i in mylist if 'aa' in i]
#with enumerate:
eg. indices = [i for i, s in enumerate(mylist) if 'aa' in s]



#number of occurances: (import collections)
collections.Counter(iterable) #returns the number of times an element occurs in an iterable.
iterable.most_common(3) #returns the three most common elements.


#lowest number in the list
eg. min(1, 2, 3, 4, 0, 2, 1) #returns 0
#highest number
eg. max(1, 2, 3, 4, 0, 2, 1) #returns 7

#distance of a number from 0 (absolute value)
eg. print(abs(-99)) #returns 99



#sum of all numbers
eg. sum([1, 2, 3, 4, 5]) #returns 15
									


# get average of list contents
sum(list_) / float(len(list_))
#alternately, instead of casting to float, you can add 0.0 to the sum.
sum(list_, 0.0) / len(list_)
#or using numpy: (import numpy as np)
np.mean(list_)

# normalize list contents (with face normals; dividing a nonzero normal vector by its vector norm)
normalizedList = [float(i)/max(list_) for i in list_]
normalizedList = [float(i)/sum(list_) for i in list_]
#if list contains negative values:
normalizedList = [float(i)-min(list_)/(max(list_)-min(list_)) for i in list_]



#convert data type
eg. list(map(int, list_)) # [1, 2, 3]
eg. [map(int, x) for x in list_] #ie. from str to int/float   python3: [list(map(int, x)) for x in T1]
eg. [[int(column) for column in row] for row in list_]
eg. [[int(y) for y in x] for x in T1]
#exclued non-integer string values: (may fail on neg values. also: try/except)
eg. list(list(int(a) for a in b) for b in list_ if a.isdigit())



#Remove capitalization #dot notation only works with strings
eg. list_.lower()          
eg. map(str.lower,['A','B','C']) #['a', 'b', 'c']

# Convert to ALL caps
eg. list_.upper()
eg. map(str.upper,['a','b','c']) #['A', 'B', 'C']




#append object at end. List.append(element)            
eg. [1, 2, 3].append([4, 5]) #returns: [1, 2, 3, [4, 5]]
#when modifying lists; If it changes the object in place, it returns None. 
#If it creates a new object, it returns the new object.
eg. list_.append([1,2,3], 4) #appends [1,2,3] and 4 to list_


#append the contents of an iterable to the end of a list:              
eg. [1, 2, 3].extend([4, 5]) #returns: [1, 2, 3, 4, 5] 


#insert at the beginning of the list        
eg. list_.insert(0, 'x')

#insert at given position          
eg. [1, 2, 3].insert(0, 5) #or (0, [4,5,6]) to insert a list  #returns [5, 1, 2, 3]        

#move an element
list_.insert(0, list_.pop(list_.index('element'))) #moves 'element' to index 0

# replace an element
eg. list_[list_.index(item)] = replaceWiththis

# replace elements in a list as rounded values
eg. for pos in point:
		roundedPos = round(pos, 2)
		index = point.index(pos)
		point[index] = roundedPos


#reverse a list
eg. list_.reverse()
#does not return a list. You can get a reversed list using:
eg. list(reversed(list_))
#or using slicing:
eg. list_[::-1]


#sort objects of list in alphabetical order. 
eg. list_.sort([func]) #sort with compare function
#using sorted:
eg. sorted(list_, reverse=True) #creates a new list from a provided iterable, sorts it and returns it 


# Sort a list of lists by length and value
eg. list1 = [[0, 4, 1, 5], [3, 1, 5], [4, 0, 1, 5]]
		sorted(list1, key=lambda l: (len(l), l)) #returns [[3, 1, 5], [0, 4, 1, 5], [4, 0, 1, 5]]


#re-order by length.
a.sort(key=len)
sorted(a, key=len)
#decending order:
a.sort(key=len, reverse=True)




#compare two lists.
#without duplicates:
set(x) == set(y) #returns bool. set removes duplicates so will not check for that
#with duplicates:
#import collections
compare = lambda x, y: collections.Counter(x) == collections.Counter(y) #returns bool.





#compare elements of lists.
#using >, <, ==
#or using cmp
eg. cmp(list1, list2) #Compare the two objects x and y and return an integer
#The return value is:
# negative if x < y
# zero if x == y
# positive if x > y
#or using any/all
eg. all(i in a for i in b)
eg. any(i in a for i in b)
eg. any((True for i in a if i in b))
#using 'any' with a generator:
if any(x in d for x in [a, b, c]):
#using zip
[str_ for int_,str_ in zip([1,2,3], ['1','2','3']) if int_>1] #returns ['2','3']
#list comprehension
[i for i in a if i in b]



#elements in one list not in another (inverse)
#using numpy (import numpy as np)
#for only unique elements:
ex. inverse = np.setdiff1d(list2, list1) #returns ie. ['1', '2']
#otherwise:
ex. inverse = np.setdiff1d(list2, list1, assume_unique=True) #returns ie. ['1', '2', '2']
#uing itertools (from itertools import filterfalse)
main_list = list(filterfalse(set(list_1).__contains__, list_2))
#list comprehension
ex. inverse = [item for item in list2 if item not in list1] #For larger list_1, you'd want to preconvert to a set/frozenset, e.g. set_1 = frozenset(list_1), then main_list = [item for item in list_2 if item not in set_1], reducing the check time from O(n) per item to (roughly) O(1)
#zip lists together to compare element by element
ex. inverse = [b for a, b in zip(list1, list2) if a!= b]
#using sets (doesnt preserve order)
ex. list(set(list2) - set(list1)) #leave out the final list converstion if an end result set is fine
ex. list(set(list2).difference(list1))


#get common elements between two lists
common_elements = list(set(list1).intersection(list2)) #returns the unique common elements, but not any repeated elements that may exist.


#combine lists
eg. [1, 2, 3] + [4, 5, 6] #results in [1, 2, 3, 4, 5, 6]
#using append
eg. list_.append(list_1 + list_2 + list_3)

#concatenate/combine elements of a list:
#of strings
eg. ','.join(['spam', 'ham', 'eggs']) #returns spam, ham, eggs
eg. '\n'.join(['spam', 'ham', 'eggs']) #to print each element on a new line

#using non string elements
eg. str(list_of_ints).strip('[]') #returns 80,443,8080,8081 from [80,443,8080,8081]
eg. str(list_of_ints)[1:-1]
#using generator expression  conserves memory by not building the list at all (vs list comprehension). Instead of creating the entire list in memory at once, they generate each element as required.
ex. ','.join(str(x) for x in list_)
#using list comprehension
eg. ','.join([str(x) for x in list_])
#using lambda
eg. ','.join(map( lambda x: str(x), list_))

#convert non string elements to strings and then combine
eg. ', '.join(map(str, list_of_ints)) #returns 80, 443, 8080, 8081


#flatten list (combine a list of lists)
#nested list comprehension (third fastest)
eg. flattened = [i for sublist in list_ for i in sublist]
#list addition with the += operator (fastest)
flattened=[]
for sublist in list_:
    flattened += sublist
#List.extend (second fastest)
flattened=[]
for sublist in list_:
    flattened.extend(sublist)
#List.append (fourth fastest)
flattened=[]
for sublist in list_:
    for val in sublist:
        flattened.append(val)
#using itertools (from itertools import chain.)
eg. list(chain(*list_of_lists))
eg. list(chain.from_iterable(list_of_lists))



#combine sequential numbers into separate lists eg. [1,4,5,6] becomes [[1],[4,5,6]] #sequence
eg. split = [0]+[i for i in range(1,len(list_)) if list_[i]-list_[i-1]>1]+[None]
		list_=[list_[b:e] for (b, e) in [(split[i-1],split[i]) for i in range(1,len(split))]]
eg. [list(map(itemgetter(1), g)) for k, g in groupby(enumerate(list_), lambda x: x[0]-x[1])]
eg.	#from operator import itemgetter #from itertools import *
	for k, g in groupby(enumerate(list_), lambda (i,x):i-x):
		NewList.append(map(itemgetter(1), g))


#combine lists that share elements ie. l = [['a', 'b', 'c'], ['d', 'e', 'a'], ['f', 'g']]
eg:	out=[]
	while len(l)>0:
	    first, *rest = l
	    first = set(first)

	    lf = -1
	    while len(first)>lf:
	        lf = len(first)

	        rest2 = []
	        for r in rest:
	            if len(first.intersection(set(r)))>0:
	                first |= set(r)
	            else:
	                rest2.append(r)     
	        rest = rest2

	    out.append(first)
	    l = rest

	print(out)

#using itertools: (import itertools; from itertools import product, groupby)
eg.	l=[set(x) for x in l] #inner lists to sets (to list of sets)

	for a,b in product(l,l): #cartesian product merging elements if some element in common
	    if a.intersection( b ):
	       a.update(b)
	       b.update(a)

	l = sorted([sorted(list(x)) for x in l]) #back to list of lists
	list(l for l,_ in groupby(l)) #remove duplicates

#alt using itertools: (import itertools)
eg.	l2 = set(itertools.chain.from_iterable(l1)) #ll is {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'k', 'o', 'p'}

	for each in l2:
	  components = [x for x in l1 if each in x]
	  for i in components:
	    l1.remove(i)
	  l1 += [list(set(itertools.chain.from_iterable(components)))]




#convert bitArray to an array
#bitArray to list of indices:
eg. [i for i, bit in enumerate(bitArray) if bit==1] #returns a list of indices that are on (True). useful if indices correspond to component numbers



#remove an element
#by value
#remove first occurance (raises ValueError if element not in list)
eg. list_.remove(element)
#all occurances using linear function
eg. list_ = list(filter(lambda x: x!= 2, list_))
#all occurances using list comprehension
eg. list_ = [x for x in list_ if x != 20]
#by index or specify a slice [::-1]
eg. del list_[-1] #deletes the last element
#to delete an item x.pop(index)
eg. x.pop(0)#delete the first index.
#
eg. x.pop(list_.index(x))


#remove duplicates in a list: 
#If list order is not important, then convert to a set.
eg. set_ = set(list_) 
#convert back to list using list()
eg. list_ = list(set(list_))
#else, to maintain list order:
eg. for l in list_:
		if list_.count(l)>1:
			list_.remove(l)
eg. l=[]; [l.append(i) for i in list_ if not l.count(i)]
	print list(reversed(l))
#or using OrderedDict: (will not work for a unhashable type aka; a list of dictionaries)
	list(OrderedDict.fromkeys(list_))
eg.	from collections import OrderedDict
	print list(reversed(OrderedDict.fromkeys(reversed(list_))))
eg. from collections import OrderedDict
	OrderedDict((x, True) for x in list_).keys()
	# use the fact that OrderedDict remembers the insertion order of keys, 
	# and does not change it when a value at a particular key is updated. 
	# We insert True as values, but we could insert anything, values are just not used. 
	# (set works a lot like a dict with ignored values, too.)



#remove specific elements:
#using list comprehension:
eg. [ x for x in list_ if '2' not in x ] #returns ['1', '336'] from ['1', '32', '523', '336']
eg. [i for i in list_ if i] #remove None values from list:
#using filter:
eg. list(filter(None, list_))




#remove all elements of one list from another:
eg. [x for x in list1 if x not in list2] #new list will contain [1, 6], can be reversed to return those not in l2.
#or using sets: (element ordering is lost)
eg. set_ = set(list1) -set(list2) 


#strip characters from each element in a list. #see strings\.strip. 
#'www.example.com'.strip('cmowz.') #returns 'example'
eg. [x.strip() for x in list_] #with list comprehension
#strip using map function
# with a lambda
eg. strip_list = map(lambda it: it.strip(), lines)
# without a lambda
eg. strip_list = map(str.strip, lines)



#delete an entire list
eg. del list_[:]
#using slice:   
eg. list_[:]=[]
#by assigning an empty list to the list variable (clear list)
eg. list_=[]
#
eg. list_.clear()						


#delete multiple elements
list_ = [1,2,3,4,5]
del list_[::2] # [2, 4]
#delete every nth
del list_[1::2] #[1, 2, 5]






'Tuples___unmodifiable lists________________________________________________________________'
#,  created the same as lists but with () instead of []

#convert to tuple
tuple()

List  = [123, 'xyz', 'zara', 'abc'];
Tuple = tuple(aList)

print 'Tuple elements : ', aTuple
#prints:  Tuple elements :  (123, 'xyz', 'zara', 'abc')



#Convert a tuple into a list
list(seq)











'Sets_______________________________________________________________________________________'
#Sets share several list operations such as len. They are unordered and therefore cannot
# be indexed. They cannot contain duplicate elements. Because of the way they are stored
# they are faster in retrieving results than lists, but are slower to iterate over.

# creating a set:
eg. set() #Creates an empty set
eg. set([1,2,3,4,'5']) #creates a set 1,2,3,4,'5'


# add element
eg. s.add(-6) #appends integer -6 to the set

# get element (random as sets are not ordered)
eg. e = next(iter(s))


#check membership
x in s
x not in s


# query set elements between two sets
s.issubset(t)             s <= t  #test whether every element in s is in t
s.issuperset(t)           s >= t  #test whether every element in t is in s




#combine lists as sets sorted by index
#using zip (zip can take more than two arguments)
zip([1,2,3], [1,2,3]) #returns [(1, 1), (2, 2), (3, 3)]


# combining sets with other iterable objects:
eg. print (s|=t)
eg. print s.update(t)
s.update(t)               s |= t  #return set s with elements added from t
s.intersection_update(t)  s &= t  #return set s keeping only elements also found in t
s.difference_update(t)    s -= t  #return set s after removing elements found in t
s.symmetric_difference_update(t)  s ^= t #return set s with elements from s or t but not both
s.union(t)                s | t   #new set with elements from both s and t
s.intersection(t)         s & t   #new set with elements common to s and t
s.difference(t)           s - t   #new set with elements in s but not in t
s.symmetric_difference(t) s ^ t   #new set with elements in either s or t but not both
s.copy()                          #new set with a shallow copy of s



#remove element
# raises KeyError if not present.
eg. s.remove(1)
# does not throw error if key doesn't exist.
eg. s.discard(x)

# remove and return an arbitrary element; raises KeyError if empty
eg. s.pop()


# remove all elements
s.clear()


# subtract the elements of one set from another
set([1,2,6,8]) - set([2,3,5,8])
#returns set([1, 6])










'Dictionary__(aka_hashtable,map_/_associative_array)___used_to_bind_keys_to_values__________'
# keys are Immutable objects (cannot be changed).



d = {} #empty dictionary

d = {'key1':1, 'key2':2, 'key3':3}  # assign <key:value> on creation



#create dictionary with all keys having the same value:
#dict.fromkeys is the fastest way to create a dictionary where all the keys map to the same value.
eg. dict.fromkeys(range(1, 11), True) #returns {1: True, 2: True, 3: True, 4: True, 5: True, 6: True, 7: True, 8: True, 9: True, 10: True}

#dict of list values with integer keys
dict_ = dict(enumerate(list_, 0)) #starting from 0
#using itertools:
from itertools import count
dict_ = dict(zip(list_, count(0))) #starting from 0
#using range, len and zip:
dict_ = dict(zip(list_, range(x, len(list_)+x)))


#using dictionary comprehension
eg. dict_ = {key: value for key in range(5)}




#set Key:Value pair
#d['key'] = 'value'
eg.	myDict['key'] = 'value' #dict_name[new_key] = new_value
#using setdefault
dict_.setdefault('key', 'value') #returns 'value' and modifies dict_ with new key value pair.
#create key:list value and append
dict_.setdefault('key', []).append('value')
#using update
dict_.update({'key':'value'})
#__setitem__ (poor performance(computationally inefficient))
dict_.__setitem__('key', 'value')
#using * (creates a new dict)
eg. dict_ = {**oldDict, **{'key': 'value'}}



# append to an existing key:
dict_['key'].append('value')
temp = dict_['key']
temp.extend(new_value)
dict_['key'] = temp



#get all keys:
eg. dict_.keys() #dict_.iterkeys() (python 2.x)
#get all values:
eg. dict_.values() #eg. dict_.itervalues() (python 2.x)
#get key and values:
eg. dict_.items() #eg.	dict_.iteritems() (python 2.x)


# Get Value using Key.
dictionary['key']
dictionary.get('key')
#specify default value for key. If none is specified the value returns None.
dictionary.get('key', default_value)


# Get Key using value
eg. [i for i in dict_ if dict_[i]=='something']
#returns the first key assigned to value 'something'
eg. next(key for key, value in dict_.items() if value=='something')
#return first key with value something and key not somethingElse
eg. next(key for key, value in dict_.items() if value=='something' and key not 'somethingElse')
#key from value as a element in a list:
eg. [i for i in dict_ if dict_[i][0]=='something']


# Get min/max
#min key
eg. min(dict_, key=dict_.get)
#max value
eg. max(dict_, value=dict_.get)




# check membership
#for key
#searches dictionary KEYS (returns: boolean)
if key in dict_:
if key not in dict_:
# has_key (returns: bool)  removed in python 3 and half as fast as using 'if in' statement 
dict_ = {'1':'one','2':'two'}
dict_.has_key('1')





# looping
#keys
eg. key in dict_
#values:
eg. value in dict_.itervalues()
#keys and values:
eg.	key, value in dict_.iteritems()
#keys, values, and indices:
eg. index, (key, value) in enumerate(dict_.items())



# match key values in two dictionaries
for key, value in dict1.viewitems() & dict2.viewitems():
	print '%s: %s is present in both dict1 and dict2' % (key, value)
# The & operator here gives you the intersection of both sets; alternatively you could write:
set(dict1.items()).intersection(set(dict2.items()))
# A shortcut would be to only test the keys:
for key in set(dict1) & set(dict2):
	if dict1[key] == dict2[key]:
		print '%s: %s is present in both dict1 and dict2' % (key, value)
# alt
eg. all(dict2[k] == v for k, v in dict1.iteritems() if k in dict2)





# add key (or value) from a dictionary to a list
listContents=[]
for key in seqDict:
	listContents.append(key)
# using list comprehension
eg. [k for k in _sbDict]



# Switch key/value pairs:
result = dict((v,k) for k,v in dict_.iteritems()) #python 3: result = {v:k for k,v in dict_.items()}



# merge duplicate values into single keys:
#from: {'key1':'b', 'key2':'b'}
#to:   {'key1': 'b'}
temp = {v: k for k,v in dict_.items()} #{tuple(y): x .. for nested dicts
print dict([[v,k] for k,v in temp.items()])


# combine keys with duplicate values into lists by inverting:
#from: {'a':1, 'b':2, 'c':3, 'd':2}
#to:   {1: ['a'], 2: ['b', 'd'], 3: ['c']}
from itertools import groupby
print {k : [i[0] for i in list(v)] for k, v in groupby(dict_.items(),lambda x:x[1])}
#same as:
invert = {}
for k, v in dict_.iteritems():
	keys = invert.setdefault(v, [])
	keys.append(k)


# merge two dictionaries:
dict1.update(dict2)
#or #(without overwriting duplicates)
eg. dict_ = dict(dict1, **dict2)


# merge values of two dictionaries by index:
# for key in dict1:
#   if key in dict2:



#sort (acsending or decending using reverse)
#by key
eg. sorted = sorted(dict_)
#by key using collections (output as a dict)
eg. sorted = OrderedDict(dict_)
#by key using operator (output as a list)
eg. sorted = sorted(dict_.items(), key=operator.itemgetter(0))
#by value using operator (output as a list)
eg. sorted = sorted(dict_.items(), key=operator.itemgetter(1))



# SWITCH/CASE using a dictionary
#when you pass an argument to the switch_demo function, it is looked up against the switcher dictionary mapping. 
#If a match is found, the associated value is returned, else a default string (‘Invalid Month’) is printed.
def switch_demo(argument):
	switcher = {
			1: 'January',
			2: 'February',
			3: 'March',
			4: 'April'
	return switcher.get(argument, 'Invalid month')

superClassDict = {
			GeometryClass: 'GeometryClass',
			shape: 'shape',
			light: 'light',
			camera: 'camera',
			SpacewarpObject: 'SpacewarpObject',
			helper: 'helper',
			system: 'system',
			default: 'default' #aka unknown type
		}
		superClass = superClassDict.get(superClass,'superClass: Unknown')




#building a simple hash table in python
hash_string = '1;2;3' #can be built dynamically
hash_ = {}
(hash_['key1'],hash_['key2'],hash_['key3'])=hash_string.split(';')
print (hash_['key2'])


#using a hash table to compare two sets for common elements
from maya.api.OpenMaya import MVector

class PointHash(object):

		def __init__(self, p1, p2, v):
				self.p1 = p1
				self.p2 = p2
				self.value = v
				self._hashvalue = hash((p1.x, p1.y, p1.z, p2.x, p2.y, p2.z, v))

		def __hash__(self):
				return self._hashvalue

		def __eq__(self, other):
				return hash(self) == hash(other)

		def __repr__(self):
				return 'PointHash %i' % self.__hash__()

#sample data
a = MVector(1.1, 2.2, 3.3)
b = MVector(1.0009, 2.00019, 3.0001)
c = MVector(21.0, 22.0, 23.0)

# some lists
set_one = set((PointHash(a, b, 1.0), PointHash(b, a, 1.0), PointHash(a, b, 2.0), PointHash(b, c, 1.0)))
set_two = set((PointHash(a, b, 1.0), PointHash(b, a, 1.1), PointHash(a, b, -1.0), PointHash(b, c, 1.0)))

print 'common:'
for item in set_one.intersection(set_two):
		print item.p1, item.p2, item.value





# dictionary comprehension
#combine two lists in a dictionary as key/value pairs
{n:list2[i] for i, n in enumerate(list1)}
#list index as key and int as value
dct = {i:k for i,k in enumerate(list_,x)}
#list index as value and int as key 
dct = {k:i for i,k in enumerate(list_,x)}





# Delete
#key (returns the value of the key upon deletion)
eg. dict_.pop('key', None) #if key doesn't exist; return the second argument.

#value              
eg. del dict_['key']
#element from a list stored as a value
eg. dict_['key'].remove('item in list')

#all keys/values
dict_.clear()
















'Functions_(subroutines)____________________________________________________________________'
#functions are first-class objects. This means that functions can be passed around
#, and used as arguments, just like any other value 


#lambda
ex.
widgetType = lambda n='i021': n[0] if [c for c in n[1:] if c.isdigit()] else n


#nested functions
#Inner functions can access variables from the enclosing scope.
eg.		def parent():
			print('Printing from the parent() function.')

			def first_child():
				return 'Printing from the first_child() function.'

			def second_child():
				return 'Printing from the second_child() function.'

		print(first_child())
		print(second_child())
		#calling parent() returns; Printing from the parent() function.
															#Printing from the first_child() function.
															#Printing from the second_child() function

#return a function from within another function.
built-in  functions list:   #https://docs.python.org/2/library/functions.html


header    The header includes the def keyword, the variable name of the function
					& any argument parameters that the function requires. eg. def hello_world(): 

					eg. def function(arg):#header: def, function name, any arguments
						return arg *2

body      Indented body which describes the procedures the function carries out.


print      just shows the human user a string representing what is going on inside the 
						computer

return     The return statement causes your function to exit and hand back a value to
						its caller.





# Scope
#defining global functions
def create_global_function():
		global foo
		def foo(): return 'bar'

#The same applies to a class body or method:
class ClassWithGlobalFunction:
		global spam
		def spam(): return 'eggs'

		def method(self):
				global monty
				def monty(): return 'python'

class X:
	global d
	def d():
		print 'I might be defined in a class, but I\'m global'









'Lambda_Expressions_(anonymous_function)____________________________________________________'

# Are single-expression functions that are not necessarily bound to a name (they can be anonymous).
# Can't use regular Python statements and always include an implicit return statement.

eg. add = lambda x, y: x + y #add(5, 3) returns: 8
#alt:
eg. (lambda x, y: x + y)(5, 3) #returns: 8



eg. lambda x,y: x+y #can be assigned a variable although it is usually better to just define a function with def
 


eg. def function(arg1, arg2):             
#lambda function plugged into another function as an argument where 
# (lambda x: 2*x) == arg1 and 5 == arg2
		return arg1(arg2)

	 function(lambda x: 2*x, 5)



# lambda functions with lists 
variable = list(map(lambda x: x+5, myList)) 
#map allows to preform a function across a list. 
#In this case a lambda function is used to simplify things
#using list explicitly before map converts the result into a list. 
# without this the result will not print.



filter  
variable = list(filter(lambda x: x < 5, myList)) 
#filters out items in the list that do not match a predicate 
# (a function that returns a boolean).











'Generators_(coroutines)____________________________________________________________________'

generators  #are iterators, but you can only iterate over them once. Its because they do
			#not store all the values in memory. As they iterate through a list they 
			#preform one funtion, drop it from memory and move on to the next. 

			eg. myGenerator = (x*x for x in range(3)) #define the generator function
				for i in myGenerator: #iterate through the range of 3 (0,1,2) and 
					print(i) #prints 0 1 4
					



yield       #instead of a return statement the yield statement returns a generator.
			#When you call the function, the code you have writted in the function body
			# does not run. The function only returns the generator object.
			#Then, your code will be run each time the for uses the generator.
			#Meaning the function does not neccissarily re-start at line one but to
			# where the yield statement sends it after evaluating. 
			#The body of a generator can also contain a return statement if needed.

			eg. def f():
					while True:
						yield 7 #generate 7's

			eg. def f(x):
					for i in range(x):
						if i<11:
							yield i #re-define i



next()      eg. gen = generator #assuming already have a generator defined
				next(gen) #iterates to generators next value.
				next(gen) #and the value after that. When the end is reached and next is
									# called an error will occur. Unless working with a while
									# loop and an infinate condition. 
									#if not called again the state when last called is 
									# (eventually) discarded.









'Decorators_________________________________________________________________________________'
# * Decorators allow to modify a function while leaving the origional function intact.
# * A decorated function is wrapped by a function which calls the decorated function and returns 
# 	what it returns.
# * A single function can have multiple decorators to extend functionality.

#basic decorator
ex.
@classmethod
def message(cls, fn):
	def wrapper(self, *args, **kwargs):
		self.messageBox(self, *args, **kwargs)
		return fn(self, *args, **kwargs)
	return wrapper


#using functools wraps
from functools import wraps

def mydecorator(f):
	@wraps(f)
	def wrapped(*args, **kwargs):
		print 'Before decorated function'
		r = f(*args, **kwargs)
		print 'After decorated function'
		return r

@mydecorator
def myfunc(myarg):
	print 'my function', myarg
	return 'return value'

r = myfunc('asdf')


# decorator usage in an inherited class:
class X(object):
    @classmethod
    def foo(cls, fun):
        def wrapper(self, *args, **kwargs):
            self.write(*args, **kwargs)
            return fun(self, *args, **kwargs)
        return wrapper

    def write(self, *args, **kwargs):
        print(args, kwargs)

class Y(X):
    @X.foo
    def bar(self, x):
        print("x:", x)

Y().bar(3)







'Recursion__________________________________________________________________________________'
#Recursion
eg. 
def removeDups(word):
	if len(word) <= 1:
		return word
	elif word[0] == [1]:
		return removeDups(word[1:])
	else:                         
		return word[0] + removeDups(word[1:])#recursion is a function within a
																				 # function, calling that functions
word = 'aabbccdd'                        # value & preforming any needed
print (removeDups(word))                 # changes to it. In this case it's
																				 # iterating over a list.











'Classes____________________________________________________________________________________'



#get Docstring
class_.__doc__ #gives us the docstring of that class.



#get class:
#all within current module
eg. [o for n, o in inspect.getmembers(sys.modules[__name__], inspect.isclass) if o.__module__ is __name__]


#get class name (str)
eg. classInstance.__class__.__name__
#all within current module (str)
eg. [n for n, o in inspect.getmembers(sys.modules[__name__], inspect.isclass) if o.__module__ is __name__]





#get class attributes
#using dir(): 
dir(Class)
#get only keyword results (empty string returns all)
kw = ''
limit = None #int or None - limit amount of returned results.
print [i for i in dir(uv) if kw in i or kw.title() in i or kw.swapcase() in i or kw.upper() in i or kw.lower() in i][:limit]

#using __dict__:
Class.__dict__ #get the attributes defined for the instance. returns: {attribute name:value}

#
vars(Class)

#using help():
help(Class) # Class information

#using inspect (import inspect):
inspect.getmembers(Class, predicate=inspect.isroutine) #predicate=inspect.ismethod
#alt (same output as inspect method)
methods = [(m, getattr(c, m)) for m in dir(c) if callable(getattr(c, m)) and not all([m.startswith('__'), m.endswith('__')])] #c = class



#check if instance:
obj.isinstance(potentialInstOf, Class) # is instance of class [bool]
obj.issubclass(potentialSubcalss, Class) # is class subclass of [bool]
#
issubclass(SubClass, object)

#get subclasses
class_.__subclasses__()



#check if instance exists:
'instance' in locals()
'instance' in globals()


#number of instances:
class Obj:
	_counter = 0
	def __init__(self):
		Obj._counter += 1
		self.id = Obj._counter
#using itertools:
from itertools import count

class Obj(object):
  _ids = count(0)

  def __init__(self):
	self.id = next(self._ids)
#using a generator:
def get_next_id():
	curr_id = 1
	while True:
		yield curr_id
		curr_id += 1




#get class object from name string.
class_ = globals()['ClassName']() #(returns a dictionary with global symbol table.)
class_ = locals()['methodName']() #(returns a dictionary with a current local symbol table.)
#the current script/module's global variables as a dictionary 
class_ = globals()[self.__class__.__name__]
class_ = getattr(sys.modules[__name__], 'ClassName')()
class_ = getattr(sys.modules[__main__], 'ClassName')()

#using getattr multiple times:
print(getattr(getattr(Class, attribute)), 'methodName')() ()


# get the object value and in this case assign it to a variable.
buttonObject = getattr(self.ui, 'string')() #You can use getattr along with dir to iterate over all attribute names and get their values:
#using getattr with additional arguments:
buttonObject = getattr(obj, attribute)(arg1, arg2, arg3)
#with args/kwargs:
args = ['flip', 'do']
kwargs = {'foo':'bar'}
buttonObject = getattr(obj, attribute)(*args, **kwargs)


#get object attributes:
#using dict:
vars(obj)		#returns __dict__
obj.__dict__	#ex. {'multi': 4, 'str': '2'}
#using dir:
dir(obj)		#returns __dir__
obj.__dir__()	#ex. ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'multi', 'str']






# check if class object attribute exists.
if hasattr(self.ui, 'string')


#allows you to set an attribute of an object having its name
setattr(person, 'Name', 'Linus')
person.name  # accessing instance attribute
#returns 'Linus'
Person.name  # accessing class attribute
#returns 'Name'

setattr(x, 'y', v) #is equivalent to x.y = v






# calling an instance of a class (instantiating the class:)
instance = Class()
instance.classMethod()
#same as (for single use case)
Class().classMethod()
#instance from string using getattr
instance = getattr(module, 'ClassName')()




#bypass/override init method when calling a class
def skip_init(cls):
	actual_init = cls.__init__
	cls.__init__ = lambda *args, **kwargs: None
	instance = cls()
	cls.__init__ = actual_init
	return instance
#use
# a = skip_init(Class)
# a.myfunction()










'Class_Inheritance______________________________________________________________________________'

class Base(object): 
	def __init__(self, a, b):
		print a


class Derived(Base): 
	def __init__(self, a=None, b=None, c=None):
		super(Derived, self).__init__(a, b)
		print a, b

	def method(self):
		print a, b, c


Derived (a='aaa',b='bbb') ##calls baseClass first, then subClass
# returns:
# aaa
# aaa bbb



#get base class from derived
#with single inheritance, __mro__ is just the tuple of: the class, its base, its base's base, and so on up to object.
__class__.__base__
#with multiple inheritance, __mro__ no class is duplicated, and no class comes after its ancestors, classes that first enter at the same level of multiple inheritance are in the __mro__ left to right.
__class__.__mro__[1] #mro() (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <type 'object'>)
__class__.__bases__[0]
#get base class name from derived
__class__.__mro__[1].__name__
__class__.__bases__[0].__name__



#super(subClass, instance).method(args)
#using 'super' to call base class init method and get base class arguments 
super().__init__(argsFromBaseClass) 
# *args **kwargs to pass arguments unmodified to the base class
super().__init__(*args, **kwargs) 

#alternative method explicitly calling the base class
BaseClass.__init__(self, argsFromBaseClass)

class Button(QtCore.QObject):
	def __init__(self, qObject, otherArgs):
		super(Class, self).__init__(qObject)

super(ChildClass, self).method()



#passing arguments to child of a class
class Main(object):
	def __init__(self, master):
		self.master = master
		self.display()
				
	def display(self):
		self.p = 2
		self.pp = 0
		# to make self.p and self.pp available to class Child
		# pass them on as instance arguments
		child = Child(self.p, self.pp)
				
class Child(object):
	def __init__(self, p, pp): # if the derived class doesn't have __init__, base one will be used instead.
		total = p * pp
		print 'final price =', total

main = Main('dummy')



class Parent(object):
	def do_stuff(self, a, b):
		# some logic

class Child(Parent):
	def do_stuff(self, c, *args, **kwargs):
		super(Child, self).do_stuff(*args, **kwargs)
			# some logic with c











'classmethod_&_staticmethod_________________________________________________________________'

# static & class methods

# class method takes class as first argument instead of instance (self).
# static method is simply a reg method nested within a class that doesn't require an instance (self) argument.
class Date(object):

		def __init__(self, day=0, month=0, year=0): #constructor
				self.day = day
				self.month = month
				self.year = year

		#'cls' holds class itself, not an instance of the class as 'self' does.
		# if you define something to be a classmethod, it is probably because you intend to call it from the class rather than from a class instance.
		@classmethod
		def from_string(cls, date_as_string): 
				date1 = cls(day, month, year)
				return date1

		@staticmethod
		def is_date_valid(date_as_string):
				day, month, year = map(int, date_as_string.split('-'))
				return day <= 31 and month <= 12 and year <= 3999

date2 = Date.from_string('11-09-2012')
is_date = Date.is_date_valid('11-09-2012')











'property___________________________________________________________________________________'
#properties provide a way of customizing access to instance attributes. such as read-only
def foo(self): #when the instance method with the same name as the method is accessed, the
	return self._foo                                          #method will be called instead.
attribute = property(setAttributeFunc, getAttributeFunc)
#to define a setter/getter, you need to use a decorator of the same name as the property,
#followed by a dot and setter/getter keyword.
@setAttributeFunc.setter
def setAttributeFunc(self,value):
# @property
#allows to call class as an attribute '.foo' instead of a class method '.foo()''
@property
def foo(self):
	return self._foo











'Magic Methods_(dunder_methods)_____________________________________________________________'
class X:
	def __init__(self,x,y):#magic method.
		self.x = x
		self.y = y

class Y:
	def __add__(self,z):
		return X()   


eg. 
class Polygon: #define super class
	def __init__(self, vertices, faces) #magic method & attributes
		self.vertices = verts #assign variables to attributes
		self.faces    = faces

	class Cube: #define a subclass.                          eg. cube.faces()
	def cube(Polygon): #methods of a subclass can be called globally.
		cube.faces = 6 #subclass overrides inherits of a superclass unless
		cube.verts = 8 # 'super' is called. eg. super().superclassFuncName()
		return cube.faces

	class Sphere:
	def sphere(Polygon):  




dir(__builtins__)   #command lists all python built-in methods.
help(method_name)   #lists information on that module.

#basic:             initialization, new & delete
__init__  


__str__             enduser output.   readable output.
__repr__            debugging output. generate output which can be read by the interpreter 
					#possible use for formatting


__abstractmethods__
__base__
__bases__ 				#The tuple of base classes of a class object.



__basicsize__
__call__
__class__ 				#The class to which a class instance belongs.
__delattr__
__dict__ 				#A dictionary or other mapping object used to store an object’s (writable) attributes.
__dictoffset__
__dir__
__doc__
__eq__
__flags__
__format__
__ge__
__getattribute__
__gt__
__hash__
__init__
__instancecheck__
__itemsize__
__le__
__lt__
__module__				
__mro__ 				#also: mro() This attribute is a tuple of classes that are considered when looking for base classes during method resolution.
__name__ 				#The name of the class, type, function, method, descriptor, or generator instance.
__ne__
__new__
__prepare__
__qualname__
__reduce__
__reduce_ex__
__repr__
__setattr__
__sizeof__
__subclasscheck__
__subclasses__ 			#Each new-style class keeps a list of weak references to its immediate subclasses. This method returns a list of all those references still alive.
__subclasshook__
__weakrefoffset__



python3:
__self__ 		#(Read-Only) the class instance object, 
__func__ 		#(Read-Only) the function object;
__doc__ 		#(Writable) The function’s documentation string, or None if unavailable; not inherited by subclasses.
__name__ 		#(Writable) The function’s name.
__qualname__	#(Writable) The function’s qualified name.
__module__		#(Writable) The name of the module the function was defined in, or None if unavailable.
__defaults__	#(Writable) A tuple containing default argument values for those arguments that have defaults, or None if no arguments have a default value.
__code__		#(Writable) The code object representing the compiled function body.
__globals__		#(Read-Only) A reference to the dictionary that holds the function’s global variables — the global namespace of the module in which the function was defined.
__dict__		#The namespace supporting arbitrary function attributes.
__closure__		#(Read-Only) None or a tuple of cells that contain bindings for the function’s free variables. See below for information on the cell_contents attribute.
__annotations__ #(Writable) A dict containing annotations of parameters. The keys of the dict are the parameter names, and 'return' for the return annotation, if provided.
__kwdefaults__	#(Writable) A dict containing defaults for keyword-only parameters.






'rich operators:____________________________________________________________________________'
#Perform “rich comparisons” between a and b
#https://docs.python.org/2/library/operator.html

# Ordering
operator.lt(a, b)           #equivalent to a < b
operator.le(a, b)           #equivalent to a <= b
operator.ge(a, b)           #equivalent to a >= b
operator.gt(a, b)           #equivalent to a > b
# Equality
operator.eq(a, b)           #equivalent to a == b
# Difference
operator.ne(a, b)           #equivalent to a != b
# Bitwise And
operator.and_(a, b)         #Return a + b, for a and b numbers    
# Bitwise Or
operator.or_(a, b)          #Return the bitwise or of a and b
#Exclusive Or
operator.xor(a, b)          #Return the bitwise exclusive or of a and b
#Bitwise Inversion
operator.invert(obj)        #Return the bitwise inverse of the number obj  
# Negation (Logical)
operator.not_(obj)          #Return the outcome of not obj     
# Truth Test
operator.truth(obj)         #Return True if obj is true, and False otherwise
# Identity
operator.is_(a, b)          #Return a is b. Tests object identity
operator.is_not             #Return a is not b. Tests object identity
# Addition
operator.add(a, b)          #Return a + b, for a and b numbers
# Subtraction
operator.sub(a, b)          #Return a - b
# Multiplication
operator.mul(a, b)          #Return a * b, for a and b numbers
# Division
operator.div(a, b)          #Return a / b
operator.floordiv(a, b)     #Return a // b
# Exponentiation
operator.pow(a, b)          #Return a ** b
# Absolute Value
operator.abs(obj)           #Return the absolute value of obj
# Modulus
operator.mod(a, b)          #Return a % b
# Negation (Arithmetic)
operator.neg(obj)           #Return obj negated (-obj)
# Positive
operator.pos(obj)           #Return obj positive (+obj)
# Left Shift
operator.lshift(a, b)       #Return a shifted left by b
# Right Shift
operator.rshift(a, b)       #Return a shifted right by b
# Number of Occurrences
operator.countOf(a, b)      #Return the number of occurrences of b in a
# Containment Test
operator.contains(a, b)     #Return the outcome of the test b in a
# Indexing
operator.index(a)           #Return the index of the first of occurrence of b in a
operator.indexOf(a, b)      #Return the index of the first of occurrence of b in a
operator.getitem(a, b)      #Return the value of a at index b
#Indexed Assignment
operator.setitem(a, b, c)   #Set the value of a at index b to c
#Indexed Deletion
operator.delitem(a, b)      #Remove the value of a at index b
# Slicing
.getitem(seq, slice(i, j))          #Return seq[i:j]
#Slice Assignment
.setitem(seq, slice(i, j), values)  #Return seq[i:j] = values
#Slice Deletion
.delitem(seq, slice(i, j))          #Delete seq[i:j]
# Concatenation
operator.concat(a, b)       #Return a + b for a and b sequences
# String Formatting
mod(s, obj)                 #Return s % obj





					 
	 




'User_Input_________________________________________________________________________________'

#raw_imput  promts user input  
eg. var = raw_imput('y')


# using sys module:
# import sys
eg.	print('user input prompt') 
	userInput = sys.stdin.readline()
	print('You have entered', userInput)



eg. var = choice(['A', 'B', 'C'])










'Keyboard/Mouse_____________________________________________________________________________'



# mouse tracking:
class Point(Structure):
	_fields_ = [("x", c_long), ("y", c_long)]


def getMousePosition():
	pt = Point()
	windll.user32.GetCursorPos(byref(pt))
	return {"x": pt.x, "y": pt.y}





# .net framework
#--getKeyState---------------------------------------------------------------------------
#using ctypes (from ctypes import windll)
#The state will either be 0 or 1 when not pressed, and increase to something like 60000 when 
#pressed, so to get a True/False result, checking for > 1
#key = virtual-key code #https://msdn.microsoft.com/en-us/library/windows/desktop/dd375731(v=vs.85).aspx
#microsoft docs: https://msdn.microsoft.com/en-us/library/windows/desktop/ff468859(v=vs.85).aspx
def getKeyState(key):
	#args: [string]
	#returns: [bool]
	if (key == 'shift'): #VK_LSHIFT #left
		key = 0xA0
	if (key == 'ctrl'): #VK_CONTR
		key = 0x11
	if (key == 'alt'): #VK_MENU
		key = 0x12
	if (key == 'del'): #VK_DELETE
		key = 0x2E
	if (key == 'esc'): #VK_ESCAPE
		key = 0x1B
	if (key == 'enter'): #VK_RETURN
		key = 0x0D
	value = windll.user32.GetKeyState(key)
	# if value > 1:
	#   return True #key down
	# else:
	#   return False #key up
	#commented out as block was causing odd highlighting in lower notes




# simulate a mouse click
#using ctypes
SetCursorPos = ctypes.windll.user32.SetCursorPos
mouse_event = ctypes.windll.user32.mouse_event

def left_click(x, y, clicks=1):
	SetCursorPos(x, y)
	for i in xrange(clicks):
		mouse_event(2, 0, 0, 0, 0)
		mouse_event(4, 0, 0, 0, 0)

left_click(200, 200) #left clicks at 200, 200 on your screen. Was able to send 10k clicks instantly.




#mouse keyboard actions using ctypes:
#https://docs.microsoft.com/en-us/windows/desktop/api/winuser/nf-winuser-mouse_event
ctypes.windll.user32.SetCursorPos(100, 20) #x,y

ctypes.windll.user32.mouse_event(10, 0, 0, 0,0) #right up, relative coords, dx=0, dy=0
ctypes.windll.user32.mouse_event(8, 0, 0, 0,0) #right down. arg: 8 or 0x8

ctypes.windll.user32.mouse_event(4, 0, 0, 0,0) #left up
ctypes.windll.user32.mouse_event(2, 0, 0, 0,0) #left down

ctypes.windll.user32.mouse_event(40, 0, 0, 0,0) #left up
ctypes.windll.user32.mouse_event(20, 0, 0, 0,0) #left down





#using keyboard module (import keyboard)
shortcut = 'alt+x' #define hot-key



keyboard.add_hotkey(shortcut, event) #attach the function to hot-key








'External_Files_____________________________________________________________________________'
 

# check if the object is a file
#using os.path
eg. os.path.isfile() #returns a boolean value


# get file
#using os.walk and fnmatch: (import os, fnmatch)
def findFile(dir_, pattern):
	for root, dirnames, filenames in os.walk(dir_):
		for fn in fnmatch.filter(filenames, pattern):
			yield os.path.join(root, fn)
print (next(findFile(dir_root, file)))


# get all files of given type
#using glob (import glob)
txt_files = glob.glob('/dir/*.txt') #returns a list.
#using pathlib (from pathlib import Path)
txt_files = Path('/tmp').glob('*.txt') #matches files only in the top level directory.
txt_files = Path('/tmp').glob('*.txt') #matches all files in the directory and all subdirectories, recursively.



# environment variables
# get environment variable
#import os.environ
eg. home = os.environ['HOME']
# using get will return `None` if a key is not present rather than raise a `KeyError`

os.putenv #changes the actual OS-level environment variables, but in a way that doesn't show up through os.getenv, os.environ, or any other stdlib way of inspecting environment variables
#instead use:
os.environ['KEY'] = 'NEW_KEY'
os.environ['KEY'] #Returns: 'NEW_KEY'
os.environ.get('KEY')
# os.getenv is equivalent, and can also give a default value instead of `None`
os.getenv('KEY_THAT_MIGHT_EXIST', default_value)

# get all environment variables:
eg. allVar = os.environ

# check if environment variable exists:
eg. 'HOME' in os.environ





# FILE PATH

#get current folder (import os)
os.path.basename(os.path.abspath('.'))


#get all paths:
#using sys (import sys)
for s in  sys.path: print s


# get current working directory 
#using os.getcwd
eg. os.getcwd() #ie. /Users/mbp/Documents/my-project/python-snippets/notebook
#using os.listdir
eg. os.listdir(os.curdir)

# create a filepath safely using os.join
eg. os.path.join('c:\\', 'temp', 'new folder')

# get module full dir path
eg. __file__ #for current module
eg. module.__file__ #for an imported module (import module). returns: ie. <fullpath>\module.py
# get filename with extension
eg. os.path.basename(__file__)
# get directory name
eg. os.path.dirname(__file__) #ie. data/src

# get absolute path (including file).
eg. os.path.abspath(__file__) #ie. /path/to/dir/foobar.py
# get absolute path (excluding file).
eg. os.path.dirname(os.path.abspath(__file__)) #ie. /path/to/dir/
eg. os.path.split(script_path)[0] #ie. /path/to/dir/
# from relative path
eg. os.path.join(script_dir, 'subfolder/file.txt')
# using inspect (import inspect)
file_path = inspect.getfile(lambda: None)
# alt using inspect (import os, inspect)
currentFrame = inspect.currentframe()
currentFile = os.path.abspath(inspect.getfile(currentFrame))
currentDir = os.path.dirname(currentFile)


# dir navigation
#up one directory
'..'
#up two directory levels etc
'../..'
#using os.path (import os.path)
eg. two_up =  os.path.abspath(os.path.join(__file__ ,'../..')) #__file__=current file. can substitute this for another dir

#get path above current file path:
'/'.join(os.path.dirname(os.path.abspath(__file__)).split('\\')[:-1]) #adjust the [:int] for each dir above.



#append to system path
path = os.path.expandvars(r'%CLOUD%/_programming/Python/2.7/__path/Lib/site-packages/win32')
sys.path.append(path)



#Append multiple directories to the system path
paths = r'%CLOUD%/____Graphics/Maya/scripts/__path;%CLOUD%/____Graphics/Maya/scripts/__path/tk_ui;%CLOUD%/____Graphics/Maya/scripts/__path/tk_slots'''
(sys.path.append(os.path.expandvars(path)) for path in paths.split(';'))


#append relative directories:
#(sys.path[0] = /path/foo/currentModule.py  appended path = /path/foo/bar/sub/dir)
sys.path.append(os.path.join(sys.path[0],'bar','sub','dir')) #os.getcwd(), sys.argv[0], sys.path[0]

#append a directory in an adjacent folder to the current module: 
#(sys.path[0] = /path/foo/currentModule.py  and bar = /path/bar)
sys.path.append(os.path.join(os.path.dirname(sys.path[0]),'bar'))


sys.argv	#list of python command line arguments. ie. python myscript.py -a -b --input myfile --another_argument, would give ['myscript.py', '-a', '-b', '--input', 'myfile', '--another_argument']


# search directory
eg. for (dir,_,files) in os.walk('.'): #('./') 
		for f in files: #indent twice
			path = os.path.join(dir, f) 
			if os.path.exists(path)#: 
				print path #prints file, subfolder/file format



# using glob.glob to list all the files in the current working directory whose filename ends with .mod:
#import fileinput, glob, sys
eg. for line in fileinput.input(glob.glob('*.mod'), inplace=True):
		if fileinput.filelineno() == 32:     
			sys.stdout.write('TextToInsertIntoLine32' '\n') #adds new line and text to line 32 

#get all files in a directory
files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
files = [f for f in os.listdir(directory) if f.endswith('.mod')]

#fileinput will take the filenams from sys.argv by default. You don't even have to use 
# enumerate, as fileinput numbers the lines in each file
#import sys, fileinput
eg. for line in fileinput.input(inplace=True)#:
		sys.stdout.write(line.replace('sit', 'SIT'))
		if fileinput.filelineno() == 30#:
			sys.stdout.write('TextToInsertIntoLine32' '\n')



#search recursively for directory and file names
#import fnmatch, os
eg. matches = []
		for root, dirnames, filenames in os.walk('src'):
			for filename in fnmatch.filter(filenames, '*.c'):
				matches.append(os.path.join(root, filename))




A = os.path.join(os.path.dirname(__file__), '..')
# A is the parent directory of the directory where program resides.

B = os.path.dirname(os.path.realpath(__file__))
# B is the canonicalised (?) directory where the program resides.

C = os.path.abspath(os.path.dirname(__file__))
# C is the absolute path of the directory where the program resides.

# You can see the various values returned from these here (import os)
print __file__
print os.path.join(os.path.dirname(__file__), '..')
print os.path.dirname(os.path.realpath(__file__))
print os.path.abspath(os.path.dirname(__file__))




# RENAME A FILE
os.rename(old, newname)



# move a file
#using shutil (import shutil)
shutil.move(src, dest)
#move and replace existing: (when specifying the full path to the destination, any existing file will be overwritten.)
shutil.move(os.path.join(src, filename), os.path.join(dst, filename))
#using rename
os.rename(src, dest) #using forwardslashes, change the dest path




# get last modified time stamp
fileName = os.path.join(root, sc) #join fileName to include the path.
mtime = os.path.getmtime(file_name) #returns float value which can be used with comparators.
last_modified_date = datetime.fromtimestamp(mtime) #convert to readable format



#OPEN A FILE
#mode arguments:    
# 'r' read mode  #(default)
# 'w' write mode  #re-write the contents of a file. 
# #if it doesnt already exist, it will create a file.
# #if it does exist the contents will be deleted.
# 'a' append mode #adding new content to the end of the file
# 'b' binary mode #non-text files (such as image and sound)
eg. variable = open('path or filename if in same folder as parent', 'specify mode if needed')  
eg. open('filename.bin', 'wb')
eg.	f = open(file_)
#or
eg.	with open(file_) as f: #reassign opened file with a simplified variable
		fileContents = f.read()

#open and convert to a list:
list(open('file.txt') #[line.strip() for line in open('file.txt')]


#open last modified file of a given extension (import glob, os)
eg. path = r'C:\Users\m3\AppData\Roaming\Autodesk\MAYA\Autosave'
		extentions = '*.[mb][ma]*' #* for all, *.mb for single

		list_of_files = glob.glob(path+'/'+extentions)
		latest_file = max(list_of_files, key=os.path.getctime)
		print '// Result: '+latest_file

		pm.openFile (latest_file, open=True, force=True) #pymel syntax for opening a file in maya.


# similar to the exec statement, but parses a python file instead of a string.
#python 2
eg. execfile
#python 3
eg. exec(open('userSetup.py').read())



# READING A FILE:
#if read argument is left empty then it will read the entire file.
eg. contents = file_.read() #can be followed by a print(content) statement

#read a single line from file.
eg. file_.readline()[2] #returns the third line

#read the contents of a file into a list.
eg. list(file_) #list(open('file.txt')
#removing whitespace
eg. [line.strip() for line in open('file.txt')] #['test1', 'test2', 'test3', 'test4']


#returns a list where each element is a line in the file.
#you can use a for loop to iterate through those lines.          
eg. file_.readline() #places newline at the end.
#returns a list containing all the lines in the file.
eg. file_.readlines()
eg.  list_ = [line.split(',') for line in file_]
eg.  list_ = file_.read().splitlines()
#Returns a generator to loop over every single line in the file.
eg. file_.xreadlines() #in most cases you would use 'for line in file:' instead
#read a file and splits it line by multi-line
eg. file_.read().splitlines()[1:] #from the second line of file 'x'
#read all and return slice
eg. contents = file_.read()[1:]
eg. contents = file_.read(optionalArgNumberOfBytesToBeRead ie.16)
#read single (or multiple) character(s) at a time
eg. f = open(file) 
		next = f.read(1)
		while next != '':
			print(next)
			next = f.read(1)

#gets the nth word in nth line
eg. file_.read()[1:2].split()[3] #gets 2nd word in line 2 (also: readline())




# read & write non-string characters in an external file.
eg. json


#get the byte location of an object in the file
#UTF-8 uses one byte for any ASCII character
eg. file.tell() #returns an integer
#search within a given range
eg. file.seek(offset,from_what) 
# 0 -beginning of the file (default)
# 1 -current file position
# 2 -end of file
eg. file.seek(-3,2) #returns 3rd byte before the end of the file.
										









# WRITING TO A FILE
#Write string to file
eg. with open('filename.txt') as f: #creates a variable 'f' that is only accessible within the block statement)
		f.write('write something to the file') #only write as a string
#
eg. with open('file.txt', 'a') as f:
		f.write('hello world') #['test1\n', 'test2\n', 'test3\n', 'test4\n', 'hello world']




#close a file previously opened
eg. f.close() #the file is automatically closed at the end of 'with' statements. also.'try:' & 'finally:'





#get file timestamp
#modified date
eg. os.path.getmtime(file)

#convert to readable format
# using datetime (from datetime import datetime)
eg. datetime.fromtimestamp(1382189138.4196026).strftime('%Y-%m-%d %H:%M:%S') #returns '2013-10-19 16:25:38'




# DELETING FILES AND/OR DIRECTORIES
# delete a file
os.remove(file_path) #use exception handling to catch OSError.
os.unlink(file_path)
#using pathlib (from pathlib import Path)
file_path = Path('/tmp/file.txt')
file_path.unlink()
#check if file exists:
eg. os.path.exists(file_)
#check if file 'isFile':
eg.	os.path.isfile(file_)



# delete a directory
#delete an empty directory
os.rmdir()
#using pathlib (from pathlib import Path)
dir_path = Path('/tmp/img')
dir_path.rmdir()
#delete a non-empty directory.
#using shutil (import shutil)
dir_path = '/tmp/img' #The argument passed to shutil.rmtree() cannot be a symbolic link to a directory.
shutil.rmtree(dir_path) #except OSError, e: print ('Error: %s - %s.' % (e.filename, e.strerror))












'Modules_____________________________________________________________________________________'


# relative import
from .. import module
import ..module as m
#system paths
#append path (import sys)
#up one directory
'..'
#up two directory levels etc
'../..'
sys.path.append('..')  #add parent directory to python modules path.


# implicitly import a module 
#using imp (import imp)
eg. moduleVar = imp.load_source('file', 'fullpath/file.ext')
#
eg. max_customTools_main = imp.load_source('max_customTools_main', os.path.expandvars('%CLOUD%/____Graphics/3ds Max/Scripts/_Python/___Python_path/max_customTools_main.py'))


# importing a module. kw: import module
eg. moduleName.variable  #to access that variable`s functions and values


import package.a           #Absolute import
import package.a as a_mod  #Absolute import bound to different name
from package import a      #Alternate absolute import
import a                   #Implicit relative import (deprecated, python 2 only, generally avoid)
from . import a            #Explicit relative import


#single
eg. from module import method
eg. import method from module
eg. import module.method
eg. import module.method as var
#multiple
eg. from module import method1
eg. from module import (method1, method2, method3)
eg. from module import method1 as var1#, method2 as var2
#all
eg. from module import * #import all
eg. from module.classid import *




# from string
#using eval:
eval("from %s%s import QtCore, QtGui' % ('Python', 'Qt')")


#using importlib (import importlib)
#The first(name) argument specifies what module to import in absolute or relative terms (e.g. either pkg.mod or ..mod).
#If the name is specified in relative terms, then the package argument must be specified to the package which is to act as the anchor for resolving the package name (e.g. import_module('..mod', 'pkg.subpkg') will import pkg.mod).
eg. module = importlib.import_module(str(module), package=None) #the specified module will be inserted into sys.modules and returned.
eg. importlib.import_module(module, module[module.rfind('_')+1:])


#using __import__:
eg. module = __import__('module') #returns module
#
eg. module = __import__(module, globals(), locals(), [module[module.rfind('_')+1:]]) #ie. import tk_buttons_maya_init as init. use module[strip at char] to get module variable from module name
#using relative path
eg. module = __import__('path.to.module.Module', fromlist=[''])
#import all
eg. module = __import__(module, globals(), locals(), ['*'])



# pass arguments on import
eg. module.method(args)
	x = module.Class(range(1, 5))



#get module file name
eg. module = os.path.splitext(os.path.basename(__file__))[0]
#
eg. packageName = os.path.split(__file__)[1].split('.')[0] #Get the package name from the current python file base name
#using sys (import sys)
eg. __import__(sys.argv[1]) #sys.argv[0]
#using special variable
eg. module.__name__ #when run directly the name will be main. else when importing, it will be full name of the module
 


#re-import module
#using importlib (import importlib)
eg. importlib.reload(<module>)
#global and local are dicts.
eg.	module = 'tk_slots_maya_edit'
	if module not in locals() or module not in globals(): 
		__import__(module)
	else:
		reload(module)

#alt method re-importing all modules containing 'tk'
#untested; may return the imported module alias instead of the module name.
	for module in [m for m in sys.modules.keys() if 'tk' in m]:
		m = __import__(module); reload(m)




#delete system module: (sys.modules is a dict so it is also possible to check for key)
#using sys (import sys)
eg. del sys.modules['tk_slots_maya_edit']










'Packages___________________________________________________________________________________'


globals()['__package__'] = 'radial.ui.widgets'


# import module from a package
#using importlib (import importlib)
module = import_module(module_name, package='my_current_pkg') #__package__


#import all modules from a package
# using importlib (from importlib import import_module; import os)
__all__ = [
	import_module('.%s' % f, package=package) # import_module('.%s' % f, __package__)
	for f in [os.path.splitext(i)[0] for i in os.listdir(os.path.dirname(__file__)) if i.endswith('.py')]
	if f is not '__init__'
]



# location of python install
#command line:
python -c "from distutils.sysconfig import get_python_lib; print get_python_lib()"


# pip install
eg. python -m install pip
eg. python -m pip install --upgrade pip #windows env variable.
eg. C:/python -m pip install --upgrade pip #explicit dir
eg. python -m pip #install, uninstall, download, list, show, check, config, search, wheel, version, 
eg. C:/python38/Scripts/pip.exe install PySide2
# uninstall
eg. pip uninstall PySide2
# version, location, dependancies 
eg. pip show PySide2












'Encoding___________________________________________________________________________________'


#!/usr/bin/python3

#!/usr/bin/env python
# -*- coding: utf-8 -*-

#convert string from unicode to encoded text / bytes.
string.encode('utf-8')










'Time_______________________________________________________________________________________'

# pause, stop, wait, or sleep
#sleep
#using time (import time)
ex.
time.sleep(5) #wait for 5 seconds
time.sleep(.300) #wait for 300 milliseconds






# check speed
<code>
t1=time.time()
#using timeit (os agnostic)
t0=timeit.default_timer()
<code>
t1=timeit.default_timer()
print t1-t0
#alt:
% python -mtimeit  'function'








'Processes__________________________________________________________________________________'



#kill system process (import os, psutil)
pid = os.getpid()
parent = psutil.Process(pid)
for child in parent.children(recursive=True):
	child.kill()
parent.kill()









'Errors__(error handling)___________________________________________________________________'

# easier to ask forgiveness then ask permission
try:
	something
except:
	on error do this


# try # of times
eg.
complete=False
for num in range(3)
	while not complete:
		try:
			# something
			complete=True
		except Name.Error, e:
			attempts += 1

# hacky examples of a one liner try statement:
exec 'try: some_problematic_thing()\nexcept: problem=sys.exc_info()'
#or:
parse_float = lambda x, y=exec('def f(s):\n try:\n  return float(s)\n except:  return None'): f(x)



# supress error: (python 3)
from contextlib import suppress
with suppress(ValueError):
    a.remove('b')


# print to console
raise RuntimeError('')



# print error on exception:
eg.
except Exception as error:
	if not type(error)==AttributeError:
		raise error


#traceback module provides methods for formatting and printing exceptions and their tracebacks, 
#this would print exception like the default handler does:
eg.
import traceback
except: traceback.print_exc()




#Exceptions:
AttributeError: #attempting to access an attribute on an object that does not exist

KeyError:		#attempting to access a key in a dictionary that does not exist

TypeError:		#raised when an argument to a function is not the right type (e.g. a str instead of int)

ImportError:    #an import fails; python cannot find the module

IndexError:     #a list is indexed with an out-of-range number;

NameError:      #an unknown variable is used;

SyntaxError:    #the code cant be parsed properly;

TypeError:      #a function is called on a value of an inappropriate type; when an argument to a function is the right type but not in the right domain (e.g. an empty string)

ValueError:     #a function is called on a value of the correct type, but with an inappropriate value.

IOError:        #If the file cannot be opened. raised when Python cannot access a file correctly on disk

KeyboardInterrupt:#Raised when the user hits the interrupt key (normally Control-C or Delete)

EOFError:       #Raised when one of the built-in functions (input() or raw_input()) hits an
								#end-of-file condition (EOF) without reading any data




try:      #If an error is encountered, a try block code execution is stopped and transferred
except:   #down to the except block. without an exception error specified will catch all errors.
					eg. except ImportError run alternate block of code. you can use multiple exception blocks

finally:  #In addition to using an except block after the try block, you can also use the
					#finally block. code in the finally block will be executed regardless of whether an 
					#exception occurs.

raise()          eg. raise NameError('Unkown Variable')  #allows you to output an exception 
								 # error with an argument.
								 #in except blocks, the raise statement can be used without arguments to 
								 # re-raise whatever exception occured. eg. except: code block raise

assert()         #assert statement as true or false.  If true run code otherwise raise an 
								 # exception AssertionError.
								 #arguement is passed to the AssertionError output. 
								 eg. assert(1 > 2), 'Statement is False'




# debugging
# run script checking for indentation
python -tt script.py







# non descript errors/ typos----------

# Syntax Error: with wrong line number 
#parenthesis in wrong place or around entire code block
#expression in the above line is missing closing ')'





# Standard errors---------------------




# call needs a function or class. got undefined.
#method is out of scope or doesnt exist


# called-with-the-wrong-argument-type (string variable instead of object)
# Change:
button = 'self.ui.'+prefix+numString
# to
button = getattr(self.ui, prefix+numString)


# RuntimeError: '__init__' method of object's base class not called
#Adding super to the Interface class makes it work for me:
class Class(object):
	def __init__(self):
		super(Class, self).__init__()


# SystemError: error return without exception set



# Attribute Error:  object has no attribute '__getitem__'
#when attempting to apply the index operator [] on an int, not a list.


# Attribute Error:  object has no attribute
#specify the full path to the file.
import folder.file


# TypeError: unbound method xxxx() must be called with xxxx instance as first argument (got xxxx instance instead)
Class.method()
classInstance = Class()  # create instance of class
classInstance.method() # call classMethod


# TypeError: 'Method'() takes exactly 1 argument (self) (0 given) --
#instantiate an object of type ToolBar before calling a method of it
toolBar = hb_main.ToolBar()
toolBar.hbShow()
#or
ToolBar().hbShow()


# TypeError: 'Method' takes exactly 2 arguments (3 given)
#missing self from argument list if the method is part of a class. 
def classMethod(self, arg1, arg2):
#or (calling the class instance more than once):
self.ui.button.buttonId(self.ui,'m',10)
# should be:
self.ui.button.buttonId('m',10)


# ValueError: 'Attempted relative import in non-package'
#assure __init__.py in dir
from max.max_materials import selectByMaterialID #ex. import standalone function in max_materials module one level above current module from 'max' folder.
# single . if you want to import from folder in same directory . for each step back add one more.

# mod1.py
# some_dir/
#   mod2.py

# from .some_dir import mod2 #mod1.py
# from .. import mod1 #import mod1 from mod2.py


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

