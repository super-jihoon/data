import streamlit as st

st.header('드롭다운')

option = st.selectbox(
     '가장 좋아하는 야구팀은 무엇인가요?',
     ('기아타이거즈', '삼성라이온즈', '한화이글스'))

st.write('당신이 좋아하는 야구팀은 ', option)
