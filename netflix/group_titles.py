'''
    Question: Given an array of titles, find similar titles

    Answer:
    What we want to do is to find the occurance of every character in the title
    load it into the hashmap and compare the other titles. If there is a similar title,
    we add that to a specific key in the hashmap. In the end, we will return the array of
    grouped titles by accessing the values of our hashmap

    Complexity:
        let n be the size of the list of strings, and k be the maximum length that a single string can have
        Time: O(NxK) -> we are counting each letter for each string in a list, including the string's max length

        Space: O(NxK) -> We are storing the list of size n and the size of the string itself can be k.
'''


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
