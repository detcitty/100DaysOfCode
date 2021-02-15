import numpy as np
import pandas as pd
import scipy.stats as stats
import  statsmodels.stats.api as sms
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
from math import ceil

#%matplotlib inline

plt.style.use('seaborn-whitegrid')
font = {
    'family' : 'Helvetica',
    'weight' : 'bold',
    'size'   : 14
    }
mpl.rc('font', **font)
effect_size = sms.proportion_effectsize(0.13, 0.15)

required_n = sms.NormalIndPower().solve_power(
    effect_size, 
    power=0.8, 
    alpha=0.05, 
    ratio=1
    )

required_n = ceil(required_n)

print(required_n)
