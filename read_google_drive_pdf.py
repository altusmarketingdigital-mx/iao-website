import requests
import io
import PyPDF2

url = 'https://drive.google.com/uc?export=download&id=1RFoB0f-3ajXQx3hTKqKUTGwSt4BAdNZg'

try:
    response = requests.get(url)
    if response.status_code == 200:
        pdf_file = io.BytesIO(response.content)
        reader = PyPDF2.PdfReader(pdf_file)
        text = ''
        for page in reader.pages:
            text += page.extract_text() + '\n'
        print(text)
    else:
        print(f"Failed to download. Status code: {response.status_code}")
except Exception as e:
    print(f"Error: {e}")
