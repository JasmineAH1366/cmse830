
import streamlit as st
import pandas as pd
import altair as alt
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image
import plotly.express as px
from sklearn.model_selection import train_test_split



#Data
salary = pd.read_csv("C:\\Users\\12058\\OneDrive\\Documents\\CMSE 830 - Foundations of Data Science\\Datasets\\Salary_Data.csv")


#Title
st.title("A ROADTRIP TO SUCCESS :red_car:")

#Tab Order and Names
tab1, tab2, tab3, tab4, tab5 = st.tabs(["Buckle Up: Introduction", "Maintenance: Data", "Let's Ride!", "Add a Stop: Discovery", "And the Journey Continues..."])

#Tab1
with tab1: 
    col11, col12 = st.columns(2)
    with col11:
        image1 = Image.open("C:\\Users\\12058\\OneDrive\\Documents\\CMSE 831 - Computational Optimization\\Homework\\path.jpg")
        image1_new = image1.resize((600,400))
        st.image(image1_new)
    with col12:
        st.write("What do you want to do? What are your next steps? These are just some of the many questions we get asked when deciding what to do with our life.  Choosing a career can be a difficult decision for some and for others, it can be a fairly easy decision. Whether you know the next steps to take, decided to just go with the flow and see what happens, or maybe something in between, it's a choice we all have to make.")
    st.write("Worried? No need to be. Let's start here! This app will present you with an opportunity to see various career fields. It will further show you how much you could make depending on age, gender, level of education, and years of experience.")
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
        image2 = Image.open("C:\\Users\\12058\\OneDrive\\Documents\\CMSE 831 - Computational Optimization\\Homework\\success.jpg")
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
        st.write("The input values in the Gender column are Female, Male, and Other. Other may have been selected if participant does not identify as either male or female and/or chose to not share gender information.")
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
salary['Age'] = salary['Age'].astype('int')
salary['Years of Experience'] = salary['Years of Experience'].astype('int')
with tab4:
    st.write("There are many ways that we can visually analyze our data.")
    st.write("Let's take it one stop at a time!")
    st.subheader(":octagonal_sign: FIRST STOP: PARTICIPANTS")
    st.write("Who all participated in this survey?")
    st.caption("In the last tab, we saw more of a range of the participants within in each column. Here, we will see a more in depth representation of the participants.")
    st.markdown(
        """
        **NOTE:** Frequency (y-axis) of each plot is the amount of participants in this dataset. 
        """)
    variable = st.selectbox("Choose a Variable", ["Age","Gender","Education Level","Job Title", "Years of Experience","Salary","All"])
    order_age = salary['Age'].value_counts().sort_index()
    order_yoe = salary['Years of Experience'].value_counts().sort_index()
    if variable == "Age":
        fig, ax = plt.subplots()
        order_age.plot(ax=ax, kind='bar', title='Age', ylabel='Frequency')
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
        st.caption("Displayed are the Top 10 Job Titles, ranked based on the number of participants who have chosen each title as their career. It is listed from highest to lowest amount of participants. ")
    if variable == "Years of Experience":
        fig, ax = plt.subplots()
        order_yoe.plot(ax=ax, kind='bar', title='Years of Experience', xlabel = 'Years of Experience', ylabel='Frequency')
        st.pyplot(fig)
    if variable == "Salary":
        fig, ax = plt.subplots()
        salary['Salary'].plot(kind='hist', bins=25, edgecolor="black", title='Salary', ylabel='Frequency')
        st.pyplot(fig)
    if variable == "All":
        fig, axes = plt.subplots(nrows = 2, ncols=3, figsize=(30,20))
        order_age.plot(ax=axes[0,0], kind='bar', title='Age', ylabel='Frequency')
        salary['Gender'].value_counts().plot(ax=axes[0,1], kind='bar', title='Gender', ylabel='Frequency')
        salary['Education Level'].value_counts().plot(ax=axes[0,2], kind='bar', title='Education Level', ylabel='Frequency')
        salary['Job Title'].value_counts()[:10].plot(ax=axes[1,0], kind='bar', title='Job Title', ylabel='Frequency')
        order_yoe.plot(ax=axes[1,1], kind='bar', title='Years of Experience', ylabel='Frequency')
        salary['Salary'].plot(ax=axes[1,2],kind='hist', bins=25, edgecolor="black", title='Salary', ylabel='Frequency')
        st.pyplot(fig)
    po = st.checkbox(":large_green_circle: Participant Observations")
    if po:
        st.markdown(
            """
            Most of the participants are:
            - 35 years old or younger
            - Male
            - Have Bachelor Degrees
            - Software Engineers and Data Scientists
            - Have 10 or less years of experience
            - Have a salary amount between \$50,000.00 to \$60,000.00 """)
    st.subheader(":octagonal_sign: SECOND STOP: JOB TITLES")
    st.write("In this section, we will focus on the Top 10 Job Titles presented in this dataset.")
    st.markdown(
        """
        Select a Job Title.  
        Within that specific job title, you will see the distribution of the following variables:
        - Age
        - Gender
        - Education Level 
        - Years of Experience
        - Salary """)
    st.markdown(""" NOTE: _This should be used for inspirational purposes only._""")
    bin_edges = [50000,55000,60000,65000,70000,75000,80000,85000,90000,95000,100000,105000,110000,115000,120000,125000,130000,135000,140000,145000,150000,155000,160000,165000,170000,175000,180000,185000,190000,195000,200000,205000,210000,215000,220000,225000,230000,235000,240000,245000,250000]
    jt = st.selectbox("Select a Job Title", ["Software Engineer","Data Scientist","Software Engineer Manager","Data Analyst","Senior Project Engineer","Product Manager","Full Stack Engineer","Marketing Manager","Back End Developer","Senior Software Engineer"])
    if jt == "Software Engineer":
        se = salary[(salary["Job Title"] == "Software Engineer")]
        se
        order_age_se = se['Age'].value_counts().sort_index()
        order_yoe_se = se['Years of Experience'].value_counts().sort_index()
        st.write("There are a total of 518 Software Engineers.")
        fig, axes = plt.subplots(nrows = 1, ncols=3, figsize=(16,6))
        order_age_se.plot(ax=axes[0], kind='bar', title='Age', ylabel='Frequency')
        se['Gender'].value_counts().plot(ax=axes[1], kind='bar', title='Gender', ylabel='Frequency')
        se['Education Level'].value_counts().plot(ax=axes[2], kind='bar', title='Education Level', ylabel='Frequency')
        st.pyplot(fig, title= "Software Engineer")
        fig, axes = plt.subplots(nrows = 1, ncols=2, figsize=(16,6))
        order_yoe_se.plot(ax=axes[0], kind='bar', title='Years of Experience', ylabel='Frequency')
        se['Salary'].plot(ax=axes[1],kind='hist',bins=bin_edges, edgecolor="black", title='Salary', ylabel='Frequency')
        st.pyplot(fig)
        seo = st.checkbox(":large_green_circle: Software Engineer Observations")
        if seo:
            st.markdown(
                """ 
                Most of the Software Engineers are:
                - 27 years of age
                - Male
                - Have a Bachelor's Degree
                - Have 4 years of experience
                - Have a salary amount between \$160,000.00 to \$165,000.00""")
    if jt == "Data Scientist":
        ds = salary[(salary["Job Title"] == "Data Scientist")]
        ds
        order_age_ds = ds['Age'].value_counts().sort_index()
        order_yoe_ds = ds['Years of Experience'].value_counts().sort_index()
        st.write("There are a total of 453 Data Scientsts.")
        fig, axes = plt.subplots(nrows = 1, ncols=3, figsize=(16,6))
        order_age_ds.plot(ax=axes[0], kind='bar', title='Age', ylabel='Frequency')
        ds['Gender'].value_counts().plot(ax=axes[1], kind='bar', title='Gender', ylabel='Frequency')
        ds['Education Level'].value_counts().plot(ax=axes[2], kind='bar', title='Education Level', ylabel='Frequency')
        st.pyplot(fig, title= "Data Scientist")
        fig, axes = plt.subplots(nrows = 1, ncols=2, figsize=(16,6))
        order_yoe_ds.plot(ax=axes[0], kind='bar', title='Years of Experience', ylabel='Frequency')
        ds['Salary'].plot(ax=axes[1],kind='hist',bins=bin_edges, edgecolor="black", title='Salary', ylabel='Frequency')
        st.pyplot(fig)
        dso = st.checkbox(":large_green_circle: Data Scientist Observations")
        if dso:
            st.markdown(
                """ 
                Most of the Data Scientists are:
                - 30 years of age
                - Male
                - Have a PhD
                - Have 6 years of experience
                - Have a salary amount between \$140,000.00 to \$145,000.00""")        
    if jt == "Software Engineer Manager":
        sem = salary[(salary["Job Title"] == "Software Engineer Manager")]
        sem
        order_age_sem = sem['Age'].value_counts().sort_index()
        order_yoe_sem = sem['Years of Experience'].value_counts().sort_index()
        st.write("There are a total of 376 Software Engineer Managers.")
        fig, axes = plt.subplots(nrows = 1, ncols=3, figsize=(16,6))
        order_age_sem.plot(ax=axes[0], kind='bar', title='Age', ylabel='Frequency')
        sem['Gender'].value_counts().plot(ax=axes[1], kind='bar', title='Gender', ylabel='Frequency')
        sem['Education Level'].value_counts().plot(ax=axes[2], kind='bar', title='Education Level', ylabel='Frequency')
        st.pyplot(fig)
        fig, axes = plt.subplots(nrows = 1, ncols=2, figsize=(16,6))
        order_yoe_sem.plot(ax=axes[0], kind='bar', title='Years of Experience', ylabel='Frequency')
        sem['Salary'].plot(ax=axes[1],kind='hist', bins=bin_edges, edgecolor="black", title='Salary', ylabel='Frequency')
        st.pyplot(fig)
        semo = st.checkbox(":large_green_circle: Software Engineer Manager Observations")
        if semo:
            st.markdown(
                """ 
                Most of the Software Engineer Managers are:
                - 54 years of age
                - Male
                - Have a PhD
                - Have 16 years of experience
                - Have a salary amount between \$185,000.00 to \$190,000.00""")       
    if jt == "Data Analyst":
        da = salary[(salary["Job Title"] == "Data Analyst")]
        da
        order_age_da = da['Age'].value_counts().sort_index()
        order_yoe_da = da['Years of Experience'].value_counts().sort_index()
        st.write("There are a total of 363 Data Analysts.")
        fig, axes = plt.subplots(nrows = 1, ncols=3, figsize=(16,6))
        order_age_da.plot(ax=axes[0], kind='bar', title='Age', ylabel='Frequency')
        da['Gender'].value_counts().plot(ax=axes[1], kind='bar', title='Gender', ylabel='Frequency')
        da['Education Level'].value_counts().plot(ax=axes[2], kind='bar', title='Education Level', ylabel='Frequency')
        st.pyplot(fig)
        fig, axes = plt.subplots(nrows = 1, ncols=2, figsize=(16,6))
        order_yoe_da.plot(ax=axes[0], kind='bar', title='Years of Experience', ylabel='Frequency')
        da['Salary'].plot(ax=axes[1],kind='hist',bins=bin_edges, edgecolor="black", title='Salary', ylabel='Frequency')
        st.pyplot(fig)
        dao = st.checkbox(":large_green_circle: Data Analyst Observations")
        if dao:
            st.markdown(
                """ 
                Most of the Data Analysts are:
                - 25 years of age
                - Male
                - Have a Bachelor's Degree
                - Have 2 years of experience
                - Have a salary amount between \$100,000.00 to \$105,000.00""")   
    if jt == "Senior Project Engineer":
        spe = salary[(salary["Job Title"] == "Senior Project Engineer")]
        spe
        order_age_spe = spe['Age'].value_counts().sort_index()
        order_yoe_spe = spe['Years of Experience'].value_counts().sort_index()
        st.write("There are a total of 318 Senior Project Engineer.")
        fig, axes = plt.subplots(nrows = 1, ncols=3, figsize=(16,6))
        order_age_spe.plot(ax=axes[0], kind='bar', title='Age', ylabel='Frequency')
        spe['Gender'].value_counts().plot(ax=axes[1], kind='bar', title='Gender', ylabel='Frequency')
        spe['Education Level'].value_counts().plot(ax=axes[2], kind='bar', title='Education Level', ylabel='Frequency')
        st.pyplot(fig)
        fig, axes = plt.subplots(nrows = 1, ncols=2, figsize=(16,6))
        order_yoe_spe.plot(ax=axes[0], kind='bar', title='Years of Experience', ylabel='Frequency')
        spe['Salary'].plot(ax=axes[1],kind='hist',bins=bin_edges, edgecolor="black", title='Salary', ylabel='Frequency')
        st.pyplot(fig)
        speo = st.checkbox(":large_green_circle: Senior Project Engineer Observations")
        if speo:
            st.markdown(
                """ 
                Most of the Data Analysts are:
                - 43 years of age
                - Male
                - Have a PhD
                - Have 16 years of experience
                - Have a salary amount between \$185,000.00 to \$190,000.00""")  
    if jt == "Product Manager":
        pm = salary[(salary["Job Title"] == "Product Manager")]
        pm
        order_age_pm = pm['Age'].value_counts().sort_index()
        order_yoe_pm = pm['Years of Experience'].value_counts().sort_index()
        st.write("There are a total of 313 Product Managers.")
        fig, axes = plt.subplots(nrows = 1, ncols=3, figsize=(16,6))
        order_age_pm.plot(ax=axes[0], kind='bar', title='Age', ylabel='Frequency')
        pm['Gender'].value_counts().plot(ax=axes[1], kind='bar', title='Gender', ylabel='Frequency')
        pm['Education Level'].value_counts().plot(ax=axes[2], kind='bar', title='Education Level', ylabel='Frequency')
        st.pyplot(fig)
        fig, axes = plt.subplots(nrows = 1, ncols=2, figsize=(16,6))
        order_yoe_pm.plot(ax=axes[0], kind='bar', title='Years of Experience', ylabel='Frequency')
        pm['Salary'].plot(ax=axes[1],kind='hist', bins=bin_edges, edgecolor="black", title='Salary', ylabel='Frequency')
        st.pyplot(fig)
        pmo = st.checkbox(":large_green_circle: Product Manager Observations")
        if pmo:
            st.markdown(
                """ 
                Most of the Product Managers are:
                - 32 years of age
                - Male
                - Have a Bachelor's Degree
                - Have 7 years of experience
                - Have a salary amount between \$195,000.00 to \$200,000.00""") 
    if jt == "Full Stack Engineer":
        fse = salary[(salary["Job Title"] == "Full Stack Engineer")]
        fse
        order_age_fse = fse['Age'].value_counts().sort_index()
        order_yoe_fse = fse['Years of Experience'].value_counts().sort_index()
        st.write("There are a total of 308 Full Stack Engineers.")
        fig, axes = plt.subplots(nrows = 1, ncols=3, figsize=(16,6))
        order_age_fse.plot(ax=axes[0], kind='bar', title='Age', ylabel='Frequency')
        fse['Gender'].value_counts().plot(ax=axes[1], kind='bar', title='Gender', ylabel='Frequency')
        fse['Education Level'].value_counts().plot(ax=axes[2], kind='bar', title='Education Level', ylabel='Frequency')
        st.pyplot(fig)
        fig, axes = plt.subplots(nrows = 1, ncols=2, figsize=(16,6))
        order_yoe_fse.plot(ax=axes[0], kind='bar', title='Years of Experience', ylabel='Frequency')
        fse['Salary'].plot(ax=axes[1],kind='hist', bins=bin_edges, edgecolor="black", title='Salary', ylabel='Frequency')
        st.pyplot(fig)
        fseo = st.checkbox(":large_green_circle: Full Stack Engineer Observations")
        if fseo:
            st.markdown(
                """ 
                Most of the Full Stack Engineers are:
                - 33 years of age
                - Female
                - Have a Master's Degree
                - Have 6 years of experience
                - Have a salary amount between \$115,000.00 to \$120,000.00""") 
    if jt == "Marketing Manager":
        mm = salary[(salary["Job Title"] == "Marketing Manager")]
        mm
        order_age_mm = mm['Age'].value_counts().sort_index()
        order_yoe_mm = mm['Years of Experience'].value_counts().sort_index()
        st.write("There are a total of 255 Marketing Managers.")
        fig, axes = plt.subplots(nrows = 1, ncols=3, figsize=(16,6))
        order_age_mm.plot(ax=axes[0], kind='bar', title='Age', ylabel='Frequency')
        mm['Gender'].value_counts().plot(ax=axes[1], kind='bar', title='Gender', ylabel='Frequency')
        mm['Education Level'].value_counts().plot(ax=axes[2], kind='bar', title='Education Level', ylabel='Frequency')
        st.pyplot(fig)
        fig, axes = plt.subplots(nrows = 1, ncols=2, figsize=(16,6))
        order_yoe_mm.plot(ax=axes[0], kind='bar', title='Years of Experience', ylabel='Frequency')
        mm['Salary'].plot(ax=axes[1],kind='hist', bins=bin_edges, edgecolor="black", title='Salary', ylabel='Frequency')
        st.pyplot(fig)
        mmo = st.checkbox(":large_green_circle: Marketing Manager Observations")
        if mmo:
            st.markdown(
                """ 
                Most of the Marketing Managers are:
                - 33 years of age
                - Female
                - Have a Master's Degree
                - Have 9 years of experience
                - Have a salary amount between \$130,000.00 to \$135,000.00""") 
    if jt == "Back End Developer":
        bed = salary[(salary["Job Title"] == "Back end Developer")]
        bed
        order_age_bed = bed['Age'].value_counts().sort_index()
        order_yoe_bed = bed['Years of Experience'].value_counts().sort_index()
        st.write("There are a total of 244 Back End Developers.")
        fig, axes = plt.subplots(nrows = 1, ncols=3, figsize=(16,6))
        order_age_bed.plot(ax=axes[0], kind='bar', title='Age', ylabel='Frequency')
        bed['Gender'].value_counts().plot(ax=axes[1], kind='bar', title='Gender', ylabel='Frequency')
        bed['Education Level'].value_counts().plot(ax=axes[2], kind='bar', title='Education Level', ylabel='Frequency')
        st.pyplot(fig)
        fig, axes = plt.subplots(nrows = 1, ncols=2, figsize=(16,6))
        order_yoe_bed.plot(ax=axes[0], kind='bar', title='Years of Experience', ylabel='Frequency')
        bed['Salary'].plot(ax=axes[1],kind='hist',bins=bin_edges, edgecolor="black", title='Salary', ylabel='Frequency')
        st.pyplot(fig)
        bedo = st.checkbox(":large_green_circle: Back End Developer Observations")
        if bedo:
            st.markdown(
                """ 
                Most of the Back End Developers are:
                - 27 years of age
                - Male
                - Have a Bachelor's Degree
                - Have 3 years of experience
                - Have a salary amount between \$100,000.00 to \$105,000.00""") 
    if jt == "Senior Software Engineer":
        sse = salary[(salary["Job Title"] == "Senior Software Engineer")]
        sse
        order_age_sse = sse['Age'].value_counts().sort_index()
        order_yoe_sse = sse['Years of Experience'].value_counts().sort_index()
        st.write("There are a total of 244 Senior Software Engineers.")
        fig, axes = plt.subplots(nrows = 1, ncols=3, figsize=(16,6))
        order_age_sse.plot(ax=axes[0], kind='bar', title='Age', ylabel='Frequency')
        sse['Gender'].value_counts().plot(ax=axes[1], kind='bar', title='Gender', ylabel='Frequency')
        sse['Education Level'].value_counts().plot(ax=axes[2], kind='bar', title='Education Level', ylabel='Frequency')
        st.pyplot(fig)
        fig, axes = plt.subplots(nrows = 1, ncols=2, figsize=(16,6))
        order_yoe_sse.plot(ax=axes[0], kind='bar', title='Years of Experience', ylabel='Frequency')
        sse['Salary'].plot(ax=axes[1],kind='hist', bins=bin_edges, edgecolor="black", title='Salary', ylabel='Frequency')
        st.pyplot(fig)
        sseo = st.checkbox(":large_green_circle: Senior Software Engineer Observations")
        if sseo:
            st.markdown(
                """ 
                Most of the Senior Software Engineers are:
                - 42 years of age
                - Male
                - Have a Master's Degree
                - Have 7 years of experience
                - Have a salary amount between \$170,000.00 to \$175,000.00""") 
    st.write("We have completed all of our stops and now we're ready to continue our journey.:red_car:")
with tab5:
    st.write("Hopeful that this has been a great roadtrip so far. Remember that this is only the start of your journey. Continue this journey by discovering your interests, researching careers and career paths, connecting and networking with people in your field, and more.") 
    st.write("We may not know what's ahead of us, but always strive to reach your destination. Never quit, alter your route, if need be, but continue this journey for as long as you need to.")
    st.write("Most importantly, ENJOY THE RIDE!")
    


    


            


    
    





    




