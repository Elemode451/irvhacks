from app.utils.constants import ALLOWED_FIELDS


def filter_json(doctor_entry):
    filtered_data = {}

    for doctor_name, details in doctor_entry.items():
        if 'data' in details and 'healthgrades' in details['data']:
            extracted_data = []

            for item in details['data']['healthgrades']:
                filtered_item = {
                    field: item.get(field) for field in ALLOWED_FIELDS if field in item
                }
                extracted_data.append(filtered_item)

            filtered_data[doctor_name] = extracted_data

    return filtered_data

prefixes = ["Dr.", "Prof.", "Mr.", "Mrs.", "Ms.", "Sir.", "Lady", "Drs."]
suffixes = ["PhD", "MD", "DDS", "MBA", "DO", "DPT", "Esq", "RN", "FAAN", "FACS"]

def clean_name(name):
    for prefix in prefixes:
        if name.startswith(prefix):
            name = name[len(prefix):].strip()
            break  

    for suffix in suffixes:
        if name.endswith(f", {suffix}") or name.endswith(f" {suffix}"):
            name = name[: -len(suffix)].strip().rstrip(",")
            break

    return name.strip()

    
def split_name(name):
    """
    Split a full name into first name and last name.
    Handles cases like initials and multi-word names.
    """
    parts = name.split()
    
    if len(parts) == 0:
        return ("", "")
    if len(parts) == 1:
        return (parts[0], "")  

    last_name = parts[-1]

    if len(parts) > 2 and parts[0][-1] == ".":
        first_name = " ".join(parts[:-1])  
    else:
        first_name = " ".join(parts[:-1])  

    return (first_name.strip(), last_name.strip())