# string concatenation
"""
name = "Luthfi"
print("selamat datang " + name)
print("selamat datang {}".format(name))
print(f"selamat datang {name}")
"""
name = input("Masukan nama panggilan anda : ")
diff = input("Tingkat kseulitan game : ")
madlib = f"selamat datang di game {name}, anda akan bermain di tingkat kesulitan {diff}"
print(madlib)