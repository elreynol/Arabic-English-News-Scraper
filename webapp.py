!pip install -q gradio newspaper3k

import newspaper

# instead of importing transformers directly, just use them through gradio
import gradio as gr
from gradio.mix import Series

# Translate it to English
translator = gr.Interface.load("Helsinki-NLP/opus-mt-ar-en", src="huggingface")
# Summarize it
summarizer = gr.Interface.load("facebook/bart-large-cnn", src="huggingface")
translator.launch()
