import streamlit as st
 
def convert_units(value,unit_from,unit_to):
    
    conversions = {
       "meters_kilometers": 0.001,
       "kilometers_meters": 1000,
       "grams_kilograms": 0.001,
       "kilograms_grams": 1000,
    
    }
   
    key=f"{unit_from}_{unit_to}"
    
    if key in conversions:
        conversion=conversions[key]
        return value * conversion
    else:
        return "conversion not supported"
    
st.title("Unit Converter")

value=st.number_input("Enter the value:")

unit_from = st.selectbox("convert from:",["meters","kilometers","gram","kilograms"])

unit_to=st.selectbox ("convert to:",["meters","kilometers","gram","kilograms"])

if st.button("Convert"):
    result=convert_units(value,unit_from,unit_to)
    st.success(f"The converted value is {result}")
    
    
    
