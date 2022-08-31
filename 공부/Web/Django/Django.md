1. Django Intro
   
   - Framework : 서비스 개발에 필요한 기능들을 미리 구현해서 모아 놓은 것
   
   - 클라이언트 : 정보를 요청하는 주체(폰, 컴, 크롬 등)
   
   - 서버 : 정보를 제공하는 주체(컴퓨터, 웹 페이지 등)
   
   - 웹 브라우저 : 웹 페이지 코드를 받으면 우리가 보는 화면처럼 바꾸어 주는(렌더링, rendering) 프로그램(HTML, CSS, JS 등의 코드를 읽어 변환)
   
   - Django는 서버를 구현하는 웹 프레임워크
   
   - 웹 페이지 : 웹에 있는 문서. 우리가 보는 화면 한 장 한 장이 웹 페이지
     
     - 정적 웹 페이지(static) : 한 번 작성된 HTML파일의 내용이 변하지 않고 모든 사용자에게 동일한 모습으로 전달되는 것
     
     - 동적 웹 페이지(dynamic) : 사용자의 요청에 따라 웹 페이지에 추가적인 수정이 되어 클라이언트에게 전달되는 웹 페이지
       
       - 웹 페이지의 내용을 바꾸는 주체 == 서버
       
       - 서버에서 동작하고 있는 프로그램이 웹 페이지를 변경. 이러한 프로그램을 쉽게 만들 수 있게 도와주는 프레임워크가 Django

2. Django 구조 이해하기 (MTV Design Pattern)
   
   - Design Pattern : 자주 사용되는 구조를 일반화 해서 하나의 공법으로 만든 것(하나의 방법론)
   
   - Django's Design Pattern : MTV 패턴
     
     - MTV 패턴은 MVC 디자인 패턴을 기반으로 조금 변형된 패턴
     
     - MVC 소프트웨어 디자인 패턴
       
       - Model(데이터와 관련된 로직을 관리) - View(레이아웃과 화면을 처리) - Controller(명령을 model과 view부분으로 연결)
       
       - 데이터 및 논리 제어를 구현하는데 널리 사용
       
       - 하나의 큰 프로그램을 세 가지 역할로 구분한 개발 방법론
     
     - MVC의 목적 : 관심사 분리를 통해 더 나은 업무의 분리와 향상된 관리를 제공
     
     - MTV = Model(=Model) - Template(=View) - View(=Controller)
       
       - Model : 데이터와 관련된 로직을 관리. 응용프로그램의 데이터 구조를 정의하고 데이터베이스의 기록을 관리
       
       - Template : 레이아웃과 화면을 처리. 화면상의 사용자 인터페이스 구조와 레이아웃을 정리
       
       - View : Model & Template과 관련한 로직을 처리해서 응답을 반환. 클라이언트의 요청에 대해 처리를 분기하는 역할.
         
         - ex) 데이터가 필요하면 Model에 접근하여 데이터를 가져오고 가져온 데이터를 Template으로 보내 화면을 구성하고, 구성된 화면을 응답으로 만들어 클라이언트에게 반환

