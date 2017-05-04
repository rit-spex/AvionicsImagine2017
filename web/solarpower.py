import numpy as np
import math

# define points on cube
CUBE_SIZE = 5
V1 = -CUBE_SIZE, CUBE_SIZE, -CUBE_SIZE
V2 = CUBE_SIZE, CUBE_SIZE, -CUBE_SIZE
V3 = -CUBE_SIZE, -CUBE_SIZE, -CUBE_SIZE
V4 = CUBE_SIZE, -CUBE_SIZE, -CUBE_SIZE
V5 = -CUBE_SIZE, CUBE_SIZE, CUBE_SIZE
V6 = CUBE_SIZE, CUBE_SIZE, CUBE_SIZE
V7 = -CUBE_SIZE, -CUBE_SIZE, CUBE_SIZE
V8 = CUBE_SIZE, -CUBE_SIZE, CUBE_SIZE
SUN = 0, 1000, 0

def unit_vector(vector):
    """ Returns the unit vector of the vector.  """
    return vector / np.linalg.norm(vector)

def angle_between(v1, v2):
    """ Returns the angle in radians between vectors 'v1' and 'v2'::

            >>> angle_between((1, 0, 0), (0, 1, 0))
            1.5707963267948966
            >>> angle_between((1, 0, 0), (1, 0, 0))
            0.0
            >>> angle_between((1, 0, 0), (-1, 0, 0))
            3.141592653589793
    """
    v1_u = unit_vector(v1)
    v2_u = unit_vector(v2)
    return np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0))
    

def rotate(x, y, z, pitch, roll, yaw):
    a = (x * (math.cos(roll) * math.cos(yaw)) + y * (math.sin(yaw) * math.cos(roll)) - z * (math.sin(roll)))
    b = (x * (math.sin(pitch) * math.sin(roll) * math.sin(yaw) - math.sin(yaw) * math.cos(pitch)) + y * (math.sin(pitch) * math.sin(roll) * math.sin(yaw) + math.cos(pitch) * math.cos(yaw)) + z * (math.sin(pitch) * math.cos(roll)))
    c = (x * (math.sin(pitch) * math.sin(yaw) + math.sin(roll) * math.cos(pitch) * math.cos(yaw)) + y * (-math.sin(pitch) *math.cos(yaw) + math.sin(roll) * math.sin(yaw) * math.cos(pitch)) + z * (math.cos(roll) * math.cos(pitch)))
    return (a, b, c)
def getNormalVector(v1, v2):
    return tuple(x+y for x, y in zip(v1, v2))

def getPlanes(v1, v2, v3, v4, v5, v6, v7, v8):
    return (getNormalVector(v1, v7), getNormalVector(v1, v6), getNormalVector(v6, v7), getNormalVector(v6, v4), getNormalVector(v4, v7), getNormalVector(v1, v4))

def getSolarPower(pitch, roll, yaw):
    verticies = (V1, V2, V3, V4, V5, V6, V7, V8)
    verticies = tuple(rotate(*v, pitch, roll, yaw) for v in verticies)
    planes = getPlanes(*verticies)
    angles = tuple(angle_between(v, SUN) for v in planes)
    angles = tuple(angle for angle in angles if math.pi / 2> angle > -math.pi / 2)
    intensities = tuple(math.fabs(math.cos(angle)) for angle in angles)
    return sum(intensities)

def main():
    print(getSolarPower(math.pi/24,.1,.1))

if __name__ == '__main__':
    main()
