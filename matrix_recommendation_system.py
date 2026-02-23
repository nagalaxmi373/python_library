import numpy as np

# User affinity matrix (3 users × 2 genres)
users = np.array([
    [5, 2],   # User 1
    [3, 4],   # User 2
    [1, 5]    # User 3
])

# Song profiles (3 songs × 2 genres)
songs = np.array([
    [4, 1],
    [2, 5],
    [3, 3]
])

# Transpose songs to align for multiplication
songs_T = songs.T

# Dot product to get preference matrix
preference_matrix = users @ songs_T

print("Preference Matrix:")
print(preference_matrix)

# Vectorized: Double high-score songs (score > 20)
preference_matrix[preference_matrix > 20] *= 2

print("\nAfter Doubling High Scores:")
print(preference_matrix)
