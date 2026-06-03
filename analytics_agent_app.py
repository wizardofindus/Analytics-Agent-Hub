import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px
import google.generativeai as genai

from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

# ====================================================
# CONFIG
# ====================================================

GEMINI_API_KEY = "AIzaSyCTIsYh2ciuusbThZ5YyMNTy1OF55y9_s0"

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

st.set_page_config(
    page_title="Analytics Agent Hub",
    layout="wide"
)

# ====================================================
# LOAD DATA
# ====================================================

@st.cache_data
def load_data():

    df = pd.read_csv("ai_sql_sales_data.csv")

    return df

df = load_data()

# ====================================================
# SQLITE DATABASE
# ====================================================

@st.cache_resource
def create_database():

    conn = sqlite3.connect(
        "analytics.db",
        check_same_thread=False
    )

    df.to_sql(
        "sales",
        conn,
        if_exists="replace",
        index=False
    )

    return conn

conn = create_database()

# ====================================================
# VECTOR DATABASE
# ====================================================

@st.cache_resource
def load_vectorstore():

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectorstore = FAISS.load_local(
        "advanced_rag_faiss_index",
        embeddings,
        allow_dangerous_deserialization=True
    )

    return vectorstore

try:
    vectorstore = load_vectorstore()
except:
    vectorstore = None

# ====================================================
# MEMORY
# ====================================================

if "history" not in st.session_state:
    st.session_state.history = []

# ====================================================
# SQL ASSISTANT
# ====================================================

import re

def generate_sql(question):

    prompt = f"""
    You are a SQLite expert.

    Return ONLY executable SQL.

    No explanation.
    No markdown.
    No code fences.

    Table: sales

    Question:
    {question}
    """

    response = model.generate_content(prompt)

    text = response.text.strip()

    match = re.search(
        r"(SELECT.*?;)",
        text,
        re.IGNORECASE | re.DOTALL
    )

    if match:
        return match.group(1).strip()

    return text

    st.code(sql)

def execute_sql(sql):

    try:

        result = pd.read_sql_query(
            sql,
            conn
        )

        return result

    except Exception as e:

        return str(e)

# ====================================================
# RAG CHATBOT
# ====================================================

def rag_answer(question):

    if vectorstore is None:
        return "FAISS index not found."

    docs = vectorstore.similarity_search(
        question,
        k=4
    )

    context = "\n".join(
        [d.page_content for d in docs]
    )

    prompt = f"""
    Answer ONLY using context.

    Context:
    {context}

    Question:
    {question}
    """

    response = model.generate_content(
        prompt
    )

    return response.text

# ====================================================
# KPI ANALYSIS
# ====================================================

def generate_kpi_insights():

    sales = df["Sales"].sum()

    profit = df["Profit"].sum()

    prompt = f"""
    Analyze:

    Total Sales = {sales}

    Total Profit = {profit}

    Give:

    Executive Summary
    Risks
    Opportunities
    Recommendations
    """

    response = model.generate_content(
        prompt
    )

    return response.text

# ====================================================
# CHART CREATOR
# ====================================================

def create_chart(df_result):

    if len(df_result.columns) < 2:
        return None

    fig = px.bar(

        df_result,

        x=df_result.columns[0],

        y=df_result.columns[1]

    )

    return fig

# ====================================================
# EXECUTIVE INSIGHTS
# ====================================================

def executive_summary(data):

    prompt = f"""
    Analyze:

    {data}

    Generate:

    Executive Summary

    Key Insights

    Risks

    Recommendations
    """

    response = model.generate_content(
        prompt
    )

    return response.text

# ====================================================
# SIDEBAR
# ====================================================

st.sidebar.title(
    "Analytics Agent Hub"
)

module = st.sidebar.selectbox(

    "Select Module",

    [

        "Dashboard",

        "AI SQL Assistant",

        "RAG Chatbot",

        "Dashboard Insight Generator",

        "Enterprise BI Copilot"

    ]
)

# ====================================================
# DASHBOARD
# ====================================================

if module == "Dashboard":

    st.title(
        "Executive Dashboard"
    )

    col1,col2,col3 = st.columns(3)

    col1.metric(
        "Total Sales",
        f"{df['Sales'].sum():,.0f}"
    )

    col2.metric(
        "Total Profit",
        f"{df['Profit'].sum():,.0f}"
    )

    col3.metric(
        "Orders",
        len(df)
    )

    region_sales = (

        df.groupby("Region")
        ["Sales"]
        .sum()
        .reset_index()

    )

    fig = px.bar(

        region_sales,

        x="Region",

        y="Sales"

    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ====================================================
# SQL ASSISTANT
# ====================================================

elif module == "AI SQL Assistant":

    st.title(
        "AI SQL Assistant"
    )

    question = st.text_input(
        "Ask SQL Question"
    )

    if st.button(
        "Generate & Execute SQL"
    ):

        sql = generate_sql(question)

        st.subheader(
            "Generated SQL"
        )

        st.code(sql)

        result = execute_sql(sql)

        if isinstance(
            result,
            pd.DataFrame
        ):

            st.dataframe(result)

            fig = create_chart(result)

            if fig:
                st.plotly_chart(
                    fig,
                    use_container_width=True
                )

        else:

            st.error(result)

# ====================================================
# RAG CHATBOT
# ====================================================

elif module == "RAG Chatbot":

    st.title(
        "Enterprise RAG Chatbot"
    )

    question = st.text_input(
        "Ask Document Question"
    )

    if st.button(
        "Search Documents"
    ):

        answer = rag_answer(question)

        st.write(answer)

# ====================================================
# DASHBOARD INSIGHTS
# ====================================================

elif module == "Dashboard Insight Generator":

    st.title(
        "AI Dashboard Insight Generator"
    )

    st.dataframe(
        df.head()
    )

    if st.button(
        "Generate Insights"
    ):

        insights = generate_kpi_insights()

        st.write(
            insights
        )

# ====================================================
# ENTERPRISE BI COPILOT
# ====================================================

elif module == "Enterprise BI Copilot":

    st.title(
        "Enterprise BI Copilot"
    )

    question = st.text_input(
        "Ask Business Question"
    )

    if st.button(
        "Analyze"
    ):

        prompt = f"""
        You are an enterprise analytics copilot.

        Dataset Columns:

        {list(df.columns)}

        Business Question:

        {question}

        Provide:

        1 Executive Summary

        2 Key Insights

        3 Recommended KPIs

        4 Recommended Charts

        5 Business Recommendations
        """

        response = model.generate_content(
            prompt
        )

        st.write(
            response.text
        )

        st.session_state.history.append(
            {
                "question":question,
                "answer":response.text
            }
        )

    st.subheader(
        "Conversation History"
    )

    for item in reversed(
        st.session_state.history[-5:]
    ):

        st.write(
            f"Q: {item['question']}"
        )

        st.write(
            f"A: {item['answer']}"
        )

        st.divider()