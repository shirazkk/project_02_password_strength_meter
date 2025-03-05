import streamlit as st
from app1 import PasswordStrengthMeter

# Custom CSS for enhanced styling
st.markdown("""
<style>
    /* Main app styling */
    .stApp {
        background-color: #f8f9fa;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    /* Container styling */
    .main-container {
        background-color: white;
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
    }
    
    /* Input field styling */
    .stTextInput > div > div > input {
        background-color: #f8f9fa;
        border: 2px solid #6c5ce7;
        border-radius: 10px;
        padding: 12px 15px;
        color: #2d3436;
        font-size: 16px;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.05);
        transition: all 0.3s ease;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #5e52cc;
        box-shadow: 0 0 0 3px rgba(108, 92, 231, 0.2);
    }
    
    /* Button styling */
    .stButton > button {
        background-color: #6c5ce7;
        color: white;
        border-radius: 10px;
        border: none;
        padding: 12px 24px;
        font-weight: 600;
        letter-spacing: 0.5px;
        transition: all 0.3s ease;
        box-shadow: 0 4px 6px rgba(108, 92, 231, 0.2);
    }
    
    .stButton > button:hover {
        background-color: #5e52cc;
        transform: translateY(-2px);
        box-shadow: 0 6px 8px rgba(108, 92, 231, 0.3);
    }
    
    .stButton > button:active {
        transform: translateY(0);
    }
    
    /* Progress bar styling */
    .stProgress > div > div {
        background-color: #6c5ce7;
        border-radius: 10px;
    }
    
    /* Message styling */
    .success-msg {
        background-color: #d4edda;
        color: #155724;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #28a745;
        margin: 10px 0;
    }
    
    .warning-msg {
        background-color: #fff3cd;
        color: #856404;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #ffc107;
        margin: 10px 0;
    }
    
    .error-msg {
        background-color: #f8d7da;
        color: #721c24;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #dc3545;
        margin: 10px 0;
    }
    
    .info-msg {
        background-color: #e2f0fd;
        color: #0c5460;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #17a2b8;
        margin: 10px 0;
    }
    
    /* Sidebar styling */
    .css-1d391kg, .css-12oz5g7 {
        background-color: #f1f2f6;
        border-right: 1px solid #e1e4e8;
    }
    
    .sidebar-content {
        background-color: white;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
        margin-bottom: 10px;
    }
    
    .password-item {
        background-color: #f8f9fa;
        padding: 10px 15px;
        border-radius: 8px;
        margin: 5px 0;
        border-left: 3px solid #6c5ce7;
        font-family: monospace;
        font-size: 14px;
    }
    
    /* Divider */
    hr {
        margin: 20px 0;
        border: 0;
        height: 1px;
        background-image: linear-gradient(to right, rgba(0, 0, 0, 0), rgba(108, 92, 231, 0.5), rgba(0, 0, 0, 0));
    }
</style>
""", unsafe_allow_html=True)

# App header with enhanced styling
st.markdown("""
    <div style='text-align: center; padding: 20px 0 30px 0;'>
        <h1 style='color: #2d3436; font-size: 42px; font-weight: 700; 
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1); margin-bottom: 10px;'>
        🔐 Password Strength Meter
        </h1>
        <p style='color: #636e72; font-size: 18px; max-width: 600px; margin: 0 auto;'>
        Create and test secure passwords to protect your online accounts
        </p>
    </div>
""", unsafe_allow_html=True)

