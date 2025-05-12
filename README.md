# Understanding and Predicting Employee Turnover at Jaya Jaya Maju

## Project Overview

This project aims to analyze and predict employee turnover (attrition) at Jaya Jaya Maju. The tasks include data understanding, exploratory data analysis (EDA), data preprocessing, model building, evaluation, and saving the best model for future predictions.

## Project Structure

- `model/model.ipynb`: Main notebook containing all analysis, modeling, and evaluation steps.
- `result_model.pkl`: Saved best model for predicting employee attrition.
- `requirements.txt`: List of required Python packages.
- `employee_data.csv`: Main dataset used for analysis and modeling.

## How to Open and Run the Project

1. **Clone or Download the Repository**
   - Clone the repository or download the project files to your local machine.

2. **Open the Project Directory**
   - Open the project folder in [Visual Studio Code](https://code.visualstudio.com/) or your preferred IDE.

3. **Install Dependencies**
   - Make sure you have Python installed.
   - Install the required packages using:
     ```
     pip install -r requirements.txt
     ```

4. **Open the Notebook**
   - Navigate to the `model` folder.
   - Open `model.ipynb` in Jupyter Notebook or VS Code's notebook interface.

5. **Run the Notebook**
   - Execute the cells sequentially to reproduce the analysis, modeling, and evaluation.

## Project Tasks

- **Data Understanding**: Explore the dataset, understand feature meanings, and check for missing values or duplicates.
- **Exploratory Data Analysis (EDA)**: Visualize and analyze patterns related to employee attrition.
- **Data Cleaning & Preprocessing**: Handle missing values, outliers, encode categorical variables, and prepare data for modeling.
- **Model Building**: Train multiple machine learning models (Logistic Regression, Decision Tree, Random Forest, XGBoost, Naive Bayes) to predict attrition.
- **Model Evaluation**: Evaluate models using metrics such as accuracy, precision, recall, F1-score, and ROC-AUC.
- **Model Selection & Saving**: Select the best-performing model and save it as `result_model.pkl` for future use.

## Dataset Information

- **employee_data.csv**: Contains employee records with features such as age, department, education, job role, satisfaction levels, salary, years at company, and attrition status.
- **Features include**:
  - EmployeeId, Attrition, Age, BusinessTravel, DailyRate, Department, DistanceFromHome, Education, EducationField, EnvironmentSatisfaction, Gender, HourlyRate, JobInvolvement, JobLevel, JobRole, JobSatisfaction, MaritalStatus, MonthlyIncome, MonthlyRate, NumCompaniesWorked, Over18, OverTime, PercentSalaryHike, PerformanceRating, RelationshipSatisfaction, StandardHours, StockOptionLevel, TotalWorkingYears, TrainingTimesLastYear, WorkLifeBalance, YearsAtCompany, YearsInCurrentRole, YearsSinceLastPromotion, YearsWithCurrManager.

## Author

- Wildan Fadhil Nazaruddin
- Email: wildanfadhil76@gmail.com

---
Feel free to explore, modify, and extend the project for your own analysis or business needs!