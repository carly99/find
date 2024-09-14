import find.find as find
class TestUnit:
    
    def test_aggiungi_prodotto_inventario_0(self):
        inventario = find.Inventario()
        inventario.aggiungi_prodotto("caffe", 6, 3)
        expected_result = 6
        computed_value = inventario.restituisci_inventario()["caffe"]["quantita"]
        assert expected_result == computed_value
    def test_aggiungi_prodotto_inventario_1(self):
        inventario = find.Inventario() 
        inventario.aggiungi_prodotto("biscotti", 2, 2.0) 
        inventario.aggiungi_prodotto("biscotti", 3, 2.0 )
        expected_result = 5
        computed_value = inventario.restituisci_inventario()["biscotti"]["quantita"]
        assert expected_result == computed_value 
    def test_rimuovi_prodotto_inventario_0(self):
        inventario = find.Inventario()
        inventario.aggiungi_prodotto("giochi", 4, 3)
        inventario.rimuovi_prodotto("giochi", 2)
        expected_result = 2
        computed_value = inventario.restituisci_inventario()["giochi"]["quantita"]
        assert expected_result == computed_value
    def test_rimuovi_prodotto_inventario_1(self):
        inventario = find.Inventario()
        inventario.aggiungi_prodotto("pizzette", 2, 3)
        inventario.rimuovi_prodotto("pizzette", 4)
        expected_result = 2
        computed_value = inventario.restituisci_inventario()["pizzette"]["quantita"]
        assert expected_result == computed_value
    def test_rimuovi_prodotto_inventario_2(self):
        inventario = find.Inventario()
        inventario.aggiungi_prodotto("cioccolatini", 2, 3.0)
        inventario.rimuovi_prodotto("cocco", 3)
        expected_result = 2
        computed_value = inventario.restituisci_inventario()["cioccolatini"]["quantita"]
        assert expected_result == computed_value
    def test_rimuovi_prodotto_inventario_3(self):
        inventario = find.Inventario()
        inventario.aggiungi_prodotto("barrette", 4, 3)
        inventario.rimuovi_prodotto("barrette", 4)
        expected_result = {}
        computed_value = inventario.restituisci_inventario()
        assert expected_result == computed_value
    def test_aggiungi_prodotto_carrello_0(self):
        inventario = find.Inventario()
        inventario.aggiungi_prodotto("formaggio", 3, 10.0) 
        carrello = find.Carrello() 
        carrello.aggiungi_prodotto("formaggio", 1, inventario)  
        expected_result = 1
        computed_value = carrello.restituisci_carrello()["formaggio"]
        assert expected_result == computed_value
    def test_aggiungi_prodotto_carrello_1(self):
        inventario = find.Inventario()
        inventario.aggiungi_prodotto("ananas", 3, 1.0)
        inventario.aggiungi_prodotto("lego", 3, 90) 
        carrello = find.Carrello() 
        carrello.aggiungi_prodotto("ananas", 1, inventario) 
        carrello.aggiungi_prodotto("ananas", 1, inventario) 
        expected_result = 2
        computed_value = carrello.restituisci_carrello()["ananas"] 
        assert expected_result == computed_value
    def test_rimuovi_prodotto_carrello_0(self):
        inventario = find.Inventario()
        inventario.aggiungi_prodotto("crocchette", 3, 8.5)
        carrello = find.Carrello()
        carrello.aggiungi_prodotto("crocchette", 2, inventario)
        carrello.rimuovi_prodotto("crocchette", 1)
        expected_result = 1
        computed_value = carrello.restituisci_carrello()["crocchette"]
        assert expected_result == computed_value
    def test_rimuovi_prodotto_carrello_2(self):
        inventario = find.Inventario()
        inventario.aggiungi_prodotto("torta", 3, 8.0)
        carrello = find.Carrello()
        carrello.aggiungi_prodotto("torta", 2, inventario)
        carrello.rimuovi_prodotto("macaron", 1)
        expected_result = 2
        computed_value = carrello.restituisci_carrello()["torta"]
        assert expected_result == computed_value
    def test_rimuovi_prodotto_carrello_3(self):
        inventario = find.Inventario()
        inventario.aggiungi_prodotto("mele", 6, 1.5)
        carrello = find.Carrello()
        carrello.aggiungi_prodotto("mele", 3, inventario)
        carrello.rimuovi_prodotto("mele", 4)
        expected_result = 3
        computed_value = carrello.restituisci_carrello()["mele"]
        assert expected_result == computed_value
    def test_rimuovi_prodotto_carrello_4(self):
        inventario = find.Inventario()
        inventario.aggiungi_prodotto("Crocchette", 6, 8.5)
        carrello = find.Carrello()
        carrello.aggiungi_prodotto("Crocchette", 3, inventario)
        carrello.rimuovi_prodotto("Crocchette", 3)
        expected_result = {}
        computed_value = carrello.restituisci_carrello()
        assert expected_result == computed_value
    def test_calcola_tot_acquisto_0(self):
        inventario = find.Inventario()
        inventario.aggiungi_prodotto("tovaglia", 2, 7.5)
        carrello = find.Carrello()
        carrello.aggiungi_prodotto("tovaglia", 1, inventario)
        expected_result = 7.5
        computed_value = carrello.calcola_tot_acquisto(inventario)
        assert expected_result == computed_value
    def test_calcola_tot_acquisto_1(self):
        inventario = find.Inventario()
        inventario.aggiungi_prodotto("crocchette", 2, 8.5)
        carrello = find.Carrello()
        carrello.aggiungi_prodotto("pane", 5, inventario)
        expected_result = 0
        computed_value = carrello.calcola_tot_acquisto(inventario)
        assert expected_result == computed_value
