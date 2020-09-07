# CIS40: Chapter 4 Exercise 6: Nandhini Pandurangan
# This program prompts the user for their email address and returns the domain
# name of the email address

flag = True

# input validation
while flag:
    s = input("Please enter your email address: ")
    if "@" in s and "." in s:
        at = s.find("@")
        dot = s.find(".")
        email_host = s[at + 1:dot]
        print("The domain name of your email address is", email_host)

        flag = False
    else:
        print("\nPlease enter a valid email address\n")

'''
Output:

Please enter your email address: student@gmail.com
The domain name of your email address is gmail
----------------------------------------------------

Please enter your email address: hello World 

Please enter a valid email address

Please enter your email address: studentemail.com

Please enter a valid email address

Please enter your email address: studentemail@com

Please enter a valid email address

Please enter your email address: studentemail@yahoo.com
The domain name of your email address is yahoo

'''
