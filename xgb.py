import numpy
import xlrd
import xgboost
from sklearn.metrics import accuracy_score

# load data
file = xlrd.open_workbook("clinical.xls")
sheet = file.sheet_by_index(0)
dataset_age = []
dataset_days = []
test_age = []
test_days = []
age = []
days = []
row_number = sheet.nrows
if row_number > 0:
        for row in range(0, row_number):
            if sheet.row(row)[3] != "--" and sheet.row(row)[9] != "--":
                dataset_age.append(sheet.row(row)[3])
                dataset_days.append(sheet.row(row)[9])
                if sheet.row(row)[3] != "--" and sheet.row(row)[9] == "--":
                    test_age.append(sheet.row(row)[3])

#sprint('\n'.join(dataset_age))

age = ','.join(map(str, dataset_age))
days = ','.join(map(str, dataset_days))
model = xgboost.XGBClassifier()
model.fit(dataset_age, dataset_days)
predict = model.predict(test_age)
predictions = [round(value) for value in predict]
print(predictions)
