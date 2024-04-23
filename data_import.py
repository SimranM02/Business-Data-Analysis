from google.colab import files
uploaded = files.upload()

#run this in a separate cell
import pandas as pd
import io
df = pd.read_csv(io.BytesIO(uploaded['blood test data.csv']))
print(df)

#run this in a separate cell
import random
for _ in range(54):
    number = random.uniform(150, 2000)
    #if random.random() < 0.5:
        #number = round(number, 1)
    print(f"{number:.2f}")

#run this in a separate cell
import pandas as pd
import io
df = pd.read_csv(io.BytesIO(uploaded['range test.csv']))
print(df)
