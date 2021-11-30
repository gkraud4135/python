import requests

#res google.com 정상 접속시 실행
res = requests.get("http://google.com")
res.raise_for_status()

#길이와 내용
print(len(res.text))
print(res.text)

#mygoogle.html라는 이름으로 'w'rite 쓰기모드로 f.write 글씨를 넣음 (파일읽고쓰기)
with open("mygoogle.html", "w", encoding="utf8") as f:
    f.write(res.text)