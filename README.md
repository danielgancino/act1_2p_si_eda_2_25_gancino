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

