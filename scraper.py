class airquality:
    data = []
    def __init__(self,dataurl="https://airnow.tehran.ir/"):
        self.url= dataurl
                
    def threadfunc(self):
        while (1):
            import time
            from requests import get
            import requests
            from bs4 import BeautifulSoup
            try:
                response = get(self.url, timeout=60)
            except requests.exceptions.Timeout as e:
                print ('excepted')
            
            html_soup = BeautifulSoup(response.text , 'html.parser')
            tmpdata = html_soup.find('span',attrs={"id":"ContentPlaceHolder1_lblAqi3h"})
            self.data.append(tmpdata.text)
            print('exiting thread func')
            time.sleep(300)

    def getairquality(self):
        return self.data[-1]
        
