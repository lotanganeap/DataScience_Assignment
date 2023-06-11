#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("List")


# In[2]:


# Create your first tuple

tuple1 = ("disco",10,1.2 )
tuple1


# In[3]:


# Print the type of the tuple you created

type(tuple1)


# In[4]:


# Print the variable on each index

print(tuple1[0])
print(tuple1[1])
print(tuple1[2])


# In[5]:


# Print the type of value on each index

print(type(tuple1[0]))
print(type(tuple1[1]))
print(type(tuple1[2]))


# In[6]:


# Use negative index to get the value of the last element

tuple1[-1]


# In[7]:


# Concatenate two tuples

tuple2 = tuple1 + ("hard rock", 10)
tuple2


# In[8]:


# Slice from index 0 to index 2

tuple2[0:3]


# In[9]:


# Slice from index 3 to index 4

tuple2[3:5]


# In[10]:


# Get the length of tuple

len(tuple2)


# In[11]:


# A sample tuple

Ratings = (0, 9, 6, 5, 10, 8, 9, 6, 2)


# In[12]:


# Sort the tuple

RatingsSorted = sorted(Ratings)
RatingsSorted


# In[13]:


# Create a nest tuple

NestedT =(1, 2, ("pop", "rock") ,(3,4),("disco",(1,2)))


# In[14]:


# Print element on each index

print("Element 0 of Tuple: ", NestedT[0])
print("Element 1 of Tuple: ", NestedT[1])
print("Element 2 of Tuple: ", NestedT[2])
print("Element 3 of Tuple: ", NestedT[3])
print("Element 4 of Tuple: ", NestedT[4])


# In[15]:


# Print element on each index, including nest indexes

print("Element 2, 0 of Tuple: ",   NestedT[2][0])
print("Element 2, 1 of Tuple: ",   NestedT[2][1])
print("Element 3, 0 of Tuple: ",   NestedT[3][0])
print("Element 3, 1 of Tuple: ",   NestedT[3][1])
print("Element 4, 0 of Tuple: ",   NestedT[4][0])
print("Element 4, 1 of Tuple: ",   NestedT[4][1])


# In[16]:


NestedT[2][1][0]


# In[17]:


NestedT[2][1][1]


# In[18]:


NestedT[4][1][0][0]


# In[19]:


NestedT[4][1][0]


# In[20]:


# sample tuple

genres_tuple = ("pop", "rock", "soul", "hard rock", "soft rock", \
                "R&B", "progressive rock", "disco") 
genres_tuple


# In[21]:


len(genres_tuple)


# In[22]:


1,2,3]+[1,1,1]


# In[23]:


[1,2,3]+[1,1,1]


# In[24]:


[1].append([2,3,4,5])


# In[25]:


len([1].append([2,3,4,5]))


# In[26]:


A=[1]
A.append([2,3,4,5])
len(A)


# In[27]:


print(A)


# In[28]:


# Create the dictionary

Dict = {"key1": 1, "key2": "2", "key3": [3, 3, 3], "key4": (4, 4, 4), ('key5'): 5, (0, 1): 6}
Dict


# In[29]:


# Access to the value by the key

Dict["key1"]


# In[30]:


# Access to the value by the key

Dict[(0, 1)]


# In[31]:


# Create a sample dictionary

release_year_dict = {"Thriller": "1982", "Back in Black": "1980", \
                    "The Dark Side of the Moon": "1973", "The Bodyguard": "1992", \
                    "Bat Out of Hell": "1977", "Their Greatest Hits (1971-1975)": "1976", \
                    "Saturday Night Fever": "1977", "Rumours": "1977"}
release_year_dict


# In[32]:


# Get value by keys

release_year_dict['Thriller'] 


# In[33]:


# Get value by key

release_year_dict['The Bodyguard'] 


# In[34]:


# Get value by key

release_year_dict['The Bodyguad'] 


# In[35]:


# Get all the keys in dictionary

release_year_dict.keys() 


# In[36]:


# Get all the keys in dictionary

release_year_dict.keys(1) 


# In[37]:


# Get all the values in dictionary

release_year_dict.values() 


# In[38]:


# Append value with key into dictionary

