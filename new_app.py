import streamlit as st
import pickle
import pandas as pd
from functions import convert_continent,calc_wage,label_company_size
st.title("Visa Prediction")
preprocessor=pickle.load(open("preprocessor.pkl","rb"))
data=pickle.load(open("train.pkl","rb"))
model=pickle.load(open("model.pkl","rb"))
preprocessor.fit_transform(data)
continent=st.selectbox(label="Enter the Continent you live in",options=["Asia","Europe","North America","South America","Africa","Oceania"])
continent=convert_continent(row={"continent":continent})
education_of_employee=str(st.selectbox(label="Enter your highest qualification",options=["High School","Bachelor's","Master's","Doctorate"]))
has_job_experience=st.radio(label="Do you have a prior work experince",options=["Yes","No"],horizontal=True)
has_job_experience="Y" if has_job_experience=="Yes" else "N"
region_of_employment=st.selectbox("What region You are employed in",options=["West","Northeast","South","Midwest","Island"])
full_time_position=st.radio(label="Do you have a full time job",options=["Yes","No"],horizontal=True)
full_time_position="Y" if full_time_position=="Yes" else "N"
unit_of_wage=st.selectbox("Please select the unit of wage",options=["Hour","Week","Month","Year"])
hours=0
if unit_of_wage=="Hour":
    hours=st.number_input("Enter the hours per week",max_value=80,min_value=10)
prevailing_wage=st.number_input("Enter your wage",min_value=10)
data={
    "unit_of_wage":unit_of_wage,
    "prevailing_wage":prevailing_wage
}
yearly_wage=calc_wage(data,hours=hours)
no_of_employees=st.number_input("Enter the number of employes that are likely to be in your company",min_value=5)
company_size=label_company_size({"no_of_employees":no_of_employees})
company_age=st.number_input("How old is Your Company",min_value=0)
input_df = pd.DataFrame(
    data=[[continent, education_of_employee, has_job_experience, region_of_employment,
           full_time_position,  yearly_wage,company_size, company_age]],
    columns=["continents_modified", "education_of_employee", "has_job_experience", "region_of_employment","full_time_position" ,"yearly_wage" ,"company_size", "company_age"]
)
input_df=preprocessor.transform(input_df)
if st.button("predict"):
    if int(model.predict(input_df))==1:
        st.write("### Congrats ! Your visa is approved 🎉🎉")
    else:
        st.write("### Unfortunately, your visa application was not approved 💔")
