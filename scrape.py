from bs4 import BeautifulSoup as bs 
import requests
import pandas as pd

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
page= requests.get(START_URL)
soup=bs(page.text,"html.parser")
start_table= soup.find("table")
temp_list=[]
table_rows=start_table.find_all("tr")
for tr in table_rows:
    td=tr.find_all("td")
    row=[i.text.rstrip()for i in td]
    temp_list.append(row)

start_names=[]
distance=[]
mass=[]
radius=[]
lum=[]

for i in range(1,len(temp_list)):
    start_names.append(temp_list[i][1])
    distance.append(temp_list[i][3])
    mass.append(temp_list[i][5])
    radius.append(temp_list[i][6])
    lum.append(temp_list[i][7])
df2=pd.DataFrame(list(zip(start_names,distance,mass,radius,lum)),columns=['Star_names','Distance','Mass','Radius','Luminosity'])
print(df2)
df2.to_csv("estrellas_brillantes.csv")
    
