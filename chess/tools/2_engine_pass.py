import json,io,re,chess,chess.pgn,chess.engine
gs=json.load(open('rapid.json'))
e=chess.engine.SimpleEngine.popen_uci("./stockfish/stockfish-linux-x86-64-universal")
e.configure({"Threads":4,"Hash":128})
V={1:1,2:3,3:3,4:5,5:9,6:0}
def mat(b,col):
    return sum(V[p.piece_type]*(1 if p.color==col else -1) for p in b.piece_map().values())
def ev(b,col):
    i=e.analyse(b,chess.engine.Limit(nodes=150000))
    return max(-1000,min(1000,i['score'].pov(col).score(mate_score=1000))), i.get('pv',[])
out=[]
for g in gs:
    game=chess.pgn.read_game(io.StringIO(g['pgn']))
    me=chess.WHITE if g['white']['username'].lower()=='misas10' else chess.BLACK
    side='white' if me else 'black'; opp='black' if me else 'white'
    b=game.board(); rows=[]
    s,pv=ev(b,me)
    for node in game.mainline():
        mv=node.move; mover=b.turn; san=b.san(mv); fen=b.fen(); best=b.san(pv[0]) if pv else None
        mb=mat(b,me)
        b.push(mv)
        if b.is_game_over():
            s2=1000 if b.is_checkmate() and mover==me else (-1000 if b.is_checkmate() else 0); pv2=[]
        else: s2,pv2=ev(b,me)
        # material after 3-ply pv
        bb=b.copy()
        for m in pv2[:3]: bb.push(m)
        rows.append(dict(n=(len(rows)//2)+1,mine=mover==me,san=san,before=s,after=s2,best=best,fen=fen,clk=node.clock(),mat=mb,mat3=mat(bb,me),reply=b.san(pv2[0]) if pv2 else None))
        s,pv=s2,pv2
    out.append(dict(url=g['url'],me=side,res=g[side]['result'],ores=g[opp]['result'],myr=g[side]['rating'],opr=g[opp]['rating'],end=g['end_time'],eco=g.get('eco','').split('/')[-1],rows=rows))
    print(len(out),g[side]['result'],len(rows),flush=True)
e.quit(); json.dump(out,open('an.json','w'))