3. Django Quick start
   
   1. 가상환경 설치 : python -m venv venv
   
   2. 가상환경 실행 : source venv/Scripts/activate (종료시 deactivate)
   
   3. Django 3.2(LTS) 버전 설치 : pip install django==3.2.13(설치 후 pip list 하면 설치되었는지 확인 가능)
      
      - LTS : Long Term Support (장기 지원 버전). 배포자는 LTS 확정을 통해 장기적, 안정적 지원을 보장
   
   4. 패키지 목록 생성 : pip freeze > requirements.txt
   
   5. 프로젝트 생성 : django-admin startproject firstpjt .
      
      - __init__.py : python에게 이 디렉토리를 하나의 python 패키지로 다루도록 지시. 별도의 추가 코드를 작성하지 않음.
      
      - asgi.py : Django 애플리케이션이 비동기식 웹서버와 연결 및 소통하는 것을 도움. 추후 배포시에 사용하며 지금은 수정하지 않음.
      
      - settings.py : Django 프로젝트 설정을 관리
      
      - urls.py : 사이트의 url과 적절한 views의 연결을 지정
      
      - wsgi.py : Django 애플리케이션이 웹 서버와 연결 및 소통하는 것을 도움. 추후 배포시에 사용하며 지금은 수정하지 않음.
      
      - manage.py : Django 프로젝트와 다양한 방법으로 상호작용 하는 커맨드라인 유틸리티
   
   6. 애플리케이션(앱) 생성 : python manage.py startapp articles
      
      - 일반적으로 앱 이름은 '복수형'으로 작성하는 것을 권장
      
      - admin.py : 관리자용 페이지를 설정하는 곳
      
      - apps.py : 앱의 정보가 작성된 곳. 별도로 추가 코드를 작성하지 않음.
      
      - models.py : 애플리케이션에서 사용하는 model을 정의하는 곳. MTV 패턴의 M에 해당
      
      - tests.py : 프로젝트의 테스트 코드를 작성하는 곳
      
      - views.py : view 함수들이 정의되는 곳. MTV 패턴의 V에 해당
   
   7- 애플리케이션 등록
   
   - 프로젝트에서 앱을 사용하기 위해서는 반드시 INSTALLED_APPS 리스트에 추가해야 함.
   
   - 경로 : firstpjt/setting.py 내부에서 INSTALLED_APPS 리스트 찾아서 추가
   
   - 참고 : Project & Application
     
     - Project : 앱의 집합. 하나의 프로젝트에는 여러 앱이 포함될 수 있음.
     
     - App : 실제 요청을 처리하고 페이지를 보여주는 등의 역할 담당.
   
   - 주의사항
     
     - 반드시 생성 후 등록 : INSTALLED_APPS에 등록하기 전에 반드시 생성
     
     - INSTALLED_APPS 리스트 내에서는 장고앱들을 맨 밑에 배치
   
   8- 요청과 응답 : URL -> VIEW -> TEMPLATE 순의 작성순서로 코드를 작성해보고 데이터의 흐름 이해하기
   
   9- URLs 
   
   - firstpjt의 urls.py 파일에서 'from articles import views' 를 써주어 이전에 생성했던 articles 앱과 연결
   
   - 하단의 urlpatterns에 보면 admin은 되어있고, 그 아래에 'path('index/', views.index),'를 작성하여 사용자가 주소창에 index/를 입력할 경우 articles앱 안의 views파일 내부의 index라는 함수(?)로 이동하게 됨
   
   10- View
   
       - articles/views.py 파일로 이동하여
       
         ```python
         def index(request):
             return render(request, 'index.html')
         ```
       
         이렇게 index 함수를 선언해 줌.
       
       - views.py 파일에서는 요청을 수신하여 index.html이라는 template에게 응답서식을 받아와서 render한 후 반환함
       
       - 참고 : render(request, template_name, context)
       
         - request : 응답을 생성하는 데 사용되는 요청 객체
       
         - template_name : 템플릿의 전체 이름 또는 템플릿 이름의 경로
       
         - context : 템플릿에서 사용할 데이터(반드시 딕셔너리 타입)
   
   11- Templates : 실제 내용을 보여주는 데 사용되는 파일
   
       - template 파일의 기본 경로 : app_name/templates/
       
       - 지금은 articles 폴더에서 templates라는 폴더명을 가진 폴더를 생성한 후 index.html이라는 파일을 생성해 주면 됨
   
   12- 추가 설정 : firstpjt/settings.py 들어가서 LANGUAGE_CODE = 'ko-kr', TIME_ZONE = 'Asia/Seoul' 로 설정
   
   13. 서버 실행 : python manage.py runserver
   
   14. 이후 참고
       
       - 앱 만들기 : python manage.py startapp pages
       
       - 등록 : firstpjt/setting.py 들어가서 installed apps에 'pages' 등록
       
       - firstpjt/urls.py 들어가서 python manage.py startapp pages
       
       - url에 path 설정하고 views에서 def로 생성. 그리고 templates에서 해당 이름의 html파일 만들어서 사용

