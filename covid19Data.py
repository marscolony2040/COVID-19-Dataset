import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import requests
import json


from matplotlib import rcParams

rcParams['figure.autolayout'] = True
fig = plt.figure(figsize=(10, 5), dpi=120)
ax=fig.add_subplot(111)#, projection='3d')
fig.patch.set_facecolor('black')
ax.set_facecolor('black')
ax.tick_params(axis='x', colors='yellow')
ax.tick_params(axis='y', colors='yellow')

fig.tight_layout()

r = requests.get('https://covid19-api.weedmark.systems/api/v1/stats').json()

data = r['data']['covid19Stats']

lk = lambda t: [p[t] for p in data]

feed = pd.DataFrame(data=[[p['keyId'], float(p['confirmed']), float(p['deaths']), float(p['recovered'])] for p in data if len(p['province']) == 0], columns=['ID','Confirmed','Deaths','Recovered'])

feed = feed.sort_values(by='Confirmed')


confirmed = feed['Confirmed'].values
deaths = feed['Deaths'].values
recovered = feed['Recovered'].values


for k, x, y, z in zip(feed['ID'].values, confirmed, deaths, recovered):
    ax.scatter(x, y, color='red' if z/(x+0) <= 0.4 else 'limegreen', s=int(z/np.sum(recovered)*(x-y)/100+4))
    ax.set_title("COVID-19: John Hopkins Dataset", color='magenta', fontsize=15)
    ax.annotate(k, (x, y), color='cyan', fontsize=10)
    ax.set_xlabel("Confirmed Cases", color='magenta')
    ax.set_ylabel("Confiremd Deaths", color='magenta')

    plt.pause(0.0001)




plt.show()
