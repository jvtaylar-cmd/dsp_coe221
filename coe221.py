import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Title
st.title("Aliasing Demonstration")

# Sidebar inputs
st.sidebar.header("Signal Parameters")
f_signal = st.sidebar.slider("Signal Frequency (Hz)", min_value=1, max_value=100, value=10)
f_sample = st.sidebar.slider("Sampling Rate (Hz)", min_value=5, max_value=200, value=30)
duration = st.sidebar.slider("Signal Duration (seconds)", min_value=0.1, max_value=2.0, value=1.0)

# Generate time values
t_continuous = np.linspace(0, duration, 1000)  # Continuous-time (for plotting)
t_sampled = np.arange(0, duration, 1/f_sample)  # Discrete sampling instants

# Signal (sine wave)
signal_continuous = np.sin(2 * np.pi * f_signal * t_continuous)
signal_sampled = np.sin(2 * np.pi * f_signal * t_sampled)

# Plotting
fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(t_continuous, signal_continuous, label="Continuous Signal", color='blue')
ax.stem(t_sampled, signal_sampled, linefmt='r-', markerfmt='ro', basefmt='gray', label="Sampled Signal")
ax.set_xlabel("Time (s)")
ax.set_ylabel("Amplitude")
ax.set_title("Signal vs Sampled Signal")
ax.legend()
ax.grid(True)

# Show the plot
st.pyplot(fig)

# Nyquist warning
if f_sample < 2 * f_signal:
    st.warning("⚠️ Aliasing occurs! The sampling rate is below the Nyquist rate (2 × signal frequency).")
else:
    st.success("✅ Sampling rate satisfies the Nyquist criterion.")
