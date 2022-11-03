import unittest
from client import NamedEntityClient

class TestClient(unittest.TestCase):

    def test_get_ents_returns_dictionary_given_empty_string(self):
        client = NamedEntityClient()
        ents = client.get_ents("")
        self.assertIsInstance(ents, dict)

            