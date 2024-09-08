import os

ini_folder = './ximalaya_data/'
filename = ''
for i in range(1, 6):
    try:
        foldername = ini_folder + str(i) + '_upload/2_audio/'
        filename = foldername + str(i) + '.m4a'
        cmd = 'faad ' + filename + ' > ' + foldername + 'temp' + str(i)
        os.system(cmd)
    except Exception as err:
        print(err)
        print("file name: " + filename)
