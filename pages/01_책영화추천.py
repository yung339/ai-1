import streamlit as st

# 페이지 설정 (반드시 최상단)
st.set_page_config(page_title="MBTI 책 & 영화 추천 💫", page_icon="📚", layout="centered")

# ----- HTML/CSS/JS (정리된 버전) -----
decor_html = """
<style>
/* 페이지 배경: 핑크 그라데이션 */
html, body {
    background: linear-gradient(135deg, #ffd1dc 0%, #ffe6f2 50%, #fff0f6 100%);
    height: 100%;
    margin: 0;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial;
}

/* 하트 컨테이너는 pointer-events none 해서 인터랙션 방해하지 않음 */
#hearts {
    position: fixed;
    left: 0;
    top: 0;
    width: 100vw;
    height: 100vh;
    pointer-events: none;
    overflow: hidden;
    z-index: 0;
}

/* 하트 애니메이션 */
@keyframes floatHearts {
    0% { transform: translateY(110vh) scale(0.5); opacity: 0; }
    10% { opacity: 1; }
    100% { transform: translateY(-20vh) scale(1.1); opacity: 0; }
}
.heart {
    position: absolute;
    font-size: 28px;
    will-change: transform, opacity;
    filter: drop-shadow(0 4px 6px rgba(0,0,0,0.08));
}

/* 스파클(반짝이) 스타일 */
.sparkle {
    position: absolute;
    font-size: 26px;
    pointer-events: none;
    animation: sparkleFade 800ms forwards;
    transform-origin: center;
    z-index: 9999;
}
@keyframes sparkleFade {
    0% { opacity: 1; transform: scale(0.6) translateY(0px); }
    100% { opacity: 0; transform: scale(1.6) translateY(-30px); }
}

/* Streamlit 컨텐츠가 위로 올라오게 (z-index) */
[data-testid="stAppViewContainer"] > div {
    position: relative;
    z-index: 1;
}
</style>

<div id="hearts"></div>

<script>
/* 하트 무한 생성 */
const heartColors = ["#ff99cc", "#ff66b2", "#ffb6c1", "#ff80bf"];
function createHeart() {
    const container = document.getElementById("hearts");
    if (!container) return;
    const heart = document.createElement("div");
    heart.className = "heart";
    heart.innerText = "💗";
    // 랜덤 위치와 크기, 애니메이션 속도
    const left = Math.random() * 100; // vw
    const size = 18 + Math.random() * 22; // px
    const duration = 4 + Math.random() * 4; // s
    heart.style.left = left + "vw";
    heart.style.fontSize = size + "px";
    heart.style.color = heartColors[Math.floor(Math.random() * heartColors.length)];
    heart.style.animation = `floatHearts ${duration}s linear forwards`;
    container.appendChild(heart);
    // 제거 타이밍: duration(초) + 여유
    setTimeout(() => { heart.remove(); }, (duration + 0.5) * 1000);
}
// 간격을 조금 랜덤하게 하여 자연스럽게
setInterval(createHeart, 700);

/* 스파클: 클릭한 위치에 반짝이 추가 */
function makeSparkle(x, y) {
    const sparkle = document.createElement("div");
    sparkle.className = "sparkle";
    sparkle.innerText = "✨";
    // 약간의 위치 보정 (중앙 정렬)
    sparkle.style.left = (x - 12) + "px";
    sparkle.style.top = (y - 12) + "px";
    document.body.appendChild(sparkle);
    setTimeout(() => sparkle.remove(), 900);
}
// 화면 클릭/터치 이벤트에 반짝이 연결
document.addEventListener('click', function(e){
    // 클릭 좌표를 사용
    makeSparkle(e.clientX, e.clientY);
});
document.addEventListener('touchstart', function(e){
    const t = e.touches[0];
    if (t) makeSparkle(t.clientX, t.clientY);
});
</script>

<!-- 배경음: 자동 재생이 브라우저 정책에 의해 차단될 수 있음.
     재생 차단 시 사용자가 화면을 한 번 클릭하면 재생될 가능성이 높음. -->
<audio id="bgm" autoplay loop>
  <source src="https://cdn.pixabay.com/download/audio/2023/03/15/audio_9e17ffb7ee.mp3?filename=lofi-study-112191.mp3" type="audio/mp3">
  <!-- 대체 텍스트 없음 -->
</audio>
"""

# 위 HTML/CSS/JS 주입
st.markdown(decor_html, unsafe_allow_html=True)

