# AI Customer Research - Project Guide

**AI-powered customer research analysis system using Ollama for text analysis and insights extraction.**

## Project Overview

**Purpose**: Analyze customer feedback, surveys, and research data using AI to extract actionable insights and patterns.

**Core Capabilities**:
- Text analysis and sentiment detection
- Survey response processing
- Customer feedback categorization
- Insight extraction and summarization
- Pattern recognition in customer data

**Technology Stack**:
- **AI Framework**: Ollama (local LLM inference)
- **Data Processing**: pandas, numpy
- **Text Processing**: NLTK, spaCy (optional)
- **Visualization**: matplotlib, seaborn
- **Testing**: pytest, pytest-cov

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Install Ollama (if not already installed)
# Visit: https://ollama.ai or run: curl -fsSL https://ollama.ai/install.sh | sh

# Pull required models
ollama pull llama2
ollama pull mistral

# Run analysis
python -m src.main --input data/input/sample.csv

# Run tests
pytest tests/
```

## Project Structure

```
ai-customer-research/
├── CLAUDE.md                    # This file - project guide
├── .claude/
│   ├── settings.json           # Claude Code configuration
│   └── commands/               # Custom slash commands
│       ├── analyze.md          # /project:analyze
│       ├── test.md             # /project:test
│       └── debug.md            # /project:debug
├── config/
│   ├── models/
│   │   └── ollama.yaml        # Ollama model configuration
│   └── pipeline.yaml          # Processing pipeline settings
├── src/
│   ├── __init__.py
│   ├── main.py                # Entry point
│   ├── models/
│   │   ├── __init__.py
│   │   ├── ollama_client.py  # Ollama API integration
│   │   └── analyzer.py       # Analysis logic
│   ├── data/
│   │   ├── __init__.py
│   │   ├── loader.py         # Data loading utilities
│   │   └── processor.py      # Text preprocessing
│   └── utils/
│       ├── __init__.py
│       ├── config.py         # Configuration management
│       └── logger.py         # Logging setup
├── tests/
│   ├── unit/
│   │   ├── test_ollama_client.py
│   │   └── test_analyzer.py
│   ├── integration/
│   │   └── test_pipeline.py
│   └── fixtures/
│       └── sample_data.json
├── data/
│   ├── input/                 # Raw data files
│   ├── processed/            # Processed data
│   └── output/               # Analysis results
├── docs/
│   └── API.md                # API documentation
└── requirements.txt          # Python dependencies
```

## AI Model Configuration

### Ollama Setup

**Recommended Models**:
- **llama2**: General purpose, balanced performance
- **mistral**: Faster inference, good for production
- **codellama**: If code analysis is needed
- **neural-chat**: For conversational analysis

**Model Configuration** (`config/models/ollama.yaml`):
```yaml
default_model: llama2
temperature: 0.7
max_tokens: 2000
context_window: 4096

models:
  llama2:
    use_case: "general analysis"
    temperature: 0.7
  mistral:
    use_case: "fast inference"
    temperature: 0.6
```

### Ollama Client Usage

```python
from src.models.ollama_client import OllamaClient

client = OllamaClient(model="llama2")
response = client.analyze(text="Customer feedback here...")
```

## Data Processing Pipeline

### 1. Data Loading
```python
from src.data.loader import DataLoader

loader = DataLoader()
data = loader.load_csv("data/input/survey.csv")
```

### 2. Text Preprocessing
```python
from src.data.processor import TextProcessor

processor = TextProcessor()
cleaned = processor.clean(data['feedback'])
```

### 3. AI Analysis
```python
from src.models.analyzer import CustomerAnalyzer

