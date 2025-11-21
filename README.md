# Book Rating Prediction using Multiple Linear Regression

This project applies a multiple linear regression model to predict the rating of books based on their attributes such as author, publisher, publication year, format, number of pages, category, and popularity.
The goal is to simulate a dataset of books with diverse features (author, publisher, year, pages, format, category, etc.) and analyze how each variable influences the final rating.

## Task
Predict the book rating (0–5) using multiple input variables such as:

- Author
- Publisher
- Publication Year
- Number of Pages
- Format (Physical/Digital)
- Category
- Popularity

## Tools and libraries used
| Tool                     | Purpose                                    |
| ------------------------ | ------------------------------------------ |
| **Python 3.x**           | Main programming language                  |
| **NumPy**                | Numerical computations                     |
| **Pandas**               | Data manipulation and CSV handling         |
| **Matplotlib**           | Visualization and statistical plots        |


# Dataset Generation
Script used:
baselibros.py — a Python script developed to synthetically generate book data for regression analysis.

## How the data was obtained:
The dataset was generated using a custom Python script named baselibros.py. The dataset was not collected from real sources.
This script synthetically creates a realistic dataset of books by combining randomized attributes using Python’s random library.

Each record corresponds to a unique book with the following variables:

| Variable              | Description                                                         | Type        |
| --------------------- | ------------------------------------------------------------------- | ----------- |
| **libro**             | Book title, created by combining a random prefix and category.      | Categorical |
| **autor**             | Randomly selected from a list of fictitious authors.                | Categorical |
| **editorial**         | Random publisher from a predefined list.                            | Categorical |
| **anio_publicacion**  | Random integer between 2000 and 2024.                               | Numerical   |
| **num_paginas**       | Random integer between 120 and 800.                                 | Numerical   |
| **formato**           | Either *Físico* or *Digital*.                                       | Categorical |
| **categoria**         | General field such as Ingeniería, Informática, Educación, etc.      | Categorical |
| **rating**            | Random float between 0.0 and 5.0 representing book evaluation.      | Numerical   |
| **popularidad_libro** | Random integer representing how many times the book has been rated. | Numerical   |

## **Changes made to the project**

The preprocessing and modeling processes of the book rating prediction system were updated. The implemented changes are briefly described below:

### 1. Dataset enhancement
- A new synthetic dataset was generated using a custom Python script.
- Added additional book-related variables (author, publisher, category, format, pages, year, popularity).
- Removed unnecessary student information (name, ID, major) based on instructor feedback.
- Ensured that the dataset contains meaningful features for regression tasks.

### 2. Application of coding techniques
Three techniques for processing categorical variables were included:
- **Label Encoding** for exploration
- **Target Encoding** for analisis
- **One-Hot Encoding** final technique used in the model

### 3. Feature Scaling application
- **StandardScaler** was applied to scale the numerical variables and the variables coded with OHE, improving the stability of the final model.

### 4. Training of two models
- **Modelo A (baseline):** without encoding or scaling techniques, using only numerical variables.
- **Modelo B (processed):** using One-Hot Encoding and Feature Scaling.

### 5. Performance comparison
- Metrics (R², MSE, RMSE) were calculated for both models.
- The impact of the applied techniques on the quality of the prediction was analyzed.


