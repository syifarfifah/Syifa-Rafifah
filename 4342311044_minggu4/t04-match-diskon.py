hargaBarang = float(input("Input harga: \n"))
jumlahBarang = int(input("Input jumlah barang: \n"))
isMember = input("Ada membernya kak??? \n")

match isMember:
    case "yes" | "YES" | "ya" | "YA" | "y":
        typeMember = input("Input jenis member??? (silver/gold/platinum) \n")
        
        match typeMember:
            case "Silver" | "SILVER" | "silver" | "sv" | "SV":
                diskon = (jumlahBarang*hargaBarang)*(100-25)/100
                print("Total harga setelah diskon adalah ", diskon)

            case "Gold" | "GOLD" | "gold" | "gd" | "GD":
                diskon = (jumlahBarang*hargaBarang)*(100-50)/100                  
                print("Total harga setelah diskon adalah ", diskon)

            case "Platinum" | "PLATINUM" | "platinum" | "pt" | "PT":
                diskon = (jumlahBarang*hargaBarang)*(100-75)/100                  
                print("Total harga setelah diskon adalah ", diskon)

            case _:
                print("Tipe Member tidak dikenali")
    
    case "no" | "NO" | "tidak" | "tdk" | "TIDAK" | "TDK":
        total = hargaBarang * jumlahBarang
        print("Total harga barang adalah ", total)
    
    case _:
        print("Member tidak dikenali") 
        # Member yang tidak dikenali akan di lakukan logika yang sama seperti tidak memiliki member
        total = hargaBarang * jumlahBarang
        print("Total harga barang adalah ", total)