# config.py

OPENROUTER_API_KEY = "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"
GOOGLE_SHEETS_CREDENTIALS_FILE = "E:\Pyhton\AI_Job_Agent\\aijobagent-458205-8c7c44694ea4.json"
SHEET_NAME = "Job Applications"
OLD_RESUME_PATH = "E:\Pyhton\AI_Job_Agent\Venkatesh_Enakonda_QA.docx"
NEW_RESUME_DOCX_PATH = "E:\Pyhton\AI_Job_Agent\\new_resume.docx"
NEW_RESUME_PDF_PATH = "E:\Pyhton\AI_Job_Agent\\new_resume.pdf"


STOPWORDS = set([
    'the', 'and', 'to', 'in', 'for', 'of', 'a', 'with', 'on', 'at', 'as', 'is', 'by', 'an', 'be', 'or',
    'from', 'this', 'that', 'are', 'your', 'will', 'we', 'our', 'you', 'job', 'role'
])

MIN_KEYWORD_FREQUENCY = 2