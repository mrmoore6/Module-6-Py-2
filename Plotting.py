"""
Name: Michael Moore
Date: 3/3/21

This is a visualization of Steam_Store_Analysis_copy.
"""
from DATASET.Steam_Store_Analysis_copy import pd_copy
import matplotlib.pyplot as plt
df = pd_copy('steam_copy.csv')
df = df.reset_index()
df.plot(x="publisher", y="positive_ratings",  kind="bar")
fig, axs = plt.subplots(2,2, gridspec_kw={'width_ratios':[3,3],'height_ratios':[3,3]})

axs[0,0].plot(df['positive_ratings'],color='b')
axs[0,0].axes.get_xaxis().set_visible(False)
axs[0,0].title.set_text("Positive Ratings")
axs[0,0].set_ylim([df['positive_ratings'].min(), df['positive_ratings'].max()])


axs[0,1].plot(df['negative_ratings'],color='g')
axs[0,1].axes.get_xaxis().set_visible(False)
axs[0,1].title.set_text("Negative Ratings")

axs[1,0].plot(df['positive_percentile'],color='r')
axs[1,0].axes.get_xaxis().set_visible(False)
axs[1,0].title.set_text("Positive Percentile")
axs[1,0].set_ylim([df['positive_percentile'].min(), df['positive_percentile'].max()])

axs[1,1].plot(df['negative_percentile'], color='y')
axs[1,1].axes.get_xaxis().set_visible(False)
axs[1,1].title.set_text("Negative Percentile")
axs[1,1].set_ylim([df['negative_percentile'].min(),df['negative_percentile'].max()])

plt.show()
