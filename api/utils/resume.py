import re
from collections import Counter
from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer, LTChar, LTTextLineHorizontal


def extract_resume_sections_from_pdf(pdf_file_object):
    """
    Extracts structured sections from a resume PDF by analyzing font size and keywords.

    This function parses a PDF and identifies section headers based on a combination of
    heuristics: larger font size than the body text, matching common section titles,
    and being in all-caps. It then returns a dictionary where keys are normalized
    section titles and values are the text content of those sections.

    Args:
        pdf_path (str): The file path to the resume PDF.

    Returns:
        dict: A dictionary of the extracted sections (e.g., {'Experience': '...', 'Education': '...'}).
    """

    # --- 1. Define Section Headers and Normalization Map ---
    # Maps various header names to a standardized name.
    section_mapping = {
        "experience": "Experience",
        "work experience": "Experience",
        "professional experience": "Experience",
        "employment history": "Experience",
        "education": "Education",
        "academic background": "Education",
        "skills": "Skills",
        "technical skills": "Skills",
        "certifications": "Certifications",
        "licenses & certifications": "Certifications",
        "projects": "Projects",
        "personal projects": "Projects",
        "summary": "Summary",
        "objective": "Summary",
        "professional summary": "Summary",
        "contact": "Contact",
        "contact information": "Contact",
        "achievements": "Achievements",
        "awards": "Achievements",
        "publications": "Publications",
        "references": "References",
    }
    # A regex pattern to catch any of the keys in the mapping.
    header_pattern = re.compile(r"|".join(section_mapping.keys()), re.IGNORECASE)

    # --- 2. Extract Text Lines with Font Information ---
    lines_with_meta = []
    try:
        for page_layout in extract_pages(pdf_file_object):
            for element in page_layout:
                if isinstance(element, LTTextContainer):
                    for text_line in element:
                        if isinstance(text_line, LTTextLineHorizontal):
                            line_text = text_line.get_text().strip()
                            # Get the font size of the first character in the line
                            first_char_size = 0
                            if line_text:
                                for char in text_line:
                                    if isinstance(char, LTChar):
                                        first_char_size = round(char.size, 2)
                                        break
                            if line_text and first_char_size > 0:
                                lines_with_meta.append(
                                    {"text": line_text, "size": first_char_size}
                                )
    except Exception as e:
        print(f"Error processing PDF {pdf_path}: {e}")
        return {}

    if not lines_with_meta:
        return {}

    # --- 3. Determine Body Text Font Size ---
    font_sizes = [line["size"] for line in lines_with_meta]
    if not font_sizes:
        return {}
    # The most common font size is likely the body text
    body_font_size = Counter(font_sizes).most_common(1)[0][0]

    # --- 4. Identify Headers and Group Content ---
    sections = {}
    current_section_title = "Header"  # For content before the first recognized section
    current_section_content = []

    for line in lines_with_meta:
        text = line["text"]
        size = line["size"]

        # Heuristic to identify a header:
        # 1. Font size is larger than the body text.
        # 2. Or, it's a short line in all caps.
        # 3. Or, it matches one of our predefined header keywords.
        is_header = (
            size > body_font_size + 1  # Epsilon for minor variations
            or (len(text.split()) < 5 and text.isupper())
            or header_pattern.match(text)
        )

        if is_header:
            # When a new header is found, save the previous section
            if current_section_title and current_section_content:
                # Normalize the title before saving
                normalized_title = section_mapping.get(
                    current_section_title.lower(), current_section_title
                )
                sections[normalized_title] = "\n".join(current_section_content).strip()

            # Start a new section
            current_section_title = text
            current_section_content = []
        else:
            # Append content to the current section
            current_section_content.append(text)

    # Don't forget to save the last section being processed
    if current_section_title and current_section_content:
        normalized_title = section_mapping.get(
            current_section_title.lower(), current_section_title
        )
        sections[normalized_title] = "\n".join(current_section_content).strip()

    # Clean up potential "Header" section if it's empty or just contact info
    if "Header" in sections and len(sections["Header"].split()) < 10:
        if "Contact" not in sections:
            sections["Contact"] = sections.pop("Header")
        else:
            # Append to existing contact info
            sections["Contact"] = sections["Header"] + "\n" + sections["Contact"]
            sections.pop("Header")

    return sections
