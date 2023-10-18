
import streamlit as st
import pandas as pd
import altair as alt
import seaborn as sns
import matplotlib.pyplot as plt

salary = pd.read_csv("Salary_Data.csv")

salary = salary.drop([172,260,2011,3136,5247,6455])

salary['Education Level'].replace("Bachelor's Degree", "Bachelor's", inplace=True)
salary['Education Level'].replace("Master's Degree", "Master's", inplace=True)

salary['Education Level'].replace("phD", "PhD", inplace=True)

salary = salary.drop(salary[salary['Gender'] == 'Other'].index)

salary_V3 = salary[(salary["Job Title"] == 'Data Scientist') | (salary["Job Title"] == 'Software Engineer') | (salary["Job Title"] == 'Marketing Manager') | (salary["Job Title"] == 'Full Stack Engineer')]

DS = salary_V3[salary_V3["Job Title"] == 'Data Scientist']
SE = salary_V3[salary_V3["Job Title"] == 'Software Engineer']
MM = salary_V3[salary_V3["Job Title"] == 'Marketing Manager']
FSE = salary_V3[salary_V3["Job Title"] == 'Full Stack Engineer']

st.title("Salary Comparison")
st.subheader("Salary is based upon job title, gender, education level, and years of experience.")

st.write("Let's visually dive into analyzing our data.")

cat = st.selectbox("Choose a Categorical Variable",("Gender","Education Level","Job Title"))
num = st.selectbox("Choose a Numerical Variable",("Age","Years of Experience","Salary"))

if cat == "Gender":
    color = st.selectbox("Choose a Hue", ("Education Level","Job Title","None"))
elif cat == "Education Level":
    color = st.selectbox("Choose a Hue", ("Gender","Job Title","None"))
elif cat == "Job Title":
    color = st.selectbox("Choose a Hue", ("Gender","Education Level","None"))

fig = plt.figure(figsize=(8, 4))
if color == "None":
    if cat == "Gender" and num == "Age":
        g_a_nh = sns.violinplot(x= 'Gender',y= 'Age', data=salary_V3)
        st.pyplot(fig)
    elif cat == "Gender" and num == "Years of Experience":
        g_y_nh = sns.violinplot(x= 'Gender',y= 'Years of Experience', data=salary_V3)
        st.pyplot(fig)
    elif cat == "Gender" and num == "Salary":
        g_s_nh = sns.violinplot(x= 'Gender',y= 'Salary', data=salary_V3)
        st.pyplot(fig)
    elif cat == "Education Level" and num == "Age":
        e_a_nh = sns.violinplot(x= 'Education Level',y= 'Age', data=salary_V3)
        st.pyplot(fig)
    elif cat == "Education Level" and num == "Years of Experience":
        e_y_nh = sns.violinplot(x= 'Education Level',y= 'Years of Experience', data=salary_V3)
        st.pyplot(fig)
    elif cat == "Education Level" and num == "Salary":
        e_s_nh = sns.violinplot(x= 'Education Level',y= 'Salary', data=salary_V3)
        st.pyplot(fig)
    elif cat == "Job Title" and num == "Age":
        j_a_nh = sns.violinplot(x= 'Job Title',y= 'Age', data=salary_V3)
        st.pyplot(fig)
    elif cat == "Job Title" and num == "Years of Experience":
        j_y_nh = sns.violinplot(x= 'Job Title',y= 'Years of Experience', data=salary_V3)
        st.pyplot(fig)
    elif cat == "Job Title" and num == "Salary":
        j_s_nh = sns.violinplot(x= 'Job Title',y= 'Salary', data=salary_V3)
        st.pyplot(fig)   
elif color == "Gender":
    if cat == "Education Level" and num == "Age":
        e_a_hg = sns.violinplot(x= 'Education Level',y= 'Age', hue = "Gender", data=salary_V3)
        st.pyplot(fig)
    elif cat == "Education Level" and num == "Years of Experience":
        e_y_hg = sns.violinplot(x= 'Education Level',y= 'Years of Experience', hue = "Gender", data=salary_V3)
        st.pyplot(fig)
    elif cat == "Education Level" and num == "Salary":
        e_s_hg = sns.violinplot(x= 'Education Level',y= 'Salary', hue = "Gender", data=salary_V3)
        st.pyplot(fig)
    elif cat == "Job Title" and num == "Age":
        j_a_hg = sns.violinplot(x= 'Job Title',y= 'Age', hue = "Gender", data=salary_V3)
        st.pyplot(fig)
    elif cat == "Job Title" and num == "Years of Experience":
        j_y_hg = sns.violinplot(x= 'Job Title',y= 'Years of Experience', hue = "Gender", data=salary_V3)
        st.pyplot(fig)
    elif cat == "Job Title" and num == "Salary":
        j_s_hg = sns.violinplot(x= 'Job Title',y= 'Salary', hue = "Gender", data=salary_V3)
        st.pyplot(fig)     
