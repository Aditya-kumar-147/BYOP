import streamlit as st
import pickle

# Streamlit app Random forest

random_model=pickle.load(open('log_model.pkl','rb'))

def classify(num):
    if num == 0:
        return 'Safe'
    else:
        return 'Not Safe'
    
def main():

    html_temp = """
    <div style="background-color:teal ; padding:10px">
    <h2 style="color:white; text-align:center;">CVD Prediction </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    tem2 = """
    <style>
    body {
        background-color: green; 
    }
    </style>
    """
    st.markdown(tem2, unsafe_allow_html=True)

    gender=st.radio("Select your gender", ['Male','Female'])
    if gender is 'Male':
        gender = 1
    else:
        gender = 0
    height=st.number_input("Enter your height (cms)",value=0.1)
    weight=st.number_input("Enter your weight (Kgs)")
    height = height/100
    
    bmi = weight / (height ** 2)
    if height > 0:
        bmi = weight / (height ** 2)
        st.write(f"BMI calculated: ",round(bmi, 2))
    else:
        st.write("Please enter a valid height greater than zero.")
    ap_hi=st.number_input("Enter your systolic blood pressure (ap_hi)")
    ap_lo=st.number_input("Enter your diastolic blood pressure (ap_lo)")

    map = ( ( 2 * ap_lo) + ap_hi ) / 3
 
    years = st.number_input("Enter your age (Yrs)")

    if years >= 0 and years <= 20:
        age_bin =  0
    elif years > 20 and years <= 30:
        age_bin =  1
    elif years > 30 and years <= 35:
        age_bin =  2
    elif years > 35 and years <= 40:
        age_bin =  3
    elif years > 40 and years <= 45:
        age_bin =  4
    elif years > 45 and years <= 50:
        age_bin =  5
    elif years > 50 and years <= 55:
        age_bin =  6
    elif years > 55 and years <= 60:
        age_bin =  7
    elif years > 60 and years <= 65:
        age_bin =  8
    elif years > 65 and years <= 70:
        age_bin =  9
    elif years > 70 and years <= 75:
        age_bin =  10
    elif years > 75 and years <= 80:
        age_bin =  11
    elif years > 80 and years <= 85:
        age_bin =  12
    elif years > 85 and years <= 90:
        age_bin =  13
    elif years > 90 and years <= 95:
        age_bin =  14
    elif years > 95 and years <= 100:
        age_bin =  15
    else:
        return 'Invalid Age Range'
    
    if bmi < 18.5 :
        bmi_class = 1  #UnderWeight
    elif bmi > 18.5 and bmi  < 24.9:   
        bmi_class = 2  #NormalWeight
    elif bmi > 24.9 and bmi < 29.9:  
        bmi_class = 3  #OverWeight
    elif bmi > 29.9 and bmi < 34.9:  
        bmi_class = 4  #ClassObesity_1
    elif bmi > 34.9 and bmi < 39.9:  
        bmi_class = 5  #ClassObesity_2
    elif bmi > 39.9 and bmi < 49.9:  
        bmi_class = 6  #ClassObesity_3
    elif bmi > 49.9:  
        bmi_class = 'Error'
        
    else:           
        bmi_class = 'Not_Rated'


    if map < 69.9:    
        map_class = 1 #Low
    elif map > 70 and map  < 79.9:   
        map_class = 2 #Normal
    elif map > 79.9 and map < 89.9:  
        map_class = 3 #Normal
    elif map > 89.9 and map < 99.9:  
        map_class = 4#Normal
    elif map > 99.9 and map < 109.9:  
        map_class = 5 #High
    elif map > 109.9 and map < 119.9:  
        map_class = 6 #Normal
    elif map > 119.9:  
        map_class = 7
        
    else:           
        map_class = 0


    chol=st.radio("Select your Cholestrol Level", ['Normal','Above Normal','Well above Normal'])
    if chol is 'Normal':
        chol = 1
    elif chol is 'Above Normal':
        chol = 2
    else:
        chol = 3
    gluc=st.radio("Select your Glucose Level (1-Normal, 2-Above Normal,3-Well Above Normal)", ['Normal','Above Normal','Well above Normal'])
    if gluc is 'Normal':
        gluc = 1
    elif gluc is 'Above Normal':
        gluc = 2
    else:
        gluc = 3
    smoke=st.radio("Do you smoke?", ['Yes','No'])
    if smoke is 'Yes':
        smoke = 1
    else:
        smoke = 0
    active=st.radio("Are you physically acitve?", ['Yes','No'])
    if active is 'Yes':
        active = 1
    else:
        active = 0

    inputs = [[gender,height,weight,bmi,ap_hi,ap_lo,map,years,age_bin,bmi_class,map_class,chol,gluc,smoke,active]]

    if st.button('Predict'):#button name is Classify
        st.success(classify(random_model.predict(inputs)))

if __name__ == "__main__":
    main()
