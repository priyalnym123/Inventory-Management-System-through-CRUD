import pandas as pd
import base64
import requests

def get_as_base64(url):
	return base64.b64encode(requests.get(url).content)

df = pd.read_csv("data.csv")
for i in range(len(df)):
	img_link = df.loc[i, "imagelink"]
	b64 =  get_as_base64(img_link)
	df.loc[i, "imagelink"] = b64

df.to_csv('output.csv')
