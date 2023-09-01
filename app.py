from flask import Flask, render_template, request
from sklearn.metrics.pairwise import linear_kernel
import pandas as pd
import joblib
import mysql.connector
from src.db.db_config import db_config

app = Flask(__name__)

connection = mysql.connector.connect(**db_config)

# Load the data and pickle files
df = pd.read_sql("SELECT * FROM destinations", con=connection)
cosine_similarity_matrix = joblib.load(r'src\model\cosine_similarity.pkl')
tfidf_matrix = joblib.load(r'src\model\tfidf_matrix.pkl')
tfidf_vectorizer = joblib.load(r'src\model\tfidf_vectorizer.pkl')

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
    app.run(debug=True)
