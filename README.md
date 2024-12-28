# FontAwesome Brand Icons Generator

This Python script generates a C# static class containing constants for Font Awesome brand icons based on glyph names and Unicode mappings from a font file.

## Features

- Converts glyph names to PascalCase constant names, replacing hyphens with underscores.
- Ensures all constant names are valid C# identifiers.
- Extracts Unicode mappings from the font's `cmap` table.
- Writes the generated C# class to a file.

## Example Output

The script generates a C# class like this:

```csharp
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CSharp.Sample.Helpers
{
    public static class FontAwesomeBrandIcons
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
        // ... more constants
    }
}
