kucuk_harfler = "".join(chr(s) for s in range(ord('a'), ord('z') + 1))
buyuk_harfler = "".join(chr(s) for s in range(ord('A'), ord('Z') + 1))
sayilar = "0123456789"
ifadeler = "+-*/?}])([{&%$#£" 

p_length = int(input("Şifreniz kaç haneli olsun?"))
parola = ""






for i in range(p_length): 
    if i % 4 == 0:
        parola += random.choice(kucuk_harfler)
    elif i % 4 == 1:
        parola += random.choice(buyuk_harfler)
    elif i % 4 == 2:
        parola += random.choice(sayilar)
    elif i % 4 == 3:
        parola += random.choice(ifadeler)

print(f"Parolanız: {parola}")
