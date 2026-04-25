import streamlit as st
import pandas as pd
import shap
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing
from sklearn.ensemble import RandomForestRegressor

# --------------------- 终极方案：使用官方推荐的加州房价数据集（无任何错误） ---------------------
st.write("""
         # California House Price Prediction App
         
         This app predicts the **California House Prices** using a Random Forest Regressor.
         """)
st.write('---')

# 加载纯数值、无bug、官方推荐的数据集
housing = fetch_california_housing()
X = pd.DataFrame(housing.data, columns=housing.feature_names)
Y = pd.DataFrame(housing.target, columns=['MEDV'])

st.sidebar.header('Specify Input Parameters')

def user_input_features():
    # 加州房价8个特征（纯数值，无字符串，无计算错误）
    MedInc = st.sidebar.slider('MedInc (Median Income)', float(X.MedInc.min()), float(X.MedInc.max()), float(X.MedInc.mean()))
    HouseAge = st.sidebar.slider('HouseAge (House Age)', float(X.HouseAge.min()), float(X.HouseAge.max()), float(X.HouseAge.mean()))
    AveRooms = st.sidebar.slider('AveRooms (Avg Rooms)', float(X.AveRooms.min()), float(X.AveRooms.max()), float(X.AveRooms.mean()))
    AveBedrms = st.sidebar.slider('AveBedrms (Avg Bedrooms)', float(X.AveBedrms.min()), float(X.AveBedrms.max()), float(X.AveBedrms.mean()))
    Population = st.sidebar.slider('Population', float(X.Population.min()), float(X.Population.max()), float(X.Population.mean()))
    AveOccup = st.sidebar.slider('AveOccup (Avg Occupants)', float(X.AveOccup.min()), float(X.AveOccup.max()), float(X.AveOccup.mean()))
    Latitude = st.sidebar.slider('Latitude', float(X.Latitude.min()), float(X.Latitude.max()), float(X.Latitude.mean()))
    Longitude = st.sidebar.slider('Longitude', float(X.Longitude.min()), float(X.Longitude.max()), float(X.Longitude.mean()))

    data = {
        'MedInc': MedInc,
        'HouseAge': HouseAge,
        'AveRooms': AveRooms,
        'AveBedrms': AveBedrms,
        'Population': Population,
        'AveOccup': AveOccup,
        'Latitude': Latitude,
        'Longitude': Longitude
    }
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.header('Specified Input parameters')
st.write(df)
st.write('---')

# 训练模型
model = RandomForestRegressor()
model.fit(X, Y)

# 预测
prediction = model.predict(df)

st.header('Prediction of House Price (MEDV)')
st.write(prediction)
st.write('---')

# SHAP特征解释
explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X)

st.header('Feature Importance')
plt.figure()
shap.summary_plot(shap_values, X)
st.pyplot(plt, bbox_inches='tight')
st.write('---')

plt.figure()
plt.title('Feature Importance based on SHAP values')
shap.summary_plot(shap_values, X, plot_type="bar")
st.pyplot(plt, bbox_inches='tight')