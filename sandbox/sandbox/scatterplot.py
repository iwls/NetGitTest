
import numpy as np
import matplotlib.pyplot as plt


N = 50
x = np.random.rand(N) ## this generates N random numbers between 0.00000000 and 0.99999999
y = np.random.rand(N) ## this generates N random numbers between 0.00000000 and 0.99999999
colors = np.random.rand(N) ## this generates N random numbers between 0.00000000 and 0.99999999
area = np.pi * (15 * np.random.rand(N))**2  # 0 to 15 point radiuses

plt.scatter(x, y, s=area, c=colors, alpha=0.5)
plt.show()



###this code works together with the online platform of plotly
#import matplotlib.pyplot as plt
#import plotly.plotly as py
#import numpy as np

## Learn about API authentication here: https://plot.ly/python/getting-started
## Find your api_key here: https://plot.ly/settings/api

#fig, ax = plt.subplots()
#ax.scatter(np.linspace(-1, 1, 50), np.random.randn(50))

#plot_url = py.plot_mpl(fig, filename="mpl-scatter")


