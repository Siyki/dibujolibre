import streamlit as st
from streamlit_drawable_canvas import st_canvas

st.set_page_config(
    page_title="Tablerito de Dibujito",
    page_icon="🎨",
    layout="centered"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Fredoka&display=swap');

html, body, .stApp {
    background: linear-gradient(to right, #fbd3e9, #bb377d);
    color: #2e2e2e;
    font-family: 'Fredoka', sans-serif;
    text-align: center;
}

h1, h2, h3, h4, h5, h6, .stTitle, .stHeader {
    color: #ffffff;
    text-align: center;
}

.stSidebar {
    background-color: #ffffff33 !important;
    color: #000000;
}

.stButton>button {
    background-color: #ff6ec7;
    color: white;
    border: none;
    border-radius: 10px;
    font-weight: bold;
    padding: 10px 20px;
}

.block-container {
    padding-left: 5%;
    padding-right: 5%;
}
</style>
""", unsafe_allow_html=True)

st.title("🎨 Tablerito de Dibujito 🖌️")

with st.sidebar:
    st.subheader("🛠️ Propiedades del Tablero")
    drawing_mode = st.selectbox(
        "✏️ Herramienta de Dibujo:",
        ("freedraw", "line", "rect", "circle", "transform", "polygon", "point"),
    )

    stroke_width = st.slider('🪄 Ancho de línea', 1, 30, 15)
    stroke_color = st.color_picker("🎨 Color del trazo", "#FFFFFF", key="a")
    bg_color = st.color_picker("🌈 Color de fondo", "#000000", key="b")

canvas_result = st_canvas(
    fill_color="rgba(255, 165, 0, 0.3)",
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_color=bg_color,
    height=700,
    width=500,
    drawing_mode=drawing_mode,
    key="canvas",
)
