lake = ["fish", "rocks", "stillwater"]
if len(lake) == 3:
    print("The lake looks perfect, go for a swim!")
fish_in_lake = ["carp", "stout", "salmon"]
for fish in fish_in_lake:
    if fish == "carp":
        print("I can see", len(lake), "elements in the lake:", lake)
    elif fish == "salmon":
        print("There is", lake, "and the fish found are:", fish_in_lake)
    else:
        print("There is a fish called", fish, "in the lake")