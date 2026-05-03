!pip install beautifulsoup4 requests
import requests
from bs4 import BeautifulSoup
import numpy as np
#Assignment
assignment_url = "https://faruk-hasan.com/ai_resources/missing_data.html"
get_req = requests.get(assignment_url) #visit url
parse = BeautifulSoup(get_req.text, 'html.parser') #parse it
fruit_name_list = parse.find_all("div", class_="fruit")
fruits_set = set()
for i in fruit_name_list:
  clean_fruits = i.text.strip().lower()
  fruits_set.add(clean_fruits)
fruit_array = np.array(list(fruits_set),dtype=str)
for i in range(len(fruit_array)):
  if fruit_array[i] in ["", "null", "nan"]:
    fruit_array[i] = "unknown"
for i in fruit_array:
  if i != "":
    var = i.capitalize()
    print(var)
