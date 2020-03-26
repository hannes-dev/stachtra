from sta.models import Achievement

list = [
    ("001", "Complete the Prologue."),
    ("002", "Complete Main Quest \"Aya\"."),
    ("003", "Complete Main Quest \"Pompeius Magnus\"."),
    ("004", "Complete Main Quest \"The Scarab's Lies\"."),
    ("005", "Complete Main Quest \"The Hyena\"."),
    ("006", "Complete Main Quest \"The Crocodile's Jaws\"."),
    ("007", "Complete Main Quest \"The Lizard's Face\"."),
    ("008", "Complete Main Quest \"The Aftermath\"."),
    ("009", "Complete Main Quest Dream Sequence."),
    ("010", "Complete Main Quest \"The Final Weighing\"."),
    ("011", "Complete the last Main Quest."),
    ("024", "Complete Side Quest \"Seven Farmers\"."),
    ("025", "Complete Side Quest \"Lady of Slaughter\"."),
    ("027", "Destroy 100 breakable objects."),
    ("032", "Defeat 8 Ship Captains."),
    ("035", "Use the eagle for a total of 30 minutes."),
    ("036", "Swim for 1500m, ride for 40km and run for 10km."),
    ("041", "Run away from 3 fights with a hippo."),
    ("044", "Use Dawn & Dusk to make time speed forward 30 times."),
    ("056", "Assasinate Tacito, Ptahmose and Ampelius (The Hidden Ones)"),
    ("057", "Complete Side DLC Quests \"Rise of Shaqilat\" and \"Shadows of the Scarab\" (The Hidden Ones)"),
    ("058", "Complete Main DLC Quest \"The Greater Good\" (The Hidden Ones)"),
    ("062", "Defeat Tutankhamun in the Afterlife (The Curse of the Pharaohs)"),
]

for item in list:
    ach = Achievement.objects.get(pk=item[0])
    ach.description = item[1]
    ach.save()