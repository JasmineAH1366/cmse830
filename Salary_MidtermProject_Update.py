
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
    st.write("Let's start by viewing our data below.")
    view_data = st.checkbox("View Data :wrench:")
    if view_data:
        salary
        url = "https://www.kaggle.com/datasets/mohithsairamreddy/salary-data"
        st.caption(url)
        st.write("The data above has a total of 6,704 rows and 6 columns.")
    st.write("Let's check to see if there are any missing values in our dataset.")
    missing_values = st.checkbox("Missing Values :wrench:")
    if missing_values:
        mv = salary.loc[salary.isnull().any(axis=1)]    
        mv
        st.write("The data has a total of 6 rows that display missing data. Removing this data will not have a significant effect on our overall goal with the data. Thus, these rows will be deleted.")
    salary = salary.drop([172,260,2011,3136,5247,6455])
    st.write("Let's check for any inconsistent values.")
    incon_value = st.checkbox("Inconsistent Values :wrench:")   
    if incon_value:
        iv = salary['Education Level'].value_counts()
        iv
        st.write("As we can see above, there are inconsistent values. To fix this issue, we need to change the variables so that they can be consistent with one another. For example, Bachelor's and Bachelor's Degree should be one name since it is describing one degree. You can change it depending on your preference. For now, it will be changed to 'Bachelor's' and likewise for the other values.")
        salary['Education Level'].replace("Bachelor's Degree", "Bachelor's", inplace=True)
        salary['Education Level'].replace("Master's Degree", "Master's", inplace=True)
        salary['Education Level'].replace("phD","PhD",inplace=True)    
        st.write("The changes are below.")
        iv_new = salary['Education Level'].value_counts()
        iv_new
        st.write("We now have consistent values.")
        st.write("We have checked and taken care of all the maintenance. Let's Ride! :red_car:")
salary['Education Level'].replace("Bachelor's Degree", "Bachelor's", inplace=True)
salary['Education Level'].replace("Master's Degree", "Master's", inplace=True)
salary['Education Level'].replace("phD","PhD",inplace=True)
with tab3:
    st.write("Below is our new dataset.")
    salary
    st.write("Let's take a look at each column.")
    age_box = st.checkbox("Age")
    if age_box:
        age_range = salary.Age.unique()
        age_range.sort()
        age_range
        st.caption("OBSERVATION:")
        st.write("The ages of the participants range from 21 to 62 years old. ")
    gender_box = st.checkbox("Gender")
    if gender_box:
        gender_range = salary.Gender.unique()
        gender_range
        st.caption("OBSERVATION:")
        st.write("The input values in the Age column are Female, Male, and Other. Other may have been selected if participant does not identify as either male or female and/or chose to not share gender information.")
    edu_box = st.checkbox("Education Level")
    if edu_box:
        edu_range = salary['Education Level'].unique()
        edu_range
        st.caption("OBSERVATION:")
        st.write("The input values in the Education Level column are Bachelor's, Master's, PhD, and High School as we have seen in the previous tab.")
    job_box = st.checkbox("Job Title")
    if job_box:
        job_range = salary['Job Title'].unique()
        job_range
        st.caption("OBSERVATION:")
        st.write("There are a total of 191 Job Titles represented in this dataset.")
    yoe_box = st.checkbox("Years of Experience")
    if yoe_box:
        yoe_range = salary['Years of Experience'].unique()
        yoe_range.sort()
        yoe_range
        st.caption("OBSERVATION:")
        st.write("The input values in the Years of Experience column ranges from 0 to 34 years.")
    salary_box = st.checkbox("Salary")
    if salary_box:
        salary_range = salary["Salary"].unique()
        salary_range.sort()
        salary_range
        st.caption("OBSERVATION:")
        st.write("The salary amount ranges from \$350 to \$250,000.")
        st.write("Now, that we've taken a look at each column and have gained a better understanding of our data, we can continue our journey. As we continue our journey, let us not forget to enjoy the beautiful views.")
        st.write("Next, we will visually analyze our data. :red_car:")
with tab4:
    st.write("There are many ways that we can visually analyze our data.")
    st.write("Let's take it one stop at a time!")
    st.subheader(":octagonal_sign: FIRST STOP: PARTICIPANTS")
    st.write("Who all participated in this survey?")
    st.caption("In the last tab, we saw more of a range of the participants within in each column. Here, we will see a more in depth representation of the participants.")
    variable = st.selectbox("Choose a Variable", ["Age","Gender","Education Level","Job Title", "Years of Experience","Salary","All"])
    if variable == "Age":
        fig, ax = plt.subplots()
        salary['Age'].value_counts().plot(ax=ax, kind='bar', title='Age', ylabel='Frequency')
        st.pyplot(fig)
    if variable == "Gender":
        fig, ax = plt.subplots()
        salary['Gender'].value_counts().plot(ax=ax, kind='bar', title='Gender', ylabel='Frequency')
        st.pyplot(fig)
    if variable == "Education Level":
        fig, ax = plt.subplots()
        salary['Education Level'].value_counts().plot(ax=ax, kind='bar', title='Education Level', ylabel='Frequency')
        st.pyplot(fig)
    if variable == "Job Title":
        fig, ax = plt.subplots()
        salary['Job Title'].value_counts()[:10].plot(ax=ax, kind='bar', title='Job Title', ylabel='Frequency')
        st.pyplot(fig)
    if variable == "Years of Experience":
        fig, ax = plt.subplots()
        salary['Years of Experience'].value_counts().plot(ax=ax, kind='bar', title='Years of Experience', ylabel='Frequency')
        st.pyplot(fig)
    if variable == "Salary":
        fig, ax = plt.subplots()
        salary['Salary'].plot(kind='hist', title='Salary', ylabel='Frequency')
        st.pyplot(fig)
    if variable == "All":
        fig, axes = plt.subplots(nrows = 2, ncols=3, figsize=(25,16))
        salary['Age'].value_counts().plot(ax=axes[0,0], kind='bar', title='Age', ylabel='Frequency')
        salary['Gender'].value_counts().plot(ax=axes[0,1], kind='bar', title='Gender', ylabel='Frequency')
        salary['Education Level'].value_counts().plot(ax=axes[0,2], kind='bar', title='Education Level', ylabel='Frequency')
        salary['Job Title'].value_counts()[:10].plot(ax=axes[1,0], kind='bar', title='Job Title', ylabel='Frequency')
        salary['Years of Experience'].value_counts().plot(ax=axes[1,1], kind='bar', title='Years of Experience', ylabel='Frequency')
        salary['Salary'].plot(ax=axes[1,2],kind='hist', title='Salary', ylabel='Frequency')
        st.pyplot(fig, title= "Data Distribution")
    po = st.checkbox("Participant Observations")
    if po:
        st.markdown(
            """
            Most of the participants are:
            - 35 years old or younger
            - Male
            - Have Bachelor Degrees
            - Software Engineers and Data Scientists
            - Have 10 or less years of experience""")

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
    




