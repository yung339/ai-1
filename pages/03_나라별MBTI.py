import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import os

# -----------------------
# 페이지 설정 & 테마 스타일
# -----------------------
st.set_page_config(page_title="💗 국가별 MBTI 분포", page_icon="💗", layout="centered")

# 핑크 톤 스타일
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #ffeef6 0%, #ffd7ec 50%, #ffb6db 100%);
        color: #d63384;
        font-family: "Segoe UI", Roboto, "Helvetica Neue", Arial;
    }
    .big-title {
        font-size:30px;
        font-weight:800;
        color:#ff1493;
        text-align:center;
        margin-top:10px;
        margin-bottom:20px;
    }
    .floating-heart {
        position: fixed;
        bottom: 15px;
        left: 50%;
        transform: translateX(-50%);
        font-size: 34px;
        z-index: 9999;
        animation: float 2s ease-in-out infinite;
    }
    @keyframes float {
        0% { transform: translateX(-50%) translateY(0); }
        50% { transform: translateX(-50%) translateY(-10px); }
        100% { transform: translateX(-50%) translateY(0); }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="big-title">💗 국가별 MBTI 분포 (핑크 테마)</div>', unsafe_allow_html=True)

# -----------------------
# 데이터 로드
# -----------------------
DATA_FILE = "countriesMBTI_16types.csv"

if not os.path.exists(DATA_FILE):
    st.error(f"데이터 파일 '{DATA_FILE}'를 찾을 수 없습니다. CSV를 같은 폴더에 업로드해주세요.")
    st.stop()

df = pd.read_csv(DATA_FILE)
df = df.set_index("Country")

# MBTI 컬럼 목록
mbti_cols = [
    "INFJ", "ISFJ", "INTP", "ISFP", "ENTP", "INFP", "ENTJ", "ISTP",
    "INTJ", "ESFP", "ESTJ", "ENFP", "ESTP", "ISTJ", "ENFJ", "ESFJ"
]

# -----------------------
# 사이드바
# -----------------------
st.sidebar.header("🎀 설정")
country = st.sidebar.selectbox("국가 선택", df.index)
sort_desc = st.sidebar.checkbox("막대 정렬: 내림차순", value=True)
show_values = st.sidebar.checkbox("막대 위에 값 표시", value=True)
st.sidebar.markdown("---")
st.sidebar.markdown("💗 핑크테마 모드 💗")

# -----------------------
# 선택 국가 데이터
# -----------------------
values = df.loc[country, mbti_cols].astype(float)
if sort_desc:
    values = values.sort_values(ascending=False)

# -----------------------
# 색상: 핑크 그라데이션 + 1등 진한 핑크
# -----------------------
def make_gradient(start_hex, end_hex, steps):
    import colorsys
    import numpy as np
    def hex_to_rgb(h):
        h = h.lstrip("#")
        return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
    def rgb_to_hex(rgb):
        return "#%02x%02x%02x" % rgb

    s = np.linspace(0, 1, steps)
    start_rgb = hex_to_rgb(start_hex)
    end_rgb = hex_to_rgb(end_hex)
    grad = []
    for t in s:
        rgb = tuple(int(start_rgb[i] + (end_rgb[i] - start_rgb[i]) * t) for i in range(3))
        grad.append(rgb_to_hex(rgb))
    return grad

colors = make_gradient("#ffd6ec", "#ff80bf", len(values))
colors[0] = "#ff1493"  # 1등 진한 핑크 강조

# -----------------------
# Plotly 그래프
# -----------------------
fig = go.Figure(
    go.Bar(
        x=values.values,
        y=values.index,
        orientation="h",
        marker=dict(color=colors),
        text=[f"{v*100:.2f}%" for v in values] if show_values else None,
        textposition="outside" if show_values else None,
        hovertemplate="%{y}: %{x:.2%}<extra></extra>",
    )
)

fig.update_layout(
    title=f"💗 {country}의 MBTI 분포 💗",
    title_font=dict(color="#ff1493", size=24),
    xaxis_title="비율 (%)",
    xaxis=dict(color="#ff66b2"),
    yaxis=dict(color="#ff66b2", autorange="reversed"),
    plot_bgcolor="rgba(0,0,0,0)",
    paper_bgcolor="rgba(0,0,0,0)",
    font=dict(color="#d63384", size=14),
    margin=dict(l=80, r=30, t=80, b=30),
    height=520,
)

st.plotly_chart(fig, use_container_width=True)

# -----------------------
# 하단 하트 애니메이션
# -----------------------
st.markdown('<div class="floating-heart">💗</div>', unsafe_allow_html=True)
