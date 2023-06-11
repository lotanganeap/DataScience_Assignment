#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Use quotation marks for defining string

"Michael Jackson"


# In[2]:


# Use single quotation marks for defining string

'Michael Jackson'


# In[3]:


# Digitals and spaces in string

'1 2 3 4 5 6 '


# In[4]:


# Special characters in string

'@#2_#]&*^%$'


# In[5]:


# Print the string

print("hello!")


# In[6]:


# Assign string to variable

name = "Michael Jackson"
name


# In[7]:


# Print the first element in the string

print(name[0])


# In[8]:


# Print the element on index 6 in the string

print(name[6])


# In[9]:


# Print the element on the 13th index in the string

print(name[33])


# In[10]:


print(name[-1])


# In[11]:


print(name[-25])


# In[12]:


# Find the length of string

len("Michael Jackson")


# In[13]:


# Take the slice on variable name with only index 0 to index 3

name[0:4]


# In[14]:


# Take the slice on variable name with only index 8 to index 11

name[8:12]


# In[15]:


# Take the slice on variable name with only index 8 to index 11

name[8:12]


# In[16]:


# Get every second element in the range from index 0 to index 4

name[0:5:2]


# In[17]:


statement = name + "is the best"
statement


# In[18]:


name = "Michael Jackson"
name = name + " is the best"
name


# In[19]:


# New line escape sequence

print(" Michael Jackson \n is the best" )


# In[20]:


# New line escape sequence

print(" Michael Jackson \n \n is the best" )


# In[21]:


# Convert all the characters in string to upper case

a = "Thriller is the sixth studio album"
print("before upper:", a)
b = a.upper()
print("After upper:", b)


# In[22]:


# Convert all the characters in string to lower case
a = "MICHAEL JACKSON IS THE BEST"
print("Before lower:", a)
b = a.lower()
print("After lower:", b)


# In[23]:


a = "Michael Jackson is the best"
b = a.replace('Michael', 'Janet')
b


# In[24]:


# Replace the old substring with the new target substring by removing some punctuations.

a = "Hello! Michael Jackson has: 12 characters."
print(a)
b = a.replace('!','').replace(':','').replace('.','')
print(b)


# In[25]:


# Find the substring in the string. Only the index of the first elment of substring in string will be the output

name = "Michael Jackson"
name.find('el')


# In[26]:


# Find the substring in the string.

name.find('Jack')


# In[27]:


# If cannot find the substring in the string

name.find('Jasdfasdasdf')


# In[28]:


#Split the substring into list
name = "Michael Jackson"
split_string = (name.split())
split_string


# In[29]:


import re


# In[30]:


s1 = "Michael Jackson is the best"

# Define the pattern to search for
pattern = r"Jackson"

# Use the search() function to search for the pattern in the string
result = re.search(pattern, s1)

# Check if a match was found
if result:
    print("Match found!")
else:
    print("Match not found.")


# In[31]:


pattern = r"\d\d\d\d\d\d\d\d\d\d"  # Matches any ten consecutive digits
text = "My Phone number is 1234567890"
match = re.search(pattern, text)

if match:
    print("Phone number found:", match.group())
else:
    print("No match")


# In[32]:


pattern = r"\W"  # Matches any non-word character
text = "Hello, world!"
matches = re.findall(pattern, text)

print("Matches:", matches)


# In[33]:


s2 = "Michael Jackson was a singer and known as the 'King of Pop'"


# Use the findall() function to find all occurrences of the "as" in the string
result = re.findall("as", s2)

# Print out the list of matched words
print(result)


# In[34]:


# Use the split function to split the string by the "\s"
split_array = re.split("\s", s2)

# The split_array contains all the substrings, split by whitespace characters
print(split_array) 


# In[35]:


# Write your code below and press Shift+Enter to execute 

a = "1"


# In[36]:


a


# In[37]:


# Write your code below and press Shift+Enter to execute

b = "2"


# In[38]:


c = a + b


# In[39]:


c


# In[40]:


d = "ABCDEFG"


# In[41]:


print(d[:3]) 


# In[42]:


print(d[0:3])


# In[43]:


print("\\\\\\")


# In[44]:


f.upper()


# In[46]:


# Write your code below and press Shift+Enter to execute

f2 = "You are wrong"
f2.lower()


# In[49]:


#Write your code below and press Shift+Enter to execute

g = "Mary had a little lamb Little lamb, little lamb Mary had a little lamb \
Its fleece was white as snow And everywhere that Mary went Mary went, Mary went \
Everywhere that Mary went The lamb was sure to go"
g.find("snow")


# In[50]:


g.replace("Mary", "Bob")


# In[51]:


g.replace(',','.')


# In[52]:


g.split()


# In[54]:


# Use the search() function to search for the "\d" in the string
s3 = "House number- 1105"
result = re.search("\d", s3)

# Check if a match was found
if result:
    print("Digit found")
else:
    print("Digit not found.")


# In[56]:


# Use re.sub() to replace "fox" with "bear"
str1= "The quick brown fox jumps over the lazy dog."
new_str1 = re.sub(r"fox", "bear", str1)

print(new_str1)


# In[57]:


str2= "How much wood would a woodchuck chuck, if a woodchuck could chuck wood?"

# Write your code below and press Shift+Enter to execute
# Use re.findall() to find all occurrences of "woo"
matches = re.findall(r"woo", str2)

print(matches)


# In[58]:


"hello Mike".find("Mike") 


# In[59]:


A=(1,2,3,4,5)
A[1:4]


# In[ ]:




