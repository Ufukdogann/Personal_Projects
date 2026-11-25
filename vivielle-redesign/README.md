# Vivielle – Premium-Redesign (Prototyp)

Statischer Prototyp für ein Redesign von vivielle-intimates.com. Öffnen: `index.html` über einen lokalen Server
(`python3 -m http.server` in diesem Ordner, dann http://localhost:8000). Inhalte, Bilder und Video stammen von der Live-Seite.

## Ausgangslage (Live-Seite)
- Shopify-Store (Dawn-basiertes Theme), Sprache Deutsch, 5 Produkte: Body Bonny 99,99 €, Vivielle BH 59,99 €,
  Vivielle Tanga 39,99 €, Set Body+BH+Tanga 99,99 €, Bundle BH+Tanga 89,98 €.
- Branche: Luxus-Lingerie / Dessous, Direct-to-Consumer, Gründerinnen-Marke (Julie Vivien, Dreieich).
- Stärken: echte, stimmungsvolle Fotos in Schwarz; die Gründerinnen-Geschichte; 802 Bewertungen; Atelier-Video.
- Schwächen: Rabatt-Sprache dominiert („Cyber Monday“ im Menü und als Hero), verspieltes KI-Monogramm-Logo,
  Dawn-Standardlayout, widersprüchliche Angaben (Versand frei ab 79 € vs. 59 €; Set-Vergleichspreis 189,99 / 199,97 / 199,98 €),
  generische englische Bewertungen mit identischem Datum, Länderliste mit 200+ Einträgen im HTML.

## Wettbewerbsanalyse
| Marke | Konzept | Palette | Typografie | Ansprache |
|---|---|---|---|---|
| Agent Provocateur | Provokant, Film-Noir, Kampagnenbilder | Schwarz, Pink-Akzent | Kräftige Serif, Versalien | Verführerisch, selbstbewusst |
| Bordelle | Architektonisch, „Kapitel“-Kollektionen (Chapter 1: Astri) | Schwarz/Weiß, wenige Farbakzente | Neue Helvetica, Versalien | Kurz, kühl, Kollektion im Mittelpunkt; Showroom-Termine |
| Fleur du Mal | Editorial, Magazin-Look | Weiß, Schwarz, Blush (#d4857b) | Dala Floda (Serif) + Suisse (Grotesk) | Leicht, modisch, Kategorien nach Material (Charlotte Lace, Silk Luxe) |
| Kiki de Montparnasse | Pariser Boudoir, „World Of“, „In Confidence“ | Off-White, Anthrazit #222 | Cormorant (Serif) + Akzidenz Light | Leise, intim, viel Weißraum |
| Coco de Mer | „Home of Pleasure“, Salons, Personal Shopping | Pflaume #332124, Gold #ba8748, Creme | Serif + Montserrat | Warm, beratend, Club-Gefühl („Confidante“) |

Gemeinsame Muster: Wortmarke statt Bildlogo, Serif-Display + leichte Grotesk, Versal-Labels mit Laufweite, große Bilder ohne Rahmen,
Rabatte klein und ruhig, Material und Detail als Verkaufsargument, Beratung (Größe, Personal Shopping) als Service.

## Umsetzung im Prototyp
- **Marke:** Wortmarke VIVIELLE in Bodoni Moda mit „Belle Intimates“, Fließtext in Jost.
- **Palette:** Perl-Rosé als Grund, Noir für Bildbänder, Champagner-Gold nur als feiner Akzent (wie die Goldkette am BH),
  Bordeaux aus dem Atelier-Video für den Set-Bereich.
- **Struktur:** Hero mit Produktversprechen statt Rabatt; Service-Leiste; 3-Stück-Kollektion; Set als eigenes Kapitel mit
  transparenter Preisrechnung; Detail-Editorial; Atelier mit Video; persönlicher Brief; kuratierte Bewertungen;
  integrierter Größenrechner; Newsletter „neue Stücke in kleiner Auflage“.
- **Funktionen:** Kollektion mit Filtern, Produktseiten mit Größenwahl, Größenberater-Drawer (übernimmt Größe direkt),
  Warenkorb mit Fortschritt zum Gratisversand, Suche, mobile Navigation.

## Offene Punkte für die Live-Seite
- Versandschwelle (79 € oder 59 €) und Set-Vergleichspreis vereinheitlichen.
- Die generischen englischen Bewertungen vom 11.10.2024 prüfen bzw. entfernen; sie schaden der Glaubwürdigkeit.
- Material- und Pflegeangaben pro Produkt ergänzen (z. B. Zusammensetzung, Handwäsche).
- Umsetzung als Shopify-Theme (Sections/Liquid) auf Basis dieses Prototyps.
