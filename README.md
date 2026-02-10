# Alby Intelligence
***Alby Intelligence's acronim is "AI"***

This is a multi-purpose personal project.
- The first purpose (as of today 10 Feb 2026) is a pure accademic one; I want and need to learn how to write an develop a web app with Django. 
- The second one is to demonstrate to a specific company that I want to work for them by creating a web app similar to the one they develop and sell (even with strong limitations due to the fact that I didn't studied the topic deeply).
- The third is to have a web app in which I can experiment with new tools, such as LLMs.

## Main features
| Area | Funzionalità | Descrizione breve |
| --- | --- | --- |
| Rapporto di lavoro | Assunzioni 100% digitali | Digitalizzazione dell’assunzione e processi collegati (contratto, onboarding). |
| Rapporto di lavoro | Firma elettronica del contratto | Firma del contratto con audit trail, autenticazione adeguata, conservazione a norma; collegabile a flussi HR. |
| Rapporto di lavoro | Onboarding digitale | Dopo firma: creazione “cartelle/documenti”, impostazioni operative (es. regole presenze), documenti accessori. |
| Persone | Directory dipendenti | Anagrafica centralizzata dei dipendenti (directory). |
| Ecosistema | Professionisti esterni | Accesso/coinvolgimento di figure esterne (es. consulenti del lavoro) nel flusso HR/payroll. |
| Tempo e presenze | Ferie e permessi | Gestione richieste/approvazioni ferie e permessi (time-off). |
| Tempo e presenze | Turni e lavoro intermittente | Pianificazione turni con controllo costi, straordinari e maggiorazioni; gestione assenze nel calendario; template e copia pianificazioni; calcoli “in base al CCNL”. |
| Tempo e presenze | Rilevazione presenze (timbrature) | Timbrature digitali per presenze (app/web), con opzioni come QR code e geolocalizzazione; output utilizzabile per payroll. |
| Paghe e rimborsi | Elaborazione cedolini online | Workflow paghe: import automatico di ferie e rimborsi in cedolino; gestione bonus/variabili; controllo differenze rispetto mese precedente; invio cedolini ai dipendenti (notifica + disponibilità in app). |
| Paghe e rimborsi | Stipendi: pagamento SEPA “unico” | Pagamento stipendi raggruppato con bonifico SEPA unico; calcolo importi netti e distribuzione ai dipendenti. |
| Paghe e rimborsi | F24 integrato + scadenze + invio a professionisti | Generazione modello F24 dopo pagamento stipendi, reminder scadenza; possibilità di invio automatico al commercialista. |
| Paghe e rimborsi | Nota spese (app + approvazione + cedolino) | Dipendente invia nota spese con foto giustificativo; manager approva/rifiuta; rimborso entra automaticamente in cedolino; archivio digitale “a norma”. |
| Paghe e rimborsi | Simulatore costo azienda e netto | Calcolo costo azienda e conversioni lordo-netto; confronto forme contrattuali (incluse non dipendenti); valutazione agevolazioni (es. Under 36, Donne, ecc.). |
| Scadenze e compliance | Scadenzario HR digitale | Calendario condiviso di scadenze (contratti, prova, corsi sicurezza, visite mediche, ecc.) con notifiche; integrato con HR e cedolini; orientato a compliance/audit. |
| Sicurezza lavoro | Corsi sicurezza e visite mediche | Tracciamento e gestione operativa di corsi/visite come parte degli adempimenti e dello scadenzario. |
| Reporting | Report e budget del personale | Report su costo azienda (anche per dipartimento/dipendente), saldi ferie, TFR; creazione budget e simulazioni assunzioni; export Excel; possibilità di report personalizzati. |
| Reporting | Report HR e KPI | Analytics (turnover, assenteismo, ore lavorate, ferie residue, costo medio, ecc.) con aggiornamento automatico dai moduli (presenze, ferie, cedolini, note spese). |
| IT asset | Device aziendali (noleggio/gestione) | Modulo per “device aziendali” (il sito lo presenta come feature di piattaforma). |
| Sicurezza dati | Privacy e sicurezza | Posizionamento su GDPR e standard di sicurezza (es. ISO/IEC 27001) e gestione dati personali. |
| Integrazioni | Integrazioni HRIS/ATS + API | Supporto concettuale a integrazioni: precompilazione dati contratto; aggiornamenti di stato; firme “in massa”; sincronizzazione con HRIS; collegamenti con onboarding. |
| Recruiting | “Software selezione personale” (ATS) | Modulo ATS o integrazione ATS. |
| Assenze | Malattia e giustificativi assenza | Gestione assenze oltre ferie (malattia, permessi speciali). |

## Technical specs
***Django is similar to MVC, but the View the layer that decide what to show in the template***

### Template
***No dependency, just native HTML, CSS and JavaScript***

- The UI needs to adhere to the best principles of web design. 
- In each page all the possible (and allowed) actions needs to be clearly understandable by the user.
- The colors needs to have a very good contracts between them, aiming at a AAA rating. 
- The font needs to be super fast to load and very easily readable, because the user will probably spend a lot of time in front of this during his working day.

### View
Django framework

### Model
***Tables***
- Employees
- Contracts
- External_consultants
- Documents
- Folders
- Ferie
- Permessi
- Malattia
- employee_presence_stamping
- expense_reports (note spesa)
- devices


