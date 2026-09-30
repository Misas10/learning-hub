import json,glob,collections
gs=[]
for f in sorted(glob.glob('g_*.json')):
    gs+=json.load(open(f))['games']
gs=[g for g in gs if g['time_class']=='rapid' and g.get('rules')=='chess']
gs.sort(key=lambda g:g['end_time'])
print(len(gs),'rapid games')
c=collections.Counter(); tc=collections.Counter()
for g in gs:
    me='white' if g['white']['username'].lower()=='misas10' else 'black'
    opp='black' if me=='white' else 'white'
    r=g[me]['result']; ro=g[opp]['result']
    c[(r if r!='win' else 'win:'+ro)]+=1; tc[g['time_control']]+=1
print(c); print(tc)
import datetime
for f in sorted(glob.glob('g_*.json')):
    print(f, sum(1 for g in json.load(open(f))['games'] if g['time_class']=='rapid'))
json.dump(gs,open('rapid.json','w'))
