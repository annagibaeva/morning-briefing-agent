import os

PLAN_FILE = r"C:\Users\annag\OneDrive\Documents\Claude-Cowork\PROJECTS\agent-pm-learning-plan.md"
RESOURCES_FILE = r"C:\Users\annag\Downloads\agent-pm-resources.md"
PROGRESS_FILE = os.path.join(os.path.dirname(__file__), "progress.json")
LOG_FILE = os.path.join(os.path.dirname(__file__), "logs", "briefing.log")
TOKEN_FILE = os.path.join(os.path.dirname(__file__), "token.json")
CREDENTIALS_FILE = os.path.join(os.path.dirname(__file__), "credentials.json")

EMAIL_TO = "annagibaeva05@gmail.com"
MODEL = "claude-sonnet-4-6"
ANTHROPIC_BLOG_URL = "https://www.anthropic.com/engineering"

GOOGLE_SCOPES = [
    "https://www.googleapis.com/auth/calendar.readonly",
    "https://www.googleapis.com/auth/gmail.readonly",
    "https://www.googleapis.com/auth/gmail.send",
]
