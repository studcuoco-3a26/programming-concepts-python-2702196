def applica_sconto_benvenuto(prezzo_iniziale):
    return prezzo_iniziale - 5

prodotti = {
    "maglietta": 25,
    "scarpe": 80,
    "cappello": 15
}

totale = 0

print(" Benvenuto! Digita 'stop' per terminare.")

while True:
    prodotto = input("Cosa vuoi comprare? ").lower()  
    if prodotto == "stop":
        break

    if prodotto in prodotti:
        prezzo = prodotti[prodotto]
        totale += prezzo
        print(f"Aggiunto {prodotto} - {prezzo}€")
    else:
        print(" Prodotto non disponibile")

if totale > 0:
    print("\nTotale prima dello sconto:", totale, "€")

    totale_finale = applica_sconto_benvenuto(totale)

    print("Totale dopo lo sconto:", totale_finale, "€")
else:
    print("Non hai acquistato nulla.")