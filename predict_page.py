import numpy as np
import pandas as pd
import pickle
import streamlit as st

def load_model():
    with open('wine_quality_prediction_saved_model.pkl','rb') as file:
        data = pickle.load(file)
        return data
    
data = load_model()
model = data['model']   # Random forest classsifier
    
    #[fixed acidity, volatile acidity,	citric acid,	 residual sugar	
    # chlorides	,free sulfur dioxide, total sulfur dioxide,	density, pH, sulphates,	alcohol]

def show_predicted_page():
    st.title("Wine Quality Prediction")

    st.write("""### We need some information about your wine: """)

    fixed_acidity, volatile_acidity, citric_acid = st.columns(3)
    residual_sugar, chlorides, free_sulfur_dioxid = st.columns(3)
    total_sulfur_dioxide, density, pH = st.columns(3)
    sulphates, alcohol = st.columns(2)

    x1 = fixed_acidity.text_input("fixed_acidity :")
    x2 = volatile_acidity.text_input("volatile_acidity:")
    x3 = citric_acid.text_input("citric_acid:")
    x4 = residual_sugar.text_input("residual_sugar:")
    x5 = chlorides.text_input("chlorides:")
    x6 = free_sulfur_dioxid.text_input("free_sulfur_dioxid:")
    x7 = total_sulfur_dioxide.text_input("total_sulfur_dioxide:")
    x8 = density.text_input("density:")
    x9 = pH.text_input("pH_value:")
    x10 = sulphates.text_input("sulphates:")
    x11 =alcohol.text_input("alcohol:")

    ok = st.button("Predict")

    if ok:
        X = np.asarray([[x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11]])
        x_reshaped = X.reshape(1,-1)

        prediction = model.predict(x_reshaped)
        
        if (prediction[0] == 1):
            st.success("Good Quality Wine")
        else:
            st.warning("Bad Quality Wine")