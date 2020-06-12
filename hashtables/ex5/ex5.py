# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    cache = {}
    result = []

    for i in files:
        new_i = i.split('/')
        for j in new_i:
            if j not in cache:
                cache[j] = i

    for k, v in cache.items():
        if k in queries:
            result.append(v)

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
