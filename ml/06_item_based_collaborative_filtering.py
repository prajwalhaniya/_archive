import pandas as pd
import numpy as np

# Sample user-item ratings DataFrame
ratings = pd.DataFrame({
    'User': ['User1', 'User1', 'User2', 'User2'],
    'Movie': ['A', 'B', 'A', 'C'],
    'Rating': [5, 3, 4, 2]
})

user_item_matrix = ratings.pivot(index='User', columns='Movie', values='Rating').fillna(0)

from sklearn.metrics.pairwise import cosine_similarity

item_similarity = cosine_similarity(user_item_matrix.T)
item_similarity_df = pd.DataFrame(item_similarity, index=user_item_matrix.columns, columns=user_item_matrix.columns)

def recommend_items(user, num_recommendations=2):
    user_ratings = user_item_matrix.loc[user]
    similar_scores = item_similarity_df.dot(user_ratings)
    similar_scores = similar_scores[user_ratings == 0] # Only consider unrated items
    return similar_scores.nlargest(num_recommendations)

print(recommend_items('User1'))