from select import select

import pandas as pd
import requests
from io import StringIO

url = "https://interview_task.zip"
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:66.0) Gecko/20100101 Firefox/66.0"}
req = requests.get(url, headers=headers)
data = StringIO(req.text)
pd.read_csv(data.csv)
pd.read_csv('report.csv')
pd.read_csv('data.csv', select(image_name,objects_detected,timestamp))


pd.read_csv('report.csv', index_col='threat,occurence')