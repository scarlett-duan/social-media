
for num in range(1, 6):
    try:
        print(num, ':')
        foldername = "../000毕业设计+信安大赛/ximalaya_data/" + \
            str(num) + "_upload/2_audio/"
        filename = foldername + "temp" + str(num)
        with open(filename, 'r') as f:
            lines = f.readlines()
        i = 0
        data_list = []
        save_name = foldername + "result_" + str(num) + '.csv'
        fd = open(save_name, 'w')
        new_data = ''
        for line in lines:
            i = i + 1
            if i < 5:
                continue

            data_line = line.strip().split(' ')
            # data_line = list(data_line.replace(" ", ",")
            for k in data_line.copy():
                if k == '':
                    data_line.remove(k)
            data_line = ','.join(data_line)
            data_list.append(data_line)
            # print(i, data_line)
            if (i-4) % 103 == 0:
                new_line = str(int((i-4)/103)) + ',' + ','.join(data_list)
                # print(new_line)
                new_data = new_data + new_line + '\n'
                data_list = []
            if i % 1000 == 0:
                print('\r', "total:%d, now:%d..." % (len(lines), i), end='')
        fd.write(new_data)
        fd.close()
        print('\n')
    except Exception as err:
        print(err)
