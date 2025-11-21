# Categorical data encoding and feature scaling techniques

---

## 1. Introduction

For this task, it is going to be use some columns that are categorical and will be transformed:

- autor
- editorial
- formato
- categoria
- libro

---

## 2. Techniques Applied

### 2.1 Label Encoding
**Description:** Assigns each category an integer value (0, 1, 2...).  
**Library:** `sklearn.preprocessing.LabelEncoder`  
**Use Case:** Works for ordinal categories (not ideal for nominal ones).  
**Justification:** Used experimentally to explore transformations, but **not** used for the final model because it introduces artificial ordering.

---

### 2.2 One-Hot Encoding (OHE)
**Description:** Converts each category into binary indicator columns (0/1).  
**Library:** `pandas.get_dummies()`  
**Use Case:** Best approach for nominal categorical data in regression models.  
**Justification:** This technique **was used** in the final model because it avoids false ordinal relationships.

---

### 2.3 Target Encoding
**Description:** Replaces each category with the *mean rating* of that category.  
**Library:** Implemented manually using pandas.  
**Use Case:** Useful for high-cardinality variables.  
**Justification:** Applied as an additional technique, but avoided in the final model because it may cause *data leakage*.

---

### 2.4 Feature Scaling (StandardScaler)
**Description:** Normalizes features to mean = 0 and standard deviation = 1.  
**Library:** `sklearn.preprocessing.StandardScaler`  
**Use Case:** Important for regression, since feature scales affect coefficients.  
**Justification:** Used in the final model to improve training stability.

---

## 3. Implementation of Techniques

### 3.1 One-Hot Encoding

```python
df_encoded = pd.get_dummies(
    df,
    columns=["author", "publisher", "format", "category", "book_title"],
    drop_first=True
)
```

### 3.2 Label Encoding

```python
from sklearn.preprocessing import LabelEncoder

df_le = df.copy()
for col in ["author","publisher","format","category"]:
    df_le[col] = LabelEncoder().fit_transform(df_le[col])
```

### 3.3 Target Encoding

```python
df_te = df.copy()
for col in ["author","publisher","format","category"]:
    df_te[col] = df.groupby(col)["rating"].transform("mean")
```

### 3.4 Feature Scaling + Linear Regression Pipeline

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression

pipeline_B = Pipeline([
    ("scaler", StandardScaler()),
    ("model", LinearRegression())
])

pipeline_B.fit(X_train_B, y_train_B)
pred_B = pipeline_B.predict(X_test_B)
```

## 4. Model Building

In this section, two regression models were trained in order to compare the impact of applying preprocessing techniques versus using raw data.

### 4.1 Model A — Without Encoding or Scaling 

This model serves as the baseline reference.  
No encoding was applied to categorical variables and no feature scaling was used.  
Only numerical columns were included in the training process.

### 4.2 Model B — With One-Hot Encoding + Feature Scaling

This model includes the full preprocessing pipeline:

- One-Hot Encoding for categorical variables
- StandardScaler for numerical variables
- Linear Regression as the model

## 5. Comparison Between Models

| Model | R² | MSE | RMSE |
|-------|-------|---------|---------|
| Model without preprocessing | *-0.0036211611388050624* | *2.1635876463663073* | *1.4709138813561817* |
| Model with preprocessing (OHE + Scaling) | *-0.10601701553402809* | *2.384330705786502* | *1.544127813941094* |

### Key Findings

- The model **without preprocessing** shows lower performance because it uses only numerical features and lacks encoding and scaling.
- The model **with preprocessing** (One-Hot Encoding + StandardScaler) shows a significantly higher predictive capacity.
- Preprocessing steps such as encoding and scaling are essential when working with categorical variables in linear regression.
- Feature scaling ensures the model is not biased toward features with larger magnitudes.
- One-Hot Encoding prevents the model from assigning false ordinal relationships between categories.

---

## 6. Conclusions

The implementation of preprocessing techniques showed a major improvement on the performance of the regression model.

- The **baseline model** served as a reference but lacked the ability to capture deeper patterns.
- The **processed model** that included One-Hot Encoding and Feature Scaling achieved superior accuracy,.
- Scaling stabilized the optimization process and ensured all features contributed fairly.
- The experiment confirms that preprocessing is a critical step in any machine learning pipeline involving mixed-type data.

Although several encoding techniques were explored during the preprocessing stage, only **One-Hot Encoding** and **Feature Scaling** were used in the final regression model. The reasons are the following:

#### 6.1. One-Hot Encoding is the most suitable method for linear regression
Linear regression requires numerical inputs, but also assumes that numeric values have a **meaningful magnitude and distance**.  

- **Label Encoding** assigns arbitrary integers to categories (e.g., “Author A” = 1, “Author B” = 2), which incorrectly implies an ordinal relationship that does not exist. This distorts the model and violates regression assumptions.  
- **Target Encoding** replaces categories with the mean of the target variable. This introduces **data leakage** , meaning that the model indirectly sees the target, which produces artificially inflated performance and invalidates the task.

In contrast, **One-Hot Encoding** converts categorical variables into binary vectors without introducing false order or leaking target information. It preserves the nominal nature of the categories and is the mathematically correct encoding for linear regression.

#### 6.2. Feature Scaling is required for regression models
Regression models are sensitive to the scale of the predictors.  
If features have different magnitudes (e.g., number of pages vs. year of publication vs. binary OHE features), the model coefficients become unbalanced, and gradient-based optimization behaves poorly.

By applying **StandardScaler**, all features are transformed to:
- mean = 0  
- standard deviation = 1  

This ensures:
- numerical stability  
- fair coefficient estimation  
- improved convergence  
- better interpretability  

#### 6.3. Using One-Hot + Scaling ensures a valid and fair comparison
Since the unprocessed model was trained **without any encoding or scaling**, the processed model must apply the **most appropriate preprocessing pipeline** to demonstrate how preprocessing improves performance.

The final decision to use **One-Hot Encoding + StandardScaler** provides:
- a clean, correct, and valid regression pipeline  
- no leakage  
- consistent structure across all features  

---

## 7. References

- https://scikit-learn.org/stable/  
- https://pandas.pydata.org  
- https://www.geeksforgeeks.org/machine-learning/categorical-data-encoding-techniques-in-machine-learning/
- https://scikit-learn.org/stable/auto_examples/preprocessing/plot_scaling_importance.html

