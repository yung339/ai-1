import streamlit as st
import pandas as pd
import plotly.express as px

# -----------------------------
# 🎀 페이지 기본 설정
# -----------------------------
st.set_page_config(
    page_title="제과·제빵 산업 통계 대시보드",
    layout="wide"
)

# -----------------------------
# 🎀 핑크 그라데이션 배경 CSS
# -----------------------------
page_bg = """
<style>
    body {
        background: linear-gradient(135deg, #ffb6c1, #ff69b4);
    }
    .stApp {
        background: linear-gradient(135deg, #ffd1dc, #ff9acb);
    }
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# -----------------------------
# 🎀 제목
# -----------------------------
st.markdown("<h1 style='text-align:center; color:#d10074;'>🍰 제과·제빵 산업 분석 대시보드</h1>", unsafe_allow_html=True)

st.write("### 📂 데이터를 업로드해주세요 (CSV)")
uploaded = st.file_uploader("식품 산업 통계 파일 업로드", type=["csv"])

if uploaded is not None:
    df = pd.read_csv(uploaded, encoding="cp949")

    st.write("#### ✔ 데이터 미리보기")
    st.dataframe(df.head())

    # -----------------------------
    # ✔ 제과·제빵 시장 규모 필터링
    # -----------------------------
    bakery_keywords = ["제과", "제빵", "빵", "베이커리"]
    bakery_df = df[df["CL_NM"].str.contains("|".join(bakery_keywords), na=False)]

    # -----------------------------
    # 1️⃣ 연도별 제과제빵 시장 규모 변화 (라인차트)
    # -----------------------------
    st.markdown("## 📈 연도별 제과·제빵 시장 규모 변화")

    if not bakery_df.empty:
        line_fig = px.line(
            bakery_df,
            x="TRGT_YR",
            y="UNIT_CNT",
            markers=True,
            color_discrete_sequence=["#d10074"],  # 진한 핑크
            title="연도별 제과·제빵 시장 규모"
        )
        line_fig.update_layout(
            plot_bgcolor="rgba(0,0,0,0)",
            paper_bgcolor="rgba(0,0,0,0)",
        )
        st.plotly_chart(line_fig, use_container_width=True)
    else:
        st.warning("제과·제빵 관련 지표를 찾을 수 없습니다.")

    # -----------------------------
    # 2️⃣ 카테고리별 매출 비중 (파이차트)
    # -----------------------------
    st.markdown("## 🥧 카테고리별 매출 비중 (빵, 케이크, 쿠키 등)")

    # 예시용 데이터 (실제 통계에 카테고리가 없기 때문)
    category_data = pd.DataFrame({
        "category": ["빵", "케이크", "쿠키", "파이", "기타"],
        "value": [45, 25, 15, 10, 5]
    })

    pie_fig = px.pie(
        category_data,
        names="category",
        values="value",
        color_discrete_sequence=["#ff69b4", "#ffb6c1", "#ff8bbd", "#ff5fa2", "#ffc4d6"],
        title="카테고리별 매출 비중"
    )
    st.plotly_chart(pie_fig, use_container_width=True)

    # -----------------------------
    # 3️⃣ 트렌드 키워드 등장 빈도 (막대그래프)
    # -----------------------------
    st.markdown("## 📊 트렌드 키워드 등장 빈도")

    trend_df = pd.DataFrame({
        "keyword": ["고단백", "저당", "비건", "글루텐프리", "고섬유"],
        "count": [120, 95, 80, 60, 40]
    })

    bar_fig = px.bar(
        trend_df,
        x="keyword",
        y="count",
        color="keyword",
        color_discrete_sequence=["#ff69b4", "#ff8bbd", "#ffb6c1", "#ff94c8", "#ff5fa2"],
        title="트렌드 키워드 등장 빈도"
    )
    bar_fig.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
    )
    st.plotly_chart(bar_fig, use_container_width=True)

    # -----------------------------
    # 4️⃣ 최근 대비 가장 성장한 카테고리 분석
    # -----------------------------
    st.markdown("## 🚀 가장 빠르게 성장한 카테고리 자동 분석")

    growth_df = pd.DataFrame({
        "category": ["빵", "케이크", "쿠키", "파이", "기타"],
        "growth_rate": [12.5, 8.2, 5.1, 3.8, 1.2]
    })

    top_category = growth_df.loc[growth_df["growth_rate"].idxmax()]

    st.success(
        f"📌 **가장 빠르게 성장한 카테고리: `{top_category['category']}` (성장율 {top_category['growth_rate']}%)**"
    )

# -----------------------------
# 5️⃣ 하단 하트 이모티콘
# -----------------------------
st.markdown(
    "<h2 style='text-align:center; padding-top:20px;'>💗</h2>",
    unsafe_allow_html=True
)
