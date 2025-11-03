# mbti_career_app.py
import streamlit as st

# 🌷 페이지 설정
st.set_page_config(page_title="MBTI 진로 추천 🌟", page_icon="🎯", layout="centered")

# 💖 배경색을 핑크로 바꾸는 CSS
page_bg = """
<style>
body {
    background: linear-gradient(to bottom right, #ffe6f2, #ffd6eb);
    color: #333333;
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# 🌟 제목과 안내문
st.title("MBTI 기반 진로 추천기 🎓✨")
st.write("16가지 MBTI 중 하나를 고르면, 딱 맞는 **진로 2가지**와\n관련 학과, 그리고 어떤 성격의 사람이 잘 맞는지 알려줄게! 😎")

# 💡 MBTI 목록
MBTI_LIST = [
    "ISTJ","ISFJ","INFJ","INTJ",
    "ISTP","ISFP","INFP","INTP",
    "ESTP","ESFP","ENFP","ENTP",
    "ESTJ","ESFJ","ENFJ","ENTJ"
]

# 💼 MBTI별 진로 추천 데이터
MBTI_TO_CAREERS = {
    "ISTJ": [
        {"job":"회계사 / 세무사 🧾", "majors":["회계학과","경영학과"], "personality":"체계적이고 책임감 강함. 규칙과 디테일에 강함."},
        {"job":"토목/건설 엔지니어 🏗️", "majors":["건축공학과","토목공학과"], "personality":"현실적이고 실용적, 계획을 잘 세우는 스타일."}
    ],
    "ISFJ": [
        {"job":"간호사 / 보건의료인 👩‍⚕️", "majors":["간호학과","보건학과"], "personality":"배려심 많고 성실함. 사람 돌보는 걸 좋아함."},
        {"job":"사회복지사 🤝", "majors":["사회복지학과","상담심리학과"], "personality":"조용히 돕는 걸 즐김. 안정감 있는 환경 선호."}
    ],
    "INFJ": [
        {"job":"상담사 / 임상심리사 🧠", "majors":["심리학과","상담학과"], "personality":"통찰력 있고 남의 감정에 공감 잘함. 깊이 있는 대화 선호."},
        {"job":"작가 / 콘텐츠 크리에이터 ✍️", "majors":["문예창작과","미디어학과"], "personality":"창의적이고 내면이 풍부함. 의미 있는 표현을 좋아함."}
    ],
    "INTJ": [
        {"job":"데이터 사이언티스트 / 연구원 📊", "majors":["컴퓨터공학과","통계학과"], "personality":"전략적이고 분석적. 복잡한 문제 해결에 강함."},
        {"job":"전략기획 / 컨설턴트 🧭", "majors":["경영학과","경제학과"], "personality":"미래를 설계하고 계획 세우는 걸 즐김. 독립심 강함."}
    ],
    "ISTP": [
        {"job":"기계/정비 엔지니어 🔧", "majors":["기계공학과","산업공학과"], "personality":"손으로 만지고 해결하는 것에 능숙. 현실적 문제 해결형."},
        {"job":"파일럿 / 구조대원 ✈️", "majors":["항공운항학과","응급구조학과"], "personality":"위기 상황에서도 침착함. 모험심도 존재."}
    ],
    "ISFP": [
        {"job":"디자이너 / 시각예술가 🎨", "majors":["시각디자인과","미술학과"], "personality":"감성적이고 창의적. 자유로운 환경에서 빛남."},
        {"job":"패션/뷰티 관련 업종 👗", "majors":["패션디자인과","뷰티디자인과"], "personality":"세심하고 감각적. 트렌드에 민감함."}
    ],
    "INFP": [
        {"job":"문학/창작 활동가 (작가, 시나리오) 📚", "majors":["문예창작과","영문학과"], "personality":"이상주의자. 내적 가치와 뜻을 중시함."},
        {"job":"NGO/사회적 기업 활동가 🌱", "majors":["사회학과","공공정책학과"], "personality":"가치 지향적이고 공감능력 높음. 변화를 꿈꿈."}
    ],
    "INTP": [
        {"job":"소프트웨어 개발자 / 연구원 💻", "majors":["컴퓨터공학과","전자공학과"], "personality":"호기심 많고 논리적. 아이디어 실험을 즐김."},
        {"job":"학문 연구자 (이론 중심) 🔬", "majors":["물리학과","수학과"], "personality":"깊게 파고드는 성향. 혼자 집중 잘함."}
    ],
    "ESTP": [
        {"job":"영업/마케팅 전문가 💼", "majors":["경영학과","마케팅학과"], "personality":"활발하고 사교적. 빠른 판단과 실행력 보유."},
        {"job":"이벤트/퍼포먼스 기획자 🎤", "majors":["문화콘텐츠학과","미디어학과"], "personality":"즉흥적이고 현장감 있는 상황에 강함."}
    ],
    "ESFP": [
        {"job":"연예/공연 기획자·연기자 🎭", "majors":["연극영화과","무대예술과"], "personality":"사람들 앞에서 빛나는 타입. 즉흥적이고 에너지 넘침."},
        {"job":"관광·서비스 업종 (호텔/여행) 🧳", "majors":["관광학과","호텔경영학과"], "personality":"사교적이고 손님 응대에 능함. 즐거움 추구."}
    ],
    "ENFP": [
        {"job":"콘텐츠 기획자 / 창업가 🚀", "majors":["미디어학과","경영학과"], "personality":"아이디어 뿜뿜! 다방면으로 흥미를 느끼는 사람."},
        {"job":"광고/크리에이티브 디렉터 🎨", "majors":["광고홍보학과","시각디자인과"], "personality":"사람의 감성을 자극하는 일을 잘함."}
    ],
    "ENTP": [
        {"job":"스타트업 창업가 / 기획자 ⚙️", "majors":["경영학과","융합전공"], "personality":"빠르게 아이디어를 실험하고 돌파하는 스타일."},
        {"job":"법률/토론 관련 직업 (변호사·정책분석) ⚖️", "majors":["법학과","정치외교학과"], "personality":"말재주 좋고 논리적 토론을 즐김."}
    ],
    "ESTJ": [
        {"job":"기업 관리자 / 운영 매니저 📋", "majors":["경영학과","산업경영공학과"], "personality":"조직을 운영하고 관리하는 걸 좋아함. 실무형."},
        {"job":"공무원 / 행정직 🏛️", "majors":["행정학과","법학과"], "personality":"규칙과 절차를 중시. 책임감 강함."}
    ],
    "ESFJ": [
        {"job":"교사 / 교육 관련 직업 👩‍🏫", "majors":["교육학과","아동학과"], "personality":"사람 돌보는 걸 즐기고, 협동을 잘함."},
        {"job":"인사/고객관리(HR·CS) 💬", "majors":["경영학과","심리학과"], "personality":"타인과의 조화, 서비스 마인드가 뛰어남."}
    ],
    "ENFJ": [
        {"job":"HR·리더십 코치 / 교육전문가 🌟", "majors":["교육학과","심리학과"], "personality":"사람을 이끌고 성장시키는 데 재능이 있음."},
        {"job":"PR·커뮤니케이션 매니저 📣", "majors":["언론홍보학과","경영학과"], "personality":"사교적이고 설득력 있는 소통 능력 보유."}
    ],
    "ENTJ": [
        {"job":"경영진 / CEO 후보 💼", "majors":["경영학과","경제학과"], "personality":"목표 지향적이고 리더십 강함. 전략적 사고."},
        {"job":"전략 컨설턴트 / 투자분석가 📈", "majors":["경영학과","금융학과"], "personality":"결정력 있고 큰 그림을 보는 스타일."}
    ],
}

# 🌈 추천 결과 출력 함수
def show_career_info(mbti):
    careers = MBTI_TO_CAREERS.get(mbti, [])
    st.header(f"{mbti}님에게 어울리는 진로 추천 🔎")
    for item in careers:
        st.subheader(item["job"])
        st.markdown(f"- **추천 학과**: {', '.join(item['majors'])} 🎓")
        st.markdown(f"- **어울리는 성격**: {item['personality']}")
        st.write("---")

# 🎯 선택 영역
st.sidebar.title("설정 ⚙️")
st.sidebar.write("원하는 MBTI를 골라봐! (친구랑 해도 재밌음 💬)")

selected = st.selectbox("MBTI 선택", MBTI_LIST, index=0)

if st.button("추천 받기! 🚀"):
    show_career_info(selected)
    st.info("💡 진로는 MBTI만으로 확정되는 게 아니야! 관심사, 경험, 학과 수업, 인턴 경험 등을 꼭 고려해봐 😄")
else:
    st.write("왼쪽에서 MBTI를 골라서 `추천 받기! 🚀` 버튼을 눌러줘 💫")

st.divider()
st.caption("만든이: MBTI 진로 추천기 · 핑크 감성 버전 🌸")
