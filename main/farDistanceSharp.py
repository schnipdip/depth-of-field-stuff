import math
from hyperfocal import hyperfocal

'''
	Purpose: Calculate the Far Distance of Acceptable Sharpness.
	Variables: 
		H = Hyperfocal Distance
		f = Focal length
		N = Aperture
		c = Circle of Confusion -> for this .02/.03 (Nikon/Canon)
		i = 1,2,3...22 for f/1.4, f/2, f/2.8...
        s = focus distance/subject distance (feet)

	Formula(s):
		DF = s * H / [H - (s - f)]

	Resources:
		Circle of Confusion Table: http://www.dofmaster.com/digital_coc.html
''' 
class sharpnessFar():
    def __init__(self, focalLength, aperture, camera, subjectDistance):
        self.focalLength = focalLength
        self.aperture = aperture
        self.camera = camera
        self.subjectDistance = subjectDistance
    
    def calculate_sharpnessFar(self):
        self.H = hyperfocal(self.focalLength, self.aperture, self.camera)
        
        self.hyperfocal = self.H.calculate_hyperfocal()

        #convert feet to milimeters
        self.subjectDistance = self.subjectDistance * 304.8

        self.mult_hyperfocal_subject = float(self.hyperfocal) * float(self.subjectDistance)

        self.sub_subject_focal = float(self.subjectDistance) - float(self.focalLength)

        self.sub_hyperfocal_ssf = float(self.hyperfocal) - float(self.sub_subject_focal)

        self.div_mhs_shssf = self.mult_hyperfocal_subject / self.sub_hyperfocal_ssf

        #calculates the Near Sharpness in MM

        return(int(round(self.div_mhs_shssf)))
        
#test = sharpnessFar(20, "11", "canon", 5)
#test.calculate_sharpnessFar()