# -*- coding: utf-8 -*-
from pyqtgraph.Qt import QtGui, QtCore
import numpy as np
import pyqtgraph as pg
from IPython import embed
from hrp2_motors_parameters import *
from hrp2_names import *
from ros_utils import *
from PyQt4.QtGui import *
from config_plotLowLevelXY import *

if ROS_MASTER_URI != None :
  set_ros_master_uri(uri=ROS_MASTER_URI)
rospy.init_node('listener', anonymous=True)  
rosData = RosTopic2Vector()
rosData.addSubscriber('jointsVelocities','dq',N_PTS)
rosData.addSubscriber('jointsTorques','tau',N_PTS)
rosData.addSubscriber('currentFiltered','i',N_PTS)
rosData.addSubscriber('i_des','id',N_PTS)

win = pg.GraphicsWindow(title="Motor models")
#~ win.resize(1000,600)

win.setWindowTitle('Online motor model plot')
# Enable antialiasing for prettier plots
pg.setConfigOptions(antialias=True)

pIT = win.addPlot()
pIV = win.addPlot()
win.nextRow()
pIId = win.addPlot()
def redraw_model():
  global pIT,pIV, curveIT, curveIV, pointIT, pointIV, curveIId, pointIId, pIId
  #Plot IT
  pIT.clear()
  pIT.setTitle("I-Torque "+IdTolongName[jID])
  pIT.showGrid(x=True, y=True)
  pIT.setLabel('left', "Current", units='A')
  pIT.setLabel('bottom', "Torque", units='Nm')
  pIT.plot([minTau,maxTau],[Kt_p[jID]*minTau+Kf_p[jID] ,Kt_p[jID]*maxTau+Kf_p[jID]],pen=pg.mkPen('w', width=3))#,'g:',lw=5)
  pIT.plot([minTau,maxTau],[Kt_n[jID]*minTau-Kf_n[jID] ,Kt_n[jID]*maxTau-Kf_n[jID]],pen=pg.mkPen('w', width=3))#,'g:',lw=5)
  curveIT = pIT.plot(pen='y')
  pointIT = pIT.plot([0],[0], pg.mkPen('r', width=3), symbolBrush=(255,0,0), symbolPen='w')
  pIT.enableAutoRange('xy', False) 

  #Plot IV
  pIV.clear()
  pIV.setTitle("I-dq "+IdTolongName[jID])
  pIV.showGrid(x=True, y=True)
  pIV.setLabel('left', "Current", units='A')
  pIV.setLabel('bottom', "Velocity", units='rad/s')
  pIV.plot([0.0,maxdq],[ Kf_p[jID],Kv_p[jID]*maxdq+Kf_p[jID]],pen=pg.mkPen('w', width=3))#,'g:',lw=5)
  pIV.plot([0.0,mindq],[-Kf_n[jID],Kv_n[jID]*mindq-Kf_n[jID]],pen=pg.mkPen('w', width=3))#,'g:',lw=5)
  curveIV = pIV.plot(pen='y')
  pointIV = pIV.plot([0],[0], pen=(200,200,200), symbolBrush=(255,0,0), symbolPen='w')
  pIV.enableAutoRange('xy', False) 

  #Plot IId
  pIId.clear()
  pIId.setTitle("I-Id "+IdTolongName[jID])
  pIId.showGrid(x=True, y=True)
  pIId.setLabel('left', "Current", units='A')
  pIId.setLabel('bottom', "Control Current", units='A')
  pIId.plot([-5.0,5.0],[-5.0,5.0],pen=pg.mkPen('w', width=3))#,'g:',lw=5)
  #~ pIId.plot([0.0,mindq],[-Kf_n[jID],Kv_n[jID]*mindq-Kf_n[jID]],pen=pg.mkPen('w', width=3))#,'g:',lw=5)
  curveIId = pIId.plot(pen='y')
  pointIId = pIId.plot([0],[0], pen=(200,200,200), symbolBrush=(255,0,0), symbolPen='w')
  pIId.enableAutoRange('xy', False) 

redraw_model()

def update():
    global rosData
    
    # Update Plot IT
    global curveIT, pointIT
    try:
      y=rosData.i_history[:,jID].T
      x=rosData.tau_history[:,jID].T
      minlen = min(len(x),len(y))
      curveIT.setData(x[0:minlen] ,y[0:minlen])
      pointIT.setData([x[0]],[y[0]])    
    except(TypeError):
      pass
      
    # Update Plot IV
    global curveIV, pointIV
    try:
      y=rosData.i_history[:,jID].T
      x=rosData.dq_history[:,jID].T
      minlen = min(len(x),len(y))
      curveIV.setData(x[0:minlen] ,y[0:minlen])
      pointIV.setData([x[0]],[y[0]])
    except(TypeError):
      pass
      
    # Update Plot IId
    global curveIId, pointIId
    try:
      y=rosData.i_history[:,jID].T
      x=rosData.id_history[:,jID].T
      minlen = min(len(x),len(y))
      curveIId.setData(x[0:minlen] ,y[0:minlen])
      pointIId.setData([x[0]],[y[0]])
    except(TypeError):
      pass
      
      
timer = QtCore.QTimer()
timer.timeout.connect(update)
timer.start(1000./DISPLAY_FPS)
win.nextRow()
while(1):
    try:
      i = int(raw_input("Enter a joint ID: "))
      if i < 0 or i >= NBj : raise ValueError
      jID=i
      redraw_model()      
      print '  Plotting data for: ' + IdTolongName[jID]
    except ValueError:
      print '  invalid joint ID'

#~ embed()

## Start Qt event loop unless running in interactive mode or using pyside.
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()

        embed()
