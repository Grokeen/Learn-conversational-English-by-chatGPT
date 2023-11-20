'''
이 코드를 실행하면 네이버가 한번에 보여주는 이미지 갯수 만큼 50개의 이미지가 저장된다
참고자료 https://ultrakid.tistory.com/13
https://bskyvision.com/721
'''
#사진 크롤링에 필요한 import 목록
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from urllib.parse import quote_plus

#필요한 설치 목
#pip install beautifulsoup4 이미지 저장
#pip install requests


#[CODE 1]
#검색한 주소,  우리가 원하는 검색어의 이미지를 크롤링하기 위하여 뒤에 검색어는 파이썬 실행시에 입력하도록 plusurl이라는 변수로 생성
baseUrl = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query='
plusUrl = input('검색어를 입력하세요 : ')
#crawl_num = int(input('크롤링할 갯수 입력(최대 50개): '))


# url = baseurl + 검색어
url = baseUrl + quote_plus(plusUrl) #한글 검색 자동 변환
html = urlopen(url)
soup = bs(html, "html.parser")
img = soup.find_all(class_='_img')



#[CODE 2]
n = 1
for i in img:
    imgUrl = i['data-source']
    with urlopen(imgUrl) as f:
        with open('./img/' + plusUrl + str(n)+'.jpg','wb') as h: # w - write b - binary
            img = f.read()
            h.write(img)
    n += 1
    if n > crawl_num:
        break
        
    
print('다운로드 완료')
