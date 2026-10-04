# AI Data Agent

Intelligent multi-agent system for automating data operations, SQL query generation, and ETL pipeline construction using LangChain and Claude AI.

## 📋 Overview

The AI Data Agent is a conversational system designed to handle complex data tasks through specialized agents. It understands natural language queries and routes them to appropriate data processing agents, enabling users to generate SQL queries, build ETL pipelines, and perform data analysis without manual coding.

**Tech:** LangChain, LangGraph, Claude AI, PostgreSQL, Python  
**Features:** SQL query generation, ETL design, multi-agent orchestration  
**Status:** 🚀 Active Development

---

## 🏗️ Architecture

```
User Query
    ↓
[LangGraph Orchestrator]
    ├→ [SQL Analyst Agent] - SQL query generation & execution
    ├→ [ETL Analyst Agent] - Pipeline design & orchestration
    └→ [Data Orchestrator Agent] - Multi-step workflow coordination
    ↓
Structured Response
```

---

## 🛠️ Tech Stack

| Category | Technologies |
|----------|---------------|
| **LLM Framework** | LangChain, LangGraph |
| **AI Model** | Claude (Anthropic API) |
| **Database** | PostgreSQL |
| **Language** | Python 3.9+ |
| **Data Processing** | Pandas, SQLAlchemy |
| **Interface** | Interactive CLI |

---

## 📁 Project Structure

```
AI_Data_Agent/
├── agents/                    # Specialized agent implementations
│   ├── data_orchestrator.py
│   ├── sql_analyst.py
│   └── etl_analyst.py
├── models/                    # Pydantic schemas
├── utils/                     # Utility functions
├── src/                       # Additional source modules
├── data/                      # Data files and resources
├── main.py                    # CLI entry point
├── feed_db.py                 # Database utilities
├── pyproject.toml             # Project configuration
└── README.md
```

---

## 🚀 Quick Start

### Prerequisites
- Python 3.9+
- PostgreSQL database
- Anthropic API key

### Installation

```bash
# Clone repository
git clone https://github.com/vinayshetty777/AI_Data_Agent.git
cd AI_Data_Agent

# Install dependencies
uv sync
# Or: pip install -e .

# Configure environment
cp .env.example .env
# Add your credentials to .env
```

### Run Agent

```bash
python main.py
```

---

## 📖 Usage Examples

### Generate SQL Query
```
User: "Show me all customers with orders over $1000 in the last month"
Agent: [Analyzes schema, generates optimized SQL, returns results]
```

### Design ETL Pipeline
```
User: "Build a pipeline to clean customer data and load to warehouse"
Agent: [Designs workflow, implements transformations, sets up scheduling]
```

### Data Analysis
```
User: "What are the top 10 products by revenue? Show 6-month trend"
Agent: [Analyzes data, generates insights, returns visualizations]
```

---

## ✨ Key Features

- **Multi-Agent Architecture** - Specialized agents for different data tasks
- **Natural Language Processing** - Understand complex data queries
- **SQL Generation** - Automatic query generation from natural language
- **ETL Pipeline Design** - Build data transformation workflows
- **Error Recovery** - Intelligent error handling and retry logic
- **Database Integration** - Direct PostgreSQL connectivity

---

## 🧪 Testing

```bash
# Run all tests
pytest

# Run specific test
pytest tests/test_agents.py -v

# With coverage
pytest --cov=.
```

---

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| Connection refused | Ensure PostgreSQL is running and DATABASE_URL is correct |
| API key errors | Verify ANTHROPIC_API_KEY is set correctly |
| Agent not responding | Check LLM API usage limits and network connectivity |

---

## 🔐 Best Practices

✅ **Do:**
- Use descriptive query names
- Validate input data before processing
- Log all operations for debugging
- Keep agent responsibilities focused

❌ **Don't:**
- Modify schemas directly without backups
- Run untested queries on production
- Ignore error messages
- Hardcode credentials

---

## 🤝 Contributing

Contributions welcome! Please:
1. Follow PEP 8 style guide
2. Add tests for new features
3. Update documentation
4. Submit pull requests with detailed descriptions

---

## 📚 Resources

- [LangChain Documentation](https://python.langchain.com/)
- [LangGraph Guide](https://langchain-ai.github.io/langgraph/)
- [Claude API Docs](https://docs.anthropic.com/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)

---

**Last Updated:** 2026-09-30  
**Python Version:** ≥3.9
