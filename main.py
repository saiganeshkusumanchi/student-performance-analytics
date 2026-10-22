import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv("data.csv")

print("Dataset:")
print(df)

print("\nDataset Information:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())

print("\nMissing Values:")
print(df.isnull().sum())
print("\nAverage Marks:")
print(df[["Python", "Maths", "AI"]].mean())

print("\nTop 5 Students:")
df["Total"] = df[["Python", "Maths", "AI"]].sum(axis=1)
print(df.nlargest(5, "Total")[["Name", "Total"]])

print("\nDepartment-wise Average:")
print(df.groupby("Department")[["Python", "Maths", "AI"]].mean())
# Average Marks
print("\nAverage Marks:")
print(df[["Python", "Maths", "AI"]].mean())

# Calculate Total Marks
df["Total"] = df[["Python", "Maths", "AI"]].sum(axis=1)

# Calculate Percentage
df["Percentage"] = df["Total"] / 3

# Display Top 5 Students
print("\nTop 5 Students:")
print(df.nlargest(5, "Total")[["Name", "Total", "Percentage"]])

# Save Analyzed Data
df.to_csv("analyzed_data.csv", index=False)

print("\nAnalyzed data saved successfully!")
# Subject-wise Average Marks Graph
subject_avg = df[["Python", "Maths", "AI"]].mean()

plt.figure(figsize=(8, 5))
subject_avg.plot(kind="bar")

plt.title("Subject-wise Average Marks")
plt.xlabel("Subjects")
plt.ylabel("Average Marks")
plt.tight_layout()
plt.savefig("subject_average.png")
plt.show()
# Grade and Pass/Fail Analysis

def calculate_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"

df["Average"] = df[["Python", "Maths", "AI"]].mean(axis=1)

df["Grade"] = df["Average"].apply(calculate_grade)

df["Result"] = np.where(
    (df[["Python", "Maths", "AI"]] >= 40).all(axis=1),
    "Pass",
    "Fail"
)

print("\nStudent Grades and Results:")
print(df[["Name", "Average", "Grade", "Result"]])

print("\nPass/Fail Count:")
print(df["Result"].value_counts())
# Highest and Lowest Performance

highest_student = df.loc[df["Average"].idxmax()]
lowest_student = df.loc[df["Average"].idxmin()]

print("\nHighest Performing Student:")
print("Name:", highest_student["Name"])
print("Average:", highest_student["Average"])

print("\nLowest Performing Student:")
print("Name:", lowest_student["Name"])
print("Average:", lowest_student["Average"])

# Overall Class Average
class_average = df["Average"].mean()
print("\nOverall Class Average:", round(class_average, 2))

# Best Performing Subject
subject_avg = df[["Python", "Maths", "AI"]].mean()
best_subject = subject_avg.idxmax()

print("\nSubject-wise Average Marks:")
print(subject_avg)

print("\nBest Performing Subject:", best_subject)
print("Highest Subject Average:", round(subject_avg.max(), 2))
# Save Final Analyzed Dataset

df.to_csv("analyzed_data.csv", index=False)

print("\nFinal Dataset Saved Successfully!")
print("Total Students:", len(df))
print("Total Columns:", len(df.columns))
print("\nFinal Dataset Preview:")
print(df.head())
