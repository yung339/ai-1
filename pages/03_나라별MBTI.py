# app.py
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import os
import numpy as np
import streamlit.components.v1 as components

# --- 페이지 설정
st.set_page_config(page_title="💗 국가별 MBTI 분포", page_icon="💗", layout="centered")

# --- 상단에 별도 iframe으로 CSS + JS 삽입 (click-heart, sparkle)
# components.html을 사용하면 JS가 정상적으로 실행됩니다.
html_code = """
<!doctype html>
<html>
<head>
<meta charset="utf-8">
<style>
  /* fullscreen-like container inside iframe */
  :root { --pink-light: #ffeaf2; --pink-mid: #ffcce5; --pink-strong: #ffb6db; }
  html, body { margin:0; padding:0; background: transparent; }
  .overlay {
    position: relative;
    width: 100%;
    height: 260px; /* iframe 높이와 맞춰주세요 */
    pointer-events: none; /* 기본적으로 iframe이 아래 UI를 가리지 않게 */
  }

  /* 반짝이 배경 (visually nice, low opacity) */
  .sparkle {
    position:absolute;
    inset:0;
    background: radial-gradient(circle, rgba(255,255,255,0.85) 8%, transparent 10%) repeat;
    background-size: 120px 120px;
    animation: sparkle 6s linear infinite;
    opacity: 0.18;
    z-index: 1;
    pointer-events: none;
  }
  @keyframes sparkle {
    from { background-position: 0 0; }
    to { background-position: 240px 480px; }
  }

  /* 클릭시 생성되는 하트(iframe 내부) */
  .heart {
    position: absolute;
    font-size: 26px;
    animation: rise 2s ease-out forwards;
    pointer-events: none;
    z-index: 9999;
  }
  @keyframes rise {
    0% { opacity: 1; transform: translateY(0) scale(1); }
    60% { opacity: 0.9; transform: translateY(-60px) scale(1.15); }
    100% { opacity: 0; transform: translateY(-140px) scale(1.4); }
  }

  /* 중앙 하트 (하단 고정) */
  .floating-heart {
    position: absolute;
    left: 50%;
    transform: translateX(-50%);
    bottom: 8px;
    font-size: 30px;
    z-index: 2;
    opacity: 0.9;
    pointer-events: none;
  }
</style>
</head>
<body>
  <div class="overlay" id="overlay">
    <div class="sparkle"></div>
    <div class="floating-heart">💗</div>
  </div>

<script>
(function() {
  // 클릭이벤트: overlay 영역(iframe 내부)에서만 작동
  var overlay = document.getElementById('overlay');
  overlay.addEventListener('click', function(e) {
    var rect = overlay.getBoundingClientRect();
    var x = e.clientX - rect.left;
    var y = e.clientY - rect.top;

    var heart = document.createElement('div');
    heart.className = 'heart';
    heart.style.left = (x - 12) + 'px';
    heart.style.top = (y - 12) + 'px';
    heart.textContent = '💗';
    overlay.appendChild(heart);

    setTimeout(function(){ heart.remove(); }, 2000);
  }, false);
})();
</script>
</body>
</html>
"""

# height는 iframe 높이(px). overlay 높이와 일치시켜 자연스럽게 보이게 함.
components.html(html_code, height=260, scrolling=False)

# --- 타이틀 (Streamlit 텍스트, 핑크 스타일)
st.markdown(
    """
    <div style="text-align:center; font-size:28px; font-weight:800; color:#ff1493; margin-top:6px;">
      💗 국가별 MBTI 분포 (핑크 반짝이 테마)
    </div>
    """,
    unsafe_allow_html=True,
)

# --- 데이터 로드
DATA_FILE = "countriesMBTI_16types.csv"
if not os.path.exists(DATA_FILE):
    st.error(f"데이터 파일 '{DATA_FILE}'를 찾을 수 없습니다. 프로젝트 루트에 CSV 파일을 업로드해 주세요.")
    st.stop()

try:
    df = pd.read_csv(DATA_FILE)
except Exception as e:
    st.error(f"CSV 파일 로드 중 오류: {e}")
    st.stop()

# 필수 컬럼 검사
expected_mbti = ['INFJ','ISFJ','INTP','ISFP','ENTP','INFP','ENTJ','ISTP',
                 'INTJ','ESFP','ESTJ','ENFP','ESTP','ISTJ','ENFJ','ESFJ']
if 'Country' not in df.columns:
    st.error("CSV에 'Country' 컬럼이 필요합니다.")
    st.stop()
missing = [c for c in expected_mbti if c not in df.columns]
if missing:
    st.error(f"CSV에 아래 MBTI 컬럼들이 필요합니다: {', '.join(missing)}")
    st.stop()

