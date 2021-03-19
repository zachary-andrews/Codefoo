import unittest
from solution import unscramble

class importTests(unittest.TestCase):
    def setUp(self):
        self.unscramble = unscramble()

    def test_1(self):
        self.assertEqual("URYYB JBEYQ", self.unscramble.get_word("HELLO WORLD"))
    
    def test_2(self):
        self.assertEqual("WNPX FVYIRE NOBEG ZVFFVBA LBH NER PBZCEBZVFRQ", self.unscramble.get_word("JACK SILVER ABORT MISSION YOU ARE COMPROMISED"))
     
    def test_3(self):
        self.assertEqual("YOUR MISSION IS IF YOU ACCEPTED TO CURE ALL DECIESES FROM THE WORLD AND BRING WORLD PEACE EVERY AND EACH ONE", self.unscramble.get_word("LBHE ZVFFVBA VF VS LBH NPPRCGRQ GB PHER NYY QRPVRFRF SEBZ GUR JBEYQ NAQ OEVAT JBEYQ CRNPR RIREL NAQ RNPU BAR"))
     
    def test_4(self):
        self.assertEqual("THIS HACK WILL BE WAIT FOR IT LEGENDARY", self.unscramble.get_word("GUVF UNPX JVYY OR JNVG SBE VG YRTRAQNEL"))
     

if __name__ == '__main__':
    unittest.main()