# Book Recommender System

This repository contains a Python-based book recommendation system that utilizes machine learning techniques to provide personalized book suggestions. The project employs a popularity-based recommendation approach, collaborative filtering, and a hybrid model to deliver tailored recommendations.

## Features

- **Popularity-Based Recommendations**: Suggests books based on the average rating and number of reviews, prioritizing books with at least 250 ratings.
- **Collaborative Filtering**: Recommends books based on user similarity, accounting for ratings given by similar users.
- **Hybrid Recommendations**: Combines popularity and collaborative filtering for more robust suggestions.
- **Web Interface**: Uses Flask to provide a simple interface for interacting with the recommendation system.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Aarush-Parashar/book-recommender.git
    ```

2. Navigate to the project directory:

    ```bash
    cd book-recommender
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the application:

    ```bash
    python app.py
    ```

## Usage

1. Start the server using the command above.
2. Interact with the recommendation system by entering user preferences or viewing popular books.

## Project Structure

- **app.py**: Main file for running the Flask web server.
- **models/**: Contains data processing and recommendation models.
- **templates/**: HTML templates for the web interface.
- **static/**: Static files, including CSS for the web app.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue to discuss improvements, new features, or bug fixes.
