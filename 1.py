import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

name = 'Abhishek'
subjects = ['Math', 'Physics', 'Chemistry', 'Biology', 'English']
num_subjects = len(subjects)

# Generate random marks for 5 subjects
np.random.seed(0)  # For reproducibility
marks = np.random.randint(50, 100, num_subjects)

# Create the plot with 4 subplots
fig, axs = plt.subplots(2, 2, figsize=(12, 10))

# First subplot
axs[0, 0].bar(subjects, marks)
axs[0, 0].set_title(f'{name} - Subplot 1')
axs[0, 0].set_xlabel('Subjects')
axs[0, 0].set_ylabel('Marks')
axs[0, 0].grid(True)

# Second subplot with some variation
axs[0, 1].bar(subjects, marks + np.random.randint(-10, 10, num_subjects))
axs[0, 1].set_title(f'{name} - Subplot 2')
axs[0, 1].set_xlabel('Subjects')
axs[0, 1].set_ylabel('Marks')
axs[0, 1].grid(True)

# Third subplot with different variation
axs[1, 0].bar(subjects, marks + np.random.randint(-20, 20, num_subjects))
axs[1, 0].set_title(f'{name} - Subplot 3')
axs[1, 0].set_xlabel('Subjects')
axs[1, 0].set_ylabel('Marks')
axs[1, 0].grid(True)

# Fourth subplot with another variation
axs[1, 1].bar(subjects, marks + np.random.randint(-5, 5, num_subjects))
axs[1, 1].set_title(f'{name} - Subplot 4')
axs[1, 1].set_xlabel('Subjects')
axs[1, 1].set_ylabel('Marks')
axs[1, 1].grid(True)

plt.tight_layout()

# Display the plot in Streamlit
st.title("Marks Distribution Across 4 Subplots")
st.pyplot(fig)
