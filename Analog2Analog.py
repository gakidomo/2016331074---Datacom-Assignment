# -*- coding: utf-8 -*-
"""Analog_To_Analog_Conversion_AM_FM_PM.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1X8mVAqDmCT_GyXEkn3FEZxnEYwXzB3RP
"""

import numpy as np
import matplotlib.pyplot as plt
import math

# Signal Plotting function
def plot_signal(t, s):
  '''
  t and x are time vector and signal respectively 
  '''
  plt.figure(figsize=(18, 6))
  plt.plot(t, s)
  plt.show()

"""##Amplitude Modulation(AM)

[Amplitude Modulation Tutorial](https://en.wikipedia.org/wiki/Amplitude_modulation)

----------------------------------
<br/>

**Amplitude modulation (AM)** is a modulation technique used in electronic communication, most commonly for transmitting messages with a radio wave.

### *In amplitude modulation:*
* The amplitude of the carrier signal is varied in proportion to that of the message signal.
* The carrier signal is modulated so that it's amplitude varies with the changing amplitudes of the modulating signal. 
* The frequency and phase of the carrier remain the same; only the amplitude changes to follow variations in the information.

<br/>

1. The carrier wave (sine wave) of frequency $f_{c}$ and amplitude $A$ is expressed by:

$$c(t)=Asin(2{\pi}f_{c}t)$$

2. The message signal, such as an audio signal that is used for modulating the carrier, is $m(t)$, and has a frequency $f_{m}$, 

$$m(t) = Mcos(2{\pi}f_{m}t+{\phi})$$
$$m(t) = Amcos(2{\pi}f_{m}t+{\phi}),$$

where $m$ is the amplitude sensitivity, $M$ is the amplitude of modulation. also, $M = A * m$.


3. Amplitude modulation results when the carrier $c(t)$ is multiplied by the positive quantity $(1 + \frac{m(t)}{A})$:

$$y(t) = [1 + \frac{m(t)}{A}]*c(t)$$
$$y(t) = [1 + \frac{Amcos(2{\pi}f_{m}t+{\phi})}{A}]*Asin(2{\pi}f_{c}t)$$
$$y(t) = [1 + mcos(2{\pi}f_{m}t+{\phi})]*Asin(2{\pi}f_{c}t)$$

<br/>

* For $m = 0.5$, carrier amplitude varies by 50% above (and below) its unmodulated level. For $m = 1.0$, it varies by 100%.


* [More details about AM](https://en.wikipedia.org/wiki/Amplitude_modulation)

###**Step 1: Creating Carrier Signal**
$$c(t)=Asin(2πfct)$$
"""

'''
a for Amplitude 
f for Frequency
t for time vector
ct for carrier signal
'''
a=2; 
f=0.5; 
t=np.arange(0, 50, 0.1)
ct=A*np.sin(2*np.pi*fc*t); 
plot_signal(t, ct)

"""###**Step 2: Creating message Signal**
$$m(t) = Mcos(2{\pi}f_{m}t+{\phi})$$
$$m(t) = Amcos(2{\pi}f_{m}t+{\phi})$$

where m = amplitude sensitivity => $\frac{\text{peak value of m(t)}}{A}$ => $\frac{m(t)}{A}$

and $M=A*m$
"""

'''
m for amplitude sensitivity
M for amplitude
f - frequency 
p - phase 
mt - modulating signal

we consider message signal here for forementioned parameters
'''
m = 1.0
M = A * m
f=.05
phase=0
mt=M*np.cos((2*np.pi*fm*t)+p)
plot_signal(t, mt)

"""###**Step 3: Computing Amplitude modulation**

$$y(t) = [1 + mcos(2{\pi}f_{m}t+{\phi})]*Asin(2{\pi}f_{c}t)$$

"""

'''
yt - Amplitude modulated signal
'''
yt=(1+m*np.cos((2*np.pi*fm*t) + phase))*A*np.sin(2*np.pi*fc*t);
plot_signal(t, yt)

