"""Sample data for the Knowledge Platform (Enterprise Brain) mini-app - UI only.

Deliberately reuses names/entities from app/seed_data.py (Villa 12's delay,
Anil Kumar, Hyderabad Steel Traders) so this reads as one shared business
graph across Operations and Knowledge, not two disconnected demos.
"""

HEALTH = {
    "documents": 1842,
    "conversations": 8421,
    "emails": 24231,
    "audio": 312,
    "videos": 18,
    "business_records": 3821,
    "connected_sources": 4,
    "indexed_items": 38624,
}

INGESTION_HEALTH = {
    "processing": 12,
    "completed": 38540,
    "failed": 23,
    "needs_review": 8,
    "duplicate": 4,
    "permission_errors": 2,
}

AI_USAGE = {
    "questions_answered": 412,
    "avg_sources": 4.2,
    "avg_response_time": "1.8s",
    "unanswered": 14,
    "low_confidence": 9,
}

CONNECTORS = [
    # Communication
    {"id": "whatsapp", "name": "WhatsApp Business", "category": "Communication",
     "desc": "Messages, voice notes, photos and documents shared with customers, vendors, and site teams.",
     "status": "Connected", "item_summary": "8,421 conversations", "last_sync": "Live", "health": "Healthy"},
    {"id": "gmail", "name": "Gmail", "category": "Communication",
     "desc": "Customer and vendor email threads, quotes, and contracts.",
     "status": "Connected", "item_summary": "24,231 emails", "last_sync": "2 minutes ago", "health": "Healthy"},
    {"id": "outlook", "name": "Outlook", "category": "Communication",
     "desc": "Microsoft 365 mail and calendar.", "status": "Not connected", "item_summary": "—", "last_sync": "—", "health": "Disconnected"},
    {"id": "teams", "name": "Microsoft Teams", "category": "Communication",
     "desc": "Team chats, channels, and shared files.", "status": "Not connected", "item_summary": "—", "last_sync": "—", "health": "Disconnected"},
    {"id": "slack", "name": "Slack", "category": "Communication",
     "desc": "Channel messages and shared files.", "status": "Not connected", "item_summary": "—", "last_sync": "—", "health": "Disconnected"},
    # Files
    {"id": "google-drive", "name": "Google Drive", "category": "Files",
     "desc": "Search your company documents, spreadsheets and presentations.",
     "status": "Connected", "item_summary": "12,421 items", "last_sync": "4 minutes ago", "health": "Healthy"},
    {"id": "onedrive", "name": "OneDrive", "category": "Files",
     "desc": "Microsoft 365 documents and personal files.", "status": "Not connected", "item_summary": "—", "last_sync": "—", "health": "Disconnected"},
    {"id": "sharepoint", "name": "SharePoint", "category": "Files",
     "desc": "Team sites and document libraries.", "status": "Not connected", "item_summary": "—", "last_sync": "—", "health": "Disconnected"},
    {"id": "dropbox", "name": "Dropbox", "category": "Files",
     "desc": "Shared folders and files.", "status": "Not connected", "item_summary": "—", "last_sync": "—", "health": "Disconnected"},
    # Business
    {"id": "tally", "name": "Tally", "category": "Business",
     "desc": "Invoices, payments, and ledger entries — kept live, not just indexed.",
     "status": "Connected", "item_summary": "3,821 records", "last_sync": "Yesterday", "health": "Warning"},
    {"id": "zoho", "name": "Zoho CRM", "category": "Business",
     "desc": "Leads, deals, and customer records from Zoho.", "status": "Not connected", "item_summary": "—", "last_sync": "—", "health": "Disconnected"},
    {"id": "salesforce", "name": "Salesforce", "category": "Business",
     "desc": "Opportunities, accounts, and contacts.", "status": "Not connected", "item_summary": "—", "last_sync": "—", "health": "Disconnected"},
    {"id": "hubspot", "name": "HubSpot", "category": "Business",
     "desc": "Marketing and sales CRM records.", "status": "Not connected", "item_summary": "—", "last_sync": "—", "health": "Disconnected"},
    {"id": "erp", "name": "ERP System", "category": "Business",
     "desc": "Generic ERP connector — inventory, procurement, and finance modules.", "status": "Not connected", "item_summary": "—", "last_sync": "—", "health": "Disconnected"},
    # Projects
    {"id": "jira", "name": "Jira", "category": "Projects",
     "desc": "Issues, sprints, and project tracking.", "status": "Not connected", "item_summary": "—", "last_sync": "—", "health": "Disconnected"},
    {"id": "asana", "name": "Asana", "category": "Projects",
     "desc": "Tasks and project boards.", "status": "Not connected", "item_summary": "—", "last_sync": "—", "health": "Disconnected"},
    {"id": "clickup", "name": "ClickUp", "category": "Projects",
     "desc": "Tasks, docs, and goals.", "status": "Not connected", "item_summary": "—", "last_sync": "—", "health": "Disconnected"},
    {"id": "monday", "name": "Monday.com", "category": "Projects",
     "desc": "Boards and work tracking.", "status": "Not connected", "item_summary": "—", "last_sync": "—", "health": "Disconnected"},
    {"id": "construction-platform", "name": "Construction Platform", "category": "Projects",
     "desc": "Site progress, BOQ, and material data from your construction-management tool.", "status": "Not connected", "item_summary": "—", "last_sync": "—", "health": "Disconnected"},
    # Database
    {"id": "postgresql", "name": "PostgreSQL", "category": "Database",
     "desc": "Connect a Postgres database directly.", "status": "Not connected", "item_summary": "—", "last_sync": "—", "health": "Disconnected"},
    {"id": "mysql", "name": "MySQL", "category": "Database",
     "desc": "Connect a MySQL database directly.", "status": "Not connected", "item_summary": "—", "last_sync": "—", "health": "Disconnected"},
    {"id": "sqlserver", "name": "SQL Server", "category": "Database",
     "desc": "Connect a Microsoft SQL Server database.", "status": "Not connected", "item_summary": "—", "last_sync": "—", "health": "Disconnected"},
    {"id": "mongodb", "name": "MongoDB", "category": "Database",
     "desc": "Connect a MongoDB collection.", "status": "Not connected", "item_summary": "—", "last_sync": "—", "health": "Disconnected"},
    # Web
    {"id": "website", "name": "Website", "category": "Web",
     "desc": "Crawl your own company website and public pages.", "status": "Not connected", "item_summary": "—", "last_sync": "—", "health": "Disconnected"},
    {"id": "sitemap", "name": "Sitemap", "category": "Web",
     "desc": "Crawl a full site via its sitemap.xml.", "status": "Not connected", "item_summary": "—", "last_sync": "—", "health": "Disconnected"},
    # Custom
    {"id": "uploads", "name": "File Upload", "category": "Custom",
     "desc": "Anything uploaded manually — photos, scanned bills, PDFs.",
     "status": "Connected", "item_summary": "142 files", "last_sync": "3 hours ago", "health": "Healthy"},
    {"id": "api", "name": "Custom API", "category": "Custom",
     "desc": "Point at any REST API with your own field mapping.", "status": "Not connected", "item_summary": "—", "last_sync": "—", "health": "Disconnected"},
    {"id": "webhook", "name": "Webhook", "category": "Custom",
     "desc": "Receive events pushed from another system in real time.", "status": "Not connected", "item_summary": "—", "last_sync": "—", "health": "Disconnected"},
    {"id": "mcp", "name": "MCP", "category": "Custom",
     "desc": "Connect any MCP-compatible tool or data source.", "status": "Not connected", "item_summary": "—", "last_sync": "—", "health": "Disconnected"},
]

