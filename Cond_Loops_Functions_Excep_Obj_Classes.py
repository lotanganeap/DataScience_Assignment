#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Condition Equal

a = 5
a == 6


# In[2]:


# Greater than Sign

i = 6
i > 5


# In[3]:


# Greater than Sign

i = 2
i > 5


# In[4]:


# Inequality Sign

i = 2
i != 6


# In[5]:


# Inequality Sign

i = 6
i != 6


# In[6]:


# Use Equality sign to compare the strings

"ACDC" == "Michael Jackson"


# In[7]:


# Use Inequality sign to compare the strings

"ACDC" != "Michael Jackson"


# In[8]:


# Compare characters

'B' > 'A'


# In[9]:


# Compare characters

'BA' > 'AB'


# In[10]:


# If statement example

age = 19
#age = 18

#expression that can be true or false
if age > 18:
    
    #within an indent, we have the expression that is run if the condition is true
    print("you can enter" )

#The statements after the if statement will run regardless if the condition is true or false 
print("move on")


# In[11]:


# Else statement example

age = 18
# age = 19

if age > 18:
    print("you can enter" )
else:
    print("go see Meat Loaf" )
    
print("move on")


# In[12]:


# Elif statment example

age = 18

if age > 18:
    print("you can enter" )
elif age == 18:
    print("go see Pink Floyd")
else:
    print("go see Meat Loaf" )
    
print("move on")


# In[13]:


# Condition statement example

album_year = 1983
album_year = 1970

if album_year > 1980:
    print("Album year is greater than 1980")
    
print('do something..')


# In[14]:


# Condition statement example

album_year = 1983
#album_year = 1970

if album_year > 1980:
    print("Album year is greater than 1980")
else:
    print("less than 1980")

print('do something..')


# In[15]:


# Condition statement example

album_year = 1980

if(album_year > 1979) and (album_year < 1990):
    print ("Album year was in between 1980 and 1989")
    
print("")
print("Do Stuff..")


# In[16]:


# Condition statement example

album_year = 1980

if(album_year > 1979) and (album_year < 1990):
    print ("Album year was in between 1980 and 1989")
    
print("A")
print("Do Stuff..")


# In[17]:


# Condition statement example

album_year = 1990

if(album_year < 1980) or (album_year > 1989):
    print ("Album was not made in the 1980's")
else:
    print("The Album was made in the 1980's ")


# In[18]:


# Condition statement example

album_year = 1983

if not (album_year == 1984):
    print ("Album year is not 1984")


# In[19]:


Annie=1996
Jane=1999
if Annie%4==0:
    print("Annie was born in a leap year")
elif Jane%4==0:
    print("Jane was born in a leap year")
else:
    print("None of them were born in a leap year")


# In[26]:


Ashish=1991
Sonika=1996
if Ashish%4==0:
    print("Ashish was born in a leap year")
elif Sonika%4==0:
    print("Sonika was born in a leap year")
else:
    print("None of them were born in a leap year")


# In[27]:


age = 10
if age <=9:
    print ("You will get a bowl of porridge!")
elif age>=10 and age<=14:
    print ("You will get a sandwich!")
elif age>=15 and age<=17:
    print("You will get a burger!")


# In[28]:


1=2


# In[29]:


'a'=='A'


# In[30]:


for x in range(0,3):
     print(x)


# In[31]:


for i,x in enumerate(['A','B','C']):
    print(i,x)


# In[32]:


range(3)


# In[33]:


# For loop example

dates = [1982,1980,1973]
N = len(dates)

for i in range(N):
    print(dates[i])


# In[34]:


# Example of for loop

for i in range(0, 8):
    print(i)


# In[35]:


# Use for loop to change the elements in list

squares = ['red', 'yellow', 'green', 'purple', 'blue']

for i in range(0, 5):
    print("Before square ", i, 'is',  squares[i])
    squares[i] = 'white'
    print("After square ", i, 'is',  squares[i])


# In[36]:


# Loop through the list and iterate on both index and element value

squares=['red', 'yellow', 'green', 'purple', 'blue']

for i, square in enumerate(squares):
    print(i, square)


# In[37]:


