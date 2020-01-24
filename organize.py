import argparse
import os
import cv2
import numpy
import shutil
import csv
from decimal import Decimal



numpy.set_printoptions(precision=20)

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True,
                help="path to input folder")
ap.add_argument("-c", "--csv", required=True,
                help="path to input csv IMU")
ap.add_argument("-o", "--output", required=True,
                help="path to output csv IMU")
args = vars(ap.parse_args())


if not os.path.exists(args['output']):
    os.makedirs(args['output'])

f = []
for (dirpath, dirnames, filenames) in os.walk(args['input']):
    f.extend(filenames)
    break
    
data = numpy.genfromtxt(args['csv'], delimiter=',')

stamp = data[1:, 0]
quat = data[1:, 7:]

# print(stamp)

for filename in f:
    number = int(filename.split('.')[0])
    nearest = min(stamp, key=lambda x:abs(x-number))
    index = numpy.where(stamp == nearest)
    
    csvfilename = filename.split('.')[0]
    thequat = quat[index]
    numpy.savetxt(os.path.join(args['output'],csvfilename+'.csv'), thequat, delimiter=',')
    
