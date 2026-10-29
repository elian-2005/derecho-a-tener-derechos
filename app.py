

import streamlit as st

st.title("Derecho a tener derechos")

opcion = st.selectbox(

    "Escoge un derecho",

    ["Educación", "Salud", "Vivienda"]

)

if opcion == "Educación":

    st.write("Todas las personas tienen derecho a recibir educación.")

elif opcion == "Salud":

    st.write("Todas las personas tienen derecho a recibir atención médica.")

elif opcion == "Vivienda":

    st.write("Todas las personas tienen derecho a una vivienda digna.")
