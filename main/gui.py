from hyperfocal import hyperfocal
from farDistanceSharp import sharpnessFar
from nearDistanceSharp import sharpnessNear
from angleofview import angleofview
from fieldofview import fieldofview

#create objects
#distance in ft
camera = "nikon"
aperture = 8
focalLength = 20
subjectDistance = 100
backgroundDistance = 100 #from camera
sensor = "full frame"



farDistance = sharpnessFar(focalLength, aperture, camera, subjectDistance)
nearDistance = sharpnessNear(focalLength, aperture, camera, subjectDistance)
hyperfocalDistance = hyperfocal(focalLength, aperture, camera)
angleOfView = angleofview(focalLength, sensor)
fieldOfView = fieldofview(focalLength, sensor, subjectDistance)



farDistance = farDistance.calculate_sharpnessFar() / 304.8 #convert mm to ft
nearDistance = nearDistance.calculate_sharpnessNear() / 304.8
hyperfocalDistance = hyperfocalDistance.calculate_hyperfocal() / 304.8
angleOfView = angleOfView.calculate_angleOfView()
fieldOfView = fieldOfView.calculate_fieldOfView()


print(
    'Depth of Field Far Limit(ft):', int(round(farDistance)), 
    '\nDepth of Field Near Limit(ft):', int(round(nearDistance)),
    '\nDepth of Fiend(ft):', round(farDistance - nearDistance, 1),
    '\nHyperfocal Distance(ft):', round(hyperfocalDistance, 1),
    '\nAngle of View Diagonal(degrees):', angleOfView[0],
    '\nAngle of View Vertical(degrees):', angleOfView[1],
    '\nAngle of View Horizontal(degrees):', angleOfView[2],
    )
