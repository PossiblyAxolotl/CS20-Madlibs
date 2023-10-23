import streamlit as st
import os, random

# page setup
st.set_page_config(
    page_title="Madlibs Generator",
    page_icon="🎄",
)

st.title("My Christmas Break")

st.write("From https://www.writing.com/main/madlibs/item_id/1351203-My-Christmas-Holiday")

# list each prompt for a madlib and what list contains its default values
default_file_names = os.listdir("default values")
defaults = {}

defaults["numbers"] = range(-1000,1000) # don't wanna make a text file of numbers

for filename in default_file_names:
    with open(f"default values/{filename}", "r") as file:
        values = []
        for line in file:
            values.append(line[:-1])
        
        defaults[filename.replace(".txt","")] = values

# list prompts and create the text fields needed
prompts = {
    "Noun":defaults["nouns"],
    "Number":defaults["numbers"],
    "Second noun":defaults["nouns"],
    "Height":defaults["heights"],
    "Second number":defaults["numbers"],
    "Adjective":defaults["adjectives"],
    "Plural noun":defaults["pnouns"],
    "Third number":defaults["numbers"],
    "Secon plural noun":defaults["pnouns"],
    "Second adjective":defaults["adjectives"]
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
    
    # write generated madlib
    st.write(f'''This Christmas holiday, I plan to cook a giant {answers[0]} for our Christmas dinner. \
We will invite {answers[1]} people over to enjoy the dinner. My two year old cousin will be given a {answers[2]} for her present. \
There will be a {answers[3]} Christmas tree this year! I'll put {answers[4]} presents under the tree. \
Me and my family hope this will be a {answers[5]} Christmas this year! Usually, everyone is tired after all of that excitement. \
Many times, there's {answers[6]} lying all over the floor because people were partying so hard! \
Plus, the kids got some candy, so they're a little energetic the next day. \
They threw {answers[7]} {answers[8]} all over the living room last year because they got so energetic they couldn't control themselves! \
Can you believe it???\n\nAfter the party, we all say, "Have a {answers[9]} Christmas next year, too!"'''
)

# button to generate madlibs
if st.button("Generate"):
    generate()
