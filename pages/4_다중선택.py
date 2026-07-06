import streamlit as st

st.header('다중선택')

options = st.multiselect(
     '가장 좋아하는 야구팀은 무엇인가요',
     ['기아타이거즈', '삼성라이온즈', '한화이글스', 'LG트윈스'],
     ['기아타이거즈', '삼성라이온즈'])

st.write('당신이 선택한 색상:', options)
st.header('체크박스')

st.write ('주문하고 싶은 것이 무엇인가요?')

icecream = st.checkbox('아이스크림')
coffee = st.checkbox('커피')
cola = st.checkbox('콜라')

if icecream:
     st.write("좋아요! 여기 더 많은 🍦")

if coffee: 
     st.write("알겠습니다, 여기 커피 있어요 ☕")

if cola:
     st.write("여기 있어요 🥤")
