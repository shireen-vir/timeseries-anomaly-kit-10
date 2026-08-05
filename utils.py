class AnomalyDetector:
    """This class provides functionality for detecting anomalies in time series data."""

    def __init__(self, data):
        self.data = data

    def detect_anomalies(self):
        # For this example, we'll use a simple threshold-based approach.
        mean = sum(self.data) / len(self.data)
        threshold = mean * 2
        anomalies = [x for x in self.data if x > threshold]
        return anomalies

import pandas as pd
import numpy as np

def main():
    data = pd.Series(np.random.randn(100))  # Generate some random data
    detector = AnomalyDetector(data)
    anomalies = detector.detect_anomalies()
    print("Anomalies detected:", anomalies)

if __name__ == "__main__":
    main()