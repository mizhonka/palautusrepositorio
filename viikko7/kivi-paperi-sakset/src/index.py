from peli import Peli


def main():
    while True:
        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )

        vastaus = input()
        tyyppi=vastaus[-1]

        if tyyppi in "abc":
            uusi_peli=Peli.luo_peli(tyyppi)
            uusi_peli.pelaa()
        else:
            break


if __name__ == "__main__":
    main()
