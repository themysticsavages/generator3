import requests
import flask
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
      ht = open(targets[i]['name']+'.html'.lower(),'w')
      fh.write('{}\n'.format(targets[i]['name']))

      ht.write("""
      <!doctype html>
      <html>
        <head>
          <script src="https://scratchblocks.github.io/js/scratchblocks-v3.5.2-min.js"></script>
        </head>
        <body>
          <p class="blocks">
      """)

      for k in targets[i]['blocks']:
        opcode = targets[i]['blocks'][k]['opcode']
        root = targets[i]['blocks'][k]
        fnd = targets[i]
        let = ''

        print(opcode)
        if opcode == 'event_whenflagclicked':
          let += 'when flag clicked:'
        if opcode == 'event_whenbroadcastreceived':
          br = root['fields']['BROADCAST_OPTION'][0]
          let += 'when i receive [{}]'.format(br)
        if opcode == 'looks_seteffectto':
          ef = root['fields']['EFFECT'][0]
          num = root['inputs']['VALUE'][1][1]

          let += 'set [{}] effect to ({})'.format(ef.lower(),num)
        if opcode == 'control_create_clone_of':
          mn = root['inputs']['CLONE_OPTION'][1]
          opt = targets[i]['blocks'][mn]['fields']['CLONE_OPTION'][0].replace('_','')
          
          let += 'create clone of [{}]'.format(opt)
        if opcode == 'motion_gotoxy':
          try:
            x = root['inputs']['X'][2][0]
            y = root['inputs']['Y'][2][1]
          except IndexError:
            x = root['inputs']['X'][1][0]
            y = root['inputs']['Y'][1][1]
          
          let += 'go to x ({}) y ({})'.format(x,y)
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
          
          let += 'glide ({}) secs to x ({}) y ({})'.format(secs,x,y)
        if opcode == 'looks_switchcostumeto':
          cos = root['inputs']['COSTUME'][1]

          try:
            let += 'switch costume to [{}]'.format(targets[i]['blocks'][cos]['fields']['COSTUME'][0])
          except KeyError:
            let += 'switch costume to (not found)'
        if opcode == 'looks_changeeffectby':
          cha = root['inputs']['CHANGE'][1][1]
          ef = root['fields']['EFFECT'][0]

          let += 'change [{}] effect by ({})'.format(ef.lower(), cha)
        if opcode == 'looks_show':
          let += 'show '
        if opcode == 'looks_hide':
          let += 'hide '
        if opcode == 'data_setvariableto':
          var = root['fields']['VARIABLE'][0]
          val = root['inputs']['VALUE'][1][1]

          let += 'set [{}] to [{}]'.format(var,val)
        if opcode == 'sound_playuntildone':
          d = root['inputs']['SOUND_MENU'][1]
          val = targets[i]['blocks'][d]['fields']['SOUND_MENU'][0]

          let += 'play sound [{}] until done'.format(val)

        fh.write(let+'\n')
        ht.write(let+'\n')

      ht.write("""
      </p>
      <script type="text/javascript">
      scratchblocks.renderMatching("p.blocks", {
          style: 'scratch3'
      })
      </script>
      """)

  def serveHTML():
    app = flask.Flask('__main__')

    @app.get('/<f>')
    def getf(f):
      return open(f+'.html').read()

    app.run(host='0.0.0.0')
