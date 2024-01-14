import pandas as pd
def preprocess_data(data):

  # Changing all uppercase letters to lowercase
  data['job_title'] = data['job_title'].str.lower()
  data['location'] = data['location'].str.lower()
  data['connection'] = data['connection'].str.lower()

  # Getting rid of punctuation
  data = data.replace('[,\.\|\()\!]','', regex=True)

  # Concatenating data in new df
  data_concat = pd.DataFrame()
  data_concat["data_concat"] = data[["job_title", "location", "connection"]].apply(" ".join, axis=1)
  return data_concat
