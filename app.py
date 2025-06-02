import streamlit as st
import pandas as pd
from datetime import datetime
import os

# Safely import analysis modules
try:
    from text_analysis import analyze_text
except ImportError:
    analyze_text = None

try:
    from image_analysis import analyze_image
except ImportError:
    analyze_image = None

try:
    from urgency_estimator import estimate_urgency
except ImportError:
    estimate_urgency = None

# Streamlit UI
st.title("🌍 Real-Time Disaster Impact Estimation Tool")
st.markdown("Upload a disaster report (text + image) to analyze its impact in real-time.")

# Inputs
disaster_type = st.selectbox("Select Disaster Type", ["Flood", "Fire", "Earthquake", "Cyclone"])
location = st.text_input("Enter Location")
text_input = st.text_area("Disaster Description")
image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

# Analyze
if st.button("Analyze"):
    if not (text_input.strip() and location.strip() and image):
        st.warning("Please fill in all fields: text, location, and image.")
    elif not (analyze_text and analyze_image and estimate_urgency):
        st.error("One or more analysis modules failed to load.")
    else:
        # Run analysis
        score, label = analyze_text(text_input)
        caption, tags = analyze_image(image)
        urgency = estimate_urgency(label, tags)

        # Show results
        st.success(f"Sentiment: {label} ({score})")
        st.info(f"Image Caption: {caption}")
        st.error(f"Urgency Level: {urgency}")

        # Optional: Save to CSV
        csv_path = "data/disaster_data.csv"
        os.makedirs(os.path.dirname(csv_path), exist_ok=True)
        write_header = not os.path.exists(csv_path)

        row = [
            datetime.now().isoformat(),
            location,
            disaster_type,
            text_input.replace(",", " "),
            label,
            ', '.join(tags),
            caption,
            urgency
        ]

        with open(csv_path, "a") as f:
            if write_header:
                f.write("Timestamp,Location,Disaster Type,Text,Sentiment,Image Tags,Caption,Urgency\n")
            f.write(','.join(map(str, row)) + "\n")
