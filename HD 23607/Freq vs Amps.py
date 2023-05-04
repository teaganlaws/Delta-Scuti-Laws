#!/usr/bin/env python
# coding: utf-8

# # Freq vs Amp HD 23607

# ## Packages

# In[1]:


import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import numpy as np


# ## Crucial GLS Information

# In[2]:


"""
Best sine frequency:  38.372929 +/- 0.000070
Best sine period:     0.026060 +/- 0.000000
Amplitude:            0.001608 +/- 0.000011
Phase (ph):           -0.483827 +/- 0.001104
Phase (T0):           2447.703491 +/- 0.000029
Offset:               0.999998 +/- 0.000008
"""


# In[4]:


# read in gls file
FvA = np.loadtxt('results.csv', unpack = True)
freq = FvA[0]
amp = FvA[1]
print(freq)

amperr = 0.000011
limit4 = amperr*4
limit3 = amperr*3
limit2 = amperr*2
limit1 = amperr
#print(limit)


# # Log Graphs

# In[25]:


fig = plt.figure(dpi = 1200)
plt.plot(freq, amp, 'k.',markersize = 1)
plt.axhline(y = limit4, color = 'r', linestyle = '-')
plt.axhline(y = limit3, color = 'g', linestyle = '-')
plt.axhline(y = limit2, color = 'c', linestyle = '-')
plt.axhline(y = limit1, color = 'm', linestyle = '-')
plt.yscale('log')
plt.xlabel('Frequency')
plt.ylabel('Amplitude')
plt.legend(['Data','4\u03C3','3\u03C3','2\u03C3','\u03C3'])

#plt.savefig('FvA.jpg', format='jpg')


# In[27]:


fig = plt.figure(dpi = 1200)
plt.plot(freq, amp, 'k.',markersize = 1)
plt.axhline(y = limit4, color = 'r', linestyle = '-')
plt.yscale('log')
plt.xlim(26,27.5)
plt.ylim(1e-05,1e-02)
plt.xlabel('Frequency')
plt.ylabel('Amplitude')
plt.legend(['Data','4\u03C3'])


# # Linear Graphs

# In[26]:


fig = plt.figure(dpi = 1200)
plt.plot(freq, amp, 'k.',markersize = 1)
plt.axhline(y = limit4, color = 'r', linestyle = '-')
plt.ylim(limit4,0.002)
plt.xlabel('Frequency')
plt.ylabel('Amplitude')
plt.legend(['Data','4\u03C3'])

