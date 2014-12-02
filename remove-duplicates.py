"""
This removes the duplicate files from the current directory
Has a dependency on FSLint's generated files (which must be named duplicates.txt)
"""

import os

group_counter = 0
duplicate_counter = 0

with open('duplicates.txt') as f:
    for line in f:
        # Skip empty lines
        if not line.strip():
            continue
        # Lines beginning with '#' are the beginning of duplicate groups
        elif line.startswith('#'):
            group_counter += 1
            duplicate_counter = 0
        else:
            duplicate_counter += 1
            file_name = line.strip()
            if duplicate_counter == 1:
                # We do NOT want to delete the first duplicate
                print('{0}.{1} - KEEP: {2}'.format(group_counter, duplicate_counter, file_name))
            else:
                # The first duplicate has already been kept, so delete this one
                print('{0}.{1} - DELETE: {2}'.format(group_counter, duplicate_counter, file_name))
                try:
                    os.remove(file_name)
                except:
                    print('NO FILE: {0}'.format(file_name))
