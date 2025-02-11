import os, shutil
os.chdir('Manga')
print('Analysing files...')
filesCount = 0
for i in os.listdir():
    filesCount += len(os.listdir(os.getcwd() + '\\' + i))

curr_page = 1
folders = sorted(os.listdir(), key=lambda x:(float(x.split('-')[0][1:]), float(x.split('-')[1][1:])))

page_rank = len(str(filesCount))
volume_rank = 3
chapter_rank = 4

print('Files count:', filesCount)
print('Start renaming...')
os.makedirs('../Export')
for i in folders:
    os.chdir(i)
    files = sorted(os.listdir(), key = lambda x: int(x.split('-')[0][1:]))
    for name in files:
        path_dir = i.split('-')
        new_name = 'v' + '0' * (volume_rank - len(path_dir[0]) + 1) + path_dir[0][1:] + '-n' + '0' * (chapter_rank - len(str(int(float(path_dir[1][1:]))))) + str(int(float(path_dir[1][1:]))) + '-p' + '0' * (page_rank - len(str(curr_page))) + str(curr_page) + '.jpg'
        # new_name = 'p' + '0' * (page_rank - len(str(curr_page))) + str(curr_page) + '.jpg'
        os.rename(name, '../../Export/' + new_name)
        curr_page += 1
    os.chdir('..')
print('Complete!')

os.chdir('..')

print('Start archiving..')
shutil.make_archive('Manga', 'zip', 'Export/')
shutil.rmtree('Export', ignore_errors=True)
print('Complete!')