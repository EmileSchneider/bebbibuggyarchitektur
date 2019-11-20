import Interpretation
import Driving

class Decision:
    states = ["BOOT", "FAHREN", "VORFAHRT", "PARKIEREN"]

    def __init__(self):
        self.initialState = "BOOT"
        self.Interpretation = Interpretation.Interpretation()


    def drive(self):
        while(not self.Interpretation.stopLineDetected()):
            if(self.Interpretation.toFarLeft()):
                Driving.correctLeft(self.Interpretation.distanceLeftLane())

