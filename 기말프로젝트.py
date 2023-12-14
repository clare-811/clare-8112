import requests
from bs4 import BeautifulSoup
import bs4
import csv
import pprint
import pandas as pd
from pandas import DataFrame
from datetime import datetime, timedelta

datas = []
# 각 행의 컬럼, 이름, 값을 가지는 리스트 만들기
seatcnt_list = [] # 좌석 수 리스트
totnmrs_list = [] # 티켓 판매 수 리스트

start = "20170801"
last = "20170810"
start_date = datetime.strptime(start, "%Y%m%d")
last_date = datetime.strptime(last, "%Y%m%d")

#예술의 전당
#인증키 입력
encoding ='3b021e221f954651a71f6834030e5406' #발급받은 인코딩키 입력
# 종료일 까지 반복
while start_date <= last_date:
    string = str(start_date.year)
    if (start_date.month<10):
        string = string + str(0)
        string = string + str(start_date.month)
    else:
        string = string + str(start_date.month)
    if (start_date.day<10):
        string = string + str(0)
        string = string + str(start_date.day)
    else:
        string = string + str(start_date.day)
    print(string)
    #url 입력
    url = 'https://www.kopis.or.kr/openApi/restful/prfstsPrfByFct?'
    params ={'service' : encoding , 'cpage' : '1', 'rows' : '10', 'stdate' : string, 'eddate' : string,'sharea':'11','shprfnmfct':'예술의전당' }

    response = requests.get(url, params=params)

    content = response.text

    xml_obj = bs4.BeautifulSoup(content,'lxml-xml')
    rows = xml_obj.findAll('prfst')
    print(rows)

    # xml 안의 데이터 수집
    for item in rows:
        seatcnt = item.find('seatcnt') #좌석 수
        seatcnt = seatcnt.get_text()
        totnmrs = item.find('totnmrs') #총 티켓 판매 수
        totnmrs = totnmrs.get_text()
        data = [seatcnt,totnmrs]
        datas.append(data)

    df = pd.DataFrame(datas, columns=['좌석 수', '티켓 판매수'])
    start_date += timedelta(days=1)
    
#충무아트센터
start = "20180801"
last = "20180910"
start_date = datetime.strptime(start, "%Y%m%d")
last_date = datetime.strptime(last, "%Y%m%d")

#인증키 입력
encoding ='3b021e221f954651a71f6834030e5406' #발급받은 인코딩키 입력
# 종료일 까지 반복
while start_date <= last_date:
    string = str(start_date.year)
    if (start_date.month<10):
        string = string + str(0)
        string = string + str(start_date.month)
    else:
        string = string + str(start_date.month)
    if (start_date.day<10):
        string = string + str(0)
        string = string + str(start_date.day)
    else:
        string = string + str(start_date.day)
    print(string)
    #url 입력
    url = 'https://www.kopis.or.kr/openApi/restful/prfstsPrfByFct?'
    params ={'service' : encoding , 'cpage' : '1', 'rows' : '10', 'stdate' : string, 'eddate' : string,'sharea':'11','shprfnmfct':'충무아트센터' }

    response = requests.get(url, params=params)

    content = response.text

    xml_obj = bs4.BeautifulSoup(content,'lxml-xml')
    rows = xml_obj.findAll('prfst')
    print(rows)

    # xml 안의 데이터 수집
    for item in rows:
        seatcnt = item.find('seatcnt') #좌석 수
        seatcnt = seatcnt.get_text()
        totnmrs = item.find('totnmrs') #총 티켓 판매 수
        totnmrs = totnmrs.get_text()
        data = [seatcnt,totnmrs]
        datas.append(data)

    df = pd.DataFrame(datas, columns=['좌석 수', '티켓 판매수'])
    start_date += timedelta(days=1)
    
#세종문화회관
start = "20191001"
last = "20191110"
start_date = datetime.strptime(start, "%Y%m%d")
last_date = datetime.strptime(last, "%Y%m%d")

