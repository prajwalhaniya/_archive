'''
Content based filtering

- Data collection
- Feature representation
- User profile creation
- Similarity calculation
- Recommendation generation
'''
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

books = pd.DataFrame({
    'title': ['Book A', 'Book B', 'Book C', 'Book D'],
    'description': ['A thrilling mystery', 'An insightful science fiction', 'A romantic novel', 'A non-fiction']
})
print(books)

tfidf = TfidfVectorizer()
tfidf_matrix = tfidf.fit_transform(books['description'])

liked_books = ['Book A', 'Book C']
user_profile = tfidf.transform(books[books['title'].isin(liked_books)]['description'])

cosine_sim = cosine_similarity(user_profile, tfidf_matrix)

recommendations = list(enumerate(cosine_sim[0]))
recommendations = sorted(recommendations, key=lambda x: x[1], reverse=True)

recommended_indices = [i[0] for i in recommendations if books['title'][i[0]] not in liked_books]
top_recommendations = books['title'].iloc[recommended_indices].head(2)

print("Recommended Books:", top_recommendations.tolist())
