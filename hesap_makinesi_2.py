x=float(input("İlk sayıyı giriniz.:"))
y=float(input("İkinci sayıyı giriniz.:"))
islem=input("Yapmak istediğiniz işlemi seçiniz.:(+,-,*,/)")
print(f"Girdiğiniz sayılar ve işlem: {x},{y},{islem}")

if(islem=="+"):
    print("Sonuç: ",x+y)
elif(islem=="-"):
    print("Sonuç: ", x-y)
elif(islem=="/"):
    print("Sonuç: ",x/y)
elif(islem=="*"):
    print("Sonuç: ",x*y)
else:
    print("Geçersiz bir işlem yaptınız!")
    
