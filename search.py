# search.py
def search_keyword(text, keyword):
    """
    Search for a keyword in the extracted text.
    """
    if keyword in text:
        return True
    else:
        return False
