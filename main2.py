def maximax(alternatives):
    # Find the maximum value for each alternative
    max_values = [max(alt[1:]) for alt in alternatives]
    # Find the index of the alternative with the highest maximum value
    max_index = max_values.index(max(max_values))
    # Return the 1-based index of the alternative
    return max_index + 1  


def maximin(alternatives):
    # Find the minimum value for each alternative
    min_values = [min(alt[1:]) for alt in alternatives]
    # Find the index of the alternative with the highest minimum value
    max_index = min_values.index(max(min_values))
    # Return the 1-based index of the alternative
    return max_index + 1


def hurwicz(alternatives, alpha):
    # Calculate the weighted average of the maximum and minimum values for each alternative
    weighted_values = [(alpha * max(alt[1:]) + (1 - alpha) * min(alt[1:])) for alt in alternatives]
    # Find the index of the alternative with the highest weighted average value
    max_index = weighted_values.index(max(weighted_values))
    # Return the 1-based index of the alternative
    return max_index + 1


def equally_likely(alternatives):
    # Calculate the average value for each alternative
    avg_values = [sum(alt[1:]) / len(alt[1:]) for alt in alternatives]
    # Find the index of the alternative with the highest average value
    max_index = avg_values.index(max(avg_values))
    # Return the 1-based index of the alternative
    return max_index + 1