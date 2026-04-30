import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

df = pd.read_csv("Data\Excel_File\Arts_Students_Career_Data.csv") 

print(df.head())

X = df[["History", "Political_Science", "English"]]  
y = df["Future_Career"]                                

le = LabelEncoder()
y_encoded = le.fit_transform(y)

X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print(f"\n🎯 Model Accuracy: {accuracy * 100:.2f}%\n")
print("📊 Classification Report:")
print(classification_report(y_test, y_pred, target_names=le.classes_))

new_student = pd.DataFrame({"History": [90],"Political_Science": [85],"English": [92]})

predicted_career = le.inverse_transform(model.predict(new_student))[0]
print(f"\n🧠 Predicted Career for new student: {predicted_career}")

import pickle
pickle.dump(model,open("student_stream_Arts_model.sav","wb"))
pickle.dump(le, open("label_encoder_Arts.sav", "wb"))
print("\n💾 Model Saved as student_stream_model.sav")