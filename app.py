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
    # Nivel 1 (4 espacios): dentro del botón
    if (6.0 <= pH <= 8.0) and (18.0 <= temperatura <= 25.0):
        # Nivel 2 (8 espacios): dentro del primer if
        resultado = "Aceptado"
    else:
        # Nivel 2 (8 espacios): dentro del else
        resultado = "Rechazado"
    
    # Nivel 1 (4 espacios): al nivel del botón
    st.write(f"Resultado: {resultado}")
