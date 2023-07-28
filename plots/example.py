#######################
#Import dependencies
########################

import pandas as pd
import matplotlib.pyplot as plt
import mpld3

x = [1, 2, 3, 4, 5, 6]
y = [1, 4, 9, 16, 25, 36]

fig, ax1 = plt.subplots()
ax1.plot(x, y)



################################################
#Save the figure to our local machine
################################################

plt.savefig('example_plot.png')


# Transform to HTML code
html_str = mpld3.fig_to_html(fig)
Html_file= open("example_plot.html","w")
Html_file.write(html_str)
Html_file.close()
