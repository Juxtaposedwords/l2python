import unittest
import  kangaroo 

class KangarooCourt(unittest.TestCase):
    def test_same_velocities(self):
       x = kangaroo.Kang() 
       self.assertTrue(x.magic(0,2,4,2) == "NO")

if __name__ == '__main__':
    unittest.main()
