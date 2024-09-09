import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

names = ['Abhishek', 'Sandeep', 'Vikas', 'Viswa']
num_companies = 10
companies = [f'Company {i+1}' for i in range(num_companies)]


np.random.seed(0)
chances = np.random.rand(len(names), num_companies)


chances[1] += 0.5

chances[2] += 0.2
chances = np.clip(chances / chances.max(), 0, 1)

fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(companies, chances[0], marker='o', label=names[0])
ax.plot(companies, chances[1], marker='o', label=names[1])
ax.plot(companies, chances[2], marker='o', label=names[2])
ax.plot(companies, chances[3], marker='o', label=names[3])

ax.set_xlabel('Companies')
ax.set_ylabel('Chance of Placement')
ax.set_title('Placement Chances for Different People in Various Companies')
ax.legend(loc='best')
ax.grid(True)
st.title("Placement Chances Visualization")
st.pyplot(fig)