count = 1
while count <= 5:
    print(count)
    count += 1


# In[38]:


# While Loop Example

dates = [1982, 1980, 1973, 2000]

i = 0
year = dates[0]

while(year != 1973):    
    print(year)
    i = i + 1
    year = dates[i]
    

print("It took ", i ,"repetitions to get out of loop.")


# In[39]:


rg = [-5,-4,-3,-2,-1,0,1,2,3,4,5]
N = len(rg)

for i in range(N):
    print(rg[i])


# In[40]:


for i in range(-4, 5):
    print(i)


# In[41]:


Genres=[ 'rock', 'R&B', 'Soundtrack', 'R&B', 'soul', 'pop']
for Genre in Genres:
    print(Genre)


# In[42]:


squares=['red', 'yellow', 'green', 'purple', 'blue']
for square in squares:
    print(square)


# In[43]:


PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]
i = 0
rating = PlayListRatings[0]
while(i < len(PlayListRatings) and rating >= 6):
    print(rating)
    i = i + 1 
    rating = PlayListRatings[i] 


# In[44]:


squares = ['orange', 'orange', 'purple', 'blue ', 'orange']
new_squares = []
i = 0
while(i < len(squares) and squares[i] == 'orange'):
    new_squares.append(squares[i])
    i = i + 1
print (new_squares)


# In[45]:


print("Multiplication table of 6:")
for i in range (10):
    print("6*",i,"=",6*i)
print("Multiplication table of 7:")
for i in range (10):
    print("7*",i,"=",7*i)


# In[46]:


Animals = ["lion", "giraffe", "gorilla", "parrots", "crocodile","deer", "swan"]
New = []
i=0
while i<len(Animals):
    j=Animals[i]
    if(len(j)==7):
        New.append(j)
    i=i+1
print(New)


# In[51]:


for x in range(0,3):
    print(x)


# In[52]:


L=[1,3,2]
sorted(L)
L


# In[53]:


L=[1,3,2]
sort(L)
L


# In[54]:


def Print(A):
    for a in A:
        print(a+'1')
        
Print(['a','b','c'])


# In[55]:


def add(a):
    """
    add 1 to a
    """
    b = a + 1
    print(a, "if you add one", b)
    return(b)


# In[56]:


add(7)


# In[57]:


help(add)


# In[58]:


def Mult(a, b):
    c = a * b
    return(c)
    print('This is not printed')
    
result = Mult(12,2)
print(result)


# In[59]:


x = 3
# Makes function call and return function a y
y = square(x)
y


# In[60]:


def square(a):
    
    # Local variable b
    b = 1
    c = a * a + b
    print(a, "if you square + 1", c) 
    return(c)


# In[61]:


x = 3
# Makes function call and return function a y
y = square(x)
y


# In[62]:


square(2)


# In[63]:


def MJ():
    print('Michael Jackson')
    
def MJ1():
    print('Michael Jackson')
    return(None)


# In[64]:


MJ()


# In[65]:


MJ1()


# In[66]:


MJ1(1)


# In[67]:


print(MJ())
print(MJ1())


# In[68]:


def con(a, b):
    return(a + b)


# In[69]:


con("This ", "is")


# In[70]:


# a and b calculation block1

a1 = 4
b1 = 5
c1 = a1 + b1 + 2 * a1 * b1 - 1
if(c1 < 0):
    c1 = 0 
else:
    c1 = 5
c1   


# In[71]:


# a and b calculation block2

a2 = 0
b2 = 0
c2 = a2 + b2 + 2 * a2 * b2 - 1
if(c2 < 0):
    c2 = 0 
else:
    c2 = 5
c2  


# In[72]:


# Make a Function for the calculation above

def Equation(a,b):
    c = a + b + 2 * a * b - 1
    if(c < 0):
        c = 0 
    else:
        c = 5
    return(c) 


# In[73]:


a1 = 4
b1 = 5
c1 = Equation(a1, b1)
c1


# In[74]:


a2 = 0
b2 = 0
c2 = Equation(a2, b2)
c2


# In[75]:


# Build-in function print()

