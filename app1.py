import streamlit as st
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

# Nhập giá trị từ người dùng
st.title("🚀 Rocket Motion Simulation")
m0 = st.slider("Initial Mass m0 (kg)", 1.0, 100.0, 50.0)
y0 = st.slider("Initial Position y0 (m)", 0.0, 500.0, 0.0)
v0 = st.slider("Ejection Velocity v0 (m/s)", 0.1, 100.0, 10.0)
k = st.slider("Burn Rate k (kg/s)", 0.1, 10.0, 1.0)

if st.button("Calculate"):
    g = 9.81
    t = sp.symbols('t')
    v = v0 * sp.ln(m0 / (m0 - k*t)) - g * t
    a = sp.diff(v, t)
    y = y0 + sp.integrate(v, t)

    fuel_end = m0 / k

    st.markdown("### 📋 Output")
    st.write(f"Acceleration a(t): `{sp.simplify(a)}`")
    st.write(f"Position y(t): `{sp.simplify(y)}`")
    st.write(f"Fuel ends at: `{fuel_end:.2f}` seconds")

    y_func = sp.lambdify(t, y, "numpy")
    t_vals = np.linspace(0.01, float(fuel_end), 300)
    y_vals = y_func(t_vals)

    st.markdown("### 📈 Height vs Time Graph")
    fig, ax = plt.subplots()
    ax.plot(t_vals, y_vals)
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Height (m)")
    ax.set_title("Rocket Motion")
    ax.grid(True)
    st.pyplot(fig)