CONNECTOR_CATEGORIES = ["Communication", "Files", "Business", "Projects", "Database", "Web", "Custom"]

CONNECTOR_ERRORS = {
    "tally": [
        {"file": "GRN-118.xml", "reason": "Rate limit", "timestamp": "2026-09-30 22:14"},
        {"file": "Ledger export — Sep", "reason": "Authentication expired", "timestamp": "2026-09-30 09:02"},
    ]
}

LIBRARY_ITEMS = [
    {"title": "Villa 12 — Site Update, 12 Sep", "type": "WhatsApp", "category": "conversations", "source": "WhatsApp",
     "owner": "Anil Kumar", "updated": "2026-09-29", "language": "Telugu",
     "related": ["Villa 12", "Block C"]},
    {"title": "ABC Villa 31 — Steel Purchase Order #381", "type": "Document", "category": "documents", "source": "Google Drive",
     "owner": "Priya Sharma", "updated": "2026-09-20", "language": "English",
     "related": ["Villa 31", "Hyderabad Steel Traders"]},
    {"title": "Hyderabad Steel Traders — Invoice INV-2291", "type": "Invoice", "category": "invoices", "source": "Tally",
     "owner": "Kiran Rao", "updated": "2026-09-18", "language": "English",
     "related": ["Villa 31", "Hyderabad Steel Traders"]},
    {"title": "Re: Steel delivery delay", "type": "Email", "category": "emails", "source": "Gmail",
     "owner": "Srinivas Reddy", "updated": "2026-09-27", "language": "English",
     "related": ["Villa 31", "Hyderabad Steel Traders"]},
    {"title": "Villa 24 — Client progress call, 25 Sep", "type": "Call", "category": "conversations", "source": "Phone",
     "owner": "Lakshmi Prasad", "updated": "2026-09-25", "language": "English",
     "related": ["Villa 24", "Rajesh Enterprises"]},
    {"title": "Villa 7 — Interior material sheet", "type": "Spreadsheet", "category": "documents", "source": "Google Drive",
     "owner": "Arjun Reddy", "updated": "2026-09-22", "language": "English",
     "related": ["Villa 7"]},
    {"title": "Villa 12 — Electrical PO approval request", "type": "Document", "category": "documents", "source": "File Upload",
     "owner": "Priya Sharma", "updated": "2026-09-28", "language": "English",
     "related": ["Villa 12"]},
]

