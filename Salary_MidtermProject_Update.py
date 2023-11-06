
import streamlit as st
import pandas as pd
import altair as alt
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image

#Data
salary = pd.read_csv("Salary_Data.csv")
#Title
st.title("A ROADTRIP TO SUCCESS :red_car:")

#Tab Order and Names
tab1, tab2, tab3, tab4, tab5 = st.tabs(["Buckle Up: Introduction", "Maintenance: Data", "Let's Ride!", "Add a Stop: Discovery", "And the Journey Continues..."])

#Tab1
with tab1: 
    col11, col12 = st.columns(2)
    with col11:
        image1 = Image.open("path.jpg")
        image1_new = image1.resize((600,400))
        st.image(image1_new)
    with col12:
        st.write("What do you want to do? What are your next steps? These are just some of the many questions we get asked when deciding what to do with our life.  Choosing a career can be a difficult decision for some and for others, it can be a fairly easy decision. Whether you know the next steps to take, decided to just go with the flow and see what happens, or maybe something in between, it's a choice we all have to make.")
    st.write("Worried? No need to be. Let's start here! This app will present you with an opportunity to see various career fields. It will further show you how much you could make depending on gender, level of education, and years of experience.")
    st.write("This app should only serve the purpose of just being a piece, if not the start, of your exploration. Furthermore, I advise you to continue to research your desired career field(s) (whether listed here or not), locate others who are in or may have been in this particular field, connect and network, recognize their degree(s) and/or experience, and whatever more you deem to be necessary. Lastly, see how you can apply it your life. Is it applicable? Yes, it is. It is applicable in your very own way. Your path may not look exactly like someone else's, but nevertheless you will still make it to your destination.")
    col111, col112 = st.columns(2)
    with col111:
        st.write("Your journey to success awaits you!")
        st.write("Continue to go through this app by navigating to the next following tabs:")
        st.markdown("**Maintenance: Data**")  
        st.markdown("**Let's Ride!**")
        st.markdown("**Add a Stop: Discovery**")
        st.markdown("**And the Journey Continues...**")
    with col112:
        image2 = Image.open("success.jpg")
        st.image(image2)
with tab2:
    st.write("Before we start our journey, we need to make sure everything is fit for a safe trip. ")
    st.write(":wrench: View Data")
    salary
    url = "https://www.kaggle.com/datasets/mohithsairamreddy/salary-data"
    st.caption(url)
    st.write("The data above has a total of 6,704 rows and 6 columns.")
    st.write(":red_car: Missing Values")
    salary.loc[salary.isnull().any(axis=1)]    
    st.write("The data has a total of 6 rows that display missing data. Removing this data will not have a significant effect on our overall goal with the data. Thus these rows will be deleted.")
    salary = salary.drop([172,260,2011,3136,5247,6455])
    st.write(":red_car: Entries")
    salary['Education Level'].replace("Bachelor's Degree", "Bachelor's", inplace=True)
    salary['Education Level'].replace("Master's Degree", "Master's", inplace=True)
    salary['Education Level'].replace("phD","PhD",inplace=True)
    st.write("Some variable entries were altered so that we can have consistent entries. This is important when grouping.")
    st.write("The following changes were made:")
    st.markdown("**Bachelor's Degree to Bachelor's**")
    st.markdown("**Master's Degree to Master's**")
    st.markdown("**phD to PhD**")
    st.write("We have checked and taken care of all the maintenance. Let's Ride! :red_car:")
with tab3:
    st.write("Below is our new dataset.")
    salary
    st.write("Along our journey, let us not forget to enjoy the beautiful views.")
    st.write("Next, we will visually analyze our data. :red_car:")
with tab4:
    st.write("There are many ways that we can visually analyze our data.")
    st.write("Let's break it down into 2 subsections: **Gender** and **Education Level**")
    st.header("GENDER")
    gender = st.selectbox("Choose a Gender", ["Female", "Male", "Other"])
    female = salary.query("Gender == 'Female'")
    if gender == "Female":
        female = salary.query("Gender == 'Female'")
        female
        st.caption("There are 3013 rows.")
    elif gender == "Male":
        male = salary.query("Gender == 'Male'")
        male
        st.caption("There are 3671 rows.")
    elif gender == "Other":
        other = salary.query("Gender == 'Other'")
        other
        st.caption("There are 14 rows.")
    




