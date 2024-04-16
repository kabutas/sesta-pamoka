mix_list = [1, "zodis", 1.7, True, ["a", "b", "c"], {"a": "k", "j": "nieko"}]

# print(*mix_list, sep=" | ")
for i in mix_list:
    print(type(i), i, sep=" | ")
