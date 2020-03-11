import unittest
from libs import *
import requests


class TestRequest(unittest.TestCase):

    def create_request(self, url):
        return Connection(url)

    def test_create_request(self):
        try:
            self.create_request("http://www.google.com")
            self.create_request("http://www.linkedin.com")
            self.create_request("http://www.facebook.com")
        except requests.exceptions.ConnectionError:
            self.fail("ConnectionError exception occurred!")
        try:
            self.create_request("http://www.google.com")
            self.create_request("http://www.linkedin.com")
            self.create_request("http://www.facebook.com")
        except requests.exceptions.ConnectTimeout:
            self.fail("ConnectTimeout exception occurred!")
        try:
            self.create_request("http://www.google.com")
            self.create_request("http://www.linkedin.com")
            self.create_request("http://www.facebook.com")
        except SyntaxError:
            self.fail("SyntaxError exception occurred!")

    def test_get_url(self):
        r_google = self.create_request("http://www.google.com")
        r_linkedin = self.create_request("http://www.linkedin.com")
        r_facebook = self.create_request("http://www.facebook.com")

        self.assertEqual(r_google.geturl(), "http://www.google.com")
        self.assertEqual(r_linkedin.geturl(), "http://www.linkedin.com")
        self.assertEqual(r_facebook.geturl(), "http://www.facebook.com")

    def test_get_request(self):
        r_google = self.create_request("http://www.google.com")
        r_linkedin = self.create_request("http://www.linkedin.com")
        r_facebook = self.create_request("http://www.facebook.com")

        self.assertIsNotNone(r_google.getrequest())
        self.assertIsNotNone(r_linkedin.getrequest())
        self.assertIsNotNone(r_facebook.getrequest())

    def test_request_code_200(self):
        r_google = self.create_request("http://www.google.com")
        r_linkedin = self.create_request("http://www.linkedin.com")
        r_facebook = self.create_request("http://www.facebook.com")

        self.assertEqual(r_google.getrequest().status_code, 200)
        self.assertEqual(r_linkedin.getrequest().status_code, 200)
        self.assertEqual(r_facebook.getrequest().status_code, 200)


class TestElements(unittest.TestCase):
    pass

if __name__ == "__main__":
    unittest.main()
