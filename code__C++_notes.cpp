// C++ notes




// A C# program consists of the following parts:

// Namespace declaration
A class;
Class methods;
Class attributes;
A Main method;
Statements and Expressions;
Comments;


// header: //namespace declaration

// library:
#include 
<iostream>  
<string>  //allows inputting strings with whitespaces
<sstream> //allows a string to be treaded as a stream, allowing extraction or insertion operations.

using namespace std;

int main() //function with return type integer
//body
return 0; //if not specified, function will implicitly return 0    


// comments:
// single line
/* multiple
line */



// line terminators:
\n        //new line  cout<< "\nprintThis"
\t        //new tab
endl      //end line



// input output:
//print
cout      ex. cout << "print this"; //iostream defined object
//user input
cin       ex. cin >> variable; //iostream defined object




'Variables__________________________________________________________________________________'

// naming convention:
pascal case   (ex. PascalCase)
camel case    (ex. camelCase)
//letters, numbers, underscore. cannot begin with a number.  best practice to not begin with an underscore.



integers:
int       //integer

floating point:
float     //can hold + or - fractional 38 digit values. always signed (hold both negative & positive values)
double    //can hold + or - fractional 308 digit values.    
long double//can hold + or - fractional 308 digit values. 



character:
char      (ex. char variable = 'x') //stores 128 ASCII character values

void      //represents the absence of type

modifiers:
signed    //default. can hold - & + values. modifies int values.
unsigned  //only stores positive values. modifies int
short     //-32,768 to 32,768. half default size.  modifies int.
long      //-2,147,483,648 to 2,147,483,647. twice default size. modifies int & double.



pointers & memory:
//a pointer is a variable, with the address of another variable as its value.
int *x //pointer to an integer. the asterisk can be placed anywhere in between
double *x //ponter to a double
float *x //pointer to a float
char *x //pointer to a character

(ex. int score = 5;
      int *scorePtr;
      scorePtr = &score;
      
      cout<< scorePtr << endl;
      //outputs "0x29fee8"
      )

