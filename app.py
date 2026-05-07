import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="FlowState Dashboard",
    layout="wide"
)

# -----------------------------
# LOAD DATASET
# -----------------------------
df = pd.read_csv("datasets/train.csv")

# Remove missing values
df.dropna(inplace=True)

# -----------------------------
# TITLE
# -----------------------------
st.title("FlowState — Productivity Analytics Dashboard")

st.markdown(
    "Analyze employee burnout trends, workload patterns, and productivity indicators."
)

# -----------------------------
# KPI METRICS
# -----------------------------
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="Average Burn Rate",
        value=round(df["Burn Rate"].mean(), 2)
    )

with col2:
    st.metric(
        label="Maximum Burn Rate",
        value=round(df["Burn Rate"].max(), 2)
    )

with col3:
    st.metric(
        label="Average Fatigue Score",
        value=round(df["Mental Fatigue Score"].mean(), 2)
    )

# -----------------------------
# DATASET PREVIEW
# -----------------------------
st.subheader("Dataset Preview")

st.write(df.head())

# -----------------------------
# BURN RATE DISTRIBUTION
# -----------------------------
st.subheader("Burn Rate Distribution")

fig1, ax1 = plt.subplots(figsize=(8,5))

sns.histplot(
    df["Burn Rate"],
    bins=30,
    kde=True,
    ax=ax1
)

ax1.set_title("Burn Rate Distribution")

st.pyplot(fig1)

# -----------------------------
# FATIGUE VS BURN RATE
# -----------------------------
st.subheader("Mental Fatigue vs Burn Rate")

fig2, ax2 = plt.subplots(figsize=(8,5))

sns.scatterplot(
    x=df["Mental Fatigue Score"],
    y=df["Burn Rate"],
    ax=ax2
)

ax2.set_title("Mental Fatigue vs Burn Rate")

st.pyplot(fig2)

# -----------------------------
# RESOURCE ALLOCATION VS BURN RATE
# -----------------------------
st.subheader("Resource Allocation vs Burn Rate")

fig3, ax3 = plt.subplots(figsize=(8,5))

sns.scatterplot(
    x=df["Resource Allocation"],
    y=df["Burn Rate"],
    ax=ax3
)

ax3.set_title("Resource Allocation vs Burn Rate")

st.pyplot(fig3)

# -----------------------------
# HEATMAP
# -----------------------------
st.subheader("Feature Correlation Heatmap")

fig4, ax4 = plt.subplots(figsize=(8,5))

sns.heatmap(
    df.corr(numeric_only=True),
    annot=True,
    cmap="coolwarm",
    ax=ax4
)

st.pyplot(fig4)

# -----------------------------
# BURNOUT ESTIMATION
# -----------------------------
st.subheader("Burnout Risk Estimation")

fatigue = st.slider(
    "Mental Fatigue Score",
    0.0,
    10.0,
    5.0
)

resource = st.slider(
    "Resource Allocation",
    0.0,
    10.0,
    5.0
)

# Formula-based burnout estimation
burnout_score = (
    fatigue * 0.6
    +
    resource * 0.4
)

# -----------------------------
# PREDICTION OUTPUT
# -----------------------------
st.metric(
    label="Estimated Burnout Score",
    value=round(burnout_score, 2)
)

# -----------------------------
# RISK CLASSIFICATION
# -----------------------------
if burnout_score < 3:
    risk = "Low"

elif burnout_score < 6:
    risk = "Medium"

else:
    risk = "High"

# -----------------------------
# RISK DISPLAY
# -----------------------------
if risk == "Low":
    st.success("Low Burnout Risk")

elif risk == "Medium":
    st.warning("Medium Burnout Risk")

else:
    st.error("High Burnout Risk")

# -----------------------------
# RECOMMENDATIONS
# -----------------------------
st.subheader("Recommendations")

if risk == "High":
    st.warning(
        """
        High burnout risk detected.

        Recommendations:
        - Reduce workload
        - Improve work-life balance
        - Increase rest periods
        - Encourage wellness programs
        """
    )

elif risk == "Medium":
    st.info(
        """
        Moderate burnout risk detected.

        Recommendations:
        - Maintain healthy work routines
        - Monitor stress levels
        - Take regular breaks
        """
    )

else:
    st.success(
        """
        Healthy productivity levels detected.

        Recommendations:
        - Maintain current work habits
        - Continue healthy scheduling
        """
    )

# -----------------------------
# FOOTER
# -----------------------------
st.markdown("---")

st.caption("FlowState — Productivity Analytics Dashboard")