import pickle
import pandas as pd

# 1. Load model
with open('model/result_model.pkl', 'rb') as file:
    model = pickle.load(file)

# 2. Daftar kolom sesuai training (ganti dengan urutan kolom df_model Anda)
kolom_training = [
    'Age', 'BusinessTravel', 'Department', 'DistanceFromHome', 'Education', 'EducationField',
    'EnvironmentSatisfaction', 'Gender', 'HourlyRate', 'JobInvolvement', 'JobLevel', 'JobRole',
    'JobSatisfaction', 'MaritalStatus', 'MonthlyIncome', 'MonthlyRate', 'NumCompaniesWorked',
    'Over18', 'OverTime', 'PercentSalaryHike', 'PerformanceRating', 'RelationshipSatisfaction',
    'StandardHours', 'StockOptionLevel', 'TotalWorkingYears', 'TrainingTimesLastYear',
    'WorkLifeBalance', 'YearsAtCompany', 'YearsInCurrentRole', 'YearsSinceLastPromotion',
    'YearsWithCurrManager', 'DailyRate', 'EmployeeCount'
]

# 3. Data baru (isi semua kolom di atas, urutan dan nama harus sama)
data_baru = pd.DataFrame([{
    'Age': 35,
    'BusinessTravel': 1,
    'DailyRate': 800,
    'Department': 1,
    'DistanceFromHome': 5,
    'Education': 3,
    'EducationField': 1,
    'EnvironmentSatisfaction': 3,
    'Gender': 1,
    'HourlyRate': 60,
    'JobInvolvement': 3,
    'JobLevel': 2,
    'JobRole': 2,
    'JobSatisfaction': 4,
    'MaritalStatus': 2,
    'MonthlyIncome': 5000,
    'MonthlyRate': 14000,
    'NumCompaniesWorked': 2,
    'OverTime': 0,
    'PercentSalaryHike': 13,
    'PerformanceRating': 3,
    'RelationshipSatisfaction': 3,
    'StockOptionLevel': 1,
    'TotalWorkingYears': 10,
    'TrainingTimesLastYear': 3,
    'WorkLifeBalance': 3,
    'YearsAtCompany': 5,
    'YearsInCurrentRole': 2,
    'YearsSinceLastPromotion': 1,
    'YearsWithCurrManager': 2
}])[[
    'Age', 'BusinessTravel', 'DailyRate', 'Department', 'DistanceFromHome', 'Education',
    'EducationField', 'EnvironmentSatisfaction', 'Gender', 'HourlyRate', 'JobInvolvement',
    'JobLevel', 'JobRole', 'JobSatisfaction', 'MaritalStatus', 'MonthlyIncome', 'MonthlyRate',
    'NumCompaniesWorked', 'OverTime', 'PercentSalaryHike', 'PerformanceRating',
    'RelationshipSatisfaction', 'StockOptionLevel', 'TotalWorkingYears',
    'TrainingTimesLastYear', 'WorkLifeBalance', 'YearsAtCompany', 'YearsInCurrentRole',
    'YearsSinceLastPromotion', 'YearsWithCurrManager'
]]

hasil = model.predict(data_baru)
print("Hasil prediksi (0=tidak keluar, 1=keluar):", hasil[0])

# 4. Prediksi
hasil = model.predict(data_baru)
print("Hasil prediksi (0=tidak keluar, 1=keluar):", hasil[0])