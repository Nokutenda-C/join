atimport math
YN =float(input("enter YN Y coordinate:"))
XN =float(input("enter XN X coordinate:"))
YC =float(input("enter YC Y coordinates:"))
XC =float(input("enter XC X coordinate:"))
DY =YC-YN
DX = XC-XN
R = math.sqrt(DY ** 2 + DX ** 2)
F = DY/DX
T = math.degrees(math.atan(F))
Q1 = T
Q2 = 180 - T
Q3 = 180 + T
Q4 = 180 - T
if DX > 0 and DY > 0:
    print(f"join NC : {R} m , {Q1} degrees")
elif DX > 0 and DY < 0 :
    print(f"join NC : {R} m , {Q2} degrees")
elif DX < 0 and DY < 0 :
     print(f'join NC : {R} m , {Q3} degrees')
else:
     print(f"join NC : {R} m ,{Q4} degrees")







