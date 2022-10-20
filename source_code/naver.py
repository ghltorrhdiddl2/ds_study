import requests
import pandas as pd
# from urllib.request.Request
from bs4 import BeautifulSoup

url = "https://finance.naver.com/marketindex/"
res = requests.get(url)
# requests.get(), requests.post()   get()방식, post()방식
# res.text
soup = BeautifulSoup(res.text, "html.parser")

exchangeList = soup.select("#exchangeList > li")

print("-----------------------eee")
# 4개 데이터 수집
exchange_datas = []
baseUrl = "https://finance.naver.com"

for item in exchangeList:
    data = {
        "title" : item.select_one(".h_lst").text,
        "exchange" :item.select_one(".value").text,
        "change" : item.select_one(".change").text,
        "updown" : item.select_one(".head_info.point_dn > .blind").text,
        "link" : baseUrl + item.select_one("a").get("href")
    }
    exchange_datas.append(data)
df = pd.DataFrame(exchange_datas)     #[{}] 리스트 안에 딕셔녀리 자료형은 DataFrame으로 만들기 좋다!!
df
df.to_excel("./naverfinance.xlsx", encoding="utf-8")