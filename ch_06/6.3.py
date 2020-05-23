# ALDS1_5_C: Koch Curve
# https://onlinejudge.u-aizu.ac.jp/problems/ALDS1_5_C
import math

TH = math.radians(60)
COS = math.cos(TH)
SIN = math.sin(TH)


def koch_inside(n: int, P: list, px: float, py: float, qx: float, qy: float) -> list:

    if n == 0:
        return P
    else:
        sx, sy = (2*px+1*qx)/3, (2*py+1*qy)/3
        tx, ty = (1*px+2*qx)/3, (1*py+2*qy)/3
        ux, uy = (tx-sx)*COS-(ty-sy)*SIN+sx, (tx-sx)*SIN+(ty-sy)*COS+sy

        P = koch_inside(n=n-1, P=P, px=px, py=py, qx=sx, qy=sy)
        P.append([sx, sy])
        P = koch_inside(n=n-1, P=P, px=sx, py=sy, qx=ux, qy=uy)
        P.append([ux, uy])
        P = koch_inside(n=n-1, P=P, px=ux, py=uy, qx=tx, qy=ty)
        P.append([tx, ty])
        P = koch_inside(n=n-1, P=P, px=tx, py=ty, qx=qx, qy=qy)
        return P
    
    
def koch(n: int, P: list, px: float, py: float, qx: float, qy: float) -> list:
    P.append([px, py])
    P = koch_inside(n=n, P=P, px=px, py=py, qx=qx, qy=qy)
    P.append([qx, qy])
    return P


def main():
    P = []

    ax, ay = 0, 0
    bx, by = 100, 0

    n = int(input())

    koch(n=n, P=P, px=ax, py=ay, qx=bx, qy=by)

    for p in P:
        print('{:.8f} {:.8f}'.format(p[0], p[1]))


if __name__ == '__main__':
    main()
