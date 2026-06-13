import streamlit as st
st.title("Welcome to BMI calculator ")
st.subheader("Enter your details to calculate BMI")
name=st.text_input("Enter your name")
weight=(st.number_input("Enter your weight in kg: "))
height=(st.number_input("Enter your height in centimeter: "))


if st.button("Calculate"):
    if height<=0:
        st.error("Height cannot be zero")
    elif weight<=0:
        st.error("Weight cannot be zero")
    elif name=="":
        st.warning("Please enter a valid name")
    else:
        bmi=weight/(height/100)**2
        st.write("Your BMI is ", round(bmi, 2))
        if bmi<18.5:
            st.warning(f"{name}, you are Underweight")
        elif bmi < 25:
            st.success(f"{name}, you are in Normal range")
        elif bmi <30:
            st.warning(f"{name}, you are Overweight ")
        else:
            st.error(f"{name}, you are Obese")