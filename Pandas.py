#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas 


# In[2]:


2+3


# In[3]:





# In[4]:


#Define a dictionary 'x'
import pandas as pd
x = {'Name': ['Rose','John', 'Jane', 'Mary'], 'ID': [1, 2, 3, 4], 'Department': ['Architect Group', 'Software Group', 'Design Team', 'Infrastructure'], 
      'Salary':[100000, 80000, 50000, 60000]}

#casting the dictionary to a DataFrame
df = pd.DataFrame(x)

#display the result df
df


# In[5]:


#Retrieving the "ID" column and assigning it to a variable x
x = df[['ID']]
x


# In[6]:


type(x)


# In[7]:


#Retrieving the Department, Salary and ID columns and assigning it to a variable z

z = df[['Department','Salary','ID']]
z


# In[8]:


a = {'Student':['David', 'Samuel', 'Terry', 'Evan'],
     'Age':['27', '24', '22', '32'],
     'Country':['UK', 'Canada', 'China', 'USA'],
     'Course':['Python','Data Structures','Machine Learning','Web Development'],
     'Marks':['85','72','89','76']}
df1 = pd.DataFrame(a)
df1


# In[9]:


b = df1[['Marks']]
b


# In[10]:


# Access the value on the first row and the first column

df.iloc[0, 0]


# In[11]:


df.iloc[0,2]


# In[12]:


# Access the column using the name

df.loc[0, 'Salary']


# In[13]:


df2=df
df2=df2.set_index("Name")


# In[14]:


df2


# In[15]:


# Dependency needed to install file 

get_ipython().system('pip install xlrd')
get_ipython().system('pip install openpyxl')


# In[16]:


# Import required library

import pandas as pd
# Read data from CSV file

csv_path = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/TopSellingAlbums.csv'
df = pd.read_csv(csv_path)


# In[17]:


df


# In[18]:


# Print first five rows of the dataframe

df.head()


# In[19]:


# Read data from Excel File and print the first five rows

xlsx_path = 'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%204/Datasets/TopSellingAlbums.xlsx'

df = pd.read_excel(xlsx_path)
df.head()


# In[20]:


pip install openpyxl


# In[21]:


# Read data from Excel File and print the first five rows

xlsx_path = 'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%204/Datasets/TopSellingAlbums.xlsx'

df = pd.read_excel(xlsx_path)
df.head()


# In[22]:


# Read data from Excel File and print the first five rows

xlsx_path = 'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%204/Datasets/TopSellingAlbums.xlsx'

df = pd.read_excel(xlsx_path)
df.head()


# In[23]:


# Access to the column Length

x = df[['Length']]
x


# In[24]:


# Get the column as a series

x = df['Length']
x


# In[25]:


# Access to multiple columns

y = df[['Artist','Length','Genre']]
y


# In[26]:


# Access the value on the first row and the first column

df.iloc[0, 0]


# In[27]:


# Slicing the dataframe

df.iloc[0:2, 0:3]


# In[29]:


new_index=['a','b','c','d','e','f','g','h']
df_new=df
df_new.index=new_index
df_new.loc['a', 'Artist']
df_new.loc['a':'d', 'Artist']


# In[31]:


import numpy as np
b=np.array([1,-2,3,4,5])
max_b=b.max()


# In[32]:


max_b


# In[33]:


pip install matplotlib 


# In[34]:


# Create a python list

a = ["0", 1, "two", "3", 4]
# Print each element

print("a[0]:", a[0])
print("a[1]:", a[1])
print("a[2]:", a[2])
print("a[3]:", a[3])
print("a[4]:", a[4])


# In[35]:


# import numpy library

import numpy as np 
# Create a numpy array

a = np.array([0, 1, 2, 3, 4])
a


# In[36]:


# Print each element

print("a[0]:", a[0])
print("a[1]:", a[1])
print("a[2]:", a[2])
print("a[3]:", a[3])
print("a[4]:", a[4])


# In[37]:


print(np.__version__)


# In[38]:


type(a)


# In[39]:


