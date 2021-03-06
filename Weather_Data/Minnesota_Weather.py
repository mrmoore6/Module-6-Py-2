import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('2491073.csv', sep=',')

new_df = df.drop(["STATION","DSND","DSNW","EMSD","EMSN","EMXP"], axis=1)

new_df = new_df.set_index("NAME")
new_df = new_df.sort_index()
new_df = new_df.dropna()
max_snow_values = new_df['SNOW'].sort_values(ascending=False).head()

new_df_old_dates = new_df.loc[new_df["DATE"] == "2021-01"]
old_dates_snow = new_df_old_dates.sort_values(by="SNOW", ascending=True)
old_dates_rain = new_df_old_dates.sort_values(by="PRCP", ascending=True)

new_df_new_dates = new_df.loc[new_df["DATE"] == "2021-02"]
new_dates_snow = new_df_new_dates.sort_values(by='SNOW',ascending=True)
new_dates_rain = new_df_new_dates.sort_values(by="PRCP", ascending=True)
print(old_dates_snow)
print(new_dates_snow)

fig, axs = plt.subplots(4)
axs[0].plot(old_dates_snow['SNOW'], color='y')
axs[0].xaxis.set_visible(False)
axs[0].set_title("2021-01 Snow Totals Minnesota")

axs[1].plot(old_dates_rain['PRCP'], color='r')
axs[1].xaxis.set_visible(False)
axs[1].set_title("2021-01 Rain Totals Minnesota")

axs[2].plot(new_dates_snow['SNOW'],color='b')
axs[2].xaxis.set_visible(False)
axs[2].set_title("2021-02 Snow Totals Minnesota")

axs[3].plot(new_dates_rain['PRCP'],color='g')
axs[3].xaxis.set_visible(False)
axs[3].set_title("2021-02 Rain Totals Minnesota")

plt.show()