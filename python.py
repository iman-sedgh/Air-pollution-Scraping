from requests import get
from bs4 import BeautifulSoup

url = "https://airnow.tehran.ir/"
response = get(url)
#print(response.text)
html_soup = BeautifulSoup(response.text , 'html.parser')
data = html_soup.findAll('span',attrs={"id":"ContentPlaceHolder1_lblAqi3h"})
#print (data)
data2 = str ( data[0] )
start =str ( data2 [ int ( data2.index(">") )  +1 : ] )
#print (start)
final = str ( start [:start.index("<")])
print (final) 
#start = start [1:data.index("<")]
#print  (start 