import os
import json
import traceback
import pandas as pd
from dotenv import load_dotenv
from src.mcqgenerator.utils import read_file,get_table_data
import streamlit as st
from langchain_community.callbacks import get_openai_callback
from src.mcqgenerator.MCQGenerator import generate_evaluate_chain
from src.mcqgenerator.logger import logging

#loading json file
with open('/Users/hari31/OpenAI/mcqgenai/Response.json','r') as file:
    RESPONSE_JSON = json.load(file)

    #creating a title for the app
    st.title("MCQs CREATOR APPLCIAION WITH LANGCHAIN")

    #create a form usig st.form
    with st.form("user_inputs"):
        #FileUpload
        uploaded_file=file_uploader("Upload a PDF or TXT file")

        # Input Fields
        mcq_count=st.number_input("No. Of MCQs",min_value=3,max_value=50)

        #Subject
        subject=st.text_input("Insert Subject",max_chars=20)

        #Quiz tone
        tone=st.text_input("Complexity Level Of Questions", max_chars=20, placeholder="Simple")

        #Add.Botton
        button=st.form_submit_button("Create MCQs")

        # Check if the button is clicked and all the fields have inputs
        