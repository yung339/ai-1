
import streamlit as st
st.title('나의 첫 웹 서비스 만들기!')
st.write('안녕하세요, 만나서 야르합니다!')

name=st.text_input('이름을 입력하세용~')
if st.button('인사말 생성'):
  st.write(name+'님! 똥먹어!')
st.balloons()