album_ratings = [10.0, 8.5, 9.5, 7.0, 7.0, 9.5, 9.0, 9.5] 
print(album_ratings)


# In[76]:


sum(album_ratings)


# In[77]:


len(album_ratings)


# In[78]:


# Function example

def type_of_album(artist, album, year_released):
    
    print(artist, album, year_released)
    if year_released > 1980:
        return "Modern"
    else:
        return "Oldie"
    
x = type_of_album("Michael Jackson", "Thriller", 1980)
print(x)


# In[79]:


# Print the list using for loop

def PrintList(the_list):
    for element in the_list:
        print(element)


# In[80]:


PrintList(['1', 1, 'the man', "abc"])


# In[81]:


#Compare Two Strings Directly using in operator
# add string
string= "Michael Jackson is the best"

# Define a funtion
def check_string(text):
    
# Use if else statement and 'in' operatore to compare the string
    if text in string:
        return 'String matched'
    else:
        return 'String not matched'

check_string("Michael Jackson is the best")


# In[82]:


#Compare two strings using == operator and function
def compareStrings(x, y):
# Use if else statement to compare x and y
    if x==y:
        return 1
    
# Declare two different variables as string1 and string2 and pass string in it
string1 = "Michael Jackson is the best"
string2 = "Michael Jackson is the best"

# Declare a variable to store result after comparing both the strings
check = compareStrings(string1, string2)

#Use if else statement to compare the string
if check==1:
    print("\nString Matched")
else:
    print("\nString not Matched")


# In[83]:


# Python Program to Count words in a String using Dictionary
def freq(string):
    
    #step1: A list variable is declared and initialized to an empty list.
    words = []
    
    #step2: Break the string into list of words
    words = string.split() # or string.lower().split()
    
    #step3: Declare a dictionary
    Dict = {}
    
    #step4: Use for loop to iterate words and values to the dictionary
    for key in words:
        Dict[key] = words.count(key)
        
    #step5: Print the dictionary
    print("The Frequency of words is:",Dict)
    
#step6: Call function and pass string in it
freq("Mary had a little lamb Little lamb, little lamb Mary had a little lamb.Its fleece was white as snow And everywhere that Mary went Mary went, Mary went \
Everywhere that Mary went The lamb was sure to go")


# In[84]:


freq("Google")


# In[85]:


freq("o")


# In[88]:


# Python Program to Count words in a String using Dictionary
def freq(string):
    
    #step1: A list variable is declared and initialized to an empty list.
    words = []
    
    #step2: Break the string into list of words
    words = string.split() # or string.lower().split()
    
    #step3: Declare a dictionary
    Dict = {}
    
    #step4: Use for loop to iterate words and values to the dictionary
    for key in words:
        Dict[key] = words.count(key)
        
    #step5: Print the dictionary
    print("The Frequency of words is:",Dict)
    
#step6: Call function and pass string in it
freq("Google Google")


# In[87]:


string = "Google";
print("All the duplicate characters in the string are: "); 
# Counting every characters of the string 
for s in range(0, len(string)): 
   count = 1; 
   for t in range(s+1, len(string)):
      if(string[s] == string[t] and string[s] != ' '): 
         count = count + 1; 
# setting the string t to 0 to avoid printing the characters already taken 
   string = string[:t] + '0' + string[t+1:]; 
# If the count is greater than 1, the character is considered as duplicate 
   if(count > 1 and string[s] != '0'): 
      print(string[s]," - ",count);


# In[89]:


def finddup(string):
    print("All the duplicate characters in the string are: "); 
    # Counting every characters of the string 
    for s in range(0, len(string)): 
       count = 1; 
       for t in range(s+1, len(string)):
          if(string[s] == string[t] and string[s] != ' '): 
             count = count + 1; 
    # setting the string t to 0 to avoid printing the characters already taken 
       string = string[:t] + '0' + string[t+1:]; 
    # If the count is greater than 1, the character is considered as duplicate 
       if(count > 1 and string[s] != '0'): 
          print(string[s]," - ",count);


# In[90]:


finddup("Google")


# In[91]:


# Example for setting param with default value

def isGoodRating(rating=4): 
    if(rating < 7):
        print("this album sucks it's rating is",rating)
        
    else:
        print("this album is good its rating is",rating)


