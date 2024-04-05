# SSH Brute Force Tool

This Python script is designed for conducting SSH brute force attacks on target systems. It attempts to gain unauthorized access to SSH servers by trying different combinations of usernames and passwords from provided lists.
Once access is gained, the script provides an interactive shell through which remote commands can be executed on the target system.

## Installation

1. Clone the repository:

2. Install dependencies:

pip install paramiko
   
## Usage

1. Make sure you have two text files containing lists of usernames and passwords in the format described below:

    - `users.txt`: List of usernames, with each username on a separate line.
    - `passwords.txt`: List of passwords, with each password on a separate line.

2. Run the script:

    python SSH-Brute-Force-Tool.py

3. Follow the on-screen instructions to execute the SSH brute force attack.

## Contributing

Contributions are welcome! If you want to contribute to this project, please fork the repository and submit a pull request with your changes.

## Disclaimer

This tool is intended for educational and ethical testing purposes only. Unauthorized access to computer systems is illegal and unethical. Use this tool responsibly and only on systems for which you have explicit permission to test.

Author: Michał Botuliński
