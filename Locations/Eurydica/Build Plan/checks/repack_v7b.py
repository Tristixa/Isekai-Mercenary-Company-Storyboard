"""Rerun only the canonical props/landscape stage on already authored access geometry."""
import sys,json,copy,math,random,hashlib
from pathlib import Path
sys.dont_write_bytecode=True
import inherited_checks as g
from geometry_v7b import *
from check_plan import gap
R=Path(__file__).resolve().parent
V=json.loads((R/'eurydica-plan.json').read_bytes());P=json.loads((R/'eurydica-plan-v7b.json').read_bytes())
B={b['id']:b for b in P['buildings']};cs={c['id']:c for c in P['clusters']}
S=[(b['id'],[g.rotate(v,b) for v in g.boxpoly(f)]) for b in P['buildings'] for f in b.get('collision_rectangles',[b['footprint']])]
blocked=[s for _,s in S]+[P['river']['polygon'],P['waterworks']['feeder_polygon'],P['hq_reservation']['polygon']]
red=next(t for t in P['green']['trees'] if t['id']=='tree_08')
source=(R/'build_v7b.py').read_text(encoding='utf-8')
exec(compile(source[source.index('# Props are packed'):],str(R/'build_v7b.py'),'exec'))
