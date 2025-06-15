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
