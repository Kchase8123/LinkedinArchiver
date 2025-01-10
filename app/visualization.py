# app/visualization.py
import matplotlib.pyplot as plt

def visualize_data(data):
    # Example: Plotting the number of transfers over time
    dates = [d['date'] for d in data]
    counts = [d['count'] for d in data]
    plt.plot(dates, counts)
    plt.xlabel('Date')
    plt.ylabel('Number of Transfers')
    plt.title('Transfers Over Time')
    plt.show()
