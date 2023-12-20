# This function prompts the user to enter the number of alternatives and market states,
# and then collects user input for each alternative and market state.
# It returns a table containing the user input.
def get_user_input():
    num_alternatives = int(input("Enter the number of alternatives: "))
    num_states = int(input("Enter the number of market states: "))

    table = []
    for i in range(num_alternatives):
        alternative = [input(f"Enter the name of Alternative {i + 1}: ")]
        for j in range(num_states):
            value = input(f"Enter the expected value for Alternative {i + 1} in State {j + 1}: ")
            if value.strip() == "":
                value = 0.0
            else:
                value = float(value.replace('–', '-').replace(',', ''))
            alternative.append(value)
        table.append(alternative)

    return table

def maximax(alternatives):
    max_values = [max(alt[1:]) for alt in alternatives]
    max_index = max_values.index(max(max_values))
    return max_index + 1  

def maximin(alternatives):
    min_values = [min(alt[1:]) for alt in alternatives]
    max_index = min_values.index(max(min_values))
    return max_index + 1

def hurwicz(alternatives, alpha):
    weighted_values = [(alpha * max(alt[1:]) + (1 - alpha) * min(alt[1:])) for alt in alternatives]
    max_index = weighted_values.index(max(weighted_values))
    return max_index + 1

def equally_likely(alternatives):
    avg_values = [sum(alt[1:]) / len(alt[1:]) for alt in alternatives]
    max_index = avg_values.index(max(avg_values))
    return max_index + 1

def minimax_regret(alternatives):
    max_values = [max(alt[1:]) for alt in alternatives]
    regret_table = [[max_value - value for value in alt[1:]] for alt, max_value in zip(alternatives, max_values)]
    max_regrets = [max(regret) for regret in regret_table]
    max_index = max_regrets.index(min(max_regrets))
    return max_index + 1

def main():
    user_table = get_user_input()

    print(f"Maximax choice: Alternative {maximax(user_table)}")
    print(f"Maximin choice: Alternative {maximin(user_table)}")
    alpha = float(input("Enter the coefficient of optimism (alpha) for the Hurwicz criterion: "))
    print(f"Hurwicz choice (alpha={alpha}): Alternative {hurwicz(user_table, alpha)}")
    print(f"Equally likely choice: Alternative {equally_likely(user_table)}")
    print(f"Minimax regret choice: Alternative {minimax_regret(user_table)}")

if __name__ == "__main__":
    main()