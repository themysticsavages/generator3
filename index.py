import requests
import json
import time

class util():
  def __init__(self,id):
    self.id = str(id)
  def getScripts(self):
    targets = json.loads(requests.get('https://projects.scratch.mit.edu/'+self.id).text)['targets']

    JSON = []
    fh = open('results.txt','a')

    for i in range(len(targets)):
      fh.write('\n'+targets[i]['name']+'\n----------\n')

      for k in targets[i]['blocks']:
        opcode = targets[i]['blocks'][k]['opcode']
        root = targets[i]['blocks'][k]
        fnd = targets[i]
        let = ''

        if opcode == 'event_whenflagclicked':
          let += 'when flag clicked:'
        if opcode == 'looks_seteffectto':
          effect = root['fields']['EFFECT'][0]
          num = root['inputs']['VALUE'][1][1]

          let += 'set ({}) effect to ({})'.format(effect,num)

        if opcode == 'event_whenbroadcastreceived':
          msg = root['fields']['BROADCAST_OPTION'][0]
          let += 'when i receive ({}):'.format(msg)

        if opcode == 'motion_gotoxy':
          try:
            x = root['inputs']['X'][2][1]
            y = root['inputs']['Y'][2][1]
          except IndexError:
            x = root['inputs']['X'][1][1]
            y = root['inputs']['Y'][1][1]
          
          let += 'go to x: ({}) y: ({})'.format(x,y)

        if opcode == 'motion_changeyby':
          y = root['inputs']['DY'][2][1]

          let += 'change y by ({})'.format(y)
        if opcode == 'motion_glidesecstoxy':
          secs = root['inputs']['SECS'][1][1]
          
          try:
            x = root['inputs']['X'][2][1]
            y = root['inputs']['Y'][2][1]
          except IndexError:
            x = root['inputs']['X'][1][1]
            y = root['inputs']['Y'][1][1]

          print(x,y)
          
          let += 'glide ({}) secs to x ({}) y ({})'.format(secs,x,y)

        if opcode == 'looks_switchcostumeto':
          cos = root['inputs']['COSTUME'][1]

          try:
            let += 'switch costume to ({})'.format(targets[i]['blocks'][cos]['fields']['COSTUME'][0])
          except KeyError:
            let += 'switch costume to (not found)'

        if opcode == 'looks_switchbackdropto':
          bg = root['inputs']['BACKDROP'][1]
          nm = fnd['blocks'][bg]['fields']['BACKDROP'][0]

          let += 'switch backdrop to ({})'.format(nm)

        if opcode == 'looks_switchbackdroptoandwait':
          bg = root['inputs']['BACKDROP'][1]
          nm = fnd['blocks'][bg]['fields']['BACKDROP'][0]

          let += 'switch backdrop to ({}) and wait'.format(nm)

        if opcode == 'looks_changeeffectby':
          cha = root['inputs']['CHANGE'][1][1]
          ef = root['fields']['EFFECT'][0]

          let += 'change ({}) effect by ({})'.format(ef, cha)

        if opcode == 'looks_show':
          let += 'show '

        if opcode == 'looks_hide':
          let += 'hide '

        fh.write(let+'\n')