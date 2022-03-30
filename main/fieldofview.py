import math
from angleofview import angleofview

'''
    Purpose:
        Calculate Field of View
    Formula:
        FoV = 2 * SubjectDistance * tan(AoV/2)
'''

class fieldofview():
    def __init__(self, focalLength, sensor, subjectDistance):
        self.focalLength = focalLength
        self.sensor = sensor
        self.subjectDistance = subjectDistance

    def calculate_fieldOfView(self):
        #get Diagonal Angle of View
        self.angleOfView = angleofview(self.focalLength, self.sensor)

        self.aov = self.angleOfView.calculate_angleOfView()
        
        self.div_tan_aov_2 = math.atan(self.aov[0] / 2)

        self.mult_2_subjectDistance = 2 * self.subjectDistance

        self.fieldOfView_diagonal = self.div_tan_aov_2 * self.mult_2_subjectDistance

        print(self.fieldOfView_diagonal)

test = fieldofview(20, 'full frame', 10)
test.calculate_fieldOfView()





