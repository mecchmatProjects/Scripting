import secrets

token = secrets.token_urlsafe() # store in database for further recognition
passwordResetUrl = 'https://website.com/passwordReset=' + token
print(token)
# output: QJlwR4G8EkW-3VTZjvrGJzsRvcnG4_4b_B4aMe2NLjc
print(passwordResetUrl)
# output: https://website.com/passwordReset=QJlwR4G8EkW-3VTZjvrGJzsRvcnG4_4b_B4aMe2NLjc