# ----- Streamlit 컨텐츠 -----
st.markdown("<h1 style='text-align:center; margin-top:20px;'>✨ MBTI로 알아보는 나에게 딱 맞는 책 & 영화 추천 💫</h1>", unsafe_allow_html=True)
st.write("너의 성격 유형(MBTI)을 골라줘! 반짝이는 추천 가져올게 💖")

mbti_list = [
    "ISTJ", "ISFJ", "INFJ", "INTJ",
    "ISTP", "ISFP", "INFP", "INTP",
    "ESTP", "ESFP", "ENFP", "ENTP",
    "ESTJ", "ESFJ", "ENFJ", "ENTJ"
]

user_mbti = st.selectbox("👉 내 MBTI는...", mbti_list)

recommendations = {
    "ISTJ": {"books": ["『미움받을 용기』", "『원칙』"], "movies": ["셜록 홈즈 🕵️‍♂️", "인셉션 🌀"]},
    "ISFJ": {"books": ["『작은 아씨들』", "『비밀의 화원』"], "movies": ["업 🎈", "겨울왕국 ❄️"]},
    "INFJ": {"books": ["『데미안』", "『이기적 유전자』"], "movies": ["인사이드 아웃 💭", "어바웃 타임 ⏰"]},
    "INTJ": {"books": ["『총, 균, 쇠』", "Thinking, Fast and Slow"], "movies": ["인터스텔라 🚀", "아이언맨 🤖"]},
    "ISTP": {"books": ["『나미야 잡화점의 기적』", "『셜록 홈즈 단편집』"], "movies": ["분노의 질주 🚗", "킹스맨 🕶️"]},
    "ISFP": {"books": ["『아몬드』", "『너에게 가는 속도 493km』"], "movies": ["라라랜드 🎵", "위대한 쇼맨 🎪"]},
    "INFP": {"books": ["『달러구트 꿈 백화점』", "『연의 편지』"], "movies": ["월-E 🤖", "라이언 일병 구하기 🎖️"]},
    "INTP": {"books": ["『호모 데우스』", "『문명과 수학』"], "movies": ["매트릭스 🕶️", "테넷 ⏳"]},
    "ESTP": {"books": ["『죽은 시인의 사회』", "『나는 나로 살기로 했다』"], "movies": ["탑건 ✈️", "미션 임파서블 💥"]},
    "ESFP": {"books": ["『그냥 흘러넘쳐도 좋아』", "『어쩌면 별들이 너의 슬픔을 가져갈지도 몰라』"], "movies": ["맘마미아 🎤", "주토피아 🦊"]},
    "ENFP": {"books": ["『모든 순간이 너였다』", "『하루 3분 마음챙김』"], "movies": ["소울 🎷", "라따뚜이 🐭"]},
    "ENTP": {"books": ["『생각의 탄생』", "『크리에이티브 스테이트』"], "movies": ["조커 🃏", "아이언맨 🤖"]},
    "ESTJ": {"books": ["『7가지 습관』", "『성공하는 사람들의 조건』"], "movies": ["머니볼 ⚾", "설국열차 🚆"]},
    "ESFJ": {"books": ["『언어의 온도』", "『좋은 사람에게만 좋은 사람이면 돼』"], "movies": ["인턴 👔", "인사이드 아웃 💭"]},
    "ENFJ": {"books": ["『미라클 모닝』", "『어린왕자』"], "movies": ["포레스트 검프 🏃‍♂️", "해리포터 🪄"]},
    "ENTJ": {"books": ["『나폴레온 힐 성공의 법칙』", "『제로 투 원』"], "movies": ["다크 나이트 🦇", "인터스텔라 🚀"]}
}

if user_mbti:
    rec = recommendations.get(user_mbti, None)
    if rec:
        st.markdown(f"<h3 style='text-align:center;'>💫 {user_mbti} 유형에게 딱 어울리는 추천 💫</h3>", unsafe_allow_html=True)
        st.write(f"📚 **책 추천:** {rec['books'][0]}  /  {rec['books'][1]}")
        st.write(f"🎬 **영화 추천:** {rec['movies'][0]}  /  {rec['movies'][1]}")
        st.success("✨ 마음에 드는 게 있으면 찾아봐! 완전 너에게 찰떡일걸 😎")

# 하단 꽃 이모지 고정 (Streamlit 컨텐츠 내부)
st.markdown("<div style='text-align:center; margin-top:18px; font-size:28px;'>🌷 🌸 🌼 🌺 🌻</div>", unsafe_allow_html=True)
st.caption("💖 made with love and sparkle ✨ by ChatGPT 🌸")
