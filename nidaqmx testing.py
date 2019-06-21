import nidaqmx
import matplotlib.pyplot as plt
import numpy as np
import time

tock = time.time()
Samples_Per_Ch_To_Read = 500 

  
with nidaqmx.Task() as task:
    task1 = task
    
    task1.ai_channels.add_ai_voltage_chan("Dev2/ai2")    

    #task.timing.cfg_samp_clk_timing(10000, u'',10280,10178,20) 
    
    data = task1.read(Samples_Per_Ch_To_Read )
    
    task.ai_channels.add_ai_voltage_chan("Dev2/ai3")
    
    data2 = task.read(Samples_Per_Ch_To_Read )

tick=time.time()
print('The program took {}s to run'.format(round(tick-tock,4)))

plt.plot(data2[1],data2[0])