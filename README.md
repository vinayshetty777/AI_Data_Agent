# AI Data Agent

An intelligent multi-agent system powered by LangChain, LangGraph, and Claude AI that automates data operations, SQL query generation, and ETL pipeline construction.

## 🎯 Project Overview

The AI Data Agent is a conversational system designed to handle complex data tasks through specialized agents. It understands natural language queries and routes them to appropriate data processing agents, enabling users to:

- **Generate and execute SQL queries** - Understand database schemas and construct complex queries
- **Build ETL pipelines** - Design and implement data transformation workflows
- **Perform data analysis** - Derive insights and statistics from datasets
- **Manage database operations** - Handle data ingestion, transformation, and validation

## 🏗️ Architecture

```
User Query
    ↓
[LangGraph Orchestrator]
    ├→ [SQL Analyst Agent]
    │  └→ SQL query generation & execution
    ├→ [ETL Analyst Agent]
    │  └→ Pipeline design & orchestration
    └→ [Data Orchestrator Agent]
       └→ Multi-step workflow coordination
    ↓
Structured Response
```

### Agent Specializations

- **Data Orchestrator**: Coordinates complex multi-step workflows and manages dependencies
- **SQL Analyst**: Handles database schema analysis, query generation, and execution
- **ETL Analyst**: Designs data transformation pipelines and implements business logic

## 🛠️ Tech Stack

- **LLM Framework**: LangChain + LangGraph
- **AI Model**: Claude (via Anthropic API)
- **Database**: PostgreSQL
- **Language**: Python 3.9+
- **Data Processing**: Pandas, SQLAlchemy
- **Interface**: Interactive CLI

## 📁 Project Structure

```
AI_Data_Agent/
├── agents/                 # Specialized agent implementations
│   ├── data_orchestrator.py
│   ├── sql_analyst.py
│   └── etl_analyst.py
├── models/                 # Pydantic schemas and data models
│   ├── data_models.py
│   └── schemas.py
├── utils/                  # Utility functions
│   ├── llm_selection.py
│   └── helpers.py
├── src/                    # Additional source modules
├── data/                   # Data files and resources
├── main.py                 # CLI entry point
├── feed_db.py              # Database population utilities
├── pyproject.toml          # Project configuration
└── README.md               # This file
```

## 🚀 Setup & Installation

### Prerequisites
- Python 3.9 or higher
- PostgreSQL database running
- Anthropic API key
- pip or uv package manager

### Installation Steps

1. **Clone the repository:**
   ```bash
   git clone https://github.com/vinayshetty777/AI_Data_Agent.git
   cd AI_Data_Agent
   ```

2. **Install dependencies:**
   ```bash
   # Using uv (recommended)
   uv sync
   
   # Or using pip
   pip install -e .
   ```

3. **Configure environment variables:**
   ```bash
   # Create .env file
   cp .env.example .env
   
   # Add your credentials
   ANTHROPIC_API_KEY=your_api_key_here
   DATABASE_URL=postgresql://user:password@localhost:5432/database_name
   ```

4. **Initialize the database:**
   ```bash
   python feed_db.py
   ```

## 📖 Usage

### Running the Interactive CLI

```bash
python main.py
```

### Example Queries

**SQL Query Generation:**
```
User: "Show me all customers with orders over $1000 in the last month"
Agent: Analyzes schema, generates optimized SQL, and returns results
```

**ETL Pipeline Design:**
```
User: "Build a pipeline to clean customer data, deduplicate records, and load to warehouse"
Agent: Designs workflow, implements transformations, and sets up scheduling
```

**Data Analysis:**
```
User: "What are the top 10 products by revenue? Show me the trend over the last 6 months"
Agent: Analyzes data, generates insights, and returns visualizations
```

## 🤖 Agent Capabilities

### Data Orchestrator
- Breaks down complex requests into steps
- Coordinates multiple agents
- Manages dependencies between tasks
- Handles error recovery

### SQL Analyst
- Analyzes database schemas
- Generates optimized SQL queries
- Handles complex joins and aggregations
- Provides query performance insights

### ETL Analyst
- Designs data transformation logic
- Creates reusable pipeline components
- Implements data validation rules
- Handles incremental and full-load scenarios

## 📊 Data Models

The system uses Pydantic models for type safety:

```python
class QueryRequest(BaseModel):
    query: str
    context: Optional[Dict] = None
    agent_type: Optional[str] = None

class QueryResponse(BaseModel):
    response: str
    agent_used: str
    execution_time: float
```

## 🔄 Data Flow

```
1. User Input → Natural Language Query
2. LangGraph Orchestrator → Agent Selection
3. Selected Agent → Task Processing
4. Database/LLM Operations → Query Execution
5. Response Generation → User Output
```

## 🧪 Testing

Run tests to verify functionality:

```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_agents.py

# Run with coverage
pytest --cov=.
```

## 🐛 Troubleshooting

### Issue: "Connection refused" error
**Solution:** Ensure PostgreSQL is running and DATABASE_URL is correct in `.env`

### Issue: API key errors
**Solution:** Verify ANTHROPIC_API_KEY is set correctly in environment variables

### Issue: Agent not responding
**Solution:** Check LLM API usage limits and verify network connectivity

## 🔧 Development

### Adding a New Agent

1. Create a new agent file in `agents/`
2. Implement the agent class inheriting from `BaseAgent`
3. Register the agent in the orchestrator
4. Add tests for the new agent

### Example:

```python
from agents.base import BaseAgent

class CustomAgent(BaseAgent):
    def process(self, query: str) -> str:
        # Implementation
        pass
```

## 📝 Best Practices

✅ **Do:**
- Use descriptive query names
- Validate input data before processing
- Log all operations for debugging
- Keep agent responsibilities focused

❌ **Don't:**
- Modify schemas directly without backups
- Run untested queries on production
- Ignore error messages
- Leave hardcoded credentials

## 🤝 Contributing

Contributions welcome! Please:
1. Follow PEP 8 style guide
2. Add tests for new features
3. Update documentation
4. Submit pull requests with detailed descriptions

## 📄 License

This project is open source and available under the MIT License.

## 🔗 Related Resources

- [LangChain Documentation](https://python.langchain.com/)
- [LangGraph Guide](https://langchain-ai.github.io/langgraph/)
- [Claude API Docs](https://docs.anthropic.com/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)

---

**Project Status:** Active Development  
**Last Updated:** 2026-09-30  
**Python Version:** ≥3.9
