#!/usr/bin/env python
# coding: utf-8

# In[1]:


def one_dict(list_dict):
    keys=list_dict[0].keys()
    out_dict={key:[] for key in keys}
    for dict_ in list_dict:
        for key, value in dict_.items():
            out_dict[key].append(value)
    return out_dict    


# In[2]:


import pandas as pd
import matplotlib.pyplot as plt


# In[3]:


dict_={'a':[11,21,31],'b':[12,22,32]}


# In[4]:


df=pd.DataFrame(dict_)
type(df)


# In[5]:


df.head()


# In[6]:


df.mean()


# In[7]:


pip install nba_api


# In[8]:


from nba_api.stats.static import teams
import matplotlib.pyplot as plt


# In[9]:


nba_teams = teams.get_teams()


# In[10]:


nba_teams[0:3]


# In[11]:


dict_nba_team=one_dict(nba_teams)
df_teams=pd.DataFrame(dict_nba_team)
df_teams.head()


# In[12]:


df_warriors=df_teams[df_teams['nickname']=='Warriors']
df_warriors


# In[13]:


id_warriors=df_warriors[['id']].values[0][0]
# we now have an integer that can be used to request the Warriors information 
id_warriors


# In[14]:


from nba_api.stats.endpoints import leaguegamefinder


# In[15]:


# Since https://stats.nba.com does not allow api calls from Cloud IPs and Skills Network Labs uses a Cloud IP.
# The following code is commented out, you can run it on jupyter labs on your own computer.
# gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable=id_warriors)
# Since https://stats.nba.com does not allow api calls from Cloud IPs and Skills Network Labs uses a Cloud IP.
# The following code is commented out, you can run it on jupyter labs on your own computer.
# gamefinder.get_json()
# Since https://stats.nba.com does not allow api calls from Cloud IPs and Skills Network Labs uses a Cloud IP.
# The following code is comment out, you can run it on jupyter labs on your own computer.
# games = gamefinder.get_data_frames()[0]
# games.head()


# In[16]:


import requests

filename = "https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%205/Labs/Golden_State.pkl"

def download(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, "wb") as f:
            f.write(response.content)

download(filename, "Golden_State.pkl")


# In[17]:


file_name = "Golden_State.pkl"
games = pd.read_pickle(file_name)
games.head()


# In[18]:


games_home=games [games ['MATCHUP']=='GSW vs. TOR']
games_away=games [games ['MATCHUP']=='GSW @ TOR']


# In[19]:


games_home.mean()['PLUS_MINUS']


# In[20]:


games_away.mean()['PLUS_MINUS']


# In[21]:


fig, ax = plt.subplots()

games_away.plot(x='GAME_DATE',y='PLUS_MINUS', ax=ax)
games_home.plot(x='GAME_DATE',y='PLUS_MINUS', ax=ax)
ax.legend(["away", "home"])
plt.show()


# In[22]:


import requests


# In[23]:


import os 
from PIL import Image
from IPython.display import IFrame


# In[24]:


url='https://www.ibm.com/'
r=requests.get(url)


# In[25]:


r


# In[26]:


r.status_code


# In[27]:


print(r.request.headers)


# In[28]:


print("request body:", r.request.body)


# In[29]:


header=r.headers
print(r.headers)


# In[30]:


header['date']


# In[31]:


header['Content-Type']


# In[32]:


r.encoding


# In[33]:


r.text[0:100]


# In[34]:


# Use single quotation marks for defining string
url='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/IDSNlogo.png'


# In[35]:


r=requests.get(url)


# In[36]:


print(r.headers)


# In[37]:


r.headers['Content-Type']


# In[38]:


path=os.path.join(os.getcwd(),'image.png')
path


# In[39]:


with open(path,'wb') as f:
    f.write(r.content)


# In[40]:


Image.open(path)  


# In[41]:


url='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/Example1.txt'
path=os.path.join(os.getcwd(),'example1.txt')
r=requests.get(url)
with open(path,'wb') as f:
    f.write(r.content)


# In[42]:


r


# In[43]:


url_get='http://httpbin.org/get'


# In[44]:


payload={"name":"Joseph","ID":"123"}


# In[45]:


r=requests.get(url_get,params=payload)


# In[46]:


r.url


# In[47]:


print("request body:", r.request.body)


# In[48]:


print(r.status_code)


# In[49]:


print(r.text)


# In[50]:


r.headers['Content-Type']


# In[51]:


r.json()


# In[52]:


r.json()['args']


# In[53]:


url_post='http://httpbin.org/post'
r_post=requests.post(url_post,data=payload)


# In[54]:


print("POST request URL:",r_post.url )
print("GET request URL:",r.url)


# In[55]:


print("POST request body:",r_post.request.body)
print("GET request body:",r.request.body)


# In[56]:


r_post.json()['form']


# In[57]:


get_ipython().system('pip install randomuser')


# In[58]:


from randomuser import RandomUser
import pandas as pd


# In[59]:


pip install randomuser


# In[60]:


from randomuser import RandomUser
import pandas as pd


# In[61]:


r = RandomUser()


# In[62]:


some_list = r.generate_users(10)


# In[63]:


some_list


# In[64]:


name = r.get_full_name()


