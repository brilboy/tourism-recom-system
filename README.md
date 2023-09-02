# Bali Destination Recommendation System

## General Description

The Bali Destination Recommendation is a web-based application that enhances tourists' experiences by providing personalized recommendations for destinations in Bali, Indonesia. This recommendation system leverages a content-based approach, taking into account user preferences and the descriptions of various Bali destinations.

## Project Overview

The project is designed to assist tourists in discovering and planning their visits to Bali. It aims to recommend destinations that align with their interests and preferences. By analyzing destination descriptions and user-provided keywords, the system suggests the top destinations that match the user's input.

## Key Features

- **Data Scraping**: The system scrapes data from Google Maps, collecting information about various tourist destinations in Bali using Selenium.

- **Database Management**: The scraped data is stored efficiently in a MySQL database, ensuring easy access and retrieval.

- **Content-Based Recommendation**: By creating TF-IDF vectors and utilizing cosine similarity, the system offers personalized recommendations that consider factors such as location, description, labels, ratings, and more.

- **Flask Web Application**: The recommendation system is deployed using Flask, providing a user-friendly interface where users can input their preferences and receive tailored recommendations.

- **AWS Deployment**: The project is hosted on AWS Elastic Beanstalk, ensuring scalability and reliability. Continuous Integration/Continuous Deployment (CI/CD) pipelines are set up for seamless updates.

## How to Use

1. Visit the [demo website](http://bali-destination-recommendation-env.eba-qtdfie27.ap-southeast-2.elasticbeanstalk.com/).
2. Enter your preferences or keywords related to your ideal destination in Bali.
3. Click the "Search" button to receive personalized recommendations.
4. Explore the top recommended Bali destinations.

## Resources and References

- This project was developed with the assistance of ChatGPT by OpenAI.
- [CI/CD in AWS](https://youtu.be/gbJn2Ls2QsI?si=OxkN_j_39j86_Cl_) by Krish Naik on YouTube for an in-depth explanation and walkthrough of CI/CD configuration in AWS.
- [Data Source](https://www.google.com/maps) from Google Maps to get dataset.

---

**Note**: This project was developed as a demonstration and learning experience. It's not intended for commercial use.
