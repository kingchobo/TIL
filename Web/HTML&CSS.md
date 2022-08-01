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

- 정수 자료형(int)

- 진수 표현
  
  - 2진수(binary) : 0b
  
  - 8진수(Octal) : 0o
  
  - 16진수(hexadecimal) : 0x
    
    ```python
    print(0b10) # 2
    print(0o30) # 24
    print(0x10) # 16
    ```

- 실수 자료형(float)
  
  - 부동소수점 문제 : 컴퓨터는 2진수, 사람은 10진수를 사용하기 때문에 소수표현이 완전히 동일하지 않고 근사값을 사용하게 됨.
    
    ```python
    print(3.2 - 3.1) # 0.10000000000000009
    ```
  
  - 해결방법
    
    ```python
    import math
    print(math.isclose(a, b)) # True
    ```

##### 2) HTML 문서 구조화

- Escape sequence : backslash 뒤에 특정 문자가 와서 특수한 기능을 하는 문자 조합
  
  - \r : 캐리지 리턴
  
  - \0 : Null
  
  - \\\ : \
  
  - \' : '
  
  - \" : "

- String Interpolation(문자열을 변수를 활용하여 만드는 법)
  
  - f-strings

##### 

## 3. CSS

##### 1) CSS Selectors

- mutable : 변경 가능한(<-> immutable)

- 

##### 2) CSS 단위

##### 3) Selectors 심화

- 생성시 주의사항 : 단일 항목의 경우 값 뒤에 ,를 붙여야 함. 복수 항목의 경우에도 권장.
  
  ```python
  a = (1,)
  print(a) # (1,)
  b = (1,2,3,)
  print(type(b) # <class 'tuple'>
  ```

##### 4) Box model

- 사용 예시
  
  ```python
  print(list(range(1,5,2)))  # [1, 3]
  print(list(range(6,1,-1))) # [6,5,4,3,2]
  print(list(range(6,1,1)))  # []
  ```

##### 5) Display

- 사용예시
  
  ```python
  '12345'[::-1] # '54321'
  ```

##### 6) Position
