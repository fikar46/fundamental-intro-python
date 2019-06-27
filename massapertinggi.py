import math;
x=input("Masukan Massa(kg) : ");
y=input("Masukan Tinggi(cm) : ");
tinggi=(float(y)/100);
imt = float(x)/float(tinggi**2);
print(imt)
print("Massa " + str(x)+" kg & tinggi "+str(tinggi)+" m");

if(imt<18.5):
    print("Berat badan kurang ideal");
elif(imt<=24.9) :
    print("berat badan ideal");
elif(imt<=29.9) :
    print("berat badan berlebih");
elif(imt<=39.9) :
    print("berat badan sangat berlebih");
else :
    print("Kamu obesitas");