SEARCH_SUGGESTIONS = [
    "Why is Villa 12 delayed?",
    "How much have we spent on steel for Villa 31?",
    "Find all documents related to Hyderabad Steel Traders",
    "Show me everything we know about Anil Kumar",
    "What did the customer ask us yesterday?",
]

AI_ANSWERS = {
    "why is villa 12 delayed?": {
        "question": "Why is Villa 12 delayed?",
        "answer": "Villa 12 is currently 6 days behind schedule. The latest site update indicates the "
                  "fitting team has not reached Block C, even though materials were delivered on time. "
                  "Project manager Lakshmi Prasad has not yet confirmed a revised date.",
        "sources": [
            {"title": "WhatsApp — Anil Kumar, Site Supervisor", "detail": "Telugu voice/text message, 29 Sep 2026",
             "source": "WhatsApp"},
            {"title": "Task — Fitting team delay, Block C", "detail": "Created automatically, status: overdue",
             "source": "Tasks"},
            {"title": "Villa 12 — Project record", "detail": "Health: At risk, 72% complete",
             "source": "Projects"},
        ],
        "related": ["Villa 12", "Anil Kumar", "Lakshmi Prasad"],
        "followups": ["Who is responsible for the fitting team?", "Has this happened before on Villa 12?"],
    },
    "how much have we spent on steel for villa 31?": {
        "question": "How much have we spent on steel for Villa 31?",
        "answer": "₹280,000 is currently outstanding to Hyderabad Steel Traders for Villa 31, against "
                  "Purchase Order #381. Combined with earlier payments on the same PO, total steel spend "
                  "on Villa 31 to date is above the project's budgeted allocation by roughly 11%.",
        "sources": [
            {"title": "Hyderabad Steel Traders — Invoice INV-2291", "detail": "Tally record, 18 Sep 2026", "source": "Tally"},
            {"title": "Purchase Order #381", "detail": "Google Drive, 20 Sep 2026", "source": "Google Drive"},
            {"title": "Villa 31 — Project record", "detail": "Budget vs. spent", "source": "Projects"},
        ],
        "related": ["Villa 31", "Hyderabad Steel Traders"],
        "followups": ["Show the full payment history with Hyderabad Steel Traders", "Is there a cheaper alternative vendor?"],
    },
}

ENTITIES = {
    "anil-kumar": {
        "name": "Anil Kumar",
        "type": "Person — Employee",
        "role": "Site Supervisor",
        "projects": ["Villa 12"],
        "summary": "Site Supervisor on Villa 12 (Block C). Primary contact for daily site updates, "
                    "usually communicates by WhatsApp in Telugu.",
        "related_documents": ["Villa 12 — Site Update, 12 Sep"],
        "related_conversations": ["WhatsApp — Villa 12 Site Group"],
        "related_tasks": ["Fitting team delay — Block C"],
    },
    "hyderabad-steel-traders": {
        "name": "Hyderabad Steel Traders",
        "type": "Company — Vendor",
        "role": "Steel supplier",
        "projects": ["Villa 31"],
        "summary": "Steel vendor for Villa 31. ₹280,000 currently outstanding against Invoice INV-2291. "
                    "Recent delivery delay flagged by the project manager.",
        "related_documents": ["ABC Villa 31 — Steel Purchase Order #381", "Hyderabad Steel Traders — Invoice INV-2291"],
        "related_conversations": ["Re: Steel delivery delay (email)"],
        "related_tasks": ["Review steel delivery delay"],
    },
}

