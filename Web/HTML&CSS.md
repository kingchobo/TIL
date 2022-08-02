# Web

## 1. Web이란?

##### 1) 웹사이트의 구성 요소

- 웹사이트 : 웹페이지(문서)들의 모음

- 링크를 통해 여러 웹페이지를 연결한 것이 웹사이트

- HTML = 구조, CSS = 표현, Javascript = 동작

##### 2) 웹 표준과 크로스 브라우징

- 웹사이트는 브라우저를 통해 동작 but  브라우저마다 동작이 약간씩 달라서 문제가 생김(파편화) -> 이를 해결하기 위해 웹 표준이 등장

- 웹 표준
  
  - 웹에서 표준적으로 사용되는 기술이나 규칙
  
  - 어떤 브라우저든 웹 페이지가 동일하게 보이도록 함(크로스 브라우징)

##### 3) 개발 환경 설정

- HTML/CSS 코드 작성을 위한 VS Code 추천 확장 프로그램
  
  - Open in browser
  
  - Auto rename tag
  
  - Highlight Matching Tag

- 주석(comment) 꼭 달기 but 무분별한 사용은 금지

- 가급적 같은줄에 작성하지 말고 함수 정의 바로 아래에 ''' ''' 사용하여 간결하게 작성

## 2. HTML

##### 1) HTML 기본 구조

- Hyper Text Markup Language(팀 버너스리)

- HTML만 사용하면 구조만 잡는것 -> 이것을 보기 좋게 정렬하는게 CSS -> Java Script를 쓰면 행동까지 생김(애니메이션?)

- Hyper Text : 링크로 넘어가는 텍스트

- Markup Language : 태그 등을 활용하여 보기 좋게 정렬하는 것

- 파이썬은 4 space indent, html은 2 space!

- html문서 = head(문서 메타데이터 요소) + body(문서 본문 요소)로 구성.

- head 예시 : <title>, <meta>, <link>, <script>, <style> - CSS

- html 요소 : 시작태그 + 요소 + 종료태그(없는경우도 있음) -> 요소의 중첩을 통해 문서를 구조화

- 속성 : 태그를 구체화해주는 것, 속성명 + 속성값으로 구성, html에서는 = 앞뒤로 공백 x

- 주석 : ctrl + / 로 사용

- 시멘틱 태그 : 태그가 고유한 이름과 의미를 가지는 것(의미론적 마크업 - 검색엔진 최적화)

- 렌더링 : 웹사이트 코드를 웹사이트로 만드는 과정 - DOM(document object model) 트리를 이용하여 렌더링

##### 2) HTML 문서 구조화

- 인라인 / 블록 요소

- 인라인:
  
  - <a></a> : href 속성을 활용하여 하이퍼링크 생성
  
  - <strong></strong> : 굵은 글씨
  
  - <i></i> : 글씨 기울임
  
  - <br : 줄바꿈(괄호닫으면 줄바껴서 안닫음)
  
  - <아이mg> : 이미지
  
  - <span></span> : 의미 없는 인라인 컨테이너

- 블록:
  
  - <p></p> : 하나의 문단
  
  - <hr> : 문단 레벨 요소에서 주제의 분리, 수평선으로 표현
  
  - <ol></ol> : 순서가 있는 리스트(ordered list), 숫자로 구분
  
  - <ul></ul> : 순서가 없는 리스트, 그냥 점으로 구분
  
  - <pre> </=>:  HTML에 작성한 내용을 그대로 표현
  
  - <blockquote></=> : 텍스트가 긴 인용문, 들여쓰기를 한 것으로 표현됨
  
  - <div></=> : 의미없는 블록 컨테이너

- form
  
  - <form>은 정보를 서버에 제출하기 위해 사용하는 태그(ex.로그인)
  
  - 기본속성 : action(데이터를 보낼 곳)
  
  - input : form 내에서 어떤 형식으로 input을 받을건지 설정
  
  - input label
    
    ```html
    <label for="agreement">개인정보 수집에 동의합니다.</label>
    <input type="checkbox" name="agreement" id="agreement">
    ```
  
  - input 유형 - 일반 : text, password, email, number, file
  
  - input 유형 - 항목 중 선택 : checkbox(다중선택), radio(단일선택)

## 3. CSS(Cascading Style Sheets)

##### 1) CSS Selectors

- 선택자 유형 : 기본선택자, 결합자, 의사 클래스/요소
  
  - 전체선택자 : *
  
  - 요소선택자 : 태그를 부르는 것
  
  - 클래스선택자 : 마침표(.) 문자로 시작. 해당 클래스가 적용된 항목을 선택
  
  - ID선택자 : #으로 시작, 해당 아이디가 적용된 항목을 선택. 일반적으로 하나의 문서에 한 번만 사용.

- Lorem + tab : 랜덤한 문자열 자동 생성

- CSS 적용 우선순위 : 범위가 좁을수록 강하다(important >> 인라인 > id > class, 속성 > 요소 > *)
  
  - 만약 같은 범위라면 적는 순서에서 아래에 있는 것이 더 쎔

- CSS 상속 : 부모요소를 자식요소에게 상속
  
  - 상속 되는 것 : Text 관련 요소
  
  - 안되는 것 : Layout 관련 요소

##### 2) CSS 단위

##### 3) Selectors 심화

- ##### 4) Box model

- 

##### 5) Display

- ##### 6) Position