#인증키 입력
encoding ='3b021e221f954651a71f6834030e5406' #발급받은 인코딩키 입력
# 종료일 까지 반복
while start_date <= last_date:
    string = str(start_date.year)
    if (start_date.month<10):
        string = string + str(0)
        string = string + str(start_date.month)
    else:
        string = string + str(start_date.month)
    if (start_date.day<10):
        string = string + str(0)
        string = string + str(start_date.day)
    else:
        string = string + str(start_date.day)
    print(string)
    #url 입력
    url = 'https://www.kopis.or.kr/openApi/restful/prfstsPrfByFct?'
    params ={'service' : encoding , 'cpage' : '1', 'rows' : '10', 'stdate' : string, 'eddate' : string,'sharea':'11','shprfnmfct':'세종문화회관' }

    response = requests.get(url, params=params)

    content = response.text

    xml_obj = bs4.BeautifulSoup(content,'lxml-xml')
    rows = xml_obj.findAll('prfst')
    print(rows)

    # xml 안의 데이터 수집
    for item in rows:
        seatcnt = item.find('seatcnt') #좌석 수
        seatcnt = seatcnt.get_text()
        totnmrs = item.find('totnmrs') #총 티켓 판매 수
        totnmrs = totnmrs.get_text()
        data = [seatcnt,totnmrs]
        datas.append(data)

    df = pd.DataFrame(datas, columns=['좌석 수', '티켓 판매수'])
    start_date += timedelta(days=1)
    
#예스24스테이지
start = "20170101"
last = "20170201"
start_date = datetime.strptime(start, "%Y%m%d")
last_date = datetime.strptime(last, "%Y%m%d")

#인증키 입력
encoding ='3b021e221f954651a71f6834030e5406' #발급받은 인코딩키 입력
# 종료일 까지 반복
while start_date <= last_date:
    string = str(start_date.year)
    if (start_date.month<10):
        string = string + str(0)
        string = string + str(start_date.month)
    else:
        string = string + str(start_date.month)
    if (start_date.day<10):
        string = string + str(0)
        string = string + str(start_date.day)
    else:
        string = string + str(start_date.day)
    print(string)
    #url 입력
    url = 'https://www.kopis.or.kr/openApi/restful/prfstsPrfByFct?'
    params ={'service' : encoding , 'cpage' : '1', 'rows' : '10', 'stdate' : string, 'eddate' : string,'sharea':'11','shprfnmfct':'예스 24 스테이지(구. DCF 대명문화공장)' }

    response = requests.get(url, params=params)

    content = response.text

    xml_obj = bs4.BeautifulSoup(content,'lxml-xml')
    rows = xml_obj.findAll('prfst')
    print(rows)

    # xml 안의 데이터 수집
    for item in rows:
        seatcnt = item.find('seatcnt') #좌석 수
        seatcnt = seatcnt.get_text()
        totnmrs = item.find('totnmrs') #총 티켓 판매 수
        totnmrs = totnmrs.get_text()
        data = [seatcnt,totnmrs]
        datas.append(data)

    df = pd.DataFrame(datas, columns=['좌석 수', '티켓 판매수'])
    start_date += timedelta(days=1)
    
#코엑스
start = "20211210"
last = "20220115"
start_date = datetime.strptime(start, "%Y%m%d")
last_date = datetime.strptime(last, "%Y%m%d")

