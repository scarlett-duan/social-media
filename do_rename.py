import os

print(os.listdir())
foldername = ("./weibo_data/data_1/")
for num in range(1, 16):
    try:
        i = str(num)
        filename = foldername + i + "_upload/1_video/"

        files = os.listdir(filename)
        print(files)
        name = ''
        for f in files:
            if "segment" in f:
                name = f
                print(name)
                break

        new_filename = filename + i
        if os.path.exists(new_filename):
            continue

        old_filename = filename + name
        old_fd = open(old_filename, 'rb')
        data = old_fd.read()

        with open(new_filename, 'wb') as fd:
            fd.write(data)
        old_fd.close()
        fd.close()
    except Exception as err:
        print(err)
