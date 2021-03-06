# CoPoDo
 Corona Präventions Dokumentations Software
 
 
 ## Funktion
 Über einen QR Code wird z.B. in einem Restaurant an jedem Tisch ein eigener Code generiert und angebracht. Kunden scannen bei Ankuft mit der passenden App den Code ab und sind damit in der Datenbank erfasst. Nach einer gewissen Zeit wird nachgefragt ob Location schon verlassen wurde oder noch anwesend ist. Bei negativer oder keiner Antwort wird der User automatisch ausgelogt.
 
 ## Vorteile
 + Kein Papierkrieg mehr
 + Verifizierte Angaben
 + Datenschutz für Kunden
 + Umweltfreundlicher
 + Entlastung der Gesundheitsämter
 
 ## Komponenten
 
 ### App
 Über die App werden die User registriert und verifiziert. Checkin und Checkout läuft über die App sowie die einsicht in die eigene Historie
 
 ### Server
 Der Server ist der Schlüssel bei dem System. Hier werden die Daten gesammelt und gespeichert. Gleichzeitig richten die Geschäfte hier ihre Konten ein und managen diese
 
 ### WebApp
 Gleiche wie App, nur als WebApp für Offline User
 
 
 ## RoadMap
 
 ### Server
 1. Grundgerüst über PHP --> DB Struktur + Anbindungs Klasse
 2. Rest API Oauth 2.0 (2FA)
 3. Backend gerüst erstellen
 4. Framework integrieren
 5. Funktionen ausbauen
 6. API + DB verschlüsselung integrieren und ausbauen (MD5? RSA?)
 
 
 
 ## Changelog
 
 Version 0.0.1-A
 ```
 + Initial Commit
 + Gerüst aufgebaut
 + Ausarbeitung Projekt
 ```
