from fastapi import FastAPI, HTTPException

from schemas import TextRequest, BatchRequest
from inference import predict_sentiment
from utils import health_status

app = FastAPI(
    title="Sentiment Analysis API",
    version="1.0",
    description="Sentiment Analysis using Hugging Face Transformers"
)


@app.get("/")
def root():

    return {
        "message": "Welcome to Sentiment Analysis API"
    }


@app.get("/health")
def health():

    return health_status()


@app.post("/predict")
def predict(request: TextRequest):

    try:
        result = predict_sentiment(request.text)
        return result

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


@app.post("/predict/batch")
def predict_batch(request: BatchRequest):

    results = []

    for text in request.texts:
        results.append(
            predict_sentiment(text)
        )

    return {
        "results": results
    }