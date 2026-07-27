import streamlit as st
import requests
import os
import base64
from PIL import Image

# 1. Page Configuration
st.set_page_config(
    page_title="فقيه | المستشار القانوني الذكي",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Backend API Endpoint
DEFAULT_API_URL = "https://coherent-endowment-outpost.ngrok-free.dev"
if "api_url" not in st.session_state:
    st.session_state.api_url = DEFAULT_API_URL

# Load and encode logo
LOGO_PATH = os.path.join(os.path.dirname(__file__), "logo.jpg")
logo_b64 = ""
if os.path.exists(LOGO_PATH):
    try:
        with open(LOGO_PATH, "rb") as f:
            logo_b64 = base64.b64encode(f.read()).decode()
    except Exception:
        pass

# 2. Inject External FontAwesome & Custom CSS
st.markdown("""
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
<style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@300;400;500;700;800;900&display=swap');

    /* Global RTL Typography */
    html, body, [class*="css"] {
        font-family: 'Tajawal', sans-serif !important;
        direction: rtl !important;
        text-align: right !important;
    }

    /* 🌈 1. DYNAMIC COLOR-CHANGING ANIMATED GRADIENT BACKGROUND (BLUE / NAVY) */
    @keyframes navyCycle {
        0%   { background-position: 0% 50%; }
        50%  { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    .stApp {
        background: linear-gradient(
            -45deg, 
            #060d1a, /* كحلي شديد السواد */
            #0f172a, /* أزرق داكن */
            #020617, /* لون منتصف الليل */
            #111827  /* رمادي مزرق غامق */
        ) !important;
        background-size: 300% 300% !important;
        animation: navyCycle 14s ease-in-out infinite !important;
        color: #f8fafc !important;
        min-height: 100vh !important;
    }

    /* HIDE SIDEBAR & STREAMLIT CHROME */
    section[data-testid="stSidebar"], #MainMenu, footer, header {
        display: none !important;
        visibility: hidden !important;
    }

    /* Layout Container Centering */
    .block-container {
        max-width: 860px !important;
        margin: 0 auto !important;
        padding-top: 2.5rem !important;
        padding-bottom: 120px !important;
    }

    /* ══ 2. TOP-LEFT DEVELOPER CONTACT CAPSULE ══ */
    .vertical-contact-capsule {
        position: fixed !important;
        top: 30px !important;
        left: 30px !important;
        z-index: 999999 !important;
    }

    .capsule-main-btn {
        list-style: none !important;
        cursor: pointer !important;
        background: rgba(15, 23, 42, 0.88) !important;
        border: 1.8px solid rgba(212, 175, 55, 0.7) !important;
        border-radius: 30px !important;
        padding: 10px 20px !important;
        color: #f59e0b !important;
        font-weight: 800 !important;
        font-size: 0.92rem !important;
        display: flex !important;
        align-items: center !important;
        gap: 8px !important;
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.5), 0 0 15px rgba(212, 175, 55, 0.25) !important;
        backdrop-filter: blur(16px) !important;
        transition: all 0.3s ease !important;
    }

    .capsule-main-btn::-webkit-details-marker {
        display: none !important;
    }

    .capsule-main-btn:hover {
        transform: translateY(-2px) scale(1.03) !important;
        background: rgba(30, 41, 59, 0.95) !important;
        border-color: #f5c518 !important;
    }

    .capsule-vertical-menu {
        position: absolute !important;
        top: 52px !important;
        left: 0 !important;
        display: flex !important;
        flex-direction: column !important;
        gap: 8px !important;
        width: 220px !important;
        padding-top: 8px !important;
        animation: fadeInDown 0.3s ease !important;
    }

    @keyframes fadeInDown {
        from { opacity: 0; transform: translateY(-10px); }
        to { opacity: 1; transform: translateY(0); }
    }

    .vertical-item {
        display: flex !important;
        align-items: center !important;
        gap: 12px !important;
        padding: 11px 18px !important;
        border-radius: 22px !important;
        color: #ffffff !important;
        text-decoration: none !important;
        font-weight: 700 !important;
        font-size: 0.92rem !important;
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.5) !important;
        transition: all 0.25s ease !important;
        backdrop-filter: blur(16px) !important;
    }

    .vertical-item:hover {
        transform: translateX(5px) scale(1.03) !important;
    }

    .item-linkedin { background: linear-gradient(135deg, #0a66c2, #004182) !important; border: 1px solid rgba(255,255,255,0.2) !important; }
    .item-gmail { background: linear-gradient(135deg, #ea4335, #c62828) !important; border: 1px solid rgba(255,255,255,0.2) !important; }
    .item-whatsapp { background: linear-gradient(135deg, #25d366, #128c7e) !important; border: 1px solid rgba(255,255,255,0.2) !important; }

    /* Hero Header Section */
    .hero-box {
        text-align: center !important;
        padding: 10px 20px 20px 20px !important;
        margin-bottom: 20px !important;
    }

    /* SINGLE ANIMATED LOGO */
    .hero-logo-single {
        width: 125px !important;
        height: 125px !important;
        border-radius: 50% !important;
        border: 3.5px solid rgba(212, 175, 55, 0.85) !important;
        box-shadow: 0 0 45px rgba(212, 175, 55, 0.6), 0 0 90px rgba(212, 175, 55, 0.25) !important;
        object-fit: cover !important;
        margin: 0 auto 16px auto !important;
        display: block !important;
        animation: floatGlow 3.5s ease-in-out infinite !important;
    }

    .hero-logo-fallback-single {
        width: 125px !important;
        height: 125px !important;
        border-radius: 50% !important;
        border: 3.5px solid rgba(212, 175, 55, 0.85) !important;
        background: linear-gradient(135deg, #1e1b4b, #0f172a) !important;
        box-shadow: 0 0 45px rgba(212, 175, 55, 0.6) !important;
        font-size: 4rem !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        margin: 0 auto 16px auto !important;
        animation: floatGlow 3.5s ease-in-out infinite !important;
    }

    @keyframes floatGlow {
        0%, 100% { transform: translateY(0px); box-shadow: 0 0 35px rgba(212, 175, 55, 0.5); }
        50% { transform: translateY(-10px); box-shadow: 0 15px 55px rgba(212, 175, 55, 0.8); }
    }

    .hero-title {
        font-size: 4.2rem !important;
        font-weight: 900 !important;
        background: linear-gradient(135deg, #ffffff 0%, #fceabb 40%, #f8b500 70%, #ffffff 100%) !important;
        background-size: 200% auto !important;
        -webkit-background-clip: text !important;
        -webkit-text-fill-color: transparent !important;
        animation: shimmer 3s linear infinite !important;
        margin-bottom: 6px !important;
        letter-spacing: -1px !important;
    }

    @keyframes shimmer {
        0% { background-position: 0% center; }
        100% { background-position: 200% center; }
    }

    .hero-subtitle {
        color: #cbd5e1 !important;
        font-size: 1.2rem !important;
        font-weight: 500 !important;
    }

    /* ══ ELEGANT GOLDEN BADGES ══ */
    .elegant-badge {
        display: inline-flex !important;
        align-items: center !important;
        gap: 8px !important;
        background: rgba(20, 20, 20, 0.6) !important;
        border: 1px solid rgba(212, 175, 55, 0.4) !important;
        color: #fde047 !important;
        padding: 8px 24px !important;
        border-radius: 40px !important;
        font-size: 0.95rem !important;
        font-weight: 600 !important;
        margin-top: 14px !important;
        backdrop-filter: blur(8px) !important;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3) !important;
    }

    .disclaimer-banner {
        background: rgba(20, 20, 20, 0.6) !important;
        border: 1px solid rgba(245, 158, 11, 0.4) !important;
        color: #fcd34d !important;
        padding: 9px 22px !important;
        border-radius: 14px !important;
        font-size: 0.95rem !important;
        font-weight: 700 !important;
        display: inline-block !important;
        margin-top: 14px !important;
    }

    /* ══ 3. BUTTONS (HOVER TO SOLID GOLD) ══ */
    .stButton > button {
        background: rgba(15, 23, 42, 0.7) !important;
        border: 1.5px solid rgba(212, 175, 55, 0.4) !important;
        color: #f8fafc !important;
        border-radius: 30px !important;
        font-size: 1rem !important;
        font-weight: 700 !important;
        padding: 12px 14px !important;
        min-height: 52px !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        text-align: center !important;
        transition: all 0.3s ease !important;
        width: 100% !important;
        backdrop-filter: blur(12px) !important;
        box-shadow: 0 6px 20px rgba(0,0,0,0.2) !important;
    }

    .stButton > button:hover {
        background: rgba(212, 175, 55, 0.95) !important; 
        border-color: #f5c518 !important;
        color: #0f172a !important; 
        transform: translateY(-3px) scale(1.02) !important;
        box-shadow: 0 10px 25px rgba(212, 175, 55, 0.5) !important;
    }

    /* ══ 4. LARGER TEXT FOR CHAT MESSAGES ══ */
    [data-testid="stChatMessage"] {
        background: rgba(10, 16, 30, 0.8) !important;
        backdrop-filter: blur(18px) !important;
        border: 1px solid rgba(212, 175, 55, 0.15) !important;
        border-radius: 20px !important;
        padding: 20px 24px !important;
        margin-bottom: 16px !important;
        box-shadow: 0 10px 35px rgba(0, 0, 0, 0.45) !important;
        
        /* 🔥 تكبير الخط للرسائل ليصبح ضخماً ومريحاً 🔥 */
        font-size: 1.6rem !important; 
        line-height: 2.2 !important;
        color: #f1f5f9 !important;
    }

    [data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-user"]) {
        border-color: rgba(212, 175, 55, 0.5) !important;
        background: rgba(20, 28, 50, 0.88) !important;
    }

    /* ══ 5. LARGER TEXT FOR CHAT INPUT ══ */
    [data-testid="stChatInput"] {
        padding-bottom: 20px !important;
    }

    [data-testid="stChatInput"] textarea {
        border-radius: 25px !important;
        border: 1.8px solid rgba(212, 175, 55, 0.7) !important;
        background: rgba(10, 16, 30, 0.95) !important;
        color: #ffffff !important;
        
        /* 🔥 تكبير الخط لخانة الكتابة 🔥 */
        font-size: 1.5rem !important; 
        font-weight: 600 !important;
        padding: 16px 65px 16px 25px !important;
        box-shadow: 0 12px 40px rgba(0, 0, 0, 0.6) !important;
        line-height: 1.5 !important;
    }

    [data-testid="stChatInput"] textarea:focus {
        border-color: rgba(253, 224, 71, 0.95) !important;
        box-shadow: 0 0 0 4px rgba(212, 175, 55, 0.35) !important;
        outline: none !important;
    }

    /* CENTER SEND ARROW VERTICALLY */
    [data-testid="stChatInput"] button {
        position: absolute !important;
        right: 18px !important;
        left: auto !important;
        top: 50% !important;
        transform: translateY(-50%) !important;
        color: #f59e0b !important;
        background: transparent !important;
        border: none !important;
    }
</style>

<!-- ══ TOP-LEFT DEVELOPER CONTACT CAPSULE ══ -->
<details class="vertical-contact-capsule">
    <summary class="capsule-main-btn" title="انقر للتواصل مع المطور">
        <i class="fa-solid fa-headset"></i>
        <span>التواصل مع المطور</span>
        <i class="fa-solid fa-chevron-down"></i>
    </summary>
    <div class="capsule-vertical-menu">
        <a href="https://www.linkedin.com/in/kareem-aboalnoor-a14a562b1?utm_source=share_via&utm_content=profile&utm_medium=member_android" target="_blank" class="vertical-item item-linkedin">
            <i class="fa-brands fa-linkedin" style="font-size: 1.2rem;"></i>
            <span>LinkedIn</span>
        </a>
        <a href="mailto:kareemaboalnoor8@gmail.com" target="_blank" class="vertical-item item-gmail">
            <i class="fa-solid fa-envelope" style="font-size: 1.1rem;"></i>
            <span>Gmail</span>
        </a>
        <a href="https://wa.me/201011724820" target="_blank" class="vertical-item item-whatsapp">
            <i class="fa-brands fa-whatsapp" style="font-size: 1.2rem;"></i>
            <span>واتساب: 01011724820</span>
        </a>
    </div>
</details>
""", unsafe_allow_html=True)

# 3. Hero Section (ONLY ONE SINGLE ANIMATED SCALE LOGO)
if logo_b64:
    logo_html = f'<img class="hero-logo-single" src="data:image/jpeg;base64,{logo_b64}" alt="فقيه"/>'
else:
    logo_html = '<div class="hero-logo-fallback-single">⚖️</div>'

st.markdown(f"""
<div class="hero-box">
    {logo_html}
    <div class="hero-title">فقـيـه</div>
    <div class="hero-subtitle">المساعد القانوني الذكي المتخصص حصرياً في التشريعات والقوانين المصرية</div>
    <div>
        <div class="elegant-badge">
            <i class="fa-solid fa-scale-balanced" style="color: #fde047;"></i>
            <span>تحديث شامل للقوانين والتشريعات المصرية</span>
        </div>
    </div>
    <div>
        <div class="disclaimer-banner">
            ⚠️ تنبيه هام: جميع الإجابات للأغراض التعليمية والاسترشادية فقط وليست بديلاً عن استشارة محامٍ متخصص.
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# 4. Quick Suggestion Chips (UPDATED WITH YOUR QUESTIONS)
st.markdown("<h5 style='color: #cbd5e1; text-align: center; margin-bottom: 14px;'>💬 أسئلة قانونية شائعة بنقرة واحدة:</h5>", unsafe_allow_html=True)
col1, col2, col3, col4 = st.columns(4)

selected_prompt = None
with col1:
    if st.button("⚖️ محضر بالشرطة", use_container_width=True):
        selected_prompt = "إيه الإجراءات القانونية لتحرير محضر في قسم الشرطة؟"
with col2:
    if st.button("👨‍💼 فصل تعسفي", use_container_width=True):
        selected_prompt = "ما هي حقوق العامل إذا تم فصله تعسفياً؟"
with col3:
    if st.button("👩‍👧 حقوق الطلاق", use_container_width=True):
        selected_prompt = "ما هي حقوق الزوجة بعد الطلاق؟"
with col4:
    if st.button("📄 إيصال الأمانة", use_container_width=True):
        selected_prompt = "ما هي عقوبة خيانة الأمانة (إيصال أمانة)؟"

st.markdown("<br>", unsafe_allow_html=True)

# 5. Chat History Management
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "أهلاً بك! أنا **فقيه**، مستشارك القانوني الذكي المتخصص في **القانون والتشريعات المصرية**.\n\nكيف يمكنني مساعدتك في قضيتك أو استشارتك اليوم؟"
        }
    ]

# Display Existing Messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User Prompt Input
user_prompt = st.chat_input("اطرح سؤالك أو قضيتك القانونية هنا...")
if selected_prompt:
    user_prompt = selected_prompt

if user_prompt:
    st.session_state.messages.append({"role": "user", "content": user_prompt})
    with st.chat_message("user"):
        st.markdown(user_prompt)

    with st.chat_message("assistant"):
        try:
            def response_stream_generator():
                res = requests.post(
                    f"{st.session_state.api_url}/ask_stream",
                    json={"question": user_prompt},
                    headers={
                        "Content-Type": "application/json",
                        "ngrok-skip-browser-warning": "69420"
                    },
                    stream=True,
                    timeout=90
                )
                if res.status_code == 200:
                    for chunk in res.iter_content(chunk_size=10, decode_unicode=True):
                        if chunk:
                            yield chunk
                else:
                    yield f"⚠️ حدث خطأ في الاستجابة من السيرفر (كود: {res.status_code}). يرجى التأكد من تشغيل نوت بوك Kaggle."

            full_response = st.write_stream(response_stream_generator)
            st.session_state.messages.append({"role": "assistant", "content": full_response})

        except Exception as e:
            st.error(f"❌ تعذر الاتصال بسيرفر Kaggle. يرجى التأكد من تشغيل النوت بوك ورابط ngrok.\n\nالتفاصيل: {e}")

# Clear Chat Option at bottom
st.markdown("<br>", unsafe_allow_html=True)
col_c1, col_c2, col_c3 = st.columns([3, 2, 3])
with col_c2:
    if st.button("🗑️ مسح المحادثة بالكامل", use_container_width=True):
        try:
            requests.post(
                f"{st.session_state.api_url}/reset",
                headers={"Content-Type": "application/json", "ngrok-skip-browser-warning": "69420"},
                timeout=5
            )
        except Exception:
            pass
        st.session_state.messages = []
        st.rerun()