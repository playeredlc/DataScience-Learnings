FILE_PATH = 'test_email.txt'

file = open(FILE_PATH, 'r', encoding='utf-8')
full_email = file.read()
print('FULL EMAIL:\n', type(full_email), '\n', full_email, '\n')

# extracting email body
file.seek(0) # change the stream position back to the start

is_body = False
body_lines = []

for line in file:
	if is_body:
		body_lines.append(line)
	elif line == '\n':
		# the first blank line in the email separates the header from the body
		is_body = True

print('FOR OUTPUT:\n', body_lines, '\n')
email_body = '\n'.join(body_lines)
print('CLEAN EMAIL BODY:\n', email_body)

file.close()
