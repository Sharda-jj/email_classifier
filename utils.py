import re

def mask_pii_neutral_order(text):
    """
    Detects and masks personally identifiable information (PII) in the input text.
    Ensures that overlapping entities are resolved based on defined priority.
    
    Args:
        text (str): Raw email text containing potential PII.

    Returns:
        masked_text (str): Text with PII replaced by [entity_type] placeholders.
        final_entities (list): List of dicts with original entity, position, and classification.
    """
    entities = []

    # Priority ranking: lower number = higher importance
    priority = {
        "credit_debit_no": 1,
        "aadhar_num": 2,
        "phone_number": 3,
        "email": 1,
        "full_name": 2,
        "dob": 2,
        "cvv_no": 1,
        "expiry_no": 2
    }

    # Regex patterns for each PII type
    patterns = {
        'email': r'\b[\w\.-]+@[\w\.-]+\.\w+\b',
        'credit_debit_no': r'\b\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}\b',
        'aadhar_num': r'\b\d{4}[-\s]?\d{4}[-\s]?\d{4}\b',
        'phone_number': r'\+?\d{1,3}[-\s]?\d{1,4}[-\s]?\d{3,4}[-\s]?\d{4}',
        'full_name': r'\b(?!My\b)[A-Z][a-z]+(?: [A-Z][a-z]+)+\b',
        'dob': r'\b\d{2}[/-]\d{2}[/-]\d{4}\b',
        'expiry_no': r'\b(0[1-9]|1[0-2])[/\-](\d{2}|\d{4})\b',
        'cvv_no': r'(?<!\[)\b\d{3}\b(?!\])'
    }

    # Step 1: Collect all matches
    for label, pattern in patterns.items():
        for match in re.finditer(pattern, text):
            entities.append({
                "start": match.start(),
                "end": match.end(),
                "classification": label,
                "entity": match.group(),
                "priority": priority[label]
            })

    # Step 2: Sort by start, then by priority
    entities.sort(key=lambda x: (x["start"], x["priority"]))

    # Step 3: Filter out overlapping entities based on priority
    filtered_entities = []
    for ent in entities:
        overlap = any(
            not (ent["end"] <= kept["start"] or ent["start"] >= kept["end"])
            for kept in filtered_entities
        )
        if not overlap:
            filtered_entities.append(ent)

    # Step 4: Replace in reverse order to preserve character indices
    for ent in sorted(filtered_entities, key=lambda x: x["start"], reverse=True):
        text = text[:ent['start']] + f"[{ent['classification']}]" + text[ent['end']:]

    # Step 5: Prepare final output
    final_entities = [{
        "position": [ent['start'], ent['end']],
        "classification": ent['classification'],
        "entity": ent['entity']
    } for ent in filtered_entities]

    return text, final_entities
