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
            }
        </style>
    """, unsafe_allow_html=True)

components_html = """
        <html>
        <head>
            <title>Welcome to Disease Detection</title>
            <!-- Your CSS styles go here -->
        </head>
        <body>
            <div class='header'>
                <h1>Welcome to Disease Detection</h1>
                <p>Your Health, Our Priority</p>
            </div>
            <div class='container'>
                <h2>What We Offer</h2>
                <p>We provide advanced disease detection solutions to help you stay healthy and informed. Our platform offers early detection for diseases like <b>Diabetes, Heart & Lung Cancer</b></p>
                <a href='Info' target='_self'>
                    <button id="myButton" style="background-color: #0074CC; color: white; padding: 10px 10px; border: none; border-radius: 12px; cursor: pointer; width: 30%;">Get Started</button>
                </a>
            </div>
        </body>
        </html>"""
st.markdown(components_html, unsafe_allow_html=True)
