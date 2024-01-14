import pandas as pd
from google.colab import files

def load_data(file_path):
  uploaded = files.upload()
  data = pd.read_csv(file_path)
  return data
