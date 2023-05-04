#!/usr/bin/env python
# coding: utf-8

# # Freq vs Amp HD 23732

# ## Packages

# In[1]:


import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import numpy as np


# ## Crucial GLS Information

# In[2]:


"""
Best sine frequency:  0.149829 +/- 0.000132
Best sine period:     6.674283 +/- 0.005896
Amplitude:            0.000358 +/- 0.000005
Phase (ph):           0.466124 +/- 0.002074
Phase (T0):           2444.579793 +/- 0.013845
Offset:               1.000055 +/- 0.000003
"""


# In[3]:


# read in gls file
FvA = np.loadtxt('results.csv', unpack = True)
freq = FvA[0]
amp = FvA[1]
print(freq)

amperr = 0.000005
limit4 = amperr*4
limit3 = amperr*3
limit2 = amperr*2
limit1 = amperr
#print(limit)


# # Log Graphs

# In[4]:


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


# In[5]:


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

# In[6]:


fig = plt.figure(dpi = 1200)
plt.plot(freq, amp, 'k.',markersize = 1)
plt.axhline(y = limit4, color = 'r', linestyle = '-')
plt.ylim(limit4,0.002)
plt.xlabel('Frequency')
plt.ylabel('Amplitude')
plt.legend(['Data','4\u03C3'])

