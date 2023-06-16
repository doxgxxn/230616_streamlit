# streamlit run app.py

import streamlit as st
st.title("프로필 만들기")

st.header("")
st.header("")
st.header("")
st.header("")


cols = st.columns(3)
col1, col2, col3 = cols
with col2:
    st.image("img/cat.jpeg", width=300, caption="사진을 업로드하세요")




name = st.text_input("이름을 입력하세요!")
st.write("---")

co1,co2,co3 = st.columns(3)

if name != '':
     with co2:
        st.subheader(name+ '님의 정보')

age = st.slider(f'{name}님의 나이', 1, 80)
c1,c2,c3,c4 = st.columns(4)
with c2:
    if age < 20:
        st.image("img/young.jpg", width= 400, caption="너무 어리구나")
    elif age >60:
        st.image("img/old.jpeg", width= 400, caption="어르신,,")
belt ={4:"쥐",
       3:"소",
       2:"호랑이",
       1:"토끼",
       0:"용",
       11:"뱀",
       10:"말",
       9:"양",
       8:"원숭이",
       7:"닭",
       6:"개",
       5:"돼지"}
w_belt = belt[age%12]

st.markdown(f"<h3 style='text-align: center; color: black;'>당신은 {w_belt}띠 입니다!</h1>", unsafe_allow_html=True)
# st.write(f"당신은 **{w_belt}띠** 입니다!")

adress = st.text_input(f'{name}님의 주소를 입력하세요',max_chars=10)
st.subheader(adress)

language = ['운동', '영화감상', '음악듣기', '산책하기', '자기']
st.multiselect(f'{name}님의 취미를 선택하세요. 복수 선택 가능', language)

my_date = st.date_input('약속 날짜')
my_time = st.time_input('시간을 선택하세요',key=30)
day = my_date.strftime('%a')


st.markdown(f"<h3 style='text-align: center; color: grey;'>{my_date}일 {day} {my_time}에 만나요</h1>", unsafe_allow_html=True)