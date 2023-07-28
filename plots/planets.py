# Plot planet positions w.r.t. Earth using SPICE kernels
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import pandas as pd
import matplotlib.pyplot as plt
import mpld3
import numpy as numpy
import planetmapper
from datetime import datetime

# Get current date and time
datetime_now = datetime.now()

# Plot wireframe of Saturn geometry w.r.t. Earth
body = planetmapper.Body('saturn', '2023-07-28')
body.plot_wireframe_radec()

# Add Titan to wireframe plot
body.add_other_bodies_of_interest('titan')
body.coordinates_of_interest_lonlat.append((360, -45)) # mark this specific coordinate (if visible) on any wireframe plots

# Make figure
fig, ax = plt.subplots(figsize=(3, 3), dpi=200)
body.plot_wireframe_radec(ax, color='white')
ax.set_title(str(datetime_now), color='white')

# Change colour of plot
ax.set_facecolor('#1a1919') # make plot background colour same as website background colour

# Save figure locally
plt.savefig('planets_plot.png')


# Transform to HTML code
html_str = mpld3.fig_to_html(fig)
Html_file= open("planets_plot.html","w")
Html_file.write(html_str)
Html_file.close()
