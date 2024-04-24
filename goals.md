## 0. using GCP for deployment:
- Use GCP for deployment
- Gitlab CI/CD

## 1. Fetch test data via https from OMDB API
OK - You should fetch 100 movies from OMDB API. It's up to you what kind of movies you will get.
OK - Movies should be saved in the database.
OK - This method should be ran only once if database is empty.

## 2. Implement an api
OK - The api should have a method that returns a list of movies from the database
OK - There should be option to set how many records are returned in single API response (by default 10)
OK - There should be pagination implemented in the backend
OK - Data should be ordered by Title
OK - The api should have a method that returns a single movie from the database
OK - There should be option to get the movie by title
OK - The api should have a method to add a movie to the database
OK - Title should be provided in request
OK - All movie details should be fetched from OMDB API and saved in the database
OK - The api should have a method to remove a movie from the database
OK - There should be option to remove movie with it's id
- This method should be protected so only authorized user can perform this action

## 3. Testing
- Unit testing for all cases
- Integrated testing

