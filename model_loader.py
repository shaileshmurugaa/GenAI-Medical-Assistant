# model_loader.py
import os
import time
from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline, AutoModel
from config import MODEL_DIR

class Models:
    def __init__(self, model_name_or_path="dmis-lab/biobert-v1.1"):
        # set local paths
        self.model_name_or_path = model_name_or_path
        self.ner_pipeline = None
        self.embedding_model = None
        self.tokenizer = None
        self.load_models()

    def load_models(self):
        # load tokenizer and NER model (try local first)
        print("Loading tokenizer and NER model (may take a while the first time)...")
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name_or_path, cache_dir=MODEL_DIR)
        try:
            ner_model = AutoModelForTokenClassification.from_pretrained(self.model_name_or_path, cache_dir=MODEL_DIR)
            # fallback: if token-class model isn't available, skip NER and use basic heuristics
            self.ner_pipeline = pipeline("ner", model=ner_model, tokenizer=self.tokenizer, aggregation_strategy="simple")
        except Exception as e:
            print("NER model not available for chosen model:", e)
            self.ner_pipeline = None

        # Use an embedding model (a small sentence-transformers model) for similarity if available
        # Use sentence-transformers like 'sentence-transformers/all-MiniLM-L6-v2' if offline downloaded
        try:
            from sentence_transformers import SentenceTransformer
            self.embedding_model = SentenceTransformer('all-MiniLM-L6-v2', cache_folder=MODEL_DIR)
        except Exception as e:
            print("SentenceTransformer not available, embeddings won't be available", e)
            self.embedding_model = None

models = Models()
