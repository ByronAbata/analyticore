def is_valid_text(text: str) -> bool:
    return text and len(text.strip()) > 0 and len(text) <= 5000