def userPassword():
    # Main content container
    st.markdown("<div class='main-container'>", unsafe_allow_html=True)
    
    st.markdown("""
        <h2 style='color: #2d3436; font-size: 24px; margin-bottom: 5px;'>Test Your Password</h2>
        <p style='color: #636e72; margin-bottom: 20px;'>Create a strong password with at least 8 characters, including uppercase, lowercase, numbers, and special characters.</p>
    """, unsafe_allow_html=True)
    
    if 'allPasswords' not in st.session_state:
        st.session_state.allPasswords = []

    password = st.text_input(label="Enter your password", type="password")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        check_button = st.button("Check Password Strength")
    
    with col2:
        save_button = st.button("Save Password")
    
    if check_button:
        if not password:
            st.markdown("<div class='warning-msg'>Please enter a password to check its strength.</div>", unsafe_allow_html=True)
        else:
            score, messages = PasswordStrengthMeter(password)
            
            # Password strength meter visualization
            st.markdown("<div style='margin: 20px 0;'>", unsafe_allow_html=True)
            
            if score >= 4:
                st.markdown(f"""
                    <div class='success-msg'>
                        <h3 style='margin: 0 0 10px 0; font-size: 18px;'>Password Strength: Strong</h3>
                        <div style='background-color: #e8f5e9; height: 10px; border-radius: 5px; margin-top: 5px;'>
                            <div style='width: {min(score * 20, 100)}%; background-color: #28a745; height: 10px; border-radius: 5px;'></div>
                        </div>
                    </div>
                """, unsafe_allow_html=True)
            elif score >= 3:
                st.markdown(f"""
                    <div class='warning-msg'>
                        <h3 style='margin: 0 0 10px 0; font-size: 18px;'>Password Strength: Moderate</h3>
                        <div style='background-color: #fff3cd; height: 10px; border-radius: 5px; margin-top: 5px;'>
                            <div style='width: {min(score * 20, 100)}%; background-color: #ffc107; height: 10px; border-radius: 5px;'></div>
                        </div>
                    </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                    <div class='error-msg'>
                        <h3 style='margin: 0 0 10px 0; font-size: 18px;'>Password Strength: Weak</h3>
                        <div style='background-color: #f8d7da; height: 10px; border-radius: 5px; margin-top: 5px;'>
                            <div style='width: {max(min(score * 20, 100), 10)}%; background-color: #dc3545; height: 10px; border-radius: 5px;'></div>
                        </div>
                    </div>
                """, unsafe_allow_html=True)
            
            st.markdown("</div>", unsafe_allow_html=True)
            
            # Feedback messages
            if messages:
                st.markdown("<div style='margin-top: 20px;'>", unsafe_allow_html=True)
                st.markdown("<h3 style='color: #2d3436; font-size: 18px; margin-bottom: 10px;'>Password Feedback:</h3>", unsafe_allow_html=True)
                
                for msg in messages:
                    st.markdown(f"<div class='info-msg'>{msg}</div>", unsafe_allow_html=True)
                
                st.markdown("</div>", unsafe_allow_html=True)
    
    if password and save_button:
        if password not in st.session_state.allPasswords:
            st.session_state.allPasswords.append(password)
            st.markdown("<div class='success-msg'>Your password has been added to the list.</div>", unsafe_allow_html=True)
        else:
            st.markdown("<div class='error-msg'>Password already in session</div>", unsafe_allow_html=True)
    
    # Password tips section
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("""
        <h3 style='color: #2d3436; font-size: 18px; margin-bottom: 10px;'>Tips for Strong Passwords:</h3>
        <ul style='color: #636e72; padding-left: 20px;'>
            <li>Use at least 8 characters</li>
            <li>Include uppercase and lowercase letters</li>
            <li>Add numbers and special characters</li>
            <li>Avoid common words or phrases</li>
            <li>Don't use personal information</li>
        </ul>
    """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)

    # Sidebar styling
    with st.sidebar:
        st.markdown("""
            <div style='text-align: center; margin-bottom: 20px;'>
                <h2 style='color: #2d3436; font-size: 22px;'>
                    📋 Saved Passwords
                </h2>
            </div>
        """, unsafe_allow_html=True)
        
        if st.session_state.allPasswords:
            st.markdown("<div class='sidebar-content'>", unsafe_allow_html=True)
            
            for pwd in st.session_state.allPasswords:
                st.markdown(f"<div class='password-item'>{pwd}</div>", unsafe_allow_html=True)
            
            st.markdown("</div>", unsafe_allow_html=True)
        else:
            st.markdown("""
                <div class='sidebar-content' style='text-align: center; padding: 20px;'>
                    <p style='color: #636e72;'>No passwords saved yet</p>
                </div>
            """, unsafe_allow_html=True)

userPassword()