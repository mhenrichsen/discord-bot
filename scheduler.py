import schedule
import time
from bot import write_message

schedule.every().minute.do(write_message, "https://discord.com/channels/840898407022460948/844470172001894400", """**<Animal Prison> is recruiting! INTERESTED IN PLAYERS FOR WOTLK** 

Here is why you should join us: 
```diff
+ Currently progessing in SWP (lots of fun!)
+ Hyjal 5/5, BT 9/9 - First week
+ Gruul/Kara cleared first week, Mag second!
+ SSC 6/6, TK 4/4 (pre-nerf ofc). Clearing all in 1 night + Gruul/Mag
+ We got Bob Ross. Shit hunter but good painter
+ We have more fun
+ We have our own special wheelchair system. Do something retarded in raid and get a wheelchair appended to your Discord name! [Patent Pending]
+ Transparent and easy to understand loot system
```
We need you (if you are not mentally challenged and play one of the following classes): 
```fix
∞x ANY PLAYER/CLASS FOR WOTLK
1x Warlock
1x Resto shaman
1x Resto druid
1x Boomkin
1x Shadow Priest
1x Arms Warrior
∞x Good players of any class feel free to reach out
```
Raid times:
```diff
- Wednesday 19:30-23
- Sunday 19:30-23
```
We do our best to have as much fun as possible while clearing all content fast and efficient. We expect our raiders to come with all consums and overall prepared for our raids.

Please join our discord or reach out to me or @Knagg  for more information! https://discord.gg/aNVNgtzBGp
""")

while True:
    schedule.run_pending()
    time.sleep(60)