---
description: "Systematic troubleshooting for project issues"
category: "project"
---

# Project Debug Command

Systematic diagnostic and troubleshooting workflow for AI customer research project.

## Usage

```bash
/project:debug [options]
```

## Options

- `--check-models`: Verify Ollama models availability
- `--check-data`: Validate data files and formats
- `--check-config`: Review configuration files
- `--verbose`: Detailed diagnostic output
- `--fix`: Attempt automatic fixes for common issues
- `--log-level`: Set logging level (DEBUG|INFO|WARNING|ERROR)

## Diagnostic Steps

1. **Environment Check**
   - Python version and dependencies
   - Virtual environment status
   - Required packages installed

2. **Ollama Status**
   - Service running status
   - Available models
   - Connection test
   - Model loading test

3. **Configuration Validation**
   - Config file syntax
   - Model settings
   - Pipeline configuration
   - Environment variables

4. **Data Validation**
   - Input directory accessible
   - Sample files readable
   - Data format validation
   - Output directory writable

5. **Integration Tests**
   - Ollama client connection
   - Simple analysis test
   - End-to-end pipeline test

6. **Log Analysis**
   - Recent error messages
   - Warning patterns
   - Performance issues

## Common Issues & Fixes

### Ollama Not Running
```bash
# Check status
ollama list

# Start service
ollama serve
```

### Model Not Found
```bash
# Pull required model
ollama pull llama2
```

### Configuration Error
- Validate YAML syntax
- Check model names match available models
- Verify paths in config files

### Data Loading Error
- Check file format (CSV, JSON, TXT)
- Validate encoding (UTF-8)
- Verify file permissions

## Example

```bash
/project:debug --verbose
/project:debug --check-models --fix
/project:debug --check-data
```

## Expected Output

- System status summary
- Issue identification with severity
- Recommended fixes
- Detailed logs (if --verbose)
- Automatic fixes applied (if --fix)
