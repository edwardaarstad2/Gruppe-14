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