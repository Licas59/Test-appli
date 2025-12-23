import streamlit as st 
from streamlit_gsheets import 
GSheetsConnection 

st.set_page_config(page_title="Family", page_icon="🏠")
st.title("🏠Dashboard de la Famille🏠")

conn = st.connection("gsheets", type = GSheetsConnection)
url = "https://docs.google.com/spreadsheets/d/1-GcU9NzoVJd2KMQmnQPjnH2VxJOR7sIMe49Jkg78ynA/edit?usp=drivesdk"

user = st.sidebar.text_input("Qui est tu ?")
if not user :
    st.warning("Veuillez entrer votre nom dans le menu à gauche. ")
    st.stop()
