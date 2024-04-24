from styling_dict import styling_dict
import os

# Get a list of all the fonts in the /fonts folder
all_fonts = set([f'./fonts/{font}' for font in os.listdir('./fonts')])

# Get a list of all the fonts used in the styling_dict
used_fonts = set()
for key, value in styling_dict.items():
    for inner_key, inner_value in value.items():
        if hasattr(inner_value, 'font'):
            used_fonts.add(inner_value.font)

# Find the fonts that are in the /fonts folder but not in the styling_dict
unused_fonts = all_fonts - used_fonts

for font in unused_fonts:
    print(font)

