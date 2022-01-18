from os import walk # https://docs.python.org/3/library/os.html#os.walk
from os.path import join # https://docs.python.org/3/library/os.path.html#os.path.join
import pandas as pd

def email_body_extraction(path):
	for root, dirs, files in walk(path):
		for f_name in files:
			f_path = join(root, f_name)
			f_stream = open(f_path, 'r', encoding='latin-1')

			# extract body from email
			f_stream.seek(0)
			is_body = False
			body_lines = []
			for line in f_stream:
				if is_body:
					body_lines.append(line)
				elif line == '\n':
					is_body = True
			f_stream.close()
			email_body = '\n'.join(body_lines)

			yield f_name, email_body

def get_emails_df(path, classification):
	"""
		Extract the body content from all the email files contained in the directory. Returns a DataFrame with the content extracted and the category.

		Args:
			path: The path to the directory where the email files are stored.
			classification: The category of the emails being returned. [SPAM or HAM (nonspam)].

	"""

	rows = []
	row_names = []

	for f_name, email_body in email_body_extraction(path):
		rows.append({ 'MESSAGE': email_body, 'CATEGORY': classification })
		row_names.append(f_name)

	return pd.DataFrame(rows, index=row_names)