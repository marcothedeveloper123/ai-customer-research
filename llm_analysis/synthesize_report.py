#!/usr/bin/env python3
"""
Synthesize Analysis Results
Creates a final report in the format specified in the project instructions
"""

import json
from pathlib import Path
from collections import Counter, defaultdict
from config import OUTPUT_DIR, OLLAMA_MODEL
import ollama


def load_all_analyses():
    """Load all individual analysis files."""
    output_path = Path(OUTPUT_DIR)
    analysis_files = list(output_path.glob("*_response_*_analysis.json"))
    
    analyses = []
    for file_path in analysis_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                analysis = json.load(f)
                if 'error' not in analysis and 'parsing_error' not in analysis:
                    analyses.append(analysis)
        except Exception as e:
            print(f"⚠️  Error loading {file_path.name}: {e}")
    
    print(f"📊 Loaded {len(analyses)} successful analyses")
    return analyses


def aggregate_findings(analyses):
    """Aggregate findings across all analyses."""
    aggregated = {
        'behaviors': [],
        'pain_points': [],
        'trust_factors': [],
        'desires': [],
        'quotes': [],
        'unique_insights': []
    }
    
    for analysis in analyses:
        aggregated['behaviors'].extend(analysis.get('key_behaviors', []))
        aggregated['pain_points'].extend(analysis.get('pain_points', []))
        aggregated['trust_factors'].extend(analysis.get('trust_factors', []))
        aggregated['desires'].extend(analysis.get('desires', []))
        
        # Store quotes with participant info
        participant_id = analysis.get('participant_id', 'Unknown')
        for quote_obj in analysis.get('verbatim_quotes', []):
            aggregated['quotes'].append({
                'quote': quote_obj.get('quote', ''),
                'topic': quote_obj.get('topic', ''),
                'participant': participant_id
            })
        
        # Collect unique insights
        unique = analysis.get('unique_insights', '')
        if unique:
            aggregated['unique_insights'].append({
                'participant': participant_id,
                'insight': unique
            })
    
    return aggregated


def synthesize_with_ollama(aggregated_data, total_interviews):
    """Use Ollama to synthesize insights from aggregated data."""
    
    synthesis_prompt = f"""You are an expert UX Researcher creating a final analysis report.

RESEARCH QUESTIONS:
1. Current behaviors: How people use AI tools in their personal lives
2. Pain points and failures: Where today's tools break down
3. Mental models of trust and reliance: What makes people trust an AI assistant
4. Desire and delight: What would make the ideal AI assistant

AGGREGATED DATA FROM {total_interviews} INTERVIEWS:

BEHAVIORS ({len(aggregated_data['behaviors'])} items):
{json.dumps(aggregated_data['behaviors'], indent=2)}

PAIN POINTS ({len(aggregated_data['pain_points'])} items):
{json.dumps(aggregated_data['pain_points'], indent=2)}

TRUST FACTORS ({len(aggregated_data['trust_factors'])} items):
{json.dumps(aggregated_data['trust_factors'], indent=2)}

DESIRES ({len(aggregated_data['desires'])} items):
{json.dumps(aggregated_data['desires'], indent=2)}

TASK:
Create a comprehensive analysis report with the following sections:

1. OVERALL INSIGHTS (5-7 key insights that answer the research questions)
   - For each insight: provide title, how many interviews it applies to, description, and which quotes support it
   
2. PATTERNS AND THEMES
   - Identify recurring patterns across interviews
   - Group similar findings together
   
3. ALIGNMENT WITH RESEARCH QUESTIONS
   - Explicitly address each of the 4 research questions
   - Provide specific findings for each

Format your response as a detailed markdown report. Be specific and evidence-based.
"""

    print("🤖 Synthesizing final report with Ollama...")
    
    try:
        response = ollama.chat(
            model=OLLAMA_MODEL,
            messages=[{
                'role': 'user',
                'content': synthesis_prompt
            }],
            options={
                'temperature': 0.3,
            }
        )
        
        report = response['message']['content']
        print("✅ Synthesis complete!")
        return report
    
    except Exception as e:
        print(f"❌ Error during synthesis: {e}")
        return None


def create_quotes_section(quotes_data):
    """Create a formatted quotes section organized by topic."""
    quotes_by_topic = defaultdict(list)
    
    for quote_data in quotes_data:
        topic = quote_data.get('topic', 'General')
        quotes_by_topic[topic].append(quote_data)
    
    quotes_section = "\n## 💬 SUPPORTING QUOTES BY TOPIC\n\n"
    
    for topic, quotes in quotes_by_topic.items():
        quotes_section += f"\n### {topic}\n\n"
        for q in quotes[:10]:  # Limit to 10 quotes per topic
            participant = q.get('participant', 'Unknown')
            quote_text = q.get('quote', '')
            quotes_section += f'- "{quote_text}" — *{participant}*\n'
    
    return quotes_section


def main():
    """Main execution function."""
    print("🚀 Starting Report Synthesis")
    print()
    
    # Load all analyses
    analyses = load_all_analyses()
    
    if not analyses:
        print("❌ No analyses found to synthesize!")
        return
    
    # Aggregate findings
    print("📊 Aggregating findings...")
    aggregated = aggregate_findings(analyses)
    
    # Generate synthesis report
    synthesis_report = synthesize_with_ollama(aggregated, len(analyses))
    
    if not synthesis_report:
        print("❌ Failed to generate synthesis report!")
        return
    
    # Add unique insights section
    unique_section = "\n\n## 🌟 UNIQUE FINDINGS\n\n"
    for item in aggregated['unique_insights'][:15]:  # Limit to 15
        unique_section += f"**{item['participant']}**: {item['insight']}\n\n"
    
    # Add quotes section
    quotes_section = create_quotes_section(aggregated['quotes'])
    
    # Combine all sections
    full_report = f"""# AI ASSISTANT USER RESEARCH - ANALYSIS REPORT
Generated from {len(analyses)} interview transcripts

---

{synthesis_report}

{unique_section}

{quotes_section}

---

## 🔎 Let's Dive Deeper

What other questions do you have about these findings?

---
*Report generated using {OLLAMA_MODEL} via Ollama*
"""
    
    # Save report
    report_path = Path(OUTPUT_DIR) / "FINAL_ANALYSIS_REPORT.md"
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(full_report)
    
    print(f"\n✨ Final report saved to: {report_path}")
    print(f"\n📖 View the report at: {report_path}")


if __name__ == "__main__":
    main()
