# Master Password-Protected Password Manager  

A beginner-friendly **password manager** designed for securely storing and managing your passwords using **encryption**. This project features a master password for authentication, ensuring your sensitive information remains protected.  

---
## Features  
- **Master Password Protection**: Access your stored passwords securely with a single master password.  
- **Encryption**: Passwords are encrypted to maintain confidentiality.  
- **User-Friendly Interface**: Intuitive and easy-to-use design for all users.  
- **Secure Storage**: Safely store multiple passwords in a secure database or file system.

---
## Prerequisites  
- **Python 3.7+**  
- Any additional libraries (mentioned in `requirements.txt`)

---
## Installation  
1. Clone the repository:  
   ```bash
   git clone https://github.com/kl-priyanka/CyberSecurityProject.git
2. Install dependencies (if required):  
   ```bash
   pip install -r requirements.txt
   ```  

---

## Usage  
1. Run the application:  
   ```bash
   streamlit run password_manager.py
   ```  
2. Set up a **master password** if you’re running it for the first time.  
3. Use the application to:  
   - Save new passwords.  
   - Retrieve stored passwords.  
   - Manage your saved accounts securely.  

---

### Files Generated
The following files will be created automatically when you run the application:
- `passwords.json`: Stores the encrypted passwords.
- `master_password.txt`: Contains the hashed master password.
- `key.key`: The encryption key used to secure passwords.  

---

## Project Structure  
```
CyberSecurityProject/
├── password_manager.py   # Main application file
├── key.key               # Encryption key file for securing passwords
├── master_password.txt   # Stores the hashed master password
├── passwords.json        # Stores encrypted passwords in JSON format
├── requirements.txt      # Dependencies list for the project
├── README.md             # Project documentation
├── .gitignore            # Specifies files and folders to ignore in version control
```  

## Contributing  
Contributions are welcome! If you’d like to improve this project, please:  
1. Fork the repository.  
2. Create a new branch for your feature or bug fix.  
3. Submit a pull request.  

---

## License  
This project is licensed under the [MIT License](LICENSE).  

---

## Acknowledgments  
This project is a beginner-level cybersecurity tool, created to learn and implement basic encryption and secure storage concepts.  

Feel free to suggest improvements or provide feedback! 🚀  
