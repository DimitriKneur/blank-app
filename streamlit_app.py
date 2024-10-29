import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

st.header("Créer une page")

st.write('A la racine du repo github, créer un dossier "pages" :')

st.image("assets/capture_ecran_nouvelle_page.png")

st.write("Chaque fichier du format nom_de_fichier.py situé dans ce dossier 'pages' deviendra une page interactive dans streamlit.")
st.write("Ainsi, si on veut créer une page qui sera nommée 'Short_Demo_Streamlit.py', dans le dossier 'pages', on va créer le fichier 'Short_Demo_Streamlit.py' :")

st.image("assets/capture_ecran_page_demo_streamlit.png")

st.write("Dans ce fichier, on écrira le code selon ce que l'on veut afficher dans la page correspondante.")
st.write("La particularité est que les pages dans une application streamlit doivent être écrites en utilisat la librairie streamlit.")
st.write("Du coup, dans notre nouvelle page, la première ligne à écrire sera l'importation de la librairie streamlit : ")

codestreamlit = '''
import streamlit as st'''
st.code(codestreamlit, language='python')

st.write("il va aussi falloir installer la librairie streamlit : ")

codestreamlit = '''
pip install streamlit'''
st.code(codestreamlit, language='python')