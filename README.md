# Restaurant Management System 🍕

A simple GUI-based restaurant management system built using Python and Tkinter. It simulates customer interaction for ordering food at **ABC Restaurant**, including booking, menu display, billing, and feedback collection.

---

## 📌 Features

- **Welcome Screen**: Displays a splash screen for 2 seconds before transitioning to the main app.
- **Main Dashboard**: Full-screen GUI with a navigation menu.
- **Booking System**:
  - Select table number
  - Choose food items and quantity
  - Indicate possession of a government/corporate ID
- **Menu Viewer**: Displays items and prices in a clean format.
- **Billing**:
  - Calculates total based on menu item and quantity
  - Adds a service charge
  - Applies a discount for users with a valid ID
- **Feedback Form**:
  - Collects name, email, DOB, and ratings
  - Stores responses in an SQLite database

---

## 💾 Tech Stack

- **Frontend**: Python Tkinter (GUI)
- **Backend**: SQLite (for feedback storage)

---

## 📂 Project Structure

```text
abc_restaurant/
├── main.py            # Main Python GUI application
├── restaurant.db      # SQLite database file (created at runtime)
└── README.md          # Project documentation
