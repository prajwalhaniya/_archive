from sklearn.feature_extraction.text import TfidfVectorizer

documents = [
    "The dog sat on the log.",
    "Cats and dogs are great pets."
]

vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(documents)

print(vectorizer.vocabulary_)
