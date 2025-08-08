from flask import Blueprint, request, jsonify
from parser.pdf_parser import parse_pdf
from parser.doc_parser import parse_doc
from db.models import db, Candidate

api = Blueprint('api', __name__)

@api.route('/upload', methods=['POST'])
def upload_resume():
    file = request.files.get('file')
    if not file:
        return jsonify({'error': 'No file provided'}), 400

    if file.filename.endswith('.pdf'):
        data = parse_pdf(file)
    elif file.filename.endswith('.doc') or file.filename.endswith('.docx'):
        data = parse_doc(file)
    else:
        return jsonify({'error': 'Unsupported file format'}), 400

    candidate = Candidate(**data)
    db.session.add(candidate)
    db.session.commit()

    return jsonify({'message': 'Resume uploaded and parsed successfully', 'data': data}), 201

@api.route('/candidates', methods=['GET'])
def get_candidates():
    candidates = Candidate.query.all()
    return jsonify([candidate.to_dict() for candidate in candidates]), 200