# Check the type of the values stored in numpy array

a.dtype


# In[40]:


b = np.array([3.1, 11.02, 6.2, 213.2, 5.2])

# Enter your code here
type(b)
    
b.dtype 


# In[41]:


# Create numpy array

c = np.array([20, 1, 2, 3, 4])
c


# In[42]:


# Assign the first element to 100

c[0] = 100
c


# In[43]:


c[4] = 0
c


# In[44]:


a = np.array([10, 2, 30, 40,50])

# Enter your code here
a[1]=20
a


# In[45]:


# Slicing the numpy array

d = c[1:4]
d


# In[46]:


# Set the fourth element and fifth element to 300 and 400

c[3:5] = 300, 400
c


# In[47]:


arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5:2])


# In[50]:


# Create a numpy array

a = np.array([0, 1, 2, 3, 4])
a
a.size


# In[51]:


a.ndim


# In[52]:


a.shape


# In[53]:


# Create a numpy array

a = np.array([1, -1, 1, -1])
# Get the mean of numpy array

mean = a.mean()
mean


# In[54]:


# Get the standard deviation of numpy array

standard_deviation=a.std()
standard_deviation


# In[55]:


u = np.array([1, 0])
u
v = np.array([0, 1])
v


# In[56]:


z = np.add(u, v)
z


# In[57]:


import time 
import sys
import numpy as np 

import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

def Plotvec1(u, z, v):
    
    ax = plt.axes() # to generate the full window axes
    ax.arrow(0, 0, *u, head_width=0.05, color='r', head_length=0.1)# Add an arrow to the  U Axes with arrow head width 0.05, color red and arrow head length 0.1
    plt.text(*(u + 0.1), 'u')#Adds the text u to the Axes 
    
    ax.arrow(0, 0, *v, head_width=0.05, color='b', head_length=0.1)# Add an arrow to the  v Axes with arrow head width 0.05, color red and arrow head length 0.1
    plt.text(*(v + 0.1), 'v')#Adds the text v to the Axes 
    
    ax.arrow(0, 0, *z, head_width=0.05, head_length=0.1)
    plt.text(*(z + 0.1), 'z')#Adds the text z to the Axes 
    plt.ylim(-2, 2)#set the ylim to bottom(-2), top(2)
    plt.xlim(-2, 2)#set the xlim to left(-2), right(2)


# In[58]:


# Plot numpy arrays

Plotvec1(u, z, v)


# In[59]:


arr1 = np.array([10, 11, 12, 13, 14, 15])
arr2 = np.array([20, 21, 22, 23, 24, 25])
arr3 = np.add(arr1, arr2)
arr3


# In[61]:


a = np.array([10, 20, 30])
a
b = np.array([5, 10, 15])
b


# In[62]:


c = np.subtract(a, b)

print(c)


# In[63]:


arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([2, 1, 2, 3, 4, 5])
arr3 = np.multiply(arr1, arr2)
arr3


# In[64]:


X = np.array([1, 2])
Y = np.array([3, 2])
# Calculate the dot product

np.dot(X, Y)


# In[65]:


#Elements of X
print(X[0])
print(X[1])


# In[66]:


#Elements of Y
print(Y[0])
print(Y[1])


# In[67]:


np.pi


# In[68]:


# Create the numpy array in radians

x = np.array([0, np.pi/2 , np.pi])


# In[69]:


x


# In[70]:


# Makeup a numpy array within [-2, 2] and 5 elements

np.linspace(-2, 2, num=5)


# In[71]:


# Make a numpy array within [-2, 2] and 9 elements

np.linspace(-2, 2, num=9)


# In[72]:


# Make a numpy array within [0, 2π] and 100 elements 

x = np.linspace(0, 2*np.pi, num=100)


# In[73]:


x


# In[74]:


# Calculate the sine of x list

y = np.sin(x)


# In[75]:


y


# In[76]:


# Plot the result

plt.plot(x, y)


# In[77]:


# Write your code below and press Shift+Enter to execute

u = np.array([1, 0])
v = np.array([0, 1])


