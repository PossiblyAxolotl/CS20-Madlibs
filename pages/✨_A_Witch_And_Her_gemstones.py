import streamlit as st
import os, random

# page setup
st.set_page_config(
    page_title="Madlibs Generator",
    page_icon="✨",
)

st.title("A Witch And Her Gemstones")

st.write("From https://www.writing.com/main/madlibs/item_id/2282119-A-Witch-and-Her-Gemstones")

# list each prompt for a madlib and what list contains its default values
default_file_names = os.listdir("default values")
defaults = {}

for filename in default_file_names:
    with open(f"default values/{filename}", "r") as file:
        values = []
        for line in file:
            values.append(line[:-1])
        
        defaults[filename.replace(".txt","")] = values

# list prompts and create the text fields needed
prompts = {
    "Girl name":defaults["names"],
    "Verb":defaults["verbs"],
    "Animal":defaults["animals"],
    "Gemstone":defaults["gems"],
    "Adjective":defaults["adjectives"],
    "Different gemstone":defaults["gems"],
    "Flower":defaults["flowers"],
    "Third gemstone":defaults["gems"],
    "Different flower":defaults["flowers"]
}

text_fields = {}
answers = []

for prompt in prompts:
    field = st.text_input(prompt)
    text_fields[prompt] = field

# generate the madlibs, fill in anything left blank
def generate():
    answers = []
    for key in text_fields.keys():
        field = text_fields[key]
        if field.replace(" ", "") == "":
            answers.append(random.choice(prompts[key]))
        else:
            answers.append(field)
    
    st.write(f"{answers[0]} was a witch who lived in the Black Forest. \
One day she {answers[1]} over Muritz Castle and spied a handsome man who was grooming his {answers[2]}. \
Wanting to attract him, she left a {answers[3]} on a rock nearby. He spied the precious stone and became {answers[4]} Looking around, he tried to see who left it. \
A few feet away, he found {answers[5]}. A trail of items led to a waterfall. Catching the scent of a {answers[6]} he turned around and spied her. \
She offered him a {answers[7]}. He smiled and gave her a {answers[8]}."
    )

# button to generate madlibs
if st.button("Generate"):
    generate()
