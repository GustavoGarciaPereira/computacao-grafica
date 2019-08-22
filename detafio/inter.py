

r1p1x = int(input("r1 P1x: "))
r1p1y = int(input("r1 P2y: "))

r1p2x = int(input("r1 P2x: "))
r1p2y = int(input("r1 P2y: "))


r2p1x = int(input("r2 P1x: "))
r2p1y = int(input("r2 P2y: "))

r2p2x = int(input("r2 P2x: "))
r2p2y = int(input("r2 P2y: "))


r1ponx = r1p2x - r1p1x
r1pony = r1p2y - r1p1y
print("<xr1>",r1ponx)
print("<xr1>",r1pony)


r2ponx = r2p2x - r2p1x
r2pony = r2p2y - r2p1y
print("<xr1>",r2ponx)
print("<xr1>",r2pony)

if r1ponx < r2ponx and r1pony < r2pony:
    print("se c")