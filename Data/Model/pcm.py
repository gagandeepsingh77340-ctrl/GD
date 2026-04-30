import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

data = pd.read_csv("Data\Excel_File\PCM_Students_Career_Data.csv")

print("Dataset Preview:")
print(data.head())

# Step 2: Check for missing values
print("\nMissing Values:")
print(data.isnull().sum())

if data['Future_Career'].dtype == 'object':
    le = LabelEncoder()
    data['Future_Career'] = le.fit_transform(data['Future_Career'])

X = data[['Physics', 'Chemistry', 'Maths']]
y = data['Future_Career']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train_scaled, y_train)

y_pred = knn.predict(X_test_scaled)

# print("\nAccuracy:", accuracy_score(y_test, y_pred))
# print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
# print("\nClassification Report:\n", classification_report(y_test, y_pred))

print("\n--- Predict Future Career for New Student ---")
new_student = [[85, 78, 90]]  
new_student_scaled = scaler.transform(new_student)
predicted_career = le.inverse_transform(knn.predict(new_student_scaled))
print("Predicted Career:", predicted_career[0])

import pickle
pickle.dump(knn,open("student_stream_PCM_model.sav","wb"))
pickle.dump(le, open("label_encoder_PCM.sav", "wb"))
print("\n💾 Model Saved as student_stream_model.pkl")