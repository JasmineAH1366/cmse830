
import streamlit as st
import pandas as pd
import altair as alt

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
