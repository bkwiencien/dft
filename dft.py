import numpy as np
import matplotlib.pyplot as plotter
import pdb
def addNoise(ain):
    #pdb.set_trace()
    array = np.random.uniform(-3,3,ain.size)
    return (np.add(ain,array))
def getif(xin):
    done = False
    res = 0
    while (done  == False):
      print("enter {} frequency value between 1 and 100".format(xin))
      try:
        res = int(input())
        done = True
      except:
        print("must be an integer")
      if (res >100) or (res<1):
        done=False
        print("Frequency must be between 1 and 101")
    return (res)    
def doit():
#  
  samplingFrequency   = 100 
# 
  samplingInterval       = 1 / samplingFrequency;
# 
  beginTime           = 0; 
# 
  endTime             = 10; 

  signal1Frequency     = getif('first');
  print ("signal1Frequency {}".format(signal1Frequency))
  signal2Frequency     = getif('second');
  print ("signal2Frequency {}".format(signal2Frequency))  

  time        = np.arange(beginTime, endTime, samplingInterval);
# 
  amplitude1 = np.sin(2*np.pi*signal1Frequency*time)
  amplitude2 = np.sin(2*np.pi*signal2Frequency*time) 
# Create subplot
  figure, axis = plotter.subplots(5, 1)
  #pdb.set_trace()
  plotter.subplots_adjust(hspace=1)
  F = plotter.gcf()
  DPI = F.get_dpi()
  DefaultSize = F.get_size_inches()
  F.set_size_inches( (DefaultSize[0]*4, DefaultSize[1]*4) )
# Time domain representation for sine wave 1
  axis[0].set_title('Sine wave with a frequency of {} Hz'.format(signal1Frequency),fontdict = {'fontsize' : 20})
  axis[0].plot(time, amplitude1)
  axis[0].set_xlabel('Time')
  axis[0].set_ylabel('Amplitude')  
# Time domain representation for sine wave 2
  axis[1].set_title('Sine wave with a frequency of {} Hz'.format(signal2Frequency),fontdict = {'fontsize' : 20})
  axis[1].plot(time, amplitude2)
  axis[1].set_xlabel('Time')
  axis[1].set_ylabel('Amplitude') 
# Add the sine waves
  amplitude = amplitude1 + amplitude2 
# Time domain representation of the resultant sine wave
  axis[2].set_title('Sine wave with multiple frequencies',fontdict = {'fontsize' : 20})
  axis[2].plot(time, amplitude)
  axis[2].set_xlabel('Time',fontdict = {'fontsize' : 20})
  axis[2].set_ylabel('Amplitude',fontdict = {'fontsize' : 20}) 
# with noise added
  amplitude = addNoise(amplitude) 
  axis[3].set_title('With noise',fontdict = {'fontsize' : 20})
  axis[3].plot(time, amplitude)
  axis[3].set_xlabel('Time',fontdict = {'fontsize' : 20})
  axis[3].set_ylabel('Amplitude',fontdict = {'fontsize' : 20}) 
# Frequency domain representation
  fourierTransform = np.fft.fft(amplitude)/len(amplitude)           
  fourierTransform = fourierTransform[range(int(len(amplitude)/2))] 
  #pdb.set_trace()
  tpCount     = len(amplitude)
  values      = np.arange(int(tpCount/2))
  timePeriod  = tpCount/samplingFrequency
  frequencies = values/timePeriod 
# Frequency domain representation
  axis[4].set_title('Fourier transform depicting the frequency components',fontdict = {'fontsize' : 20}) 
  axis[4].plot(frequencies, abs(fourierTransform))
  axis[4].set_xlabel('Frequency',fontdict = {'fontsize' : 20})
  axis[3].set_ylabel('Amplitude',fontdict = {'fontsize' : 20}) 
  axis[4].set_xticks(np.arange(0, 100, step=1.0)) 
  plotter.show()
if (__name__=="main"):
    doit()