def search_and_highlight_keyword(text, keyword):
    """
    Search for a keyword in the extracted text and highlight it.
    """
    if keyword.lower() in text.lower():
        # Highlight all occurrences of the keyword
        highlighted_text = text.replace(
            keyword, f'<span style="background-color: red">{keyword}</span>'
        )
        return highlighted_text
    return None
