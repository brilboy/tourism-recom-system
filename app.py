from flask import Flask, render_template, request
from sklearn.metrics.pairwise import linear_kernel
import pandas as pd
import joblib
import os
#import mysql.connector
#from src.db.db_config import db_config

application = Flask(__name__)

app = application

#connection = mysql.connector.connect(**db_config)

# Get the absolute path
csv_file_path = os.path.join(os.getcwd(), 'src', 'destination_data.csv')
cosine_file_path = os.path.join(os.getcwd(), 'src', 'model', 'cosine_similarity.pkl')
matrix_file_path = os.path.join(os.getcwd(), 'src', 'model', 'tfidf_matrix.pkl')
vectorizer_file_path = os.path.join(os.getcwd(), 'src', 'model', 'tfidf_vectorizer.pkl')

# Load the data and pickle files
#df = pd.read_sql("SELECT * FROM destinations", con=connection)
df = pd.read_csv(csv_file_path)
cosine_similarity_matrix = joblib.load(cosine_file_path)
tfidf_matrix = joblib.load(matrix_file_path)
tfidf_vectorizer = joblib.load(vectorizer_file_path)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Get user input from the form
        keyword = request.form['keyword']

        # Transform the user input into a TF-IDF vector
        keyword_vector = tfidf_vectorizer.transform([keyword])

        # Transform the user input into a TF-IDF vector
        cosine_scores = linear_kernel(keyword_vector, tfidf_matrix).flatten()

        # Get the index of destinations sorted by cosine similarity scores
        sorted_indices = cosine_scores.argsort()[::-1]

        # Get the names of the recommended destinations
        recommendations = [df['name'].iloc[i] for i in sorted_indices[1:6]]
        return render_template('recommendations.html', recommendations=recommendations)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
