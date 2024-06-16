[sel YESNO_SEL top]
[f 0 5 65278][f 2 1]Yes[e]
[f 0 5 65278][f 2 1]No[e]

[msg GET_ITEM_MES]
[f 0 5 65278][f 2 1]I obtained [f 2 5 3 65535 0].[n][f 1 1][e]

[msg GET_MONEY_MES]
[f 0 5 65278][f 2 1]I obtained [f 2 4 0] yen.[n][f 1 1][e]

[msg TBOX_ENEMY_APPEAR]
[f 0 5 65278][f 2 1]Look out![n][f 1 1][e]

[msg NOT_OPEN_SHORTCUT]
[f 0 5 65278][f 2 1]We can't go through...[n][f 1 1][e]

[msg OPENED_BOX]
[f 0 5 65278][f 2 1][f 6 1 3 0 0 9]There's nothing else here...[n][f 1 1][e]

[msg EXIT_DUNGEON_SEL]
[f 0 5 65278][f 2 1]Should I drop out of this movie?[n][f 1 1][e]

[msg SHORTCUT_ASK]
[f 0 5 65278][f 2 1]There's a hidden passage...[n][f 1 1][e]

[sel SEL_SHORTCUT_ASK top]
[f 0 5 65278][f 2 1]Use[e]
[f 0 5 65278][f 2 1]Don't use[e]

[msg ONEWAY_ASK]
[f 0 5 65278][f 2 1]This shortcut looks like it only goes one[n]way; I can go through, [f 0 1 2]but I won't be[n]able to come back from the other side...[n][f 1 1][e]

[sel SEL_ONEWAY_ASK top]
[f 0 5 65278][f 2 1]Use[e]
[f 0 5 65278][f 2 1]Don't use[e]

[msg BAG_FULL]
[f 0 5 65278][f 2 1][f 6 1 3 0 0 9]It looks like my bag is full...[n][f 1 1][e]

[msg GATHER_SUSPENSE]
[f 0 5 65278][f 2 1]I searched the Treasure Spot...[n][f 1 1][e]
[f 0 5 65278][f 2 1]...?[n][f 1 1][e]

[sel JIJIKU_SEL top]
[f 0 5 65278][f 2 1]Save[e]
[f 0 5 65278][f 2 1]Leave the labyrinth[e]
[f 0 5 65278][f 2 1]Cancel[e]

[msg JIJIKU_ASK]
[f 0 5 65278][f 2 1]What should I do?[n][f 1 1][e]

[msg FIND_QUEST_TEST]
[f 0 5 65278][f 2 1]Perhaps we should return to[n]the theater and check the[n]status of the quest...[n][f 1 1][e]

[sel SEL_QUEST_ESCAPE_TEST top]
[f 0 5 65278][f 2 1]Return to the theater[e]
[f 0 5 65278][f 2 1]Proceed forward[e]

[msg ALERT_MSG]
[f 0 5 65278][f 2 1]This leads outside of the special screening.[n]What should I do?[n][f 1 1][e]

[sel SEL_ALERT_MSG top]
[f 0 5 65278][f 2 1]Return to the theater[e]
[f 0 5 65278][f 2 1]Continue exploring[e]

[msg MAPPING_FAILED_MSG]
[f 0 5 65278][f 2 1][f 3 1 1 0 0 0]The treasure chest map is[n]emitting a mysterious glow![n][f 1 3 65535][f 1 1][e]
[f 0 5 65278][f 2 1][f 3 1 1 0 0 0]It seems to be indicating locations[n]that haven't been visited...[n][f 1 3 65535][f 1 1][e]

[sel POWER_SPOT_SEL top]
[f 0 5 65278][f 2 1]Search cautiously[e]
[f 0 5 65278][f 2 1]Search thoroughly[e]
[f 0 5 65278][f 2 1]Cancel[e]

[msg USE_AUTO_RECOVER_ASK]
[f 0 5 65278][f 2 1]Should I use auto-recovery?[n][f 1 1][e]

[sel AUTO_RECOVER_SEL top]
[f 0 5 65278][f 2 1]Use[e]
[f 0 5 65278][f 2 1]Do not use[e]

[msg AUTO_RECOVER_NOT_USE_MSG]
[f 0 5 65278][f 2 1]Maybe not.[n][f 1 1][e]

