import index
import time
import os

try: 
  os.remove('results.txt') 
except FileNotFoundError: pass

for item in os.listdir('./'):
    if item.endswith(".html"):
        os.remove(os.path.join('./', item))

inp = input('[LOG] Enter a project ID > ')

print('[LOG] Fetching project',str(inp),'...')

ds = int(time.time()*1000)
index.util(inp).getScripts()

print('[LOG] Finished in {}ms'.format(int(time.time()*1000-ds)))
print('[LOG] Starting temporary webserver ...')
index.util.serveHTML()