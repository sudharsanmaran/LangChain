import json
import streamlit as st
from calendar_utils.events import insert_event
from llm_utils import  handle_prompts

st.title('User Prompt')
user_prompt = st.text_input('user prompt')

if user_prompt:
    event_dict = handle_prompts.handle_create_event_prompt(user_prompt)

    st.title('Parssed prompt data')
    with st.form(key='my_form'):
        for key, value in event_dict.items():
            if isinstance(value, dict):
                for sub_key, sub_value in value.items():
                    st.text_input(f'{key} - {sub_key}', value=sub_value)
            else:
                st.text_input(key, value=value)
        
        submit_button = st.form_submit_button(label='Submit')

    if submit_button:
        res = insert_event(json.dumps(event_dict))
        st.title('Response')
        st.text(res)


