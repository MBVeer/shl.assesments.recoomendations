import pandas as pd
import pickle
from sentence_transformers import SentenceTransformer, util

catalog = pd.read_csv("app/data/shl_catalog.csv")
with open("app/embeddings/index.pkl", "rb") as f:
    embeddings = pickle.load(f)

model = SentenceTransformer("all-MiniLM-L6-v2")

def recommend_assessments(query, top_k=10):
    query_emb = model.encode(query, convert_to_tensor=True)
    scores = util.cos_sim(query_emb, embeddings)[0]
    top_k_indices = scores.argsort(descending=True)[:top_k]

    results = []
    for idx in top_k_indices:
        row = catalog.iloc[idx.item()]
        results.append({
            "Assessment Name": row["Assessment Name"],
            "Duration": row["Duration"],
            "Test Type": row["Type"],
            "Remote": row["Remote Support"],
            "Adaptive": row["Adaptive Support"],
            "Link": row["URL"]
        })

    return pd.DataFrame(results)
