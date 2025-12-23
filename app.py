import streamlit as st

# Configuration de la page pour qu'elle ressemble à une App
st.set_page_config(page_title="App Famille", page_icon="🏠")

st.title("🏠 Notre App Familiale")

# --- PARTIE 1 : BIENVENUE ---
prenom = st.text_input("C'est qui ?", placeholder="Ton prénom...")
if prenom:
    st.write(f"### Salut {prenom} ! 👋")

# --- PARTIE 2 : LISTE DE TÂCHES (Simple) ---
st.divider()
st.subheader("📝 Choses à faire")

# On utilise une liste simple pour l'exemple
# (Note: avec cette méthode simple, la liste revient à zéro à chaque mise à jour du code)
taches = ["Acheter du pain", "Sortir les poubelles", "Appeler Mamie"]

for t in taches:
    st.checkbox(t)

# --- PARTIE 3 : INTERACTION ---
st.divider()
if st.button("🎈 Lancer une fête !"):
    st.balloons()
    st.toast("C'est la fête dans l'app !")

# --- BAS DE PAGE ---
st.caption("vive les vacances enft")

