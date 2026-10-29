#IS-118 Gruppeinnlevering 2 - Gruppe 14
# Master: felles løsning basert på ideer fra Ema, Fredrik og Edward. 
# Spilleren er prosjektleder Erling og tar tre valg som avgjør om teamet kommer seg gjennom storming-fasen.

# -------- VARIABLER --------
tillit = 0      # tillitspoeng, øker når Erling bygger tillit (fra Ema)
fremdrift = False   # blir True hvis Erling prioriterer leveransen (fra Edward)

# -------- INTRO --------
print("=" * 50)
print("DEN DIGITALE MEDBORGERPORTALEN")
print("=" * 50)
print("Du er Erling, prosjektleder for kommunens nye medborgerportal.")
print("Det har gått seks uker, og teamet er i storming-fasen.")
print("Silje og Elias er uenige om teknologi og design.")
print("Hamdi og Hallgeir er uenige om digitale folkemøter.")
print("Første prototype skal være klar om tre uker.")
print("Svar med a eller b for å ta et valg.")

# -------- BESLUTNING 1 --------
print()
print("BESLUTNING 1: Konflikten mellom Silje og Elias.")
print("Silje vil prioritere design, mens Elias vil prioritere sikkerhet og kostnader.")
print("Uenighten har blitt personlig, og begge trekker støtte fra sine nærmeste i teamet.")
print()
print("a) Arrangere et strukturert møte med Silje og Elias")
print("b) Ha individuelle samtaler med hver av dem")

valg1 = input("Hva gjør du? (a/b): ")

if valg1 == "a" or valg1 == "A":
    # alternativ a: felles møte
    print()
    print("Diskusjonen blir intens, men begge får forklare synspuinktene sine.")
    print("Du holder fokus på prosjektets behov, ikke personene.")
    print("De blir enige om hva som er viktigst for portalen.")
    tillit = tillit + 1
elif valg1 == "b" or valg1 == "B":
    # alternativ b: individuelle samtaler
    print()
    print("Du får en bedre forståelse av begge perspektivene.")
    print("Men Silje og Elias har fortsatt ikke snakket sammen, og begge lurer på om du tar parti med den andre.")
else:
    print()
    print("Du nøler og gjør ingenting. Konflikten fortsetter.")

# -------- BESLUTNING 2 --------
print()
print("BESLUTNING 2: Uenigheten mellom Hamdi og Hallgeir")
print("Hamdi vil ha en kontrollert løsning gjennom kommunens plattform.")
print("Hallgeir vil ha et åpent system med rom for spontane innspill.")
print("Uenigheten er fortsatt lavmælt, men frustrasjonen vokser.")
print()
print("a) Arrangere et felles avklaringsmøte nå")
print("b) Avvente og la dem finne en løsning selv")

valg2 = input("Hva gjør du? (a/b): ")

if valg2 == "a" or valg2 == "A":
    # alternativ a: avklaringsmøte (gir 1 tillitspoeng)
    print()
    print("Hamdi og Hallgeir får tydeliggjort behovene sine.")
    print("Dere finner en løsning som kombinerer kontroll og åpenhet.")
    print("Konflikten blir håndtert før den vokser.")
    tillit = tillit + 1
elif valg2 == "b" or valg2 == "B":
    # alternativ b: avvente (gir 0 tillitspoeng)
    print()
    print("Hamdi og Hallgeir får større selvstendighet, men en uke senere jobber de i hver sin retninng og beslutningen om folkemøtene blir utsatt.")
else:
    #ugyldig svar: Erling nøler og gjør ingenting
    print()
    print("Du nøler og gjør ingenting. Uenigheten fortsetter å vokse.")

# -------- BESLUTNING 3 --------
print()
print("BESLUTNING 3: Motivasjonen i teamet")
print("Konfliktene har påvirket stemningen, og fristen nærmer seg.")
print()
print("a) Sette av tid til en teamøkt med relasjonsbygging og felles spilleregler")
print("b) Prioritere fremdrift med tydelige delmål og tett oppfølging")

valg3 = input("Hva gjør du? (a/b): ")

if valg3 == "a" or valg3 == "A":
    # alternativ a: relasjonsbygging (gir 1 tillitspoeng)
    print()
    print("Teamet diskuterer samarbeidet og blir enige om felles spilleregler")
    print("Det blir lettere å være uenig på en konstruktiv måte.")
    print("Dere mister litt tid nå, men samarbeidet går lettere videre.")
    tillit = tillit + 1
elif valg3 == "b" or valg3 == "B":
    # alternativ b: fremdrift (gir 0 tillitspoeng, men lagrer at Erling valgte fremdrift)
    print()
    print("Du setter delmål, fordeler oppgaver og følger opp tett.")
    print("Arbeidet går raskere, men noen føler at konfliktene ikke har blitt tatt på alvor.")
    fremdrift = True
else:
    #ugyldig svar: Erling nøler, og gjør ingenting
    print()
    print("Du nøler og gjør ingenting. Stemingen blir ikke bedre.")

# -------- AVSLUTNING --------
print()
print("=" * 50)
print("HISTORIENS SLUTT")
print("=" * 50)
print("Dine valg:")
print(f"- Valg 1: {valg1}")
print(f"- Valg 2: {valg2}")
print(f"- Valg 3: {valg3}")
print("Tillitspoeng:", tillit, "av 3")
print()

if tillit == 3:
    # utfall 1: Erling valgte samarbeid i alle tre beslutningene
    print("ENDEPUNKT 1: TILLIT OG SAMARBEID")
    print("Teamet gjenoppretter tilliten og går videre til norming-fasen.")
    print("Dere har felles spilleregler, og prototypen blir klar i tide.")
elif tillit == 1 or tillit == 2:
    # utfall 2: en blanding av valg
    print("ENDEPUNKT 2: DDELVIS LØSNING")
    print("Konflikten er delvis løst, men relasjonene er sårbare.")
    print("Prosjektet fortsetter, men teamet trenger oppfølging.")
    if fremdrift == True:
        # ekstra setning hvis Erling prioriterte fremdrift i beslutning 3
        print("Fokuset på fremdrift hold fristen, men på bekostning av teamet.")
else: 
    # utfall 3: Erling tok ingen valg som bygget tillit
    print("ENDEPUNKT 3: SVEKKET SAMHOLD")
    print("Prosjektet mister samhold, og konfliktene har vokst.")
    print("Motivasjonen synker, og prototypen blir ikke klar i tide.")

print()
print("Takk for at du spilte! Kjør spillet på nytt for å se hvordan andre valg påvirker teamet.")
