# CurseForge API

The notes I have collected while researching this subject.

### Base URL: https://addons-ecs.forgesvc.net/api/v2

[Jump to bottom](#section-ids)

### Game ids
- World of Warcraft: 1
- Dark and Light: 10
- Dungeons & Dragons Online: 11
- EVE Online: 12
- EverQuest: 13
- Lineage II: 21
- The Lord of the Rings Online: 33
- Star Trek Online: 36
- The Secret World: 64
- StarCraft II: 65
- 9Dragons: 70
- Knight Online: 122
- RuneScape: 162
- Runes of Magic: 335
- Star Wars: The Old Republic: 339
- LOL: 341
- FINAL FANTASY XIV Online: 391
- Guild Wars 2: 412
- Diablo III: Reaper of Souls: 414
- APB: 418
- World of Tanks: 423
- Rift: 424
- Terraria: 431
- Minecraft: 432
- Tropico 4: 438
- Dragon Nest: 441
- Fallout: New Vegas: 447
- Just Cause 2: 448
- The Elder Scrolls V: Skyrim: 449
- Borderlands 2: 452
- WildStar: 454
- The Elder Scrolls Online: 455
- Firefall: 456
- Strife: 457
- Smite: 458
- Hearthstone: 459
- ArcheAge: 460
- Team Fortress 2: 461
- Heroes of the Storm: 462
- Dota 2: 463
- Sid Meier's Civilization V: 464
- Counter-Strike: Global Offensive: 465
- Battlefield 4: 466
- Path of Exile: 467
- DayZ: 468
- Middle-earth: Shadow of Mordor: 469
- Life is Feudal: Your Own: 470
- Warframe: 471
- Borderlands: The Pre-Sequel!: 472
- Evolve: 473
- Company of Heroes 2: 474
- Call of Duty: Black Ops II: 475
- Unturned: 476
- War Thunder: 477
- Arma 3: 478
- XCOM: Enemy Unknown: 479
- Robocraft: 480
- Total War: Rome II: 481
- Payday: The Heist: 482
- Counter-Strike: Source: 483
- Garry's Mod: 484
- Payday 2: 487
- Sid Meier's Civilization: Beyond Earth: 488
- FIFA 15: 489
- Call of Duty: Advanced Warfare: 490
- Dragon Age: Inquisition: 491
- Rust: 492
- Left 4 Dead 2: 493
- Far Cry 4: 495
- Grand Theft Auto V: 496
- The Binding of Isaac: Rebirth: 497
- ArmA II: Operation Arrowhead: 498
- Heroes & Generals: 499
- Mount & Blade: Warband: 500
- This War of Mine: 501
- Counter-Strike Nexon: Zombies: 502
- Cube World: 503
- Euro Truck Simulator 2: 504
- Infinite Crisis: 505
- Insurgency: 506
- Neverwinter: 508
- Titanfall: 509
- The Sims 4: 510
- 7 Days to Die: 540
- BioShock Infinite: 541
- Call of Duty: Black Ops II Zombies: 542
- Call of Duty: Black Ops: 543
- Chivalry: Medieval Warfare: 545
- Crusader Kings II: 547
- Dark Souls: 548
- Dark Souls II: 549
- DC Universe Online: 551
- Defiance: 552
- Distance: 553
- FTL: Faster Than Light: 554
- Goat Simulator: 555
- Grand Theft Auto IV: 556
- GRID 2: 557
- Killing Floor: 559
- Marvel Heroes Omega: 560
- Medieval II: Total War: 561
- Boundless: 562
- PlanetSide 2: 563
- Saints Row: The Third: 564
- Starbound: 566
- Stronghold Kingdoms: 567
- Sunless Sea: 568
- The Binding of Isaac: 569
- Total War: Shogun 2: 570
- Warface: 571
- Wasteland 2: 572
- Just Survive: 604
- Fractured Space: 605
- Brawlhalla: 606
- Grey Goo: 607
- Darkest Dungeon: 608
- Total War: Attila: 609
- Besiege: 610
- Reign Of Kings: 611
- Cities: Skylines: 612
- World of Warships: 613
- Football Manager 2015: 614
- Battlefield Hardline: 615
- Pillars of Eternity: 616
- Magicka: Wizard Wars: 618
- Magicka 2: 620
- The Witcher 3: Wild Hunt: 621
- Clicker Heroes: 622
- ARK: 623
- LEGO Worlds: 625
- Rebuild 3: Gangs of Deadsville: 626
- Galactic Civilizations III: 627
- Killing Floor 2: 628
- AdVenture Capitalist: 629
- Dirty Bomb: 631
- Rocket League: 632
- Trove: 633
- osu!: 634
- Skyforge: 635
- Awesomenauts: 636
- Empyrion: Galactic Survival: 637
- Mad Max: 638
- Metal Gear Solid V: The Phantom Pain: 639
- Tom Clancy's Rainbow Six: Siege: 640
- Star Wars: Battlefront: 641
- Total War: ARENA: 643
- Overwatch: 644
- Battle Battalions: 645
- Fallout 4: 646
- Paladins: 647
- Tom Clancy's The Division: 648
- Paragon: 649
- Stellaris: 650
- Tekken 6: 651
- Street Fighter V: 652
- Dark Souls III: 653
- Total War: WARHAMMER: 654
- Call of Duty: Black Ops III: 655
- FIFA 16: 656
- Pantheon: Rise of the Fallen: 658
- Football Manager 2016: 659
- Doom: 660
- Factorio: 661
- Portal: 662
- Portal 2: 663
- NBA 2K16: 664
- Hearts of Iron IV: 665
- Dead by Daylight: 666
- Tree of Savior: 667
- Europa Universalis IV: 668
- Stardew Valley: 669
- Elite: Dangerous: 670
- ShellShock Live: 671
- Undertale: 672
- Hurtworld: 673
- Don't Starve: 674
- Don't Starve Together: 675
- Sid Meier's Civilization IV: 676
- Sid Meier's Civilization III: 677
- Insanity Clicker: 678
- Remember Me: 679
- Z1 Battle Royale: 680
- Star Citizen: 681
- No Man's Sky: 682
- Call of Duty: Infinite Warfare: 684
- Battlefield 1: 687
- Albion Online: 720
- Battlerite: 721
- FIFA 17: 722
- Breakaway: 724
- Streamline: 725
- Gears of War 4: 726
- Sid Meier's Civilization VI: 727
- Watch Dogs: 728
- Watch Dogs 2: 729
- Shadow Warrior 2: 730
- Mafia III: 731
- Planet Coaster: 732
- Football Manager 2017: 733
- NBA 2K17: 734
- Astroneer: 735
- Kerbal Space Program: 4401
- Tyranny: 4402
- For Honor: 4403
- Disc Jam: 4404
- Anomaly 2: 4405
- Axiom Verge: 4406
- Breach & Clear: 4407
- Broken Age: 4408
- Drawful 2: 4410
- Enter the Gungeon: 4411
- Fibbage: 4412
- Firewatch: 4413
- Heavy Bullets: 4414
- Anomaly: Warzone Earth: 4415
- Hard Reset: 4416
- Kathy Rain: 4417
- Kingdom: New Lands: 4418
- Love: 4419
- Nuclear Throne: 4420
- Okhlos: 4421
- Psychonauts: 4422
- Punch Club: 4423
- Quiplash: 4424
- RunGunJumpGun: 4425
- The Banner Saga: 4427
- The Banner Saga 2: 4428
- The Jackbox Party Pack 2: 4429
- The Jackbox Party Pack 3: 4430
- The Jackbox Party Pack: 4431
- The Wolf Among Us: 4432
- Titan Souls: 4434
- The Walking Dead: 4435
- The Walking Dead: Season Two: 4436
- The Walking Dead: A New Frontier: 4437
- Zombie Night Terror: 4438
- PLAYERUNKNOWN'S BATTLEGROUNDS: 4439
- BATMAN - The Telltale Series: 4440
- Clustertruck: 4441
- Candle: 4442
- 1979 Revolution: 4444
- MXM: 4445
- NieR Automata: 4446
- Mass Effect: Andromeda: 4447
- Black Desert Online: 4448
- Magic: The Gathering: 4449
- Friday the 13th: The Game: 4450
- Dreadnought: 4451
- Gwent: The Witcher Card Game: 4452
- Tekken 7: 4453
- Secret World Legends: 4455
- Ultimate Chicken Horse: 4456
- Fortnite: 4457
- LawBreakers: 4459
- Subnautica: 4482
- Gigantic: 4507
- RimWorld: 4588
- Final Fantasy XV: 4593
- Destiny 2: 4627
- Grim Dawn: 4675
- Space Engineers: 4892
- Divinity: Original Sin: 4907
- Divinity: Original Sin II: 4915
- Monopoly: 6170
- BattleTech: 6222
- My Time at Portia: 6647
- Kenshi: 6820
- Middle-earth: Shadow of War: 6943
- Big Pharma: 6999
- Call of Duty: WWII: 7263
- Dr. Mario: 8104
- Assassin's Creed Origins: 11905
- Wolfenstein II: The New Colossus: 12135
- The Evil Within 2: 12439
- Rend: 12471
- WarGroove: 14331
- Total War: Warhammer II: 15600
- Staxel: 18237
- Far Cry 5: 20925
- Frostpunk: 22191
- South Park: The Fractured But Whole: 53721
- ELEX: 53750
- Star Wars Battlefront II: 54782
- Anno 1800: 58208
- Warhammer: Vermintide 2: 58234
- Surviving Mars: 61489
- Farming Simulator 19: 64244
- Fallout 76: 65814
- Satisfactory: 66022
- Minecraft Dungeons: 69271
- Among Us: 69761
- Chronicles of Arcadia: 70667

### Section ids
Anything missing does not have specific sections

[Jump to bottom](#sort-types)

> World of Warcraft

- Addons: 1

> The Secret World

- Mods: 14

> Runes of Magic

- Addons: 4571

> World of Tanks

- Skins: 9
- Mods: 8

> Rift

- Addons: 4564

> Minecraft

- Resource Packs: 12
- Modpacks: 4471
- Mods: 6
- Worlds: 17

> The Elder Scrolls V: Skyrim

- Mods: 7

> WildStar

- Addons: 18

> The Elder Scrolls Online

- Addons: 19

> Darkest Dungeon

- Mods: 4613

> Stardew Valley

- Mods: 4643

> Sid Meier's Civilization VI

- Mods: 4852

> Kerbal Space Program

- Mods: 4470
- Missions: 4660

> Secret World Legends

- Mods: 4592

> Staxel

- Mods: 4633

> Surviving Mars

- Mods: 4662

> Satisfactory

- Mods: 4801

> Minecraft Dungeons

- Mods: 4944

> Chronicles of Arcadia

- Addons: 4783

### Sort types
- Featured: 0
- Popularity: 1
- Last Update: 2
- Name: 3
- Author: 4
- Total Downloads: 5

### Get addon info
``GET /addon/:addon_id``
> Returns an Addon object

### Get multiple addons
``POST /addon``
> Returns an array of Addon objects

**Body**:

``[:addon_id, :addon_id, ...]``

### Search addons
``GET /addon/search``
> Returns an array of Addon objects matching the query

**Parameters**:

int ``gameId`` (**Required**)
> Searches for addons with the specified [game id](#game-ids)

int ``sectionId`` (**Required**)
> Searches for addons within this [section](#section-ids)

int ``categoryId``
> Refers to the category of mods to search for

string ``gameVersion``
> The game version to use; for Minecraft, use "1.x.x" eg "1.12.2"

int ``index``
> The page index to use

int ``pageSize``
> The total amount of results to display per-page

string ``searchFilter``
> Filters addons based on this string

int ``sort``
> Sorts the results based on the [provided integer](#sort-types)

### Get addon description
``GET /addon/:addon_id/description``
> Returns the specified Addon's description, in html-compatible format

### Get addon file information
``GET /addon/:addon_id/file/:file_id``
> Returns the File object for the specified Addon ID and File ID. File IDs can be obtained from the Addon object.

### Get addon file changelog
``GET /addon/:addon_id/file/:file_id/changelog``
> Returns the changelog for the specified Addon's file, in html-compatible format. File IDs can be obtained from the Addon object.

### Get addon file download url
``GET /addon/:addon_id/file/:file_id/download-url``
> Returns the direct download URL for the specified Addon ID and File ID.
> 
> Note: The content-type header returns ``application/json``, however it is just a URL.

### Get addon files
``GET /addon/:addon_id/files``
> Returns an array of File objects for the specified Addon.

### Get featured addons
``POST /addon/featured``
> Returns an array of featured Addons.

**Body**:

int ``gameId``
> The Game ID.

array[int] ``addonIds``
> An array of Addon IDs to filter.

int ``featuredCount``
> unsure

int ``popularCount``
> unsure

int ``updatedCount``
> unsure

### Get addons database timestamp
``GET /addon/timestamp``
> not sure what this means, might be last-uploaded?

### Get addon by fingerprint
``POST /fingerprint``
> Returns an Addon by its ``packageFingerprint``

**Body**:
``[:fingerprint, ...]``

> Note: unsure if multiple fingerprints are acceptable

### Get minecraft version timestamp
``GET /minecraft/version/timestamp``
> not sure what this means, possibly last minecraft version update

### Get minecraft version list
``GET /minecraft/version``
> Returns a list of Version objects for minecraft versions on CurseForge

### Get minecraft version info
``GET /minecraft/version/:version``
> Returns a Version object for the specified ``:version``, eg ``1.12.2``.