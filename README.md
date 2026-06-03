# Enterprise GenAI Analytics Platform

Analytics Agent Hub is a unified AI-powered analytics platform that combines SQL generation, Retrieval-Augmented Generation (RAG), dashboard insight automation, conversational business intelligence, and executive analytics into a single enterprise-grade application.

**Built using:**

* Python
* Streamlit
* Google Gemini
* SQLite
* FAISS
* LangChain
* Plotly
* Sentence Transformers.

  
### Project Overview

Organizations often maintain separate tools for:

* Business Intelligence
* SQL Querying
* Dashboard Analysis
* Document Search
* Executive Reporting

Analytics Agent Hub unifies these capabilities into one conversational interface.

## Architecture:
<img width="1536" height="1024" alt="Analytics_agent_hub_architecture_diagram" src="https://github.com/user-attachments/assets/afe3247d-6db0-4af0-9e55-caeea72c745a" />


## Features:

### 1. AI SQL Assistant

**Natural language to SQL generation.**

Example:

Show total sales by region

Generated SQL:

SELECT Region,
SUM(Sales) AS TotalSales
FROM Sales
GROUP BY Region;

**Capabilities:**

* SQL generation
* SQL validation
* SQL execution
* SQLite integration
* Dynamic result visualization

### 2. Enterprise RAG Chatbot

**Retrieval-Augmented Generation system for enterprise documents.**

**Capabilities:**

* PDF ingestion
* Vector embeddings
* Semantic search
* Context-aware question answering
* FAISS vector database

### Workflow:
<img width="1024" height="1536" alt="RAG_pipeline" src="https://github.com/user-attachments/assets/2ab73510-fe5c-4e1a-a524-a5ee9d189b78" />


### 3. Dashboard Insight Generator

Automated business intelligence insights.

**Capabilities:**

* KPI detection
* Trend analysis
* Region analysis
* Category analysis
* Executive summaries
* Business recommendations

**Generated Output:**

Executive Summary

Key Insights

Risks

Opportunities

Recommendations

### 4. Enterprise BI Copilot

Natural language business intelligence assistant.

**Examples:**

* Why did profit decline?
* What KPIs should management track?
* Recommend dashboard visuals.

**Capabilities:**

* KPI reasoning
* Analytics recommendations
* Visualization suggestions
* Executive reporting


## Technology Stack

* Frontend:	Streamlit
* LLM:	Gemini 2.5 Flash
* Vector Database:	FAISS
* Embeddings:	MiniLM
* Database:	SQLite
* Analytics:	Pandas
* Visualization:	Plotly
* RAG Framework:	LangChain

### Installation

**Clone Repository**

git clone https://github.com/yourusername/Analytics-Agent-Hub.git

cd Analytics-Agent-Hub

**Install Dependencies**

pip install -r requirements.txt

**Configure Gemini API:**

Inside analytics_agent_hub.py:

GEMINI_API_KEY="YOUR_API_KEY"

**Run Application**

streamlit run analytics_agent_app.py

Application launches at:

http://localhost:8501

### Screenshots

Executive Dashboard:
<img width="1347" height="588" alt="Dashboard_1" src="https://github.com/user-attachments/assets/195dee60-33fa-4d33-b7dd-d76ad8181ab7" />

SQL Assistant:
<img width="1357" height="604" alt="AI_SQL_Assistant_1" src="https://github.com/user-attachments/assets/228f1972-8486-4782-a366-73ea6650fb17" />

RAG Chatbot:
<img width="1364" height="577" alt="Enterprise_RAG_Chatbot_1" src="https://github.com/user-attachments/assets/e94ed40e-d4ee-4a38-9507-975060f193a9" />

Dashboard Insights:
<img width="1361" height="608" alt="AI_Dashboard_Insights_Generator_1" src="https://github.com/user-attachments/assets/25fe4bec-6460-403b-97ea-2dca7fb1917e" />

Enterprise BI:
<img width="1360" height="605" alt="Enterprise_BI_Copilot_1" src="https://github.com/user-attachments/assets/53bc9889-089f-4cf3-9483-4bde7dc07c32" />


**Example Questions**

SQL Assistant:

* Profit by region
* Top 2 Products by sales

RAG Chatbot:

* Summarize operational risks
* What policies mention inventory management?

BI Copilot:

* Why is profitability declining?
* Suggest revenue improvement strategies.

### Business Value

The platform enables:

* Self-service analytics
* Faster decision making
* Natural language data exploration
* Executive reporting automation
* Enterprise knowledge retrieval
* AI-assisted business intelligence

## Future Enhancements:

Planned improvements:

* Multi-Agent Workflow Engine
* Authentication
* Azure OpenAI Integration
* Power BI Integration
* Snowflake Integration
* Real-time Database Connections
* Dashboard Export to PDF
* KPI Forecasting
* Anomaly Detection Engine.

### Author:

Sayan Mukherjee
