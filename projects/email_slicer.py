#Email Slicer used for detecting email and the domain with email id.


#user input
email = input("Enter your Email: ").strip()

#get username and domain
username = email[:email.index('@')]
domain = email[email.index('@') + 1:]

print(f"Your username is {username} & domain is {domain})

