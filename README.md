# Encrypted Message Accessing Application

## Overview
The Encrypted Message Accessing Application is designed to securely manage and access encrypted messages. Users can encrypt and decrypt messages using a password set by the message sender for added security. The application stores user credentials and encrypted data in a MySQL database and ensures that decrypted messages are automatically deleted from the server.

## Features
- **Encryption**:
  - Users can enter a message to be encrypted.
  - The message is encrypted using AES encryption and saved in the database with a unique username and password.
- **Decryption**:
  - Users can decrypt a message by providing their username and password set during encryption.
  - The decrypted message is displayed, and the entry is deleted from the server to maintain security.
- **User Authentication**:
  - The application authenticates users based on their username and password.
- **Data Management**:
  - Encrypted data and AES keys are stored securely in a MySQL database.
  - Decrypted messages are removed from the server after access to prevent unauthorized access.

## Technical Details
- **Programming Language**: Python
- **Database**: MySQL
- **Encryption Library**: `cryptography.hazmat`
- **User Interface**: Command-line interface

## Database Structure
The `app_data` table consists of the following fields:
- `date` (VARCHAR(50)): The date and time when the message was encrypted.
- `data` (BLOB): The encrypted message.
- `aes_key` (BLOB): The AES key used for encryption.
- `username` (VARCHAR(100)): The username associated with the message.
- `psswd` (VARCHAR(100)): The password set by the message sender for decryption.

## Example Usage
### Encrypt a Message
1. User enters the text to be encrypted.
2. The text is encrypted and saved with the username and password.
3. The application confirms that the message is saved.

### Decrypt a Message
1. User enters their username and password.
2. The application retrieves and decrypts the message.
3. The decrypted message is displayed, and the entry is deleted from the database.

## Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/encrypted-message-accessing-application.git
   cd encrypted-message-accessing-application
   ```

2. **Install Required Packages**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Setup MySQL Database**:
   - Create a database named `encryption_app`.
   - Create a table `app_data` with the structure provided in the Database Structure section.

4. **Configure Database Connection**:
   - Update the database connection details in the Python script.

## Running the Application
Execute the main script to start the application:
```bash
python main.py
```

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contact
For any inquiries or issues, please open an issue on GitHub or contact me at ghoshsuryakanti.official@gmail.com .