KNOWLEDGE_GAPS = [
    {"question": "What is our standard retention policy for site photos?", "times_asked": 6, "confidence": "No source found"},
    {"question": "What are the payment terms with new vendors?", "times_asked": 4, "confidence": "Conflicting — 2 sources disagree"},
]

# ===================== Ingestion =====================

INGESTION_STAGES = ["Fetch", "Parse", "OCR / Transcribe", "Classify", "Extract", "Chunk", "Embed", "Index", "Entity Resolution", "Knowledge Graph", "Ready"]

INGESTION_QUEUE = [
    {"item": "Villa 24 — Client progress call, 25 Sep.mp3", "source": "Phone", "type": "Audio", "stage": "Transcribe", "progress": 60, "started": "2 min ago", "status": "processing"},
    {"item": "Electrical PO approval request.pdf", "source": "File Upload", "type": "Document", "stage": "OCR", "progress": 35, "started": "1 min ago", "status": "processing"},
    {"item": "GRN-118.xml", "source": "Tally", "type": "Record", "stage": "Fetch", "progress": 10, "started": "4 min ago", "status": "processing"},
    {"item": "Hyderabad Steel Traders — Invoice INV-2291.pdf", "source": "Tally", "type": "Invoice", "stage": "Ready", "progress": 100, "started": "18 Sep", "status": "completed"},
    {"item": "Villa 12 — Site Update, 12 Sep", "source": "WhatsApp", "type": "Message", "stage": "Ready", "progress": 100, "started": "29 Sep", "status": "completed"},
    {"item": "Ledger export — Sep.xlsx", "source": "Tally", "type": "Spreadsheet", "stage": "Fetch", "progress": 0, "started": "—", "status": "failed"},
]

# ===================== Collections =====================

COLLECTIONS = [
    {"name": "Hyderabad Villa Projects", "icon": "🏠", "rule": "Project type = Construction, Location = Hyderabad", "item_count": 2841},
    {"name": "Finance", "icon": "💰", "rule": "Source = Tally OR Type = Invoice", "item_count": 3821},
    {"name": "Vendor Contracts", "icon": "📄", "rule": "Type = Contract, Entity type = Vendor", "item_count": 47},
    {"name": "Client ABC — Villa 31", "icon": "👤", "rule": "Manual additions", "item_count": 18},
]

# ===================== Data Quality =====================

DATA_QUALITY = {
    "duplicate_content": 14,
    "conflicting_information": 1,
    "stale_content": 23,
    "missing_metadata": 31,
    "unknown_owner": 6,
    "permission_mismatch": 2,
    "low_quality_ocr": 9,
    "low_confidence_extraction": 12,
    "unmapped_identity": 7,
}

DATA_CONFLICTS = [
    {
        "topic": "Villa 7 handover date",
        "doc_a": {"title": "Project Schedule — Villa 7 (Google Drive)", "value": "30 September 2026"},
        "doc_b": {"title": "WhatsApp — Srinivas Reddy, 20 Sep", "value": "15 October 2026"},
    }
]

STALE_ITEMS = [
    {"title": "Vendor rate card — 2025", "owner": "Priya Sharma", "last_updated": "2026-01-14", "age": "8+ months"},
    {"title": "HR leave policy v2", "owner": "Sunitha Devi", "last_updated": "2025-11-02", "age": "10+ months"},
]

# ===================== Security =====================

AI_SOURCE_POLICY = [
    {"source": "Google Drive", "can_search": True, "can_summarize": True, "sensitive": False},
    {"source": "WhatsApp", "can_search": True, "can_summarize": True, "sensitive": False},
    {"source": "Gmail", "can_search": True, "can_summarize": True, "sensitive": False},
    {"source": "Tally — Finance records", "can_search": True, "can_summarize": False, "sensitive": True},
    {"source": "HR documents", "can_search": False, "can_summarize": False, "sensitive": True},
]

