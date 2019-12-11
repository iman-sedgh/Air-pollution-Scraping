class airquality:

    def __init__(self,dataurl="https://airnow.tehran.ir/"):
        self.url= dataurl
                
    
    def getairquality(self):
        from requests import get
        from bs4 import BeautifulSoup
        response = get(self.url)
        #print ("geting URL")
     
        html_soup = BeautifulSoup(response.text , 'html.parser')
        data = html_soup.find('span',attrs={"id":"ContentPlaceHolder1_lblAqi3h"})
        data = data.text
        return data 
#print airquality.getairquality()