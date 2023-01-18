#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import Float64, String

def straight_line_command():
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('straight_line_publisher', anonymous=True)
    pub_right_back = rospy.Publisher('/Assem3_6/back_right_wheel/command', Float64, queue_size=10) # Add your topic here between ''. Eg '/my_robot/steering_controller/command'
    pub_left_back = rospy.Publisher('/Assem3_6/back_left_wheel/command', Float64, queue_size=10)
    pub_right_turn = rospy.Publisher('/Assem3_6/front_right_wheel/command', Float64, queue_size=10)
    pub_left_turn = rospy.Publisher('/Assem3_6/front_left_wheel/command', Float64, queue_size=10)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        for i in range(100000000000):
            pub_left_turn.publish(0.0)
            pub_right_turn.publish(0.0)
            pub_left_back.publish(10.0)
            pub_right_back.publish(10.0)
        # print("Published velocity command")


if __name__ == '__main__':
    try:
        straight_line_command()
    except rospy.ROSInterruptException:
        pass