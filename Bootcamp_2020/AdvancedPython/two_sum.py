def two_sum(nu, t):
    """
    Looking for the target between two numbers in 'the list'
    :param nu: list numbers []
    :param t: target or goal
    :return: key:value, and iteration if find result (target - each number) and the iteration it ended up.
    if no result is found,it'll return -1
    """
    d = dict()
    for i in range(len(nu)):
        if t - nu[i] in d:
            print(d)
            return d[t - nu[i]], i
        d[nu[i]] = i
    return -1


my_list = [6, 10, 5, 4, 2]
print(two_sum(my_list, 10))
