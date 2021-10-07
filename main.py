import index
import time
import os
try: 
  os.remove('results.txt') 
except FileNotFoundError: pass

inp = input('[LOG] Enter a project ID > ')

print('[LOG] Fetching project',str(inp),'...')

ds = int(time.time()*1000)
index.util(inp).getScripts()

print('[LOG] Finished in {}ms'.format(int(time.time()*1000-ds)))
