# 📘 Linear Regression – AI & ML Internship Task (Elevate Labs)

This repository contains the complete solution for **Task 3: Linear Regression** from the **AI & ML Internship Program** by Elevate Labs (USME, Govt. of India).

The task covers implementing and understanding **simple & multiple linear regression** using:
- Scikit-learn  
- Pandas  
- Matplotlib  

---

## 📌 Objective
Build and analyze a Linear Regression model to predict a continuous variable using a suitable dataset (e.g., house price prediction).

---

## 📂 Project Structure
```
Linear-Regression-Task/
│
├── house_price.csv
├── linear_regression.py
└── README.md
```

---

## 🧠 Steps Performed

### ✔ 1. Loaded and explored dataset  
- Checked first rows  
- Verified missing values  
- Identified features & target  

### ✔ 2. Preprocessed data  
- Selected relevant columns  
- Prepared X (features) and y (target)

### ✔ 3. Train-test split  
Performed 80-20 split using `train_test_split`.

### ✔ 4. Trained Linear Regression Model  
Used:
```
LinearRegression() from sklearn
```

### ✔ 5. Evaluated using:  
- **MAE** – Mean Absolute Error  
- **MSE** – Mean Squared Error  
- **RMSE** – Root Mean Squared Error  
- **R² Score** – Goodness of fit  

### ✔ 6. Interpreted Model Output  
- Intercept  
- Feature coefficients  
- Checking model performance  

### ✔ 7. Visualized Regression line  
(if dataset had only one independent feature)

---

## 🧪 Results
The script prints:
- Dataset preview  
- Training/testing samples  
- Model errors (MAE, MSE, RMSE, R²)  
- Feature coefficients  
- Intercept  

---

## 🚀 How to Run the Project

### **1️⃣ Install dependencies**
```
pip install pandas numpy scikit-learn matplotlib
```

### **2️⃣ Place dataset**
Add your dataset as:
```
house_price.csv
```

### **3️⃣ Run the script**
```
python linear_regression.py
```

---

## 📝 Interview Questions (with answers)

### **1. What assumptions does Linear Regression make?**
- Linearity  
- No multicollinearity  
- Homoscedasticity  
- Normal distribution of errors  
- Independence of observations  

### **2. How do you interpret coefficients?**  
A coefficient tells how much the target variable changes when the feature increases by 1 unit (keeping other features constant).

### **3. What is R² Score?**  
It measures how much variance in the target variable is explained by the model.

### **4. When do we prefer MSE over MAE?**  
When we want to penalize large errors more strongly.

### **5. How do you detect multicollinearity?**  
- Correlation matrix  
- VIF (Variance Inflation Factor)

### **6. Difference between Simple & Multiple Regression?**  
- Simple → 1 independent feature  
- Multiple → 2 or more independent features  

### **7. Can Linear Regression be used for classification?**  
Not ideal; Logistic Regression is used instead.

### **8. What happens if regression assumptions are violated?**  
Model becomes unreliable, inaccurate, and unstable.

---

## 🧑‍💻 Author
*Change your name*  
AI & ML Internship – Elevate Labs  

---

## 🎉 Completion Note
This GitHub repository fulfills all requirements for the **Task 3 submission**, including code, documentation, and evaluation.
