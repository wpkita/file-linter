"""
This removes the duplicate files from the current directory
Has a dependency on FSLint's generated files (which must be named duplicates.txt)
"""

import os

group_counter = 0
duplicate_counter = 0

# Open duplicates.txt
with open('duplicates.txt') as f:
    # Iterate over lines
    for line in f:
        if not line.strip():
            # skip empty lines
            continue
        elif line.startswith('#'):
            # if line starts with #, then it is the beginning of a duplicate group
            # increment group counter
            group_counter += 1
            # reset duplicate counter
            duplicate_counter = 0
        else:
            # otherwise, we are still within the same duplicate group
            # increment duplicate counter
            duplicate_counter += 1
            file_name = line.strip()
            if duplicate_counter == 1:
                # if this is the first duplicate for this group
                # we DO NOT want to delete it
                # print its name
                print('{0}.{1} - KEEP: {2}'.format(group_counter, duplicate_counter, file_name))
            else:
                # otherwise, we've already saved the first duplicate
                # delete the file referenced by the current line
                print('{0}.{1} - DELETE: {2}'.format(group_counter, duplicate_counter, file_name))
                try:
                    os.remove(file_name)
                except:
                    print('NO FILE: {0}'.format(file_name))
