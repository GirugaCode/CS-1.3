from redact_problems import redact_lists
import unittest

class Redact_Problems(unittest.TestCase):
    def test_redact_problems(self):
        assert redact_lists(['A', 'B', 'C'], ['C', 'D', 'E']) == ['A','B']
    
    def test_redact_empty(self):
        assert redact_lists([' ', 'E', 'A'], ['D', 'E', 'D']) == [' ', 'A']

    def test_redact_duplicates(self):
        assert redact_lists(['A', 'B', 'C'], ['A', 'B', 'C']) == []
        
if __name__ == '__main__':
    unittest.main()







    