# In[92]:


isGoodRating()
isGoodRating(10)


# In[93]:


# Example of global variable

artist = "Michael Jackson"
def printer1(artist):
    internal_var1 = artist
    print(artist, "is an artist")
    
printer1(artist)
# try runningthe following code
#printer1(internal_var1) 


# In[94]:


artist = "Michael Jackson"

def printer(artist):
    global internal_var 
    internal_var= "Whitney Houston"
    print(artist,"is an artist")

printer(artist) 
printer(internal_var)


# In[95]:


# Example of global variable

myFavouriteBand = "AC/DC"

def getBandRating(bandname):
    if bandname == myFavouriteBand:
        return 10.0
    else:
        return 0.0

print("AC/DC's rating is:", getBandRating("AC/DC"))
print("Deep Purple's rating is:",getBandRating("Deep Purple"))
print("My favourite band is:", myFavouriteBand)


# In[98]:


# Deleting the variable "myFavouriteBand" from the previous example to demonstrate an example of a local variable 

del myFavouriteBand

# Example of local variable

def getBandRating(bandname):
    myFavouriteBand = "AC/DC"
    if bandname == myFavouriteBand:
        return 10.0
    else:
        return 0.0

print("AC/DC's rating is: ", getBandRating("AC/DC"))
print("Deep Purple's rating is: ", getBandRating("Deep Purple"))
print("My favourite band is", myFavouriteBand)


# In[99]:


# Example of global variable and local variable with the same name

myFavouriteBand = "AC/DC"

def getBandRating(bandname):
    myFavouriteBand = "Deep Purple"
    if bandname == myFavouriteBand:
        return 10.0
    else:
        return 0.0

print("AC/DC's rating is:",getBandRating("AC/DC"))
print("Deep Purple's rating is: ",getBandRating("Deep Purple"))
print("My favourite band is:",myFavouriteBand)


# In[100]:


def printAll(*args): # All the arguments are 'packed' into args which can be treated like a tuple
    print("No of arguments:", len(args)) 
    for argument in args:
        print(argument)
#printAll with 3 arguments
printAll('Horsefeather','Adonis','Bone')
#printAll with 4 arguments
printAll('Sidecar','Long Island','Mudslide','Carriage')


# In[101]:


def printDictionary(**args):
    for key in args:
        print(key + " : " + args[key])

printDictionary(Country='Canada',Province='Ontario',City='Toronto')


# In[102]:


def addItems(list):
    list.append("Three")
    list.append("Four")

myList = ["One","Two"]

addItems(myList)

myList


# In[103]:


def div(a, b):
    return(a/b)


# In[105]:


div(7,5)


# In[106]:


def con(a, b):
    return(a + b)
con(2, 2)
con(['a', 1], ['b', 1])


# In[107]:


con(2, 2)


# In[108]:


def freq(string,passedkey):

    #step1: A list variable is declared and initialized to an empty list.
    words = []

    #step2: Break the string into list of words
    words = string.split() # or string.lower().split()

    #step3: Declare a dictionary
    Dict = {}

    #step4: Use for loop to iterate words and values to the dictionary
    for key in words:
        if(key == passedkey):
            Dict[key] = words.count(key)   
    #step5: Print the dictionary
    print("Total Count:",Dict)

#step6: Call function and pass string in it
freq("Mary had a little lamb Little lamb, little lamb Mary had a little lamb.Its fleece was white as snow And everywhere that Mary went Mary went, Mary went \
Everywhere that Mary went The lamb was sure to go","little")


# In[109]:


1/0


# In[110]:


y = a + 5


# In[111]:


y


# In[112]:


a = [1, 2, 3]
a[10]


# In[113]:


a = 1

try:
    b = int(input("Please enter a number to divide a"))
    a = a/b
    print("Success a=",a)
except:
    print("There was an error")


# In[116]:


a = 1

try:
    b = int(input("Please enter a number to divide a"))
    a = a/b
    print("Success a=",a)
except ZeroDivisionError:
    print("The number you provided cant divide 1 because it is 0")
except ValueError:
    print("You did not provide a number")
