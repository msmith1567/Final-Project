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