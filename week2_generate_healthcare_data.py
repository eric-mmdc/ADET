import pandas as pd
import numpy as np
from datetime import datetime, timedelta

num_records = 100
data = []

sensor_types = {
    "Heart Rate": lambda: f"{np.random.randint(60, 100)} bpm",
    "Blood Pressure": lambda: f"{np.random.randint(100, 140)}/{np.random.randint(60, 90)} mmHg",
    "Oxygen Level": lambda: f"{np.random.randint(95, 100)}%",
    "Body Temperature": lambda: f"{round(np.random.uniform(36.0, 38.0), 1)}°C"
}

for _ in range(num_records):

    data_type = np.random.choice(list(sensor_types.keys()))

    record = {
        "timestamp": datetime.now() - timedelta(minutes=np.random.randint(0, 1440)),
        "device_id": f"PAT{np.random.randint(100, 999)}",
        "data_type": data_type,
        "data_value": sensor_types[data_type]()
    }

    data.append(record)

df = pd.DataFrame(data)

df.to_csv("formatted_healthcare_data.csv", index=False)
df.to_json("formatted_healthcare_data.json", orient="records")

print(df.head())
print("Healthcare IoT data generated successfully!")