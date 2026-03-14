# AI Powered Directory Management System

## Overview

The AI Powered Directory Management System is a Python-based automation tool that monitors a directory and automatically organizes files into categorized folders.

The system currently classifies files based on their extensions and moves them to appropriate folders. Future versions will include AI-based document classification to improve accuracy and intelligent sorting.

## Features

* Real-time directory monitoring
* Automatic file classification based on file extensions
* Automated file movement into categorized folders
* Logging system to track file operations
* Modular and scalable Python architecture

## Project Structure

```
ai-directory-manager
│
├── main.py                 # Main program that monitors directory
├── classifier.py           # File classification logic
├── file_operations.py      # File moving and handling
├── config.py               # Configuration settings
│
├── watched_folder          # Folder being monitored
├── organized               # Destination folder for sorted files
└── logs                    # Log files for system activity
```

## How It Works

1. The system continuously monitors the **watched_folder**.
2. When a new file is detected, the system identifies the file type using its extension.
3. The file is categorized into folders such as Images, Documents, Videos, etc.
4. The file is automatically moved to the **organized** directory.
5. The operation is recorded in the log file for tracking and debugging.

## Technologies Used

* Python
* File System Automation
* Logging System
* Modular Software Design

## Installation

Clone the repository:

```
git clone https://github.com/sreeharprassad/ai-directory-manager.git
```

Navigate to the project folder:

```
cd ai-directory-manager
```

Install required dependencies:

```
pip install -r requirements.txt
```

Run the program:

```
python main.py
```

## Future Improvements

* AI-based document classification using machine learning
* Duplicate file detection
* GUI dashboard for system monitoring

## Author

Sreehar Prassad
