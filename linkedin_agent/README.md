# LinkedIn Agent

A multi-agent system for creating viral LinkedIn content from any source material.

## Architecture

This LinkedIn agent follows the Google ADK multi-agent pattern:

```
linkedin_agent/
├── linkedin_agent/
│   ├── sub_agents/           # Specialized sub-agents
│   │   ├── brief_extractor/  # Extracts structured insights from content
│   │   └── quote_generator/  # Generates LinkedIn posts from briefs
│   ├── tools/                # Orchestration tools
│   ├── agent.py              # Root agent that coordinates sub-agents
│   └── prompt.py             # Root agent instructions
├── pyproject.toml            # Project configuration
└── README.md                 # This file
```

## Sub-Agents

### Brief Extractor
- **Purpose**: Analyzes any content to extract structured insights
- **Input**: Raw content (articles, videos, podcasts, ideas)
- **Output**: Structured brief with pain points, insights, and proof

### Quote Generator  
- **Purpose**: Creates viral LinkedIn posts from content briefs
- **Input**: Structured content brief
- **Output**: LinkedIn post optimized for engagement

## Setup

### 1. Configure Google Cloud / Vertex AI

1. Copy the environment template:
```bash
cp .env-sample .env
```

2. Edit `.env` and set your Google Cloud project details:
```bash
GOOGLE_CLOUD_PROJECT=your-project-id
GOOGLE_CLOUD_REGION=your-region
```

3. Authenticate with Google Cloud:
```bash
gcloud auth application-default login
```

### 2. Install Dependencies

1. Create a virtual environment:
```bash
uv venv
```

2. Activate the virtual environment:
```bash
source .venv/bin/activate  # On macOS/Linux
```

3. Install the project:
```bash
uv pip install -e .
```

## Usage

### Complete Pipeline
Transform any content directly into a LinkedIn post:
```python
from linkedin_agent import linkedin_agent

# Process raw content into LinkedIn post
content = """
Article about productivity techniques...
"""

response = linkedin_agent.run(f"Create a LinkedIn post from this content: {content}")
print(response.text)
```

### Step-by-Step Process
Extract insights first, then generate post:
```python
# Step 1: Extract brief
response = linkedin_agent.run(f"Extract insights from: {content}")
brief = response.text

# Step 2: Generate LinkedIn post  
response = linkedin_agent.run(f"Create a LinkedIn post from this brief: {brief}")
post = response.text
```

### Available Tools
The root agent has access to:
- `extract_brief`: Extract structured insights from raw content
- `generate_linkedin_post`: Create LinkedIn posts from briefs
- `process_content_to_post`: Complete pipeline from content to post

## Content Types Supported
- Blog articles and newsletters
- Podcast transcripts
- Video content summaries
- Book excerpts
- Personal experiences and stories
- Industry insights and observations

## LinkedIn Post Features
- Mobile-optimized hooks
- Proven engagement formulas
- Professional storytelling
- Actionable frameworks
- Pain point amplification
- Authority building
- Call-to-action optimization