import pandas as pd
import matplotlib
from numpy.random import randn
import matplotlib.pyplot as plt
import matplotlib.pylab as pylab
from matplotlib.ticker import FuncFormatter

params = {'legend.fontsize': 'x-large',
          'figure.figsize': (15, 5),
         'axes.labelsize': 'x-large',
         'axes.titlesize':'x-large',
         'xtick.labelsize':'x-large',
         'ytick.labelsize':'x-large'}
pylab.rcParams.update(params)


def to_percent(y, position):
    # Ignore the passed in position. This has the effect of scaling the default
    # tick locations.
    s = str(100 * y)

    # The percent symbol needs escaping in latex
    if matplotlib.rcParams['text.usetex'] is True:
        return s + r'$\%$'
    else:
        return s + '%'


csv_file = 'normal.csv'
df1 = pd.read_csv(csv_file, skiprows=range(6))

x1 = df1.usr + df1.sys
plt.hist(x1, bins=25, normed=True, alpha=0.5, label = "Data Storage")

csv_file2 = 'local.csv'
df2 = pd.read_csv(csv_file2, skiprows=range(6))
x2 = df2.usr + df2.sys

plt.hist(x2, bins=25, normed=True, alpha=0.5, label= "Data Processing and Storage")
formatter = FuncFormatter(to_percent)
plt.gca().yaxis.set_major_formatter(formatter)

plt.ylim([0, 0.21])

plt.xlabel("CPU Usage (%)")
plt.ylabel("Density")
plt.legend(loc='upper right')

plt.show()