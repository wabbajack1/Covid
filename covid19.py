#!/usr/bin/env python3

import numpy
import math
import matplotlib.pyplot as plt
import requests
import time
import pandas
resultPlot = [51.0,9.0,0,0,0,0,0,1,4,4,4,5,8,10,12,12,12,12,13,13,14,14,16,16,16,16,16,16,16,16,16,16,16,16,16,16,17,27,46,48,79,130,159,196,262,482,670,799,1040,1176,1457,1908,2078,3675,4585,5795,7272,9257,12327,15320,19848,22213,24873,29056,32986,37323,43938,50871]
cnt = 0

while True:
  covid_req = requests.get("https://opendata.arcgis.com/datasets/dd4580c810204019a7b8eb3e0b329dd6_0.geojson")
  req_json = covid_req.json()
  

  #lokale varibale 
  result = 0

  for i in req_json["features"]:
    ii = i["properties"]
    print(type(ii))
    for p in ii.keys():
      print(p, "-->", ii[p])
      if p == "IdBundesland":
        print("----")  
      if p == "AnzahlFall":
        result += ii[p]
        
  if result not in resultPlot and result < result + 10 and  result > result - 10:
    resultPlot.append(result)
 
  print(result)
  print(resultPlot)
  
  wb = open("currentData.txt", "w")
  wb.write(str(resultPlot))
  print("Wrote to file....")
  wb.close()
  

  """  
  plt.plot(resultPlot)
  plt.show(block = False)
  plt.pause(2)
  plt.close()
  """
  
  cnt+=1
  print("Es ist die " + str(cnt) + " Iteration")
  
  data = req_json["features"]
  
  t = pandas.DataFrame(data)
  print(t)
  print(type(t))
  time.sleep(60)


