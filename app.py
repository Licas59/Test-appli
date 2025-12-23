import streamlit as st 
from streamlit_gsheets import GSheetsConnection 

st.set_page_config(page_title="Family", page_icon="🏠")
st.title("La Family🏠")

conn = st.connection("gsheets", type = GSheetsConnection)
url = "https://docs.google.com/spreadsheets/d/1-GcU9NzoVJd2KMQmnQPjnH2VxJOR7sIMe49Jkg78ynA/edit?usp=drivesdk"

user = st.sidebar.text_input("Qui est tu ?")
if not user :
    st.warning("Veuillez entrer votre nom dans le menu à gauche. ")
    st.stop()
data = conn.read(spreadsheet=url)
st.dataframe(data)

st.divider()
st.subheader("Message a faire passer")
with st.form("form_message"):
    auteur = st.text_input("Ton prénom")
    texte = st.text_area("message a faire passer")
    bouton_valider = st.form_submit_button("Envoyer le message")
if bouton_valider :
    if auteur and texte :
        nouvelle_donnee = [auteur, texte]
        conn.create(spreadsheet=url,data = [nouvelle_donnee])
        st.success("C'est envoyé ! Actualise pour l'afficher")
        st.balloons()
    else :
        st.error("il faut remplir les 2 cases")
