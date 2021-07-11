# CovScan
 EU Digital Covid Vaccination Certificates Scan System, based on Python 3.
 
 
 ## Funktion
 Basierend auf einem Raspberry Pi 3B / 3B+ soll das System über eine angeschlossene Kamera die QR Codes scannen.
 Bei erfolgreichem Scan und Verifikation, wird ein Audiovisuelles Signal (in Form von z.B. einem Bildschirm, einer LED, einem Buzzer, ...) abgegeben, um so einer Aufsichtsperson Feedback zu geben.
 
 Das System soll zu einem Systemverbund vernetzt werden können, inkl. einem Administratorpanel mit Monitoring-Funktion.
 U.U. ist geplant ein tracking ein zu bauen, welches gescannte QR Codes speichert, um eine illegale doppelte Nutzung zu verhindern (Code Sharing).
 In wie fern ein tracking möglich ist, vor dem Hintergrund des Verlassens und Wiedereintritt der Location ist noch zu klären (Abmeldung, Wiederanmeldung bei Code Sharing Blockade). Das Trackingsystem muss auf das jeweilige Vorhaben angepasst werden (z.B. mit Code Sharing Timeout).
 
 
 ## Vorteile
 + Weniger Personal zum Scannen notwendig
 + Personen schneller abfertigen
 + Code Sharing Blockade
 + Tracking über Besucher / Zahl der Scans
 + Mehrere Scan Stationen verbinden
 + Monitoring der Scan Stationen
 

 ## Komponenten
 + Raspberry Pi 3B / 3B+
 + Kamera (min. 5MP / 1080p)
 + LEDs / Buzzer / Screen
 
 
 ## Changelog
 
 Version 0.0.1-A | 11.07.2021
 ```
 + Initial Commit
 + Gerüst aufgebaut
 + Ausarbeitung Projekt
 ```
