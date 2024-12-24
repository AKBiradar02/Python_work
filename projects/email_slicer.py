#Email Slicer used for detecting email and the domain with email 
#email slicer
#get user email id from user input

email = input("Enter your email:").strip()
#get user name
user_name = email[:email.index("@")]
#get domain name
domain_name = email[email.index("@")+1:]
#get formatted output
output = "Your user name is '{}' and your domain name is '{}'".format(user_name,domain_name)
#print output
print(output)
