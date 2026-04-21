import streamlit as st
import pandas as pd
import numpy as np 
import pickle
from sklearn.ensemble import RandomForestClassifier

st.write("""# Penguin Prediction App
         This app uses a machine learning model to predict the species of penguin based on the characteristics of the penguin.
""")


st.sidebar.header('User Input Parameters')
st.sidebar.markdown("""This is a markdown text in the sidebar.""")

# Collects user input features into dataframe
uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type=["csv"])

if uploaded_file is not None:
    input_df = pd.read_csv(uploaded_file)
else:
    def user_input_features():
        island = st.sidebar.selectbox('Island',('Biscoe', 'Dream', 'Torgersen'))
        sex = st.sidebar.selectbox('Sex',('male', 'female'))
        bill_length_mm = st.sidebar.slider('Bill Length (mm)', float(32.1), float(59.6), float(43.9))
        bill_depth_mm = st.sidebar.slider('Bill Depth (mm)', float(13.1), float(21.5), float(17.2)) 
        flipper_length_mm = st.sidebar.slider('Flipper Length (mm)', float(172.0), float(231.0), float(201.0))
        body_mass_g = st.sidebar.slider('Body Mass (g)', float(2700.0), float(6300.0), float(4207.0))
        data = {'island': island,   
                'bill_length_mm': bill_length_mm,
                'bill_depth_mm': bill_depth_mm,
                'flipper_length_mm': flipper_length_mm,
                'body_mass_g': body_mass_g,
                'sex': sex}
        features = pd.DataFrame(data, index=[0])        
        return features
    input_df = user_input_features()

# Combines user input features with penguins dataset
# This will be useful for the encoding phase
penguins_raw = pd.read_csv('penguins_cleaned.csv')
penguins = penguins_raw.drop(columns=['species'])
df = pd.concat([input_df, penguins], axis=0)

# Encoding of ordinal features
encode = ['sex', 'island']
for col in encode:
    dummy = pd.get_dummies(df[col], prefix=col)
    df = pd.concat([df, dummy], axis=1)
    del df[col]
df = df[:1] # Selects only the first row (the user input data)


# Displays the user input features
st.subheader('User Input features')

if uploaded_file is not None:
    st.write(df)
else:    
    st.write('Awaiting CSV file to be uploaded. Currently using example input parameters (shown below).')
    st.write(df)


# Reads in saved classification model
load_clf = pickle.load(open('penguins_clf.pkl', 'rb'))


# Apply model to make predictions   
prediction = load_clf.predict(df)
prediction_proba = load_clf.predict_proba(df)


st.subheader('Prediction')
penguin_species = np.array(['Adelie', 'Chinstrap', 'Gentoo'])
st.write(penguin_species[prediction])

st.subheader('Prediction Probability')
st.write(prediction_proba)
