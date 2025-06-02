🌎 Real-Time Disaster Impact Estimation Tool

This Streamlit application allows users to analyze real-time disaster reports with both text and image inputs to:

🧠 Detect sentiment of the report

🖼️ Generate image captions and tags

⚠️ Estimate urgency level of the situation


Supports disaster types like floods, fires, earthquakes, and cyclones.


---

🚀 Run Locally (with pip)

1. Clone the repository (or download and unzip it):



git clone https://github.com/NBSUJITA04/project.git
cd sample-main

2. Install the required packages using pip:



pip install -r requirements.txt

3. Run the Streamlit app:



streamlit run app.py


---

📦 Requirements

Install dependencies from requirements.txt, which includes:

streamlit
pandas
Pillow


---

🧠 Features

📝 Text Sentiment Analysis (basic keyword-based approach)

🖼️ Image Analysis: caption + tag simulation

⚠️ Urgency Estimator based on text + image interpretation

📊 CSV Logging of input and output for future analysis



---

📁 Project Structure

sample-main/
├── app.py # Main Streamlit app
├── text_analysis.py # Text sentiment analysis logic
├── image_analysis.py # Simulated image captioning and tagging
├── urgency_estimator.py # Urgency level computation
├── disaster_data_sample.csv# Sample output
├── requirements.txt # pip dependencies
├── Architecture diagram.png# High-level system design
├── banner.png # Banner for the UI
├── power bi report.png # Optional reporting output
└── README.md # Project documentation


---

📝 Output Format

The app logs results to a CSV file with the following columns:


Disaster Type

Sentiment

Image Tags

Urgency Level



---

📌 Notes

Image analysis is simulated; you can replace it with a real ML model.

The project is modular
---