#인증키 입력
encoding ='3b021e221f954651a71f6834030e5406' #발급받은 인코딩키 입력
# 종료일 까지 반복
while start_date <= last_date:
    string = str(start_date.year)
    if (start_date.month<10):
        string = string + str(0)
        string = string + str(start_date.month)
    else:
        string = string + str(start_date.month)
    if (start_date.day<10):
        string = string + str(0)
        string = string + str(start_date.day)
    else:
        string = string + str(start_date.day)
    print(string)
    #url 입력
    url = 'https://www.kopis.or.kr/openApi/restful/prfstsPrfByFct?'
    params ={'service' : encoding , 'cpage' : '1', 'rows' : '10', 'stdate' : string, 'eddate' : string,'sharea':'11','shprfnmfct':'코엑스' }

    response = requests.get(url, params=params)

    content = response.text

    xml_obj = bs4.BeautifulSoup(content,'lxml-xml')
    rows = xml_obj.findAll('prfst')
    print(rows)

    # xml 안의 데이터 수집
    for item in rows:
        seatcnt = item.find('seatcnt') #좌석 수
        seatcnt = seatcnt.get_text()
        totnmrs = item.find('totnmrs') #총 티켓 판매 수
        totnmrs = totnmrs.get_text()
        data = [seatcnt,totnmrs]
        datas.append(data)

    df = pd.DataFrame(datas, columns=['좌석 수', '티켓 판매수'])
    start_date += timedelta(days=1)
    
#아트원씨어터
start = "20180306"
last = "20180415"
start_date = datetime.strptime(start, "%Y%m%d")
last_date = datetime.strptime(last, "%Y%m%d")

#인증키 입력
encoding ='3b021e221f954651a71f6834030e5406' #발급받은 인코딩키 입력
# 종료일 까지 반복
while start_date <= last_date:
    string = str(start_date.year)
    if (start_date.month<10):
        string = string + str(0)
        string = string + str(start_date.month)
    else:
        string = string + str(start_date.month)
    if (start_date.day<10):
        string = string + str(0)
        string = string + str(start_date.day)
    else:
        string = string + str(start_date.day)
    print(string)
    #url 입력
    url = 'https://www.kopis.or.kr/openApi/restful/prfstsPrfByFct?'
    params ={'service' : encoding , 'cpage' : '1', 'rows' : '10', 'stdate' : string, 'eddate' : string,'sharea':'11','shprfnmfct':'대학로아트원씨어터' }

    response = requests.get(url, params=params)

    content = response.text

    xml_obj = bs4.BeautifulSoup(content,'lxml-xml')
    rows = xml_obj.findAll('prfst')
    print(rows)

    # xml 안의 데이터 수집
    for item in rows:
        seatcnt = item.find('seatcnt') #좌석 수
        seatcnt = seatcnt.get_text()
        totnmrs = item.find('totnmrs') #총 티켓 판매 수
        totnmrs = totnmrs.get_text()
        data = [seatcnt,totnmrs]
        datas.append(data)

    df = pd.DataFrame(datas, columns=['좌석 수', '티켓 판매수'])
    start_date += timedelta(days=1)
    
#아르코 예술극장
start = "20180401"
last = "20180501"
start_date = datetime.strptime(start, "%Y%m%d")
last_date = datetime.strptime(last, "%Y%m%d")

#인증키 입력
encoding ='3b021e221f954651a71f6834030e5406' #발급받은 인코딩키 입력
# 종료일 까지 반복
while start_date <= last_date:
    string = str(start_date.year)
    if (start_date.month<10):
        string = string + str(0)
        string = string + str(start_date.month)
    else:
        string = string + str(start_date.month)
    if (start_date.day<10):
        string = string + str(0)
        string = string + str(start_date.day)
    else:
        string = string + str(start_date.day)
    print(string)
    #url 입력
    url = 'https://www.kopis.or.kr/openApi/restful/prfstsPrfByFct?'
    params ={'service' : encoding , 'cpage' : '1', 'rows' : '10', 'stdate' : string, 'eddate' : string,'sharea':'11','shprfnmfct':'아르코예술극장' }

    response = requests.get(url, params=params)

    content = response.text

    xml_obj = bs4.BeautifulSoup(content,'lxml-xml')
    rows = xml_obj.findAll('prfst')
    print(rows)

    # xml 안의 데이터 수집
    for item in rows:
        seatcnt = item.find('seatcnt') #좌석 수
        seatcnt = seatcnt.get_text()
        totnmrs = item.find('totnmrs') #총 티켓 판매 수
        totnmrs = totnmrs.get_text()
        data = [seatcnt,totnmrs]
        datas.append(data)

    df = pd.DataFrame(datas, columns=['좌석 수', '티켓 판매수'])
    start_date += timedelta(days=1)
    
