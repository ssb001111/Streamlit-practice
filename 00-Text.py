import streamlit as st

st.title('이것은 타이틀 입니다')

# emoji
# https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/ 에서 원하는 것 가져다 쓸 수 있음!

st.title('스마일 :sunglasses:')

st.header('헤더를 입력할 수 있어요! :sparkles:')

st.subheader('이것은 subheader 입니다')

st.caption('캡션을 한 번 넣어 보았습니다~')

# Code
sample_code = '''
def function():
    print('hello, world!)
'''
st.code(sample_code, language="python")

st.text('일반적인 텍스트를 입력해 보았습니다')

# Markdown
st.markdown('streamlit은 **마크다운 문법을 지원**합니다')
# Color code : blue, green, orange, red, violet
# https://colored-text.streamlit.app/
st.markdown('텍스트의 색상을 :green[초록색]으로, 그리고 **:blue[파란색]** 볼드체로 설정할 수 있습니다.')
st.markdown(':green[$\sqrt{x^2+y^2}=1$] 와 같이 latex 문법의 수식 표현도 가능합니다.')

st.latex(r'\sqrt{x^2+y^2}=1')
