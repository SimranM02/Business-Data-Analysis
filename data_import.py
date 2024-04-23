from google.colab import files
uploaded = files.upload()

import pandas as pd
import io
df = pd.read_csv(io.BytesIO(uploaded['blood test data.csv']))
print(df)

import random
for _ in range(54):
    number = random.uniform(150, 2000)
    #if random.random() < 0.5:
        #number = round(number, 1)
    print(f"{number:.2f}")
