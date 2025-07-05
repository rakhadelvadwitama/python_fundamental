
def runMatch():
    num = int(input("Masukkan angka: "))
    match num:
        case 1:
            print("Anda memilih opsi 1")
        case 2:
            print("Anda memilih opsi 2")
        case 3:
            print("Anda memilih opsi 3")
        case _:
            print("Opsi tidak valid")