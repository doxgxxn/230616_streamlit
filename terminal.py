# app.py, main.py, streamlit_app.py, home.py ...
# 리팩토링 -> 코드를 깔끔하고 간명하게 만드는 작업...

# streamlit
import streamlit as st # streamlit 기능묶음(패키지) -> import 불러오고, as ~한 변수명으로 쓰겠다.
# 짧은 별칭(별명) -> 길다보니까 사용성이 낮아져서...
from widget.food_list import get_food_list
from widget.food_detail import get_food_detail

st.title("신대방삼거리 3대맛집")
# streamlit run app.py
# -> 프로젝트 생성 -> 가상환경 (파이썬 관련 설치를 매번 독립적)
# 새로운 프로젝트를 만들면 -> 새롭게 설치
# pip install streamlit

# https://crop-circle.imageonline.co/
# store1 = {
#     "name": "모스키친",
#     "img": "img/s1.png",
#     "star": 5,
#     "desc": "**모스키친**은 신대방삼거리역에 위치한 돈까스 전문점입니다. 이곳의 돈까스는 프리미엄 등심돈까스와 스페셜 등심돈까스 등으로 구성되어 있으며, 특히 스페셜 등심돈까스는 가브리살이 포함되어 더욱 쫄깃한 식감을 제공합니다. 이들 메뉴는 품질에 비해 가격이 매우 합리적이며, 맛있는 음식과 함께 접객이 빠른 서비스로 많은 손님들에게 인기가 있습니다. 최고의 맛을 위해 히말라야 소금에 콕 찍어 와사비를 얹어 먹는 것을 추천합니다."
# }
def make_store(name, img, star, desc, map, link):
    return dict(name=name, img=img, star=star, desc=desc, map=map, link=link)
store1 = make_store(
    "모스키친", "img/s1.png", 5,
    "**모스키친**은 신대방삼거리역에 위치한 돈까스 전문점으로,"\
    "가성비 좋은 고급 돈까스와 빠른 서비스로 인기를 끌고 있습니다."\
    "특히 스페셜 등심돈까스는 가브리살이 포함되어 쫄깃한 식감을 제공하며,"
    "히말라야 소금에 와사비를 얹어 먹는 것을 추천합니다.",
    "img/m1.png",
    "https://naver.me/5JJQDIz0",
)
store2 = make_store(
    "스미비부타동", "img/s2.png", 4,
    "**스미비부타동**은 신대방삼거리역에 위치한 일본식 돼지고기 덮밥(부타동) 전문점으로,"\
    "맛과 양이 풍부하여 혼밥하기 좋은 곳이며, 가격도 합리적이다",
    "img/m2.png",
    "https://naver.me/xfavYBSR",
)
store3 = make_store(
    "미분당", "img/s3.png", 3,
    "**미분당**은 신대방삼거리에 위치한 베트남 음식점으로, 특히 쌀국수로 유명합니다."\
    " 이곳은 베트남 전통 음식인 쌀국수를 한국인의 입맛에 맞게 재해석하였으며,"\
    "일본풍의 분위기와 중국식 상호를 사용하여 다양한 문화와 개성을 지닌 사람들이"\
    "즐길 수 있는 문화 공간을 제공하려는 취지를 가지고 있습니다.",
    "img/m3.png",
    "https://naver.me/5NdqqXJ4",
)
stores = [store1, store2, store3]

# 일종의 딕셔너리 (페이지가 모두 공유하는 딕셔너리)
if 'detail' not in st.session_state:  # key를 확인해서
    st.session_state['detail'] = ""  # 초기값
    st.session_state['map'] = ""  # 초기값
    st.session_state['link'] = ""  # 초기값

# 맛집 리스트
get_food_list(stores)

# 맛집 상세보기
if st.session_state['detail']:  # 초기값의 빈 문자열
    get_food_detail()  # 처음에는 실행하지 않고... 클릭했을 때 반응해서 그려지게