import pandas as pd
import numpy as np

import requests
from requests import get

#Due Diligence List

csv_url = "https://data.opensanctions.org/datasets/latest/default/targets.simple.csv"

req = requests.get(csv_url)
url_content = req.content
csv_file = open('targets.Due_Diligence_List.csv', 'wb')

csv_file.write(url_content)
csv_file.close()

#Politically Exposed Persons list

csv_url1 = "https://data.opensanctions.org/datasets/latest/peps/targets.simple.csv"

req = requests.get(csv_url1)
url_content = req.content
csv_file = open('targets.Politically_Exposed_Persons.csv', 'wb')

csv_file.write(url_content)
csv_file.close()

#Consolidated Sanctioned Entities list

csv_url2 = "https://data.opensanctions.org/datasets/latest/sanctions/targets.simple.csv"

req = requests.get(csv_url2)
url_content = req.content
csv_file = open('targets.Consolidated_Sanctioned_Entities.csv', 'wb')

csv_file.write(url_content)
csv_file.close()

#Warrants and Criminal Entities list

csv_url3 = "https://data.opensanctions.org/datasets/latest/crime/targets.simple.csv"

req = requests.get(csv_url3)
url_content = req.content
csv_file = open('targets.Warrants_and_Criminal_Entities.csv', 'wb')

csv_file.write(url_content)
csv_file.close()