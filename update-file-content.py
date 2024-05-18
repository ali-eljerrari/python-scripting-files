import os

directory = 'dir_path'

for root, dirs, files in os.walk(directory):
    for filename in files:
        file_path = os.path.join(root, filename)
        
        # Open each file in read and write mode
        with open(file_path, 'r+') as file:
            content = file.read()
            
            # Seek to the beginning of the file
            file.seek(0)
            
            # Write the pattern at the beginning of the file
            file.write('```sh\n' + content)
            
            # Move to the end of the file
            file.seek(0, os.SEEK_END)
            
            # Write the pattern at the end of the file
            file.write('\n```\n')

print("Patterns have been added to each file.")
