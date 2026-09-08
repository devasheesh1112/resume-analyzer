from io import BytesIO
from pypdf import PdfReader


def extract_text(content: bytes, filename: str) -> str:

    if filename.lower().endswith(".pdf"):

        reader = PdfReader(BytesIO(content))

        text = ""

        for page in reader.pages:
            text += page.extract_text() or ""

        return text.strip()

    return content.decode("utf-8", errors="ignore").strip()