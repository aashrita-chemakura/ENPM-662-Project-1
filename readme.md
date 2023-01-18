
|Team Members
|--
|Saketh Narayan Banagiri
|Aashrita Chemakura


Robot Name: Assem3_6

Paste the folder named 'Assem3_6'(Present in the package folder) in the catkin workspace. 

Package name for this project is same as the robot name. i.e. Assem3_6

Teleop:

Run the following command in the terminal:

roslaunch Assem3_6 template_launch.launch

Now open another terminal tab and run the following command:

rosrun Assem3_6 teleop_template.py

Publisher and Subscriber:

Run the following command in the terminal:

roslaunch Assem3_6 template_launch.launch

Now open another terminal tab and run the following command:

rosrun Assem3_6 publisher.py

Now open another terminal tab and run the following command:

rosrun Assem3_6 subscriber.py

Laser Scan in Rviz:

Run the following command in the terminal:

roslaunch Assem3_6 template_launch.launch


Now open another terminal tab and run the following command:

rviz

Now add the robot model

Add topic as Laser scan

You can visualize the obstacles present in competition world scanned by the laser in rviz


