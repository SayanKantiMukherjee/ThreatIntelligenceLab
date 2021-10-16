#importing the BeautifulSoup Library  
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq  
import os
import re

file_path = os.getcwd()
output_file = file_path+'\\sha_values.csv'
file_contents = []

#Creating the requests  
myurl = "https://bazaar.abuse.ch/browse/"
# myurl = "https://electrodealpro.com/list-of-filenames-hash-sha-256-codes-contains-wannacry-malware/"
uClient  = uReq(myurl)  
page_html = uClient.read()  
uClient.close()
  
# Convert the request object to the Beautiful Soup Object  
page_soup = soup(page_html, features="html.parser")

# regex to filter the SHA content
file_contents = re.findall("[A-Fa-f0-9]{64}", page_soup.text)

# Writing the file_contents to the output_file
file = open(output_file,'w')
for items in file_contents:
    file.writelines(f"{items}\n")
file.close()
