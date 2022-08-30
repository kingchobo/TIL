1. Django Intro
   
   - Framework : 서비스 개발에 필요한 기능들을 미리 구현해서 모아 놓은 것
   
   - 클라이언트 : 정보를 달라고 요청하는 컴퓨터(크롬 같은 웹 브라우저)
   
   - 서버 : 정보를 제공하는 컴퓨터(구글 같은 웹 페이지)
   
   - 웹 브라우저 : 웹 페이지 코드를 받으면 우리가 보는 화면처럼 바꾸어 주는 프로그램(HTML, CSS, JS 등의 코드를 읽어 변환)
   
   - 웹 페이지 : 정적 웹페이지, 동적 웹 페이지
     
     - 정적 웹 페이지(static) : 
     
     - 동적 웹 페이지(dynamic) : 동적 웹 페이지를 구현하는데 필요한 게 프레임 워크

2. Django 구조 이해하기 (MTV Design Pattern)
   
   - Design Pattern : 자주 사용되는 구조를 일반화 해서 하나의 공법으로 만든 것(하나의 방법론)
   
   - MVC = Model - View - Controller, 데이터 및 논리 제어를 구현하는데 널리 사용되는 소프트웨어 디자인 패턴
   
   - MVC 소프트웨어 디자인 패턴의 목적 : 관심사 분리 + 협업
   
   - model + controller = 백엔드, view = 프론트
   
   - MTV = Model(데이터) - Template(HTML) - View(처리)

3. Django Quick start
   
   1. 가상환경 설치 : python -m venv venv
   
   2. 가상환경 실행 : source venv/Scripts/activate (종료시 deactivate)
   
   3. 라이브러리 설치 : pip install django==3.2.13 (설치 후 pip list 하면 설치되어 있는지 확인 가능)
   
   4. 백업 : pip freeze > requirments.txt
   
   5. 이후 참고
      
      - django-admin startproject firstpjt .
      
      - python manage.py runserver -> 이후 ctrl누르고 https 주소 클릭하면 생성된 서버로 이동
      
      - 서버 종료 : ctrl + c
      
      - 앱 만들기 : python manage.py startapp pages
      
      - 등록 : firstpjt/setting.py 들어가서 installed apps에 'pages' 등록
      
      - firstpjt/urls.py 들어가서 python manage.py startapp pages
      
      - url에 path 설정하고 views에서 def로 생성. 그리고 templates에서 해당 이름의 html파일 만들어서 사용
      
      - views에서 넘길 때는 반드시 3번째 인자에 딕셔너리 형식이 들어가야 함

4. Django Template
   
   - 화면 : html
   - 템플릿 상속
   - 블럭 태그 안에 내용이 없으면 화면에 안나옴

5. Sending and Retrieving form data

6. Django URLs

7. 마무리
