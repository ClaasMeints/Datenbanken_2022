# Beschreibung der Anforderungen

## Das Kühlschrank-Verwaltungssystem

- Lösung um den Inhalt von Kühl- und Gefrierschränken zu erfassen und zu verwalten
- Bedienung per App
- Anknüpfen einer IoT-Plattform zur Anbindung von Kühlschränken
- Verwenden von Barcodes zur Erfassung der Produkte -> Barcode-Scanner IoT-Device
- Perspektivisch auch Erfassung von Produkten ohne Barcode mittels Neuronaler Netze
- Datenbank zur Speicherung der Produkte als MVP
- Erweiterungen:
  - Rezepteverwaltung
  - Produkterkennung ohne Barcode
  - Anonymisierte Analysen auf zum Nutzungsverhalten
  - Ernährungsberatung / Ernährungsplanung
  - Energieverbrauchsoptimierung von Kühl- und Gefrierschränken -> IoT-Device inklusive Temperaturmessung

## Anforderungen an die Datenbank

- Speicherung der Produkte
- Benutzerverwaltung
- Geräteverwaltung
- (Automatisches) Erstellen von Einkaufslisten
- Einordnen der Produkte in Kategorien
- Speicherung von Produkthistorie -> nützlich für Einkaufslisten und um zu erkennen ob Produkte neu gekauft sind oder wieder zurückgelegt wurden
- Informationen über Haltbarkeit und Füllstand der Produkte
- Bilder und Icons für das Frontend
- Erweiterbarkeit für weitere Funktionen mitdenken:

## Abgrenzung der Anforderungen

- MVP!
- Keine voll Funktionsfähige/Ansprechende App
- Keine Verbindung zur IoT-Plattform
- Keine Anbindung echter Geräte -> Simulation durch Python Skript
- Kein Deployment in der Cloud
- Keine Benutzermanagement -> keine Authentifizierung / Autorisierung

# Modellierung der Datenbank

## Konzeptionelles Schema

## Physisches Schema

## Nachweis der Normalformen

# Entwicklung des Backends

## Entwurf der Architektur

## Schnittstellendefinition

## Implementierung des Datenbankmodells

# Entwicklung und Simulation des Frontends

## Entwurf der Android-App

## Simulation von Drittsystemen

# Ergebnisse
