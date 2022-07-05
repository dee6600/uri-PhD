#!/usr/bin/env python

import rospy
from std_msgs.msg import String

# Global variable for storing Sorted string
sorted_data = ''

# Creating a publisher object to pss output
pub = rospy.Publisher('process', String, queue_size=10)

# Callback function to grab the data from the publisher
def callback(data):
    # Define global variable for storing Sorted string
    global sorted_data

    # Sorting the Recived data and storing it in variable "sorted_data" 
    sorted_data = ' '.join(sorted(data.data))

    # Publishing the data through pub object
    pub.publish(sorted_data)

# Fuction which calls the subscriber and publisher to process the data
def process():

    # Initialising publisher node
    rospy.init_node('listener', anonymous=True)

    # Calling Subscriber 
    rospy.Subscriber("input", String, callback)

    # Publishing the sorted string
    pub.publish(sorted_data)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

# Main function
if __name__ == '__main__':
    # Function call for process
    process()