import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

names = ['Abhishek', 'Sandeep', 'Vikas', 'Viswa']
subjects = ['Math', 'Physics', 'Chemistry', 'Biology', 'English']
num_subjects = len(subjects)

np.random.seed(0)
marks = {
    name: np.random.randint(50, 100, num_subjects) for name in names
}

fig, axs = plt.subplots(2, 2, figsize=(12, 10))

axs[0, 0].bar(subjects, marks['Abhishek'])
axs[0, 0].set_title('Abhishek')
axs[0, 0].set_xlabel('Subjects')
axs[0, 0].set_ylabel('Marks')
axs[0, 0].grid(True)

axs[0, 1].bar(subjects, marks['Sandeep'])
axs[0, 1].set_title('Sandeep')
axs[0, 1].set_xlabel('Subjects')
axs[0, 1].set_ylabel('Marks')
axs[0, 1].grid(True)

axs[1, 0].bar(subjects, marks['Vikas'])
axs[1, 0].set_title('Vikas')
axs[1, 0].set_xlabel('Subjects')
axs[1, 0].set_ylabel('Marks')
axs[1, 0].grid(True)

axs[1, 1].bar(subjects, marks['Viswa'])
axs[1, 1].set_title('Viswa')
axs[1, 1].set_xlabel('Subjects')
axs[1, 1].set_ylabel('Marks')
axs[1, 1].grid(True)

plt.tight_layout()

st.title("Marks Distribution for Four People")
st.pyplot(fig)