IDENTITY_MAPPING = [
    {"source_identity": "ravi.kumar@gmail.com", "business_identity": "Ravi Kumar", "status": "Mapped"},
    {"source_identity": "+91 98xxxxx214 (WhatsApp)", "business_identity": "Anil Kumar", "status": "Mapped"},
    {"source_identity": "steel.traders.hyd@gmail.com", "business_identity": "Hyderabad Steel Traders", "status": "Mapped"},
    {"source_identity": "+91 90xxxxx071 (WhatsApp)", "business_identity": "—", "status": "Unmapped"},
]

# ===================== Capture / Upload =====================

CAPTURE_METHODS = [
    {"id": "file", "label": "Upload File", "desc": "PDF, Word, Excel, PowerPoint, images"},
    {"id": "photo", "label": "Take Photo", "desc": "Invoice, bill, or site photo"},
    {"id": "voice", "label": "Record Voice", "desc": "Speak in English, Telugu, or Hindi"},
    {"id": "audio", "label": "Upload Audio", "desc": "A call recording or voice note"},
    {"id": "video", "label": "Upload Video", "desc": "Site walkthrough or meeting recording"},
    {"id": "text", "label": "Paste Text", "desc": "Notes, a message, anything typed"},
    {"id": "url", "label": "Paste URL", "desc": "A webpage to index"},
    {"id": "excel", "label": "Import Excel", "desc": "A spreadsheet with structured data"},
]

PROCESSING_STAGES = ["Uploading", "Reading", "Understanding", "Extracting information", "Connecting to business records", "Indexing", "Ready"]

CLASSIFICATION_OPTIONS = [
    "General business knowledge", "Customer information", "Project", "Vendor",
    "Finance", "HR", "Legal", "Operations", "Product", "Other",
]

# ===================== Connector setup wizard =====================

CONNECTOR_CONTENT_TREE = {
    "include": ["/Projects", "/Contracts", "/Finance"],
    "exclude": ["/Personal", "/Archive"],
}

CONNECTOR_SYNC_OPTIONS = ["Real-time", "Every 15 minutes", "Hourly", "Daily", "Manual"]
CONNECTOR_PERMISSION_MODES = [
    {"label": "Mirror source permissions", "desc": "If someone can't see it in the source system, they can't see it here either."},
    {"label": "Everyone in company", "desc": "All employees can search this source, regardless of source-level access."},
    {"label": "Selected users/groups", "desc": "Choose exactly who can search this source."},
]
CONNECTOR_SCOPE_OPTIONS = ["Entire source", "Selected folders", "Shared drives / team spaces", "Specific folders only"]
CONNECTOR_CONTENT_TYPES = ["Documents", "Spreadsheets", "Presentations", "Comments", "Shared files"]

# ===================== Notifications =====================

NOTIFICATIONS = [
    {"text": "Tally sync failed — authentication expired", "time": "9:02 AM", "kind": "alert"},
    {"text": "Villa 7 handover date — conflicting information detected", "time": "Yesterday", "kind": "alert"},
    {"text": "Knowledge gap: \"payment terms with new vendors\" asked 4 times, no source found", "time": "2 days ago", "kind": "warn"},
    {"text": "Google Drive sync completed — 14 new items indexed", "time": "4 min ago", "kind": "info"},
]

# ===================== Audit =====================

AUDIT_EVENTS = [
    {"actor": "Ravi Kumar", "kind": "Human", "action": "Connected", "object": "Tally", "timestamp": "2026-09-15 10:02"},
    {"actor": "AI Assistant", "kind": "AI", "action": "Answered question", "object": "\"Why is Villa 12 delayed?\"", "timestamp": "2026-09-29 09:41"},
    {"actor": "Priya Sharma", "kind": "Human", "action": "Uploaded document", "object": "Electrical PO approval request.pdf", "timestamp": "2026-09-28 16:20"},
    {"actor": "System", "kind": "AI", "action": "Sync failed", "object": "Ledger export — Sep.xlsx (Tally)", "timestamp": "2026-09-30 09:02"},
    {"actor": "Sunitha Devi", "kind": "Human", "action": "Viewed", "object": "Anil Kumar — entity profile", "timestamp": "2026-09-30 11:15"},
]
