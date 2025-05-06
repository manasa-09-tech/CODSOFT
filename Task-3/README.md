#Task-3  Password Generator

##description
   Password generator is a useful tool that generates strong and random password for users.
   This project aims to create a password generator application using python
   It allows the user to specify the length and complexity of the password

## This repository contains two python script that generate strong random passwords
     1.password.py
             > Generates multiple passwords of user-defined length using the string and random modules
          Features
              > Uses predefined character sets(ascii_letters,digits,punctuation)
              > Asks for:
                    - Password length
                    - Number of passwords
              > Prints each generated password

       2.password1.py
               > A minimal version without using string methods. characters are collected manually using ASCII values from chr()
           Features
                > no use of string module
                > Bulids the character set using chr(i) from ASCII 33 to 122
                > uses random.choice() to pick characters
## How to run
    - python password.py
    - python password1.py
    - Make sure python is installed
