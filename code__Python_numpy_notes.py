# numpy notes -----------------------------------------------------------------



# create a numpy array
npa = np.array(list_)
#n-dimentional array
npa = np.array([1, 2, 3, 4], ndmin=5) #define the number of dimensions by using the ndmin argument.
npa = np.array(listoflists) #create a two dimentional array
npa = np.array(listoflists, listoflists) #create a three dimentional array
# get the number of dimentions
npa.ndim #returns: int (number of dimentions)

# get row|columns of a n-dimentional array.
npa[<row>, <column>] #ie. npa[0, 0]
npa[0:2, 0:2] #row|column slice.
# get columns
npa[:, 3] #[of all rows : get column 3]
npa[:, 1:3] #[of all rows : get columns 1,2]
npa[:, [1,3,4]] #[of all rows : get columns [1, 3, 4]]
npa[2, 1:4] #[from row 2 : get columns 1-3]
npa[1:, 4] #[from row 1 on : get column 4]

# get number of rows|columns
npa.shape #returns: row, column
# get data type
npa.dtype #returns: datatype in the array


#add, subtract, multiply, or divide 1 dimentional arrays
np_array1 + np_array2 #add the contents of both lists
#add two columns
npa[:, 2] + npa[:, 3] #add columns 2 and 3


#numpy operators (works on multi-dimentional arrays)
#get min|max
npa.min()
npa.min(axis=0) #get min of columns
npa.max(axis=1) #get max of rows
#get average
npa.mean()
#get total
npa.sum()

#add, sub, multiply, divide, etc across the array
np.array([0, 1, 2]) + 10 #returns: [10, 11, 12]

#boolean operations
boolean_list = np.array([9, 11]) > 10 #returns: [False, True]
#filter an array for corresponding True indices in a boolean_list.
np.array([9, 11])[boolean_list] #returns: [11]
#filter for 2d array
np.array([9, 11], [12, 13])[boolean_list] #returns: [[12 13]]








# EXTERNAL FILES: -------------------------------------------------------------

from io import BytesIO #for handling byte strings (Python 2 and 3)
from io import StringIO #for handling unicode strings (Python 2 and 3)

# read file into an ndarray (an ndarray contains a single datatype)
ndarray = np.genfromtext('file', delimeter='', skip_header=1) #delimeter=char used to separate each value. skip_header=number of rows
#(StringIO() would be replaced by a filename.)(from StringIO import StringIO)
np.genfromtxt(<str, [str list], generator, or filename>, delimiter=None)
np.genfromtxt(StringIO(u"1, 2, 3\n4, 5, 6"), delimiter=",") #returns: [[ 1.,  2.,  3.],[ 4.,  5.,  6.]]
np.genfromtxt(StringIO(u"  1  2  3\n  4  5 67\n890123  4"), delimiter=3) #returns: [[   1.,    2.,    3.],[   4.,    5.,   67.], [ 890.,  123.,    4.]]
np.genfromtxt(StringIO(u"123456789\n   4  7 9\n   4567 9"), delimiter=(4, 3, 2)) #returns: [[ 1234.,   567.,    89.],[    4.,     7.,     9.],[    4.,   567.,     9.]]