release_year_dict['Graduation'] = '2007'
release_year_dict


# In[39]:


# Delete entries by key

del(release_year_dict['Thriller'])
del(release_year_dict['Graduation'])
release_year_dict


# In[40]:


# Question sample dictionary

soundtrack_dic = {"The Bodyguard":"1992", "Saturday Night Fever":"1977"}
soundtrack_dic 


# In[41]:


soundtrack_dic.key()


# In[42]:


soundtrack_dic.keys()


# In[43]:


soundtrack_dic.values()


# In[44]:


# Create the dictionary

Dict1 = {"Back in Black": 50, "The Bodygaurd": 50, "Thriller": 65}
Dict1


# In[45]:


# Create the dictionary

album_sales_dict = {"Back in Black": 50, "The Bodygaurd": 50, "Thriller": 65}
album_sales_dict


# In[46]:


album_sales_dict.values("Thriller")


# In[47]:


album_sales_dict["Thriller"]


# In[48]:


inventory ={}


# In[49]:


ProductNo1 = "Mobile Phone"
ProductNo1_quantity = 5
ProductNo1_price = 20000
ProductNo1_releaseYear= 2020


# In[50]:


inventory["ProductNo1"]= ProductNo1
inventory["ProductNo1_quantity"]= ProductNo1_quantity
inventory["ProductNo1_price"]= ProductNo1_price
inventory["ProductNo1_releaseYear"]=ProductNo1_releaseYear


# In[51]:


inventory


# In[52]:


"ProductNo1_releaseYear" in inventory
"ProductNo2_releaseYear" in inventory


# In[53]:


del(inventory["ProductNo1_releaseYear"])
del(inventory["ProductNo2_releaseYear"])


# In[54]:


inventory


# In[55]:


# Create a set

set1 = {"pop", "rock", "soul", "hard rock", "rock", "R&B", "rock", "disco"}
set1


# In[56]:


# Convert list to set

album_list = [ "Michael Jackson", "Thriller", 1982, "00:42:19", \
              "Pop, Rock, R&B", 46.0, 65, "30-Nov-82", None, 10.0]
album_set = set(album_list)             
album_set


# In[57]:


music_genres = set(["pop", "pop", "rock", "folk rock", "hard rock", "soul", \
                    "progressive rock", "soft rock", "R&B", "disco"])
music_genres


# In[58]:


A = set(["Thriller", "Back in Black", "AC/DC"])
A


# In[59]:


A.add("NSYNC")
A


# In[60]:


# Sample Sets

album_set1 = set(["Thriller", 'AC/DC', 'Back in Black'])
album_set2 = set([ "AC/DC", "Back in Black", "The Dark Side of the Moon"])


# In[61]:


album_set1 & album_set2


# In[62]:


album_set1.difference(album_set2)  


# In[63]:


album_set2.difference(album_set1)  


# In[64]:


# Use intersection method to find the intersection of album_list1 and album_list2

album_set1.intersection(album_set2)   


# In[65]:


# Find the union of two sets

album_set1.union(album_set2)


# In[66]:


# Check if superset

set(album_set1).issuperset(album_set2)   


# In[67]:


# Check if subset

set(album_set2).issubset(album_set1)     


# In[68]:


# Check if subset

set({"Back in Black", "AC/DC"}).issubset(album_set1) 


# In[69]:


# Check if superset

album_set1.issuperset({"Back in Black", "AC/DC"})   


# In[70]:


A = [1, 2, 2, 1]  
B = set([1, 2, 2, 1])
print("the sum of A is:", sum(A))
print("the sum of B is:", sum(B))


# In[71]:


# Write your code below and press Shift+Enter to execute

album_set1 = set(["Thriller", 'AC/DC', 'Back in Black'])
album_set2 = set([ "AC/DC", "Back in Black", "The Dark Side of the Moon"])
album_set3 = album_set1.union(album_set2)
album_set3


# In[72]:


album_set1.issubset(album_set3)


# In[73]:


A=((1),[2,3],[4])
a[2]


# In[74]:


A=((1),[2,3],[4])
A[2]


# In[75]:


A[2][0]


# In[76]:


V={'A','B'}
V.add('C')


# In[77]:


V


# In[ ]:




