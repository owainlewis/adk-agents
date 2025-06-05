# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Structure

This is a Python-based agents project using Google ADK (Agent Development Kit). The project follows the ADK agent structure pattern:

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

## Current Agents

- `linkedin-agent/` - LinkedIn networking and automation agent

## Development Commands

Each agent has its own pyproject.toml with dependencies:

```bash
# Install agent dependencies
cd linkedin-agent
pip install -e .

# Install development dependencies
pip install -e ".[dev]"

# Run tests
pytest tests/

# Format code
black agent_name/
isort agent_name/

# Type checking
mypy agent_name/
```

## ADK Agent Pattern

- Each agent should have its own directory following the ADK structure
- Use `google-adk` as the main dependency
- Separate tools, prompts, and core agent logic
- Include deployment, evaluation, and testing directories
- Use environment variables for configuration