import pandas as pd

def gen_sparse_df(df, indexed_words, labels):
	"""
	Generate the sparse matrix from df argument and return as DataFrame.
   
	Args:
		df: The full matrix. A DataFrame containing words in the columns and a DOC_ID as index. (X_train or X_test dataset)
		indexed_words: Index of words  ordered by word_id
		labels: Category as a series (y_train or y_test)
	"""

	num_row = df.shape[0]
	num_col = df.shape[1]
	word_set = set(indexed_words)
	dict_list = []

	for i in range (num_row):
		for j in range (num_col):
			word = df.iat[i, j]
			if word in word_set:
				doc_id = df.index[i]
				word_id = indexed_words.get_loc(word)
				category = labels.at[doc_id]

				# store data
				item = {'LABEL': category, 'DOC_ID': doc_id, 'OCCURENCE': 1, 'WORD_ID': word_id}
				dict_list.append(item)

	return pd.DataFrame(dict_list)
