import streamlit as st
import pandas as pd
import os #for the purpose of file modification
import plotly_express as px
st.set_page_config(
    page_title="Event Registrartion Form",
    layout="centered"
    )

#Title and Description
tab1,tab2,tab3=st.tabs(["Registration form","Stats","Information"])





CSV_FILE = "user_data.csv"

def save_to_csv(name,email,cnic,contact,age,gender,event):
    new_data = pd.DataFrame({ #pd create krta h data frame #st data view krta h
        "Name":[name],
        "Email":[email],
        "CNIC":[cnic],
        "Contact":[contact],
        "Age":[age],
        "Gender":[gender],
        "Event":[event]
        })
    #check if file exit
    if os.path.exists(CSV_FILE):
        #append to exiting file
        existing_data= pd.read_csv(CSV_FILE)
        updated_data = pd.concat([existing_data,new_data], ignore_index=True)
        updated_data.to_csv(CSV_FILE, index=False)
    else:
        #create new file
        new_data.to_csv(CSV_FILE, index=False)    
    return True
with tab1:
    st.title("Event Registrartion Form")

#input form
    with st.form("Event Registrartion Form"):
        name=st.text_input("Name", placeholder="Enter Your Full name")
        email=st.text_input("Email",placeholder="Enter Your Email")
        cnic=st.text_input("CNIC",placeholder="for ex: 42101-5555555-9")
        contact=st.text_input("Contact",placeholder="for ex: 0330-38383838")
        age=st.number_input(label="Age",min_value=18,max_value=60)
        gender=st.selectbox(label="Gender",options=["male","female"])
        event=st.selectbox(label="Event",options=["workshop","comedy","confirance"])
        
        #form submission button

        submitted=st.form_submit_button("Register for Event")

        if submitted:
            #validation

            if not name or not email or not cnic or not contact or not age or not gender:
                st.error("❌ Please fill all the filed")
            else:
            #save to csv

                if save_to_csv(name,email,cnic,contact,age,gender,event):
                    st.success("Registration For the event has been saved")
                # st.balloons
                else:
                    st.error("Error Savings Data")
with tab2:
        st.header("Information")  
        if st.button("View Saved Data"):
            if os.path.exists(CSV_FILE):
                data=pd.read_csv(CSV_FILE) 
                st.dataframe(data)     
                
                
                csv=data.to_csv(index=False)
                st.download_button(
                    label="Download csv",
                    data=csv,
                    file_name="user_data.csv",
                    mime="test/csv"
                ) 
            else:
                st.info("No Data saved yet")              

with tab3:
    col1,col2 ,col3,col4,col5,col6,col7= st.columns(7)

    data=pd.read_csv(CSV_FILE)

    col1.metric(label="Total Registration",value=data["CNIC"].nunique())
    col2.metric(label="Average Age",value=data["Age"].mean())
    col3.metric(label="Total Male", value=(data["Gender"]=="male").sum())
    col4.metric(label="Total Female",value=(data["Gender"]=="female").sum())
    col5.metric(label="Total workshop",value=(data["Event"] =="workshop").sum())
    col6.metric(label="Total comedy register",value=(data["Event"] =="comedy").sum())
    col7.metric(label="Total confirance",value=(data["Event"] =="confirance").sum())


    df1=data["Gender"].value_counts().reset_index()

    fig=px.bar(df1,x="Gender",y="count", color="Gender")

    st.plotly_chart(fig)

    df2=data["Event"].value_counts().reset_index()
    df2.columns=["Event", "count"]
    fig = px.pie(
        df2,
        names="Event",
        values="count",
        title="Total Registrations by Event"
    )

    st.plotly_chart(fig)