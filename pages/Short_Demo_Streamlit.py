import streamlit as st
import pandas as pd
import requests
import numpy as np
import altair as alt

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

st.header("Inputs")

st.write("Text input")

codetextinput = '''
title = st.text_input('Movie title', 'Life of Brian')
st.write('The current movie title is', title)'''
st.code(codetextinput, language='python')

title = st.text_input('Movie title', 'Life of Brian')
st.write('The current movie title is', title)

st.write("Number input")

codenumberinput = '''
number = st.number_input('Insert a number')
st.write('The current number is ', number)'''
st.code(codenumberinput, language='python')

number = st.number_input('Insert a number')
st.write('The current number is ', number)

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

st.header("Charts et graphiques")

st.write("Line chart")

codelinechart = '''
import numpy as np

line_chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["a", "b", "c"]
)

st.line_chart(line_chart_data)'''
st.code(codelinechart, language='python')

line_chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["a", "b", "c"]
)

st.line_chart(line_chart_data)

st.write("Scatter chart (librairie Altair)")

codescatterchart = '''
import altair as alt

alt_chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

c = (
    alt.Chart(alt_chart_data)
    .mark_circle()
    .encode(x="a", y="b", size="c", color="c", tooltip=["a", "b", "c"])
    )

st.altair_chart(c, use_container_width=True)
'''
st.code(codescatterchart, language='python')

alt_chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

c = (
    alt.Chart(alt_chart_data)
    .mark_circle()
    .encode(x="a", y="b", size="c", color="c", tooltip=["a", "b", "c"])
    )

st.altair_chart(c, use_container_width=True)

st.write("Map")

codemap = '''
df = pd.DataFrame(
                    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
                    columns=['lat', 'lon']
                )
st.map(df)'''
st.code(codemap, language='python')

df = pd.DataFrame(
                    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
                    columns=['lat', 'lon']
                )
st.map(df)

st.header("Pour aller plus loin")

st.write("Vous pouvez consulter ce projet d'application streamlit qui présente toutes les possibilités de streamlit de manière interactive :")
st.write("https://cheat-sheets.streamlit.app/")
st.write("")
st.write("Ainsi que la documentation officielle de streamlit :")
st.write("https://docs.streamlit.io/")