
import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px

st.title('Dashboard')

df = sns.load_dataset('titanic')

# Explicitly convert all object columns to strings to avoid np.unicode_ issues
df = df.applymap(lambda x: str(x) if isinstance(x, (str, bytes)) else x)

# print dataframe
st.dataframe(df)

# gender filter
gender = st.sidebar.multiselect('Gender', options = df['sex'].unique(), default = df['sex'].unique())

# class filter
pclass = st.sidebar.multiselect('Class', options = df['pclass'].unique(), default = df['pclass'].unique())

# age filter
min_age, max_age = st.sidebar.slider('Age', min_value = int(df['age'].min()), max_value = int(df['age'].min()), value = (int(df['age'].min()), int(df['age'].max())))

# filter data conditions
filtered_data = df[
    (df['sex'].isin(gender)) &
    (df['pclass'].isin(pclass)) &
    (df['age'] >= min_age) &
    (df['age'] <= max_age)   
]

# print dataframes
st.dataframe(filtered_data)

# to create sub-heading
st.subheader('Age Distribution')

fig = px.histogram(filtered_data, x='age', nbins=20, title='Age distribution')
st.plotly_chart(fig)

# pie chart for survival rate by gender
fig = px.pie(filtered_data, names='sex', values='survived', title='Survival rate by gender', color_discrete_sequence=['pink', 'blue'], hole= 0.4)
st.plotly_chart(fig)

# passenger count by class
fig = px.bar(filtered_data, x='pclass', y='survived', title='Passenger count by class', color='class',text_auto=True )
st.plotly_chart(fig)

# survival rate by age
fig = px.line(filtered_data.groupby('age')['survived'].mean().reset_index(), x='age', y='survived', title='Survival rate by age', markers=True)
st.plotly_chart(fig)

