email = input("Email: ").strip()
username = email[:email.index("@")]
domain = email[email.index("@")+1:]
print(f"Username : {username} \n Domain : {domain}")
