import numpy as np

def cosine_similarity(A, B):
    A = np.array(A)
    B = np.array(B)

    dot_product = np.dot(A, B)

    magnitude_A = np.linalg.norm(A)
    magnitude_B = np.linalg.norm(B)

    if magnitude_A == 0 or magnitude_B == 0:
        return 0.0
    return dot_product / (magnitude_A * magnitude_B)

vec1 = [1, 2, 3]
vec2 = [8, 5, 6]
similarity_score = cosine_similarity(vec1, vec2)
print(f"Cosine Similarity: {similarity_score}")