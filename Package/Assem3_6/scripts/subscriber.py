#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    
def listener():

        rospy.init_node('straight_line_subscriber')
        subscribe = rospy.Subscriber('/Assem3_6/back_right_wheel/command', Float64, callback, queue_size=10)
        subscribe = rospy.Subscriber('/Assem3_6/back_left_wheel/command', Float64, callback, queue_size=10)

        rospy.spin()

if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        pass