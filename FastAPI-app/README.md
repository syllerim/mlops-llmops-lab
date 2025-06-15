# 🚀 FastAPI

The objective of this exercise is to create a FastAPI application:

## 📸 Screenshots

The `Screenshots/` folder contains all the required evidence:

1. 📄 Screenshot of the **FastAPI UI (/docs)** displaying at least 5 modules.
2. 📥 Screenshot of **each module's response**.
3. 🌐 Screenshot of **each module called via HTTPS** (curl).
4. 🧾 All code used during the process.


## 📁 Project Structure
```bash
.
├── Dockerfile
├── main.py                
├── models.py              
├── requirements.txt       
├── README.md
└── Screenshots/
    ├── 1.png
    ├── 2.png
    └── ...           
└── Screenshots_Deployment/
    ├── 1.png
    ├── 2.png
    └── ...
```

## ⚙️ Running the App Locally

Make sure you have Python 3.10+ and install the dependencies:

```bash
pip install -r requirements.txt
```

Then run the FastAPI server:

```bash
uvicorn main:app --reload
```

Access the docs at 👉 http://127.0.0.1:8000/docs

### 📸 Screenshots

![Screenshot 1](https://github.com/syllerim/mlops-llmops-lab/blob/main/FastAPI-app/Screenshots/1.all_endpoints.png?raw=true)
![Screenshot 2](https://github.com/syllerim/mlops-llmops-lab/blob/main/FastAPI-app/Screenshots/2.reverse_name_get.png?raw=true)
![Screenshot 3](https://github.com/syllerim/mlops-llmops-lab/blob/main/FastAPI-app/Screenshots/3.user_life_stats_post.png?raw=true)
![Screenshot 4](https://github.com/syllerim/mlops-llmops-lab/blob/main/FastAPI-app/Screenshots/4.read_dataframe_get.png?raw=true)
![Screenshot 5](https://github.com/syllerim/mlops-llmops-lab/blob/main/FastAPI-app/Screenshots/5.read_dataframe_postition_get.png?raw=true)
![Screenshot 6](https://github.com/syllerim/mlops-llmops-lab/blob/main/FastAPI-app/Screenshots/6.sentiment_classifier_get.png?raw=true)
![Screenshot 7](https://github.com/syllerim/mlops-llmops-lab/blob/main/FastAPI-app/Screenshots/7.text_summarizer_get.png?raw=true)
![Screenshot 8](https://github.com/syllerim/mlops-llmops-lab/blob/main/FastAPI-app/Screenshots/8.https_calls_1.png?raw=true)
![Screenshot 9](https://github.com/syllerim/mlops-llmops-lab/blob/main/FastAPI-app/Screenshots/9.https_calls_2.png?raw=true)
