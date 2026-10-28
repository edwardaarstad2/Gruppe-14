
# Interaktiv historie: Erling og prosjektteamet

print("======================================")
print(" DEN DIGITALE MEDBORGERPORTALEN")
print("======================================")
print("Du spiller Erling, prosjektleder for et")
print("team som utvikler kommunens nye portal.")
print("Det er tre uker til prototypen skal være klar.")
print("Teamet har begynt å få samarbeidsproblemer.\n")

# BESLUTNING 1: Konflikten mellom Silje og Elias

print("VALG 1: Silje og Elias er i en opphetet konflikt.")
print("Silje vil prioritere design, mens Elias vil prioritere")
print("sikkerhet og kostnader.")
print("Hva velger du å gjøre?")
print("1: Ta konflikten opp i et felles møte.")
print("2: Snakke med dem hver for seg først.")

valg1 = input("Skriv 1 eller 2: ")

if valg1 == "1":
    print("\nDu samler teamet til et felles møte.")
    print("Begge får forklare seg, men diskusjonen blir intens.")
    print("Resten av teamet merker at stemningen er spent.")
elif valg1 == "2":
    print("\nDu snakker med Silje og Elias hver for seg.")
    print("Du får bedre forståelse for begge perspektivene.")
    print("Det blir lettere å planlegge en konstruktiv samtale.")
else:
    print("Ugyldig valg. Programmet avsluttes.")
    exit()

# BESLUTNING 2: Konflikten mellom Hamdi og Hallgeir

print("\nVALG 2: Hamdi og Hallgeir er uenige om digitale folkemøter.")
print("Hamdi ønsker kontroll, mens Hallgeir ønsker åpen dialog.")
print("Hva velger du å gjøre?")
print("1: Arrangere et felles avklaringsmøte.")
print("2: Vente og la dem forsøke å løse det selv.")

valg2 = input("Skriv 1 eller 2: ")

if valg2 == "1":
    print("\nDu arrangerer et avklaringsmøte.")
    print("Partene diskuterer behovene sine og ser etter")
    print("en løsning som kombinerer moderering og åpen dialog.")
elif valg2 == "2":
    print("\nDu lar Hamdi og Hallgeir forsøke å finne en løsning.")
    print("De får større selvstendighet, men frustrasjonen")
    print("kan vokse dersom de ikke blir enige.")
else:
    print("Ugyldig valg. Programmet avsluttes.")
    exit()

# BESLUTNING 3: Motivasjon og fremdrift

print("\nVALG 3: Teamet trenger både samarbeid og fremdrift.")
print("Hva velger du å prioritere?")
print("1: Bruke tid på tillit og relasjonsbygging.")
print("2: Prioritere arbeidsoppgaver og leveranser.")

valg3 = input("Skriv 1 eller 2: ")

if valg3 == "1":
    print("\nDu setter av tid til samarbeid og relasjonsbygging.")
    print("Teamet får mulighet til å gjenoppbygge tillit.")
elif valg3 == "2":
    print("\nDu prioriterer fremdrift og tydelige tidsfrister.")
    print("Teamet arbeider videre, men noen føler at")
    print("konfliktene ikke har blitt tatt på alvor.")
else:
    print("Ugyldig valg. Programmet avsluttes.")
    exit()

# SLUTT: Bestem endepunkt ut fra valgene

print("\n======================================")
print(" HISTORIENS SLUTT")
print("======================================")

if valg1 == "2" and valg2 == "1" and valg3 == "1":
    print("ENDepunkt 1: TILLIT OG SAMARBEID")
    print("Du har lyttet til partene, avklart uenighetene")
    print("og prioritert relasjonene i teamet.")
    print("Teamet finner bedre arbeidsformer og beveger")
    print("seg mot norming-fasen.")

elif valg1 == "1" and valg2 == "2" and valg3 == "2":
    print("ENDEPUNKT 3: SVEKKET SAMHOLD")
    print("Konfliktene har ikke blitt håndtert godt nok.")
    print("Motivasjonen synker, kommunikasjonen svekkes,")
    print("og prototypen risikerer å bli forsinket.")

else:
    print("ENDEPUNKT 2: DELVIS LØSNING")
    print("Du har tatt noen grep, men teamet har fortsatt")
    print("utfordringer med kommunikasjon og tillit.")
    print("Prosjektet fortsetter, men trenger oppfølging.")

print("\nTakk for at du spilte prosjektleder Erling!")

