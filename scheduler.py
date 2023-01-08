import schedule
import time
from bot import write_message

schedule.every(6).hours.do(write_message, "https://discord.com/channels/611132910992490506/611135278454669332", """<hov> is a Danish guild recruiting to bolster our raiding roster. 
Naxx-25 sub 1 hour
Immortal runs!
https://classic.warcraftlogs.com/reports/L1vDXYZFrqByK34x

<hov> søger friske raiders!
Om os:
Vi er en dansk-talende guild, hvori mange af os har spillet sammen siden starten af classic. Vi er et semi-hardcore guild og regner med at enchants og consumes er i orden på både main og mindst én alt. Vi stræber efter en hyggelig raid-atmosfære, hvor det er muligt at holde fokus når der skal laves progression. Vi har en Discord hvor der ofte sidder folk og hygger, og der er altid nogen klar til at hjælpe med en heroic eller to.

https://classic.warcraftlogs.com/guild/eu/gehennas/hov

Hvad vi forventer fra vores spillere:
- At du er mødestabil
- At du har kendskab til din class, og kan tage imod konstruktiv kritik
- At enchants og consumes er i orden på både main og alt
- At du er forberedt på nyt content, og har læst op på strats på forhånd

Loot: Loot-council

Vi rekrutterer:
- Warlocks
- Rogues
- Death Knights
- Andre gode spillere

Derudover tager vi selvfølgelig altid imod dygtige spillere af alle classes, og socials

Raid-skema:
Onsdag 19:00 - 23:00
Søndag 19:00 - 23:00

Smid @dresdres en besked på discord, eller hop ind på vores discord og tag fat i vores Hovding eller en Hovfficer for en snak.
https://discord.gg/p22cZ7XVsW
""")

while True:
    schedule.run_pending()
    time.sleep(5)