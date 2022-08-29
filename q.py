import shutil
import time
import requests

i = 0
while (i < 5):
  time.sleep(1)
  url = 'https://thispersondoesnotexist.com/image'
  response = requests.get(url, stream=True)
  with open('img'+str(i)+'.jpg', 'wb') as out_file:
      shutil.copyfileobj(response.raw, out_file)
  del response
  i = i + 1