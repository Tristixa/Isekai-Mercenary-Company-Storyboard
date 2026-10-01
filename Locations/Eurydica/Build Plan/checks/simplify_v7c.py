"""Remove unused terminal pavement by graph pruning, retaining every door."""
import math
import inherited_checks as g
def prune(p):
 graph,_=g.graph(p)
 fixed={'main_road','gate_arch','old_bridge','civic_approach','civic_old_ramp','civic_res_ramp','watch_stairs','view_deck','dock_ramp','dock_deck','north_riverside','allotment_lane'}
 protected={g.key(b['door_position']) for b in p['buildings']}
 protected.update(g.key(v) for r in p['routes'] if r['id'] in fixed for v in r['centreline'])
 adj={a:set(b for b,_,_ in edges) for a,edges in graph.items()}
 todo=[a for a in adj if len(adj[a])==1 and a not in protected];dead=set()
 while todo:
  a=todo.pop()
  if a in dead or len(adj[a])!=1 or a in protected:continue
  b=next(iter(adj[a]));adj[a].clear();adj[b].remove(a);dead.add(a)
  if len(adj[b])==1 and b not in protected:todo.append(b)
 routes=[];removed=[]
 for r in p['routes']:
  if r['id'] in fixed or r.get('owner'):routes.append(r);continue
  pts=[];hs=[]
  for i,(a,b) in enumerate(zip(r['centreline'],r['centreline'][1:])):
   nodes=sorted([pt for pt in graph if g.distance(pt,a,b)<1e-6 and pt not in dead],key=lambda pt:math.dist(a,pt))
   for pt in nodes:
    if pts and math.dist(pt,pts[-1])<1e-7:continue
    pts.append(list(pt));hs.append(g.segheight(r,i,pt))
  if len(pts)<2:removed.append(r['id']);continue
  r['centreline']=pts;r['heights_m']=hs;r['grade']=[(v-u)/math.dist(a,b) for u,v,a,b in zip(hs,hs[1:],pts,pts[1:])];routes.append(r)
 p['routes']=routes;p['v7c_pruned_route_ids']=removed
