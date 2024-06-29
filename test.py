from apriori import Apriori
import unittest
import json

class TestAprioriAlgorithm(unittest.TestCase):

    def setUp(self):

        self.apriori = Apriori()

    def test_transaction(self):
        
        json_file = open("expected.json", "r")
        expected = json.load(json_file)
        json_file.close()
        
        result = self.apriori.apriori("transactions.dat", 2)
        
        self.assertDictEqual(result, expected)

    def test_transaction2(self):
    
        json_file = open("expected2.json", "r")
        expected = json.load(json_file)
        json_file.close()

        result = self.apriori.apriori("transactions2.dat", 2)

        self.assertDictEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
