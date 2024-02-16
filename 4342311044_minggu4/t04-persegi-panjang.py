print("""
Pilih program perhitungan luas/keliling berikut:
- Ketikkan PSG / Persegi, untuk luas/keliling persegi
- Ketikkan LKR / Lingkaran, untuk luas/keliling lingkaran
- Ketikkan PPJ / Persegi-panjang, untuk luas/keliling persegi panjang
""")

program = input("Tentukan program: \n")

match program:
    case "PSG" | "Persegi" | "persegi" | "PERSEGI":
        hitung = input("Pilih jenis perhitungan LUAS/L dan KELILING/K: \n")
        s = float(input("Inputkan sisi: \n"))

        match hitung:
            case "L" | "LUAS":
                luas = s**2
                print("Luas persegi adalah ", luas)

            case "K" | "KELILING":
                keliling = 4**2
                print("Keliling adalah ", keliling)

            case _:
                print("Jenis perhitungan tidak dikenali")

    case "LKR" | "Lingkaran" | "LINGKARAN" | "lingkaran":
        hitung = input("Pilih jenis perhitungan LUAS/L dan KELILING/K: \n")
        r = float(input("Inputkan jari-jari: \n"))

        match hitung:
            case "L" | "LUAS":
                luas = 3.14*r*r
                print("Luas lingkaran adalah ", luas)

            case "K" | "KELILING":
                keliling = 2*3.14*r
                print("Keliling adalah ", keliling)

            case _:
                print("Jenis perhitungan tidak dikenali")

    case "PPJ" | "Persegi-panjang" | "Persegi Panjang" | "persegi-panjang" | "persegi panjang":
        hitung = input("Pilih jenis perhitungan LUAS/L dan KELILING/K: \n")
        panjang = float(input("Inputkan Panjang: \n"))
        lebar = float(input("Inputkan Lebar: \n"))

        match hitung:
            case "L" | "LUAS":
                luas = panjang * lebar
                print("Luas lingkaran adalah ", luas)
            
            case "K" | "KELILING":
                keliling = 2 * panjang + 2 * lebar
                print("Keliling adalah ", keliling)

            case _:
                print("Jenis perhitungan tidak dikenali")
                
    case _:
        print("Program tidak dikenali")