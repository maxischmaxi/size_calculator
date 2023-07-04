from os import listdir, getcwd, stat
from os.path import isfile, join, isdir

def get_file_size(path):
  size = stat(path).st_size
  # calculate if the size is in KB, MB or GB
  if size < 1024:
    # return the size in bytes
    return str(size) + " B"
  elif size < 1024 * 1024:
    # return the size in kilobytes
    return str(round(size / 1024, 2)) + " KB"
  elif size < 1024 * 1024 * 1024:
    # return the size in megabytes
    return str(round(size / (1024 * 1024), 2)) + " MB"
  else:
    # return the size in gigabytes
    return str(round(size / (1024 * 1024 * 1024), 2)) + " GB"

def get_files_of_folder(path):
    files = listdir(path)
    returning_files = []
    
    for file in files:
      if isfile(join(path, file)):
        returning_files.append((file, join(path, file), get_file_size(join(path, file))))
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
    #print the files with their size
    for file in files:
      print(file[0] + " - " + str(file[2]))