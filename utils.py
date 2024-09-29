def search_and_highlight_keyword(text, keyword):
    """
    Search for a keyword in the extracted text and highlight it.
    """
    # Check if the keyword exists in the text (case-insensitive)
    if keyword.lower() in text.lower():
        # Highlight all occurrences of the keyword (case-insensitive)
        highlighted_text = text.replace(
            keyword, f'<span style="background-color: red">{keyword}</span>'
        )
        return highlighted_text
    return text
