def extract_text_from_pdf(pdf_path):
    import pdfplumber

    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text.strip()

def parse_pdf_resume(pdf_path):
    text = extract_text_from_pdf(pdf_path)
    # Further processing can be done here to structure the data
    return {
        "raw_text": text,
        # Additional fields can be added as needed
    }