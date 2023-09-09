
import streamlit as st

# 페이지 기본설정
st.set_page_config (
    page_icon = "☻",
    page_title = "Streamlit_Web",
    # layout = "wide",
)

st.subheader("도큐먼트")

if st.button("app.py 코드 보기"):
    code = '''
# 페이지 컬럼 분할 (예, 부트스트램 컬럼, 그리드)
cols = st.columns((1,1,2))
cols[0].metric("10/11", "15 ℃", "2")
cols[0].metric("10/12", "17 ℃", "2 ℉")
cols[0].metric("10/13", "15 ℃", "2")
cols[1].metric("10/14", "17 ℃", "2 ℉")
cols[1].metric("10/15", "14 ℃", "-3 ℉")
cols[1].metric("10/16", "13 ℃", "-1 ℉")


# 라인 그래프 데이터 생성 (with. Pandas)
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns= ['a', 'b', 'c',]
)

# 컬럼 나머지 부분에 라인차트 생성
cols[2].line_chart(chart_data)
        '''
    st.code(code, language="python")