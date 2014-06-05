#! /usr/bin/env python

import rospy
from cob_people_detection_msgs.msg import Detection
from cob_people_detection_msgs.msg import DetectionArray
import os

class PeopleGreeter(object):
    def __init__(self):
        rospy.init_node('people_greeter')
        rospy.Subscriber("/cob_people_detection/detection_tracker/face_position_array", DetectionArray, self.callback)
        self.name_dict = {}
        
    def callback(self, det):
        now = rospy.get_rostime().secs
        for d in det.detections:
            print d.label
            if d.label == 'UnknownHead':
                continue
            time = self.name_dict.get(d.label, None)
            if time == None or now - time > 10.0:
                os.system("espeak  -s 155 -a 200 'hello, %s'" % d.label)
                self.name_dict[d.label] = now
            

if __name__ == '__main__':
    node = PeopleGreeter()
    rospy.spin()
