from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()


def predict_sentiment(text: str):
    scores = analyzer.polarity_scores(text)
    compound = scores["compound"]

    if compound >= 0.05:
        prediction = "Positive"
    elif compound <= -0.05:
        prediction = "Negative"
    else:
        prediction = "Neutral"

    return {
        "sentiment": prediction,
        "confidence": round(abs(compound), 4),
        "scores": {
            "negative": scores["neg"],
            "neutral": scores["neu"],
            "positive": scores["pos"],
            "compound": compound,
        },
    }
