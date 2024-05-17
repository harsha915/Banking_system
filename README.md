# project1
AHV BANKING APPLICATION USE CASE

AHV Bank Application Use Case (with Function References)
1.	Application Initialization:
●	Upon launch, the application displays an ASCII art banner for "AHV Bank".
●	Function: bannerPrinting from banner_printing.py

2.	Main Menu Options:
●	The user is presented with a menu offering the following choices:
●	Register (Account Creation)
●	Login (Access Existing Account)
●	Forgot Password (Recover Account)
●	Exit (Terminate the Application)

3.	Account Registration:
●	If the user chooses to register:
●	They are prompted to provide personal details.
●	Function: accountCreation from user_service.py
●	The application performs validation on each input.
●	Functions: Various validation functions from validations.py (e.g., emailValidation,       mobileNumValidation)
●	The user's details are saved in the database.
●	Function: insert_data from db_operations.py
●	The user receives an email with an OTP for verification.
●	Function: mailOtpVerification from mail_operations.py
4.	Login to Existing Account:
●	If the user chooses to login:
●	They provide their registered email and are authenticated.
●	Function: login (within app.py)

4.	Login to Existing Account:
●	If the user chooses to login:
●	They provide their registered email and are authenticated.
●	Function: login (within app.py)

5.	Banking Services:
●	Upon successful login, users can:
●	Display Balance: View their current account balance.
●	Function: displayBalance from banking_service.py
●	Deposit Money: Add funds to their account.
●	Function: depositMoney from banking_service.py
●	Withdraw Money: Deduct funds from their account.
●	Function: withdrawlMoney from banking_service.py
●	Transfer Money: Send funds to another user's account.
●	Function: transferMoney from banking_service.py
●	Print Transaction History: View past transactions.
●	Function: transactionHistory from banking_service.py
●	Logout: Exit the banking services menu and return to the main menu.

6.	Forgot Password:
●	If the user forgets their password:
●	They can request a password reset.
●	Function: Assumed to be within app.py or another service module, as the specific function was not provided in the reviewed content.
●	An OTP is sent to their email for verification.
●	Function: mailOtpVerification from mail_operations.py
7.	Security Measures:
●	Passwords are hashed using a salt.
●	Function: hash_password_with_salt from user_security.py
●	The application tracks login attempts.
●	Function: reset_variable_after_30_seconds from user_security.py
●	OTPs are used for email verification.
●	Function: mailOtpVerification from mail_operations.py

7.	Security Measures:
●	Passwords are hashed using a salt.
●	Function: hash_password_with_salt from user_security.py
●	The application tracks login attempts.
●	Function: reset_variable_after_30_seconds from user_security.py
●	OTPs are used for email verification.
●	Function: mailOtpVerification from mail_operations.py

8.	Exit Application:
●	If the user chooses to exit, an exit banner is displayed.
●	Function: exit_banner_printing from banner_printing.py
Tree Structure of the AHV Bank Application:
AHV Bank Application
|-- app.py
Main entry point to application
|-- banking_service.py
Display balance, deposit, withdraw, transfer money, transaction history
|-- banner_printing.py
Print entry, exit banner
|-- constants.py
|-- db_operations.py
Insert, fetch, fetch column data, update, delete
|-- mail_operations.py
Mail verification
|-- user_security.py hashing
|-- user_service.py
Create account, login, forgot password
|-- validations.py
Validate mobile number, email id, dob, gender
|-- Banner.txt
|-- exit_banner.txt


Future Update Ideas:
1.	Create a option to delete a user account
2.	Create option to update user details (email, dob, mobile number and more)
3.	Transaction History can be printed based on Timestamp interval
4.	Transaction History can be sent through mail
5.	Write a functionality to unlock blocked accounts after certain time
6.	Create another Super Admin account, who can control everything and everyone
 
Modules Used:
1.	import time
2.	import hashlib
3.	import smtplib
4.	from random import randint
5.	import mysql.connector
6.	import re

For Banner use : https://devops.datenkollektiv.de/banner.txt/index.html
![image](https://github.com/harsha915/project1/assets/109910128/e601d15b-46d2-4e63-b95b-098d08d799fa)
