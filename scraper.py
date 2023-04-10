import requests
from bs4 import BeautifulSoup
import json

url = 'https://www.zappos.com/c/shoe-size-conversion'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

tables = soup.find_all('table')
table_data = []

for table in tables:
    headers = [header.text for header in table.find_all('th')]
    rows = table.find_all('tr')
    rows_data = []

    for row in rows:
        row_data = [data.text for data in row.find_all('td')]
        rows_data.append(row_data)

    table_dict = {'headers': headers, 'data': rows_data}
    table_data.append(table_dict)

json_data = json.dumps(table_data)
with open('output.json', 'w') as f:
    f.write(json_data)
