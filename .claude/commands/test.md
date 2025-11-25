---
description: "Run comprehensive test suite with model validation"
category: "project"
---

# Project Test Command

Execute comprehensive testing including unit, integration, and model validation tests.

## Usage

```bash
/project:test [options]
```

## Options

- `--unit-only`: Run only unit tests
- `--integration-only`: Run only integration tests
- `--coverage`: Generate coverage report
- `--verbose`: Verbose output with detailed logs
- `--fast`: Skip slow integration tests
- `--model`: Test specific Ollama model

## Steps

1. **Environment Check**: Verify Python environment and dependencies
2. **Ollama Status**: Check Ollama service availability
3. **Unit Tests**: Run isolated component tests
4. **Integration Tests**: Run full pipeline tests
5. **Model Validation**: Test Ollama model responses
6. **Coverage Report**: Generate code coverage analysis
7. **Summary**: Display test results and metrics

## Test Categories

### Unit Tests
- Data loader tests
- Text processor tests
- Ollama client tests
- Utility function tests

### Integration Tests
- Full pipeline execution
- End-to-end analysis workflow
- Model interaction tests
- Output validation

### Model Validation
- Model availability check
- Response quality tests
- Performance benchmarks
- Error handling tests

## Example

```bash
/project:test --coverage --verbose
/project:test --unit-only --fast
/project:test --model llama2
```

## Expected Output

- Test results summary (passed/failed/skipped)
- Coverage report (if --coverage flag used)
- Performance metrics
- Any test failures with detailed traceback