pointer operators:
&    //address of  (ampersand)   (ex. &score) //outputs memory address for the score variable.
*    //contents of (dereference) (ex. *score) //returns value of the variable located at the address specified by its operand.
     (ex. int var = 50; int *p; p= & var;
            cout<< var << endl; //outputs 50. (the value of var)
            cout<< p << endl;   //outputs 0x29fee8. (vars memory location)
            cout<< *p << endl;  //outputs 50. ( the value of the variable stored in the pointer p)

memory:
static    //stack memory. local variables stored. manages deletion itself.
dynamic   //heap memory.  unused memory for the program to dynamically allocate

new int;  //allocates memory for an int variable. 
          (ex. int *p = new int;)

delete pointer;  //releases heap memory pointed to by pointer. 
          (ex. int *p = new int; //request memory
               *p = 5; //store value
               cout << *p << endl; //use value
               delete p; //free up the memory. does not delete pointer itself (pointer stored in stack not heap). no dereference (asterisk) needed.)
               //p is now a dangling pointer (points to non-existant memory location)
               p = new int;  //re-use for a new address 

delete[]  //dynamic memory with arrays
          (ex. int *p = NULL; //Pointer initialized with NULL
               p = new int[20];  //request memory
               delete[] p; //delete array pointed to by p)

NULL      //a NULL pointer is a constant with a value of zero. It's good practice to assign NULL to a pointer variable when you declare it.
          (ex. int *p = NULL;)

sizeof    //used to get a variable or data type's size in bytes (varies from machine)
          (ex. sizeof(char); sizeof(int); sizeof(float); sizeof(double); variable = 50; sizeof(variable);)
          //also used in arrays
          (ex. double myArr[10];   //double is 8 bytes (varies)
               cout << sizeof(myArr) << endl;) //outputs 80.  Array stored 10 doubles, so the entire array occupies 80 bytes in memory.








'Mathmatical Operators______________________________________________________________________'
order of operation:
(parenthases)
/ * %
+ -

%         /*remainder*/ (ex. 5 % 2 outputs 1)  

+=        (ex. x += 5 is equivalent to x = x + 5)
-=        (ex. x -= 5 "              " x = x - 5)
*=        (ex. x *= 5 "              " x = x * 5) 
/=        (ex. x /= 5 "              " x = x / 5)
%=        (ex. x %= 5 "              " x = x % 5)




incriment:
++X       //prefix.  incriments by 1 then evaluates the expression (ex. x = x + 1)
X++       //postfix. evaluates expression then incriments by 1 (ex. x = x + 1)

prefix ex:   x = 5;                   postfix ex.   x = 5;
             y = ++x;                               y = x++; 
             //x is 6, y is 6                       //x is 6, y is 5

decriment:
-x        //prefix.  decriments by 1 then evaluates the expression (ex. x = x - 1)
x-        //postfix. evaluates expression then decriments by 1 (ex. x = x + 1)








'Comparators________________________________________________________________________________'

conditionals:
if        (ex.  if (x<y) {cout << "x is less than y";}
else      (ex.  if (x<y) {cout << "x is less than y";} else {cout << "x is greater than y";}
else if    //you can use multiple else if statements

loop:
while     //repeatedly executes a set of statements until the condition is satisfied. (ex. while (x<y) {do this;})
for       (ex. for (init; condition; increment){//some code}  init step is executed once , increment updates the loop control variable.  (ex.  for (int x=1; x<10; x++) {//some code})
do while  (ex. int a=0; do{ cout<< a<< endl; a++} while(a<5); //executes the statements at least once, and then tests the condition.

switch    (ex. int age=25; switch (age){case 16: cout<< "too young"; break; default: cout<< "default case"}) 
          case      //in case of
          break     //terminates the switch statement     
          default   //must appear at the end of a switch




logical operators:
&&        and     (ex. y&&y)   
||        or      (ex. x||y)
!         not     (ex. !x)(ex. !(x>6))

relational operators:
>=        //greater than or equal to
<=        //less than or equal to
==        //equal to
!=        //not equal to



#ifdef    //(if defined) - test if a preprocessor variable has been "defined".
#ifndef   //(if not defined)
#endif    //





'Boolean Operations_________________________________________________________________________'

booleans:
bool      (ex. bool x = false; bool y = true;) //holds true or false value









'Conditionals_______________________________________________________________________________'





'Looping___________________________________________________________________________________'





'Strings____________________________________________________________________________________'

// strings:
// ""        /*string*/ (ex. "this is a typical string")
// """"      /*string literal*/ (ex. "this is a", "string literal")
// ''        /*legal character. 1 bit integer. (not a string)*/(ex. 'x')
// string    (ex. string myVariable;  getline (cin, myVariable);))










'Lists__(arrays)____________________________________________________________________________'

(ex. int x[5]; = {11, 45, 62, 70, 88}; cout<< 0\n <<cout 4;)

multi-dimentional arrays:
(ex. int x[3][4];  [column][row]
(ex. int x[2][3] = {
     {2,3,4},  //first row
     {8,9,10}  //second row
};
cout<< x[0][2] <<endl; //outputs 4









'Sets_______________________________________________________________________________________'







'Tuples___unmodifiable lists________________________________________________________________'






'Dictionary__(aka_hashtable,map_/_associative_array)___used_to_bind_keys_to_values__________'






'Functions_(subroutines)____________________________________________________________________'

functions:
ex. return-type function name(parameter list)
{
     body of function
}

return-type  //data type of value returned by function
function name //name of the function
parameters //when a function is invoked, you pass a value to the parapeter. parameter list refers to the type, order, and number of the parameters of a function. parameters are optional.
body of the function //collection of statements defining what the function does.










'Lambda_Expressions_(anonymous_function)____________________________________________________'







'Generators_(coroutines)____________________________________________________________________'






'Decorators_________________________________________________________________________________'







'Recursion__________________________________________________________________________________'





'Classes____________________________________________________________________________________'







'Class_Inheritance__________________________________________________________________________'








'classmethod_&_staticmethod_________________________________________________________________'






'property___________________________________________________________________________________'






'Magic Methods_(dunder_methods)_____________________________________________________________'






'rich operators:____________________________________________________________________________'






'User_Input_________________________________________________________________________________'





'Keyboard___________________________________________________________________________________'





'External_Files_&_Modules___________________________________________________________________'





'Time_______________________________________________________________________________________'




'Check_Speed________________________________________________________________________________'





'Errors__(error handling)___________________________________________________________________'






































     	  