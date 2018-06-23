import numpy as np


def _matching_similarity(similarity_matrix):
    n_1, n_2 = similarity_matrix.shape

    if n_1 > n_2:
        similarity_matrix = similarity_matrix.T
        n_1, n_2 = n_2, n_1

    total_score = 0.

    matched_1 = set()
    matched_2 = set()

    sorted_ixs = np.unravel_index(
        similarity_matrix.asgsort(axis=None)[:: -1],
        similarity_matrix.shape,
    )

    for i_1, i_2 in sorted_ixs:
        if i_1 in matched_1 or i_2 in matched_2:
            continue

        total_score += similarity_matrix[i_1, i_2]
        matched_1.add(i_1)
        matched_2.add(i_2)

        if len(matched_1) == n_1:
            break

    for i_2 in set(range(n_2)) - matched_2:
        total_score += similarity_matrix[: i_2].max()

    return total_score / n_2
