# Find And Strip Substrings

This repository provides a single function `find_and_strip_substrings(xstr, ystr, zstr)` that scans `xstr` and extracts the contents enclosed by `ystr ... zstr`, concatenating the inner parts and excluding the markers themselves.

## How It Works

- Uses `str.find` to locate the next `ystr`, then the following `zstr`.
- Extracts the inner substring and continues scanning after the found `zstr` (non-overlapping, left-to-right).
- If no complete `ystr`/`zstr` pair is found, returns the original `xstr` unchanged.
- If `ystr` or `zstr` is empty, returns the original `xstr` to avoid ambiguous matches.

Time complexity is linear in the length of `xstr`.

## Usage

```python
from subs import find_and_strip_substrings

print(find_and_strip_substrings("xyz", "x", "z"))
# -> "y"

print(find_and_strip_substrings("xyz", "a", "b"))
# -> "xyz"  (no pair found, original returned)

print(find_and_strip_substrings("aSTARThelloENDbSTARTworldEND", "START", "END"))
# -> "helloworld"
```

## Contributing
Feel free to fork the repository and submit a pull request with improvements or bug fixes.

## License
This project is licensed under the MIT License.
