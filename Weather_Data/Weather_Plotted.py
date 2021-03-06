"""
Name: Michael Moore
Date: 3/3/2021
Program: Weather_Plotted
This program compares snow totals from different states using visualization and dataframes.
"""

import matplotlib.pyplot as plt
from Weather_Data import Minnesota_Weather as ms
from Weather_Data import Iowa_Weather as ia

fig, axs = plt.subplots(8)
axs[0].plot(ia.old_dates_snow['SNOW'], color='y')
axs[0].xaxis.set_visible(False)
axs[0].set_title("2021-01 Snow Totals Iowa")

axs[1].plot(ms.old_dates_snow['SNOW'], color='y')
axs[1].xaxis.set_visible(False)
axs[1].set_title("2021-01 Snow Totals Minnesota")

axs[2].plot(ia.old_dates_rain['PRCP'], color='r')
axs[2].xaxis.set_visible(False)
axs[2].set_title("2021-01 Rain Totals Iowa")

axs[3].plot(ms.old_dates_rain['PRCP'], color='r')
axs[3].xaxis.set_visible(False)
axs[3].set_title("2021-01 Rain Totals Minnesota")

axs[4].plot(ia.new_dates_snow['SNOW'],color='b')
axs[4].xaxis.set_visible(False)
axs[4].set_title("2021-02 Snow Totals Iowa")

axs[5].plot(ms.new_dates_snow['SNOW'],color='b')
axs[5].xaxis.set_visible(False)
axs[5].set_title("2021-02 Snow Totals Minnesota")

axs[6].plot(ms.new_dates_rain['PRCP'],color='g')
axs[6].xaxis.set_visible(False)
axs[6].set_title("2021-02 Rain Totals Iowa")

axs[7].plot(ia.new_dates_rain['PRCP'],color='g')
axs[7].xaxis.set_visible(False)
axs[7].set_title("2021-02 Rain Totals Iowa")

ms_new_df = ms.new_df.sort_values(by=['PRCP', 'SNOW'])
ms_new_df = ms_new_df.head()
ms_new_df.plot(kind="bar")

ia_new_df = ia.new_df.sort_values(by=['PRCP', 'SNOW'])
ia_new_df = ia_new_df.head()
ia_new_df.plot(kind="bar")


plt.show()