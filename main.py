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


# This function displays the table of alternatives and market states.
def display_table(table):
    print("\nSTATE OF NATURE")
    print("{:<20}".format("ALTERNATIVE"), end="")
    for i in range(1, len(table[0])):
        print("{:<20}".format(f"STATE {i}"), end="")
    print()

    for row in table:
        for value in row:
            print("{:<20}".format(str(value)), end="")
        print()


# The main function calls the get_user_input function to collect user input,
# and then calls the display_table function to display the table.
def main():
    user_table = get_user_input()
    display_table(user_table)


if __name__ == "__main__":
    main()