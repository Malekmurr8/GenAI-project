import requests

url = "https://genai-project-aikv.onrender.com/generate-slide"  # Your actual Render URL
data = {"topic": "Technology", "country": "Germany"}

response = requests.post(url, json=data)

print("Status Code:", response.status_code)
print("Response:", response.json())  # Should return a success message or file
