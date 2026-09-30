import json,statistics as st,collections
A=json.load(open('an.json'))
W=[g for g in A if g['res']=='win']; L=[g for g in A if g['res'] in('resigned','timeout','checkmated')]; D=[g for g in A if g not in W and g not in L]
print(len(W),len(L),len(D))
def blunders(g,who=True,th=300):
    return [r for r in g['rows'] if r['mine']==who and r['before']-r['after']>=th] if who else [r for r in g['rows'] if not r['mine'] and r['after']-r['before']>=th]
print("\n== LOSSES ==")
cat=collections.Counter()
for g in L+D:
    rows=g['rows']; mx=max(r['after'] for r in rows); 
    mymoves=[r for r in rows if r['mine']]
    # first move after which eval <= -300 and never recovers above -150
    dec=None
    for i,r in enumerate(rows):
        if r['mine'] and r['after']<=-250 and r['before']>-250 and all(x['after']<0 for x in rows[i:]):
            dec=r;break
    bl=blunders(g)
    e12=rows[23]['after'] if len(rows)>23 else None
    lastclk=[r['clk'] for r in mymoves if r['clk'] is not None][-1:]
    print(g['url'].split('/')[-1],g['me'][0],g['res'],f"{g['myr']}v{g['opr']}",g['eco'][:28],'len',len(rows)//2,'peak',mx,'ev@12',e12,'nbl',len(bl),'clk',lastclk)
    if dec: print('   decisive:',dec['n'],dec['san'],dec['before'],'->',dec['after'],'best',dec['best'],'reply',dec['reply'],'mat',dec['mat'],'->',dec['mat3'])
    for r in bl[:6]: print('      bl',r['n'],r['san'],r['before'],'->',r['after'],'best',r['best'],'reply',r['reply'],'mat',r['mat'],'->',r['mat3'])
print("\n== WINS ==")
for g in W:
    rows=g['rows']; mn=min(r['after'] for r in rows); bl=blunders(g)
    # moves from first reaching +500 to end
    first=next((i for i,r in enumerate(rows) if r['after']>=500),None)
    print(g['url'].split('/')[-1],g['ores'],'len',len(rows)//2,'worst',mn,'nbl',len(bl),'first+5 at',rows[first]['n'] if first is not None else None)
# aggregate
allmy=[r for g in A for r in g['rows'] if r['mine']]
bl=[r for r in allmy if r['before']-r['after']>=300 and r['before']>-400]
print("\nmy moves",len(allmy),"blunders(>=300, still in game)",len(bl), "per game",len(bl)/len(A))
print("material-losing blunders (mat3 drop>=2):",sum(1 for r in bl if r['mat3']-r['mat']<=-2))
print("blunders made when ahead >=+300:",sum(1 for r in bl if r['before']>=300))
print("by phase:",collections.Counter('open' if r['n']<=12 else 'mid' if r['n']<=30 else 'end' for r in bl))
opp=[r for g in A for r in g['rows'] if not r['mine'] and r['after']-r['before']>=300 and r['before']<400]
print("opp blunders",len(opp))
# missed: opp blundered (after>=+300 for me) then my next move drops >=300
miss=0;tot=0
for g in A:
    rows=g['rows']
    for i,r in enumerate(rows[:-1]):
        if not r['mine'] and r['after']-r['before']>=300:
            tot+=1
            n=rows[i+1]
            if n['before']-n['after']>=250: miss+=1
print("opp blunders punished?",tot,"missed",miss)
print("ev@move12 all games:",[g['rows'][23]['after'] for g in A if len(g['rows'])>23])
print("games where I reached >=+300:",sum(1 for g in A if max(r['after'] for r in g['rows'])>=300),"won",sum(1 for g in W if max(r['after'] for r in g['rows'])>=300))
print("games where I reached >=+500:",sum(1 for g in A if max(r['after'] for r in g['rows'])>=500),"won",sum(1 for g in W if max(r['after'] for r in g['rows'])>=500))
print("games where opp reached <=-500:",sum(1 for g in A if min(r['after'] for r in g['rows'])<=-500),"I won",sum(1 for g in W if min(r['after'] for r in g['rows'])<=-500))
