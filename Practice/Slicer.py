# getting user email address
email = input("What is your email address? ").strip()

# slice user name
user = email[:email.index("@")]

# slice domain name
domain = email[email.index("@") + 1:]

# getting the format
output = "Your user name is {} and your domain name is {}".format(user, domain)

# output
print(output)



