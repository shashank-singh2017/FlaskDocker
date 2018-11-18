import unittest
import requests

class TestStringMethods(unittest.TestCase):

    # The /import api  should return a status code of 200
    # After Importing the file, the api should return a text as response - Database populated with words

    def test_import(self):
        response = requests.get('http://0.0.0.0:5000/import')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, 'Database populated with words')

    # The /wordcount api  should return a status code of 200
    # After Importing the file, the api should return a list of words and respective counts

    def test_wordscount(self):
        response = requests.get('http://0.0.0.0:5000/wordscount')
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(len(response.json().get("wordcount")), 0)

    def test_wordSearch(self):
        response = requests.get('http://0.0.0.0:5000/wordcount/series')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"wordcount": [ {'series': 10 } ]})

    def test_searchPattern(self):
        response = requests.get('http://0.0.0.0:5000/matchword/eri')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"wordcount": [ {'series': 10 }, { 'derivative': 1 }, { 'premiering': 1 } ]})

if __name__ == '__main__':
    unittest.main()
