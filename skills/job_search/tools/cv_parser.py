# skills/job_search/tools/cv_parser.py

import pdfplumber


def parse_cv(file_path: str) -> str:

    text = ""

    with pdfplumber.open(file_path) as pdf:

        for page in pdf.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

            if len(text) >= 3000:
                break

    return text[:3000]