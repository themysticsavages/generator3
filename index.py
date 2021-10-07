import requests
import json

class util():
  def __init__(self,id):
    self.id = str(id)
  def getScripts(self):
    targets = json.loads(requests.get('https://projects.scratch.mit.edu/'+self.id).text)['targets']
    JSON = []
    fh = open('results.txt','a')

    fh.write('Generated code\n*URLs next to sounds is the link to the file in the assets API*\n======================\n\n')
    for i in range(len(targets)):
      let = ''

      for k in targets[i]['blocks']:
        opcode = targets[i]['blocks'][k]['opcode']
        root = targets[i]['blocks'][k]
        fnd = targets[i]

        if opcode != 'sound_sounds_menu': let += opcode + ' '

        if len(root['inputs']) != 0:
          runonce = False
          for k0 in root['inputs']:
            if runonce == True: break

            if opcode == 'motion_gotoxy':
              let += '({}, {}) '.format(root['inputs'][k0][1][0], root['inputs'][k0][1][1])

            if opcode == 'sound_playuntildone':
              block = fnd['blocks'][root['inputs'][k0][1]]

              try:
                src = fnd['sounds'][1]['md5ext']
              except IndexError:
                src = 'failed to load'

              let += str('"'+block['fields']['SOUND_MENU'][0]+'"').replace(' ', '') + ' ('+src+')'

            if opcode == 'motion_glidesecstoxy':
              let += '({}, ({}, {})) '.format(root['inputs'][k0][0], root['inputs'][k0][1][0], root['inputs'][k0][1][1])
              
            if opcode == 'looks_seteffectto':
              let += '({},{}) '.format(root['fields']['EFFECT'][0],root['inputs'][k0][1][1])

            if opcode == 'sensing_keypressed':
              key = fnd['blocks'][root['inputs'][k0][1]]['fields']['KEY_OPTION'][0]

              let += '('+key+') '
            
            runonce = True

        fh.write(let+'\n')
