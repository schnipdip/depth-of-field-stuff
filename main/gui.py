from hyperfocal import hyperfocal
from farDistanceSharp import sharpnessFar
from nearDistanceSharp import sharpnessNear

#create objects
camera = "canon"
aperture = 1
focalLength = 100
subjectDistance = 100

farDistance = sharpnessFar(focalLength, aperture, camera, subjectDistance)
nearDistance = sharpnessNear(focalLength, aperture, camera, subjectDistance)


#convert mm to ft
farDistance = farDistance.calculate_sharpnessFar() / 304.8
nearDistance = nearDistance.calculate_sharpnessNear() / 304.8

print(int(round(farDistance)), int(round(nearDistance)))
