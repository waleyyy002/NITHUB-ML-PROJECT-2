# NITHUB-ML-PROJECT-2

SENTIMENT ANALYSIS

This repository includes a modern frontend served by FastAPI at `/app`.

## Run Locally

```bash
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8000
```

Open the UI at:

```text
http://127.0.0.1:8000/app
```

## API Endpoints

- `GET /health`
- `POST /predict` — body: `{ "text": "your text" }`
- `POST /predict/batch` — body: `{ "texts": ["text1", "text2"] }`

## Frontend

The UI is served at `/app` and uses `/predict` to make sentiment predictions.
