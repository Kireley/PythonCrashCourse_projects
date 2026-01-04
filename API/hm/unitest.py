import unittest
import requests

def add(a, b):
    return a + b
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")
class TestMath(unittest.TestCase):
    def test_add(self):
        self.as

if __name__ == '__main__':
    unittest.main()
