

def get_languages(tree, root, chars, languages):
    a, b, c, d = tree[root]
    if a:
        languages.append(b)
    else:
        get_languages(tree, c, chars, languages)
        if b not in chars:
            get_languages(tree, d, chars, languages)

def replace_language_names(tree, language_map, root):
    a, b, c, d = tree[root]
    if a:
        tree[root] = (a, language_map[b], c, d)
    else:
        replace_language_names(tree, language_map, c)
        replace_language_names(tree, language_map, d)

def main():
    inp = [int(x) for x in input().split(" ")]
    n, p = inp[0], inp[1]
    not_roots = set()
    possible_roots = set()
    tree = []
    all_languages = []
    for i in range(n):
        inp = input().split(" ")
        for j in range(int(inp[1]) - len(tree) + 1):
            tree.append(None)
        if inp[0] == "I":
            not_roots.add(int(inp[3]))
            not_roots.add(int(inp[4]))
            possible_roots.add(int(inp[1]))
            tree[int(inp[1])] = (False, ord(inp[2]), int(inp[3]), int(inp[4]))
        else:
            tree[int(inp[1])] = (True, inp[2], None, None)
            all_languages.append(inp[2])
    all_languages = sorted(all_languages)
    language_map = {language: i for i, language in enumerate(all_languages)}
    for el in possible_roots.difference(not_roots):
        root = el
    # print(tree)
    replace_language_names(tree, language_map, root)
    # print(tree)
    # print(language_map)
    # print(all_languages)
    # print()
    for i in range(p):
        chars = {ord(x) for x in set(input())}
        languages = []
        get_languages(tree, root, chars, languages)
        languages = sorted(languages)
        print(" ".join([all_languages[x] for x in languages]))


if __name__ == '__main__':
    main()
