This is a basic demo of Python Flask - MySQL using Docker.

Prerequisites:
1. Have the Docker Docker-compose installed.

How to Run:
1. Go to the project directory.
2. cd app ( GO to app folder)
3. Run docker-compose build
4. Run "docker-compose up".
5. open browser of your choice and navigate to 0.0.0.0/5000


APIs:

1. 0.0.0.0:5000/import
    This is a get request which basically does the data cleaning of a file which is included in the project directory. It extracts all the unique words and its count and stores it into mysql database.

    If you try to hit this api twice, the data will not be imported twice. It will simply give a response back as "File already imported".

2. 0.0.0.0:5000/wordscount
    This is a get request which queries the MySQL database and returns all the unique words and its count as the response.

3. 0.0.0.0:5000/wordcount/{word}
    This get request searched for the word in the database and returns the word and its frequency as the response.

4. 0.0.0.0:5000/matchword/{pattern}
    This get request returns all the words that has pattern as the substring.

Running Tests:

After running the application

1. cd app
2. python3 test.py ( It will not work for python 2.x as it uses a package "requests" which is not supported in Python 2.x)
