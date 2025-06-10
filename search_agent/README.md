# Search Agent

This is a simple agent that can search the internet using Google ADK.

## Setup

### 1. Configure Google Cloud / Vertex AI

Before running the agent, you need to configure access to Google Cloud's Vertex AI:

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

Alternatively, you can set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable to point to a service account key file.

### 2. Install Dependencies

1. Create a virtual environment using uv:

```bash
uv venv
```

2. Activate the virtual environment:

```bash
source .venv/bin/activate  # On macOS/Linux
```

3. Install the project in editable mode:

```bash
uv pip install -e .
```

## Usage

```
adk web
```