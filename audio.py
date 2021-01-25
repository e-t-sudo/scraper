
#--take url of the webpage and the directory in which the user wants to store the files

webpage = raw_input("Enter the url: ")
directory = raw_input("Enter the folder name where you want to store the files: ")
print("Contents of ", webpage, " will be extracted to the folder ", directory);
#--------------------------------------------------------------------------------------



#--fetch file links and append them to a list
print("Your request is being processed...")
import os
os.system("sleep 1")
import requests
result = requests.get(webpage)
page = result.text
from bs4 import BeautifulSoup
soup = BeautifulSoup(page, 'html.parser')

source_elements = soup.find_all('source')

file_links = []
for source_element in source_elements:
    link = source_element['src']
    file_links.append(link)
#---------------------------------------------

#--make the directory 
import os
os.system("mkdir %s" % directory)
#--------------------------------------------


#--get file urls and web-get them to the "directory"
for x in range(len(file_links)):
    print(x,"   ", file_links[x])
    url = file_links[x]
    os.system('wget %s -O %s/%d.mp3' % (url,directory,x+1))
    os.system('ls %s && sleep 2' % directory)
#-------------------------------------------



#--make a csv file of all the links that have been fetched
import pandas as pd

df = pd.DataFrame({'Links': file_links })
df.to_csv('links.csv', index=False, encoding='utf-8')
os.system("mv links.csv %s" % directory)

#---------------------------------------------


