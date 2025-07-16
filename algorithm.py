import pandas as pd
import joblib
from sklearn.metrics.pairwise import cosine_similarity
import time

print("Loading model and data...")

df = pd.read_csv('phishing_site_urls.csv')

good_domains = df[df["Label"] == "good"]["URL"].tolist()

start = time.perf_counter()
vectorizer = joblib.load('vectorizer.pkl')
good_vectors = vectorizer.transform(good_domains)

print("Model and data loaded.")

end = time.perf_counter()
print(f"Time taken: {end - start:.4f} seconds")

def classify_domain(domain):
    vec = vectorizer.transform([domain])
    good_sim = cosine_similarity(vec, good_vectors).max()
    print(f"Similarity to legit:    {good_sim:.4f}")
    
    if good_sim > 0.5:
        return "Legit"
    else:
        return "Phishing"