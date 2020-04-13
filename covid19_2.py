#!/usr/bin/env python3

import requests
import time

cnt = 0
current_data = []
while True:
  url = "https://covid-19-data.p.rapidapi.com/country"

  querystring = {"format":"undefined",
                "name":"turkey"}

  headers = {
      'x-rapidapi-host': "covid-19-data.p.rapidapi.com",
      'x-rapidapi-key': "e720e708fbmsh4d5fe7b2bc05716p1fd22bjsn01963d5b35a3"
      }

  response = requests.request("GET", url, headers=headers, params=querystring)

  req = response.json()
  print(req)
  data = req[0]["confirmed"]
  d_list = current_data.append(data)
  print(d_list)
  wr = open("turkeyData.txt", "w")
  wr.write(str(d_list))

  cnt += 1
  print("There are", cnt, "Iterations")
  time.sleep(3600)
