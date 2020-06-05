def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    if length == 1:
        return None

    elif length == 2:
        first_num = weights[0]
        second_num = weights[1]
        if first_num + second_num == limit:
            return [1, 0]
        else:
            return None
        
    else:
        cache = {}
        answer = []

        for i in range(0, length):
            cache[weights[i]] = i

        for k, v in cache.items():
            if limit - k in cache.keys():
                answer.append(v)
        return sorted(answer, reverse=True)
