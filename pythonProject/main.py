print(" Notlarınızı 0-100 arasında uygun şekilde doldurun.")
kisasinav1=input("kisasinav1:")
x=float(kisasinav1)

if x<0 or x>100:
    print("Lütfen not aralığında sayısal bir deger giriniz.")
elif type(x) is not float:
    print("lütfen sayısal bir değer girin.")
kisasinav2=input("kisasinav2:")
y=float(kisasinav2)

if y<0 or y>100:
    print("Lütfen not aralığında sayısal bir deger giriniz.")
elif type(y) is not float:
    print("lütfen sayısal bir değer girin.")
arasinav=input("arasinav:")
z=float(arasinav)

if z<0 or z>100:
    print("Lütfen not aralığında sayısal bir deger giriniz.")
elif type(z) is not float:
    print("lütfen sayısal bir değer girin.")

odev1=input("odev1:")
t=float(odev1)

if t<0 or t>100:
    print("Lütfen not aralığında sayısal bir deger giriniz.")
elif type(t) is not float:
    print("lütfen sayısal bir değer girin.")

odev2=input("odev2:")
e=float(odev2)

if e<0 or e>100:
    print("Lütfen not aralığında sayısal bir deger giriniz.")
elif type(e) is not float:
    print("lütfen sayısal bir değer girin.")

final=input("final:")
f=float(final)

if f<0 or f>100:
    print("Lütfen not aralığında sayısal bir deger giriniz.")
elif type(f) is not float:
    print("lütfen sayısal bir değer girin.")
ort=(x*0.1+y*0.1+z*0.2+t*0.1+e*0.1+f*0.4)
if ort>=90:
  print("notunuz:",ort,"harf notunuz:AA-geçtiniz.")
elif ort>=80:
    print("notunuz:", ort, "harf notunuz:BA -geçtiniz")
elif ort>=70:
    print("notunuz:", ort, "harf notunuz:BB -geçtiniz")
elif ort>=60:
    print("notunuz:", ort, "harf notunuz:CB -geçtiniz")
elif ort>=50:
    print("notunuz:", ort, "harf notunuz:CC -geçtiniz")
elif ort>=40:
    print("notunuz:", ort, "harf notunuz:DC -geçtiniz")
elif ort>=35:
    print("notunuz:", ort, "harf notunuz:DD -geçtiniz")
elif ort<35:
    print("notunuz:", ort, "harf notunuz:FF -KALDINIZ")