# In[78]:


u-v


# In[79]:


# Import the libraries

import time 
import sys
import numpy as np 

import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

def Plotvec2(a,b):
    ax = plt.axes()# to generate the full window axes
    ax.arrow(0, 0, *a, head_width=0.05, color ='r', head_length=0.1)#Add an arrow to the  a Axes with arrow head width 0.05, color red and arrow head length 0.1
    plt.text(*(a + 0.1), 'a')
    ax.arrow(0, 0, *b, head_width=0.05, color ='b', head_length=0.1)#Add an arrow to the  b Axes with arrow head width 0.05, color blue and arrow head length 0.1
    plt.text(*(b + 0.1), 'b')
    plt.ylim(-2, 2)#set the ylim to bottom(-2), top(2)
    plt.xlim(-2, 2)#set the xlim to left(-2), right(2)


# In[80]:


a = np.array([-1, 1])
b = np.array([1, 1])
Plotvec2(a, b)
print("The dot product is", np.dot(a,b))


# In[81]:


a = np.array([1, 0])
b = np.array([0, 1])
Plotvec2(a, b)
print("The dot product is", np.dot(a, b))


# In[82]:


a = np.array([1, 1])
b = np.array([0, 1])
Plotvec2(a, b)
print("The dot product is", np.dot(a, b))


# In[83]:


arr1 = np.array([1, 2, 3])
arr2 = np.array([8, 9, 10])

arr3 = np.add(arr1, arr2)
arr3

arr4 = np.subtract(arr1, arr2)
arr4

arr5 = np.multiply(arr1, arr2)
arr5


arr6 = np.divide(arr1, arr2)
arr6

arr7 = np.dot(arr1, arr2)
arr7


# In[84]:


Y=np.array([[2,1],[1,2]])
Z=2*Y
Z


# In[85]:


# Import the libraries

import numpy as np 
import matplotlib.pyplot as plt
# Create a list

a = [[11, 12, 13], [21, 22, 23], [31, 32, 33]]
a


# In[86]:


# Convert list to Numpy Array
# Every element is the same type

A = np.array(a)
A


# In[87]:


# Show the numpy array dimensions

A.ndim


# In[88]:


A.shape


# In[89]:


A.size


# In[90]:


# Access the element on the second row and third column

A[1, 2]


# In[91]:


# Access the element on the first row and first and second columns

A[0][0:2]


# In[92]:


# Access the element on the first and second rows and third column

A[0:2, 2]


# In[93]:


# Create a numpy array X

X = np.array([[1, 0], [0, 1]]) 
X


# In[94]:


# Create a numpy array Y

Y = np.array([[2, 1], [1, 2]]) 
Y


# In[95]:


# Add X and Y

Z = X + Y
Z


# In[96]:


# Create a numpy array Y

Y = np.array([[2, 1], [1, 2]]) 
Y


# In[97]:


# Create a numpy array Y

Y = np.array([[2, 1], [1, 2]]) 
Y


# In[98]:


# Create a numpy array X

X = np.array([[1, 0], [0, 1]]) 
X


# In[99]:


# Multiply X with Y

Z = X * Y
Z


# In[100]:


# Create a matrix A

A = np.array([[0, 1, 1], [1, 0, 1]])
A


# In[101]:


# Create a matrix B

B = np.array([[1, 1], [1, 1], [-1, 1]])
B


# In[102]:


# Calculate the dot product

Z = np.dot(A,B)
Z


# In[103]:


# Calculate the sine of Z

np.sin(Z)


# In[104]:


a=np.array([-1,1])
b=np.array([1,1])
np.dot(a,b) 


# In[105]:


X=np.array([[1,0,1],[2,2,2]]) 
out=X[0,1:3]
out


# In[106]:


X=np.array([[1,0],[0,1]])
Y=np.array([[2,1],[1,2]]) 
Z=np.dot(X,Y)


# In[107]:


Z


# In[108]:


with open("Example3.txt","w") as file1:
  
file1.write("This is line C\n")


# In[ ]:




