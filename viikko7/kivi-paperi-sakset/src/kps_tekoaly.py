from kps import KiviPaperiSakset
from tekoaly import Tekoaly


class KPSTekoaly(KiviPaperiSakset):
    def __init__(self):
        super().__init__()
        self.tekoaly=Tekoaly()

    def _toisen_siirto(self, ekan_siirto):
        siirto=self.tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {siirto}")
        return siirto
