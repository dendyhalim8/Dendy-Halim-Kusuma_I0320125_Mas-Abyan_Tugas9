import sys
Kamus = {'one':'satu',
         'two':'dua',
         'three':'tiga',
         'four':'empat',
         'five':'lima',
         'six':'enam',
         'seven':'tujuh',
         'eight':'delapa,',
         'nine':'sembilan',
         'ten':'sepuluh'}
def main():
    kata = input("Masukan kata dalam bahasa inggris: ")

    if not (kata in Kamus.keys()):
        print("'%s tidak ditemukan di dalam kamus ini"%kata)
        sys.exit(1)

    print("Arti kata '%s' adalah '%s'"%(kata, Kamus[kata]))

if __name__ == "__main__":
    main()