"""
This removes the duplicate files from the current directory
Has a dependency on FSLint's generated files (which must be named duplicates.txt)
"""

import os


class DuplicateGroup:
    def __init__(self):
        self.duplicates = []

    def add_duplicate(self, file_path):
        self.duplicates.append(file_path)

    def purge(self):
        self.duplicates.sort(key=len)

        # Will keep the file with the shortest path
        file_to_keep = self.duplicates[0]
        print('KEEPING:\t{0}'.format(file_to_keep))

        # Will delete other files
        files_to_delete = self.duplicates[1:]

        for file_path in files_to_delete:
            print('DELETING:\t{0}'.format(file_path))
            try:
                os.remove(file_path)
            except:
                print('NO FILE: {0}'.format(file_path))

duplicateGroups = []
current_group = None
duplicates_index_file = 'duplicates.txt'

with open(duplicates_index_file) as f:
    for line in f:
        print(line)
        # Skip empty lines
        if not line.strip():
            continue
        # Lines beginning with '#' are the beginning of duplicate groups
        elif line.startswith('#'):
            current_group = DuplicateGroup()
            duplicateGroups.append(current_group)
        else:
            current_group.add_duplicate(line.strip())

for group in duplicateGroups:
    group.purge()