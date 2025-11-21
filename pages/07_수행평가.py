import streamlit as st
import plotly.express as px
import pandas as pd

st.set_page_config(page_title="제과·제빵 시장 분석", page_icon="🍞", layout="wide")

# 데이터 생성
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

st.title("🍰 국내 제과·제빵 시장 분석 대시보드")
st.markdown("### 식품산업통계 기반 자동 분석 페이지")

st.subheader("📈 연도별 시장 규모 변화")
df = pd.DataFrame(data)
fig = px.line(df, x="연도", y="시장규모", markers=True)
st.plotly_chart(fig, use_container_width=True)

st.subheader("🥯 카테고리별 매출 비중")
fig2 = px.pie(category_data, names="카테고리", values="매출", hole=0.3)
st.plotly_chart(fig2, use_container_width=True)

st.subheader("🔥 가장 성장한 카테고리 분석")
st.success(f"가장 높은 매출 비중을 가진 카테고리는 **{category_data.loc[0, '카테고리']}** 입니다!")

st.subheader("🔍 제과·제빵 트렌드 키워드")
for keyword, score in trend_keywords:
    st.write(f"💡 **{keyword}** — 관심도 {score}%")

st.markdown("<h3 style='text-align:center;'>💗💗💗</h3>", unsafe_allow_html=True)

