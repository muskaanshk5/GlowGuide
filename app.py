import streamlit as st
import time

# Set page config
st.set_page_config(page_title="GlowGuide AI", layout="wide")

# Custom CSS for styling
st.markdown("""
    <style>
    /* Background Image */
    .stApp {
        background-image: url('assets/home_banner.jpg');
        background-size: cover;
        background-position: center;
    }

    /* Header Bar */
    .header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 10px 50px;
        background-color: rgba(255, 255, 255, 0.8);
        border-radius: 12px;
    }
    
    .header img {
        width: 150px;
        cursor: pointer;
    }

    .menu a {
        margin: 0 15px;
        font-size: 18px;
        text-decoration: none;
        color: #333;
        font-weight: bold;
    }

    /* Slideshow */
    .slideshow {
        text-align: center;
        margin-top: 30px;
    }

    .signup-box {
        text-align: center;
        padding: 20px;
        background: rgba(255, 255, 255, 0.9);
        border-radius: 12px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
        max-width: 400px;
        margin: 20px auto;
    }

    .footer {
        background-color: #222;
        color: white;
        padding: 20px;
        text-align: center;
        margin-top: 30px;
        border-radius: 12px;
    }

    </style>
""", unsafe_allow_html=True)

# ---- HEADER ----
col1, col2 = st.columns([1,3])

with col1:
    if st.button("🏠 GlowGuide AI"):
        st.rerun()

with col2:
    st.markdown("""
        <div class='menu'>
            <a href='#' onclick="window.location.reload()">Home</a>
            <a href='/features'>Features</a>
            <a href='/blogs'>Blogs</a>
        </div>
    """, unsafe_allow_html=True)

# ---- IMAGE SLIDESHOW ----
st.markdown("<h2 style='text-align:center;'>🌟 Your AI Skincare Assistant 🌟</h2>", unsafe_allow_html=True)

images = ["assets/slide1.jpg", "assets/slide2.jpg", "assets/slide3.jpg"]
img_placeholder = st.empty()

for _ in range(10):  # Repeat slideshow
    for img in images:
        img_placeholder.image(img, use_container_width=True)
        time.sleep(2)  # Change every 2 seconds

# ---- SIGNUP BOX ----
st.markdown("<h2 style='text-align:center;'>📝 Sign Up</h2>", unsafe_allow_html=True)

with st.form("signup_form"):
    st.text_input("Name")
    st.text_input("Email")
    st.text_input("Password", type="password")
    submit = st.form_submit_button("Sign Up")

if submit:
    st.success("You have successfully signed up!")

# ---- FOOTER ----
st.markdown("<div class='footer'><h3>📹 Videos</h3></div>", unsafe_allow_html=True)
st.video("assets/video.mp4")

st.markdown("<div class='footer'><h3>About Us</h3><p>GlowGuide AI is your trusted skincare companion, providing AI-powered skin analysis and personalized recommendations.</p></div>", unsafe_allow_html=True)