[msg AUTO_RECOVER_NOT_USE_MSG_2]
[f 0 5 65278][f 2 1]Nobody needs healing.[n][f 1 1][e]

[msg AUTO_RECOVER_NOT_USE_MSG_3]
[f 0 5 65278][f 2 1]There's not enough SP to use the[n]recovery skill.[n][f 1 1][e]

[msg AUTO_RECOVER_NOT_USE_MSG_4]
[f 0 5 65278][f 2 1]Nobody in the party can use[n]a recovery skill.[n][f 1 1][e]

[msg MSG_TUTORIAL_OTAKARA_GET]
[f 0 5 65278][f 2 1]> Treasure Spot event[n][f 1 1][e]

[msg MSG_TUTORIAL_POWERSPOT_1]
[f 0 5 65278][f 2 1]"Treasure Spots" are where you[n]may obtain [f 0 1 2]various items[f 0 1 0].[n][f 1 1][e]

[msg MSG_TUTORIAL_POWERSPOT_2]
[f 0 5 65278][f 2 1]If you choose to [f 0 1 2]Search thoroughly[f 0 1 0]...[n][f 1 1][e]
[f 0 5 65278][f 2 1][f 3 1 1 0 0 0]Then you may find [f 0 1 2]up to 5[f 0 1 0] items,[n]with a greater chance they'll be rare.[n][f 1 1][e]
[f 0 5 65278][f 2 1][f 3 1 1 0 0 0]However, you also have a greater[n]chance of triggering a battle.[n][f 1 1][e]

[msg MSG_TUTORIAL_POWERSPOT_3]
[f 0 5 65278][f 2 1]If you choose to [f 0 1 2]Search cautiously[f 0 1 0]...[n][f 1 1][e]
[f 0 5 65278][f 2 1][f 3 1 1 0 0 0]Then you may find [f 0 1 2]up to 3[f 0 1 0] items,[n]while enjoying a low risk of battle.[n][f 1 1][e]

[msg MSG_TUTORIAL_POWERSPOT_4]
[f 0 5 65278][f 2 1]There's a limited number of items in[n]each Treasure Spot, but if you [f 0 1 2]leave[n]the labyrinth[f 0 1 0], certain spots will be[n]replenished, and you can search[n]them again. Take advantage of this,[n]and you'll end up richer than a king![n][f 1 1][e]

[msg MSG_TUTORIAL_OTAKARA_GET_2]
[f 0 5 65278][f 2 1][f 3 1 1 0 0 0]> Got goods! event[n][f 1 3 65535][f 1 1][e]
[f 0 5 65278][f 2 1][f 3 1 1 0 0 0]> But let's be careful of the[n]enemy event[n][f 1 3 65535][f 1 1][e]

[msg MSG_TUTORIAL_OTAKARA_BAG]
[f 0 5 65278][f 2 1]> Inventory full event[n][f 1 1][e]

[msg MSG_TUTORIAL_QUEST_MAP_0]
[f 0 5 65278][f 2 1]If you enter a labyrinth during a[n]special screening, [f 0 1 2]some paths will[n]be inaccessible[f 0 1 0]. There might be[n]other changes as well.[n][f 1 1][e]
[f 0 5 65278][f 2 1][f 0 1 2]The map may show some differences[n]in the floor's layout.[f 0 1 0].[n][f 1 1][e]

[msg MSG_TUTORIAL_QUEST_MAP_1]
[f 0 5 65278][f 2 1]Inaccessible areas will be [f 0 1 2]colored[n]red[f 0 1 0] and [f 0 1 2]marked with a special icon[f 0 1 0][n]on the lower screen.[n][f 1 1][e]
[f 0 5 65278][f 2 1]Keep an eye on the lower screen and[n]stay alert when exploring labyrinths[n]during special screenings.[n][f 1 1][e]

[msg MSG_TUTORIAL_QUEST_MAP_2]
[f 0 5 65278][f 2 1]Also, a [f 0 1 2]special screening palette[f 0 1 0][n]will appear on the lower screen.[n][f 1 1][e]
[f 0 5 65278][f 2 1]Icons from this palette [f 0 1 2]can only be[n]placed during a special screening[f 0 1 0].[n][f 1 1][e]
[f 0 5 65278][f 2 1]Use these to mark events that only       [n]occur during special screenings.       [n][f 1 1][e]
[f 0 5 65278][f 2 1]Make use of the palette and strive[n]to complete the quest.[n][f 1 1][e]

