import pickle
import streamlit as st
import streamlit.components.v1 as components

def diabetesInfo() :
    # st.markdown("""
    #     <style>
    #            .block-container {
    #                 padding-top: 2rem;
    #                 padding-bottom: 0rem;
    #                 padding-left: 0.1rem;
    #                 padding-right: 0.1rem;
    #             }
    #     </style>
    #     """, unsafe_allow_html=True)


    # Custom CSS for the selectbox

    st.title("Precautions for Diabetes Patients")
    components.html(
    """

    <!DOCTYPE html>
    <html>
    <style>
    p {
    font-size: 30px;
    background-color:white;
    }

    li {
    font-size: 25px;
   background-color:white;
    }

    </style>
    <head>

        <title style="mergin-top:200px;">Precautions for Diabetes Patients</title>
        <style>
            .column {
                width: 50%;
                float: left;
                background-color:white;
            }
        </style>
    </head>
    <body>

        <p style="background-color:white;">Precautions for diabetes patients are essential to help manage their condition and maintain overall health. It's important to note that I'm not a doctor, so you should always consult with a healthcare professional for personalized advice and guidance. However, here are some general precautions and tips for managing diabetes:</p>
        <div class="column">
        
            <body>
        

        <h2>Monitor Blood Sugar Levels:</h2>
        <ul>
            <li>Regularly check your blood glucose levels as recommended by your healthcare provider.</li>
            <li>Keep a record of your readings to track patterns and make necessary adjustments.</li>
        </ul>

        <h2>Medication and Insulin:</h2>
        <ul>
            <li>Take prescribed medications or insulin as directed by your healthcare provider.</li>
            <li>Follow a consistent schedule for medication administration.</li>
        </ul>

        <h2>Healthy Diet:</h2>
        <ul>
            <li>Work with a registered dietitian to develop a meal plan that helps control blood sugar levels.</li>
            <li>Focus on portion control, eat a variety of nutrient-rich foods, and limit the intake of sugar, refined carbohydrates, and saturated fats.</li>
        </ul>

        <h2>Regular Physical Activity:</h2>
        <ul>
            <li>Engage in regular exercise to help improve insulin sensitivity and manage blood sugar levels.</li>
            <li>Consult your doctor before starting a new exercise program to ensure it's safe for you.</li>
        </ul>

        

        </div>

        <div class="column">
            <h2>Weight Management:</h2>
            <ul>
                <li>Achieve and maintain a healthy weight as recommended by your healthcare provider.</li>
                <li>Weight loss can improve insulin sensitivity and help control diabetes.</li>
            </ul>

            <h2>Stress Management:</h2>
            <ul>
                <li>Chronic stress can affect blood sugar levels. Practice stress-reduction techniques like mindfulness, meditation, or yoga.</li>
            </ul>

            <h2>Regular Medical Check-ups:</h2>
            <ul>
                <li>Schedule regular check-ups with your healthcare team to monitor your diabetes and overall health.</li>
                <li>Address any concerns or changes in your condition promptly.</li>
            </ul>

        
            <h2>Hydration:</h2>
            <ul>
                <li>Stay well-hydrated by drinking water throughout the day.</li>
            </ul>

            <h2>Medication and Supplies:</h2>
            <ul>
                <li>Ensure you have an adequate supply of diabetes medications, testing supplies, and emergency snacks if needed.</li>
            </ul>
        </div>
    </body>
    </html>


    """,height=1250
    )
        
        
diabetesInfo()
