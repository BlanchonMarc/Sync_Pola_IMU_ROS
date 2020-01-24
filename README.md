Collect data from Pola + IMU

# Collect data from Pola + IMU
***
## Polarcam
- Connect the Polarcam G1 to the computer. Do not forget it's POE.
- Test the Camera stream.


Initialize the Camera node:

`roslaunch pylon_camera pylon_camera_node_G1.launch`

Check the image_raw stream:

`rqt_image_view`


* * *
## IMU
- Connect the IMU to the computer. (You can also follow instructions [here](https://github.com/roboticslab-fr/euler_imu) if not installed)
- Test the IMU stream.

Initialize the IMU:

`roslaunch euler_imu imu_gx3-35_init.launch --screen`

Start the IMU:

`roslaunch euler_imu imu_gx3-35_init.launch --screen`

Check the pose stream of the IMU:

`rostopic echo /imu_3dm_node/imu/pose`

***
## Record

To record a bag containing all the current information, just create it through:

`rosbag record -a -o [Name_of_Your_Bag]`

***
## Extract the data from the recorded bag

You first need to have a bag recorded containing an IMU and a Camera stream. Refers to previous parts if you need to record bag.
When you have the bag you just have to specify the bag, the topics and the output folder.

Exemple:

`./ros/kinetic/catkin_ws/src/Kalibr/aslam_offline_calibration/kalibr/python/kalibr_bagextractor --bag PolarIMU.bag --image-topics /pylon_camera_node/image_raw --imu-topics /imu_3dm_node/imu/data --output OutputIMU2/`

It will result of a folder created in the folder you are and inside you will have the images and the csv file:

```
-> /home/mscv/
    |-> PolarIMU.bag
    |-> OutputIMU2/
        |-> cam0/
            |-> 143763883.png
            |-> 143763882.png
            |-> ...
        |-> imu0.csv
```
            

***
## Organize to build the dataset

Execute the organizer giving the folder of image, the csv file and the iutput folder for the separated csv.

Exemple:

`python organize.py --input OutputIMU2/cam0 --csv OutputIMU2/imu0.csv --output OutputIMU2/csv`

It will output synchronized imu and the synchronization. At the end, you'll have image and correspoinding imu with the same filename.

```
-> /home/mscv/
    |-> PolarIMU.bag
    |-> OutputIMU2/
        |-> cam0/
            |-> 143763883.png
            |-> 143763882.png
            |-> ...
        |-> imu0.csv
        |-> csv/
            |-> 143763883.csv
            |-> 143763882.csv
            |-> ...
```
