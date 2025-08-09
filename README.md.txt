# Subdomain Scanner

A simple and efficient subdomain scanning tool built with Python.  
It takes a subdomain prefix as input and scans for available subdomains listed in the `subdomainlist.txt` file using asynchronous HTTP requests.

---

## Features

- Graphical User Interface (GUI) using Tkinter  
- Asynchronous scanning with aiohttp for faster requests  
- Handles connection errors gracefully  
- Displays real-time results in the GUI  
- Notifies when scan is complete with an option to retry  

---

## Requirements

- Python 3.7 or higher  
- aiohttp library  
- A valid `subdomainlist.txt` file in the project directory  

---

## Installation

Install the required Python package using pip:

```bash
pip install aiohttp
