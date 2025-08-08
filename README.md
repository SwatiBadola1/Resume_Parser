# Resume Parser

This project is an automated resume parser that extracts and categorizes information from resumes in PDF and DOC formats. It utilizes various libraries such as spaCy for natural language processing, PDFPlumber for PDF handling, Flask for creating a web API, and PostgreSQL for data storage.

## Features

- Extracts candidate details such as name, skills, and education from resumes.
- Supports both PDF and DOC formats.
- Provides a RESTful API for uploading resumes and retrieving parsed data.
- Stores parsed information in a PostgreSQL database.

## Project Structure

```
resume-parser
├── src
│   ├── app.py                # Entry point of the application
│   ├── parser                # Module for parsing resumes
│   │   ├── __init__.py
│   │   ├── pdf_parser.py     # Functions for PDF resume parsing
│   │   ├── doc_parser.py     # Functions for DOC resume parsing
│   │   └── spacy_extractor.py # Functions for extracting information using spaCy
│   ├── api                   # Module for API routes
│   │   ├── __init__.py
│   │   └── routes.py         # API endpoint definitions
│   ├── db                    # Module for database interactions
│   │   ├── __init__.py
│   │   └── models.py         # Database models
│   └── utils                 # Utility functions
│       └── __init__.py
├── requirements.txt          # Project dependencies
├── README.md                 # Project documentation
└── config.py                 # Configuration settings
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd resume-parser
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up the PostgreSQL database and update the `config.py` file with your database connection details.

## Usage

1. Run the application:
   ```
   python src/app.py
   ```

2. Use a tool like Postman or cURL to interact with the API. You can upload resumes and retrieve parsed information.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
