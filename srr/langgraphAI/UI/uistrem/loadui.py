import streamlit as st
import os

from srr.langgraphAI.UI.uiconfigfile import Config


class LoadStreamlitUI:
    def __init__(self):
        self.config= Config()
        self.user_controls = {}
        
    def load_stremlit_ui(self):
        st.set_page_config(page_title = "🤖" +  self.config.get_page_title(), layout="wide")
        st.header("🤖" + self.config.get_page_title())
        
        
        with st.sidebar:
            # get options from config
            llm_options = self.config.get_llm_option()
            usecase_options = self.config.get_usecase_option()
            
            
            # LLM selection
            self.user_controls['selected_llm'] = st.selectbox("Select LLM", llm_options)
            
            if self.user_controls['selected_llm'] == "Groq":
                #model seledtinon
                model_options = self.config.get_groq_model_options()
                self.user_controls['selected_graq_model'] = st.selectbox("select Model", model_options)
                self.user_controls['GROQ_API_KEY']= st.session_state['GROQ_API_KEY'] = st.text_input("API key", type ="password")
                
                # validate api key
                if not self.user_controls['GROQ_API_KEY']:
                    st.warning("Please enter your Groq API key to proceed. Don't have? refer : https://console.groq.com/keys")
                    
                    
                    
            # usecase selection
            self.user_controls['selected_usecase'] = st.selectbox("Select Usecase", usecase_options)
            
        return self.user_controls
        


