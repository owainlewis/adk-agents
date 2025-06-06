# ADK Agents

This repository demonstrates sample agents built with the Google ADK (Agent Development Kit). It showcases different agent implementations following the ADK agent structure pattern for building intelligent, modular agents.

## About

The Google ADK provides a framework for building sophisticated agents that can interact with various services and APIs. This repository contains example implementations that demonstrate best practices for agent development, including proper project structure, tool integration, and deployment patterns.

## Project Structure

Each agent in this repository follows the standardized ADK agent structure:

```
agent-name/
├── agent_name/
│   ├── shared_libraries/           # Helper functions for tools
│   ├── sub_agents/                 # Sub-agents (if needed)
│   │   ├── tools/                  # Tools for sub-agents
│   │   ├── agent.py                # Sub-agent core logic
│   │   └── prompt.py               # Sub-agent prompts
│   ├── tools/                      # Tools used by the router agent
│   ├── __init__.py                 # Initializes the agent
│   ├── agent.py                    # Core logic of the agent
│   └── prompt.py                   # Prompts for the agent
├── deployment/                     # Deployment to Agent Engine
├── eval/                           # Evaluation methods
├── tests/                          # Unit tests for tools
├── .env.example                    # Environment variables template
├── pyproject.toml                  # Project configuration
└── README.md                       # Agent documentation
```

## Available Agents

- **`search-agent/`** - A search agent for performing various search operations
- **`linkedin-agent/`** - LinkedIn networking and automation agent

## Getting Started

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd adk-agents
   ```

2. **Choose an agent to work with:**
   ```bash
   cd search-agent  # or linkedin-agent
   ```

3. **Install the agent dependencies:**
   ```bash
   pip install -e .
   ```

4. **Install development dependencies (optional):**
   ```bash
   pip install -e ".[dev]"
   ```

5. **Set up environment variables:**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

### Development

Each agent includes standard development tools and commands:

```bash
# Run tests
pytest tests/

# Format code
black agent_name/
isort agent_name/

# Type checking
mypy agent_name/
```

### Running an Agent

Refer to each agent's individual README.md file for specific usage instructions and configuration details.

## Contributing

When adding new agents:

1. Follow the ADK agent structure pattern
2. Use `google-adk` as the main dependency
3. Separate tools, prompts, and core agent logic
4. Include deployment, evaluation, and testing directories
5. Use environment variables for configuration
6. Add comprehensive documentation

## License

[Add your license information here]