[msg MSG_TUTORIAL_QUEST_TREAS]
[f 0 5 65278][f 2 1]Special screenings have their own[n][f 0 1 2]treasure chests not found elsewhere[f 0 1 0].[n][f 1 1][e]
[f 0 5 65278][f 2 1]These contain items that will come[n]in handy, so don't miss them![n][f 1 1][e]

[msg MSG_FUTABA_IP_BTL_MSG_1]
[f 0 5 65278][f 2 1][f 3 1 1 0 0 26384]It's the Reaper... This one's[n]gonna be tough![n][f 1 6 65535][e]

[msg MSG_FUTABA_IP_BTL_MSG_2]
[f 0 5 65278][f 2 1][f 3 1 1 0 0 26385]I know this feeling... It's the[n]Reaper![n][f 1 6 65535][e]

[msg MSG_FUTABA_IP_BTL_MSG_3]
[f 0 5 65278][f 2 1][f 3 1 1 0 0 26386]Tough one on the way![n]Get ready! [n][f 1 6 65535][e]

[msg MSG_FUKA_IP_BTL_MSG_1]
[f 0 5 65278][f 2 1][f 3 1 1 0 0 14384]I'm picking up a signal... Look out,[n]it's the Reaper![n][f 1 6 65535][e]

[msg MSG_FUKA_IP_BTL_MSG_2]
[f 0 5 65278][f 2 1][f 3 1 1 0 0 14385]The Reaper is closing in on you![n]Please, stay on your guard![n][f 1 6 65535][e]

[msg MSG_FUKA_IP_BTL_MSG_3]
[f 0 5 65278][f 2 1][f 3 1 1 0 0 14386]Hm, according to my readings...[n]...Oh no! There's a Reaper![n][f 1 6 65535][e]

[msg MSG_RISE_IP_BTL_MSG_1]
[f 0 5 65278][f 2 1][f 3 1 1 0 0 6384]Uh oh, I'm picking up a Reaper nearby![n]Watch out![n][f 1 6 65535][e]

[msg MSG_RISE_IP_BTL_MSG_2]
[f 0 5 65278][f 2 1][f 3 1 1 0 0 6385]I sense The Reaper![n]Stay on your guard![n][f 1 6 65535][e]

[msg MSG_RISE_IP_BTL_MSG_3]
[f 0 5 65278][f 2 1][f 3 1 1 0 0 6386]Picking up a signal from the Reaper![n]It's coming this way![n][f 1 6 65535][e]

[msg MSG_JUSTINE_IP_BTL_MSG_1]
[f 0 5 65278][f 2 1][f 3 1 1 0 0 59384]The Reaper approaches. Please be[n]careful.[n][f 1 6 65535][e]

[msg MSG_JUSTINE_IP_BTL_MSG_2]
[f 0 5 65278][f 2 1][f 3 1 1 0 0 59385]Please take care, for there's a Reaper[n]afoot.[n][f 1 6 65535][e]

[msg MSG_JUSTINE_IP_BTL_MSG_3]
[f 0 5 65278][f 2 1][f 3 1 1 0 0 59386]It's the Reaper... Your only chance is to[n]maintain focus.[n][f 1 6 65535][e]

[msg MSG_CAROLIN_IP_BTL_MSG_1]
[f 0 5 65278][f 2 1][f 3 1 1 0 0 58384]The Reaper is near![n][f 1 6 65535][e]

[msg MSG_CAROLIN_IP_BTL_MSG_2]
[f 0 5 65278][f 2 1][f 3 1 1 0 0 58385]Incoming Reaper![n][f 1 6 65535][e]

[msg MSG_CAROLIN_IP_BTL_MSG_3]
[f 0 5 65278][f 2 1][f 3 1 1 0 0 58386]I know this sound, it's the Reaper![n][f 1 6 65535][e]

[msg MSG_ELIZABETH_IP_BTL_MSG]
[f 0 5 65278][f 2 1][f 3 1 1 0 0 54384]A Reaper makes its grand entrance![n][f 1 6 65535][e]

