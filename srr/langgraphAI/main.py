import streamlit as st

from srr.langgraphAI.UI.uistrem.loadui import LoadStreamlitUI
from srr.langgraphAI.LLMS.grokllm import GroqLLM
from srr.langgraphAI.graph.graph_builder import GraphBuilder
from srr.langgraphAI.UI.uistrem.displyui import DisplayResultStremalit

def load_langgraph_agenticai_app():
    """
    Load and runs the LangGraph AgenticAI Streamlit application with stremalit UI.
    THis function initializes the UI ,handles user input, configures the LLM model,
    sets up th egraph based on the selected use case, and displays the output while
    implelmenting exception handling for robustness.
    
    """
    
    # load Ui
    
    ui = LoadStreamlitUI()
    user_input = ui.load_stremlit_ui()
    
    if  not user_input:
        st.error("Error : Failed to load UI components.")
        return 
    
    user_messages = st.chat_input('enter your messages')
    
    
    if user_messages:
        try:
            obj_llm_config = GroqLLM(user_controls_input=user_input)
            model = obj_llm_config.get_llm_model()
            
            if not model:
                st.error("Error LLm model could not be initalized")
                return
            
            # Initialize and set up the graph based on use case
            usecase = user_input.get('selected_usecase')
            
            if not usecase:
                st.error("Error: Usecase not selected.")
                return
            
            # Graph Builder
            
            graph_builder = GraphBuilder(model)
            try:
                
                graph= graph_builder.setup_graph(usecase)
                DisplayResultStremalit(usecase,graph,user_messages).display_result_on_ui()
            
            except Exception as e:
                st.error(f"Error setting up graph: {e}")
                return
            
            
        
        except Exception as e:
            st.error(f'Error : Graph set up failed -{e}')
            return