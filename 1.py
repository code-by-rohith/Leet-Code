import matplotlib.pyplot as plt
import streamlit as st

st.title("Custom Marks Distribution Plot")

subjects = st.text_input("Enter subjects (comma-separated):")
subjects = [subject.strip() for subject in subjects.split(',')]

names = st.text_input("Enter names (comma-separated):")
names = [name.strip() for name in names.split(',')]

marks = {}

for name in names:
    st.write(f"Enter marks for {name}:")
    marks[name] = [st.number_input(f"{subject}:", min_value=0, max_value=100, value=0) for subject in subjects]

if st.button('Generate Plot'):
    fig, ax = plt.subplots(figsize=(12, 8))

    for name in names:
        ax.plot(subjects, marks[name], label=name, marker='o')

    ax.set_title('Marks Distribution')
    ax.set_xlabel('Subjects')
    ax.set_ylabel('Marks')
    ax.legend()
    ax.grid(True)

    st.pyplot(fig)
