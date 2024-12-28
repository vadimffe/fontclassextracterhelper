from fontTools.ttLib import TTFont
import re

# Function to convert glyph name to a meaningful constant name
def glyph_to_constant_name(glyph_name):
    # Replace hyphens with underscores and convert to PascalCase
    name = re.sub(r'[-]', '_', glyph_name)
    name = re.sub(r'(?<!^)(?=[A-Z])', '_', name)

    # If the name starts with a number, prefix it with an underscore
    if name[0].isdigit():
        name = f"_{name}"

    return name.capitalize()

# Load the font file
font_path = "FWBrands-Regular-400.otf"
font = TTFont(font_path)

# Access the cmap table to get Unicode mappings
cmap = font["cmap"].getcmap(3, 1)  # Platform ID 3 (Windows), Encoding ID 1 (Unicode BMP)

# Initialize the C# class definition
cs_class = [
    "using System;",
    "using System.Collections.Generic;",
    "using System.Linq;",
    "using System.Text;",
    "using System.Threading.Tasks;",
    "",
    "namespace CSharp.Sample.Helpers",
    "{",
    "    public static class FontAwesomeBrandIcons",
    "    {",
]

# Track already added constants to avoid duplicates
added_constants = set()

# Iterate through character codes and glyph names
for char_code, glyph_name in cmap.cmap.items():
    # Skip .notdef and other special glyphs
    if glyph_name.startswith("."):
        continue

    # Convert glyph name to a meaningful constant name
    constant_name = glyph_to_constant_name(glyph_name)

    # Skip if this constant name is already added
    if constant_name in added_constants:
        continue

    # Add the constant name to the set
    added_constants.add(constant_name)

    # Format the constant string
    constant = f"        public const string {constant_name} = \"\\u{char_code:04x}\";"

    # Add to the class definition
    cs_class.append(constant)

# Close the class and namespace
cs_class.extend([
    "    }",
    "}",
])

# Write the output to a .cs file
output_path = "FontAwesomeBrandIcons.cs"
with open(output_path, "w", encoding="utf-8") as file:
    file.write("\n".join(cs_class))

print(f"C# class generated and saved to {output_path}")
