# Password Generator

This project is a simple password generator with a graphical user interface (GUI) built using `PyQt5`. The application allows users to generate a random password of a specified length and copy it to the clipboard.

## Features

- Generate a random password with a default length of 16 characters.
- Specify a custom password length.
- Copy the generated password to the clipboard.

## Requirements

- Python 3.9.16
- `PyQt5` library

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/yourusername/password-generator.git
    cd password-generator
    ```

2. **Create a virtual environment (optional but recommended):**

    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**

    ```sh
    pip install PyQt5
    ```

## Usage

1. **Run the application:**

    ```sh
    python password_generator_app.py
    ```

2. **Generate a password:**

    - Enter the desired password length in the input field (default is 16).
    - Click the "Generate Password" button to generate a random password.
    - Click the "Copy to Clipboard" button to copy the generated password to the clipboard.

## Project Structure

- `pass_generate.py`: Contains the `PassGenerate` class responsible for generating passwords.
- `password_generator_app.py`: Contains the `PasswordGeneratorApp` class and the main application logic.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.