# 인덱스 설정
df = df.set_index('Country').sort_index()

# --- 사이드바 컨트롤
st.sidebar.header("🎀 설정")
country = st.sidebar.selectbox("국가 선택", df.index.tolist())
sort_desc = st.sidebar.checkbox("막대 정렬: 내림차순", value=True)
show_values = st.sidebar.checkbox("막대 위에 값 표시", value=True)
st.sidebar.markdown("---")
st.sidebar.markdown("💗 핑크테마 · 클릭으로 하트 뜸")

# --- 선택 국가 데이터 준비
row = df.loc[country, expected_mbti].astype(float)
total = row.sum()
# 데이터가 0~1인지 확실하지 않으므로 정규화(합=1) 처리 (0이면 그대로)
if total > 0:
    vals = row / total
else:
    vals = row.copy()

if sort_desc:
    vals = vals.sort_values(ascending=False)

# --- 색상 그라데이션 생성 (핑크톤) + 1등 강조
def make_gradient(start_hex: str, end_hex: str, steps: int):
    def hex_to_rgb(h):
        h = h.lstrip('#')
        return tuple(int(h[i:i+2], 16) for i in (0,2,4))
    def rgb_to_hex(rgb):
        return '#{:02x}{:02x}{:02x}'.format(*rgb)
    s_rgb = hex_to_rgb(start_hex)
    e_rgb = hex_to_rgb(end_hex)
    grad = []
    if steps == 1:
        return [rgb_to_hex(s_rgb)]
    for i, t in enumerate(np.linspace(0, 1, steps)):
        rgb = tuple(int(round(s_rgb[j] + (e_rgb[j] - s_rgb[j]) * t)) for j in range(3))
        grad.append(rgb_to_hex(rgb))
    return grad

n = len(vals)
gradient = make_gradient("#ffe6f2", "#ff66b2", n)
# 강조 색: 진한 핑크
if n > 0:
    gradient[0] = "#ff1493"  # 1등이 정렬상 첫번째일 때 강조
# 만약 정렬을 off 였고 1등을 원래 위치에 강조하고 싶으면 아래 로직 필요
if not sort_desc:
    # find original max index and set that position in colors red
    max_idx = int(row.idxmax() and list(vals.index).index(row.idxmax()))
    # recompute gradient in original order
    gradient = make_gradient("#ffe6f2", "#ff66b2", n)
    gradient[max_idx] = "#ff1493"

# --- Plotly 막대그래프 (가로)
fig = go.Figure(
    go.Bar(
        x=vals.values,
        y=vals.index,
        orientation='h',
        marker=dict(color=gradient, line=dict(color='rgba(0,0,0,0)', width=0)),
        text=[f"{v*100:.2f}%" for v in vals] if show_values else None,
        textposition='outside' if show_values else None,
        hovertemplate="%{y}: %{x:.2%}<extra></extra>"
    )
)

fig.update_layout(
    title=dict(text=f"💗 {country}의 MBTI 분포", x=0.01, xanchor='left', font=dict(color="#ff1493", size=20)),
    xaxis=dict(title="비율 (%)", tickformat='.0%', color="#ff66b2"),
    yaxis=dict(autorange='reversed', color="#ff66b2"),
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    font=dict(color="#d63384"),
    margin=dict(l=120, r=30, t=70, b=30),
    height=520
)

st.plotly_chart(fig, use_container_width=True)

# --- 요약 정보
st.markdown("---")
col1, col2 = st.columns([2,3])
with col1:
    st.markdown("**선택 국가**")
    st.write(country)
    st.markdown("**원시 합계**")
    st.write(f"{total:.6f}")
with col2:
    st.markdown("**상위 3개 MBTI**")
    top3 = vals.head(3)
    for i, (m, v) in enumerate(top3.items(), start=1):
        st.write(f"{i}. {m} — {v*100:.2f}%")

# --- (추가) 사용자가 iframe 바깥을 클릭해도 반응하길 원하면 브라우저 보안/구조상 제한이 있어 불가능합니다.
# 마지막 안내문
st.markdown(
    """
    <div style="color:#d63384; font-size:12px; margin-top:8px;">
      ⚠️ 참고: '하트 떠오르기' 애니메이션은 보안상 Streamlit의 메인 DOM에 직접 스크립트를 주입할 수 없어서
      상단의 iframe(작동 영역) 내부에서 실행됩니다. 페이지 상단 영역(iframe 높이) 내부를 클릭하면 하트가 뜹니다.
    </div>
    """,
    unsafe_allow_html=True
)


