import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import mysql.connector
from src.db.db_config import db_config
from sqlalchemy import create_engine
import joblib

# Create an SQLAlchemy engine
engine = create_engine(f"mysql+mysqlconnector://{db_config['user']}:{db_config['password']}@{db_config['host']}/{db_config['database']}")

# Define a SQL query to fetch item data
sql_query = "SELECT * FROM destinations"

# Load data from the MySQL database into a Pandas DataFrame
df = pd.read_sql(sql_query, con=engine)

# Close the SQLAlchemy engine connection
engine.dispose()

# Combine relevant columns into a single feature column
df['combined_features'] = df['label'] + ' ' + df['rating'].astype(str) + ' ' + df['location'] + ' ' + df['description']

# Create a TF-IDF vectorizer
tfidf_vectorizer = TfidfVectorizer(stop_words='english')

# Compute TF-IDF matrix
tfidf_matrix = tfidf_vectorizer.fit_transform(df['combined_features'])

# Compute cosine similarity between items based on TF-IDF vectors
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

# Function to recommend items based on item name
def get_recommendations(item_name, cosine_sim=cosine_sim):
    # Convert user input to lowercase
    item_name = item_name.lower()

    # Check if the item name exists in the DataFrame
    if item_name not in df['name'].str.lower().values:
        return []

    # Get the index of the item that matches the item_name
    idx = df[df['name'].str.lower() == item_name].index[0]

    # Get the pairwise similarity scores of all items with the given item
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Sort the items based on similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the top 5 most similar items (excluding itself)
    sim_scores = sim_scores[1:6]

    # Get the item indices
    item_indices = [i[0] for i in sim_scores]

    # Return the top 5 recommended item names
    return df['name'].iloc[item_indices]

# Save the TF-IDF vectorizer, TF-IDF matrix, and cosine similarity matrix
joblib.dump(tfidf_vectorizer, 'tfidf_vectorizer.pkl')
joblib.dump(tfidf_matrix, 'tfidf_matrix.pkl')
joblib.dump(cosine_sim, 'cosine_similarity.pkl')

# Interactive user input
user_input = input("Enter an destination name: ")
recommended_items = get_recommendations(user_input)

if not recommended_items.empty:
    print("Recommended Destinations:")
    print(recommended_items)
else:
    print("Destination not found.")