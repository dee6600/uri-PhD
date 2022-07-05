#!/usr/bin/env python


import rospy
from std_msgs.msg import String


# Function to publish the string messeages 
def talker():
    # Creating a publisher named "input" with type string and size 10
    pub = rospy.Publisher('input', String, queue_size=10)

    # Initialising publisher node
    rospy.init_node('input', anonymous=True)

    # Defining rate at with the publisher should publish
    rate = rospy.Rate(10) # 10hz

    # Loop / publish until shutdown
    while not rospy.is_shutdown():
        
        # String Data to be published 
        str_data = "hello world"

        # Printing/logging original data on console
        rospy.loginfo(str_data)

        # Publishing the data through pub object
        pub.publish(str_data)

        # ROS service will sleep for the rate defined earlier
        rate.sleep()

# Main function
if __name__ == '__main__':

    # Try catch block for publisher
    try:
        # Function call for publisher
        talker()
    # ROS exception handling
    except rospy.ROSInterruptException:
        pass