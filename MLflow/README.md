# Sentiment Analysis with MLflow Tracking

For this exercise I've taken used the NLP module assignment from the KeepCoding AI Bootcamp. You can find the original NLP lab repository [here](https://github.com/syllerim/nlp-lab).

The goal of this assignment is to implement a full sentiment analysis pipeline with MLflow tracking to monitor experimentation, metrics, and artifacts.

---

## 📌 Project Overview

I use a dataset of Amazon Software product reviews (binary sentiment: positive or negative), apply TF-IDF vectorization, and train different classifiers.
The idea is to integrate proper ML experiment tracking using **MLflow**.

---

## ⚙️ Pipeline Summary

- **Preprocessing**
  - Tokenization and text cleaning
  - TF-IDF Vectorizer with `ngram_range=(1,2)`, `max_features=3000`

- **Model Training**
  - `LogisticRegression` (manual hyperparameter sweep over `C`)
  - `MultinomialNB` (manual sweep over `alpha`)
  
- **Evaluation**
  - Accuracy, Precision, Recall, F1-score
  - Confusion matrix + classification report
  - All metrics logged to MLflow

- **Tracking with MLflow**
  - Each run tracked using `mlflow.start_run(...)`
  - Metrics, parameters, artifacts (CSV, plots) saved
  - Best models registered and loaded via the MLflow Model Registry

---

## 📁 Artifacts Logged

- `cv_results.csv`: from GridSearch that I used to start playing around with
- `idf_scores.csv` & `idf_scores.png`: visualization of TF-IDF scores from GridSearch that I used to start playing around with
- `confusion_matrix.png`: model evaluation heatmap
- `classification_report.txt`: metrics by class

---

## ✅ Final Models

Both `LogisticRegression` and `MultinomialNB` best models were tracked and registered. One model was promoted to `Production`.

---

## 🔍 Screenshots

![Screenshot 1](https://github.com/syllerim/mlops-llmops-lab/blob/main/MLflow/Screenshoots/1.png?raw=true)  
![Screenshot 2](https://github.com/syllerim/mlops-llmops-lab/blob/main/MLflow/Screenshoots/2.png?raw=true)  
![Screenshot 3](https://github.com/syllerim/mlops-llmops-lab/blob/main/MLflow/Screenshoots/3.png?raw=true)  
![Screenshot 4](https://github.com/syllerim/mlops-llmops-lab/blob/main/MLflow/Screenshoots/4.png?raw=true)  
![Screenshot 5](https://github.com/syllerim/mlops-llmops-lab/blob/main/MLflow/Screenshoots/5.png?raw=true)  
![Screenshot 6](https://github.com/syllerim/mlops-llmops-lab/blob/main/MLflow/Screenshoots/6.png?raw=true)  
![Screenshot 7](https://github.com/syllerim/mlops-llmops-lab/blob/main/MLflow/Screenshoots/7.png?raw=true)  
![Screenshot 8](https://github.com/syllerim/mlops-llmops-lab/blob/main/MLflow/Screenshoots/8.png?raw=true)  
![Screenshot 9](https://github.com/syllerim/mlops-llmops-lab/blob/main/MLflow/Screenshoots/9.png?raw=true)  
![Screenshot 10](https://github.com/syllerim/mlops-llmops-lab/blob/main/MLflow/Screenshoots/10.png?raw=true)  
![Screenshot 11](https://github.com/syllerim/mlops-llmops-lab/blob/main/MLflow/Screenshoots/11.png?raw=true)  
![Screenshot 12](https://github.com/syllerim/mlops-llmops-lab/blob/main/MLflow/Screenshoots/12.png?raw=true)  
![Screenshot 13](https://github.com/syllerim/mlops-llmops-lab/blob/main/MLflow/Screenshoots/13.png?raw=true)  
![Screenshot 14](https://github.com/syllerim/mlops-llmops-lab/blob/main/MLflow/Screenshoots/14.png?raw=true)  
![Screenshot 15](https://github.com/syllerim/mlops-llmops-lab/blob/main/MLflow/Screenshoots/15.png?raw=true)  
![Screenshot 16](https://github.com/syllerim/mlops-llmops-lab/blob/main/MLflow/Screenshoots/16.png?raw=true)  
![Screenshot 17](https://github.com/syllerim/mlops-llmops-lab/blob/main/MLflow/Screenshoots/17.png?raw=true)  
![Screenshot 18](https://github.com/syllerim/mlops-llmops-lab/blob/main/MLflow/Screenshoots/18.png?raw=true)  
![Screenshot 19](https://github.com/syllerim/mlops-llmops-lab/blob/main/MLflow/Screenshoots/19.png?raw=true)  