4. Django Template
   
   - 데이터 표현을 제어하는 도구이자 표현에 관련된 로직
   
   - Django Template을 이용하여 HTML의 정적 부분과 동적 컨텐츠 삽입
   
   - Django Template Language(DTL)
     
     - Django Template에서 사용하는 built-in template system
     - 조건, 반복, 변수치환, 필터 등의 기능을 제공(if, for 등)
     - 프로그래밍적 로직 x. 프레젠테이션을 표현하기 위한 것
   
   - DTL Syntax : Variable, Filters, Tags, Comments
     
     - Variable : {{ variable }}
       
       - 변수명은 영어, 숫자, _ 의 조합으로 구성될 수 있으나 밑줄로는 시작 x
       - dot(.)을 사용하여 변수 속성에 접근할 수 있음
       - render()의 세번째 인자로 딕셔너리 형태로 넘겨줄 때 딕셔너리의 key에 해당하는 문자열이 template에서 사용가능한 변수명이 됨
     
     - Filters : {{ variable|filter }}
       
       - 표시할 변수를 수정할 때 사용
       - 총 60가지. 일부 필터는 인자를 받기도 함
     
     - Tags : {{% tag %}}
       
       - 출력 텍스트를 만들거나, 반복 또는 논리를 수행하여 제어흐름을 만드는 등
       - 일부 태그는 시작과 종료 태그가 필요(if, endif)
       - 약 24가지
     
     - Comments : {#  #}
       
       - Django template에서 라인의 주석을 표현하기 위해 사용
       
       - 한 줄 주석에만 사용 가능(줄바꿈 불가)
       
       - 여러줄 주석은 아래와 같이 사용
         
         ```django
         {% comment %}
           여러 줄
           주석
         {% endcomment %}
         ```
   
   - Template inheritance(템플릿 상속)
     
     - 템플릿 상속은 코드의 재사용성에 초점
     
     - 템플릿 상속을 사용하면 사이트의 모든 공통 요소를 포함하고, 하위 템플릿이 재정의(override)할 수 있는 블록을 정의하는 'skeleton' 템플릿을 만들 수 있음
     
     - 템플릿 상속 관련 태그
       
       - {% extends ' ' %} : 자식(하위)템플릿이 부모 템플릿을 확장한다는 것을 알림. 반드시 템플릿 최상단에 작성(즉, 2개 이상 사용 x)
       
       - {% block content %}{% endblock content %} : 하위 템플릿에서 재지정 할 수 있는 블록을 정의. 즉, 하위 템플릿이 채울 수 있는 공간
       
       - 가독성을 높이기 위해 선택적으로 endblock 태그에 이름을 지정할 수 있음
     
     - articles/templates/base.html 이라는 경로와 이름으로 파일 생성
     
     - base.html에 부트스트랩 적용 -> 다른 템플릿으로 이동하여 최상단에 extends 'base.html' 하고 하단에 블럭만들어서 작성
     
     - 추가 템플릿 경로 추가하기
       
       - base.html의 위치를 앱 안의 templates 디렉토리가 아닌 프로젝트 최상단의 templates 디렉토리 안에 위치하고 싶을 때
       
       - setting.py 들어가서 TEMPLATES를 찾고 -> DIRS : [] 의 빈 리스트 안에다 [BASE_DIR / 'templates',], 이렇게 수정해주면 된다.

5. Sending form data
   
   - HTML <form> element : 데이터가 전송되는 방법을 정의
     
     - 웹에서 사용자 정보를 입력하는 여러 방식(text, button, submit 등)을 제공하고, 사용자로부터 할당된 데이터를 서버로 전송하는 역할
     
     - 데이터를 어디로(action), 어떤 방식으로(method) 보낼지
     
     - action : 입력 데이터가 전송될 url을 지정.
     
     - method : 입력 데이터의 HTTP request methods를 지정. HTML form 데이터는 GET 방식과 POST 방식 2가지로만 전송 가능.
   
   - HTML <input> element : 사용자로부터 데이터를 입력받기 위해 사용
     
     - 'type' 속성에 따라 동작방식이 달라진다. type을 지정하지 않은 경우 기본값은 text
     
     - 핵심속성 : name
     
     - name
       
       - form을 통해 데이터를 제출(submit)했을 때 name속성에 설정된 값을 서버로 전송하고, 서버는 name속성에 설정된 값을 통해 사용자가 입력한 데이터 값에 접근할 수 있음
       
       - 주요 용도는 GET/POST 방식으로 서버에 전달하는 파라미터(name은 key, value는 value)로 매핑하는 것.
       
       - GET 방식에서는 URL에서 '?key=value&key=value/' 형식으로 데이터를 전달
     
     - HTTP request methods
       
       - HTTP : HTML 문서와 같은 리소스(데이터)들을 가져올 수 있도록 해주는 프로토콜(규칙, 규약)
       
       - 웹에서 이루어지는 모든 데이터 교환의 기초
       
       - HTTP는 주어진 리소스가 수행 할 원하는 작업을 나타내는 request methods를 정의
       
       - 리소스에 대한 행위(수행하고자 하는 동작)를 정의
       
       - HTTP Method 예시 : GET, POST, PUT, DELETE
     
     - GET(대문자 사용을 권장)
       
       - 서버로부터 정보를 조회하는 데 사용. 서버에 리소스를 요청하기 위해 사용
       
       - 데이터를 가져올 때만 사용해야 함
       
       - 데이터를 서버로 전송할 때 Query String Parameters를 통해 전송
         
         - 데이터는 URL에 포함되어 서버로 보내짐
     
     - Query String Parameters(Query String이라고도 함)
       
       - 사용자가 입력 데이터를 전달하는 방법 중 하나로, url주소에 데이터를 파라미터를 통해 넘기는 것
       
       - 이러한 문자열은 앰퍼샌드(&)로 연결된 key=value 쌍으로 구성되며 기본 url과 물음표로 구분됨

6- Retrieving the data(Server)
   
   - 데이터 가져오기(검색하기)
   
   - throw가 보낸 데이터를 catch에서 가져오기
   
   - 모든 요청 데이터는 view 함수의 첫 번째 인자 request에 들어있다.

7. Django URLs
   
   - Dispatcher(운행 관리원)로써의 URL 이해하기
   
   - 웹 어플리케이션은 URL을 통한 클라이언트의 요청에서부터 시작
   
   - Trailing Slashes : 주소 끝에 / 붙여주기(Django에서는 자동으로 해줌)
   
   - Variable routing : 템플릿의 많은 부분이 중복되고, 일부분만 변경되는 상황에서 비슷한 URL과 템플릿을 계속 만들어야 할까?
     
     - URL주소를 변수로 사용하는 것을 의미
     
     - URL의 일부를 변수로 지정하여 view함수의 인자로 넘길 수 있음
     
     - 즉, 변수 값에 따라 하나의 path()에 여러 페이지를 연결 시킬 수 있음
     
     - 작성법:
     
     - 변수는 < >에 정의하며 view 함수의 인자로 할당됨
     
     - 기본 타입은 string이며 5가지 타입으로 명시할 수 있음
   
   - App URL mapping
     
     - 앱이 많아졌을 때 urls.py를 각 app에 매핑하는 방법을 이해하기
     
     - 두 번째 app인 pages를 생성 및 등록하고 진행
     
     - app의 view 함수가 많아지면서 사용하는 path또한 많아지고, app 또한 더 많이 작성되기 때문에 프로젝트의 urls.py에서 모두 관리하는 것은 프로젝트 유지보수에 좋지 않음
     
     - 각 앱의 view 함수를 다른 이름으로 import 할 수 있음
     
     - 하나의 플젝에 여러 앱이 존재한다면, 각각의 앱 안에 urls.py를 만들고 프로젝트 urls.py에서 각 앱의 urls.py 파일로 URL 매핑을 위탁할 수 있음.
