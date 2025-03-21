import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("METEOROLOGIE EN ILE DE FRANCE")
st.write("Vous pouvez obtenir des données météorologiques en recherchant une ville des Hauts-de-Seine dans la barre ci-dessous")
st.write("Il y'a aussi à disposition un graphique pour y voir les données sous forme de courbe")
st.write("(Ceci est un exemple, les données ne sont pas les vraies. C'est une phase de test)")

a = st.text_input("Recherchez une ville")
st.write(f"Résultat de la recherche : {a}")

prompt = st.chat_input("Tapez un message ici")

meteo_data = np.random.normal(size=1000)
meteo_data = pd.DataFrame(data=None, columns=["Dist_norm"])

plt.hist(meteo_data.Dist_norm)
fig, ax = plt.subplots()
ax.scatter(["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi"], [12, 14, 11, 15, 10, 12])

st.pyplot(fig)
plt.title("Données météorologiques de le semaine")



