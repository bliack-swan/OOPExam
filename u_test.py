import unittest
from main import Algorithm

class TestAlgorithm(unittest.TestCase):
    def setUp(self):
        self.Algorithm = Algorithm( "ssrhguhrsshruhgssssgrhhei" )
    def test_word(self):
        self.assertEqual( self.Algorithm.get_word() , ['s', 's', 'r', 'h', 'g', 'u', 'h', 'r', 's', 's', 'h', 'r', 'u',
                                                       'h', 'g', 's', 's', 's', 's', 'g', 'r', 'h', 'h', 'e', 'i'] )
    def test_result(self):
        self.assertEqual( self.Algorithm.algo(), (8,4) )

if __name__ == "__main__":
    unittest.main()