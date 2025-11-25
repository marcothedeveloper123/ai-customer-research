---
description: "Run comprehensive customer research analysis on specified data"
category: "project"
---

# Project Analysis Command

Execute comprehensive AI-powered customer research analysis.

## Usage

```bash
/project:analyze [file_path] [options]
```

## Arguments

- `file_path`: Path to input data file (CSV, JSON, or TXT)
- `--model`: Ollama model to use (default: llama2)
- `--output`: Output file path (default: data/output/analysis_results.json)
- `--format`: Output format (json|csv|markdown) (default: json)
- `--batch-size`: Batch size for processing (default: 10)
- `--focus`: Analysis focus (sentiment|themes|insights|all) (default: all)

## Steps

1. **Validate Input**: Check file exists and is readable
2. **Load Data**: Parse input file based on format
3. **Preprocess**: Clean and prepare text for analysis
4. **Ollama Check**: Verify Ollama is running and model is available
5. **Run Analysis**: Execute AI analysis with specified focus
6. **Generate Report**: Create comprehensive analysis report
7. **Save Results**: Export to specified output format

## Example

```bash
/project:analyze @data/input/customer_feedback.csv --model mistral --focus sentiment
```

## Expected Output

- Analysis results file in specified format
- Summary statistics and key insights
- Visualization data (if applicable)
- Processing metrics (time, tokens, etc.)
