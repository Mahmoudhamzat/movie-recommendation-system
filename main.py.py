# -*- coding: utf-8 -*-
"""
Created on Thu Mar 6 14:44:03 2025

@author: mmmkh
"""

import pandas as pd
from collections import deque, defaultdict
import os
import tkinter as tk
from tkinter import filedialog, messagebox

# Load movie data
def load_data(file_path):
    try:
        df = pd.read_csv(file_path)
        df.dropna(inplace=True)  # Remove null values
        df.columns = df.columns.str.strip()  # Remove extra spaces from column names
        return df
    except FileNotFoundError:
        messagebox.showerror("Error", "Data file not found!")
        return None
    except pd.errors.EmptyDataError:
        messagebox.showwarning("Warning", "The file is empty!")
        return None
    except Exception as e:
        messagebox.showerror("Error", f"Unexpected error: {e}")
        return None

# Clean usernames
def clean_usernames(df):
    df['user Name'] = df['user Name'].astype(str).apply(lambda x: f"User_{x.strip()}" if x.strip().isdigit() else x.strip())
    return df

# Build movie ratings structure
def build_movie_ratings(df):
    movie_ratings = defaultdict(list)
    for _, row in df.iterrows():
        movie_ratings[row['film Name']].append((row['user Name'], row['Rating']))
    return movie_ratings

# Show recent ratings
def show_recent_ratings(ratings_log):
    print("\n📌 Last 5 added ratings:")
    for user, movie, rating in list(ratings_log)[-5:]:
        print(f"{user} ⭐ {rating}/5 for {movie}")

# Recommendation system
def recommend_movies(movie_ratings, watched_movie):
    if watched_movie not in movie_ratings:
        print("⚠️ This movie is not in the database!")
        return []
    
    similar_users = {user for user, _ in movie_ratings[watched_movie]}
    recommendations = defaultdict(int)
    
    for movie, ratings in movie_ratings.items():
        if movie == watched_movie:
            continue
        for user, rating in ratings:
            if user in similar_users and rating >= 3.5:
                recommendations[movie] += 1
    
    return [movie for movie, _ in sorted(recommendations.items(), key=lambda x: x[1], reverse=True)[:5]]

# Add a new rating
def add_rating(df, ratings_log, user, movie, rating, file_path):
    new_entry = {'user Name': user, 'film Name': movie, 'Rating': rating}
    df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)
    ratings_log.append((user, movie, rating))
    
    df.to_csv(file_path, index=False)
    with open('log.txt', 'a', encoding='utf-8') as f:
        f.write(f"{user},{movie},{rating}\n")
    
    print(f"✅ Rating added: {user} ⭐ {rating}/5 for {movie}")
    return df

# Function to upload data file
def upload_data_file():
    file_path = filedialog.askopenfilename(title="Select CSV Data File", filetypes=[("CSV Files", "*.csv")])
    if file_path:
        df = load_data(file_path)
        if df is not None:
            df = clean_usernames(df)
            movie_ratings = build_movie_ratings(df)
            run_recommendation_system(movie_ratings, df, file_path)

# Run the recommendation system
def run_recommendation_system(movie_ratings, df, file_path):
    ratings_log = deque(maxlen=10)

    # Load previous ratings log
    if os.path.exists('log.txt'):
        with open('log.txt', 'r', encoding='utf-8') as f:
            for line in f.readlines()[-10:]:
                user, movie, rating = line.strip().split(',')
                ratings_log.append((user, movie, float(rating)))

    while True:
        print("\n🎬 Welcome to the Movie Recommendation System!")
        print("1️⃣ Show recent ratings")
        print("2️⃣ Get recommendations for a specific movie")
        print("3️⃣ Add a new rating")
        print("4️⃣ Exit the program")
        
        choice = input("🔹 Choose an option: ")
        
        if choice == "1":
            show_recent_ratings(ratings_log)
        
        elif choice == "2":
            movie = input("🎥 Enter the name of the movie you watched: ").strip()
            recommendations = recommend_movies(movie_ratings, movie)
            if recommendations:
                print("\n🎯 Recommended movies for you:")
                for rec in recommendations:
                    print(f"✅ {rec}")
        
        elif choice == "3":
            user = input("👤 Enter username: ").strip()
            movie = input("🎥 Enter movie name: ").strip()
            try:
                rating = float(input("⭐ Enter rating (1 to 5): "))
                if 1 <= rating <= 5:
                    df = add_rating(df, ratings_log, user, movie, rating, file_path)
                else:
                    print("⚠️ Invalid rating! Enter a number between 1 and 5.")
            except ValueError:
                print("❌ Error: Please enter a valid number between 1 and 5.")
        
        elif choice == "4":
            print("👋 Thank you for using the recommendation system! Goodbye!")
            break
        
        else:
            print("⚠️ Invalid option, please try again.")

# Create main application window
root = tk.Tk()
root.title("Movie Recommendation System")
root.geometry("400x200")

upload_button = tk.Button(root, text="Upload Data File", command=upload_data_file)
upload_button.pack(pady=20)

exit_button = tk.Button(root, text="Exit", command=root.quit)
exit_button.pack(pady=20)

root.mainloop()