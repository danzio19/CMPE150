
glass_size = int(input())
straw_pos = int(input())



def print_all(glass_size, straw_pos, img_i=0): # outer func for all the cups
    if img_i == glass_size-round((straw_pos+0.1)/2)+2:  # derived equation for how many cups we should print
        return

    def print_line(straw_pos, i=0):  # func for printing the straw line by line i: line index
        if i == straw_pos:  # base condition
            return

        def print_spaces(straw_pos, i, j=0):  # func for printing spaces j:space index
            if j == i:  # base condition
                return
            print(' ', end='')
            print_spaces(straw_pos, i, j+1)  # repeats itself until the base condition is satisfied

        print_spaces(straw_pos, i)  # execution
        print('o')
        print_line(straw_pos, i + 1)  # move on to the next line
    print_line(straw_pos)  # execution

    def print_cup(glass_size, straw_pos, img_i, i=0):  # func for printing the cup part
        if i == glass_size:
            return

        def print_spaces(j=0):  # func for spaces
            if j == i:
                return
            print(' ', end='')
            print_spaces(j + 1)

        print_spaces()
        print('\\', end='')

        if i < img_i:  # if this condition is satisfied, it means this line is empty
            def print_spaces_1(straw_pos, j=0):  # func for spaces before 'o'
                if j == straw_pos - 1:
                    return
                print(' ', end='')
                print_spaces_1(straw_pos, j + 1)
            print_spaces_1(straw_pos)
            print('o', end='')

            def print_spaces_2(straw_pos, i, j=0):  # func for spaces after 'o'
                if j == 2*glass_size - straw_pos - 2*i:  # derived equation for the number of spaces after 'o'
                    return
                print(' ', end='')
                print_spaces_2(straw_pos, i, j + 1)  # repeats itself until the base condition is satisfied
            print_spaces_2(straw_pos, i)  # execution

        else:  # the line is full
            def print_stars(glass_size, i, j=1):  # func for printing stars
                if j == 2 * (glass_size - i) + 1:  # derived equation for the number of stars
                    return
                print('*', end='')
                print_stars(glass_size, i, j + 1)  # repeats itself until enough stars are printed
            print_stars(glass_size, i)
        print('/')
         # move the cursor to the next line

        print_cup(glass_size, straw_pos, img_i, i + 1)  # repeats itself until enough lines are printed

    print_cup(glass_size, straw_pos, img_i)  # execution

    def print_dashed(glass_size):  # func for printing the line with two dashes
        def print_spaces(j=0):
            if j == glass_size:
                return
            print(' ', end='')
            print_spaces(j + 1)
        print_spaces()
        print('--')

    print_dashed(glass_size)

    def print_rest(glass_size,i=0):  # func for printing the stem of the cup
        if i == glass_size:
            return

        def print_spaces(j=0):
            if j == glass_size:
                return
            print(' ', end='')
            print_spaces(j + 1)
        print_spaces()
        print('||')
        print_rest(glass_size, i+1)
    print_rest(glass_size)

    print_all(glass_size, straw_pos, img_i+1)  # repeats itself until enough images are printed img_i: image(cup) index

print_all(glass_size, straw_pos)


