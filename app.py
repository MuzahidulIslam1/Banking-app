import tkinter as tk
from tkinter import messagebox, simpledialog

class BankingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Banking System")
        self.root.geometry("400x500")
        self.root.configure(bg="#e0f7fa")

        # Initialize account details
        self.accounts = {}
        self.current_user = None
        self.transaction_history = []

        # Create UI components
        self.create_widgets()

    def create_widgets(self):
        # Title label
        title_label = tk.Label(self.root, text="Welcome to the Banking System", font=("Arial", 18), bg="#e0f7fa")
        title_label.pack(pady=10)

        # Frame for login and account management
        self.login_frame = tk.Frame(self.root, bg="#e0f7fa")
        self.login_frame.pack(pady=20)

        # Username and Password Entry
        self.username_label = tk.Label(self.login_frame, text="Username:", bg="#e0f7fa")
        self.username_label.grid(row=0, column=0, padx=5, pady=5)
        
        self.username_entry = tk.Entry(self.login_frame)
        self.username_entry.grid(row=0, column=1, padx=5, pady=5)

        self.password_label = tk.Label(self.login_frame, text="Password:", bg="#e0f7fa")
        self.password_label.grid(row=1, column=0, padx=5, pady=5)

        self.password_entry = tk.Entry(self.login_frame, show='*')
        self.password_entry.grid(row=1, column=1, padx=5, pady=5)

        # Buttons for account actions
        self.create_account_button = tk.Button(self.login_frame, text="Create Account", command=self.create_account)
        self.create_account_button.grid(row=2, columnspan=2, pady=(10, 5))

        self.login_button = tk.Button(self.login_frame, text="Login", command=self.login)
        self.login_button.grid(row=3, columnspan=2)

    def create_account(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username in self.accounts:
            messagebox.showerror("Error", "Account already exists!")
            return
        
        if username and password:
            self.accounts[username] = {"password": password, "balance": 0}
            messagebox.showinfo("Success", "Account created successfully!")
            self.username_entry.delete(0, tk.END)
            self.password_entry.delete(0, tk.END)
            return
        
        messagebox.showerror("Error", "Please enter a username and password.")

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username in self.accounts and self.accounts[username]["password"] == password:
            messagebox.showinfo("Success", "Login successful!")
            self.current_user = username
            self.show_banking_actions()
            return
        
        messagebox.showerror("Error", "Invalid username or password.")

    def show_banking_actions(self):
        # Clear previous widgets
        for widget in self.root.winfo_children():
            widget.destroy()

        # Create new frame for banking actions
        action_frame = tk.Frame(self.root, bg="#e0f7fa")
        
        # Title label for banking actions
        actions_title_label = tk.Label(action_frame, text=f"Welcome {self.current_user}!", font=("Arial", 18), bg="#e0f7fa")
        actions_title_label.pack(pady=(10, 20))

        # Display current balance
        self.balance_label = tk.Label(action_frame,
                                       text=f"Current Balance: ${self.accounts[self.current_user]['balance']:.2f}",
                                       font=("Arial", 14), bg="#e0f7fa")
        
        self.balance_label.pack(pady=(10, 20))

        # Deposit button
        deposit_button = tk.Button(action_frame, text="Deposit", command=self.deposit)
        
         # Withdraw button (corrected indentation)
        withdraw_button = tk.Button(action_frame, text="Withdraw", command=self.withdraw)
        
         # View Transaction History button
        history_button = tk.Button(action_frame, text="View Transaction History", command=self.view_history)

         # Change Password button
        change_password_button = tk.Button(action_frame, text="Change Password", command=self.change_password)

         # Logout button
        logout_button = tk.Button(action_frame, text="Logout", command=self.logout)

        deposit_button.pack(pady=5)
        withdraw_button.pack(pady=5)  # Ensure this line has correct indentation
        history_button.pack(pady=5)
        change_password_button.pack(pady=5)
         
         # Pack logout button last for better UI flow
        logout_button.pack(pady=(20))

        action_frame.pack(pady=(20))

    def deposit(self):
        amount = simpledialog.askfloat("Input", "Enter amount to deposit:")
         
        if amount is None or amount <= 0:
            messagebox.showerror("Error", "Invalid amount.")
            return
         
        if not self.current_user:
            messagebox.showerror("Error", "Please log in first.")
            return

         # Update balance and transaction history
        account_info = self.accounts[self.current_user]
        account_info["balance"] += amount

         # Update the displayed balance
        self.balance_label.config(text=f"Current Balance: ${account_info['balance']:.2f}")

        messagebox.showinfo("Success", f"Deposited: ${amount:.2f}")
         
         # Add to transaction history
        self.transaction_history.append(f"Deposited: ${amount:.2f}")

    def withdraw(self):
        amount = simpledialog.askfloat("Input", "Enter amount to withdraw:")
         
        if amount is None or amount <= 0:
            messagebox.showerror("Error", "Invalid amount.")
            return
         
        if not self.current_user:
            messagebox.showerror("Error", "Please log in first.")
            return

        account_info = self.accounts[self.current_user]
         
        if amount > account_info["balance"]:
            messagebox.showerror("Error", "Insufficient funds!")
            return
         
        account_info["balance"] -= amount

         # Update the displayed balance
        self.balance_label.config(text=f"Current Balance: ${account_info['balance']:.2f}")

        messagebox.showinfo("Success", f"Withdrew: ${amount:.2f}")
         
         # Add to transaction history
        self.transaction_history.append(f"Withdrew: ${amount:.2f}")

    def view_history(self):
        if not self.transaction_history:
            messagebox.showinfo("Transaction History", "No transactions yet.")
            return
         
        history_str = "\n".join(self.transaction_history)
         
        history_window = tk.Toplevel(self.root)
         
        history_window.title("Transaction History")
         
        history_label = tk.Label(history_window, text=history_str, justify=tk.LEFT)
         
        history_label.pack(padx=10, pady=10)

    def change_password(self):
        new_password = simpledialog.askstring("Change Password", "Enter new password:", show='*')
         
        if new_password:
            account_info = self.accounts[self.current_user]
            account_info["password"] = new_password
            messagebox.showinfo("Success", "Password changed successfully!")

    def logout(self):
        messagebox.showinfo("Logout", "You have been logged out.")
        self.current_user = None
        for widget in self.root.winfo_children():
            widget.destroy()
        self.create_widgets()

if __name__ == "__main__":
    root = tk.Tk()
    app = BankingApp(root)
    root.mainloop()