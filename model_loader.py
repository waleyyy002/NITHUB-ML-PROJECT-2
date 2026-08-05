import os
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

MODEL_NAME = "cardiffnlp/twitter-roberta-base-sentiment-latest"
LOCAL_MODEL_DIR = "twitter-roberta-base-sentiment-latest"
HF_TOKEN = os.environ.get("HF_TOKEN")

use_local = os.path.isdir(LOCAL_MODEL_DIR)
model_source = LOCAL_MODEL_DIR if use_local else MODEL_NAME

# Limit CPU threads to reduce memory usage on constrained hosts
torch.set_num_threads(1)
torch.set_num_interop_threads(1)

tokenizer_kwargs = {
    "local_files_only": use_local,
}

model_kwargs = {
    "local_files_only": use_local,
    "low_cpu_mem_usage": True,
}

if not use_local and HF_TOKEN:
    tokenizer_kwargs["use_auth_token"] = HF_TOKEN
    model_kwargs["use_auth_token"] = HF_TOKEN

# CPU-backed float16 may not be fully supported on all hosts, so we use default dtype
# and low_cpu_mem_usage to reduce the model footprint.

tokenizer = AutoTokenizer.from_pretrained(model_source, **tokenizer_kwargs)
model = AutoModelForSequenceClassification.from_pretrained(model_source, **model_kwargs)
