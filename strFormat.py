#Digunakan untuk format String
nama = "Junanjing"
umur = 69
numLst = [1,2,3,4,5,6,7,8,9]
phiX = 3.696969
total = "Hai %s"
print("Hai namaku %s aku berumur %d" % (nama,umur))
print(total % nama)
print("Ini adalah list nomorku: %s" % numLst)
print("Ini adalah Phi dalam dunia Integer: %d" % phiX)
print("Ini adalah Phi dalam dunia Float: %f" % phiX)
print("Ini adalah Phi yang kecil: %.2f" % phiX)
print("Ini adalah Hex Integer besar: %X" %  umur)
print("Ini adalah Hex Integer kecil: %x" % umur)

#%s - String (or any object with a string representation, like numbers)
#%d - Integers
#%f - Floating point numbers
#%.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.
#%x/%X - Integers in hex representation (lowercase/uppercase)
