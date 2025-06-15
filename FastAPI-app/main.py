from datetime import datetime
from fastapi import FastAPI
from models import Identity
import pandas as pd

app = FastAPI()

@app.get("/reverse_name")
def root(name: str):
    reversed_name = name[::-1].capitalize()
    return {'Message': f'Hi, {name}, your name reversed is {reversed_name}.'}

@app.post('/user_life_stats')
def user_info(info: Identity):
    birth_date = datetime.strptime(info.date_of_birth, "%d-%m-%Y")
    days_alive = (datetime.now() - birth_date).days
    return {'Message': f'Hi {info.name}  {info.surname}, you have been alive for {days_alive} days.'}

@app.get('/read_dataframe')
def read_dataframe_properties():
    df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")
    value = df["sepal_length"]
    return {'Value': value}

@app.get('/read_dataframe/{position}')
def read_dataframe_properties(position: int):
    df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")
    value = df["sepal_length"][position]
    return {'Value': value}

@app.get('/sentiment_classifier')
def sentiment_classifier(query):
    from transformers import pipeline
    sentiment_pipeline = pipeline("sentiment-analysis")
    return sentiment_pipeline(query)

@app.get('/text_summarizer')
def summarize_text(query: str):
    from transformers import pipeline
    text_summarizer = pipeline("summarization")
    summary = text_summarizer(query, max_length=50, min_length=5, do_sample=False)
    return summary
