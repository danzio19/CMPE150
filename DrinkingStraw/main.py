
glass_size = int(input())
straw_pos = int(input())

straw_pos1 = round((straw_pos+0.1)/2)  # divided possible straw positions into categories of 2 (1-2=>1,3,4=>2 and so on)
for img_i in range(glass_size-straw_pos1+2):  # outer for loop for each separate glass
    for i in range(straw_pos):  # straw printed separately from the rest of the glass
        for j in range(i):
            print(' ', end='')
        print('o')
    for row_i in range(glass_size):  # for loop for glass part
        for j in range(row_i):  # spaces and \ is same for every line
            print(' ', end='')
        print('\\', end='')
        if row_i < img_i:  # if this is true, it means that line only has the 'o' part of the straw
            for j in range(straw_pos-1):  # derived equation for no of spaces before 'o'
                print(' ', end='')
            print('o', end='')
            for j in range(2*glass_size-straw_pos-2*row_i):  # derived equation for no of spaces after 'o'
                print(' ', end='')
        else:
            for j in range(2*(glass_size-row_i)):  # else: this means that line should contain stars, derived equation
                print('*', end='')
        print('/', end='')  # end of the line and spaces are the same for each possible line
        for j in range(row_i):
            print(' ', end='')
        print()  # resets the cursor to the new line after each line
    for i in range(glass_size):  # the rest of the cup seperated from the drink part,(spaces)(-- or ||)(spaces)
        print(' ', end='')
    print('--', end='')
    for i in range(glass_size):
        print(' ', end='')
    print()  # resets the cursor to the new line
    for i in range(glass_size):
        for j in range(glass_size):
            print(' ', end='')
        print('||', end='')
        for j in range(glass_size):
            print(' ', end='')
        print()  # resets the cursor to the new line




