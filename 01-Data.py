import streamlit as st
import pandas as pd
import numpy as np

st.title('데이터프레임 튜토리얼')

# 생성
dataframe = pd.DataFrame({
    'first column': [1,2,3,4],
    'second column': [10,20,30,40],
})

# 출력
# use_container_width는 데이터프레임을 전체 컨테이너 크기로 확장할 때 사용
st.dataframe(dataframe, use_container_width=False)

# 테이블 (static) : Not interactive (dataframe은 interactive)
st.table(dataframe)

# Metric
st.metric(label="온도", value="10℃", delta="1.2℃")
st.metric(label="삼성전자", value="61,000원", delta="-1,200원")

col1, col2, col3 = st.columns(3)
col1.metric(label="달러USD", value="1,228원", delta="-12.00원")
col2.metric(label="일본JPY(100엔)", value="958.63원", delta="-7.44원")
col3.metric(label="유럽연합EUR", value="1,335.82원", delta="11.44원")
