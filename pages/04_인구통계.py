st.markdown("""
    <style>
    /* 💕 구글 폰트 불러오기 (손글씨 느낌) */
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
""", unsafe_allow_html=True)
