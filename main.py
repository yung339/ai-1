import streamlit as st
st.title('나의 첫 웹 서비스 만들기!')
st.write('안녕하세요, 만나서 야르합니다!')

name=st.text_input('이름을 입력하세용~')
if st.button('인사말 생성'):
  st.write(name+'님! 똥먹어!')
st.balloons()

# mbti_career_app.py
import streamlit as st

# 🌷 페이지 기본 설정
st.set_page_config(page_title="MBTI 진로 추천 🌟", page_icon="💗", layout="centered")

# 💕 핑크 배경 + 다색 하트 + 꽃잎 + 벚꽃 하단 + 로파이 배경음악
lovely_lofi_theme = """
<style>
body {
    background: linear-gradient(135deg, #ffe6f2, #ffd6eb);
    color: #333333;
    overflow-x: hidden;
    position: relative;
    min-height: 100vh;
    padding-bottom: 180px;
}

/* 💖 하트 */
.heart {
    position: fixed;
    font-size: 20px;
    animation: float-up 1.5s ease-out forwards;
    pointer-events: none;
    z-index: 9999;
}
@keyframes float-up {
    0% {opacity: 1; transform: translateY(0) scale(1);}
    100% {opacity: 0; transform: translateY(-80px) scale(1.8);}
}

/* 🌸 꽃잎 */
.flower {
    position: fixed;
    top: -10px;
    font-size: 20px;
    opacity: 0.9;
    animation: fall 6s linear forwards;
    pointer-events: none;
    z-index: 999;
}
@keyframes fall {
    0% {transform: translateY(0) rotate(0deg);}
    100% {transform: translateY(100vh) rotate(360deg);}
}

/* 🌼 하단 배경 꽃 */
.flower-footer {
    position: fixed;
    bottom: 0;
    left: 0;
    width: 100%;
    height: 160px;
    background-image: url('https://cdn.pixabay.com/photo/2017/04/04/17/09/cherry-blossom-2209831_1280.png');
    background-size: contain;
    background-repeat: repeat-x;
    background-position: bottom;
    opacity: 0.9;
    pointer-events: none;
    z-index: 1;
}
</style>

<script>
// 🌈 랜덤 컬러 하트 + 흩날리는 꽃잎
document.addEventListener('click', createHeart);
document.addEventListener('mousemove', (e) => {
    if (Math.random() < 0.04) createHeart(e);
});
setInterval(createFlower, 800);

function createHeart(e) {
    const heart = document.createElement('div');
    heart.className = 'heart';
    const colors = ['💗','💜','❤️','🩷','💕'];
    heart.textContent = colors[Math.floor(Math.random() * colors.length)];
    const x = e ? e.pageX : Math.random() * window.innerWidth;
    const y = e ? e.pageY : Math.random() * window.innerHeight;
    heart.style.left = x + 'px';
    heart.style.top = y + 'px';
    heart.style.transform = `rotate(${Math.random() * 40 - 20}deg)`;
    document.body.appendChild(heart);
    setTimeout(() => heart.remove(), 1500);
}

function createFlower() {
    const flower = document.createElement('div');
    flower.className = 'flower';
    const petals = ['🌸','🌷','🌺','💮','🌼'];
    flower.textContent = petals[Math.floor(Math.random() * petals.length)];
    flower.style.left = Math.random() * window.innerWidth + 'px';
    flower.style.fontSize = 16 + Math.random() * 12 + 'px';
    flower.style.animationDuration = (4 + Math.random() * 3) + 's';
    document.body.appendChild(flower);
    setTimeout(() => flower.remove(), 7000);
}
</script>

<!-- 🎧 로파이 배경음악 (무료, 반복재생) -->
<audio autoplay loop>
  <source src="https://cdn.pixabay.com/download/audio/2023/06/07/audio_aa2e5ecba4.mp3?filename=lofi-study-112191.mp3" type="audio/mpeg">
</audio>

<div class="flower-footer"></div>
"""
st.markdown(lovely_lofi_theme, unsafe_allow_html=True)

# 🌟 제목
st.title("MBTI 기반 진로 추천기 💗✨")
st.write("로파이 감성 속에서, 너의 MBTI에 맞는 **진로 2가지**를 찾아줄게야르 🎧🌸")

# 💡 MBTI 목록
MBTI_LIST = [
    "ISTJ","ISFJ","INFJ","INTJ",
    "ISTP","ISFP","INFP","INTP",
    "ESTP","ESFP","ENFP","ENTP",
    "ESTJ","ESFJ","ENFJ","ENTJ"
]

# 💼 예시 데이터
MBTI_TO_CAREERS = {
    "ENFP": [
        {"job":"콘텐츠 기획자 / 창업가 🚀", "majors":["미디어학과","경영학과"], "personality":"아이디어 뿜뿜! 다방면으로 흥미를 느끼는 사람."},
        {"job":"광고/크리에이티브 디렉터 🎨", "majors":["광고홍보학과","시각디자인과"], "personality":"사람의 감성을 자극하는 일을 잘함."}
    ],
    "INFJ": [
        {"job":"상담사 / 임상심리사 🧠", "majors":["심리학과","상담학과"], "personality":"공감력 최고! 사람 마음을 읽는 감성형 리더."},
        {"job":"작가 / 콘텐츠 크리에이터 ✍️", "majors":["문예창작과","미디어학과"], "personality":"창의력 넘치는 예술적 성향. 깊은 표현력 보유."}
    ],
}

# 💫 출력 함수
def show_career_info(mbti):
    careers = MBTI_TO_CAREERS.get(mbti, [])
    st.header(f"{mbti}에게 어울리는 진로 추천 💫")
    for item in careers:
        st.subheader(item["job"])
        st.markdown(f"- **추천 학과**: {', '.join(item['majors'])} 🎓")
        st.markdown(f"- **어울리는 성격**: {item['personality']}")
        st.write("---")

# 🎯 인터랙션
st.sidebar.title("설정 ⚙️")
st.sidebar.write("MBTI를 골라봐 🎧💗 (로파이 감성 속에서 진로를 찾아보자야르)")
selected = st.selectbox("MBTI 선택", MBTI_LIST, index=0)

if st.button("추천 받기! 💖"):
    show_career_info(selected)
    st.success("🌈 진로는 MBTI뿐 아니라, 너의 열정과 호기심이 만들어가는 거야르 🌿")
else:
    st.write("왼쪽에서 MBTI를 고르고 ‘추천 받기! 💖’ 버튼을 눌러봐야르 💕")

st.divider()
st.caption("만든이: MBTI 진로 추천기 🎧 로파이+하트+꽃잎 감성버전 🌸 소희티비야르 💗")
