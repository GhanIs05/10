import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Create a random dataset
# np.random.seed(0) # For reproducibility
students = 30
subjects = 5
grades = ['A', 'B', 'C', 'D', 'E', 'F']
data = np.random.choice(grades, size=(students, subjects))
# Create a DataFrame to store the data
df = pd.DataFrame(data, columns=[f'Subject {i+1}' for i in range(subjects)])
# Define grade points
grade_points = {'A': 10, 'B': 9, 'C': 8, 'D': 7, 'E': 6, 'F': 0}
# Calculate GPA for each student
df['GPA'] = df.apply(lambda row: np.mean([grade_points[grade] for grade in row]),
axis=1)
# Calculate pass percentage
pass_percentage = (len(df[df['GPA'] >= 5]) / students) * 100
# Print pass percentage
print(f"Pass Percentage: {pass_percentage:.2f}%")
# Visualize the data
fig, axes = plt.subplots(1, 3, figsize=(18, 6))
# Bar chart
df['Pass'] = df['GPA'] >= 5
pass_fail_counts = df['Pass'].value_counts()
axes[0].bar(pass_fail_counts.index, pass_fail_counts.values)
axes[0].set_title('Pass/Fail Distribution')
axes[0].set_xlabel('Pass/Fail')
axes[0].set_ylabel('Count')
# Pie chart
pass_fail_labels = ['Pass', 'Fail']
axes[1].pie(pass_fail_counts, labels=pass_fail_labels, autopct='%1.1f%%',
startangle=90)
axes[1].set_title('Pass/Fail Percentage')
# Scatter plot
axes[2].scatter(df.index, df['GPA'], c=df['GPA'], cmap='viridis')
axes[2].set_title('Scatter Plot of GPA')
axes[2].set_xlabel('Student')
axes[2].set_ylabel('GPA')
plt.tight_layout()
plt.show()