#샤롯데씨어터
start = "20180401"
last = "20180501"
start_date = datetime.strptime(start, "%Y%m%d")
last_date = datetime.strptime(last, "%Y%m%d")

#인증키 입력
encoding ='3b021e221f954651a71f6834030e5406' #발급받은 인코딩키 입력
# 종료일 까지 반복
while start_date <= last_date:
    string = str(start_date.year)
    if (start_date.month<10):
        string = string + str(0)
        string = string + str(start_date.month)
    else:
        string = string + str(start_date.month)
    if (start_date.day<10):
        string = string + str(0)
        string = string + str(start_date.day)
    else:
        string = string + str(start_date.day)
    print(string)
    #url 입력
    url = 'https://www.kopis.or.kr/openApi/restful/prfstsPrfByFct?'
    params ={'service' : encoding , 'cpage' : '1', 'rows' : '10', 'stdate' : string, 'eddate' : string,'sharea':'11','shprfnmfct':'샤롯데씨어터' }

    response = requests.get(url, params=params)

    content = response.text

    xml_obj = bs4.BeautifulSoup(content,'lxml-xml')
    rows = xml_obj.findAll('prfst')
    print(rows)

    # xml 안의 데이터 수집
    for item in rows:
        seatcnt = item.find('seatcnt') #좌석 수
        seatcnt = seatcnt.get_text()
        totnmrs = item.find('totnmrs') #총 티켓 판매 수
        totnmrs = totnmrs.get_text()
        data = [seatcnt,totnmrs]
        datas.append(data)

    df = pd.DataFrame(datas, columns=['좌석 수', '티켓 판매수'])
    start_date += timedelta(days=1)
    
#국립극장
start = "20190401"
last = "20190501"
start_date = datetime.strptime(start, "%Y%m%d")
last_date = datetime.strptime(last, "%Y%m%d")

#인증키 입력
encoding ='3b021e221f954651a71f6834030e5406' #발급받은 인코딩키 입력
# 종료일 까지 반복
while start_date <= last_date:
    string = str(start_date.year)
    if (start_date.month<10):
        string = string + str(0)
        string = string + str(start_date.month)
    else:
        string = string + str(start_date.month)
    if (start_date.day<10):
        string = string + str(0)
        string = string + str(start_date.day)
    else:
        string = string + str(start_date.day)
    print(string)
    #url 입력
    url = 'https://www.kopis.or.kr/openApi/restful/prfstsPrfByFct?'
    params ={'service' : encoding , 'cpage' : '1', 'rows' : '10', 'stdate' : string, 'eddate' : string,'sharea':'11','shprfnmfct':'국립극장' }

    response = requests.get(url, params=params)

    content = response.text

    xml_obj = bs4.BeautifulSoup(content,'lxml-xml')
    rows = xml_obj.findAll('prfst')
    print(rows)

    # xml 안의 데이터 수집
    for item in rows:
        seatcnt = item.find('seatcnt') #좌석 수
        seatcnt = seatcnt.get_text()
        totnmrs = item.find('totnmrs') #총 티켓 판매 수
        totnmrs = totnmrs.get_text()
        data = [seatcnt,totnmrs]
        datas.append(data)

    df = pd.DataFrame(datas, columns=['좌석 수', '티켓 판매수'])
    start_date += timedelta(days=1)
    
df
df = df.astype({'티켓 판매수':'int'})
df_remove = df[df['티켓 판매수']>0]

#데이터 분석
df_remove

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(8, 6))
sns.scatterplot(x='좌석 수', y='티켓 판매수', data=df)

plt.title('seat and ticket')
plt.xlabel('seat')
plt.ylabel('ticket')
plt.show()