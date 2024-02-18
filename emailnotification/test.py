from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)
email_pass = b'tsan uyja hvbg fydf'
db_pass = b'openproject-dev-password'

email_pass_token = f.encrypt(email_pass)
db_pass_token = f.encrypt(db_pass)

print(key.decode())
print(email_pass_token.decode())
print(db_pass_token.decode())