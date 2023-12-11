from kps import KiviPaperiSakset
from tekoaly_parannettu import TekoalyParannettu


class KPSParempiTekoaly(KiviPaperiSakset):
    def __init__(self):
        super().__init__()
        self.tekoaly=TekoalyParannettu(10)

    def _toisen_siirto(self, ekan_siirto):
        siirto=self.tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {siirto}")
        self.tekoaly.aseta_siirto(ekan_siirto)
        return siirto
