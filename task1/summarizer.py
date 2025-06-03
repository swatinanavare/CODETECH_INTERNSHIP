from transformers import pipeline

# Load summarization pipeline with explicit model name
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

# Sample long text
text = """
The rise of artificial intelligence (AI) has transformed various industries across the globe.
From healthcare and finance to transportation and education, AI is making systems smarter, faster, and more efficient.
It has the potential to revolutionize how humans interact with machines and how decisions are made in complex environments.
However, ethical concerns, data privacy issues, and the fear of job displacement remain critical challenges that must be addressed.
"""

# Run summarization
summary = summarizer(text, max_length=60, min_length=20, do_sample=False)

# Print summary
print("\nSummary:\n", summary[0]['summary_text'])

