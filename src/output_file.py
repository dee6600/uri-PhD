#!/usr/bin/env python

import rospy
from std_msgs.msg import String


# Callback function to grab the data from the process publisher
def callback(data):
    # Printing sorted data to console 
    rospy.loginfo("SORTED STRING : %s", ' '.join(sorted(data.data)))

# Fucntion to subscribe to process topic    
def listener():

    # Initialising subscriber node
    rospy.init_node('listener', anonymous=True)
    # Calling Subscriber 
    rospy.Subscriber("process", String, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    # Function call for output
    listener()