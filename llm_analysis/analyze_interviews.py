#!/usr/bin/env python3
"""
Interview Analysis using Local Ollama Model
Analyzes interview transcripts using gpt-oss:120b via Ollama
"""

import json
import os
from pathlib import Path
from datetime import datetime
import ollama
from docx import Document
from config import (
    OLLAMA_MODEL,
    TRANSCRIPTS_DIR,
    OUTPUT_DIR,
    RESEARCH_QUESTIONS,
    ANALYSIS_PROMPT
)


def setup_output_directory():
    """Create output directory if it doesn't exist."""
    Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)
    print(f"✅ Output directory ready: {OUTPUT_DIR}")


def get_transcript_files():
    """Get all transcript files from the transcripts directory."""
    transcript_path = Path(TRANSCRIPTS_DIR)
    files = sorted(transcript_path.glob("*.docx"))
    print(f"📁 Found {len(files)} transcript files")
    return files


def read_transcript(file_path):
    """Read a transcript file (Word document)."""
    try:
        doc = Document(file_path)
        # Extract all text from paragraphs
        content = '\n'.join([paragraph.text for paragraph in doc.paragraphs])
        return content
    except Exception as e:
        print(f"❌ Error reading {file_path.name}: {e}")
        return None


def analyze_transcript_with_ollama(transcript_content, participant_id):
    """Analyze a single transcript using Ollama."""
    try:
        prompt = ANALYSIS_PROMPT.format(
            research_questions=RESEARCH_QUESTIONS,
            transcript=transcript_content
        )
        
        print(f"🤖 Analyzing {participant_id} with {OLLAMA_MODEL}...")
        
        response = ollama.chat(
            model=OLLAMA_MODEL,
            messages=[{
                'role': 'user',
                'content': prompt
            }],
            options={
                'temperature': 0.1,  # Low temperature for consistent analysis
            }
        )
        
        # Extract the response content
        analysis_text = response['message']['content']
        
        # Try to parse as JSON
        try:
            # Sometimes the model wraps JSON in markdown code blocks
            if '```json' in analysis_text:
                analysis_text = analysis_text.split('```json')[1].split('```')[0].strip()
            elif '```' in analysis_text:
                analysis_text = analysis_text.split('```')[1].split('```')[0].strip()
            
            analysis = json.loads(analysis_text)
            print(f"✅ Successfully analyzed {participant_id}")
            return analysis
        except json.JSONDecodeError as e:
            print(f"⚠️  JSON parsing error for {participant_id}: {e}")
            # Save raw response for debugging
            return {
                "participant_id": participant_id,
                "raw_response": analysis_text,
                "parsing_error": str(e)
            }
    
    except Exception as e:
        print(f"❌ Error analyzing {participant_id}: {e}")
        return {
            "participant_id": participant_id,
            "error": str(e)
        }


def save_individual_analysis(analysis, participant_id):
    """Save individual analysis to a JSON file."""
    filename = f"{participant_id}_analysis.json"
    filepath = Path(OUTPUT_DIR) / filename
    
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(analysis, f, indent=2, ensure_ascii=False)


def save_combined_analyses(all_analyses):
    """Save all analyses to a single JSON file."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"all_analyses_{timestamp}.json"
    filepath = Path(OUTPUT_DIR) / filename
    
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(all_analyses, f, indent=2, ensure_ascii=False)
    
    print(f"💾 Saved combined analyses to: {filename}")
    return filepath


def generate_summary_report(all_analyses):
    """Generate a summary report from all analyses."""
    print("\n" + "="*80)
    print("📊 SUMMARY REPORT")
    print("="*80)
    
    successful = [a for a in all_analyses if 'error' not in a and 'parsing_error' not in a]
    failed = [a for a in all_analyses if 'error' in a or 'parsing_error' in a]
    
    print(f"\n✅ Successfully analyzed: {len(successful)} interviews")
    print(f"❌ Failed to analyze: {len(failed)} interviews")
    
    if failed:
        print("\nFailed interviews:")
        for analysis in failed:
            print(f"  - {analysis.get('participant_id', 'Unknown')}")
    
    # Aggregate insights from successful analyses
    all_behaviors = []
    all_pain_points = []
    all_trust_factors = []
    all_desires = []
    all_quotes = []
    
    for analysis in successful:
        all_behaviors.extend(analysis.get('key_behaviors', []))
        all_pain_points.extend(analysis.get('pain_points', []))
        all_trust_factors.extend(analysis.get('trust_factors', []))
        all_desires.extend(analysis.get('desires', []))
        all_quotes.extend(analysis.get('verbatim_quotes', []))
    
    print(f"\n📌 Total findings collected:")
    print(f"  - {len(all_behaviors)} behaviors")
    print(f"  - {len(all_pain_points)} pain points")
    print(f"  - {len(all_trust_factors)} trust factors")
    print(f"  - {len(all_desires)} desires")
    print(f"  - {len(all_quotes)} quotes")
    
    return {
        'summary': {
            'total_interviews': len(all_analyses),
            'successful': len(successful),
            'failed': len(failed)
        },
        'aggregated_findings': {
            'behaviors': all_behaviors,
            'pain_points': all_pain_points,
            'trust_factors': all_trust_factors,
            'desires': all_desires,
            'quotes': all_quotes
        }
    }


def main():
    """Main execution function."""
    print("🚀 Starting Interview Analysis with Ollama")
    print(f"📦 Using model: {OLLAMA_MODEL}")
    print()
    
    # Setup
    setup_output_directory()
    
    # Get all transcript files
    transcript_files = get_transcript_files()
    
    if not transcript_files:
        print("❌ No transcript files found!")
        return
    
    # Analyze each transcript
    all_analyses = []
    
    for i, file_path in enumerate(transcript_files, 1):
        print(f"\n[{i}/{len(transcript_files)}] Processing {file_path.name}")
        
        # Read transcript
        transcript_content = read_transcript(file_path)
        if not transcript_content:
            continue
        
        # Analyze with Ollama
        participant_id = file_path.stem
        analysis = analyze_transcript_with_ollama(transcript_content, participant_id)
        
        if analysis:
            all_analyses.append(analysis)
            save_individual_analysis(analysis, participant_id)
    
    # Save combined results
    if all_analyses:
        combined_path = save_combined_analyses(all_analyses)
        
        # Generate summary report
        summary = generate_summary_report(all_analyses)
        
        # Save summary report
        summary_path = Path(OUTPUT_DIR) / f"summary_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(summary_path, 'w', encoding='utf-8') as f:
            json.dump(summary, f, indent=2, ensure_ascii=False)
        
        print(f"\n💾 Saved summary report to: {summary_path.name}")
        print(f"\n✨ Analysis complete! Check the output directory: {OUTPUT_DIR}")
    else:
        print("\n❌ No analyses were successful!")


if __name__ == "__main__":
    main()
