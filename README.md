



## **Project Overview**

This project is a **simple demonstration of K-Nearest Neighbors (KNN)** algorithm applied to the **White Wine Quality Dataset**.
The main aim is **educational**: to understand **how KNN works**, how to process data, split train/test, and make predictions.

> ⚠️ **Note:** This project is **not for high-accuracy production use**. Accuracy is moderate (\~45–50%) because only basic KNN is used.

---

## **Dataset**

* **Name:** White Wine Quality Dataset
* **Source:** [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/wine+quality)
* **Number of Instances:** 4898 wines
* **Number of Features:** 11 physicochemical properties
* **Target:** `quality` (score from 3–9)

### **Features**

| Feature              | Description                   |
| -------------------- | ----------------------------- |
| fixed acidity        | Measures acidity of wine      |
| volatile acidity     | Vinegar taste indicator       |
| citric acid          | Citrate content in wine       |
| residual sugar       | Sugar left after fermentation |
| chlorides            | Salt content                  |
| free sulfur dioxide  | Free SO₂ in wine              |
| total sulfur dioxide | Total SO₂                     |
| density              | Wine density                  |
| pH                   | Acidity level                 |
| sulphates            | Antioxidant content           |
| alcohol              | Alcohol percentage            |

---

## **Methodology**

1. **Data Loading:**
   Loaded CSV dataset and removed duplicate rows.

2. **Feature & Target Split:**

   * Features (X): 11 physicochemical properties
   * Target (y): wine quality (3–9)

3. **Train/Test Split:**

   * 80% training, 20% testing
   * Stratified split to maintain class distribution

4. **Feature Scaling:**

   * Used `StandardScaler` to normalize features
   * KNN is distance-based → scaling is necessary

5. **KNN Model:**

   * `KNeighborsClassifier(n_neighbors=7)`
   * Simple KNN, no advanced tuning

6. **Prediction & Evaluation:**

   * Predicted test set quality
   * Evaluated using **accuracy, confusion matrix, and classification report**

7. **Pipeline Creation:**

   * Used `Pipeline` (Scaler + KNN)
   * Saved with `joblib` → ready for app integration

---

## **Accuracy**

* **Simple KNN Accuracy:** \~45–50%
* Reason for moderate accuracy:

  1. Original dataset has 7 classes → overlapping features
  2. KNN is sensitive to noise and uninformative features
  3. No class balancing, no feature selection applied

> This project is primarily for **learning and understanding KNN workflow**, not for high-performance prediction.

---

## **How I Used KNN**

* Loaded dataset → cleaned duplicates
* Split into features & target
* Scaled features → required for distance-based KNN
* Trained KNN → predicted test set
* Evaluated model → observed moderate accuracy (\~45–50%)
* Created pipeline → app-ready for user input predictions

---

## **Project Purpose**

1. Learn **how KNN works** in practice
2. Understand **data preprocessing**: scaling, train/test split
3. Get hands-on experience with **pipeline creation** for app deployment
4. Educational understanding of **accuracy, limitations, and evaluation metrics**

---

## **Future Improvements**

* Feature selection → remove low-correlation features
* Class merge or oversampling → reduce imbalance
* Try other models (RandomForest, GradientBoosting) → higher accuracy
* Add visualization (EDA) → better understanding of data

---

## **Conclusion**

This project is a **knowledge-oriented KNN implementation** for white wine quality prediction.
It demonstrates the **full pipeline from data loading, preprocessing, training, testing, and saving the model** for app integration.

Even though the **accuracy is moderate**, it provides **practical experience in KNN, preprocessing, and pipeline creation**.

---

