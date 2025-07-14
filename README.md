FILE-INTEGRITY-CHECKER
COMPANY: CODTECH IT SOLUTION

NAME: SAPPIDI ESWAR SAI

INTERN ID: CT06DF1722

DOMAIN: Cyber Security & Ethical Hacking

DURATION: 6 weeks

🔐 Project: File Integrity Checker using Python 📝 Description The purpose of this project is to develop a File Integrity Checker – a security tool that monitors and verifies the integrity of files by calculating and comparing cryptographic hash values. This is a fundamental concept in cybersecurity used to detect unauthorized changes, tampering, or corruption in file systems. The tool was implemented in Python and executed within a Kali Linux environment, leveraging its built-in terminal, Python interpreter, and file system tools.

File integrity verification is critical in environments where security and compliance are paramount, such as server administration, malware analysis, and forensic investigations. By storing the original hash values of files and later comparing them to current values, the tool can identify whether files have been added, modified, or deleted. Any change in hash values indicates a potential security event such as unauthorized access, malicious modification, or even accidental data corruption.

🛠️ Tools & Technologies Used

Python 3 Python was chosen for its readability, cross-platform capabilities, and strong standard library. The hashlib module was used to compute SHA-256 hash values for file contents. Additional modules like os, json, and argparse enabled directory traversal, data storage, and command-line argument parsing.

Hashlib The hashlib library in Python supports various cryptographic hash functions such as MD5, SHA-1, and SHA-256. For this project, SHA-256 was selected due to its strong resistance to collisions and widespread use in modern systems.

Kali Linux Kali Linux was used as the operating system to run and test the tool. Kali is widely known for penetration testing and security auditing. Its powerful terminal and pre-installed Python 3 environment make it ideal for scripting and automation tasks.

GitHub Version control was maintained using Git and GitHub. All code, documentation, and future enhancements were tracked using commits and pushed to a GitHub repository. This also facilitates collaboration, issue tracking, and project management.

⚙️ How It Works Initialization: The user runs the script with a target directory and the --init flag. This stores a JSON file (file_hashes.json) containing the SHA-256 hash values of all files in the directory.

Monitoring: On subsequent runs, the tool re-scans the directory and computes new hashes. It compares these against the stored hashes to detect:

Added files: Present in current scan, but not in the original hash file.

Modified files: Present in both, but hash values differ.

Deleted files: Present in the original hash file, but missing from the current scan.

Reporting: The script outputs a summary of any detected changes. This helps users or system administrators identify unexpected file modifications that could signal a security breach.

✅ Outcome This project demonstrates the practical application of cryptographic hash functions in security monitoring. It helped develop skills in secure coding, scripting, and Linux-based tool development. It also illustrates how basic principles of cybersecurity can be implemented with simple yet effective automation.


