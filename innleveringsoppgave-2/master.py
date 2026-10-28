# IS-118 Gruppeinnlevering 2 - Gruppe 14
# Et spill der spilleren tar tre valg som avgjør om teamet kommer seg gjennom storming-fasen. 

# -------- BESLUTNING 1 --------

tillit = 0       # tillitspoeng, øker når Erling bygger tillit
fremdrift = False   # blir True hvis Erling prioriterer leveransen

print("=" * 50)
print("Erlings valg")
print("=" * 50)
print("Du er Erling, prosjektleder for kommunens nye medborgerportal.")
print("Det har gått seks uker, og teamer er i storming-fasen.")
print("Silje og Elias er uenige om teknologi og design.")
print("Hamdi og Hallgeir er uenige om digitale folkemøter.")
print("Første prototype skal være klar om tre uker.")
print()
print("BESLUTNING 1: Konflikten mellom Silje og Elias.")
print("Uenigheten om teknologi og design har blitt personlig.")
print("Begge trekker støtte fra sine nærmeste i teamet.")
print()
print("a) Arrangere et strukturert møte med Silje og Elias")
print("b) Ha individuelle samtaler med hver av dem")

valg1 = input("Hva gjør du? (a/b): ")

if valg1 == "a" or valg1 == "A":
    # det som skjer hvis spilleren valgte "a"
    print()
    print("Silje og Elias får begge forklare synspunktene sine.")
    print("Du holder diskusjonen på prosjektets behov, ikke personene.")
    print("De blir enige om hva som er viktigst for portalen.")
    tillit = tillit + 1
else: 
    # det som skjer hvis spilleren valgte "b"
    print()
    print("Samtalene demper temperaturen, og du forstår konflikten bedre.")
    print("Men Silje og Elias har fortsatt ikke snakket sammen, og begge lurer på om du tar parti med den andre.")

# -------- BESLUTNING 2 --------
print()
print("BESLUTNING 2: Uenigheten mellom Hamdi og Hallgeir")
print("Hamdi vil ha en kontrollert løsning gjennom kommunens plattform.")
print("Hallgeir vil ha et åpent system med rom for spontane innspill.")
print("Uenigheten er fortsatt lavmælt, men frustrasjonen vokser.")
print()
print("a) Arrangere et felles avklaringsmøte nå")
print("b) Avvente og la dem finne en lløsning selv")

valg2 = input ("Hva gjør du? (a/b): ")

if valg2 == "a" or valg2 == "A":
    # det som skjer hvis spilleren valgte "a"
    print()
    print("Hamdi og Hallgeir får tydeliggjort behovene sine.")
    print("Dere finner en løsning som kombinerer kontroll og åpenhet.")
    print("Konflikten blir håndtert før den vokser.")
    tillit = tillit + 1
else:
    # det som skjer hvis spilleren valgte "b"
    print()
    print("Du bruker tiden på fremdrift i stedet.")
    print("Men en uke senere har Hamdi og Hallgeir begynt å jobbe i hver sin retning.")
    print("og beslutningen om folkemøtene blir utsatt.")

# -------- BESLUTNING 3 --------
print()
print("BESLUTNING 3: Motivasjonen i teamet")
print("Konfliktene har påvirket stemningen, og fristen nærmer seg.")
print()
print("a) Sette av tid til en teamøkt med relasjonsbygging og felles spilleregler")
print("b) Prioritere fremdrift med tydelige delmål og tett oppfølging")

valg3 = input("Hva gjør du? (a/b): ")

if valg3 == "a" or valg3 == "A":
    # det som skjer hvis spilleren valgte "a"
    print()
    print("Teamet diskuterer samarbeidet og blir enige om felles spilleregler.")
    print("Det blir lettere å være uenig på en konstruktiv måte.")
    print("Dere mister litt tid nå, men samarbeidet går lettere videre.")
    tillit = tillit + 1
else:
    # det som skjer hvis spilleren valgte "b"
    print()
    print("Du setter delmål, fordeler oppgaver og følger opp tett.")
    print("Arbeidet går raskere, men de underliggende konfliktene ligger der fortsatt.")
    fremdrift = True

# -------- AVSLUTNING --------
print()
print("=" * 50)
print("RESULTAT")
print("=" * 50)
print("Dine valg:", valg1, "-", valg2, "-", valg3)
print("Tillitspoeng:", tillit, "av 3")
print()

if tillit >= 2:
    # utfall 1: 2 eller 3 tillitspoeng
    print("UTFALL 1: Teamet går videre til norming.fasen.")
    print("Tilliten er gjenopprettet, og prototypen leveres som planlagt.")
elif tillit == 1:
    # utfall 2: 1 tillitspoeng
    print("UTFALL 2: Konflikten er delvis løst.")
    print("Prototypen blir ferdig, men relasjonene er fortsatt sårbare.")
    if fremdrift == True:
        print("Fokuset på fremdrift holdt fristen, men på bekostning av teamet.")
else:
        # utfall 3: 0 tillitspoeng
        print("UTFALL 3: Prosjektet mister samhold og forsinkes.")
        print("Konfliktene har vokst, og prototypen blir ikke klar i tide.")

print()
print("Takk for at du spilte! Dette spillet er laget av gruppe 14.")
