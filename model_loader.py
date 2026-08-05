import os
from transformers import AutoTokenizer, AutoModelForSequenceClassification

MODEL_NAME = "cardiffnlp/twitter-roberta-base-sentiment-latest"
LOCAL_MODEL_DIR = "twitter-roberta-base-sentiment-latest"
HF_TOKEN = os.environ.get("HF_TOKEN")

use_local = os.path.isdir(LOCAL_MODEL_DIR)
model_source = LOCAL_MODEL_DIR if use_local else MODEL_NAME

load_kwargs = {
    "local_files_only": use_local,
    "low_cpu_mem_usage": True,
}

if not use_local and HF_TOKEN:
    load_kwargs["use_auth_token"] = HF_TOKEN

tokenizer = AutoTokenizer.from_pretrained(model_source, **load_kwargs)
model = AutoModelForSequenceClassification.from_pretrained(model_source, **load_kwargs)
