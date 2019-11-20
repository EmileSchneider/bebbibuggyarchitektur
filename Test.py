import unittest
import Interpretation


class TestInterpretations(unittest.TestCase):

    def testStopLineDetection(self):
        # provide selected images, especially edgecases
        i = Interpretation.Interpretation()

        i.vision.image = "IMAGE WITH STOPLINE"
        self.assertTrue(i.stopLineDetected())

        i.vision.image = "IMAGE WITHOUT STOPLINE"
        self.assertFalse(i.stopLineDetected())
