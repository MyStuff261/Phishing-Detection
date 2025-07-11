from transformers import pipeline
import torch

device = "cuda:0" if torch.cuda.is_available() else "cpu"

def analyze(text):
    classifier = pipeline(
        model="distilbert/distilbert-base-uncased-finetuned-sst-2-english",
        task="sentiment-analysis",
        device=0 if device == "cuda:0" else -1
    )
    res = classifier(text)
    label = f"Label: {res[0]['label']}, Score: {res[0]['score']:.2f}"
    print(label)
    return label

analyze('FUCK YOU')
