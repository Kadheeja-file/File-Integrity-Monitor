File Integrity Monitor Using Python

1. Project Overview

The File Integrity Monitor is a Python-based application developed to monitor files and identify unexpected changes. It uses the SHA-256 hashing algorithm to calculate unique hash values for files and compare them during repeated scans.

The main purpose of this project is to help identify whether files have been added, modified or deleted from a selected folder.

2. Objectives

* To monitor files in a selected folder.
* To generate SHA-256 hash values.
* To detect newly added files.
* To identify modified files.
* To detect deleted files.
* To improve awareness of file integrity and security.

3. Technologies Used

* Programming Language: Python
* Hashing Algorithm: SHA-256
* Libraries: OS, Hashlib and Time
* Web Framework: Flask
* Development Environment: Visual Studio Code
* Deployment Support: Gunicorn

4. Main Features

* File Monitoring: Scans files in a selected folder.
* SHA-256 Hashing: Generates hash values to identify file content changes.
* New File Detection: Identifies newly added files.
* File Modification Detection: Compares hash values to identify modifications.
* File Deletion Detection: Identifies files that have been deleted.
* Continuous Monitoring: Performs scans at five-second intervals.

5. Project Files

* main.py – Main Python program that monitors files and detects new, modified and deleted files.
* app.py – Flask web application that displays monitored files and their SHA-256 hash values.
* requirements.txt – Contains the required Python packages.
* sample.txt.txt – Sample text file used in the project.

6. Requirements

* Python 3 installed on the computer.
* Visual Studio Code or another Python editor.
* Required Python packages.
* Internet connection to install the required packages.

7. Installation

1. Download or clone this repository.
2. Open the project folder in Visual Studio Code.
3. Open the terminal.
4. Install the required packages using:
    pip install -r requirements.txt

8. How to Run the Project

A. Run the Main File Monitoring Program

1. Open the terminal in the project folder.
2. Execute:
    python main.py
3. Enter the folder path that you want to monitor.
4. The program displays “Monitoring started!”
5. The program scans the folder every five seconds.
6. It displays alerts when files are added, modified or deleted.

B. Run the Web Application

1. Open the terminal in the project folder.
2. Execute:
    python app.py
3. Open a web browser.
4. Visit:
    http://127.0.0.1:5000
5. The web page displays the files and their SHA-256 hash values from the application’s configured folder.

9. Working Principle

The main program first asks the user to enter a folder path. It scans the files and calculates their SHA-256 hash values.

After five seconds, the program scans the folder again and compares the new results with the previous scan.

If a new file is found, it displays a new file alert. If a hash value changes, it displays a file modification alert. If a previously detected file is missing, it displays a file deletion alert.

10. Expected Output

The main program displays messages such as:

* Monitoring started!
* NEW FILE
* FILE MODIFIED
* FILE DELETED

The web application displays file names and their corresponding SHA-256 hash values.

11. Conclusion

The File Integrity Monitor demonstrates how Python and SHA-256 hashing can be used to monitor file integrity. It provides a simple method to identify changes in files and understand the importance of file security.

12. Future Enhancements

* Add email notifications for detected changes.
* Store previous hash values permanently.
* Support monitoring of subfolders.
* Improve the web interface with additional monitoring features.

⸻

Developed using Python and SHA-256.
