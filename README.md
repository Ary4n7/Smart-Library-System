# Smart Library Management System 📚

A modern, web-based Library Management System built with Python and Streamlit. This project beautifully demonstrates core Data Structures and Algorithms (DSA) through practical application.

## Features & Highlights

- **Modern UI/UX**: A responsive, card-based interface styled with neo-brutalist aesthetics (Beige, White, Black). Features interactive navigation mimicking a mobile application.
- **Dynamic Catalog**: Includes a database of over 50 books across categories like Fiction, Technology, Science, and Programming.
- **Issue & Return Workflows**: Track book loans, borrower names, and due dates dynamically. Automatically calculates overdue days upon return.
- **Data Structures in Action**:
  - **Binary Search Tree (BST)**: Books are inserted into a BST based on their unique ID. Used for rapid searching and Inorder Traversal display.
- **Algorithms in Action**:
  - **Linear Search**: Used to search for books by title or keyword.
  - **Binary Search**: Used for fast lookups by Book ID.
  - **Bubble Sort**: Sorts the library catalog by Book ID.
  - **Selection Sort**: Sorts the catalog alphabetically by Title.
  - **Merge Sort**: Sorts the catalog alphabetically by Author.

## Technologies Used
- **Python 3**
- **Streamlit**: For the web framework and interactive UI components.
- **HTML/CSS**: Custom markdown styling to override default themes and achieve a premium look.

## Running Locally

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the application:
   ```bash
   streamlit run app.py
   ```
