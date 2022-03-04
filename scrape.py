import requests
from bs4 import BeautifulSoup
import pandas as pd
page_no= 1
url = "https://getlatka.com/?page={}"
page = requests.get(url.format(page_no))

soup = BeautifulSoup(page.content, "lxml")
arr = []
columns =[]
header = soup.find(class_="data-table_header__2WB0s")
# finding the names of each column in the table
for i in header.findAll('th'):
    columns.append(i.text)
print(columns)
df =  pd.DataFrame(columns=columns[1:])

#iterating over each page until there is no more pages further
while True:

    rows =soup.findAll(class_="data-table_row__2w7Kn")
    for row in rows:
        row_data = row.findAll('td')
        cur = [i.text for i in row_data[1:]]
        l = len(df)
        df.loc[len]=cur
    if not soup.find(class_="pagination_button__1f2SL pagination_special_button__3cnmT"):
        break
    page_no+=1
    page = requests.get(url.format(page_no))

    soup = BeautifulSoup(page.content, "lxml")
#converting dataframe "df" to json file
df.to_json('./output.json', orient='index')

    


