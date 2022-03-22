class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
    while(sx<tx and sy<ty):
        if tx<ty:
            ty=ty%tx
        else:
            tx=tx%ty
        if ty-sy<0 or tx-sx<0:
            return False
        return (sx==tx and (ty-sy)%sx==0) or (sy==ty and (tx-sx)%sy==0)
