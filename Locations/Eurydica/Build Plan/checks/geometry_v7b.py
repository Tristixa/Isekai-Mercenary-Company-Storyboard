"""Geometry shared by the authoring and renderer; validator measures independently."""
import sys, math
sys.dont_write_bytecode=True
import inherited_checks as g

def bounds(p):
 return min(x for x,z in p),min(z for x,z in p),max(x for x,z in p),max(z for x,z in p)

def area(p):
 return abs(sum(a[0]*b[1]-a[1]*b[0] for a,b in g.edges(p)))/2

def overlap(a,b):
 x,z,X,Z=bounds(a);u,v,U,V=bounds(b)
 if min(X,U)-max(x,u)<1e-6 or min(Z,V)-max(z,v)<1e-6:return False
 def cross(a,b,c):return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
 for p,q in g.edges(a):
  for r,s in g.edges(b):
   if cross(p,q,r)*cross(p,q,s)<-1e-10 and cross(r,s,p)*cross(r,s,q)<-1e-10:return True
 def strict(pt,poly):return g.inside(pt,poly) and min(g.distance(pt,c,d) for c,d in g.edges(poly))>1e-6
 for p in a:
  if strict(p,b):return True
 for p in b:
  if strict(p,a):return True
 # Mid-edge samples handle coincident / aligned rectangles and shared boundary spans.
 for poly,other in ((a,b),(b,a)):
  ctr=[sum(p[i] for p in poly)/len(poly) for i in (0,1)]
  if strict(ctr,poly) and strict(ctr,other):return True
  for p,q in g.edges(poly):
   pt=[(p[i]+q[i])/2 for i in (0,1)]
   if strict(pt,other):return True
 return False

def transform(pt,pivot,yaw,shift=(0,0)):
 a=math.radians(yaw);c,s=math.cos(a),math.sin(a);x,z=pt[0]-pivot[0],pt[1]-pivot[1]
 return [pivot[0]+c*x-s*z+shift[0],pivot[1]+s*x+c*z+shift[1]]

def nearest(pt,a,b):
 dx,dz=b[0]-a[0],b[1]-a[1];t=max(0,min(1,((pt[0]-a[0])*dx+(pt[1]-a[1])*dz)/(dx*dx+dz*dz)))
 return [a[0]+t*dx,a[1]+t*dz],t

def hull(points):
 pts=sorted(set(tuple(p) for p in points))
 def cross(o,a,b):return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
 lower=[];upper=[]
 for p in pts:
  while len(lower)>1 and cross(lower[-2],lower[-1],p)<=0:lower.pop()
  lower.append(p)
 for p in reversed(pts):
  while len(upper)>1 and cross(upper[-2],upper[-1],p)<=0:upper.pop()
  upper.append(p)
 return [list(p) for p in lower[:-1]+upper[:-1]]
