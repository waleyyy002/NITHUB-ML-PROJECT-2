import torch
from scipy.special import softmax

from model_loader import tokenizer, model

labels = ["Negative", "Positive"]


def predict_sentiment(text: str):

    encoded_input = tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        padding=True,
        max_length=512
    )

    with torch.no_grad():
        output = model(**encoded_input)

    scores = output.logits[0].numpy()
    scores = softmax(scores)

    prediction = labels[scores.argmax()]

    confidence = float(scores.max())

    top3 = {
        labels[i]: float(scores[i])
        for i in range(len(labels))
    }

    return {
        "sentiment": prediction,
        "confidence": round(confidence, 4),
        "scores": top3
    }