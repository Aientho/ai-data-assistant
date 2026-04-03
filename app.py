import streamlit as st
import pandas as pd
from langchain_experimental.agents import create_pandas_dataframe_agent
from langchain_community.llms import Ollama

# Title
st.title("📊 AI Data Assistant (Ollama Version)")

# File upload
uploaded_file = st.file_uploader("Upload your Excel/CSV file", type=["csv", "xlsx"])

if uploaded_file:
    # Read file
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    # Show data
    st.subheader("Data Preview")
    st.dataframe(df)

    # Load AI model
    llm = Ollama(model="llama3")

    # Create agent
    agent = create_pandas_dataframe_agent(llm, df, verbose=True)

    # Ask question
    query = st.text_input("Ask your data a question:")

    if query:
        with st.spinner("Thinking... 🤔"):
            result = agent.run(query)
            st.success(result)
else:
    st.info("👆 Upload a dataset to begin")