import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)
    def test_varasto_ei_negatiivinen(self):
        erivarasto = Varasto(-1, -2)
        self.assertAlmostEqual(erivarasto.tilavuus, 0)
        
    def test_lisaa_varastoon_negatiivinen(self):
        self.varasto.lisaa_varastoon(-5)
        self.assertAlmostEqual(self.varasto.tilavuus, 10)
        
    def test_poista_varastosta_negatiivinen(self):
        self.varasto.ota_varastosta(-5)
        self.assertAlmostEqual(self.varasto.tilavuus, 10)
        
    def test_ota_varastosta_liikaa(self):
        self.varasto.lisaa_varastoon(10)
        self.assertAlmostEqual(self.varasto.ota_varastosta(11), 10)
        self.assertAlmostEqual(self.varasto.saldo, 0)
    def test_saldo_eiole_suurempi_kuin_tilavuus(self):
        varasto2 = Varasto(10, 12)
        self.assertAlmostEqual(varasto2.saldo, 10)
    def test_eivoi_lisata_yli_tilavuuden(self):
        self.varasto.lisaa_varastoon(20)
        self.assertAlmostEqual(self.varasto.saldo, 9)
    def test_str(self):
        self.assertEqual(str(self.varasto), "saldo = 0, vielä tilaa 10")