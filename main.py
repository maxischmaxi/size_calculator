from os import listdir, getcwd
from os.path import isfile, join, isdir, getsize

def get_size(file_path):
  file_size = getsize(file_path)
  unit = 'bytes'

  if file_size > 1024:
    unit = 'kb'
  elif file_size > 1024 ** 2:
    unit = 'mb'
  elif file_size > 1024 ** 3:
    unit = 'gb'

  exponents_map = {'bytes': 0, 'kb': 1, 'mb': 2, 'gb': 3}
  size = file_size / 1024 ** exponents_map[unit]

  if unit == 'bytes':
    return str(file_size) + " " + unit
  else:
    return round(size, 3).__str__() + " " + unit

def get_files_of_folder(path):
    files = listdir(path)
    returning_files = []
    
    for file in files:
      if isfile(join(path, file)):
        returning_files.append((file, join(path, file), get_size(join(path, file))))
      elif isdir(join(path, file)):
        appending_files = get_files_of_folder(join(path, file))
        for appending_file in appending_files:
          returning_files.append(appending_file)
      else:
        print("Error: " + file + " is not a file or directory")

    return returning_files
        

if __name__ == '__main__':
    # get the current working directory
    cwd = getcwd()
    
    # get the files of the current working directory
    files = get_files_of_folder(cwd)
    # sort files by size
    files.sort(key=lambda x: x[2], reverse=True)

    print("Filename".ljust(50, " ") + "Size")
    print("-" * 60)

    if len(files) <= 10:
      #print the files with their size
      for file in files:
        # print the file name and the size with the name as a fixed length
        print(file[0].ljust(50, " ") +  file[2])
    else:
      #print the 10 biggest files with their size
      for i in range(10):
        # print the file name and the size with the name as a fixed length
        print(files[i][0].ljust(50, " ") + files[i][2])
    