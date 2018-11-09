## KBSC_서다영소형석최정인

내 근처 편의점에, 특정 제품의 재고가 남아있는지 확인할 수 있게 해주는 카카오 챗봇입니다.

## 사용자 기준 UI
1) 내 위치 설정 (ex. 서울특별시 관악구 대학동 1516)
2) 찾고자 하는 제품 선택 (ex. 베아제(소화제), 로얄 티라미수, etc.)
3) 제품의 재고가 있는 편의점들이 거리순으로 정렬되어 표시됨

## 개발 과정에서의 memo

### 1) AWS 관련 세팅
AWS 접속 https://aws.amazon.com/ko/ - 가입 - 콘솔에 로그인 - Amazon EC2 시작하기 - 가상 머신 시작 - AMI 선택(-검토 및 시작) - elastic IP 발급(-검토 및 시작) - Security Groups에서 포트 설정(-검토 및 시작-시작) - 새 키페어 생성 - 키페어 다운로드 - 인스턴스 시작
위에서 다운받은 키페어가 저장된 디렉토리에서 다음을 실행한다. (키페어 파일은 .pem으로 끝난다)
- 내 서버주소 : IPv4 퍼블릭IP 하단에 있는 ㅇ.ㅇ.ㅇ.ㅇ

### 2) SSH 접속
chmod 400 키페어.pem
ssh -i "키페어.pem" (내가 선택한 서버)@(내 Public DNS)
참고로 위 두 줄은 AWS의 Instances창에서 해당 인스턴스를 우클릭 후 connect를 클릭하면 나온다.
그대로 copy해서 실행하면 ubuntu@ip-(내 Private IP address)로 접속이 된다.

### 3) 웹서버 세팅
ubuntu@ip-(내 Private IP address)로 접속된 상태에서 다음을 실행한다.
웹 서버를 세팅해주는 이러한 작업은 초기에 한번만 해주면 된다.

python3 //얘python 3.6.6이라고 나와있으면 기억하셈

sudo apt-get upgrade && sudo apt-get update

sudo apt-get install apache2

sudo apt-get install libapache2-mod-wsgi-py3

sudo apt-get install python3-pip

sudo pip3 install Django

sudo apt-get install python3.6-venv

sudo apt-get install git

pip3 install flask

### 4) 코드 실행

따로 python 코드를 작성해놓고,
sudo nano numulbo.py
//위 커맨드를 치고 나타난 광활한 공백에 붙여넣는다
//그러고 아래코드를 실행한다
python3 numulbo.py

### 5) 카카오톡 플러스친구 관리자센터 https://center-pf.kakao.com/ 접속
플러스친구 개설 - "스마트채팅" - "API형" - "설정하기/시작하기"
앱 URL에 http://ㅇ.ㅇ.ㅇ.ㅇ:포트번호 입력
참고로 ㅇ.ㅇ.ㅇ.ㅇ는 1) AWS 관련 세팅의 맨 아랫줄에 언급한 IPv4 퍼블릭IP
URL 및 기타 정보들 입력한 후 "API테스트"클릭, 클릭 시 Keyboard OK가 뜨면 된다.


## 개발 계획 (2018. 11. 8.)

#### 구현해야 하는 버튼/기능
버튼 "내 위치 설정하기" - 지도 based 
버튼 "제품 선택하기"
버튼 "재고 확인하기"

things to consider : 챗봇이면 '대화형' - 문장으로부터 키워드 알아서 추출해서 대답해주는 형식도 궁극적으로는 만들어야하지 않을까
(ex. "역삼역 근처에 베아제 파는 데 알려줘")