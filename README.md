# AI Powered Directory Management System

## Overview

The **AI Powered Directory Management System** is a Python-based automation tool that monitors a directory and automatically organizes files into categorized folders.

The system combines **rule-based file classification** with **AI-based document classification**. Media files such as images and videos are sorted using file extensions, while text-based documents are analyzed using machine learning to determine their category.

This allows the system to intelligently organize files with minimal manual intervention.

---

## Features

* Real-time directory monitoring
* Automatic file classification based on file extensions
* AI-based document classification for text documents
* Automated file movement into categorized folders
* Logging system to track file operations
* Modular and scalable Python architecture

---

## Project Structure

```
ai-directory-manager
│
├── main.py                 # Main program that monitors directory
├── classifier.py           # File classification logic (rule-based + AI)
├── text_extractor.py       # Extracts text from documents
├── train_model.py          # Script used to train the ML model
├── file_operations.py      # File moving and handling
├── config.py               # Configuration settings
│
├── watched_folder          # Folder being monitored
├── organized               # Destination folder for sorted files
└── logs                    # Log files for system activity
```

---

## How It Works

1. The system continuously monitors the **watched_folder**.
2. When a new file is detected, the system identifies the file type.
3. Media files (images, videos, archives) are categorized using file extensions.
4. Document files (PDF, DOCX, TXT) are analyzed using an AI model.
5. The file is automatically moved into the appropriate folder inside **organized**.
6. Every operation is recorded in the log file for monitoring and debugging.

---

## Technologies Used

* Python
* Machine Learning for document classification
* File System Automation
* Logging System
* Modular Software Design

---

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

Train the AI model:

```
python train_model.py
```

Run the program:

```
python main.py
```

---

## Future Improvements

* Duplicate file detection
* GUI dashboard for system monitoring
* Real-time file monitoring using event-based systems

---

## Author

Sreehar Prassad
