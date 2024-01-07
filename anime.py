import os, sys, time, json
import requests as req 

url = 'https://api.jikan.moe/v4/'

idlist = 1
mal_id = []

# warna python
p = "\033[0;37m"
h = "\033[0;32m"

def pilihAnime():
    os.system('cls')
    print("My AnimeList")
    print("1. Top Anime")
    print("2. Search Anime")
    choice = input("\nPilih: ")
    if choice in ['1', '01']:
        top_anime()
    else:
        print("maaf pilihan tidak ada!")
        time.sleep(1)
        pilihAnime()


# function untuk data anime

def top_anime():
    global idlist

    print("List Top Anime")
    
    try:

        response = req.get(url + 'top/anime')
        dataJson = response.json()
        for i in dataJson['data']:
            print(f"{idlist}. {i['title']}")
            idlist += 1
            mal_id.append(i['mal_id'])
    except Exception as e:
        print("[!] Error : " + e)

    print("\nApakah Anda Ingin Lihat Detail Anime? y/t")
    choice = input("--> ").lower()

    if choice == 'y':
        inputAnime = int(input("\nMasukan nomor list anime di atas\nNomor: "))
        inputAnime -= 1
        showDetail(inputAnime)
    elif choice == 't':
        print("\nAnda akan di arahkan ke menu utama!")
        time.sleep(1)
        pilihAnime()
    else:
        print("\nMaaf pilihan tidak ada!")
        os.sys.exit()


# show detail anime

def showDetail(id):
    id = mal_id[id]
    try:
        response = req.get(url + 'anime/' + str(id))
        dataJson = response.json()['data']
        os.system('cls')
        print(f"\nTitle : {h}{dataJson['title']}{p}")
        print(f"Synopsis : {h}{dataJson['synopsis']}{p}\n")
        print(f"Type : {h}{dataJson['type']}{p}")
        print(f"Episodes : {h}{dataJson['episodes']}{p}")

    except Exception as e:
        print("[!] Error : " + e)

if __name__ == "__main__":
    pilihAnime()
