import streamlit as st

st.title("Evaluación de un lote")

pH = st.number_input(
    "pH",
    value=6.5
)

temperatura = st.number_input(
    "Temperatura (°C)",
    value=23.0
)

if st.button("Evaluar"):

    # Completa aquí la lógica
if (6.0 <= pH <= 8.0 and (18.0 <= temperatura <= 25):
    resultado= "Lote aceptado"
    else
    resultado= "Lote rechazado"
    st.write(f"Resultado: {resultado}")
  
