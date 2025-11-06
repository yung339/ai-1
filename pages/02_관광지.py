import streamlit as st
from streamlit_folium import st_folium
import folium

# --- 페이지 기본 설정 ---
st.set_page_config(page_title="서울 인기 관광지 TOP10", layout="wide")

# --- 핑크 테마 & 반짝이 효과 CSS ---
page_style = """
<style>
body {
    background: linear-gradient(to bottom right, #ffe4ec, #ffd6e8);
    color: #4a4a4a;
    overflow-x: hidden;
}

/* 제목 스타일 */
h1, h2, h3 {
    color: #e91e63;
    text-align: center;
}

/* 반짝이 효과 */
.sparkle {
    position: fixed;
    top: 0;
    left: 0;
    pointer-events: none;
    z-index: 9999;
}

.sparkle::after {
    content: "✨";
    font-size: 24px;
    position: absolute;
    animation: sparkle-move 1s ease-out forwards;
}

@keyframes sparkle-move {
    0% { transform: translateY(0) scale(1); opacity: 1; }
    100% { transform: translateY(-60px) scale(0.5); opacity: 0; }
}
</style>

<script>
document.addEventListener('click', function(e) {
    const sparkle = document.createElement('div');
    sparkle.classList.add('sparkle');
    sparkle.style.left = e.pageX + 'px';
    sparkle.style.top = e.pageY + 'px';
    document.body.appendChild(sparkle);
    setTimeout(() => sparkle.remove(), 1000);
});
</script>
"""
st.markdown(page_style, unsafe_allow_html=True)

# --- 배경음악 (로파이) ---
st.markdown("""
<audio autoplay loop>
  <source src="https://cdn.pixabay.com/download/audio/2023/04/04/audio_9d3a8b3b3f.mp3?filename=lofi-study-112191.mp3" type="audio/mpeg">
</audio>
""", unsafe_allow_html=True)

# --- 서울 인기 관광지 데이터 ---
places = [
    {"name": "경복궁", "desc": "조선 왕조의 법궁이자 서울의 대표 궁궐입니다.", "lat": 37.579617, "lon": 126.977041},
    {"name": "명동", "desc": "쇼핑과 길거리 음식으로 외국인들에게 인기 있는 명소입니다.", "lat": 37.563757, "lon": 126.982669},
    {"name": "남산타워", "desc": "서울의 랜드마크 전망대, 야경이 아름답습니다.", "lat": 37.551169, "lon": 126.988227},
    {"name": "북촌 한옥마을", "desc": "전통 한옥이 모여 있는 한국 문화 체험지입니다.", "lat": 37.582604, "lon": 126.983998},
    {"name": "홍대", "desc": "젊음의 거리로 유명한 예술과 음악의 중심지입니다.", "lat": 37.556314, "lon": 126.922016},
    {"name": "이태원", "desc": "다양한 나라의 음식과 문화가 공존하는 글로벌 거리입니다.", "lat": 37.534964, "lon": 126.994906},
    {"name": "롯데월드타워", "desc": "123층 초고층 전망대와 쇼핑몰, 한강이 보이는 명소입니다.", "lat": 37.5126, "lon": 127.1028},
    {"name": "청계천", "desc": "도심 속 힐링 산책로로 외국인 관광객에게 인기입니다.", "lat": 37.570042, "lon": 126.979596},
    {"name": "DDP (동대문디자인플라자)", "desc": "미래지향적 건축물로 패션과 디자인 중심지입니다.", "lat": 37.566484, "lon": 127.009069},
    {"name": "광장시장", "desc": "빈대떡, 마약김밥 등 한국 전통 음식을 즐길 수 있는 시장입니다.", "lat": 37.570043, "lon": 127.001906},
]

# --- 지도 생성 ---
m = folium.Map(location=[37.5665, 126.9780], zoom_start=12, tiles="cartodb positron")

for p in places:
    folium.Marker(
        [p["lat"], p["lon"]],
        popup=f"<b>{p['name']}</b><br>{p['desc']}",
        tooltip=p["name"],
        icon=folium.Icon(color="pink", icon="star"),
    ).add_to(m)

# --- 제목 출력 ---
st.title("💖 서울 인기 관광지 TOP 10 💖")
st.markdown("외국인들이 가장 좋아하는 서울의 명소를 만나보세요!")

# --- 지도 출력 ---
st_folium(m, width=800, height=600)
