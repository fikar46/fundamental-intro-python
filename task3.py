import math;
hari = 485
tahun= 360
bulan = 30
xtahun= hari / tahun
x1= math.floor(xtahun)
x = hari % tahun
x2= x / bulan
x3 = math.floor(x2)
y= x % bulan
print(str(x1)+" tahun "+str(x3)+ " bulan "+ str(y) +" hari.")