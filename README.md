# Data Agent

An intelligent AI-powered agent for data operations, built with LangChain, LangGraph, and Claude AI. This agent helps with SQL queries, ETL operations, and data analysis tasks.

## Features

- **Interactive CLI**: User-friendly command-line interface for querying the agent
- **SQL Analysis**: Intelligent SQL query generation and analysis
- **ETL Operations**: Support for Extract, Transform, Load workflows
- **Multi-Agent Architecture**: Specialized agents for different data tasks
- **Claude AI Integration**: Powered by Claude for intelligent data understanding

## Project Structure

```
data-agent/
├── agents/              # Agent implementations
│   ├── data_agent.py   # Main agent orchestrator
│   ├── sql_analyst.py  # SQL analysis agent
│   └── etl_analyst.py  # ETL operations agent
├── models/              # Pydantic models and schemas
│   └── schema.py       # Data models for agents
├── utils/               # Utility functions
│   └── llm_pick.py     # LLM selection utility
├── src/                 # Additional source code
├── data/                # Data files and resources
├── main.py              # Entry point
├── feed_db.py          # Database feeding utilities
└── pyproject.toml      # Project configuration
```

## Installation

### Prerequisites
- Python 3.9+
- PostgreSQL (for database operations)

### Setup

1. **Clone the repository**
```bash
git clone <repository-url>
cd data-agent
```

2. **Install dependencies using uv**
```bash
uv sync
```

3. **Configure environment variables**
```bash
cp .env.example .env
# Edit .env with your configuration
```

Required environment variables:
- `ANTHROPIC_API_KEY`: Your Claude API key
- `DATABASE_URL`: PostgreSQL connection string
- Other API keys as needed

## Usage

### Running the Data Agent

Start the interactive CLI:
```bash
python main.py
```

Then interact with the agent:
```
Welcome to the Data Agent!
This agent can help you with SQL queries and ETL operations.
------------------------------------------------------------

Enter your query (or 'quit' to exit): Show me the top 10 customers by revenue
```

### Example Queries

- "Generate a SQL query to find active users"
- "Help me create an ETL pipeline for customer data"
- "Analyze database performance"
- "Create a data transformation workflow"

## Architecture

### Core Components

- **Data Agent**: Main orchestrator that routes queries to appropriate specialists
- **SQL Analyst**: Handles SQL query generation and database operations
- **ETL Analyst**: Manages data extraction, transformation, and loading
- **Router**: Intelligent query router that determines the best handler

### Technology Stack

- **LangChain**: AI/LLM framework
- **LangGraph**: Graph-based agent orchestration
- **Claude AI**: Language model backbone
- **Pydantic**: Data validation
- **PostgreSQL**: Database backend
- **Python 3.9+**: Runtime

## Development

### Environment Setup

```bash
# Create virtual environment
python -m venv .venv
.venv\Scripts\activate  # On Windows
source .venv/bin/activate  # On macOS/Linux

# Install dependencies
uv sync
```

### Running Tests

```bash
# Run test suite
pytest
```

## Configuration

### Database Connection

Update `.env` with your PostgreSQL connection details:
```
DATABASE_URL=postgresql://user:password@localhost:5432/database_name
```

### LLM Configuration

Modify `utils/llm_pick.py` to configure model selection and parameters.

## API Reference

### Data Agent

Main interface for all data operations:

```python
from agents.data_agent import data_agent
from langchain_core.messages import HumanMessage

response = data_agent.invoke({
    "messages": [HumanMessage(content="Your query here")],
    "route_response": ""
})
```

## Troubleshooting

### Database Connection Issues
- Verify PostgreSQL is running
- Check `DATABASE_URL` in `.env`
- Ensure database user has required permissions

### API Key Errors
- Confirm `ANTHROPIC_API_KEY` is set in `.env`
- Verify API key is valid in Anthropic console

### Import Errors
- Run `uv sync` to install all dependencies
- Ensure Python version is 3.9+

## Contributing

1. Create a feature branch
2. Make your changes
3. Test thoroughly
4. Submit a pull request

## License

MIT

## Author

Vinay Shetty (vinayshetty7899@gmail.com)

## Support

For issues and questions, please refer to the project documentation or contact the development team.
