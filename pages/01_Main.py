import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import cv2
import numpy as np
import streamlit.components.v1 as components
import pages.A.Diabetes_Precaution as diabetes_precaution

st.set_page_config(
    page_title="Multiple Disease Detection App",
    page_icon="🤖",
    layout="wide",
)

result=''
selected =''
diseasename=''


# Load the diabetes model
with open('Models/diabetes_model_k.pkl', 'rb') as model_file:
    diabetes_model = pickle.load(model_file)

 #with open('Models/lung_cancer_model.pkl', 'rb') as model_file:
 #   lung_cancer_model = pickle.load(model_file)


# sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Detection System',
        ['Diabetes Detection', 'Heart Disease Detection', 'Lung Cancer Detection', "Precaution"],
        icons=['activity', 'heart', 'lungs-fill',""],
        default_index=0)

placeholder = st.empty()


st.markdown("""
        <style>

               .block-container {
                    padding-top: 0rem;
                    padding-bottom: 0rem;
                    padding-left: 0.1rem;
                    padding-right: 0.1rem;
                }
                section{
                    padding-top: 2rem;
                    padding-bottom: 0rem;
                    padding-left: -10rem;
                    padding-right: -10.1rem;
                }
                p {
                    font-weight: bold; /* Make the text bold */
                    font-size: 20px;  /* Adjust the font size as needed */
                    font-family: 'Times New Roman', Times, serif;
                }
                label {
                    font-weight: bold; /* Make the text bold */
                    font-size: 200rem;  /* Adjust the font size as needed */
                    font-family: 'Times New Roman', Times, serif;
                }
                span{
                    
                    font-family: 'Times New Roman', Times, serif;
                }
        </style>
        """, unsafe_allow_html=True)

##############################  Diabetes Detection Page ############################## 
if selected == 'Diabetes Detection':
    with placeholder.container():
        # page title
        st.title('Diabetes Detection Using ML')

        # getting the input data from the user
        col1, col2 = st.columns(2)

        with col1:
            Pregnancies = st.text_input("Pregnancies (0-17)")
            Glucose = st.text_input('Glucose Level (70-199 mg/dL)')
            BloodPressure = st.text_input('Blood Pressure value (60-200 Hg)')
            SkinThickness = st.text_input('Skin Thickness value (90-140 mm)')

        with col2:
            Insulin = st.text_input('Insulin Level (0-1000 μU/mL)')
            BMI = st.text_input('BMI value (18-50 kg/m2)')
            DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value (0.0-2.0)')
            Age = st.text_input('Age of the Person (14-100 years)')

        # code for Detection
        diab_diagnosis = ''

        # creating a button for Detection
        # Creating a button for Detection
        # ... (previous code)

        # creating a button for Detection
        if st.button('Diabetes Test Result'):
            # Check if any of the fields are not numeric, float, or decimal values
            def is_numeric(field):
                try:
                    float(field)
                    return True
                except ValueError:
                    return False

            numeric_fields = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]

            if all(is_numeric(field) for field in numeric_fields):
                diab_diagnosis = diabetes_model.predict([numeric_fields])
                
                if diab_diagnosis[0] == 1:
                    result = 'The person is diabetic'  
                    with placeholder.container():
                        st.write("### User Inputted Values:")
                        st.write(f"- Pregnancies: {Pregnancies}")
                        st.write(f"- Glucose Level: {Glucose} mg/dL")
                        st.write(f"- Blood Pressure: {BloodPressure} Hg")
                        st.write(f"- Skin Thickness: {SkinThickness} mm")
                        st.write(f"- Insulin Level: {Insulin} μU/mL")
                        st.write(f"- BMI value: {BMI} kg/m2")
                        st.write(f"- Diabetes Pedigree Function: {DiabetesPedigreeFunction}")
                        st.write(f"- Age of the Person: {Age} years")
                        st.success(result)
                        diabetes_precaution.diabetesInfo()
                else:
                    result = 'The person is not diabetic'
                    with placeholder.container():
                        st.write("### User Inputted Values:")
                        st.write(f"- Pregnancies: {Pregnancies}")
                        st.write(f"- Glucose Level: {Glucose} mg/dL")
                        st.write(f"- Blood Pressure: {BloodPressure} Hg")
                        st.write(f"- Skin Thickness: {SkinThickness} mm")
                        st.write(f"- Insulin Level: {Insulin} μU/mL")
                        st.write(f"- BMI value: {BMI} kg/m2")
                        st.write(f"- Diabetes Pedigree Function: {DiabetesPedigreeFunction}")
                        st.write(f"- Age of the Person: {Age} years")
                        st.success(result)
                        diabetes_precaution.diabetesInfo()
            else:
                st.error("All input fields should be numeric, float, or decimal values.")


############################## Heart Disease Detection Page ##############################
if selected == 'Heart Disease Detection':

    # page title
    st.title('Heart Disease Detection using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age (10-100 years)')
        sex = st.text_input('Sex (0:F, 1:M)')
        cp = st.text_input('Chest Pain types ')
        trestbps = st.text_input('Resting Blood Pressure')

    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
        restecg = st.text_input('Resting Electrocardiographic results')
        thalach = st.text_input('Maximum Heart Rate achieved')

    with col3:
        exang = st.text_input('Exercise Induced Angina')
        oldpeak = st.text_input('ST depression induced by exercise')
        slope = st.text_input('Slope of the peak exercise ST segment')

    # code for Detection
    
    # code for Detection
    heart_diagnosis = ''
    # creating a button for Detection
    # Creating a button for Detection
    if selected == 'Heart Disease Detection':
        # ... (previous code)

        # creating a button for Detection
        if st.button('Heart Disease Test Result'):
            # Check if any of the fields are not numeric, float, or decimal values
            def is_numeric(field):
                try:
                    float(field)
                    return True
                except ValueError:
                    return False

            numeric_fields = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope]

            if all(is_numeric(field) for field in numeric_fields):
                heart_diagnosis = heart_disease_model.predict([numeric_fields])
                if heart_diagnosis[0] == 1:
                    heart_diagnosis_text = 'The person is having heart disease'
                else:
                    heart_diagnosis_text = 'The person does not have any heart disease'
                st.success(heart_diagnosis_text)
            else:
                st.error("All input fields should be numeric, float, or decimal values.")


######################### Lung Cancer Detection Page #####################
if selected == 'Lung Cancer Detection':
    st.title("Lung Cancer Detection using ML")

    # Load your lung cancer detection model from a .pkl file
    #with open('Models/lung_cancer_model.pkl', 'rb') as model_file:
     # lung_cancer_model = pickle.load(model_file)

    # Upload an image file
    uploaded_image = st.file_uploader("Upload a lung X-ray image", type=["jpg", "png", "jpeg"])

    # page title
    st.title('Lung Cancer Detection using ML')

    # Check if an image is uploaded
    if uploaded_image is not None:
        # Read the content of the uploaded file as bytes
        image_bytes = uploaded_image.read()

        # Convert the image bytes to a NumPy array
        nparr = np.frombuffer(image_bytes, np.uint8)

        # Decode the NumPy array to an image
        image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        # Display the uploaded image
        st.image(image, caption="Uploaded Lung X-ray", use_column_width=True)


    else:
        st.warning("Please upload a lung X-ray image for analysis.")

# if selected == 'Precaution':
#     st.title("Please select", selected)
#     if diseasename == 'diabetes':
#         st.title('Precaution')
#         diabetes_precaution.diabetesInfo()


