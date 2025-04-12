# SABR: Systematic Assessment of Book Reading

## Project Overview

SABR (Systematic Assessment of Book Reading) is an AI-powered research coding system that automates qualitative data analysis in educational research. This innovative tool transforms what traditionally takes researchers days into a task that can be completed in minutes, achieving up to 94.8% agreement with expert human coders on certain coding schemes.

## Problem & Solution

### The Challenge
Educational researchers analyzing classroom discourse typically spend weeks manually coding transcripts to identify specific linguistic patterns and thematic elements. This labor-intensive process requires specialized training and creates bottlenecks in research pipelines.

### The Solution
I developed a custom LLM pipeline leveraging GPT-4 with chain-of-thought prompting to automatically analyze and code educational transcripts according to complex linguistic frameworks. The system interprets natural language, recognizes abstract patterns in discourse, and applies standardized coding schemes with remarkable accuracy.

## Technical Implementation

### Architecture
- **Core Engine**: Python-based AI processing pipeline utilizing OpenAI's GPT-4 API
- **User Interface**: Streamlit web application for researcher accessibility
- **Prompt Engineering**: Custom chain-of-thought prompting system that guides LLM reasoning through multiple structured steps
- **Data Processing**: Handles CSV/Excel inputs containing classroom transcripts and produces coded outputs with explanations

### Key Features
- **Multi-scheme Coding**: Supports 10+ linguistic and thematic coding schemes including Sequence/Temporal, Compare/Contrast, Cognition, Desires/Preferences, etc.
- **Explainability**: Provides detailed reasoning for each code assignment, enabling rapid verification by researchers
- **Batch Processing**: Analyzes hundreds of utterances in minutes, with costs averaging ~$0.05 per utterance
- **Validation Tools**: Built-in agreement calculation comparing AI vs. human coding with detailed metrics

## Results & Validation

Through rigorous testing against expert human coders, SABR demonstrated impressive agreement rates:
- 94.8% agreement on the official SABR practice transcript
- 92.8% agreement on a 10% random sample of TESOL SABR codes
- 87.1% agreement on extension question coding

Highly consistent internal reliability (intra-rater) of 80-97% across multiple coding runs, demonstrating the system's stability and reproducibility.

## Impact & Innovation

This system represents a significant advancement in qualitative research methodology by:
1. Reducing coding time from days to minutes while maintaining research-grade accuracy
2. Providing transparent explanations for coding decisions, allowing researchers to understand and verify AI reasoning
3. Creating a modular architecture that can be extended to new coding schemes with minimal adjustment
4. Democratizing access to sophisticated coding methodologies that typically require extensive training

The project demonstrates how AI can augment qualitative research methods, making complex analysis more accessible and efficient without sacrificing accuracy or interpretability.