import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Multiple Disease Detection App",
    page_icon="🤖",
    layout="wide",
)

st.markdown("""
        <style>
               .block-container {
                    padding-top: 0rem;
                    padding-bottom: 0rem;
                    padding-left: 0.1rem;
                    padding-right: 0.1rem;
                    margin-top: -10px;
		    background-color:white;
                }
                .center {
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    text-align: center;
                }
        
        </style>
        """, unsafe_allow_html=True)
# Custom CSS for the selectbox
selectbox_style = '''
<style>
div[data-baseweb="select"] {
    opacity: 5;
    width: 350px;
}
div[data-baseweb="select"] > div > div {
    color: red;
    font-size: 150%;
}
div[data-baseweb="select"] > div > div:hover {
    background-color: #808080 !important;
}
</style>
'''
selectbox_style2 = '''
<style>
div[data-baseweb="select"] {
    opacity: 0.50;
    margin-top: -10px;
}
</style>
'''

# Apply the custom CSS
st.markdown(selectbox_style, unsafe_allow_html=True)

# Disease information dictionary
disease_info = {
    "Select disease": {
        "description": """<p style='font-size:22px; max-width:100%'>
		Our machine learning models analyze various health parameters and data to assess your risk of developing diabetes. Early detection can lead to better management and a healthier lifestyle.
		We use advanced algorithms to evaluate your cardiovascular health, giving you a better understanding of your heart's condition. Timely intervention can help prevent heart-related issues.
		Our machine learning technology can identify potential signs of lung cancer based on your medical history and lifestyle factors. Early detection is crucial for improved treatment outcomes.""",
        "image_url": "Images/healthcare.jpg"
    },
    "Diabetes": {
        "description": "<p style='font-size:22px'>Diabetes is a chronic medical condition that affects how your body regulates blood sugar (glucose), which is a primary source of energy for your cells. When you eat, your body breaks down the carbohydrates in your food into glucose, which then enters your bloodstream. In response to rising blood sugar levels, your pancreas releases a hormone called insulin, which helps your cells absorb and use glucose for energy. This process helps maintain your blood sugar at a stable level. Diabetes occurs when there's a problem with this glucose regulation system.",
        "image_url": "Images/diabites.png"
    },
    "Heart Disease": {
        "description": "<p style='font-size:22px'>Heart disease, also known as cardiovascular disease (CVD), refers to a class of diseases that affect the heart and blood vessels. It is one of the leading causes of death worldwide. Heart disease encompasses various conditions, with the most common being coronary artery disease, heart failure, and arrhythmias. Symptoms of heart disease can vary but may include chest pain or discomfort, shortness of breath, fatigue, dizziness, and irregular heartbeats. Some people may experience no symptoms until a heart attack occurs.",
        "image_url": "Images/heart.png"
    },
    "Lung Cancer": {
        "description": "<p style='font-size:22px; max-width:100%'>Lung cancer is a disease caused by uncontrolled cell division in your lungs. Your cells divide and make more copies of themselves as a part of their normal function. But sometimes, they get changes (mutations) that cause them to keep making more of themselves when they shouldn’t. Damaged cells dividing uncontrollably create masses, or tumors, of tissue that eventually keep your organs from working properly.",
        "image_url": "Images/lung.png"
    }
}

# Title
st.title("Multi-Disease Detection App")
temp = components.html('<H3>Welcome to our disease detection application.</H3>', height=45)

# List of diseases
disease_selection = st.selectbox("", list(disease_info.keys()))
if disease_selection == "Select disease":
    st.markdown(selectbox_style2, unsafe_allow_html=True)
else:
    selectbox_class = ''

# Display selected disease information with description on the left and image on the right
if disease_selection in disease_info:
    description, image_url = disease_info[disease_selection]["description"], disease_info[disease_selection]["image_url"]
    col1, col2 = st.columns(2)
    with col1:
        # Use style attribute to set max-width
        components.html(f'<div style="font-size: 20px; max-height:100px;max-width:100%;text-align: justify;margin-top:-25px;background-color:white;">{description}</div>',height=355)
    with col2:
        st.image(image_url,width=390)

# ...

html_code = """
<a href='Main' target='_self'>
  <button id="myButton" style="background-color: #0074CC; color: white; padding: 10px 20px; border: none; border-radius: 12px; cursor: pointer; width: 100%;">Detect Disease</button>
</a>
"""

# Set the width of the button to 100%
st.markdown(html_code, unsafe_allow_html=True)
