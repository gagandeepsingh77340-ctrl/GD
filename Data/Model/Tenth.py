import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report
import pickle

# Load Dataset
df = pd.read_csv("Data\\Raw_Excel_File\\Tenth_Data.csv")   
print("✅ Dataset Loaded Successfully!")
print(df.head())

# Feature selection and target
X = df[['Math', 'Science', 'English', 'Social_Science']]
y = df['Stream']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# Create and train KNN model
model = KNeighborsClassifier(n_neighbors=5)  # You can tune n_neighbors for better accuracy
model.fit(X_train, y_train)

# Evaluate model
y_pred = model.predict(X_test)
print("\n🎯 Model Evaluation:")
print("Accuracy:", round(accuracy_score(y_test, y_pred)*100, 2), "%")
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Predict for a new student
print("\n🔮 Predict Stream for a New Student:")
new_student = [[78, 82, 70, 75]]  # Example marks
predicted_stream = model.predict(new_student)
print("Predicted Stream:", predicted_stream[0])

# Save the trained model
pickle.dump(model, open("student_stream_10th_knn_model.sav", "wb"))
print("\n💾 Model Saved as student_stream_10th_knn_model.sav")