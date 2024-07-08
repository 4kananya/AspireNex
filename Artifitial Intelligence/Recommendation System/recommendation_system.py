import streamlit as st
import joblib
import pandas as pd
import numpy as np 

book_similarity_matrix_path = r'Book_Recommender\book_similarity_matrix.joblib'
similarity_matrix_path = r'Movie_Recommender\similarity_matrix.joblib'
book_user_matrix_path = r'Book_Recommender\book_user_matrix.csv'
df_new_final_path = r'Movie_Recommender\df_new_final.csv'

book_similarity_matrix = joblib.load(book_similarity_matrix_path)
similarity = joblib.load(similarity_matrix_path)
book_user_matrix = pd.read_csv(book_user_matrix_path, index_col='Book-Title')
df_new_final = pd.read_csv(df_new_final_path)

def recommend_movie_names(xMovie):
    try:
        movie_index = df_new_final[df_new_final["title"].str.lower() == xMovie.lower()].index[0]
        distances = similarity[movie_index]
        list_of_movies = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
        recommended_movies = [df_new_final.iloc[i[0]]["title"] for i in list_of_movies]    
        return recommended_movies
    except IndexError:
        return []

def suggest_similar_books(book_name):
    try:
        book_idx = np.where(book_user_matrix.index == book_name)[0][0]
        scores = list(enumerate(book_similarity_matrix[book_idx]))
        scores = sorted(scores, key=lambda x: x[1], reverse=True)[1:8]
        book_recommendation = []
        for p in scores:
            temp_df = book_user_matrix[book_user_matrix.index == book_user_matrix.index[p[0]]]
            book_recommendation.extend(list(temp_df.index.drop_duplicates()))
        return book_recommendation
    except IndexError:
        return []
st.title("Recommendation System")

option = st.selectbox(
    'Choose a recommendation type:',
    ('Book Recommendation', 'Movie Recommendation')
)

if option == 'Book Recommendation':
    book_title = st.text_input("Enter a book title you like:")
    if book_title:
        recommended_books = suggest_similar_books(book_title)
        if recommended_books:
            st.write(f"Books similar to '{book_title}':")
            for book in recommended_books:
                st.write(book)
        else:
            st.write(f"No recommendations found for '{book_title}'.")

elif option == 'Movie Recommendation':
    movie_title = st.text_input("Enter a movie title you like:")
    if movie_title:
        recommended_movies = recommend_movie_names(movie_title)
        if recommended_movies:
            st.write(f"Movies similar to '{movie_title}':")
            for movie in recommended_movies:
                st.write(movie)
        else:
            st.write(f"No recommendations found for '{movie_title}'.")
