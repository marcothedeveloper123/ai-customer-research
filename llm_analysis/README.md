# LLM-Based Interview Analysis Project

## Overview
This project uses a local AI model (gpt-oss:120b via Ollama) to analyze interview transcripts for user research on AI assistant usage.

## Research Questions
1. **Current behaviors**: How people use AI tools in their personal lives
2. **Pain points and failures**: Where today's tools break down or fall short
3. **Mental models of trust and reliance**: What makes people trust an AI assistant
4. **Desire and delight**: What would make the ideal AI assistant

## Project Structure
```
llm_analysis/
├── analyze_interviews.py    # Main script to analyze all transcripts
├── synthesize_report.py      # Creates final formatted report
├── config.py                 # Configuration and prompts
├── requirements.txt          # Python dependencies
├── README.md                 # This file
└── output/                   # Generated analysis files
    ├── *_analysis.json       # Individual interview analyses
    ├── all_analyses_*.json   # Combined analyses
    ├── summary_report_*.json # Summary statistics
    └── FINAL_ANALYSIS_REPORT.md # Final formatted report
```

## Prerequisites

### 1. Install Ollama
```bash
# macOS
brew install ollama

# Linux
curl -fsSL https://ollama.com/install.sh | sh

# Start Ollama service
ollama serve
```

### 2. Pull the GPT-OSS 120B Model
```bash
ollama pull gpt-oss:120b
```
⚠️ **Note**: This is a 120 billion parameter model and will require significant disk space (~240GB) and RAM (~128GB recommended).

### 3. Install Python Dependencies
```bash
cd "/Users/marco/Documents/ai for customer research/llm_analysis"
pip install -r requirements.txt
```

## Usage

### Step 1: Analyze All Interviews
This will process all 27 interview transcripts (Word documents) and create individual JSON analysis files:

```bash
python3 analyze_interviews.py
```

**What it does:**
- Reads all transcript files from the transcripts directory
- Sends each transcript to the local Ollama model with analysis prompt
- Extracts structured data: behaviors, pain points, trust factors, desires, quotes
- Saves individual analysis files for each interview
- Creates combined analysis file with all results

**Expected output:**
```
🚀 Starting Interview Analysis with Ollama
📦 Using model: gpt-oss:120b
✅ Output directory ready: .../output
📁 Found 27 transcript files

[1/27] Processing en_response_0001-1764080428.docx
🤖 Analyzing en_response_0001-1764080428 with gpt-oss:120b...
✅ Successfully analyzed en_response_0001-1764080428
...
```

**Time estimate:** ~5-15 minutes per interview (depending on hardware)

### Step 2: Synthesize Final Report
After all individual analyses are complete, create the final formatted report:

```bash
python3 synthesize_report.py
```

**What it does:**
- Loads all individual analysis JSON files
- Aggregates findings across all interviews
- Uses Ollama to synthesize insights and identify patterns
- Creates a formatted Markdown report with:
  - Overall insights mapped to research questions
  - Pattern analysis
  - Unique findings from individual participants
  - Supporting quotes organized by topic

**Output:** `output/FINAL_ANALYSIS_REPORT.md`

## Configuration

Edit `config.py` to customize:
- **Model**: Change `OLLAMA_MODEL` to use a different model
- **Paths**: Update `TRANSCRIPTS_DIR` and `OUTPUT_DIR`
- **Analysis prompt**: Modify `ANALYSIS_PROMPT` to change how interviews are analyzed
- **Temperature**: Adjust temperature in the scripts for more/less creative responses

## Output Files

### Individual Analysis Files
Each interview gets a JSON file with:
```json
{
  "participant_id": "en_response_0001",
  "key_behaviors": ["uses AI for research", "relies on AI for coding"],
  "pain_points": ["hallucinations", "lack of context retention"],
  "trust_factors": ["accuracy", "consistency"],
  "desires": ["better memory", "proactive suggestions"],
  "verbatim_quotes": [
    {"quote": "I wish it would remember...", "topic": "memory"}
  ],
  "unique_insights": "Uses AI as a rubber duck for debugging"
}
```

### Combined Analysis File
`all_analyses_[timestamp].json` - All individual analyses in one file

### Summary Report
`summary_report_[timestamp].json` - Statistics and aggregated counts

### Final Report
`FINAL_ANALYSIS_REPORT.md` - Formatted analysis report with insights


## Troubleshooting

### Ollama Connection Error
```
Error: Failed to connect to Ollama
```
**Solution**: Make sure Ollama is running:
```bash
ollama serve
```

### Model Not Found
```
Error: model 'gpt-oss:120b' not found
```
**Solution**: Pull the model first:
```bash
ollama pull gpt-oss:120b
```

### JSON Parsing Errors
If you see parsing errors, the model may not be returning valid JSON. Check the individual analysis files for `raw_response` fields to see what the model returned.

**Solutions**:
- Lower the temperature in the scripts (already set to 0.1)
- Use a different model that's better at structured output
- Modify the prompt to be more explicit about JSON format

### Out of Memory
The gpt-oss:120b model requires substantial RAM (~128GB recommended).

**Solutions**:
- Use a smaller model: `ollama pull gpt-oss:70b` or `ollama pull gpt-oss:30b`
- Update `OLLAMA_MODEL` in `config.py`
- Process interviews in smaller batches

## Alternative Models

If gpt-oss:120b is too resource-intensive, try:

```bash
# Smaller but still capable models
ollama pull llama3.1:70b
ollama pull mixtral:8x7b
ollama pull qwen2.5:72b

# Then update config.py:
OLLAMA_MODEL = "llama3.1:70b"  # or your chosen model
```

## Tips for Best Results

1. **Review individual analyses first**: Check a few `*_analysis.json` files to ensure quality before synthesizing
2. **Adjust prompts**: Modify `ANALYSIS_PROMPT` in `config.py` if results aren't meeting expectations
3. **Iterative refinement**: You can re-run synthesis multiple times without re-analyzing transcripts
4. **Manual review**: Always review AI-generated insights with your own expert judgment

## Project Context

This analysis is part of **Analysis Technique 1: LLM-Prompting** from:
- **Project 2**: AI-Powered Analysis for Customer Research
- **Research Goal**: Design a trusted, daily-use AI assistant for consumers
- **Data**: 27 AI-moderated interviews from November 2025
- **Format**: Word documents (.docx)

## Next Steps After Analysis

1. Review the `FINAL_ANALYSIS_REPORT.md`
2. Compare findings with Analysis Technique 2 (Coloop) and Technique 3 (Marvin)
3. Identify opportunity areas for AI assistant innovation
4. Develop product hypotheses based on insights
5. Share findings with stakeholders

## License & Attribution

This project is for educational purposes as part of an AI for Customer Research course.
