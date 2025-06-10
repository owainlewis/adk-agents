# LinkedIn Agent

A LinkedIn content strategist agent for creating structured content briefs from source material.

## Architecture

This LinkedIn agent follows the Google ADK agent pattern:

```
linkedin_agent/
├── linkedin_agent/
│   ├── tools/                # Agent tools
│   │   ├── __init__.py
│   │   └── linkedin_tools.py # Content brief extraction tool
│   ├── __init__.py
│   └── agent.py              # Main agent implementation
├── pyproject.toml            # Project configuration
└── README.md                 # This file
```

## Features

The LinkedIn agent provides a single specialized tool:

### Extract Brief Tool
- **Purpose**: Provides a structured prompt template for content analysis
- **Input**: Any text content (articles, videos, podcasts, ideas)
- **Output**: A detailed prompt template for extracting structured insights
- **Use Case**: Helps analyze content to identify pain points, insights, and proof points for LinkedIn content creation

## Setup

### 1. Install Dependencies

1. Navigate to the linkedin_agent directory:
```bash
cd linkedin_agent
```

2. Install the project:
```bash
pip install -e .
```

### 2. Configure Environment (Optional)

If you need environment variables, create a `.env` file:
```bash
GOOGLE_CLOUD_PROJECT=your-project-id
GOOGLE_CLOUD_REGION=your-region
```

## Usage

### Basic Usage

```python
from linkedin_agent.linkedin_agent import root_agent

# The agent can help you analyze content for LinkedIn post creation
content = """
Your article or content here...
"""

# Ask the agent to help extract insights from content
response = root_agent.run(f"Help me analyze this content for LinkedIn: {content}")
print(response.text)
```

### Available Tool

The agent has access to one tool:
- `extract_brief`: Returns a structured prompt template for content analysis

### Content Analysis Template

When using the extract_brief tool, you'll get a template that helps you structure content analysis with these sections:
- **THE PROBLEM/PAIN**: Emotional pain points from the content
- **MISCONCEPTION**: False beliefs mentioned (optional)
- **REFRAME**: Counter-intuitive truths (optional)
- **YOUR INSIGHTS**: Key actionable lessons (1-3 points)
- **PROOF IT WORKS**: Metrics/results/examples (optional)

## Development

### Running Tests
```bash
pytest tests/
```

### Code Formatting
```bash
black linkedin_agent/
isort linkedin_agent/
```

### Type Checking
```bash
mypy linkedin_agent/
```