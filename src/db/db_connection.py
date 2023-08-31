import mysql.connector

def establish_connection():
    # Define the database configuration
    db_config = {
        "host": "localhost",
        "user": "root",
        "password": "Sql1password#",
        "database": "bali_destination",
    }

    # Establish a database connection
    connection = mysql.connector.connect(**db_config)
    return connection

def create_cursor(connection):
    # Create a cursor
    cursor = connection.cursor()
    return cursor

def create_destination_table(cursor):
    # Define the table structure (CREATE TABLE)
    create_table_query = """
    CREATE TABLE IF NOT EXISTS destinations (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        label VARCHAR(255),
        rating DECIMAL(3, 2),
        num_reviews INT,
        description TEXT,
        location VARCHAR(255)
    )
    """
    cursor.execute(create_table_query)

def insert_destination_data(cursor, data):
    # Insert data into the table (INSERT INTO)
    insert_query = """
    INSERT INTO destinations (name, label, rating, num_reviews, description, location)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    values = (
        data['Name'],
        data['Label'],
        data['Rating'],
        data['Number of Reviews'],
        data['Description'],
        data['Location']
    )
    cursor.execute(insert_query, values)
