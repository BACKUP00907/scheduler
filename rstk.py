print("hello world")
import webbrowser
import time

url = ["https://strmltpym1.streamlit.app/"]
k = 0

while k < len(url) - 1: 
  webbrowser.open(url[k])
  time.sleep(180)
  k+=1
print("done resetting network")
