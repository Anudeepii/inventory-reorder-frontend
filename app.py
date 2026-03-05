import streamlit as st
import pandas as pd
import requests

st.set_page_config(
    page_title="Inventory Reorder Prediction System",
    page_icon="📦",
    layout="wide"
)

# Title
st.title("📦 Inventory Reorder Prediction System")
st.markdown("AI-powered system to monitor material usage and predict reorder needs.")

# Sidebar
st.sidebar.title("Navigation")
menu = st.sidebar.selectbox(
    "Go to",
    ["Dashboard", "Material Entry", "Usage Entry", "Variance Report"]
)

# ---------------- DASHBOARD ----------------
if menu == "Dashboard":

    st.subheader("📊 Inventory Overview")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Materials", "45")
    col2.metric("Low Stock Items", "6")
    col3.metric("Reorder Alerts", "3")
    col4.metric("Monthly Variance", "₹5200")

    st.markdown("---")

    # Dummy data (later backend will replace this)
    data = pd.DataFrame({
        "Material": ["Steel", "Cement", "Bricks", "Sand"],
        "Planned": [100, 200, 500, 300],
        "Actual": [120, 180, 520, 250]
    })

    data["Variance"] = data["Actual"] - data["Planned"]

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Material Usage")
        st.bar_chart(data.set_index("Material")[["Planned", "Actual"]])

    with col2:
        st.subheader("Variance")
        st.bar_chart(data.set_index("Material")["Variance"])

    st.markdown("---")

    st.subheader("📋 Material Table")
    st.dataframe(data, use_container_width=True)

# ---------------- MATERIAL ENTRY ----------------
elif menu == "Material Entry":

    st.subheader("➕ Add Planned Material")

    with st.form("material_form"):

        material = st.text_input("Material Name")
        planned = st.number_input("Planned Quantity", min_value=0)

        submit = st.form_submit_button("Submit")

        if submit:
            payload = {
                "material": material,
                "planned": planned
            }

            # Backend API
            try:
                requests.post("http://127.0.0.1:5000/add_material", json=payload)
                st.success("Material added successfully")
            except:
                st.error("Backend not connected")

# ---------------- USAGE ENTRY ----------------
elif menu == "Usage Entry":

    st.subheader("📥 Add Actual Usage")

    with st.form("usage_form"):

        material = st.text_input("Material Name")
        actual = st.number_input("Actual Quantity Used", min_value=0)

        submit = st.form_submit_button("Submit")

        if submit:
            payload = {
                "material": material,
                "actual": actual
            }

            try:
                requests.post("http://127.0.0.1:5000/add_usage", json=payload)
                st.success("Usage recorded")
            except:
                st.error("Backend not connected")

# ---------------- VARIANCE REPORT ----------------
elif menu == "Variance Report":

    st.subheader("📉 Variance Analysis")

    try:
        response = requests.get("http://127.0.0.1:5000/variance")
        data = pd.DataFrame(response.json())

        st.dataframe(data, use_container_width=True)

        st.bar_chart(data.set_index("material")["variance"])

    except:
        st.warning("Backend API not running")

st.markdown("---")
st.caption("Hackathon Prototype | Streamlit Frontend")