# Promemoria per il colloquio — metriche misurate

Tre modelli, cento campioni ciascuno, generazione in locale con Ollama a
temperatura 0. Ogni metrica è riportata in percentuale.

---

## Parte statica — senza eseguire i test

### 1. Test scritti / non scritti

**100%, 100%, 100%.** Nessun fallimento della pipeline: tutti e trecento i
campioni hanno prodotto un file.

Da dire: il ramo è vuoto perché l'esecuzione è locale e deterministica. Su
NVIDIA non lo era — gli endpoint smettevano di rispondere e lo script prevedeva
sei tentativi per campione.

### 2. Validità sintattica

**1B 92%, 3B 99%, 8B 94%.** Verificata con `ast.parse`, senza eseguire nulla.

I file non validi sono quasi tutti troncati.

### 3. Troncamento della risposta

**1B 5%, 3B 0%, 8B 6%.** Non segue la taglia del modello.

Da dire: non basta scrivere troppi test per venire troncati. Fra i file tagliati
ce ne sono con 3, 5, 6 e 7 funzioni di test, cioè dentro il vincolo del prompt.
Conta anche quanto sono verbosi i singoli test.

### 4. Aderenza ai vincoli del prompt

**1B 21,7%, 3B 79,8%, 8B 96,8%** sul rispetto di tutti e quattro i vincoli
(import corretto, da 3 a 8 test, nomi conformi, un assert per test).

Il dettaglio che conta è l'import:

| | 1B | 3B | 8B |
|---|---|---|---|
| import corretto | **23,9%** | 100% | 100% |
| da 3 a 8 test | 93,5% | 100% | 98,9% |
| nomi conformi | 95,7% | 99,0% | 100% |
| un assert per test | 89,1% | 80,8% | 97,9% |

Da dire: l'import è una **soglia, non un gradiente**. Il 1B lo sbaglia tre volte
su quattro e ripiega su `import pytest`; il 3B lo rispetta sempre. E il totale
del 1B è determinato quasi solo da quella voce, visto che gli altri tre vincoli
stanno sopra l'89%.

Nota sul valore basso del 3B sull'assert: quei casi sono blocchi
`pytest.raises`, che verificano il sollevamento di un'eccezione. Alla lettera
violano il vincolo, ma un oracolo ce l'hanno — infatti sulla variante che
accetta anche `pytest.raises` il 3B fa 100%.

### 5. Tempo di generazione

**1B 24,2 s, 3B 37,2 s, 8B 90,8 s** per campione.

Confrontabile solo a parità di infrastruttura: sull'8B remoto erano circa 3
secondi.

---

## Parte dinamica — eseguendo i test

### 6. Esiti dell'esecuzione

| | 1B | 3B | 8B |
|---|---|---|---|
| passato (tutti i test del file) | 0 | 2 | 2 |
| fallito | 83 | 96 | 91 |
| non eseguibile | 16 | 1 | 6 |
| timeout | 1 | 1 | 1 |

**Questo risolve la prima domanda aperta.** I file in cui *tutti* i test passano
sono due su cento. Qualunque metrica calcolata sui "file che hanno successo"
avrebbe una base di due campioni. La lettura per singolo test è l'unica
praticabile, ed è anche quella coerente con il Pass@k di ULT.

I campioni con **almeno un** test passato sono 7, 45 e 56: è questa la base
utilizzabile per le misure che richiedono test funzionanti.

### 7. Correttezza — Pass@1 sul singolo test

**1B 3,5%, 3B 16,9%, 8B 21,6%.**

In assoluto: 25 test corretti su 709, 118 su 699, 144 su 667.

### 8. Copertura di riga

| base di calcolo | 1B | 3B | 8B |
|---|---|---|---|
| tutti i campioni | 12,2% | 68,3% | 71,1% |
| soli campioni eseguibili | 14,7% | 69,7% | 76,5% |
| soli campioni con import corretto | **61,0%** | 69,7% | 76,5% |

Da dire: il crollo del 1B è **interamente** l'import. Sui venti campioni in cui
ha importato la funzione copre il 61%, non lontano dal 3B. Senza l'import la
funzione non viene mai chiamata e la copertura è nulla per costruzione.

