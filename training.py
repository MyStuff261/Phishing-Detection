import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib

df = pd.read_csv('phishing_site_urls.csv')

bad_domains = df[df["Label"] == "bad"]["URL"].tolist()
good_domains = df[df["Label"] == "good"]["URL"].tolist()

all_domains = bad_domains + good_domains
vectorizer = TfidfVectorizer(analyzer='char_wb', ngram_range=(3, 5))
vectorizer.fit(all_domains)

joblib.dump(vectorizer, 'vectorizer.pkl')