except:
    print("Something went wrong")


# In[117]:


a = 1

try:
    b = int(input("Please enter a number to divide a"))
    a = a/b
except ZeroDivisionError:
    print("The number you provided cant divide 1 because it is 0")
except ValueError:
    print("You did not provide a number")
except:
    print("Something went wrong")
else:
    print("success a=",a)


# In[118]:


a = 1

try:
    b = int(input("Please enter a number to divide a"))
    a = a/b
except ZeroDivisionError:
    print("The number you provided cant divide 1 because it is 0")
except ValueError:
    print("You did not provide a number")
except:
    print("Something went wrong")
else:
    print("success a=",a)
finally:
    print("Processing Complete")


# In[119]:


# Import the library

import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[120]:


# Create a class Circle

class Circle(object):
    
    # Constructor
    def __init__(self, radius=3, color='blue'):
        self.radius = radius
        self.color = color 
    
    # Method
    def add_radius(self, r):
        self.radius = self.radius + r
        return(self.radius)
    
    # Method
    def drawCircle(self):
        plt.gca().add_patch(plt.Circle((0, 0), radius=self.radius, fc=self.color))
        plt.axis('scaled')
        plt.show()  


# In[121]:


RedCircle = Circle(10, 'red')


# In[122]:


dir(RedCircle)


# In[123]:


RedCircle.radius


# In[124]:


# Set the object attribute radius

RedCircle.radius = 1
RedCircle.radius


# In[126]:


# Call the method drawCircle
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
RedCircle.drawCircle()


# In[127]:


BlueCircle = Circle(radius=100)


# In[128]:


# Create a new Rectangle class for creating a rectangle object

class Rectangle(object):
    
    # Constructor
    def __init__(self, width=2, height=3, color='r'):
        self.height = height 
        self.width = width
        self.color = color
    
    # Method
    def drawRectangle(self):
        plt.gca().add_patch(plt.Rectangle((0, 0), self.width, self.height ,fc=self.color))
        plt.axis('scaled')
        plt.show()
        


# In[129]:


# Create a new object rectangle

SkinnyBlueRectangle = Rectangle(2, 3, 'blue')


# In[130]:


class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage


# In[131]:


class Vehicle:
    color = "white"

    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage


# In[132]:


class TextAnalyzer(object):
    
    def __init__ (self, text):
        # remove punctuation
        formattedText = text.replace('.','').replace('!','').replace('?','').replace(',','')
        
        # make text lowercase
        formattedText = formattedText.lower()
        
        self.fmtText = formattedText
        
    def freqAll(self):        
        # split text into words
        wordList = self.fmtText.split(' ')
        
        # Create dictionary
        freqMap = {}
        for word in set(wordList): # use set to remove duplicates in list
            freqMap[word] = wordList.count(word)
        
        return freqMap
    
    def freqOf(self,word):
        # get frequency map
        freqDict = self.freqAll()
        
        if word in freqDict:
            return freqDict[word]
        else:
            return 0


# In[133]:


analyzed = TextAnalyzer(givenstring)


# In[134]:


freqMap = analyzed.freqAll()
print(freqMap)


# In[135]:


word = "lorem"
frequency = analyzed.freqOf(word)
print(f"The word '{word}' appears {frequency} times.")


# In[136]:


x="Go"

if(x=="Go"):

  print('Go ')

else:

  print('Stop')

print('Mike')


# In[137]:


x=5
while(x!=2):
  print(x)
  x=x-1


# In[138]:


class Points(object):
  def __init__(self,x,y):

    self.x=x
    self.y=y

  def print_point(self):

    print('x=',self.x,' y=',self.y)

p1=Points("A","B")
p1.print_point()


# In[139]:


for i,x in enumerate(['A','B','C']):
    print(i+1,x)


# In[140]:


class Points(object):

  def __init__(self,x,y):

    self.x=x
    self.y=y

  def print_point(self):

    print('x=',self.x,' y=',self.y)

p2=Points(1,2)

p2.x='A'

p2.print_point()


# In[141]:


a=1

def do(x):
    a=100
    return(x+a)

print(do(1))


# In[ ]:




