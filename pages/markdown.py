import streamlit as st  # streamlit -> import (가져오기) -> as (st 이름)

# 마크다운
# https://heropy.blog/2017/09/30/markdown/
st.title("마크다운")
# st.write / st.markdown
# st.write -> 입력하는 것에 맞춰서 알아서 결정 => 마크다운
# st.markdown -> 명백하게 마크다운을 사용하겠다
st.divider()
st.subheader("제목")
# 제목 마크다운
st.write("""
# 가장 큰 제목 (h1 - headline1 - st.title)
## 그 다음 큰 제목 (h2 - headline2 - st.header)
### 그것보단 작은 제목 <- 대부분 여기까지만 씀 (h3 - headline3 - st.subheader)
#### 좀 더 작은 제목 (h4)
##### 이건 없겠지? (h5)
###### 이것도 있나? (h6)
####### 이건 없어.
""")  # 문자열을 넣으면 마크다운임
st.divider()
# 서식
st.subheader("서식")
text = """
기울임 : *별표* 또는 _언더바_ 하나씩 써주면

진하게(bold) : **별표**를 또는 __언더바__ 두개씩 써주면

기울임 + 진하게(bold) : ***별표***를 또는 ___언더바___ 세개씩 써주면

취소선 : ~물결표~

밑줄 : <u>밑줄</u>

형광펜 : <mark>형광펜</mark>
"""
# st.write(text)
# 태그를 허용하는 옵션
st.markdown(text, unsafe_allow_html=True)

# 레이아웃
st.divider()
st.subheader("레이아웃")
st.write("""
    #### 순서가 없는 리스트
    * 별표를 여백 1칸 이상과 사용하면 순서가 없는 리스트
    * 별표를 여백 1칸 이상과 사용하면 순서가 없는 리스트
    * 별표를 여백 1칸 이상과 사용하면 순서가 없는 리스트
        * 들여쓰기1
            * 들여쓰기2
                * 들여쓰기3
    - (-)를 여백 1칸 이상과 사용하면 순서가 없는 리스트
    - (-)를 여백 1칸 이상과 사용하면 순서가 없는 리스트
    - (-)를 여백 1칸 이상과 사용하면 순서가 없는 리스트
        - 들여쓰기1
            - 들여쓰기2
                - 들여쓰기3
""")
st.write("""
    #### 순서가 있는 리스트
    1. 순서가
    2. 있는
    4. 리스트 - 숫자를 건너 뛰어도 무시하고 순서를 따름
        1. 들여쓰기1
            1. 들여쓰기2 # 1로 시작하지 않으면 들여쓰기는 무시
                1. 들여쓰기3
    1. 순서가
    1. 1로 넣어도
    1. 증가됨
    ### 가로줄
    ---
    (---)
    ___
    (___)
    ### 테이블(표)
    |이름|직업|
    |-----|---|
    |파이썬|백수|
    |자바|일잘러|
""")

# 링크
st.divider()
st.subheader("링크")
l1 = "https://naver.com"
l2 = "https://cdn.pixabay.com/photo/2023/04/08/18/01/flower-7909902_640.jpg"
st.write(f"""
    * [표시할 텍스트](https://naver.com)
    * [표시할 텍스트]({l1})
    * ![이미지에 대한 설명](https://cdn.pixabay.com/photo/2023/04/08/18/01/flower-7909902_640.jpg)
    * ![이미지에 대한 설명]({l2})
    * [![이미지에 대한 설명](https://cdn.pixabay.com/photo/2023/04/08/18/01/flower-7909902_640.jpg)](https://naver.com)
""")

# 인용
st.divider()
st.subheader("인용")
st.write(f"""
    > 무언가 멋진 말 - 유명한 사람


    > 진입장벽은 수익이다 - 어느 코딩 강사

    책이나, 사람말 인용할 때...
    > 인용 첫줄
    > > 인용문 안에 인용임

    #### 코드
    `코드를 나타낼 때 주로 쓰이는 묶음 표시 (한줄)`
    ```
    여러 줄로 코드를 나타내고
    줄바꿈도 반영하고 싶으면...
    print("파이썬!")
    ```
    ```python
    print("파이썬!")
    ```
""")