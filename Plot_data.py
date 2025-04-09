
import matplotlib.pyplot as plt
import pandas as pd

def plot_data(df):
    plt.clf()

    status_map = {
        'Good Service': 1,
        'Minor Delays': 2,
        'Severe Delays': 3,
        'Part Suspended': 4,
        'Planned Closure': 5
    }

    df['status_numeric'] = df['status'].map(status_map).fillna(0)  
    pivot = df.pivot(index='timestamp', columns='line', values='status_numeric')
    pivot = pivot.ffill()

    for col in pivot.columns:
        plt.plot(pivot.index, pivot[col], label=col)

    plt.xlabel('Time')
    plt.ylabel('Status (Numeric)')
    plt.title('Tube Line Status Over Time')
    plt.xticks(rotation=45)
    plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
    plt.tight_layout()
    plt.draw()
    plt.show()  
