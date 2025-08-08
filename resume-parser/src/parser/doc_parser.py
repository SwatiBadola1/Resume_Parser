def extract_text_from_doc(file_path):
    import docx

    doc = docx.Document(file_path)
    full_text = []
    for paragraph in doc.paragraphs:
        full_text.append(paragraph.text)
    return '\n'.join(full_text)

def parse_doc_resume(file_path):
    text = extract_text_from_doc(file_path)
    # Further processing can be done here to extract structured data
    return {
        'text': text,
        'name': None,  # Placeholder for name extraction
        'skills': [],  # Placeholder for skills extraction
        'education': []  # Placeholder for education extraction
    }