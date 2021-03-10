def group_titles(titles):
    result = {}

    for title in titles:
        count = [0] * 26
        for character in title:
            index = ord(character) - ord('a')
            count[index] += 1
        key = tuple(count)
        if key in result:
            result[key].append(title)
        else:
            result[key] = [title]
    return result.values()


if __name__ == "__main__":
    titles = ["duel", "dule", "speed", "spede", "deul", "cars"]
    titlesObject = list(group_titles(titles))
    query = "dule"

    # Searching for all titles
    for title in titlesObject:
        if query in title:
            print(title)
