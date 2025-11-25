# Quick Start Guide

## Complete Setup and Run (5 minutes to start)

### 1. Check Your Setup
```bash
cd "/Users/marco/Documents/ai for customer research/llm_analysis"
./check_setup.sh
```

This will verify:
- ✅ Ollama is installed and running
- ✅ gpt-oss:120b model is available
- ✅ Python dependencies are installed (ollama, python-docx)
- ✅ Transcript files (.docx) are accessible

### 2. Run the Complete Analysis
```bash
./run_analysis.sh
```

This will:
1. Analyze all 27 interview transcripts (~2-7 hours total, depending on hardware)
2. Create individual analysis JSON files
3. Synthesize a comprehensive final report

**OR** run steps individually:

```bash
# Step 1: Analyze interviews (long-running)
python3 analyze_interviews.py

# Step 2: Create final report (fast)
python3 synthesize_report.py
```

## If You Need to Install Prerequisites

### Install Ollama
```bash
# macOS
brew install ollama

# Start the service
ollama serve
```

### Pull the Model (⚠️  ~240GB download, requires ~128GB RAM)
```bash
ollama pull gpt-oss:120b
```

**Don't have enough resources?** Use a smaller model:
```bash
# Alternative: 70B model (~140GB, ~64GB RAM)
ollama pull llama3.1:70b

# Then edit config.py and change:
# OLLAMA_MODEL = "llama3.1:70b"
```

### Install Python Dependencies
```bash
pip install -r requirements.txt
```

## Expected Timeline

| Step | Duration | Output |
|------|----------|--------|
| Setup check | < 1 min | Verification report |
| Interview analysis | 2-7 hours | 27 JSON files + summary |
| Report synthesis | 2-5 min | Final markdown report |

**Total time**: ~2-7 hours (can run overnight)

## What You Get

After completion, check the `output/` directory for:

1. **FINAL_ANALYSIS_REPORT.md** - Your main deliverable
   - Overall insights mapped to research questions
   - Pattern analysis across interviews
   - Unique findings per participant
   - Supporting quotes organized by topic

2. **Individual analysis files** - One per interview (27 files)
   - Structured JSON with behaviors, pain points, etc.

3. **Summary statistics** - Aggregated metrics

## Monitoring Progress

The analysis will print progress like:
```
[1/27] Processing en_response_0001-1764080428.docx
🤖 Analyzing en_response_0001-1764080428 with gpt-oss:120b...
✅ Successfully analyzed en_response_0001-1764080428
```

You can:
- Let it run in the background
- Check `output/` directory for completed analyses
- Stop and resume (it won't re-analyze completed interviews)

## Next Steps

1. Read `output/FINAL_ANALYSIS_REPORT.md`
2. Compare with Coloop and Marvin analyses
3. Present findings in class discussion

## Need Help?

See full `README.md` for:
- Detailed configuration options
- Troubleshooting common issues
- Alternative model recommendations
- Output file format specifications