"""##Frequency Modulation(FM)

[Frequency Modulation Tutorial](https://en.wikipedia.org/wiki/Frequency_modulation)

----------------------------------
<br/>

**Frequency modulation (FM)** is a modulation technique used in electronic communication, most commonly for transmitting messages with a radio wave.

### *In Frequency modulation:*
* The frequency of the carrier signal is modulated to follow the changing voltage level (amplitude) of the modulating signal.
* The amplitude and phase of the carrier remain the same; only the frequency changes to follow variations in the information.

<br/>

1. The carrier wave (sinusoidal carrier) with frequency $f_{c}$ and amplitude $A_{c}$ is expressed by:

$$x_{c}(t)=A_{c}cos(2{\pi}f_{c}t)$$

2. The modulating signal, such as an audio signal that is used for modulating the carrier, is $m(t)$, and has a frequency $f_{m}$.

$$x_{m}(t) = sin(2{\pi}f_{m}t)$$


3. Frequency modulation, the modulator combines the carrier with the modulating signal to get the transmitted signal,

$$y(t) = A_{c}cos(2{\pi} \int_{0}^{t} f({\tau}) \,d{\tau}) $$

$$y(t) = A_{c}cos(2{\pi} \int_{0}^{t} [f_{c}+f_{\Delta}x_{m}({\tau})]\,d{\tau}) $$

$$y(t) = A_{c}cos(2{\pi}[f_{c}t+2{\pi}f_{\Delta} \int_{0}^{t}x_{m}({\tau})]\,d{\tau}) $$

The integral of modulator signal is:

$$\int_{0}^{t}x_{m}({\tau})\,d{\tau} = \frac{sin(2{\pi}f_{m}t)}{2{\pi}f_{m}}$$

The expression for y(t) will becomes:

$$y(t) = A_{c}cos(2{\pi}[f_{c}t+2{\pi}f_{\Delta} \frac{sin(2{\pi}f_{m}t)}{2{\pi}f_{m}}]) $$

$$y(t) = A_{c}cos(2{\pi}[f_{c}t+ \frac{f_{\Delta}}{f_{m}} sin(2{\pi}f_{m}t)]) $$

$$y(t) = A_{c}cos(2{\pi}[f_{c}t+ msin(2{\pi}f_{m}t)]) $$

where $m=\frac{f_{\Delta}}{f_{m}}$ is the modulation index.

<br/>


* [More details about FM](https://en.wikipedia.org/wiki/Frequency_modulation)

###**Step 1: Creating Carrier Signal**
$$x_{c}(t)=A_{c}cos(2{\pi}f_{c}t)$$
"""

'''
Ac  - Amplitude of carrier signal
fc  - Frequency fo carrier signal
t   - Time vector for the signal
xc  - Carrier signal
'''
Ac=2; 
fc=40; 
t=np.arange(0, 1.0, 0.0001)
xc=Ac*np.cos(2*np.pi*fc*t); 
plot_signal(t, xc)

"""###**Step 2: Creating modulating signal**
$$x_{m}(t) = sin(2{\pi}f_{m}t)$$
"""

'''
m  - modulation index
fm - Frequency of message signal
xm - Modulating message signal
'''
m = 1.
fm=4
xm=np.sin((2*np.pi*fm*t))
plot_signal(t, xm)

"""###**Step 3: Computing Frequency modulation**

$$y(t) = A_{c}cos(2{\pi}[f_{c}t+ msin(2{\pi}f_{m}t)]) $$

"""

'''
yt - Frequency modulated signal
'''
# yt=Ac*np.cos((2*np.pi*fc*t) - (m * np.sin(2*np.pi*fm*t)))
yt = Ac*np.cos(2. * np.pi * (fc * t + m * np.sin(2*np.pi*fm*t)))
plot_signal(t, yt)

"""##Phase Modulation(PM)

[Phase Modulation Tutorial](https://en.wikipedia.org/wiki/Phase_modulation)

----------------------------------
<br/>

**Phase modulation (PM)** is a modulation technique used in electronic communication, most commonly for transmitting messages with a radio wave.

### *In Phase modulation:*
* The phase of a carrier signal is modulated to follow the changing signal level (amplitude) of the message signal.
* The amplitude and frequency of the carrier remain the same; only the phase changes to follow variations in the information.

<br/>

1. The carrier wave (sinusoidal carrier) with frequency $f_{c}$ and amplitude $A_{c}$ is expressed by:

$$c(t)=A_{c}sin(2{\pi}f_{c}t + {\phi_{c}})$$

2. The modulating signal, such as an audio signal that is used for modulating the carrier, is $m(t)$, and has a frequency $f_{m}$ and amplitude $A_{m}$.

$$m(t) = A_{m}sin(2{\pi}f_{m}t)$$


3. Phase modulation, the modulator combines the carrier with the modulating signal to get the transmitted signal,



$$y(t) = A_{c}sin(2{\pi}f_{c}t+ km(t) +{\phi_{c}})   $$

where $k$ is the modulation index.

<br/>


* [More details about PM](https://en.wikipedia.org/wiki/Phase_modulation)

###**Step 1: Creating Carrier Signal**

$$c(t)=A_{c}sin(2{\pi}f_{c}t + {\phi_{c}})$$
"""

'''
Ac - Amplitude of carrier signal
fc - Frequency fo carrier signal
t  - Time vector for the signal
phase - Phase of Carrier signal
ct - Carrier signal
'''
Ac=2; 
fc=2; 
t=np.arange(0, 3.0, 0.0001)
phase = 0
ct=Ac*np.sin(2*np.pi*fc*t + phase); 
plot_signal(t, ct)

"""###**Step 2: Creating message Signal**
$$m(t) = A_{m}sin(2{\pi}f_{m}t)$$
"""

'''
k  - amplitude sensitivity
fm - Frequency of message signal
Am - Amplitude of the message signal
mt - Modulating message signal
'''
k = 1.0
fm=3
Am = 2
mt=Am*np.sin(2 * np.pi*fm*t)
plot_signal(t, mt)

"""###**Step 3: Computing Phase modulation**

$$y(t) = A_{c}sin(2{\pi}f_{c}t+ km(t) +{\phi_{c}})   $$

"""

'''
yt - Phase modulated signal
'''
yt=Ac*np.sin((2*np.pi*fc*t) + (k * mt + phase))
plot_signal(t, yt)

"""**Thanks**"""