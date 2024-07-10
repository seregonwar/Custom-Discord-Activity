
# Custom-Discord-Activity

<details>
<summary>Select Language</summary>

- [English](english)
- [Italiano](italiano)

</details>

---

<details id="english">
<summary>English</summary>

This repository provides a practical example of integrating Discord Rich Presence using the `pypresence` library. Rich Presence enhances user experience by dynamically updating game status information on Discord profiles.

## Key Features

### Initialization and Connection

```python
from pypresence import Presence
import time

# Replace with your own Discord Client ID
client_id = 'YOUR_CLIENT_ID'
RPC = Presence(client_id)
RPC.connect()
```

This code block initializes and connects your program to Discord using your application's Client ID.

### Updating Game Status

```python
def update_presence():
    try:
        RPC.update(
            state="Playing as Lucia",
            details="Exploring South Beach",
            large_image="photo1",
            large_text="Grand Theft Auto VI",
            start=time.time()
        )
        print("Rich Presence updated successfully.")
    except Exception as e:
        print(f"Error updating Rich Presence: {e}")
```

The `update_presence()` function dynamically updates the game status on Discord. Customize attributes like `state`, `details`, `large_image`, and `large_text` to reflect the currently played game and other relevant information.

### Continuous Update Loop

```python
if __name__ == "__main__":
    try:
        update_presence()
        print("Rich Presence activated. Press Ctrl+C to terminate.")
        
        while True:
            time.sleep(15)
    except KeyboardInterrupt:
        print("Rich Presence terminated.")
    finally:
        RPC.close()
```

This code segment keeps Rich Presence active through a continuous update loop. Adjust `time.sleep(15)` to customize the update frequency.

### How to Use

1. **Initial Setup**: Ensure Python and `pypresence` are installed. Replace `client_id` with your Discord Client ID in the initialization.

2. **Customize Activity**: Modify parameters in `RPC.update()` within `update_presence()` to update game status and activity details.

3. **Running the Program**: Execute the Python script. Rich Presence will be activated and updated automatically on Discord.

This project serves as an essential guide for developers interested in implementing and customizing Rich Presence in their applications, enhancing visibility and engagement on Discord.

### Example
![image](https://github.com/seregonwar/Custom-Discord-Activity/assets/109359355/92b964f7-cb37-475e-8df8-f52041faac3b)

</details>

---

<details id="italiano">
<summary>Italiano</summary>

Questo repository fornisce un esempio pratico di integrazione di Discord Rich Presence utilizzando la libreria `pypresence`. Rich Presence migliora l'esperienza utente aggiornando dinamicamente le informazioni sullo stato del gioco nei profili Discord.

## Caratteristiche principali

### Inizializzazione e Connessione

```python
from pypresence import Presence
import time

# Sostituisci con il tuo ID client di Discord
client_id = 'YOUR_CLIENT_ID'
RPC = Presence(client_id)
RPC.connect()
```

Questo blocco di codice inizializza e collega il tuo programma a Discord utilizzando l'ID client della tua applicazione.

### Aggiornamento dello Stato del Gioco

```python
def update_presence():
    try:
        RPC.update(
            state="Giocando come Lucia",
            details="Esplorando South Beach",
            large_image="photo1",
            large_text="Grand Theft Auto VI",
            start=time.time()
        )
        print("Rich Presence aggiornato con successo.")
    except Exception as e:
        print(f"Errore nell'aggiornamento di Rich Presence: {e}")
```

La funzione `update_presence()` aggiorna dinamicamente lo stato del gioco su Discord. Personalizza attributi come `state`, `details`, `large_image` e `large_text` per riflettere il gioco attualmente in esecuzione e altre informazioni rilevanti.

### Ciclo di Aggiornamento Continuo

```python
if __name__ == "__main__":
    try:
        update_presence()
        print("Rich Presence attivato. Premi Ctrl+C per terminare.")
        
        while True:
            time.sleep(15)
    except KeyboardInterrupt:
        print("Rich Presence terminato.")
    finally:
        RPC.close()
```

Questo segmento di codice mantiene attivo Rich Presence tramite un ciclo di aggiornamento continuo. Regola `time.sleep(15)` per personalizzare la frequenza di aggiornamento.

### Come Usare

1. **Configurazione Iniziale**: Assicurati che Python e `pypresence` siano installati. Sostituisci `client_id` con il tuo ID client di Discord nell'inizializzazione.

2. **Personalizza Attività**: Modifica i parametri in `RPC.update()` all'interno di `update_presence()` per aggiornare lo stato del gioco e i dettagli dell'attività.

3. **Esecuzione del Programma**: Esegui lo script Python. Rich Presence verrà attivato e aggiornato automaticamente su Discord.

Questo progetto serve come guida essenziale per gli sviluppatori interessati a implementare e personalizzare Rich Presence nelle loro applicazioni, migliorando la visibilità e l'engagement su Discord.

### Esempio
![image](https://github.com/seregonwar/Custom-Discord-Activity/assets/109359355/92b964f7-cb37-475e-8df8-f52041faac3b)

</details>
