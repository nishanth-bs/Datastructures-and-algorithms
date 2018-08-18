def distance(a,b):
    def compute_distance_between_prefixes(a_idx, b_idx):
        if a_idx < 0:
            return b_idx + 1
        elif b_idx < 0:
            return a_idx + 1
        if distance_bn_prefixes[a_idx][b_idx] == -1:
            if a[a_idx] == b[b_idx]:
                distance_bn_prefixes[a_idx][b_idx] = (compute_distance_between_prefixes(a_idx-1,b_idx-1)
                                                      )
            else:
                substitute_last = compute_distance_between_prefixes(a_idx -1 , b_idx -1)
                add_last = compute_distance_between_prefixes(a_idx -1 , b_idx)
                delete_last = compute_distance_between_prefixes(a_idx, b_idx -1)
                distance_bn_prefixes[a_idx][b_idx] = 1+ min(substitute_last,
                                                            add_last, delete_last)
        return distance_bn_prefixes[a_idx][b_idx]
    distance_bn_prefixes = [[-1]  * len(b) for _ in a]
    return compute_distance_between_prefixes(len(a) -1, len(b) -1)

print(distance(list('Orchestra'),list('Carthorse')))
