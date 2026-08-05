class TimeSeriesAnomalyKit10:
    """
    A data science tool for detecting anomalies in time series data.

    Attributes:
        data (list): The input time series data.
        threshold (float): The threshold value for anomaly detection.

    Methods:
        detect_anomalies: Detects anomalies in the input time series data.
    """

    def __init__(self, data, threshold):
        self.data = data
        self.threshold = threshold

    def detect_anomalies(self):
        """
        Detects anomalies in the input time series data.

        Returns:
            list: A list of indices where anomalies were detected.
        """
        anomalies = []
        for i in range(len(self.data)):
            if self.data[i] > self.threshold:
                anomalies.append(i)
        return anomalies


import pandas as pd
import numpy as np


def main():
    data = [1, 2, 3, 4, 5, 10, 6, 7, 8, 9]
    threshold = 5
    kit = TimeSeriesAnomalyKit10(data, threshold)
    anomalies = kit.detect_anomalies()
    print("Anomalies detected at indices:", anomalies)


if __name__ == "__main__":
    main()