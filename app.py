st.sidebar.title("Actividad 7")
st.sidebar.write("Hanael Diaz, 3L, Facultad de Ciencias Quimicas")


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

    if (6.0 <= pH <= 8.0) and (18.0 <= temperatura <= 25.0):

        resultado = "Aceptado"
    else:

        resultado = "Rechazado"
    

    st.write(f"Resultado: {resultado}")
