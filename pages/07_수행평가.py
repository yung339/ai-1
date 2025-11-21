# requirements.txt
streamlit
plotly
pandas

--- 여기서부터 app.py ---
import streamlit as st
import plotly.express as px
import pandas as pd

# ------- 기본 설정 (핑크 그라데이션 + 귀여운 폰트) -------
st.set_page_config(page_title="제과·제빵 시장 분석", page_icon="🍞", layout="wide")

custom_css = """
<style>
body {
    background: linear-gradient(135deg, #ffe0f0, #ffb3d9, #ff99cc);
    font-family: 'Comic Sans MS', 'Cute Font', cursive !important;
}

h1, h2, h3, h4, h5, h6, p, div, span {
    font-family: 'Comic Sans MS', 'Cute Font', cursive !important;
}

</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# ------- 더미 데이터 -------
data = {
    "연도": [2019, 2020, 2021, 2022, 2023],
    "시장규모": [43000, 45500, 48000, 52000, 56000],
}

category_data = pd.DataFrame({
    "카테고리": ["빵", "케이크", "쿠키", "파이", "기타"],
    "매출": [40, 25, 15, 10, 10],
})

trend_keywords = [
    ("고단백", 35),
    ("저당", 28),
    ("비건", 22),
    ("프리미엄", 18),
    ("간편식", 12),
]

# ------- 페이지 타이틀 -------
st.title("🍰 국내 제과·제빵 시장 분석 대시보드")
st.markdown("### 💗 식품산업통계 기반 자동 분석 페이지 💗")

# ------- 시장 규모 변화 -------
st.subheader("📈 연도별 시장 규모 변화")
df = pd.DataFrame(data)
fig = px.line(df, x="연도", y="시장규모", markers=True, title="시장 규모 변화")
st.plotly_chart(fig, use_container_width=True)

# ------- 카테고리 매출 비중 -------
st.subheader("🥯 카테고리별 매출 비중")
fig2 = px.pie(category_data, names="카테고리", values="매출", hole=0.35,
               title="카테고리 비중")
st.plotly_chart(fig2, use_container_width=True)

# ------- 자동 분석 -------
st.subheader("🔥 가장 성장한 카테고리 분석")
st.success(f"✨ 현재 가장 매출 비중이 높은 카테고리는 **{category_data.loc[0, '카테고리']}** 입니다! ✨")

# ------- 트렌드 키워드 -------
st.subheader("🔍 제과·제빵 트렌드 키워드 분석")
for keyword, score in trend_keywords:
    st.write(f"🍓 **{keyword}** — 관심도 {score}%")

st.markdown("<h3 style='text-align:center;'>💗💗💗</h3>", unsafe_allow_html=True)
