"""
Author: Max Smith
Date written: 09/29/24
Assignment: FP
Short Desc: LiftTracker application for calculating lifting weights based on 1RM and percentage.
"""

import tkinter as tk
from tkinter import messagebox

class LiftTracker:
    def __init__(self, root):
        """
        Initializes the LiftTracker application.
        Sets up the main window and initializes the user interface components.
        """
        self.root = root  # Reference to the main application window
        self.root.title("LiftTracker")  # Title of the application
        
        # User input fields
        self.create_widgets()  # Calls the function to create the UI elements
        
        # Initialize history log
        self.history = []  # List to keep track of past calculations

    def create_widgets(self):
        """
        Creates and arranges the UI components in the main window.
        Includes input fields, result display, history log, and exit button.
        """
        # Title Bar
        title_label = tk.Label(self.root, text="LiftTracker", font=("Helvetica", 16))  # Title label
        title_label.pack(pady=10)  # Adds padding around the label

        # User Input Section
        input_frame = tk.Frame(self.root)  # Frame to hold input fields
        input_frame.pack(pady=10)  # Adds padding around the frame

        tk.Label(input_frame, text="1RM (One-Rep Max):").grid(row=0, column=0)  # Label for 1RM input
        self.one_rep_max_entry = tk.Entry(input_frame)  # Entry field for 1RM
        self.one_rep_max_entry.grid(row=0, column=1)  # Places the entry field in the grid

        tk.Label(input_frame, text="Percentage (50%, 75%, 90%):").grid(row=1, column=0)  # Label for percentage input
        self.percentage_entry = tk.Entry(input_frame)  # Entry field for percentage
        self.percentage_entry.grid(row=1, column=1)  # Places the entry field in the grid

        # Button to trigger weight calculation
        calculate_button = tk.Button(input_frame, text="Calculate", command=self.calculate_weights)  # Button with callback
        calculate_button.grid(row=2, columnspan=2, pady=10)  # Places button in the grid and spans two columns

        # Results Section
        self.results_text = tk.Text(self.root, height=10, width=50)  # Text area to display results
        self.results_text.pack(pady=10)  # Adds padding around the text area

        # History Log Section
        self.history_label = tk.Label(self.root, text="History Log:")  # Label for the history log
        self.history_label.pack(pady=10)  # Adds padding around the label
        self.history_listbox = tk.Listbox(self.root)  # Listbox to display history of calculations
        self.history_listbox.pack(pady=10)  # Adds padding around the listbox

        # Exit Button
        exit_button = tk.Button(self.root, text="Exit", command=self.exit_app)  # Button to exit the application
        exit_button.pack(pady=10)  # Adds padding around the button

    def calculate_weights(self):
        """
        Calculates the weight based on the entered 1RM and percentage.
        Updates the results display and history log.
        """
        try:
            one_rm = float(self.one_rep_max_entry.get())  # Gets the 1RM value from the input field
            percentage = float(self.percentage_entry.get().strip('%')) / 100  # Gets percentage and converts to decimal
            
            calculated_weight = one_rm * percentage  # Calculates the weight to lift
            
            # Display results
            self.results_text.delete(1.0, tk.END)  # Clears previous results
            self.results_text.insert(tk.END, f"Calculated Weight for {percentage * 100}%: {calculated_weight:.2f} lbs\n")  # Shows the new result
            
            # Append to history
            self.history.append(f"1RM: {one_rm}, Percentage: {percentage * 100}%, Weight: {calculated_weight:.2f} lbs")  # Stores the calculation
            self.update_history()  # Updates the history log display

        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numbers for 1RM and percentage.")  # Error message for invalid input

    def update_history(self):
        """
        Updates the history listbox with the latest calculations.
        Clears the listbox and adds all entries from the history list.
        """
        self.history_listbox.delete(0, tk.END)  # Clears the current listbox
        for entry in self.history:  # Loops through all entries in history
            self.history_listbox.insert(tk.END, entry)  # Adds each entry to the listbox

    def exit_app(self):
        """
        Exits the application.
        Closes the main window and terminates the program.
        """
        self.root.quit()  # Quits the Tkinter main loop

if __name__ == "__main__":
    root = tk.Tk()  # Creates the main application window
    app = LiftTracker(root)  # Initializes the LiftTracker application
    root.mainloop()  # Starts the Tkinter event loop