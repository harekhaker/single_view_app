import requests

requests.post('http://loacalhost:8990/upload_file/', files={'file':('meke.csv', open('works_metadata.csv', 'rb'))})