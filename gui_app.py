import tkinter as tk
from tkinter import ttk
import random
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class EdgeSenseGUI:
    def __init__(self, root):
        self.root = root
        self.root.title('EdgeSense IoT Fleet Visualizer & Anomaly Detector')
        self.root.geometry('1200x800')
        self.root.configure(bg='#2d2d2d')

        self.create_widgets()

    def create_widgets(self):
        # Header
        header = ttk.Label(self.root, text='EdgeSense IoT Fleet Visualizer', font=('Helvetica', 20), background='#2d2d2d', foreground='white')
        header.pack(pady=10)

        # Main Frame
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Geo-Map Frame
        map_frame = ttk.Frame(main_frame, width=600, height=400)
        map_frame.grid(row=0, column=0, padx=10, pady=10)
        map_label = ttk.Label(map_frame, text='Geo-Map', font=('Helvetica', 16), background='#2d2d2d', foreground='white')
        map_label.pack()

        # Sensor Data Dashboard Frame
        dashboard_frame = ttk.Frame(main_frame, width=600, height=400)
        dashboard_frame.grid(row=0, column=1, padx=10, pady=10)
        dashboard_label = ttk.Label(dashboard_frame, text='Sensor Data Dashboard', font=('Helvetica', 16), background='#2d2d2d', foreground='white')
        dashboard_label.pack()

        # Gauges
        self.create_gauges(dashboard_frame)

        # Charts
        self.create_charts(dashboard_frame)

        # Anomaly Detection Alerts
        alert_frame = ttk.Frame(main_frame, width=1200, height=100)
        alert_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
        alert_label = ttk.Label(alert_frame, text='Anomaly Detection Alerts', font=('Helvetica', 16), background='#2d2d2d', foreground='white')
        alert_label.pack()

        self.create_alerts(alert_frame)

        # Predictive Analytics Frame
        analytics_frame = ttk.Frame(main_frame, width=1200, height=100)
        analytics_frame.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
        analytics_label = ttk.Label(analytics_frame, text='Predictive Analytics for Fleet Health', font=('Helvetica', 16), background='#2d2d2d', foreground='white')
        analytics_label.pack()

        self.create_analytics(analytics_frame)

    def create_gauges(self, parent):
        gauge_frame = ttk.Frame(parent)
        gauge_frame.pack()

        temp_gauge = ttk.Label(gauge_frame, text='Temperature: 25°C', font=('Helvetica', 14), background='#2d2d2d', foreground='white')
        temp_gauge.pack()

        humidity_gauge = ttk.Label(gauge_frame, text='Humidity: 60%', font=('Helvetica', 14), background='#2d2d2d', foreground='white')
        humidity_gauge.pack()

    def create_charts(self, parent):
        chart_frame = ttk.Frame(parent)
        chart_frame.pack()

        fig, ax = plt.subplots(figsize=(5, 3))
        ax.plot([1, 2, 3, 4], [10, 20, 25, 30], color='white', linewidth=2)
        ax.set_facecolor('#2d2d2d')
        ax.spines['bottom'].set_color('white')
        ax.spines['top'].set_color('white')
        ax.spines['right'].set_color('white')
        ax.spines['left'].set_color('white')
        ax.tick_params(axis='x', colors='white')
        ax.tick_params(axis='y', colors='white')

        canvas = FigureCanvasTkAgg(fig, master=chart_frame)
        canvas.draw()
        canvas.get_tk_widget().pack()

    def create_alerts(self, parent):
        alert_frame = ttk.Frame(parent)
        alert_frame.pack()

        alert = ttk.Label(alert_frame, text='No anomalies detected', font=('Helvetica', 14), background='green', foreground='white')
        alert.pack()

    def create_analytics(self, parent):
        analytics_frame = ttk.Frame(parent)
        analytics_frame.pack()

        analytics = ttk.Label(analytics_frame, text='Fleet health: 95%', font=('Helvetica', 14), background='#2d2d2d', foreground='white')
        analytics.pack()

if __name__ == '__main__':
    root = tk.Tk()
    app = EdgeSenseGUI(root)
    root.mainloop()