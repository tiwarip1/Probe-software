# =============================================================================
# import visa
# 
# '''Start with a resource manager, which shows the connections to the computer
# and some properties about them'''
# rm = visa.ResourceManager()
# print(rm.list_resources())
# 
# '''Select one of the items from that list to be looked at'''
# inst = rm.open_resource("ASRL1::INSTR")
# print(inst)
# 
# print(inst.query('attr nothing'))
# =============================================================================


import ctypes
import numpy
from string import *

nidaq = ctypes.windll.nicaiu # load the DLL

##############################
# Setup some typedefs and constants
# to correspond with values in
# C:\Program Files\National Instruments\NI-DAQ\DAQmx ANSI C Dev\include\NIDAQmx.h

# the typedefs
int32 = ctypes.c_long
uInt32 = ctypes.c_ulong
uInt64 = ctypes.c_ulonglong
float64 = ctypes.c_double
TaskHandle = uInt32

buf_size = 10
buf = ctypes.create_string_buffer('\000' * buf_size)
#nidaq.DAQmxGetErrorString(err,ctypes.byref(buf),buf_size)

#nidaq.DAQmxGetSysDevNames(char *data, uInt32 bufferSize);
nidaq.DAQmxGetSysDevNames(buf, buf_size);
#print(ctypes.sizeof(buf), repr(buf.raw))
print(buf.raw)