[msg MSG_ELIZABETH_IP_BTL_MSG_2]
[f 0 5 65278][f 2 1][f 3 1 1 0 0 54385]With my incredible ears, I can hear the[n]Reaper calling.[n][f 1 6 65535][e]

[msg MSG_ELIZABETH_IP_BTL_MSG_3]
[f 0 5 65278][f 2 1][f 3 1 1 0 0 54386]That sound... It can only be a Reaper.[n][f 1 6 65535][e]

[msg MSG_THEODOR_IP_BTL_MSG_1]
[f 0 5 65278][f 2 1][f 3 1 1 0 0 56384]I wish this wasn't true, but there's a[n]Reaper coming![n][f 1 6 65535][e]

[msg MSG_THEODOR_IP_BTL_MSG_2]
[f 0 5 65278][f 2 1][f 3 1 1 0 0 56385]Incoming Reaper. Please take care![n][f 1 6 65535][e]

[msg MSG_THEODOR_IP_BTL_MSG_3]
[f 0 5 65278][f 2 1][f 3 1 1 0 0 56386]I'm sensing something, and it's most[n]certainly a Reaper![n][f 1 6 65535][e]

[msg MSG_MARGARET_IP_BTL_MSG_]
[f 0 5 65278][f 2 1][f 3 1 1 0 0 55384]The Reaper is here! Stay on guard![n][f 1 6 65535][e]

[msg MSG_MARGARET_IP_BTL_MSG__2]
[f 0 5 65278][f 2 1][f 3 1 1 0 0 55385]Remain alert. A powerful enemy is[n]approaching.[n][f 1 6 65535][e]

[msg MSG_MARGARET_IP_BTL_MSG__3]
[f 0 5 65278][f 2 1][f 3 1 1 0 0 55386]The Reaper is close. Stay vigilant.[n][f 1 6 65535][e]

[msg MSG_NANAKO_IP_BTL_MSG_1]
[f 0 5 65278][f 2 1][f 3 1 1 0 0 57384]The Reaper! That's what it is![n][f 1 6 65535][e]

[msg MSG_NANAKO_IP_BTL_MSG_2]
[f 0 5 65278][f 2 1][f 3 1 1 0 0 57385]A Reaper is coming![n][f 1 6 65535][e]

[msg MSG_NANAKO_IP_BTL_MSG_3]
[f 0 5 65278][f 2 1][f 3 1 1 0 0 57386]No! The Reaper is coming fast![n][f 1 6 65535][e]

[msg MSG_foe_exist_move_short [Futaba]]
[f 0 5 65278][f 2 1][f 4 6 26 10 100 0][f 3 1 1 0 0 26554]H-Hey! There's an FOE on the[n]other side of that shortcut![n][f 1 1][e]
[f 0 5 65278][f 2 1]Don't go through there![n][f 1 1][e]

[msg MSG_foe_exist_move_short_2 [Futaba]]
[f 0 5 65278][f 2 1][f 4 6 26 10 0 0][f 3 1 1 0 0 26054]H-Hey! There's an FOE on the[n]other side of that shortcut![n][f 1 1][e]
[f 0 5 65278][f 2 1]Don't go through there![n][f 1 1][e]

[msg MSG_foe_exist_move_short_3 [Rise]]
[f 0 5 65278][f 2 1][f 4 6 6 10 100 0][f 3 1 1 0 0 6556]Wait! There's an FOE on the[n]other side![n][f 1 1][e]
[f 0 5 65278][f 2 1]I wouldn't go through there[n]just now![n][f 1 1][e]

[msg MSG_foe_exist_move_short_4 [Fuuka]]
[f 0 5 65278][f 2 1][f 4 6 14 10 100 0][f 3 1 1 0 0 14557]Hold on, please! There's an[n]FOE through there![n][f 1 1][e]
[f 0 5 65278][f 2 1]Let's wait until it leaves before[n]going further.[n][f 1 1][e]

[msg MSG_GET_TRESURE_MAP]
[f 0 5 65278][f 2 1]The [f 0 1 2]location of the treasure[f 0 1 0] hidden in[n]this movie has been marked on the map.[n][f 1 1][e]

