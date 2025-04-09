import pandas as pd
import pickle
from sentence_transformers import SentenceTransformer

df = pd.read_csv("app/data/shl_catalog.csv")
model = SentenceTransformer("all-MiniLM-L6-v2")

text_to_embed = df["Description"].tolist()
embeddings = model.encode(text_to_embed, convert_to_tensor=True)

with open("app/embeddings/index.pkl", "wb") as f:
    pickle.dump(embeddings, f)
