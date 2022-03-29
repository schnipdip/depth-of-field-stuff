import math

'''
	Purpose: Calculate the hyperfocal distance.
	Variables: 
		H = Hyperfocal Distance
		f = Focal length
		N = Aperture
		c = Circle of Confusion -> for this .02/.03 (Nikon/Canon)
		i = 1,2,3...22 for f/1.4, f/2, f/2.8...

	Formula(s):
		N = 2^(i/2)

	Resources:
		Circle of Confusion Table: http://www.dofmaster.com/digital_coc.html
''' 

class hyperfocal():
    def __init__(self, focalLength, aperture, camera):
        self.focalLength = focalLength
        self.aperture = aperture
        self.camera = camera
		
    def calculate_hyperfocal(self):

	#assign circle of confusion based on camera system
        if self.camera.lower() == "nikon":
            self.circleOfConfusion = .02
        elif self.camera.lower() == "canon":
            self.circleOfConfusion = .03

        self.mult_focalLength = self.focalLength**2
        
        self.mult_N_CoC = float(self.aperture) * self.circleOfConfusion
        
        self.H = self.mult_focalLength / self.mult_N_CoC

        #print("Hyperfocal Distance (ft):", round(self.H / 304.8, 1))
        
        #returns millimeters
        return round(self.H)

#test = hyperfocal(20, "11", "canon")
#test.calculate_hyperfocal()
