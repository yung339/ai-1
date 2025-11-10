import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# 🌸 페이지 설정
st.set_page_config(page_title="Lovely Pink Population Viewer 💕", layout="wide")

# 🌸 CSS + JS (핑크 배경 + 하트 이펙트 + 귀여운 폰트)
st.markdown("""
    <style>
    /* 💕 구글 폰트 불러오기 */
    @import url('https://fonts.googleapis.com/css2?family=Jua&display=swap');

    html, body, [class*="css"] {
        background: linear-gradient(180deg, #ffd6eb, #ffe6f2, #fff0f6);
        color: #d63384;
        font-family: 'Jua', sans-serif;
    }

    h1, h2, h3, h4, h5, h6 {
        font-family: 'Jua', sans-serif;
        font-weight: bold;
        color: #ff1493;
        text-shadow: 1px 1px 3px #ffb6c1;
    }

    /* 하트 떠다니는 애니메이션 */
    @keyframes float {
        0% { transform: translateY(0); opacity: 1; }
        100% { transform: translateY(-100vh); opacity: 0; }
    }

    .heart {
        position: fixed;
        bottom: 0;
        font-size: 24px;
        animation: float 4s linear infinite;
        z-index: 9999;
        pointer-events: none;
    }
    </style>

    <script>
    document.addEventListener('click', function(e) {
        let heart = document.createElement('div');
        heart.classList.add('heart');
        heart.style.left = e.pageX + 'px';
        heart.style.top = e.pageY + 'px';
        heart.style.color = '#ff4da6';
        heart.innerHTML = '💖';
        document.body.appendChild(heart);
        setTimeout(() => { heart.remove(); }, 2000);
    });
    </script>
""", unsafe_allow_html=True)

# 🌸 데이터 불러오기
@st.cache_data
def load_data():
    df = pd.read_csv("population.csv", encoding="cp949")
    return df

df = load_data()

# 🌸 지역구 선택
region_col = df.columns[0]
regions = sorted(df[region_col].dropna().unique())
selected_region = st.selectbox("🌸 지역구를 선택하세요:", regions)

# 🌸 선택된 지역 데이터
region_data = df[df[region_col] == selected_region]

# 🌸 '나이' 또는 숫자 형태의 컬럼 찾기
age_cols = [c for c in df.columns if '나이' in c or '연령' in c or str(c).isdigit()]
if len(age_cols) == 0:
    st.warning("⚠️ 나이 관련 열이 없어요. CSV를 확인해주세요.")
else:
    x = age_cols
    y = region_data[age_cols].values.flatten()

    # Plotly 그래프 (진한 핑크 꺾은선)
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=x,
        y=y,
        mode='lines+markers',
        line=dict(color='#ff1493', width=4),
        marker=dict(size=7, color='#ff80bf'),
        hovertemplate='나이 %{x}세<br>인구 %{y:,}명'
    ))

    fig.update_layout(
        title=f"💗 {selected_region} 나이별 인구 분포",
        xaxis_title="나이",
        yaxis_title="인구수",
        template="simple_white",
        plot_bgcolor="#fff0f6",
        paper_bgcolor="#fff0f6",
        font=dict(color="#d63384", size=16, family="Jua, sans-serif"),
    )

    st.plotly_chart(fig, use_container_width=True)

# 🌸 하단 하트 꾸밈
st.markdown("""
    <div style="text-align:center; font-size:30px; animation: float 10s linear infinite;">
        💕 💗 💖 💞 💓 💘
    </div>
""", unsafe_allow_html=True)
