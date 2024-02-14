#1-Kullanıcının girdiği boy ve ağırlık değerlerine göre vücut kitle indeksini (VKİ = ağırlık/(boy*boy)) hesaplayınız.
#
print("Vücut kitle indeksi")
boy = float(input("Boy:"))
kilo = int(input("Kilo:"))
endeks = kilo /(boy*boy)
vucut=f"Vücut kitle indeksiniz: {endeks}"
print(vucut)


#2-Maaşı ve zam oranı girilen işçinin zamlı maaşını hesaplayarak ekranda gösteriniz.
print("Maaş ve zam oranını giriniz")
maas = int(input("Maaşı giriniz: "))
zamOrani=float(input("Zam oranını tam sayı olarak giriniz: "))
zamliMaas= float(maas+maas*(zamOrani/100))
print("Zamlı  maaşınız: ",zamliMaas," TL")

#3-Kullanıcının girdiği üç sayı arasında en büyük olanı bulan ve sonucu yazdıran bir program yazınız.
print("Üç adet tam sayı giriniz")
birinciTamsayi=int(input("birinci tam sayıyı giriniz: "))
ikinciTamsayi=int(input("ikinci tam sayıyı giriniz: "))
ucuncuTamsayi=int(input("üçüncü tam sayıyı giriniz: "))
enBuyukSayi=max(birinciTamsayi,ikinciTamsayi,ucuncuTamsayi)
print("En büyük tam sayı: ",enBuyukSayi)
  
#4-Dairenin alanını ve çevresini hesaplayan python kodunu yazınız.(Dairenin yarıçapını kullanıcıdan alınız)
print("dairenin yarı çapını giriniz")
yariCap=float(input("yarı çap değeri giriniz:"))
pi=3.14
daireAlani=pi*yariCap*yariCap
daireCevre=2*pi*yariCap
print("Dairenin Alanı =",daireAlani)
print("Dairenin Çevresi=",daireCevre)

#5-Kullanıcıdan alınan bir sayının palindrom olup olmadığını bulan bir program yazınız.
sayi=(input("sayıyı giriniz:"))

tersten = "" 
for rakam in sayi:
    tersten = rakam + tersten
    
print(tersten)
if tersten==sayi:
    print(sayi,"Sayısı Palindromdur")
else:
    print(sayi,"Sayısı Palindrom değildir")    

#github'a ekleme yapalım, linkleri paylaşalım lütfen 🙂