elif color == "Education Level":
    if cat == "Gender" and num == "Age":
        g_a_nh = sns.violinplot(x= 'Gender',y= 'Age', hue = "Education Level", data=salary_V3)
        st.pyplot(fig)
    elif cat == "Gender" and num == "Years of Experience":
        g_y_nh = sns.violinplot(x= 'Gender',y= 'Years of Experience', hue = "Education Level", data=salary_V3)
        st.pyplot(fig)
    elif cat == "Gender" and num == "Salary":
        g_s_nh = sns.violinplot(x= 'Gender',y= 'Salary', hue = "Education Level", data=salary_V3)
        st.pyplot(fig)
    elif cat == "Job Title" and num == "Age":
        j_a_hg = sns.violinplot(x= 'Job Title',y= 'Age', hue = "Education Level", data=salary_V3)
        st.pyplot(fig)
    elif cat == "Job Title" and num == "Years of Experience":
        j_y_hg = sns.violinplot(x= 'Job Title',y= 'Years of Experience', hue = "Education Level", data=salary_V3)
        st.pyplot(fig)
    elif cat == "Job Title" and num == "Salary":
        j_s_hg = sns.violinplot(x= 'Job Title',y= 'Salary', hue = "Education Level", data=salary_V3)
        st.pyplot(fig)    
elif color == "Job Title":
    if cat == "Gender" and num == "Age":
        g_a_nh = sns.violinplot(x= 'Gender',y= 'Age', hue = "Job Title", data=salary_V3)
        st.pyplot(fig)
    elif cat == "Gender" and num == "Years of Experience":
        g_y_nh = sns.violinplot(x= 'Gender',y= 'Years of Experience', hue = "Job Title", data=salary_V3)
        st.pyplot(fig)
    elif cat == "Gender" and num == "Salary":
        g_s_nh = sns.violinplot(x= 'Gender',y= 'Salary', hue = "Job Title", data=salary_V3)
        st.pyplot(fig)
    elif cat == "Education Level" and num == "Age":
        e_a_hg = sns.violinplot(x= 'Education Level',y= 'Age', hue = "Job Title", data=salary_V3)
        st.pyplot(fig)
    elif cat == "Education Level" and num == "Years of Experience":
        e_y_hg = sns.violinplot(x= 'Education Level',y= 'Years of Experience', hue = "Job Title", data=salary_V3)
        st.pyplot(fig)
    elif cat == "Education Level" and num == "Salary":
        e_s_hg = sns.violinplot(x= 'Education Level',y= 'Salary', hue = "Job Title", data=salary_V3)
        st.pyplot(fig)

st.write("Now let's look at the data as a whole by Job Title.")

option = st.selectbox("Choose a Job Title",("Data Scientist","Software Engineer","Marketing Manager","Full Stack Engineer"))

st.write('You selected:', option)

if option == "Data Scientist":
    DS_plot = (alt.Chart(DS, title = alt.Title("Data Scientist",anchor='middle',orient='top')).mark_circle().encode(
    alt.X('Salary:Q').scale(zero=False),
    y='Gender:O',
    color='Gender:N',
    row='Education Level:N',
    tooltip=['Age', 'Years of Experience', 'Salary']
    ).interactive())
    st.altair_chart(DS_plot, theme=None)
elif option == "Software Engineer":
    SE_plot = (alt.Chart(SE, title = alt.Title("Software Engineer",anchor='middle',orient='top')).mark_circle().encode(
    alt.X('Salary:Q').scale(zero=False),
    y='Gender:O',
    color='Gender:N',
    row='Education Level:N',
    tooltip=['Age', 'Years of Experience', 'Salary']
    ).interactive())
    st.altair_chart(SE_plot, theme=None)
elif option == "Marketing Manager":
    MM_plot = (alt.Chart(MM, title = alt.Title("Marketing Manager",anchor='middle',orient='top')).mark_circle().encode(
    alt.X('Salary:Q').scale(zero=False),
    y='Gender:O',
    color='Gender:N',
    row='Education Level:N',
    tooltip=['Age', 'Years of Experience', 'Salary']
    ).interactive())
    st.altair_chart(MM_plot, theme=None)
elif option == "Full Stack Engineer":
    FSE_plot = (alt.Chart(FSE, title = alt.Title("Full Stack Engineer",anchor='middle',orient='top')).mark_circle().encode(
    alt.X('Salary:Q').scale(zero=False),
    y='Gender:O',
    color='Gender:N',
    row='Education Level:N',
    tooltip=['Age', 'Years of Experience', 'Salary']
    ).interactive())
    st.altair_chart(FSE_plot, theme=None)

st.write("Want to know more about a specific person? Hover over a point on the plot to see more deatils.")
