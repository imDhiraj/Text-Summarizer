from transformers import pipeline

summarizer_pipeline = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(text: str) -> str:
    # Adjust max_length and min_length to get a richer summary
    summary = summarizer_pipeline(
        text, 
        max_length=200,   # Try 200–300 for longer summaries
        min_length=80,    # Try 80+ for more meaningful content
        do_sample=False
    )
    return summary[0]['summary_text']
