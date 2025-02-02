class Constants:
    class Parsing:
        LATEX_BLACKLIST = ["```latex", "```"]
        TEX_TEMPLATE_PATH = "../assets/template.tex"
        ALLOW_REATTEMPTS = False
        MAX_CALL_ATTEMPTS = 2
        CALL_ATTEMPT_DELAY = 1
    class Gemini:
        EXTRACT_PROMPT = "In the document, extract all the questions into a readable format for gemini. Please ensure you maintain all mathematical symbols and logic if applicable. Replace the numeric number of each question with a 'Q:' and separate each question by a string marker ‘crodie’"
        REMIX_PROMPT = """Instructions: Take the given question and remix it so that it is slightly different. If mathematics is involved, ensure that the overall structure is not heavily modified. If it is a MCQ question, replace the options with valid options for the question. Return only the LaTeX snippet in a single environment. Do not include any extra text or explanation outside the LaTeX snippet. Ensure that the latex document uses the correct symbols. Do not include documentclass or usepackage the response even if they are required. Do not use {verbatim} if there are math symbols in the response."""