analyzer = CustomerAnalyzer(model="llama2")
insights = analyzer.analyze(cleaned)
```

### 4. Results Export
```python
insights.to_csv("data/output/analysis_results.csv")
```

## Custom Slash Commands

### `/project:analyze`
Run comprehensive customer research analysis on specified data.

**Usage**:
```bash
/project:analyze @data/input/survey.csv
/project:analyze --model mistral --output results.json
```

### `/project:test`
Run test suite with model validation and integration tests.

**Usage**:
```bash
/project:test
/project:test --unit-only
/project:test --integration-only
```

### `/project:debug`
Systematic troubleshooting including Ollama connection and model issues.

**Usage**:
```bash
/project:debug
/project:debug --check-models
/project:debug --verbose
```

## Development Workflow

### Adding New Analysis Features

1. **Define analysis method** in `src/models/analyzer.py`
2. **Add configuration** to `config/pipeline.yaml`
3. **Write unit tests** in `tests/unit/`
4. **Add integration test** in `tests/integration/`
5. **Update documentation** in `docs/API.md`

### Testing Strategy

**Unit Tests**: Test individual components in isolation
```bash
pytest tests/unit/ -v
```

**Integration Tests**: Test full pipeline with real Ollama models
```bash
pytest tests/integration/ -v
```

**Coverage**: Maintain >80% code coverage
```bash
pytest --cov=src --cov-report=html
```

## Configuration Management

### Environment Variables
```bash
# Ollama connection
OLLAMA_HOST=http://localhost:11434
OLLAMA_TIMEOUT=120

# Data paths
DATA_INPUT_PATH=data/input
DATA_OUTPUT_PATH=data/output

# Logging
LOG_LEVEL=INFO
LOG_FILE=logs/app.log
```

### Config Files

**`config/models/ollama.yaml`**: Model settings and parameters
**`config/pipeline.yaml`**: Processing pipeline configuration

## Error Handling

### Common Issues

**Ollama Connection Error**:
```bash
# Check Ollama is running
ollama list

# Restart Ollama service
ollama serve
```

**Model Not Found**:
```bash
# Pull required model
ollama pull llama2
```

**Memory Issues**:
```yaml
# Reduce context window in config/models/ollama.yaml
context_window: 2048
```

## Performance Optimization

### Batch Processing
```python
analyzer = CustomerAnalyzer(batch_size=10)
results = analyzer.analyze_batch(data_list)
```

### Caching
```python
from src.utils.cache import cache_results

@cache_results(ttl=3600)
def analyze_feedback(text):
    return client.analyze(text)
```

### Async Processing
```python
import asyncio
from src.models.async_analyzer import AsyncAnalyzer

async def process_large_dataset(data):
    analyzer = AsyncAnalyzer()
    results = await analyzer.analyze_async(data)
```

## Deployment

### Local Deployment
```bash
# Ensure Ollama is running
ollama serve

# Run analysis service
python -m src.main --mode server --port 8000
```

### Docker Deployment
```bash
# Build image
docker build -t ai-customer-research .

# Run container
docker run -p 8000:8000 ai-customer-research
```

## Monitoring & Logging

**Log Files**: `logs/app.log`
**Metrics**: Track inference time, token usage, error rates

```python
from src.utils.logger import get_logger

logger = get_logger(__name__)
logger.info("Starting analysis...")
```

## Security Considerations

- **Data Privacy**: Ollama runs locally, data never leaves your machine
- **Input Validation**: Sanitize all user inputs before processing
- **Rate Limiting**: Implement rate limits for API endpoints
- **Access Control**: Secure sensitive data files with proper permissions

## Troubleshooting Guide

### Systematic Debugging Process

1. **Check Ollama Status**: `ollama list`
2. **Verify Model Availability**: `ollama show llama2`
3. **Test Simple Request**: `ollama run llama2 "test"`
4. **Check Logs**: `tail -f logs/app.log`
5. **Run Diagnostics**: `/project:debug --verbose`

### Performance Issues

- Reduce `max_tokens` in config
- Use smaller model (mistral instead of llama2)
- Enable batch processing
- Implement caching for repeated queries

## Contributing

### Code Style
- Follow PEP 8
- Use type hints
- Add docstrings to all functions
- Keep functions focused and testable

### Git Workflow
```bash
# Create feature branch
git checkout -b feature/new-analysis

# Make changes and test
pytest tests/

# Commit with descriptive message
git commit -m "feat: add sentiment analysis module"

# Push and create PR
git push origin feature/new-analysis
```

## Resources

**Ollama Documentation**: https://ollama.ai/docs
**Project Issues**: Track bugs and features in project tracker
**API Reference**: See `docs/API.md`

## Next Steps

1. ✅ Project initialized
2. ⏳ Install dependencies: `pip install -r requirements.txt`
3. ⏳ Install Ollama: https://ollama.ai
4. ⏳ Pull models: `ollama pull llama2`
5. ⏳ Add sample data to `data/input/`
6. ⏳ Run first analysis: `python -m src.main`
7. ⏳ Explore custom commands: `/project:analyze --help`

---

**Project initialized with Claude Code on 2025-11-25**
