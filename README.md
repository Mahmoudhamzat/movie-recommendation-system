```markdown
# Movie Recommendation System

This project is a movie recommendation system that allows users to upload movie ratings and receive recommendations based on their ratings. The system aims to help users discover new movies based on their preferences.

## Project Contents

- **Core Features**:
  - Load movie data from a CSV file.
  - Clean usernames.
  - Build a structure for movie ratings.
  - Show recent ratings.
  - Provide movie recommendations based on user ratings.

## System Requirements

- Python 3.x
- `pandas` library

## How to Use

1. Clone the project:
   ```bash
   git clone https://github.com/username/repository.git
   cd repository
   ```

2. Install the required libraries (if necessary):
   ```bash
   pip install pandas
   ```

3. Run the program:
   ```bash
   python movie_recommendation_system.py
   ```

4. Upload the movie data file (CSV) when prompted.

## Input Data Structure

The CSV file should contain the following columns:
- `user Name`: The name of the user.
- `film Name`: The name of the movie.
- `Rating`: The movie rating (from 1 to 5).

### Example of Data Content:

```csv
user Name,film Name,Rating
mahmoud,Doctor Strange,4.0
mahmoud,Pulp Fiction,3.0
mahmoud,Titanic,3.2
maher,Inside Out,5.0
```

## How It Works

1. **Load Data**: Users can upload a CSV file containing movie ratings.
2. **Clean Data**: Usernames are cleaned, and null values are removed.
3. **Provide Recommendations**: Users can receive movie recommendations based on the movies they have rated.

## Contribution

If you would like to contribute to this project, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
```

### Notes:

- Make sure to replace `https://github.com/username/repository.git` with the actual link to your repository.
- You can adjust any details as needed, such as adding additional instructions or information about setting up or using the project.

