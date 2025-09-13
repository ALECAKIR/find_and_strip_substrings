def find_and_strip_substrings(xstr: str, ystr: str, zstr: str) -> str:
    """
    Extract and concatenate all substrings in `xstr` that are enclosed by
    the markers `ystr` and `zstr`, excluding the markers themselves.

    Behavior:
    - Scans left-to-right, non-overlapping pairs: after a match, continues
      searching after the closing marker `zstr`.
    - Returns the concatenation of the inner contents between each pair.
    - If no complete pair is found, returns the original `xstr` unchanged.
    - If `ystr` or `zstr` is empty, returns the original `xstr` (avoids
      ambiguous or infinite-match scenarios).

    Examples:
    - find_and_strip_substrings("xyz", "x", "z") -> "y"
    - find_and_strip_substrings("xyz", "a", "b") -> "xyz"
    - find_and_strip_substrings("aSTARThelloENDbSTARTworldEND", "START", "END") -> "helloworld"
    """
    # Guard against empty markers which would create zero-length matches
    if not ystr or not zstr:
        return xstr

    results = []
    i = 0
    n = len(xstr)
    ly = len(ystr)
    lz = len(zstr)

    # Fast path: if either marker not present at all, return original
    if xstr.find(ystr) == -1 or xstr.find(zstr) == -1:
        return xstr

    while i < n:
        y_start = xstr.find(ystr, i)
        if y_start == -1:
            break
        inner_start = y_start + ly
        z_start = xstr.find(zstr, inner_start)
        if z_start == -1:
            break
        results.append(xstr[inner_start:z_start])
        i = z_start + lz

    return "".join(results) if results else xstr