# In[65]:


for user in some_list:
    print (user.get_full_name()," ",user.get_email())


# In[66]:


for user in some_list:
    print (user.get_picture())


# In[67]:


def get_users():
    users =[]
     
    for user in RandomUser.generate_users(10):
        users.append({"Name":user.get_full_name(),"Gender":user.get_gender(),"City":user.get_city(),"State":user.get_state(),"Email":user.get_email(), "DOB":user.get_dob(),"Picture":user.get_picture()})
      
    return pd.DataFrame(users)    


# In[68]:


get_users()


# In[69]:


df1 = pd.DataFrame(get_users())  


# In[70]:


df1


# In[71]:


import requests
import json


# In[72]:


data = requests.get("https://fruityvice.com/api/fruit/all")


# In[73]:


results = json.loads(data.text)


# In[74]:


data


# In[75]:


results


# In[76]:


pd.DataFrame(results)


# In[77]:


df2 = pd.json_normalize(results)


# In[78]:


df2


# In[79]:


cherry = df2.loc[df2["name"] == 'Cherry']
(cherry.iloc[0]['family']) , (cherry.iloc[0]['genus'])


# In[80]:


pip install bs4


# In[81]:


from bs4 import BeautifulSoup # this module helps in web scrapping.
import requests  # this module helps us to download a web page


# In[82]:


get_ipython().run_cell_magic('html', '', "<!DOCTYPE html>\n<html>\n<head>\n<title>Page Title</title>\n</head>\n<body>\n<h3><b id='boldest'>Lebron James</b></h3>\n<p> Salary: $ 92,000,000 </p>\n<h3> Stephen Curry</h3>\n<p> Salary: $85,000, 000 </p>\n<h3> Kevin Durant </h3>\n<p> Salary: $73,200, 000</p>\n</body>\n</html>\n")


# In[83]:


html="<!DOCTYPE html><html><head><title>Page Title</title></head><body><h3><b id='boldest'>Lebron James</b></h3><p> Salary: $ 92,000,000 </p><h3> Stephen Curry</h3><p> Salary: $85,000, 000 </p><h3> Kevin Durant </h3><p> Salary: $73,200, 000</p></body></html>"


# In[84]:


print(soup.prettify())


# In[85]:


soup = BeautifulSoup(html, 'html5lib')


# In[1]:


pip install parser


# In[2]:


url = "http://www.ibm.com"


# In[3]:


data  = requests.get(url).text 


# In[6]:


pip install BeautifulSoup


# In[5]:


pip install requests


# In[7]:


data  = requests.get(url).text 


# In[8]:


url = "http://www.ibm.com"
data  = requests.get(url).text 


# In[11]:


import requests
import BeautifulSoup
url = "http://www.ibm.com"
data  = requests.get(url).text 


# In[10]:


soup = BeautifulSoup(data,"html5lib")  # create a soup object using the variable 'data'


# In[12]:


pip install BeautifulSoup


# In[1]:


pip install BeautifulSoup


# In[1]:


import requests
import BeautifulSoup
url = "http://www.ibm.com"
data  = requests.get(url).text 


# In[2]:


from bs4 import BeautifulSoup # this module helps in web scrapping.
import requests  # this module helps us to download a web page


# In[3]:


url = "http://www.ibm.com"
data  = requests.get(url).text 


# In[1]:


soup = BeautifulSoup(data,"html5lib")  # create a soup object using the variable 'data'


# In[5]:


pip install lxml


# In[3]:


from bs4 import BeautifulSoup # this module helps in web scrapping.
import requests  # this module helps us to download a web page
url = "http://www.ibm.com"
data  = requests.get(url).text 
soup = BeautifulSoup(data,"html.parser")  # create a soup object using the variable 'data'


# In[4]:


for link in soup.find_all('a',href=True):  # in html anchor/link is represented by the tag <a>

    print(link.get('href'))


# In[5]:


from bs4 import BeautifulSoup # this module helps in web scrapping.
import requests  # this module helps us to download a web page
url = "http://www.dreamingduos.com"
data  = requests.get(url).text 
soup = BeautifulSoup(data,"html.parser")  # create a soup object using the variable 'data'
for link in soup.find_all('a',href=True):  # in html anchor/link is represented by the tag <a>

    print(link.get('href'))


# In[6]:


for link in soup.find_all('img'):# in html image is represented by the tag <img>
    print(link)
    print(link.get('src'))


# In[7]:


#The below url contains an html table with data about colors and color codes.
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/HTMLColorCodes.html"


# In[8]:


# get the contents of the webpage in text format and store in a variable called data
data  = requests.get(url).text


# In[9]:


soup = BeautifulSoup(data,"html.parser")


# In[10]:


#find a html table in the web page
table = soup.find('table') # in html table is represented by the tag <table>


# In[11]:


#Get all rows from the table
for row in table.find_all('tr'): # in html table row is represented by the tag <tr>
    # Get all columns in each row.
    cols = row.find_all('td') # in html a column is represented by the tag <td>
    color_name = cols[2].string # store the value in column 3 as color_name
    color_code = cols[3].string # store the value in column 4 as color_code
    print("{}--->{}".format(color_name,color_code))


# In[ ]:




