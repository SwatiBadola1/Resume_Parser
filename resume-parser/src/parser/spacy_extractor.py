def extract_candidate_details(text):
    import spacy

    # Load the spaCy model
    nlp = spacy.load("en_core_web_sm")

    # Process the text with spaCy
    doc = nlp(text)

    # Initialize a dictionary to hold extracted information
    candidate_info = {
        "name": None,
        "skills": [],
        "education": []
    }

    # Extract name (assuming the first proper noun is the name)
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            candidate_info["name"] = ent.text
            break

    # Extract skills (assuming skills are nouns or proper nouns)
    for token in doc:
        if token.pos_ in ["NOUN", "PROPN"] and token.text.lower() not in candidate_info["skills"]:
            candidate_info["skills"].append(token.text)

    # Extract education (assuming education is mentioned in specific phrases)
    education_keywords = ["Bachelor", "Master", "PhD", "degree", "University", "College"]
    for sent in doc.sents:
        if any(keyword in sent.text for keyword in education_keywords):
            candidate_info["education"].append(sent.text)

    return candidate_info