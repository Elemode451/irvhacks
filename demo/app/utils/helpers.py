prefixes = ["Dr.", "Prof.", "Mr.", "Mrs.", "Ms.", "Sir.", "Lady", "Drs."]
suffixes = ["PhD", "MD", "DDS", "MBA", "DO", "DPT", "Esq", "RN", "FAAN", "FACS"]

def clean_name(name):
    # Remove prefix if it exists
    for prefix in prefixes:
        if name.startswith(prefix):
            name = name[len(prefix):].strip()
            break  # Only one prefix should be removed

    # Remove suffix if it exists
    for suffix in suffixes:
        if name.endswith(f", {suffix}") or name.endswith(f" {suffix}"):
            name = name[: -len(suffix)].strip().rstrip(",")
            break  # Only one suffix should be removed

    return name.strip()

    
def split_name(name):
    """
    Split a full name into first name and last name.
    Handles cases like initials and multi-word names.
    """
    parts = name.split()
    
    # Handle empty or one-word names
    if len(parts) == 0:
        return ("", "")
    if len(parts) == 1:
        return (parts[0], "")  # Single-word name has no last name

    # Last word is always the last name
    last_name = parts[-1]

    # Handle initials (e.g., "J. Randall")
    if len(parts) > 2 and parts[0][-1] == ".":
        first_name = " ".join(parts[:-1])  # Include initials as part of the first name
    else:
        first_name = " ".join(parts[:-1])  # Exclude last name from first name

    return (first_name.strip(), last_name.strip())