import requests 
import re

code = input("종목코드를 입력하세요 : ")

re_enc = re.compile("encparam: '(.*)'", re.IGNORECASE) 
re_id = re.compile("id: '([a-zA-Z0-9]*)' ?", re.IGNORECASE)

url = "http://companyinfo.stock.naver.com/v1/company/c1010001.aspx?cmp_cd={}".format(code) 
html = requests.get(url).text 
encparam = re_enc.search(html).group(1) 
encid = re_id.search(html).group(1)

url = "http://companyinfo.stock.naver.com/v1/company/ajax/cF1001.aspx?cmp_cd={}&fin_typ=0&freq_typ=A&encparam={}&id={}".format(code, encparam, encid) 
headers = {"Referer": "HACK"}
html = requests.get(url, headers=headers).text 

from bs4 import BeautifulSoup

soup = BeautifulSoup(html, 'html.parser')


url = "http://companyinfo.stock.naver.com/v1/company/ajax/cF1001.aspx?cmp_cd={}&fin_typ=0&freq_typ=A&encparam={}&id={}".format(code, encparam, encid)
a = soup.findall("td",{"class":"title"})
print(a)
