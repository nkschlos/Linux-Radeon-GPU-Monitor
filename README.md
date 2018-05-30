# Linux-Radeon-GPU-Monitor
A simple GPU resource monitor for Radeon devices on Linux using Python

![alt text](https://github.com/nkschlos/Linux-Radeon-GPU-Monitor/blob/master/screenshot.png?raw=true)
Here is a screenshot of the monitor (left) running next to the system monitor's resource tab on gnome (right).

This program is a simple tool for monitoring the GPU usage for Radeon GPUs on linux systems.
At the time of my writing this, I could only find one tool to display this info, radeontop, and it runs in the terminal and isn't pretty.

This program runs radeontop, but instead of displaying the info graphically, it tells it to continually dump the data to a text file, then reads the text file and plots the results with matplotlib.

The dependencies for this program are *radeontop* installed on your linux distro
and *matplotlib*, *numpy*, *time*, *io*, *re*, and *os* installed on python.

To customize this for your build, you will want to

1. make sure the os.system commands will run. I have my distro set up to not prompt for password for "sudo," so this works for me.
   you may need to remove the "sudo" from these commands and run python as root. 'Radeontop', 'rm', and 'pkill' all require permissions.
2. customize it to your liking by adjusting the matplotlib settings. 
   There is a lot more information stored in data you could plot, but I was only interested in GPU and VRAM usage.
   Open data.txt in a file editor to see what is available.

**Scaling:** absolute vs. autoscale:
   * The scaling is by default absolute scaled, but you can make it autoscaled by removing lines 105 and 120
   * As for the horizontal scale, it is by default a rolling time scale, logging one minute. If you want it to cumulitively show all the data collected, delete lines 83 and 84.


I don't claim for this to be stable, fleshed-out, or concise, as I am not really a programmer.
It's a simple tool that I wrote because I wanted it, and you might like it as well.

Enjoy,
Noah Schlossberger
May 2018
