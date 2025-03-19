import os
import requests

# API URL
url = "https://genai-project-aikv.onrender.com/generate-slide"

# Define topic and country
topic = "Technology"
country = "Germany"

# JSON payload
data = {"topic": topic, "country": country}

# Send POST request to API
response = requests.post(url, json=data)

if response.status_code == 200:
    # ✅ Ensure the 'slides/' directory exists
    slides_dir = "slides"
    if not os.path.exists(slides_dir):
        os.makedirs(slides_dir)

    # ✅ Save the file using "<Topic>_<Country>.pptx" format
    file_name = f"{topic}_{country}.pptx"
    file_path = os.path.join(slides_dir, file_name)

    with open(file_path, "wb") as file:
        file.write(response.content)

    print(f"✅ Slide downloaded successfully as: {file_path}")
else:
    print("❌ Error:", response.status_code, response.text)
