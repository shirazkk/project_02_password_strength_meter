import re
import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Password Strength Meter",
    page_icon="🔐",
    layout="centered"
)

# Custom CSS for enhanced styling
st.markdown("""
<style>
    .stApp {
        background-color: #f0f2f6;
    }
    .stTextInput > div > div > input {
        background-color: white;
        border: 2px solid #3498db;
        border-radius: 10px;
        padding: 10px;
        color: #2c3e50;
    }
    .stButton > button {
        background-color: #3498db;
        color: white;
        border-radius: 10px;
        border: none;
        padding: 10px 20px;
        transition: background-color 0.3s ease;
    }
    .stButton > button:hover {
        background-color: #2980b9;
    }
    .stProgress > div > div {
        background-color: #3498db;
    }
</style>
""", unsafe_allow_html=True)

# Title with custom styling
st.markdown("""
    <h1 style='text-align: center; color: #2c3e50; 
    text-shadow: 2px 2px 4px rgba(0,0,0,0.1);'>
    🔐 Password Strength Meter
    </h1>
""", unsafe_allow_html=True)

def check_password_strength(password):
    score = 0
    messages = []
    
    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        messages.append("❌ Password should be at least 8 characters long.")
    
    # Uppercase Check
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        messages.append("❌ Password should contain at least one uppercase letter.")
    
    # Lowercase Check
    if re.search(r"[a-z]", password):
        score += 1
    else:
        messages.append("❌ Password should contain at least one lowercase letter.")
    
    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        messages.append("❌ Password should contain at least one number (0-9).")
    
    # Special Character Check
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        messages.append("❌ Password should contain at least one special character.")
    
    return score, messages

# Main form with enhanced layout
with st.form(key="password_form"):
    # Custom styled input
    user_password = st.text_input(
        "Please enter your password:", 
        type="password", 
        help="Create a strong password with at least 8 characters"
    )
    
    # Submit button
    submit_button = st.form_submit_button("Check Password Strength")

if submit_button:
    # Prevent empty password submission
    if not user_password:
        st.warning("Please enter a password to check its strength.")
    else:
        strength, feedback = check_password_strength(user_password)
        
        # Display progress bar with color-coded strength
        progress_percentage = int((strength / 5) * 100)
        progress_color = "#2ecc71" if strength >= 4 else "#f39c12" if strength == 3 else "#e74c3c"
        st.markdown(f"""
            <div style='background-color: #ecf0f1; 
                        border-radius: 10px; 
                        padding: 10px; 
                        margin-bottom: 15px;'>
                <h3 style='color: #2c3e50; margin-bottom: 10px;'>Password Strength</h3>
                <div style='width: {progress_percentage}%; 
                            background-color: {progress_color}; 
                            height: 20px; 
                            border-radius: 10px;'>
                </div>
                <p style='text-align: center; color: #34495e;'>
                    Score: {strength}/5
                </p>
            </div>
        """, unsafe_allow_html=True)
        
        # Strength Rating with enhanced messaging
        if strength >= 4:
            st.success("✅ Strong Password! You're ready to go.")
        elif strength == 3:
            st.warning("⚠️ Moderate Password - Consider adding more security features.")
        else:
            st.error("❌ Weak Password - Improve it using the suggestions below:")
        
        # Display all collected feedback messages
        for msg in feedback:
            st.info(msg)