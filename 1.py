import streamlit as st
import matplotlib.pyplot as plt
import numpy as np


st.title("Enhanced Plot Example")


x = np.linspace(0, 10, 100)
y_sin = np.sin(x)
y_cos = np.cos(x)

fig, ax = plt.subplots(figsize=(8, 6))


ax.plot(x, y_sin, label='sin(x)', color='blue', linestyle='-', linewidth=2, marker='o', markersize=5, markerfacecolor='red', markeredgewidth=2)


ax.plot(x, y_cos, label='cos(x)', color='green', linestyle='--', linewidth=2, marker='s', markersize=5, markerfacecolor='yellow', markeredgewidth=2)


ax.grid(True, which='both', linestyle='--', linewidth=0.7)

# Customize axes and title
ax.set_xlabel('X-axis', fontsize=12, fontweight='bold', color='darkblue')
ax.set_ylabel('Y-axis', fontsize=12, fontweight='bold', color='darkblue')
ax.set_title('Sine & Cosine Waves', fontsize=16, fontweight='bold', color='purple')

ax.set_xlim([0, 10])
ax.set_ylim([-1.5, 1.5])
ax.xaxis.set_ticks(np.arange(0, 11, 1))
ax.yaxis.set_ticks(np.arange(-1.5, 1.6, 0.5))


ax.legend(loc='upper right', fontsize=12)


st.pyplot(fig)
