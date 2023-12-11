from kps import KiviPaperiSakset


class KPSPelaajaVsPelaaja(KiviPaperiSakset):
    def _toisen_siirto(self, ekan_siirto):
        siirto=input("Toisen pelaajan siirto: ")
        return siirto

