from os import listdir, getcwd
from os.path import isfile, join, isdir, getsize

def get_size(file_size: int):
  unit = 'Bytes'

  if file_size > 1024 and file_size < 1024 ** 2:
    unit = 'KB'
  elif file_size > 1024 ** 2 and file_size < 1024 ** 3:
    unit = 'MB'
  elif file_size > 1024 ** 3 and file_size < 1024 ** 4:
    unit = 'GB'
  else:
    unit = 'TB'

  return str(round(file_size / (1024 ** (['Bytes', 'KB', 'MB', 'GB', 'TB'].index(unit))), 2)) + ' ' + unit

def get_files_of_folder(path):
    files = listdir(path)
    returning_files = []
    
    for file in files:
      if isfile(join(path, file)):
        size = getsize(join(path, file))
        size_description = get_size(size)
        returning_files.append((file, size, size_description))
      if isdir(join(path, file)):
        appending_files = get_files_of_folder(join(path, file))
        for appending_file in appending_files:
          returning_files.append(appending_file)

    return returning_files
        

if __name__ == '__main__':
    # get the current working directory
    cwd = getcwd()
    
    # get the files of the current working directory
    files = get_files_of_folder(cwd)
    # sort files by size
    files.sort(key=lambda x: x[1], reverse=True)

    print("Filename".ljust(50, " ") + "Size")
    print("-" * 60)

    if len(files) <= 10:
      #print the files with their size
      for file in files:
        filename = file[0]
        if len(filename) > 50:
          # take the last 50 characters of the file name
          filename = file[0][-50:]
        filename = file[0].ljust(50, " ")

        # print the file name and the size with the name as a fixed length
        print(filename +  file[2])
    else:
      #print the 10 biggest files with their size
      for i in range(10):
        filename = files[i][0]
        if len(filename) > 50:
          # take the last 50 characters of the file name
          filename = files[i][0][-50:]
        filename = files[i][0].ljust(50, " ")

        # print the file name and the size with the name as a fixed length
        print(filename + files[i][2])
    