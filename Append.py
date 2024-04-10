# Функция для открытия файлов
def openFiles(file, fileName, list_linesOfFile):
  with open (file, 'r', encoding='utf-8') as fileName:
    list_linesOfFile = fileName.readlines()
    return list_linesOfFile

list_linesOfFile1 = openFiles('c:/Users/Админ/Desktop/ReadFiles/Files/1.txt', 'file1', 'list_linesOfFile1') 
list_linesOfFile2 = openFiles('c:/Users/Админ/Desktop/ReadFiles/Files/2.txt', 'file2', 'list_linesOfFile2')
list_linesOfFile3 = openFiles('c:/Users/Админ/Desktop/ReadFiles/Files/3.txt', 'file3', 'list_linesOfFile3')

with open ('result.txt', 'w', encoding='utf-8') as file_result:
  all_files_length_dict = {'1.txt': [list_linesOfFile1, len(list_linesOfFile1)], '2.txt': [
      list_linesOfFile2, len(list_linesOfFile2)], '3.txt': [list_linesOfFile3, len(list_linesOfFile3)]}
  
  all_files_length = [len(list_linesOfFile1), len(list_linesOfFile2), len(list_linesOfFile3)]
  all_files_length = sorted(all_files_length)

  for j in all_files_length:
    for key, value in all_files_length_dict.items():
      if value[1] == j:
        file_result.write(f'{key}')
        file_result.write(f'\n{all_files_length_dict[key][1]}\n')
        for string in all_files_length_dict[key][0]:
          file_result.write(f'{string}')
        file_result.write('\n\n')
