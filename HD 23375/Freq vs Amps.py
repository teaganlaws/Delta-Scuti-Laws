#!/usr/bin/env python
# coding: utf-8

# # Freq vs Amp HD 23375

# ## Packages

# In[1]:


import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import numpy as np


# ## Crucial GLS Information

# In[2]:


"""
Best sine frequency:  3.048693 +/- 0.000089
Best sine period:     0.328009 +/- 0.000010
Amplitude:            0.000484 +/- 0.000004
Phase (ph):           0.464665 +/- 0.001405
Phase (T0):           2447.538500 +/- 0.000461
Offset:               0.999999 +/- 0.000003
"""


# In[3]:


# read in gls file
FvA = np.loadtxt('results.csv', unpack = True)
freq = FvA[0]
amp = FvA[1]
print(freq)

amperr = 0.000004
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
plt.xlim(2.5,3.5)
plt.ylim(1e-05,1e-02)
plt.xlabel('Frequency')
plt.ylabel('Amplitude')
plt.legend(['Data','4\u03C3'])


# # Linear Graphs

# In[9]:


fig = plt.figure(dpi = 1200)
plt.plot(freq, amp, 'k.',markersize = 1)
plt.axhline(y = limit4, color = 'r', linestyle = '-')
plt.ylim(limit4,0.001)
plt.xlabel('Frequency')
plt.ylabel('Amplitude')
plt.legend(['Data','4\u03C3'])

