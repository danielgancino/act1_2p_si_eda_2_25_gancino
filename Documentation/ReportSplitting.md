# Data splitting - final model

---

## 1. Project Description
The objective of this project is to apply data preprocessing techniques such as **One-Hot Encoding** and **Feature Scaling** on a book dataset to train a **multiple linear regression model**. The model predicts the **rating** of books based on various features such as author, genre, and other attributes.

---

## 2. Applied Data Splitting Techniques

### 2.1 K-Fold Cross Validation (K-Fold)
- **Description:** In this technique, the dataset is divided into K subsets(folds). The model is trained K times, each time using K-1 subsets for training and the remaining subset for evaluation.
- **Usage:** This technique is useful when dealing with a moderately large dataset and is intended to provide a more robust evaluation of the model.
- **Python Library:** `sklearn.model_selection.KFold`
- **Justification:** This technique was chosen to obtain a more reliable validation of the model by using multiple data partitions, helping avoid overfitting.

-----

### 2.2 Leave-One-Out Cross Validation (LOO-CV)
- **Description:**In this technique, the dataset is divided such that one single sample is used as the test set, and the rest of the data is used for training. This process is repeated for each sample in the dataset.
- **Usage:** This technique is useful when the dataset is small and you want to get an accurate evaluation for each sample.
- **Python Library:** `sklearn.model_selection.LeaveOneOut`
- **Justification:** This technique was chosen to provide a detailed analysis of each individual sample, though it is more computationally expensive.

-----

## 3. Model Comparison
Two models were trained using multiple linear regression:

- **Model A:** Trained using K-Fold Cross Validation with 10 splits.
- **Model B:** Trained using Leave-One-Out Cross Validation.

The results show that the K-Fold model is more computationally efficient, while the LOOCV model provides a more detailed evaluation for each individual sample, but represents an increase of the use of computational power and resources leading to an increase in computation time.

-----

## 4. Best Model and Justification:

Based on the evaluation of both models, Model A (K-Fold Cross Validation) outperforms Model B (Leave-One-Out Cross Validation) in terms of computational efficiency and generalization to unseen data.

- **R²:** Model A demonstrated a higher R² score, indicating a better fit to the data.

- **MSE and RMSE:** Model A also achieved lower MSE and RMSE scores, suggesting that the model’s predictions are more accurate with fewer errors.

While Model B provided a more detailed analysis, it was computationally expensive due to the nature of the Leave-One-Out technique. Model A, on the other hand, was faster and still showed strong results, making it the best choice for this dataset.

-----

## 5. Conclusion
- The K-Fold Cross Validation technique proved to be faster and effective for this larger dataset. The model trained with K-Fold achieved good performance in terms of R², MSE, and RMSE.
- The Leave-One-Out Cross Validation technique provided a more detailed evaluation, but was computationally expensive, especially with a dataset of 2636 samples.

I think the K-Fold Cross Validation is more suitable considering it is for larger datasets, while LOOCV is used more for smaller datasets or when more detailed sample analysis is required.

-----

## 6. Next Steps
- Improve the model: Try other algorithms such as Random Forest or Gradient Boosting to compare performance with linear regression.
- Explore more validation techniques: Investigate Stratified K-Fold or other methods to evaluate the model with different types of datasets.
- Optimize the model using techniques like regularization (Ridge, Lasso) to improve performance and prevent overfitting.


