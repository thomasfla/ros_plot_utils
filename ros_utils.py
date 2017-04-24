#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  2017 Thomas Flayols <tflayols@arequipa>


from std_msgs.msg import String
from dynamic_graph_bridge_msgs.msg import Vector
import message_filters
import os
import numpy as np
import rospy
import subprocess
import matplotlib.pyplot as plt
from time import sleep
import sys, time
import roslib
from IPython import embed

class RosTopic2Vector:
    '''This class subscribes to topics and stores values as members''' 
    def __init__(self,topics=[]):
        self._subscribers=[]
        self._ts=[]
        '''Initialize ros subscribers'''
        for (topic_name, attr_name) in topics:
             self.addSubscriber(topic_name,attr_name)
    def addSubscriber(self,topic_name, attr_name=None, historyLen = None):
        '''Subscribe to a topic and create member of your choise to store received data'''
        if attr_name == None : 
            attr_name = topic_name
        setattr(self, attr_name, None)
        setattr(self, attr_name+"_historyLen", historyLen)
        setattr(self, attr_name+"_history", None)
        self._subscribers.append(rospy.Subscriber(topic_name, Vector, self.callback, attr_name, queue_size = 1))
        print 'Subscribe to topic ' + topic_name + 'accecible via member '+ attr_name
        
    def callback(self, ros_data, attr_name):
        '''Callback function of subscribed topic. '''
        setattr(self, (attr_name), ros_data.data)
        N = getattr(self, attr_name+"_historyLen")
        if N >0:
          hist = getattr(self, attr_name+"_history")
          if hist == None:
            setattr(self, attr_name+"_history",np.array([ros_data.data]))
          else:
            setattr(self, attr_name+"_history",np.append([ros_data.data],hist[:N],axis=0));  

    #~ def callback_sync(self, ros_data,attr_names):
        #~ print 'yo mother fucker ! '
        #~ print args
#~ 
    #~ def addSynchronisedSubscribers(self,topic_names, attr_names, historyLen = None):
        #~ '''Subscribe to multiple topics to be read syncronously and create members of your choise to store received data'''
        #~ print 'Subscribe to syncronized topics: '
        #~ sub = []
        #~ for topic_name,attr_name,  in zip(topic_names, attr_names):
          #~ setattr(self, attr_name, None)
          #~ setattr(self, attr_name+"_historyLen", historyLen)
          #~ setattr(self, attr_name+"_history", None)
          # self._subscribers.append(rospy.Subscriber(topic_name, Vector, self.callback, attr_name, queue_size = 1))
          #~ print '  * ' + topic_name + ' accecible via member '+ attr_name
          #~ sub.append(message_filters.Subscriber(topic_name, Vector))
        #~ ts = message_filters.TimeSynchronizer(sub, 10)
        #~ ts.registerCallback(self.callback_sync,topic_names)        
        #~ self._ts.append(ts)


def set_ros_master_uri(uri="http://hrp2014c:11311"):
    os.environ["ROS_MASTER_URI"] = uri


#TESTs 
def main(args):
    '''Initializes and cleanup ros node'''
    #~ set_ros_master_uri(uri="http://hrp2014c:11311")
    rospy.init_node('listener', anonymous=True)    
    ros = RosTopic2Vector()
    ros.addSubscriber('estimator_jointsVelocities','dq')
    ros.addSubscriber('estimator_jointsTorques','tau',5)
    ros.addSubscriber('estimator_currentFiltered','i',1)
    #~ ros.addSynchronisedSubscribers(['estimator_jointsVelocities','estimator_jointsTorques','estimator_currentFiltered'],['dq','tau','i'])
    '''Prepare plot'''
    fig, ax = plt.subplots()
    plt.plot(np.random.randn(36))
    line, = ax.plot(np.random.randn(36))
    plt.show(block=False)        

    rate = rospy.Rate(1) # hz
    while(1):
        print ros.tau
        #~ print ros.tau_history
        #~ line.set_ydata(ros.q)
        #~ line.set_xdata(range(36))
        #~ ax.draw_artist(ax.patch)
        #~ ax.draw_artist(line)
        #~ fig.canvas.draw()
        #~ fig.canvas.flush_events()
        rate.sleep()
if __name__ == '__main__':
    main(sys.argv)







