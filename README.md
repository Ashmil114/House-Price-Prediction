# House Price Prediction

This repository contains a project for predicting house prices using a Linear Regression algorithm. The project utilizes Python libraries such as NumPy, pandas, and scikit-learn, and includes a client-side server implemented with Flask.

## Table of Contents

- Introduction
- Features
- Installation
- Usage

## Introduction

This project aims to predict house prices based on various features using a Linear Regression model. The model is trained on a dataset containing historical house prices and their corresponding features. The project also includes a Flask server to provide a web interface for making predictions.

## Features

- **Linear Regression Model**: Utilizes scikit-learn to build and train the model.
- **Data Processing**: Uses pandas and NumPy for data manipulation and preprocessing.
- **Flask Server**: Provides a client-side server for making predictions via a web interface.
- **Visualization**: Includes scripts for visualizing data and model performance.

## Installation

1. Clone the repository:
    ```bash
    https://github.com/Ashmil114/House-Price-Prediction.git
    cd House-Price-Prediction
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Train the Model**:
    Use Jupyter Notebook file on filepath train data/home_rate.ipynb

2. **Run the Flask Server**:
    ```bash
    python app.py
    ```

3. Open your web browser and go to `http://127.0.0.1:5000` to use the web interface for making predictions.


## Technology

- **Python**: Core programming language used for the project.
- **NumPy**: Library for numerical computations.
- **pandas**: Library for data manipulation and analysis.
- **scikit-learn**: Machine learning library for building and training the model.
- **Flask**: Micro web framework for the client-side server.
- **jQuery**: JavaScript library for enhancing the web interface.