### 9. Copertura di ramo

**1B 11,2%, 3B 59,1%, 8B 66,6%** sui campioni eseguibili.

Sta sistematicamente una decina di punti sotto quella di riga, come atteso su
funzioni con complessità ciclomatica non inferiore a dieci.

### 10. Copertura eseguita contro verificata *(la misura nuova)*

Calcolata due volte: con tutti i test, e con i soli test che passano.

| | 1B | 3B | 8B |
|---|---|---|---|
| righe eseguite | 54,7% | 73,2% | 77,1% |
| righe verificate | 42,6% | 58,0% | 58,0% |
| rami eseguiti | 45,9% | 64,1% | 67,5% |
| rami verificati | 26,1% | 45,0% | 45,8% |

Da dire: la differenza fra le due righe è **quanto la copertura sopravvaluta ciò
che i test garantiscono**. È l'argomento di Inozemtseva reso operativo.

E il confronto a parità di campioni — i 30 in cui sia 3B che 8B hanno almeno un
test passato: sulla copertura **eseguita** l'8B è avanti di 3,1 punti, su quella
**verificata** di 0,8. Il codice in più che l'8B raggiunge lo raggiunge con test
che falliscono.

### 11. Duplicazione

| | 1B | 3B | 8B |
|---|---|---|---|
| tutte le righe di test | 13,6% | 3,7% | **25,3%** |
| soli test passati | 10,7% | 0,7% | 8,9% |

Definizione: quota di righe ripetute sul totale delle righe di test.

Da dire: l'8B è il più ridondante, con 54 file su 93 sopra il 20% contro 5 su 98
del 3B. Ripete la stessa preparazione in ogni test — in un campione le righe
`match = [0, 1, 2]` e `m = 10` compaiono otto volte identiche. È il *Test Code
Duplication* del catalogo di van Deursen.

Cautela: il 3,7% del 3B non è un merito. Duplica poco perché scrive test più
scarni, spesso un solo assert senza preparazione.

---

## Analisi dei fallimenti — 1788 test falliti

| | 1B | 3B | 8B |
|---|---|---|---|
| `AssertionError` | 21,5% | 71,1% | 81,8% |
| `NameError` | 72,2% | 9,0% | 4,4% |
| **la funzione viene eseguita** → errore di oracolo | **25,7%** | **88,6%** | **93,9%** |
| **la funzione non si raggiunge** → errore d'uso | **74,3%** | **11,4%** | **6,1%** |

Da dire: **crescendo, il modello non fallisce di meno — fallisce in modo
diverso.** Il 1B sbaglia a livello meccanico e non tocca la funzione in tre casi
su quattro. Il 3B e l'8B seguono le istruzioni e vanno a sbattere contro
l'ostacolo successivo, che è l'oracolo.

Spiega anche perché la copertura resta alta mentre la correttezza crolla: nel
93,9% dei fallimenti dell'8B la funzione viene comunque eseguita.

---

## Da chiedere

1. **"Aderenza al formato (explicit typing)"** — cosa intendeva? Il prompt non
   chiede annotazioni di tipo.
2. **"Imitation score"** — cosa intendeva? Ipotesi: somiglianza fra test generati
   e test umani, che TestPilot misura con la distanza di edit normalizzata.
3. **Mutation score** — è l'unica metrica non ancora calcolata. Richiede suite
   che passino sul codice sano, quindi va fatto sul sottoinsieme dei test
   passati: la base è 45 campioni sul 3B e 56 sull'8B, ma solo 7 sul 1B. Vale la
   pena a questa scala, o va negli sviluppi futuri?

## Da riferire

- I file che passano interamente sono due su cento: si lavora per singolo test.
- Otto campioni sembravano falliti in generazione, ma era un bug di codifica
  UTF-8 dello script sui caratteri giapponesi, non un fallimento dei modelli.
  Corretto, ora la generazione è completa su tutti e trecento.
- Fra due esecuzioni successive le medie oscillano di circa due decimi di punto,
  perché alcune funzioni del dataset usano numeri pseudocasuali.
