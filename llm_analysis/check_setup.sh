#!/bin/bash
# Check Ollama Setup Script

echo "🔍 Checking Ollama Setup..."
echo ""

# Check if Ollama is installed
if command -v ollama &> /dev/null; then
    echo "✅ Ollama is installed"
    ollama --version
else
    echo "❌ Ollama is NOT installed"
    echo "   Install with: brew install ollama"
    exit 1
fi

echo ""

# Check if Ollama is running
if curl -s http://localhost:11434/api/tags &> /dev/null; then
    echo "✅ Ollama service is running"
else
    echo "⚠️  Ollama service is NOT running"
    echo "   Start with: ollama serve"
    echo ""
fi

# Check for gpt-oss:120b model
echo ""
echo "📦 Checking for gpt-oss:120b model..."
if ollama list | grep -q "gpt-oss:120b"; then
    echo "✅ gpt-oss:120b is installed"
else
    echo "❌ gpt-oss:120b is NOT installed"
    echo "   Install with: ollama pull gpt-oss:120b"
    echo "   ⚠️  Warning: This is ~240GB and requires ~128GB RAM"
fi

echo ""
echo "🐍 Checking Python dependencies..."
if python3 -c "import ollama" 2>/dev/null; then
    echo "✅ Python ollama package is installed"
else
    echo "❌ Python ollama package is NOT installed"
    echo "   Install with: pip install -r requirements.txt"
fi

if python3 -c "import docx" 2>/dev/null; then
    echo "✅ Python python-docx package is installed"
else
    echo "❌ Python python-docx package is NOT installed"
    echo "   Install with: pip install -r requirements.txt"
fi

echo ""
echo "📁 Checking transcript directory..."
TRANSCRIPT_DIR="/Users/marco/Documents/ai for customer research/AI for Customer Research Nov 2025"
if [ -d "$TRANSCRIPT_DIR" ]; then
    COUNT=$(ls "$TRANSCRIPT_DIR"/*.docx 2>/dev/null | wc -l | tr -d ' ')
    echo "✅ Transcript directory exists with $COUNT files"
else
    echo "❌ Transcript directory NOT found"
fi

echo ""
echo "✨ Setup check complete!"
