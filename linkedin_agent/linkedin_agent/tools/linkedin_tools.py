from google.adk.tools import FunctionTool

# Brief Extraction Tool
def _extract_brief(content: str) -> str:
    """Extract a structured brief from any content for LinkedIn post creation."""
    prompt = f"""Analyze this content and extract a structured brief:

{content}

Extract using this EXACT format:

## Content Brief

**THE PROBLEM/PAIN** (in their words):
"[Extract exact words/phrases describing the problem. Most emotionally resonant one.]"

**MISCONCEPTION**: [False belief mentioned - only if explicitly stated] (optional)

**REFRAME**: [Counter-intuitive truth offered - only if clear paradigm shift] (optional)  

**YOUR INSIGHTS** (main lessons/tips):
1. [First key insight - specific and actionable]
2. [Second key insight - specific and actionable]
3. [Third key insight - specific and actionable]

**PROOF IT WORKS** (optional):
[Any metrics/results/examples mentioned that validate the approach]

Rules:
- Use actual language from content, not paraphrased
- Only include optional sections if explicitly present
- Focus on actionable advice in insights
- Number insights clearly
- Keep concise but specific
"""
    return prompt

extract_brief = FunctionTool(_extract_brief)
