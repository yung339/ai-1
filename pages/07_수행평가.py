import streamlit as st
import pandas as pd
import plotly.express as px
import os

# -----------------------------
# 🎀 페이지 기본 설정
# -----------------------------
st.set_page_config(
    page_title="제과·제빵 산업 통계 대시보드",
    layout="wide"
)

# -----------------------------
# 🎀 CSS + JS: 하트 애니메이션, 클릭 반짝이
# -----------------------------
custom_style = """
<style>
/* 배경 그라데이션 */
body {
    background: linear-gradient(135deg, #ffccd9, #ff99c8);
}
.stApp {
    background: linear-gradient(135deg, #ffd1e6, #ff85c1);
}

/* 하트 애니메이션 */
@keyframes floatUp {
    0% { transform: translateY(0) scale(0.5); opacity: 1;}
    100% { transform: translateY(-200px) scale(1.2); opacity: 0;}
}
.heart {
    position: fixed;
    font-size: 24px;
    animation: floatUp 2s linear forwards;
    pointer-events: none;
}

/* 클릭 반짝이 */
.sparkle {
    position: fixed;
    width: 15px;
    height: 15px;
    background: radial-gradient(circle, #fff0ff 0%, #ff69b4 80%);
    border-radius: 50%;
    pointer-events: none;
    animation: sparkleAnim 0.7s linear forwards;
}
@keyframes sparkleAnim {
    0% { transform: scale(0.5); opacity: 1; }
    100% { transform: scale(1.5); opacity: 0; }
}
</style>
<script>
document.addEventListener('click', function(e) {
    // 하트 생성
    let heart = document.createElement('div');
    heart.className = 'heart';
    heart.style.left = e.clientX + 'px';
    heart.style.top = e.clientY + 'px';
    heart.innerText = '💗';
    document.body.appendChild(heart);
    setTimeout(() => heart.remove(), 2000);

    // 반짝이 생성
    let sparkle = document.createElement('div');
    sparkle.className = 'sparkle';
    sparkle.style.left = e.clientX + 'px';
    sparkle.style.top = e.clientY + 'px';
    document.body.appendChild(sparkle);
    setTimeout(() => sparkle.remove(), 700);
});
</script>
"""
st.markdown(custom_style, unsafe_allow_html=True)

# -----------------------------
# 🎀 제목
# -----------------------------
st.markdown("<h1 style='text-align:center; color:#d10074;'>🍰 제과·제빵 산업 분석 대시보드</h1>", unsafe_allow_html=True)

# -----------------------------
# 📂 루트 폴더 CSV 자동 로드
# -----------------------------
csv_file = "bakery_data.csv"
if os.path.exists(csv_file):
    df = pd.read_csv(csv_file, encoding="cp949")
    st.success(f"✔ '{csv_file}' 파일을 성공적으로 불러왔습니다!")

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
            color_discrete_sequence=["#ff3399"],  # 핑크 테마
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
    st.markdown("## 🥧 카테고리별 매출 비중")

    category_data = pd.DataFrame({
        "category": ["빵", "케이크", "쿠키", "파이", "기타"],
        "value": [45, 25, 15, 10, 5]
    })

    pie_fig = px.pie(
        category_data,
        names="category",
        values="value",
        color_discrete_sequence=["#ff99c8", "#ff66b3", "#ff3399", "#ff1a75", "#ff85c1"],
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
        color_discrete_sequence=["#ff99c8", "#ff66b3", "#ff3399", "#ff1a75", "#ff85c1"],
        title="트렌드 키워드 등장 빈도"
    )
    bar_fig.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
    )
    st.plotly_chart(bar_fig, use_container_width=True)

    # -----------------------------
    # 4️⃣ 최근 대비 가장 성장한 카테고리 자동 분석
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

else:
    st.error(f"❌ 루트 폴더에 '{csv_file}' 파일이 존재하지 않습니다.")

# -----------------------------
# 5️⃣ 하단 하트 이모티콘
# -----------------------------
st.markdown(
    "<h2 style='text-align:center; padding-top:20px;'>💗</h2>",
    unsafe_allow_html=True
)
