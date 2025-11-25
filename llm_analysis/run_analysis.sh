#!/bin/bash
# Run Complete Analysis Pipeline

echo "🚀 Starting Complete Interview Analysis Pipeline"
echo ""

# Step 1: Run setup check
echo "Step 0: Checking setup..."
bash check_setup.sh
echo ""

read -p "⚠️  Press Enter to continue with analysis, or Ctrl+C to abort..."
echo ""

# Step 2: Analyze all interviews
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "Step 1: Analyzing all interviews..."
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
python3 analyze_interviews.py

if [ $? -ne 0 ]; then
    echo ""
    echo "❌ Analysis failed! Check errors above."
    exit 1
fi

echo ""
read -p "⚠️  Analysis complete. Press Enter to generate synthesis report, or Ctrl+C to stop..."
echo ""

# Step 3: Synthesize report
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "Step 2: Synthesizing final report..."
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
python3 synthesize_report.py

if [ $? -ne 0 ]; then
    echo ""
    echo "❌ Synthesis failed! Check errors above."
    exit 1
fi

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "✨ Complete! Check output/FINAL_ANALYSIS_REPORT.md"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
