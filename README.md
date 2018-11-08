# Turtle-neck-Prevent-Program
Turtle Neck Prevent Program

## 필요성 및 동작 개요
현대 21세기에서 위험한 병인 거북목 증후군이라는 것이 있다.
이 증후군은 머리가 구부정하게 앞으로 나오는 자세를 오래 취해 목이 일자 목으로 바뀌고 뒷목, 어깨, 허리 등에 통증이 생기는 증상을 말한다.
이런 자세가 만들어지는 데에는 특히, 장시간 컴퓨터를 사용하게 될 경우 무의식적으로 머리를 앞으로 향한 채 구부정한 자세로 앉아있는데 이러한 자세를 장시간하고 있으면 이 증후군에 걸리거나 증후군 증세가 진행될 수 있다.
본 프로그램을 개발한 나도 거북목이 진행 중이며, 점점 심해지고 있고, 주위 사람들을 보면 목이 일 자인 사람들을 찾는 것이 더 어려운 시대이다.
나는 이 거북목 증후군을 미리 예방고자 컴퓨터를 많이 사용하는 현대인들을 위해 PSD(거리)센서와 파이썬을 연동시킨 프로그램을 개발하고자 한다.
PSD센서는 아두이노와 연결이 되고 그 아두이노에서 센서 값을 받아서 일정 거리에 가까워지면 시리얼 모니터를 통해서 파이썬으로 연결이 된다.
경고 메시지는 UI를 통해서 사용자에게 알려주고, 하루 동안 몇 번의 경고 메시지를 받았는지 PDF파일로 정리해주는 프로그램을 개발해보았다.


## 구현 내용
1) 아두이노 UNO를 이용해서 PSD센서의 거리 값을 실시간으로 받아왔다.
<img src = "http://www.makewith.co/media1/upload/imgs/2016/978/2207/%EC%95%84%EB%91%90%EC%9D%B4%EB%85%B8%20%EC%B5%9C%EC%A2%85.PNG">

시리얼 보레이트는 9600BPS로 설정해주고 PSD센서의 ADC값을 CM로 변환해주기 위해서 map함수와 dis공식을 사용하였다.
그래서 20cm안에 들어오면 시리얼 모니터에 1을 출력하였다.

2) serial을 통해서 아두이노와 시리얼 통신을 하였다.
<img src = http://www.makewith.co/media1/upload/imgs/2016/978/2207/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%B5%9C%EC%A2%851.PNG>
<img src = http://www.makewith.co/media1/upload/imgs/2016/978/2207/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%B5%9C%EC%A2%852.PNG>

시리얼 통신을 사용해야하기 때문에 serial모듈을 import해줘야 한다.
그리고 아두이노에서 보레이트를 9600BPS로 해주었기 때문에 파이썬에도 BPS를 9600으로 설정해주었다.
아두이노 상에서 20cm안에 들어오면 1을 출력하라고 했기 때문에 “1\r\n”을 찾으면 경고 ui를 통해 메시지를 뜨게 하였다.

3) Tkinter을 통해서 UI를 제작했다. PyQT보다 기능이 많이 없지만, 내가 구현하려고 하는 기능으로는 충분히 해볼만하다고 생각했다.
<img src = http://www.makewith.co/media1/upload/imgs/2016/978/2207/KakaoTalk_20161210_231750699.png>
처음화면 UI

ui의 기능을 사용하고 싶었기 때문에 Tkinter모듈을 import하였다.
button, label, scroll기능을 사용했다. 버튼은 다양한 기능을 위해서 사용을 했는데, 센서 활성화 버튼, PDF을 생성하는 버튼을 만들었다.
그리고 Scroll은 눈이 잘 안 보이는 분들을 위해서 글씨를 확대하고자 만든 기능이다.
마지막으로 label을 통해서 어떤 기능이 어떤 역할을 하는지 설명하는 것을 써주었다.

4) tkMessageBox을 통해서 오류 메시지 박스와 정보 박스를 보여주었다.
<img src = http://www.makewith.co/media1/upload/imgs/2016/978/2207/KakaoTalk_20161210_231932086.png>
Save PDF버튼을 누르면 나오는 알림메세지

<img src = http://www.makewith.co/media1/upload/imgs/2016/978/2207/KakaoTalk_20161210_231955561.png>
Information버튼을 누르면 나오는 알림메세지

<img src = http://www.makewith.co/media1/upload/imgs/2016/978/2207/KakaoTalk_20161210_231846299_1.png>
Activate버튼을 누르고 센서가 감지되면 나오는 알림메세지

버튼을 누르면 내가 원하는 기능이 완료되었다는(오류나 정보)신호를 주고 싶었다.
그래서 messagebox모듈을 사용했다. 내가 사용한 기능은 showinfo로 경고 메시지를 주는 box를 생성해준다.

5) pdf파일로 정리해주었다.
<img src = http://www.makewith.co/media1/upload/imgs/2016/978/2207/PDF_IMAGE.PNG>
사용자가 오늘 얼마나 거북목 형태로 목을 앞으로 내밀었는지 즉, 경고 메시지를 얼마나 많이 받았는지 정리해주는 파일을 하나 만들고 싶었다.
그래서 데이터를 pdf파일로 저장하여 깔끔하게 사용자에게 보여주는 기능을 사용하고 싶었다.
그 날의 날짜와 시간이 저장돼서 언제 거북목처럼 목을 내밀었는지 알 수 있고, 몇 번 거북목을 했는지 알 수 있으며, 심각한 상태도 알 수 있게 pdf파일을 만들었다.
또한 프로그램의 설명, pdf의 설명 등 다양한 설명들이 첨부되어있다.

## 결론
이 프로그램으로 거북목을 예방하고 치료할 수 있을 것이다. 거북목을 예방함으로서 사용자의 건강을 책임지고, 허리, 목, 어깨의 통증을 완화시켜줄 것이다. 특히, 21세기 컴퓨터 앞에서 생활을 하는 현대인에 가장 적합한 프로그램이다.
이 프로그램이 소형화가 되어서 스마트폰에도 적용이 된다면 더 큰 영향을 미칠 것이라 예상이 든다.
금전적인 문제로 다른 센서를 추가하지 못해서 풍성한 기능을 구현하지는 못해서 아쉽지만, 내가 개발한 거북목 방지 프로그램으로 거북목을 예방하는 프로그램의 시초라 생각이 든다.
그리고 추후에 센서를 살만큼 여유로워 진다면 다양한 기능을 추가해서 더 나은 프로그램을 개발하고 싶다.


[[PSD 센서 테스트 유튜브 링크]](https://youtu.be/MEnNALq1A4g)
[[PDF 파일 테스트 유튜브 링크]](https://youtu.be/BHXISS462Xk)



## 참고문헌

<거북목 증후군>
https://namu.wiki/w/%EA%B1%B0%EB%B6%81%EB%AA%A9%20%EC%A6%9D%ED%9B%84%EA%B5%B0

<메세지 상자>
http://blog.naver.com/PostView.nhn?blogId=noxburn&logNo=220731246580

<Tkinter>
http://www.w3ii.com/ko/python/tk_button.html
http://www.bment.net/405
http://www.alan-g.me.uk/tutor/korean/tutgui.htm


