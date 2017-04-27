DISPLAY_FPS = 25
N_PTS = 4000
jID = 2
#~ ROS_MASTER_URI = "http://localhost.laas.fr:11311"
#~ ROS_MASTER_URI = "http://hrp2014c.laas.fr:11311"
ROS_MASTER_URI = None

minTau,maxTau = -50, 50
mindq,maxdq =   -1, 1
mini,maxi =     -3, 3
TOPIC_NAME_dq  = 'jointsVelocities'
TOPIC_NAME_tau = 'jointsTorques'
TOPIC_NAME_i   = 'currentFiltered'
TOPIC_NAME_id  = 'i_des'  


