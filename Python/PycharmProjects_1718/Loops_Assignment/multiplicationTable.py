for column in range(1, 11):
    # the integer range for the column of the table
    for row in range(1, 11):
        # the integer range for the row of the table

        mult_num = row * column
        # create the multiplications from the integer range in the multiplication table

        if mult_num < 10:
            space = '  '
            # for spacing purposes of single digit numbers
        elif mult_num < 90:
            space = ' '
            # for spacing purposes of double digit numbers
        print(space + str(mult_num), end=' ')  # or [end = '  '] for a wider looking format
        # for spacing purposes of how far apart each number is and create the format
    print()

# inspiration sourced from: https://stackoverflow.com/questions/20415384/properly-formatted-multiplication-table
    # for how to get the spacing right (also played around a bit too)(weird to see so many different ways to solve this)
# inspiration of format also sourced from previous python programming assignment from another class for similar question