import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def main():
    weekly_df = pd.read_excel("india_unemployment.xlsx",
                              sheet_name="weekly unemployment")

    df_melt = weekly_df.melt(id_vars='Date', value_vars=['Estimated Unemployment Rate (%): total', 'Estimated Unemployment Rate (%): urban', 'Estimated Unemployment Rate (%): rural'])
    # px.line(weekly_df, x="Date", y="Estimated Unemployment Rate (%): total")
    # px.line(weekly_df, x="Date", y="Estimated Unemployment Rate (%): urban")
    fig, ax = plt.subplots()
    sns.lineplot(data=df_melt, x="Date", y="value", hue='variable', ax=ax)
    ax.set_ylabel("percentage")
    ax.set_title("unemployment rate timeseries")
    fig.savefig("viz/weekly_unemployment.png")
    plt.close(fig)


if __name__ == '__main__':
    main()