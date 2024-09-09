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

# Button to generate the plot
if st.button('Generate Plot'):
    fig, axs = plt.subplots(2, 2, figsize=(12, 10))

    for i, name in enumerate(names):
        row = i // 2
        col = i % 2
        axs[row, col].bar(subjects, marks[name])
        axs[row, col].set_title(name)
        axs[row, col].set_xlabel('Subjects')
        axs[row, col].set_ylabel('Marks')
        axs[row, col].grid(True)

    plt.tight_layout()

    st.pyplot(fig)
