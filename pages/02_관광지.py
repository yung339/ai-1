import streamlit as st
from streamlit_folium import st_folium
import folium

# --- 페이지 설정 ---
st.set_page_config(page_title="Seoul Top 10 Attractions", layout="wide")

# --- 배경 설정 (핑크색 그라데이션) ---
page_bg = """
<style>
body {
    background: linear-gradient(to bottom right, #ffd6e8, #ffe6f0);
    color: #4a4a4a;
}
h1, h2, h3 {
    color: #e91e63;
    text-align: center;
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# --- 배경음악 (로파이) ---
st.markdown("""
<audio autoplay loop>
  <source src="https://cdn.pixabay.com/download/audio/2023/04/04/audio_9d3a8b3b3f.mp3?filename=lofi-study-112191.mp3" type="audio/mpeg">
</audio>
""", unsafe_allow_html=True)

# --- 관광지 데이터 ---
places = [
    {"name": "경복궁 (Gyeongbokgung Palace)", "lat": 37.579617, "lon": 126.977041},
    {"name": "명동 (Myeongdong Shopping Street)", "lat": 37.563757, "lon": 126.982669},
    {"name": "남산타워 (N Seoul Tower)", "lat": 37.551169, "lon": 126.988227},
    {"name": "북촌 한옥마을 (Bukchon Hanok Village)", "lat": 37.582604, "lon": 126.983998},
    {"name": "홍대 (Hongdae)", "lat": 37.556314, "lon": 126.922016},
    {"name": "이태원 (Itaewon)", "lat": 37.534964, "lon": 126.994906},
    {"name": "잠실 롯데월드타워 (Lotte World Tower)", "lat": 37.5126, "lon": 127.1028},
    {"name": "청계천 (Cheonggyecheon Stream)", "lat": 37.570042, "lon": 126.979596},
    {"name": "동대문디자인플라자 (DDP)", "lat": 37.566484, "lon": 127.009069},
    {"name": "광장시장 (Gwangjang Market)", "lat": 37.570043, "lon": 127.001906},
]

# --- 지도 생성 ---
m = folium.Map(location=[37.5665, 126.9780], zoom_start=12)

for p in places:
    folium.Marker(
        [p["lat"], p["lon"]],
        popup=f"<b>{p['name']}</b>",
        tooltip=p["name"],
        icon=folium.Icon(color="pink", icon="star"),
    ).add_to(m)

# --- 제목 ---
st.title("💖 Foreigners’ Favorite Seoul Attractions (Top 10) 💖")
st.markdown("Explore the most loved spots in Seoul by international visitors!")

# --- 지도 출력 ---
st_folium(m, width=800, height=600)
