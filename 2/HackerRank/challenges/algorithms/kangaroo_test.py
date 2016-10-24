import unittest
import kangaroo 

class KangarooCourt(unittest.TestCase):

    def test_same_velocities(self):
        x = kangaroo.Kang() 
        x.slowKangLoc = "0"
        x.slowKangVel = "2"
        x.fastKangLoc = "3"
        x.fastKangVel = "4"
        self.assertTrue(x.magic() == "NO")

    def test_large_vel_disparity(self):
        x = kangaroo.Kang() 
        x.slowKangLoc = "0"
        x.slowKangVel = "1"
        x.fastKangLoc = "3"
        x.fastKangVel = "100000"
        self.assertTrue(x.magic() == "NO")


    def test_small_vel_disparity(self):
        x = kangaroo.Kang() 
        x.slowKangLoc = "0"
        x.slowKangVel = "99999"
        x.fastKangLoc = "3"
        x.fastKangVel = "100000"
        self.assertTrue(x.magic() == "NO")

    def test_small_loc_disparity(self):
        x = kangaroo.Kang() 
        x.slowKangLoc = "0"
        x.slowKangVel = "99999"
        x.fastKangLoc = "3"
        x.fastKangVel = "100000"
        self.assertTrue(x.magic() == "NO")

if __name__ == '__main__':
    unittest.main()
