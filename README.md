# AI Phishing Website Detection System

## Overview

AI Phishing Website Detection System is a Machine Learning-based web application that identifies whether a website URL is legitimate or phishing. The system analyzes URL features and uses a Random Forest Classifier to provide real-time predictions.

---

## Problem Statement

Phishing websites are designed to steal sensitive information such as usernames, passwords, banking details, and personal data. It is often difficult for users to identify fake websites. This project helps users detect suspicious websites before visiting them.

---

## Objectives

* Detect phishing websites using Machine Learning.
* Analyze URL features automatically.
* Provide real-time prediction results.
* Improve online security and user awareness.
* Create a simple and user-friendly web application.

---

## Technologies Used

* Python
* Flask
* HTML
* CSS
* JavaScript
* Pandas
* NumPy
* Scikit-Learn
* GitHub

---

## Machine Learning Algorithm

**Random Forest Classifier**

Why Random Forest?

* High Accuracy
* Handles large datasets efficiently
* Reduces overfitting
* Fast prediction performance

---

## Project Workflow

1. User enters a website URL.
2. URL features are extracted.
3. Features are processed by the Machine Learning model.
4. The model predicts whether the URL is Safe or Phishing.
5. The result is displayed on the web interface.

---

## Project Structure

AI-Phishing-Website-Detection/

├── app.py

├── Dataset.csv

├── phishing_model.pkl

├── train_model.py

├── requirements.txt

├── templates/

│ └── index.html

├── static/

│ └── style.css

└── README.md

---

## Installation

1. Clone the repository

git clone YOUR_GITHUB_REPOSITORY_LINK

2. Install dependencies

pip install -r requirements.txt

3. Run the application

python app.py

4. Open browser

http://127.0.0.1:5000

---

## Features

* Real-time URL Analysis
* Phishing Website Detection
* User-Friendly Interface
* Fast Prediction
* Machine Learning Based Security

---

## Results

Test Cases:

* amazon.in → Safe Website
* secure-paytm-login-update.xyz → Phishing Website

The system successfully classified both legitimate and phishing URLs.

---

## Future Scope

* Browser Extension
* Mobile Application
* Email Phishing Detection
* Deep Learning Integration
* Explainable AI Dashboard

---

## Author

Name: Asmita Jha

Project: AI Phishing Website Detection System
