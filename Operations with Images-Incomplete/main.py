
# return img, nested list
def read_ppm_file(f):
    fp = open(f)
    fp.readline()  # reads P3 (assume it is P3 file)
    lst = fp.read().split()
    n = 0
    n_cols = int(lst[n])
    n += 1
    n_rows = int(lst[n])
    n += 1
    max_color_value = int(lst[n])
    n += 1
    img = []
    for r in range(n_rows):
        img_row = []
        for c in range(n_cols):
            pixel_col = []
            for i in range(3):
                pixel_col.append(int(lst[n]))
                n += 1
            img_row.append(pixel_col)
        img.append(img_row)
    fp.close()
    return img, max_color_value


# Works
def img_printer(img):
    row = len(img)
    col = len(img[0])
    cha = len(img[0][0])
    for i in range(row):
        for j in range(col):
            for k in range(cha):
                print(img[i][j][k], end=" ")
            print("\t|", end=" ")
        print()


filename = input()
operation = int(input())


img, max_color_value = read_ppm_file(filename)  # useful assignment

if operation == 1:

    minimum = int(input())  # take inputs
    maximum = int(input())

    new_img = []  # output image
    for row in img:  # for every value in every pixel in every row
        new_row = []  # create a new list and append all the adjusted values to those lists
        for pxl in row:
            new_pxl = []
            for val in pxl:
                new_val = f'{((val - 0)/(max_color_value - 0) * (maximum - minimum) + minimum):{3}.{4}}' # min-max normalization operation
                new_pxl.append(new_val)
            new_row.append(new_pxl)
        new_img.append(new_row)

    img_printer(new_img)  # print the image at the end

elif operation == 2:

    means = []
    for ch_i in range(3):  # calculate the total to find the means
        total = 0
        for i in range(len(img)):
            for j in range(len(img[i])):
                total += img[i][j][ch_i]

        means.append(total/(len(img)**2))  # find the means for every channel value

    stan_devs = []
    for ch_i in range(3):  # calculate standard deviations
        stan_total = 0
        for i in range(len(img)):
            for j in range(len(img[i])):
                stan_total += (img[i][j][ch_i] - means[ch_i])**2  # this is the total in the stan_dev equation

        stan_devs.append((stan_total/(len(img))**2)**0.5)  # rest of the operation is done during appending

    new_img = []
    for row in img:  # for every value in every pixel in every row
        new_row = []  # create a new list and append all the adjusted values to those lists
        for pxl in row:
            new_pxl = []
            for ch_i in range(len(pxl)):
                new_val = '{0:.4f}'.format((pxl[ch_i] - means[ch_i]) / stan_devs[ch_i])  # z-score normalization formula
                new_val = new_val.rstrip('0')  # strip the zeros to the right
                new_pxl.append(new_val)
            new_row.append(new_pxl)
        new_img.append(new_row)

    img_printer(new_img)  # print the image at the end

elif operation == 3:

    new_img = []
    for row in img:  # for every value in every pixel in every row
        new_row = []  # create a new list and append all the adjusted values to those lists
        for pxl in row:
            new_pxl = [sum(pxl)//3]*3  # taking the average of each pixel
            new_row.append(new_pxl)
        new_img.append(new_row)
    img_printer(new_img)  # print the adjusted image

elif operation == 4:
    filter_name = input()  # take inputs
    stride = int(input())
    fd = open(filter_name, 'r')  # extract the filter
    contents = fd.read()
    fd.close()
    filter_str = contents.split('\n')  # split the filter into a 2-d list
    filter_lst = []
    for line in filter_str:
        new_line = line.split()
        filter_lst.append(new_line)

    new_img = []

    for i in range(0, len(img)-2, stride):  # for every value in every pixel in every row
        new_row = []  # create a new list and append all the adjusted values to those lists
        for j in range(0, len(img[i])-2, stride):
            new_pxl = []
            for k in range(len(img[i][j])):
                total = 0  # filter total
                for row in range(len(filter_lst)):
                    for pxl in range(len(filter_lst[row])):
                        total += img[i+row][j+pxl][k] * int(filter_lst[row][pxl])
                new_pxl.append(total)
            new_row.append(new_pxl)
        new_img.append(new_row)

    img_printer(new_img)  # print the image at the end


