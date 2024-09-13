class Inventario:
    def __init__(self):
        self._inventario = {}
    def aggiungi_prodotto(self, nome, quantita, prezzo_unitario):
        """
        Aggiunge un prodotto all'inventario del negozio con il nome, la quantità e il prezzo unitario specificati
        """
        if nome in self._inventario: #se nome è una chiave nel dizionario
            self._inventario[nome]["quantita"] = self._inventario[nome]["quantita"] + quantita
        else:
            self._inventario[nome] = {"quantita":quantita, "prezzo_uni":prezzo_unitario}
    def rimuovi_prodotto(self, nome, quantita):
        """
        Rimuove una quantità specificata di un prodotto dall'inventario
        """
        if nome in self._inventario:#se nome è una chiave nel dizionario
            if self._inventario[nome]["quantita"] >= quantita: 
                self._inventario[nome]["quantita"] = self._inventario[nome]["quantita"] - quantita
                if self._inventario[nome]["quantita"] == 0:
                    del self._inventario[nome]
            else:
                print("Quantita insufficente disponibile per rimuovere il prodotto")
        else:
            print("Il prodotto non è presente nell'inventario")
    def restituisci_inventario(self):
        """
        Restituisce l'inventario
        """
        return self._inventario


class Carrello:
    def __init__(self):
        self._carrello = {}
    def aggiungi_prodotto(self, nome_prodotto, quantita, inventario):
        """
        Aggiunge al carrello 
        """
        if nome_prodotto in inventario.restituisci_inventario():
            if nome_prodotto in self._carrello:
                self._carrello[nome_prodotto] = self._carrello[nome_prodotto] + quantita
            else:
                self._carrello[nome_prodotto] = quantita
        else:
            print("Il prodotto non è presente nel negozio")
    def rimuovi_prodotto(self, nome_prodotto, quantita):
        """
        Rimuove dal carrello
        """
        if nome_prodotto in self._carrello:
            if self._carrello[nome_prodotto] >= quantita:
                self._carrello[nome_prodotto] = self._carrello[nome_prodotto] - quantita
                if self._carrello[nome_prodotto] == 0:
                    del self._carrello[nome_prodotto]
            else:
                print("Quantita insufficiente disponibile per rimuovere il prodotto")
        else:
            print("Il prodotto non è presente nel carrello")
    def restituisci_carrello(self):
        """
        Restituisce il carrello
        """
        return self._carrello
    def calcola_tot_acquisto(self, inventario):
        """
        Calcola il totale dell'acquisto 
        """
        tot = 0
        for prodotto, quantita in self._carrello.items():
            if prodotto in inventario.restituisci_inventario():
                prezzo_unitario = inventario.restituisci_inventario()[prodotto]["prezzo_uni"]
                tot += quantita * prezzo_unitario
            else:
                print(f"Il prodotto '{prodotto}' non è disponibile.")
        return tot


def main():
    inventario = Inventario()
    print("GESTIONE DELL'INVENTARIO")
    while True:
        print("1.Aggiungi un prodotto all'inventario")
        print("2.Rimuovi dall'inventario")
        print("3.Visualizza l'inventario")
        print("4. Esci dalla gestione dell'inventario")
        print()
        scelta = input("Inserisci la scelta: ")
        if scelta == '1':
            nome_prodotto = input("Inserisci il prodotto che vuoi aggiungere: ")
            quantita = int(input("Inserisci la quantita del prodotto da aggiungere: "))
            prezzo_unitario = float(input("Inserisci il prezzo del prodotto: "))
            inventario.aggiungi_prodotto(nome_prodotto, quantita, prezzo_unitario)
        elif scelta == '2':
            nome_prodotto = input("Inserisci il prodotto che vuoi rimuovere: ")
            quantita = int(input("Inserisci la quantita del prodotto da rimuovere: "))
            inventario.rimuovi_prodotto(nome_prodotto, quantita) 
        elif scelta == '3':
            for prodotto, dettagli in inventario.restituisci_inventario().items():
                print(f"{prodotto}: {dettagli['quantita']}, Prezzo unitario: {dettagli['prezzo_uni']}")
        elif scelta == '4':
            break
    print()
    print("GESTIONE DEL CARRELLO")
    carrello = Carrello()
    while True:
        print("1.Aggiungi un prodotto al carrello")
        print("2.Rimuovi dal carrello")
        print("3.Visualizza il carrello")
        print("4.Visualizza il totale dell'acquisto")
        print("5.Esci dalla gestione del carrello")
        print()
        scelta = input("Inserisci la scelta: ")
        if scelta == '1':
            nome_prodotto = input("Inserisci il prodotto che vuoi aggiungere: ")
            quantita = int(input("Inserisci la quantita del prodotto da aggiungere: "))
            carrello.aggiungi_prodotto(nome_prodotto, quantita, inventario)
        elif scelta == '2':
            nome_prodotto = input("Inserisci il prodotto che vuoi rimuovere: ")
            quantita = int(input("Inserisci la quantita del prodotto da rimuovere: "))
            carrello.rimuovi_prodotto(nome_prodotto, quantita) 
        elif scelta == '3':
            for prodotto, quantita in carrello.restituisci_carrello().items():
                print(f"{prodotto}: {quantita}")
        elif scelta == '4':
            print("Totale", carrello.calcola_tot_acquisto(inventario))
        elif scelta == '5':
            break


if __name__  == "__main__":
    main()  


