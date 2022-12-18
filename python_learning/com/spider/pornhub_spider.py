import requests
from bs4 import BeautifulSoup
headers = {'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}

url = 'https://cn.pornhub.com/video/search?search=china'
html=requests.get(url,headers=headers)
   
soup=BeautifulSoup(html.content,'html.parser')
jpg_data=soup.find_all('img',attrs={'width':"150" })
for cur in jpg_data:
    pic_src=cur['src']
    if(".jpg" in pic_src):
        filename=cur['alt']+'.jpg'
        with open(filename,'wb') as f:
            f.write(bytes(pic_src,encoding='utf-8'))
            print(filename)
            f.close()