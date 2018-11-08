# cvsChatBot
KBSC

내 근처 편의점에, 특정 제품의 재고가 남아있는지 확인할 수 있게 해주는 카카오 챗봇입니다.

ex. "CU 대학동고시촌점"클릭 - "초코티라미수"클릭 - 재고 유무가 화면에 출력됩니다.


#1 내 key가 저장된 디렉토리에서 다음을 실행한다
chmod 400 키.pem
ssh -i "키.pem" ~ // 이 부분은 aws상에서 connect하면 뜨는거 copy하면 됨
위 두 줄을 치고 나면 ubuntu@ip-(내ip)로 접속이 된다

#2 ubuntu@ip-~ 로 들어가 있는 상태에서 다음을 차례로 침 (초기에 한번만 해주면 되는부분)
python3
//이러고 만약 python 3.6.6이라고 나와있으면 기억하셈
sudo apt-get upgrade && sudo apt-get update
sudo apt-get install apache2
sudo apt-get install libapache2-mod-wsgi-py3
sudo apt-get install python3-pip
sudo pip3 install Django
sudo apt-get install python3.6-venv
sudo apt-get install git
pip3 install flask

#3 따로 python 코드를 작성해놓고,
sudo nano numulbo.py
//위 커맨드를 치고 나타난 광활한 공백에 붙여넣는다
//그러고 아래코드를 실행한다
python3 numulbo.py

#4 카카오 거기 가서
(aws거기서 ipv4에 있는 숫자 네개짜리):(내가 할당해놓은포트넘버) 치셈

#5 위치
http://kay0426.tistory.com/3
