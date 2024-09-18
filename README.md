# Library Management System

A simple and interactive Library Management System built in Python. This program allows users to manage books within a library, including lending and returning books, adding new books, and deleting books from the inventory.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Code Structure](#code-structure)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features

- **Display Books**: View all available books in the library.
- **Lend Books**: Lend a book to a user.
- **Return Books**: Return a previously lent book.
- **Add Books**: Add new books to the library inventory.
- **Delete Books**: Remove a book from the library inventory.
- **User Authentication**: A simple password protection to delete books.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/library-management-system.git
    ```

2. Change to the project directory:
    ```bash
    cd library-management-system
    ```

3. No additional dependencies are required to run this Python script. Make sure you have Python installed on your system.

4. Run the program:
    ```bash
    python library_management.py
    ```

## Usage

Once the program is running, the following commands are available:

- **Q**: Exit the program.
- **D**: Display all books in the library.
- **L**: Lend a book. You will be prompted to enter the book name and your name.
- **R**: Return a book. You will be prompted to enter the book name and your name.
- **A**: Add a new book to the library.
- **DEL**: Delete a book from the library. You will need to enter the secret key for authentication.

### Example Workflow

1. Start the program.
2. Select an option to display the list of books.
3. Choose to lend a book by providing its name.
4. Return the book by entering the name again.
5. Add or delete books as required.

## Code Structure

The project consists of a single main class, `Library`, implemented in `library_management.py`:

- **Library Class**: Contains methods to manage books including lending, returning, adding, and deleting books.

### Sample Code

Here’s a simple usage of the code in `library_management.py`:

```python
if __name__ == "__main__":
    main()
