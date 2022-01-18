import pandas as pd
import numpy as np

def gen_full_matrix(sparse_matrix, num_words, doc_idx=0, word_idx=1, cat_idx=2, freq_idx=3):
	"""
	Generate a full matrix out of a sparse matrix and return it as a DataFrame.
	Args:
		sparse_matrix : The sparse matrix from which the full matrix will be generated. (numpy array).
		num_words : The total number of words, it is, the size of the vocabulary.
		doc_idx : Position of the document id in the sparse matrix.
		word_idx : Position of the word id in the sparse matrix.
		cat_idx : Position of the category label in the sparse matrix.
		freq_idx : Posisition of occurences of word in the sparse matrix.
	"""

	col_names = ['DOC_ID'] + ['CATEGORY'] + list(range(0, num_words))
	index_names = pd.unique(sparse_matrix[:, 0]) # all rows, col 0
	full_matrix = pd.DataFrame(index=index_names, columns=col_names)
	full_matrix.fillna(value=0, inplace=True)

	for i in range(sparse_matrix.shape[0]):
		doc_id = sparse_matrix[i][doc_idx]
		word_id = sparse_matrix[i][word_idx]
		label = sparse_matrix[i][cat_idx]
		occur = sparse_matrix[i][freq_idx]

		full_matrix.at[doc_id, 'DOC_ID'] = doc_id
		full_matrix.at[doc_id, 'CATEGORY'] = label
		full_matrix.at[doc_id, word_id] = occur

	full_matrix.set_index('DOC_ID', inplace=True)

	return full_matrix