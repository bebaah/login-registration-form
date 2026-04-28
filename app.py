import streamlit as st
import pandas as pd
import os   #operating system  #if problemso "pip install os"  #os ka package local file ko handlekrne ka hota hai

st.set_page_config(
    page_title="EVENT REGISTRATION FORM",
    layout="centered"
)
#Title & Description

st.title("EVENT REGISTRATION FORM")


CSV_FILE ="user_data.csv"  #oska istemal krk filecreate krwainge k jb user datadaly ga tw csv fileme save hga uska data jkr

def save_to_csv(name,email,cnic,contact,age,gender):
    new_data=pd.DataFrame({
        "Name":[name],              #dictionaries me li h keys  #column ka naam key hota hai
        "Email":[email],
        "Cnic":[cnic],
        "Contact":[contact],
        "Age":[age],
        "Gender":[gender]
    })
#check if file exists
    if os.path.exists(CSV_FILE):  #agr CSV_FILE exist h tw  #os system k path mejkr ekho agr fileexist krti h tw yh wlakamkro

        #append to existing file

        existing_data=pd.read_csv(CSV_FILE)  #concat krenge
        updated_data =pd.concat([existing_data,new_data],ignore_index=True)   #index nahi bnyga ignore krwadengy 

        updated_data.to_scv(CSV_FILE, index=False)  #false islielikha kiu k pandas k dataframeme woh ek unamed column bna k serial number dedegajo k nhi chhye

    else:
        new_data.to_csv(CSV_FILE, index=False)  #new data k andr save horah data or woh csv me jkrsave hojyga

        return True     #ni krengy tw jitne function die v tw NONE determine krdega

#input form

with st.form("Even Registration Form"): #with naya block dene klie likha
    name=st.text_input("Name",placeholder="Enter your Full Name")
    email=st.text_input("Email",placeholder="Enter your Email")
    cnic=st.text_input("CNIC",placeholder="for ex: 42201-5555555-9")
    contact=st.text_input("Contact",placeholder="for ex: 92 00000000000")
    age=st.number_input(label="Age",min_value=18 ,max_value=60)
    gender=st.selectbox(label="Gender",options=["Male","Female"])


    #form submission button

    submitted=st.form_submit_button("Register For Event")

    if submitted:

        #validation

        if not name or not email or not cnic or not contact or not age or not gender:
            st.error("Please Fill All The Fields")

        else:
            #save to CSV 

            if save_to_csv(name,email,cnic,contact,age,gender):
                st.success("REGISTRATION FOR THE EVENT HAS BEEN SAVED")
            else:
                st.error("ERROR SAVING DATA")












