#BankingApp
A simple GUI-based banking application built using Python and Tkinter, allowing users to create accounts, login, deposit and withdraw money, view transaction history, and change passwords.

##Table of Contents
1.Project Description
2.Features
3.Prerequisites
4.Installation
5.Usage
6.Screenshots
7.File Structure

##1.Project Description
BankingApp provides basic banking functionalities through a graphical user interface (GUI) built with Python's Tkinter library. It simulates account creation, user authentication, fund deposits and withdrawals, transaction history tracking, and password management.

The project is ideal for understanding the structure of a simple banking application, focusing on fundamental GUI elements and Python data handling. The app serves as a foundation for beginners to explore user interface development and logic handling in Python.

##2.Features
Account Creation: New users can create an account with a username and password.
User Login: Existing users can log in securely using their credentials.
Deposit & Withdraw: Logged-in users can deposit and withdraw funds, with each transaction updating the displayed balance.
Transaction History: Track deposit and withdrawal transactions.
Password Change: Users can change their account password.
Logout: Users can securely log out of the system.

##3.Prerequisites
Python 3.x
Tkinter library (usually included with Python by default)

##4.Installation
Clone the Repository:
git clone https://github.com/your-username/BankingApp.git
cd BankingApp
Install Dependencies: No additional dependencies are needed, as Tkinter is included with Python by default.

Run the Application:
python banking_app.py

##5.Usage
A.Creating an Account:

Enter a unique username and password.
Click "Create Account".
B.Logging In:

Enter your username and password.
C.Click "Login".
Performing Transactions:

After logging in, you can deposit or withdraw money, view your transaction history, and change your password.
D.Logging Out:

E.Click "Logout" to end your session.

##6.Screenshots
Login Screen
![Login Screen](Banking-app\images\Screenshot 2024-11-14 122611.png)


Banking Actions Screen
![Banking Actions Screen](Banking-app\images\Screenshot 2024-11-14 122726.png)



##7.File Structure

BankingApp/
├── banking_app.py     # Main application file
├── README.md          # Project documentation
└── images/            # Folder to store screenshots
    ├── login_screen.png
    ├── banking_actions.png
    └── transaction_history.png
