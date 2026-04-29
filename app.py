import streamlit as st
import pandas as pd
import os #for the purpose of file modification
import plotly.express as px


st.set_page_config(
    page_title="Event Registration Form",
    layout="centered"
    )

#Title and Description

st.title("Event Registration Form")



CSV_FILE = "user_data.csv"


def save_to_csv(name,email,cnic,contact,age,gender):

    new_data = pd.DataFrame({
        "Name":[name],
        "Email":[email],
        "CNIC":[cnic],
        "Contact":[contact],
        "Age" :[age],
        "Gender":[gender]

    })

    #check if file exist
    if os.path.exists(CSV_FILE):
        # append to existing file
        existing_data= pd.read_csv(CSV_FILE)
        updated_data = pd.concat([existing_data,new_data], ignore_index=True)
        updated_data.to_csv(CSV_FILE, index=False)

    else:
        #Create New File
        new_data.to_csv(CSV_FILE, index=False)

    return True


#input form

with st.form("Event Registration Form"):
   
    name=st.text_input("Name",placeholder="Enter your Full Name")
    email=st.text_input("Email",placeholder="Enter your Email")
    cnic=st.text_input("CNIC",placeholder="for ex: 42201-5555555-9")
    contact=st.text_input("Contact",placeholder="For Ex: +92 30000000")
    age=st.number_input(label="Age",min_value=18,max_value=60)
    gender=st.selectbox(label="Gender",options=["Male","Female"])

    #form Submissiion button

    submitted=st.form_submit_button("Register for Event")

    if submitted:

        #validation

        if not name or not email or not cnic or not contact or not age or not gender:
            st.error("❌ Please Fill all the fields")
        else:

            # save to CSV

            if save_to_csv(name,email,cnic,contact,age,gender):
                st.success("Registration for the Event has been saved")
                st.balloons()
            else:
                st.error("Error Saving Data")

with st.sidebar: #creating sidebar for the purpose to see user data
    st.header("Information") #for header in streamlit
    if st.button("View Saved Data"):
        if os.path.exists(CSV_FILE):
            data=pd.read_csv(CSV_FILE)
            st.dataframe(data)


            csv=data.to_csv(index=False)
            st.download_button(
                label="Download CSV",
                data=csv,
                file_name="user_data.csv",
                mime="text/csv"
            )

        else:
            st.info("No Data saved yet")


col1,col2,col3,col4 =st.columns(4)

data=pd.read_csv(CSV_FILE)

col1.metric(label="Total Registrations",value=data["CNIC"].nunique())

col2.metric(label="Average Age",value=data["Age"].mean())

col3.metric(label="Total Male", value=(data["Gender"]=="Male").sum())

col4.metric(label="Total Female",value=(data["Gender"]=="Female").sum())


