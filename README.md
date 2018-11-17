This is a basic demo of Python Flask - MySQL using Docker.

Prerequisites:
1. Have the Docker Docker-compose installed.

How to Run:
1. Clone the Repository
2. Go to the project directory.
3. Run "docker-compose up".
4. open browser of your choice and navigate to 0.0.0.0/5000


APIs:

1. 0.0.0.0/5000/import
    This is a get request which basically does the data cleaning of a file which is included in the project directory. It extracts all the unique words and its count and stores it into mysql database.

2. 0.0.0.0/5000/wordscount
    This is a get request which queries the MySQL database and returns all the unique words and its count as the response.

3. 0.0.0.0:5000/wordcount/{word}
    This get request searched for the word in the database and returns the word and its frequency as the response.

4. 0.0.0.0:5000/matchword/{pattern}
    This get request returns all the words that has pattern as the substring.
