# Font to C# Glyph Mapping Generator

This Python script generates a C# class containing Unicode character mappings as constants by reading glyph data from a font file (e.g., `.otf`, `.ttf`). It is particularly suitable for fonts like FontAwesome but can also be used with other fonts.

## Features

- **Extract Unicode mappings** from the font file's `cmap` table.
- **Convert glyph names** into valid, PascalCase C# constant names.
- Handles glyph names starting with numbers or special characters.
- Outputs a formatted C# file with Unicode constants.

---

## Example Output

```csharp
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CSharp.Sample.Helpers
{
    public static class FontAwesomeBrandsIcons
    {
        public const string Space = "\u0020";
        public const string Exclamation = "\u0021";
        public const string Zero_width_space = "\u0022";
        public const string Hashtag = "\u0023";
        public const string Dollar_sign = "\u0024";
        public const string Percent = "\u0025";
        public const string Asterisk = "\u002a";
        public const string Plus = "\u002b";
        public const string Hyphen = "\u002d";
        public const string _0 = "\u0030";
        public const string _1 = "\u0031";
    }
}
