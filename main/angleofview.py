import math

'''
    Purpose:
        Calculate the Angle of View
    Formula:
        Diagonal = d = √(sensor_width² + sensor_height_²) = 43.3mm
        Angle of view (in degrees) = 2 x arctan (diagonal/2*focalLength)
'''

class angleofview():
    def __init__(self, focalLength, sensor):
        self.focalLength = focalLength
        self.sensor = sensor

    def calculate_angleOfView(self):
        #set sensor width
        if self.sensor.lower() == 'full frame':
            self.sensor_width = 24.0
            self.sensor_height = 36.0
        elif self.sensor.lower() == 'aps-c':
            self.sensor_width = 15.0
            self.sensor_height = 22.5
        elif self.sensor.lower() == 'medium format':
            self.sensor_width = 33.0
            self.sensor_height = 44.0

        #Calculate Diagonal
        self.diagonal = round(math.sqrt(self.sensor_width**2 + self.sensor_height**2), 1)

        #Calculate Diagonal Angle of View
        self.mult_focalLength_2 = self.focalLength * 2
        self.div_sensorDiagonal_focalLength_2 = self.diagonal / self.mult_focalLength_2
        self.mult_tan_sensorDiagonal_focalLength_2 = math.atan(self.div_sensorDiagonal_focalLength_2)
        self.angleOfView_diagonal = (2 * self.mult_tan_sensorDiagonal_focalLength_2)

        #Calculate Vertical Angle of View
        self.mult_focalLength_2 = self.focalLength * 2
        self.div_sensorWidth_focalLength_2 = self.sensor_width / self.mult_focalLength_2
        self.mult_tan_sensorWidth_focalLength_2 = math.atan(self.div_sensorWidth_focalLength_2)
        self.angleOfView_vertical = (2 * self.mult_tan_sensorWidth_focalLength_2)

        #Calculate Horizontal Angle of View
        self.mult_focalLength_2 = self.focalLength * 2
        self.div_sensorHeight_focalLength_2 = self.sensor_height / self.mult_focalLength_2
        self.mult_tan_sensorHeight_focalLength_2 = math.atan(self.div_sensorHeight_focalLength_2)
        self.angleOfView_horizontal = (2 * self.mult_tan_sensorHeight_focalLength_2)

        return([round(math.degrees(self.angleOfView_diagonal),1), 
                round(math.degrees(self.angleOfView_vertical),1),
                round(math.degrees(self.angleOfView_horizontal),1)
                ])

test = angleofview(20, 'full frame')
test.calculate_angleOfView()