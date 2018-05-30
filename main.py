'''
Linux-Radeon-GPU-Monitor
A simple GPU resource monitor for Radeon devices on Linux using Python

The dependencies for this program are radeontop installed on your linux distro
and matplotlib, numpy, time, io, re, and os installed on python.

To customize this for your build, you will want to

1. Make sure the os.system commands will run. I have my distro set up to not prompt for password for "sudo," so this works for me.
   You may need to remove the "sudo" from these commands and run python as root. Radeontop, rm, and pkill all require permissions.
2. Customize it to your liking by adjusting the matplotlib settings.
   There is a lot more information stored in data you could plot, but I was only interested in GPU and VRAM usage.
   Open data.txt in a file editor to see what is available.

I don't claim for this to be stable, fleshed-out, or concise as I am not really a programmer.
It's a simple tool that I wrote because I wanted it, and you might like it as well.
Enjoy
Noah Schlossberger
May 2018
'''

import os
import re
import io
import time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib as mpl

# initialize radeontop and files

# close radeontop if already running
os.system("sudo pkill radeontop")
#  set path as current location for data file that radeontop writes
dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)
path = dir_path + "/data.txt"
print(path)
path_open= path.replace('/','\\')
# delete file if already exists
os.system("sudo rm " + path)
# start radeontop and dump data to file
os.system("sudo radeontop -d " + path + " &")
# wait two seconds to make sure entries exist before we read them
time.sleep(2)

# initialize matplotlib objects

# set matplotlib toolbar as hidden
mpl.rcParams['toolbar']='None'
#initalize our figure
fig = plt.figure()
#name the matplotlib window
fig.canvas.set_window_title('GPU Monitor')

fig.set_facecolor('#333333')
# add subplot 1 (gpu usage)
ax = fig.add_subplot(2,1,1)
ax.set_facecolor('#212121')
# add subplot 2 (vram usage)
ax2 = fig.add_subplot(2,1,2)
ax2.set_facecolor('#212121')

# create our main animation loop

def animate(i):
    #import data from  (every other line)
    with open('data.txt', 'r') as myfile:
        data=myfile.readlines()[::2]
    data = ''.join(data)
    #replace symbols with delimiters
    data = data.replace('%',',').replace(':',',')
    #remove letters
    data = re.sub('[abcdefghijklmnopqrstuvwxyz]','',data)
    #convert data to io string so that numpy can handle it
    data = io.StringIO(data)
    #generate numpy array from the data
    data = np.genfromtxt(data,delimiter=',')
    #if the program has taken more than 62 samples, keep only the last 61 samples
    #(remove this if statement to keep and plot all collected data, rather than rolling)
    if (data[:,1].size > 62):
        data = data[-61:,:]
    #get vectors from data

    vram = data[:,23]
    #vram_absolute = data[:,24] #uncomment if you want to add this plot as well
    gpu = data[:,1]
    times = data[:,0] - data[0,0]

    #plot gpu usage

    ax.clear()
    ax.plot(times,gpu)
    #ax.set_xlabel('time(s)',color='#777777') #uncomment for x axis label
    ax.set_ylabel('GPU usage (%)',color='#777777')
    ax.grid(True, 'major', 'both', color='#404040', linestyle='-', linewidth=.5)
    ax.tick_params(colors='#777777')

    ax.spines['top'].set_color('#777777')
    ax.spines['bottom'].set_color('#777777')
    ax.spines['left'].set_color('#777777')
    ax.spines['right'].set_color('#777777')
    ax.set_ylim(0,100) #set scale absolute, remove for autoscale

    #plot vram usage

    ax2.clear()
    ax2.plot(times,vram)
    #ax2.set_xlabel('times(s)',color='#777777')
    ax2.set_ylabel('VRAM usage (%)',color='#777777')
    ax2.grid(True, 'major', 'both', color='#404040', linestyle='-', linewidth=.5)
    ax2.tick_params(colors='#777777')

    ax2.spines['top'].set_color('#777777')
    ax2.spines['bottom'].set_color('#777777')
    ax2.spines['left'].set_color('#777777')
    ax2.spines['right'].set_color('#777777')
    ax2.set_ylim(0,100) #set scale absolute, remove for autoscale

#initalize animation
ani = animation.FuncAnimation(fig,animate,interval=1000)
plt.show()

#clean up
os.system("sudo pkill radeontop")
os.system("sudo rm " + path)
