import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import pickle


books = pd.read_csv('books.csv')
users = pd.read_csv('users.csv')
ratings = pd.read_csv('ratings.csv')

# Popularity-based recommendation system
# Filtering books with at least 250 ratings and ordering by average rating
ratings_with_name = ratings.merge(books, on='ISBN')
num_rating_df = ratings_with_name.groupby('Book-Title').count()['Book-Rating'].reset_index()
num_rating_df.rename(columns={'Book-Rating': 'num_ratings'}, inplace=True)

avg_rating_df = ratings_with_name.groupby('Book-Title')['Book-Rating'].mean(numeric_only=True).reset_index()
avg_rating_df.rename(columns={'Book-Rating': 'avg_rating'}, inplace=True)

popularity_df = num_rating_df.merge(avg_rating_df, on='Book-Title')

popularity_df = popularity_df[popularity_df['num_ratings'] >= 250]
popularity_df = popularity_df.sort_values('avg_rating', ascending=False).head(50)
popularity_df = popularity_df.merge(books, on='Book-Title').drop_duplicates(subset='Book-Title')[['Book-Title', 'Book-Author','Image-URL-M' ,'num_ratings', 'avg_rating']]


#collaborative filtering recommendation system
x=ratings_with_name.groupby('User-ID').count()['Book-Rating'] > 200
experienced_users= x[x].index

filtered_rating=ratings_with_name[ratings_with_name['User-ID'].isin(experienced_users)]

y=filtered_rating.groupby('Book-Title').count()['Book-Rating']>=50
famous_books=y[y].index

final_rating=filtered_rating[filtered_rating['Book-Title'].isin(famous_books)]
pt=final_rating.pivot_table(index='Book-Title',columns='User-ID',values='Book-Rating')
pt.fillna(0,inplace=True)

similarity_score = cosine_similarity(pt)

def recommend(book_name):
    sample_index= np.where(pt.index == book_name)[0][0]
    similar_books = sorted(list(enumerate(similarity_score[sample_index])),key=lambda x:x[1],reverse=True)[1:9]

    data = []
    for j in similar_books:
        item = []
        
        temp_df = books[books['Book-Title']==pt.index[i[0]]]
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))
        
        data.append(item)

    return data


#connecting program to website

pickle.dump(popularity_df,open('popular.pkl','wb'))
pickle.dump(pt, open('pt.pkl','wb'))
pickle.dump(books,open('books.pkl','wb'))
pickle.dump(similarity_score,open('similarity_scores.pkl','wb'))


            
print(recommend('1984'))


