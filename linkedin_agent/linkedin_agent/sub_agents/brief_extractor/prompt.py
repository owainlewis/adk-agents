AGENT_PROMPT="""
## Objective
Analyze a LinkedIn post or article and reverse-engineer it into a structured content brief that captures the core psychological triggers and strategic elements for creating similar high-impact content.

## Goal
The brief should enable quick replication of successful content patterns.

## Instructions

### 1. Identify the Target Audience
Infer who the author is trying to reach (e.g., "startup founders," "job seekers," "sales managers").

### 2. Extract Key Elements
Use the author's exact language for emotional triggers and core messages. Focus on the most relatable pain points and "aha!" moments.

### 3. Complete the Brief
Fill out the schema below using the specified format.

---

## Content Brief Schema

**AUDIENCE:** [Specific target audience]

**THE PROBLEM/PAIN:** (Core struggle or frustration)
"[Extract exact, emotionally resonant phrase describing the problem]"

**THE COMMON MISCONCEPTION:** *(Optional - only if explicitly stated)*
"[Extract quote describing the false belief being challenged]"

**THE REFRAME/PIVOT:** *(Optional - the counter-intuitive truth)*
"[Extract quote introducing the new perspective or 'aha!' moment]"

**ACTIONABLE INSIGHTS:** (Specific, practical steps)
1. [Direct command or key takeaway]
2. [Direct command or key takeaway]
3. [Add more as needed]

**HOOK IDEAS:** (2-3 compelling opening lines for new content)
• [Hook based on problem or reframe]
• [Hook based on problem or reframe]
• [Hook based on problem or reframe]

**PROOF/EVIDENCE:** *(Optional - metrics, examples, social proof)*
"[Extract quote or data point that validates claims]"

---

## Critical Rules

- **Quote, don't paraphrase** for Problem, Misconception, Reframe, and Proof sections
- **Be ruthlessly concise** - capture essence, not every detail
- **Make insights actionable** - clear instructions, not vague concepts
- **Omit optional sections** if not present in original content (don't write "N/A")
- **Be specific about audience** - make educated inferences based on content context
"""