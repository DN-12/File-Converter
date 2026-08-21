# 🔄 File Converter

A Python project for converting files between different formats.

The goal of this project is to simplify common file conversions while practicing Python programming, file manipulation, functions, data processing, and external libraries.

## 🚀 Supported Conversions

The current version supports:

| Source | Destination |
| ------ | ----------- |
| CSV    | XLSX        |
| XLSX   | CSV         |
| JPG    | PNG         |
| PNG    | JPG         |
| JSON   | CSV         |
| XML    | CSV         |

## 🛠️ Technologies

* Python
* Pandas
* OpenPyXL
* Pillow

## 📦 Installation

Install the project dependencies using:

```bash
pip install -r requirements.txt
```

## ▶️ How to Run

Run the main file:

```bash
python main.py
```

The program will ask for the file you want to convert and the desired output format.

### Example

```text
Enter the file: products.csv

Which format do you want to convert to?

1 = EXCEL
2 = CSV
3 = JPG
4 = PNG
5 = PDF
6 = XML
7 = JSON
8 = TXT
9 = DOCX

Enter the desired number:
```

After the conversion, the new file will be saved using the original file name.

## 📁 Project Structure

```text
File Converter/
│
├── main.py
├── README.md
└── requirements.txt
```

## 📚 What I Practiced

During the development of this project, I practiced:

* Python functions
* Parameters and arguments
* Conditional statements
* User input
* String manipulation
* File extension identification
* Reading and writing files
* Using external Python libraries
* Data manipulation with Pandas
* Image conversion with Pillow

## 🔮 Future Improvements

Possible future improvements include:

* Error handling
* File validation
* Better file path and filename handling
* Support for additional formats
* Graphical user interface
* Batch file conversion
* Improved code organization

## 🎯 Project Goal

This project is part of my development portfolio and was created to practice Python programming and automation.

## 👨‍💻 Status

**Version 1.0 — Completed**

The project may receive additional features and improvements as I continue learning.
