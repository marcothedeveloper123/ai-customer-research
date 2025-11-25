"""Configuration for the interview analysis project."""

# Ollama settings
OLLAMA_MODEL = "gpt-oss:120b"
OLLAMA_BASE_URL = "http://localhost:11434"

# Paths
TRANSCRIPTS_DIR = "/Users/marco/Documents/ai for customer research/AI for Customer Research Nov 2025"
OUTPUT_DIR = "/Users/marco/Documents/ai for customer research/llm_analysis/output"

# Research Questions
RESEARCH_QUESTIONS = """
1. **Current behaviors**: How people use AI tools in their personal lives (e.g., planning, health, learning, productivity, decision-making)?
2. **Pain points and failures**: Where today's tools break down or fall short of users' expectations?
3. **Mental models of trust and reliance**: What makes people trust an AI assistant? What are their fears or hesitations?
4. **Desire and delight**: What would make the ideal AI assistant that people would want to engage with regularly?
"""

# Analysis prompt template
ANALYSIS_PROMPT = """You are an expert UX Researcher specializing in analyzing qualitative interview data and extracting high-quality insights.

RESEARCH QUESTIONS:
{research_questions}

TASK:
Analyze the following interview transcript to identify:
- Pain points and recurring patterns
- Unique perspectives
- Behaviors related to AI tool usage
- Trust and reliance factors
- Desires and aspirations

TRANSCRIPT:
{transcript}

Provide your analysis in the following JSON format:
{{
    "participant_id": "transcript filename",
    "key_behaviors": ["behavior 1", "behavior 2", ...],
    "pain_points": ["pain 1", "pain 2", ...],
    "trust_factors": ["factor 1", "factor 2", ...],
    "desires": ["desire 1", "desire 2", ...],
    "verbatim_quotes": [
        {{"quote": "exact quote text", "topic": "what this quote is about"}},
        ...
    ],
    "unique_insights": "any unique or surprising findings from this participant"
}}

Only include findings that are explicitly stated or strongly implied in the transcript. Use ONLY verbatim quotes.
"""
