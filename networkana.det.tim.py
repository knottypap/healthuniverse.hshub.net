import time
import numpy as np
from sklearn.ensemble import IsolationForest

class NetworkAI:
    def __init__(self):
        self.model = IsolationForest(
            n_estimators=200,
            contamination=0.02,
            random_state=42
        )
        self.baseline = []

    def learn_baseline(self, packet_features):
        self.baseline.append(packet_features)
        if len(self.baseline) > 500:
            self.model.fit(self.baseline)

    def detect(self, packet_features):
        score = self.model.predict([packet_features])[0]
        return score == -1  # anomaly
