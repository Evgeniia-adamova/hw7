take_a_walk_outside = ["forest_trees", "lake", "sky"]
forest_trees = ["pine", "oak", "chestnut", "birch", "aspen"]
for tree in forest_trees:
    if tree == "pine":
        print("take a cone")
    if tree == "chestnut":
        print("we might see a fox today")
    else:
        print(tree + " is a beautiful tree")
if len(forest_trees) == 5:
    print("nature is good")