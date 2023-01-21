import requests 
import bs4 
# import sys 

myId = 'cjswogywo'

# URL = f'https://solved.ac/profile/{myId}/history'
URL = "https://www.acmicpc.net/user/"+ myId

response = requests.get(URL)
soup = bs4.BeautifulSoup(response.text,"html.parser")

# sys.stdout = open('output.txt','w')

print(soup)
    
"""
그냥 print로 해결하는 문제...
"""