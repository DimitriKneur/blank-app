import streamlit as st
import pandas as pd
import requests

st.header("Afficher du texte")

code0 = '''
st.write("Voici un texte standard")'''
st.code(code0, language='python')

st.write("Voici un texte standard")

code_0 = '''
st.text('Voici un texte un peu moche')'''
st.code(code_0, language='python')

st.text('Voici un texte un peu moche')

codecode = """
code = '''
def hello():
    print("Hello, Streamlit!")'''
st.code(code, language='python')"""
st.code(codecode, language='python')

code = '''
def hello():
    print("Hello, Streamlit!")'''
st.code(code, language='python')

st.header("Afficher une image")

code1 = '''
st.image("path/to/image_file")'''
st.code(code1, language='python')

st.write("Exemple : si on crée un dossier 'assets' à la racine du projet :")

st.image("assets/capture_ecran_assets.png")

st.write("Et qu'on y met une image istockphoto.jpg :")

st.image("assets/capture_ecran_example.png")

st.write("On peut ensuite afficher cette image avec le code suivant :")

code2 = '''
st.image("assets/istockphoto.jpg")'''
st.code(code2, language='python')

st.image("assets/istockphoto.jpg")

st.header("Afficher un dataframe")


codedataframe = '''
import streamlit as st
import pandas as pd

data = {
    "name": ["John", "Jane", "Bob"],
    "age": [25, 30, 35]
}

df = pd.DataFrame(data)

st.dataframe(df)'''
st.code(codedataframe, language='python')

data = {
    "name": ["John", "Jane", "Bob"],
    "age": [25, 30, 35]
}

df = pd.DataFrame(data)

st.dataframe(df)

st.header("Appel d'une API")

codeAPI = '''
api_url = f"https://swapi.dev/api/people/1/"
response = requests.get(api_url)
data = response.json()
st.json(data)'''
st.code(codeAPI, language='python')

api_url = f"https://swapi.dev/api/people/1/"
response = requests.get(api_url)
data = response.json()
st.json(data)