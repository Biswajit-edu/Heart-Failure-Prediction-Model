import streamlit as st
import pickle

file = open("lr_classifier.pkl",'rb')
lr_classifier = pickle.load(file)

file = open("sv_classifier.pkl",'rb')
sv_classifier = pickle.load(file)

file = open("kn_classifier.pkl",'rb')
kn_classifier = pickle.load(file)

file = open("dt_classifier.pkl",'rb')
dt_classifier = pickle.load(file)

file = open("rf_classifier.pkl",'rb')
rf_classifier = pickle.load(file)

file = open("gb_classifier.pkl",'rb')
gb_classifier = pickle.load(file)

file = open("nb_classifier.pkl",'rb')
nb_classifier = pickle.load(file)

file = open("Standard_Scaler.pkl", 'rb')
Sscaller = pickle.load(file)

def lr_predictor(to_predict):
    prediction = lr_classifier.predict(to_predict)
    print(prediction)
    return prediction

def sv_predictor(to_predict):
    prediction = sv_classifier.predict(to_predict)
    print(prediction)
    return prediction

def kn_predictor(to_predict):
    prediction = kn_classifier.predict(to_predict)
    print(prediction)
    return prediction

def dt_predictor(to_predict):
    prediction = dt_classifier.predict(to_predict)
    print(prediction)
    return prediction

def rf_predictor(to_predict):
    prediction = rf_classifier.predict(to_predict)
    print(prediction)
    return prediction

def gb_predictor(to_predict):
    prediction = gb_classifier.predict(to_predict)
    print(prediction)
    return prediction

def nb_predictor(to_predict):
    prediction = nb_classifier.predict(to_predict)
    print(prediction)
    return prediction

def main():
    st.markdown("<h1 style='text-align: center; color: red;'>Welcome!</h1>", unsafe_allow_html=True)
    htmp_temp = """ 
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:centre;">ML Heart Failure Predictor App</h2>
    </div> """
    st.markdown(htmp_temp,unsafe_allow_html=True)
    age = st.number_input("Age")
    anm = st.number_input("Do you have anaemia? : Type 1 if Yes and 0 if No")
    c_p = st.number_input("Enter your Creatinine-Phosphokinase Level")
    dbt = st.number_input("Are you diabetic? : Type 1 if Yes and 0 if No")
    ejf = st.number_input("Enter your Ejection Fraction Level")
    hbp = st.number_input("Do you have high blood pressure? : Type 1 if Yes and 0 if No")
    plt = st.number_input("Enter your Platelets Count")
    s_c = st.number_input("Enter your Serum Creatinine level")
    s_s = st.number_input("Enter your Serum sodium level")
    sex = st.number_input("Sex : Type 1 for Male and 0 for Female")
    smk = st.number_input("Do you smoke? : Type 1 if Yes and 0 if No")
    tim = st.number_input("Time")
    
    # Rescalling the values for prediction
    to_predict = [[age,anm,c_p,dbt,ejf,hbp,plt,s_c,s_s,sex,smk,tim]]
    to_predict = Sscaller.transform(to_predict)
    lr_res = ""
    if st.button("LR_Predictor"):
        lr_res = lr_predictor(to_predict)
        if lr_res == 1:
            st.warning("Heart Failure likely to occur")
        if lr_res == 0:
            st.success("Heart Failure unlikely to occur")
            
    sv_res = ""
    if st.button("SV_Predictor"):
        sv_res = sv_predictor(to_predict)
        if sv_res == 1:
            st.warning("Heart Failure likely to occur")
        if sv_res == 0:
            st.success("Heart Failure unlikely to occur")
            
    kn_res = ""
    if st.button("KN_Predictor"):
        kn_res = kn_predictor(to_predict)
        if kn_res == 1:
            st.warning("Heart Failure likely to occur")
        if kn_res == 0:
            st.success("Heart Failure unlikely to occur")
            
    dt_res = ""
    if st.button("DT_Predictor"):
        dt_res = dt_predictor(to_predict)
        if dt_res == 1:
            st.warning("Heart Failure likely to occur")
        if dt_res == 0:
            st.success("Heart Failure unlikely to occur")
            
    rf_res = ""
    if st.button("RF_Predictor"):
        rf_res = rf_predictor(to_predict)
        if rf_res == 1:
            st.warning("Heart Failure likely to occur")
        if rf_res == 0:
            st.success("Heart Failure unlikely to occur")
            
    gb_res = ""
    if st.button("GB_Predictor"):
        gb_res = gb_predictor(to_predict)
        if gb_res == 1:
            st.warning("Heart Failure likely to occur")
        if gb_res == 0:
            st.success("Heart Failure unlikely to occur")

    nb_res = ""
    if st.button("NB_Predictor"):
        nb_res = nb_predictor(to_predict)
        if nb_res == 1:
            st.warning("Heart Failure likely to occur")
        if nb_res == 0:
            st.success("Heart Failure unlikely to occur")
        
if __name__=='__main__':
    main()