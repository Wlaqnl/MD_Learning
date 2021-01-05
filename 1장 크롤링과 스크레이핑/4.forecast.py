import urllib.request
import urllib.parse

API = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"

# 매개 변수를 URL 인코딩하기
values={
    'stnId': '143' #경상북도
}

params=urllib.parse.urlencode(values)

#요청 전용 URL을 생성합니다.
url = API + "?" + params
print("url = ", url)

# 다운로드
data = urllib.request.urlopen(url).read()
text = data.decode("utf-8")
print(text)