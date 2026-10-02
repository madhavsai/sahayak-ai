"""Sample data for the Sahayak AI app shell - UI only, no real database.

Matches the demo scenario from VISION.md: Hyderabad Luxury Villas Pvt Ltd,
12 employees, 5 projects (3 active), 8 customers, 25 vendors,
English + Telugu + Hindi.
"""

ORG = {
    "name": "Hyderabad Luxury Villas Pvt Ltd",
    "industry": "Construction",
    "city": "Hyderabad",
    "state": "Telangana",
    "employees": 12,
    "languages": ["English", "Telugu", "Hindi"],
    "channels": ["WhatsApp", "Phone", "Email"],
}

CURRENT_USER = {"name": "Ravi Kumar", "role": "Owner"}

EMPLOYEES = [
    {"name": "Ravi Kumar", "role": "Owner"},
    {"name": "Lakshmi Prasad", "role": "Project Manager", "projects": ["Villa 12", "Villa 24"]},
    {"name": "Srinivas Reddy", "role": "Project Manager", "projects": ["Villa 7", "Villa 31"]},
    {"name": "Anil Kumar", "role": "Site Supervisor", "projects": ["Villa 12"]},
    {"name": "Venkat Rao", "role": "Site Supervisor", "projects": ["Villa 31"]},
    {"name": "Priya Sharma", "role": "Procurement Manager"},
    {"name": "Kiran Rao", "role": "Finance"},
    {"name": "Deepika Nair", "role": "Sales / CRM"},
    {"name": "Sunitha Devi", "role": "HR / Admin"},
    {"name": "Arjun Reddy", "role": "Site Engineer", "projects": ["Villa 7"]},
    {"name": "Ramesh Yadav", "role": "Labour Coordinator"},
    {"name": "Mohammed Irfan", "role": "Site Supervisor", "projects": ["Villa 24"]},
]

PROJECTS = [
    {
        "id": "villa-12",
        "name": "Villa 12",
        "location": "Kokapet, Hyderabad",
        "client": "Mr. & Mrs. Chandrasekhar",
        "manager": "Lakshmi Prasad",
        "progress": 72,
        "budget": 18500000,
        "spent": 14200000,
        "pending_payment": 420000,
        "deadline": "2026-12-15",
        "health": "At risk",
        "health_note": "6 days behind schedule — fitting team delay in Block C",
        "milestones": [
            {"name": "Foundation", "status": "done"},
            {"name": "Structure", "status": "done"},
            {"name": "Electrical", "status": "done"},
            {"name": "Plumbing", "status": "in_progress"},
            {"name": "Interior", "status": "pending"},
            {"name": "Finishing", "status": "pending"},
        ],
        "active": True,
    },
    {
        "id": "villa-24",
        "name": "Villa 24",
        "location": "Jubilee Hills, Hyderabad",
        "client": "Rajesh Enterprises",
        "manager": "Lakshmi Prasad",
        "progress": 45,
        "budget": 24000000,
        "spent": 10600000,
        "pending_payment": 0,
        "deadline": "2027-03-01",
        "health": "On track",
        "health_note": "No open issues",
        "milestones": [
            {"name": "Foundation", "status": "done"},
            {"name": "Structure", "status": "in_progress"},
            {"name": "Electrical", "status": "pending"},
            {"name": "Plumbing", "status": "pending"},
            {"name": "Interior", "status": "pending"},
            {"name": "Finishing", "status": "pending"},
        ],
        "active": True,
    },
    {
        "id": "villa-31",
        "name": "Villa 31",
        "location": "Financial District, Hyderabad",
        "client": "Mr. Suresh Babu",
        "manager": "Srinivas Reddy",
        "progress": 28,
        "budget": 21000000,
        "spent": 7100000,
        "pending_payment": 350000,
        "deadline": "2027-05-20",
        "health": "Delayed",
        "health_note": "Steel purchases 11% above project budget; vendor delivery late",
        "milestones": [
            {"name": "Foundation", "status": "done"},
            {"name": "Structure", "status": "in_progress"},
            {"name": "Electrical", "status": "pending"},
            {"name": "Plumbing", "status": "pending"},
            {"name": "Interior", "status": "pending"},
            {"name": "Finishing", "status": "pending"},
        ],
        "active": True,
    },
    {
        "id": "villa-7",
        "name": "Villa 7",
        "location": "Gachibowli, Hyderabad",
        "client": "Mrs. Padmavathi",
        "manager": "Srinivas Reddy",
        "progress": 90,
        "budget": 16800000,
        "spent": 15900000,
        "pending_payment": 180000,
        "deadline": "2026-11-01",
        "health": "On track",
        "health_note": "Nearing handover",
        "milestones": [
            {"name": "Foundation", "status": "done"},
            {"name": "Structure", "status": "done"},
            {"name": "Electrical", "status": "done"},
            {"name": "Plumbing", "status": "done"},
            {"name": "Interior", "status": "in_progress"},
            {"name": "Finishing", "status": "pending"},
        ],
        "active": False,
    },
    {
        "id": "villa-18",
        "name": "Villa 18",
        "location": "Kompally, Hyderabad",
        "client": "Mrs. Anitha Reddy",
        "manager": "Lakshmi Prasad",
        "progress": 100,
        "budget": 15200000,
        "spent": 15050000,
        "pending_payment": 0,
        "deadline": "2026-06-10",
        "health": "Completed",
        "health_note": "Handed over 2026-06-08",
        "milestones": [{"name": m, "status": "done"} for m in
                        ["Foundation", "Structure", "Electrical", "Plumbing", "Interior", "Finishing"]],
        "active": False,
    },
]

CUSTOMERS = [
    {"name": "Mr. & Mrs. Chandrasekhar", "project": "Villa 12", "outstanding": 420000, "status": "Active"},
    {"name": "Rajesh Enterprises", "project": "Villa 24", "outstanding": 0, "status": "Active"},
    {"name": "Mr. Suresh Babu", "project": "Villa 31", "outstanding": 350000, "status": "Active"},
    {"name": "Mrs. Padmavathi", "project": "Villa 7", "outstanding": 180000, "status": "Active"},
    {"name": "Mrs. Anitha Reddy", "project": "Villa 18", "outstanding": 0, "status": "Completed"},
    {"name": "Mr. Vikram Singh", "project": None, "outstanding": 0, "status": "Past client"},
    {"name": "Mrs. Kavitha Rao", "project": None, "outstanding": 0, "status": "Inquiry"},
    {"name": "Mr. Naveen Chowdary", "project": None, "outstanding": 0, "status": "Inquiry"},
]

LEADS = [
    {"name": "Mr. Harish Gupta", "source": "WhatsApp inquiry", "interest": "Kokapet villa", "stage": "Qualification", "owner": "Deepika Nair"},
    {"name": "Mrs. Sowmya Reddy", "source": "Referral — Mrs. Padmavathi", "interest": "Gachibowli villa", "stage": "Site visit scheduled", "owner": "Deepika Nair"},
    {"name": "Mr. Rajendra Prasad", "source": "Inbound call", "interest": "Financial District villa", "stage": "New", "owner": "Deepika Nair"},
]

VENDORS = [
    {"name": "Hyderabad Steel Traders", "category": "Steel", "outstanding": 280000},
    {"name": "Deccan Steel Corp", "category": "Steel", "outstanding": 0},
    {"name": "Ramco Cement Dealers", "category": "Cement", "outstanding": 95000},
    {"name": "ACC Authorized Dealer — Secunderabad", "category": "Cement", "outstanding": 0},
    {"name": "Bright Electricals", "category": "Electrical", "outstanding": 42000},
    {"name": "PowerLine Hyderabad", "category": "Electrical", "outstanding": 0},
    {"name": "AquaFlow Plumbing Solutions", "category": "Plumbing", "outstanding": 18000},
    {"name": "ModernPipe Traders", "category": "Plumbing", "outstanding": 0},
    {"name": "Urban Interiors Hyderabad", "category": "Interiors", "outstanding": 0},
    {"name": "Elegant Wood Works", "category": "Interiors", "outstanding": 65000},
    {"name": "Reddy Labour Contractors", "category": "Labour", "outstanding": 0},
    {"name": "Telangana Mazdoor Seva", "category": "Labour", "outstanding": 0},
    {"name": "Kajaria Tiles Dealer — Gachibowli", "category": "Flooring", "outstanding": 0},
    {"name": "Marble Palace", "category": "Flooring", "outstanding": 120000},
    {"name": "Asian Paints Authorized Dealer", "category": "Paint", "outstanding": 0},
    {"name": "ColorMax Hyderabad", "category": "Paint", "outstanding": 0},
    {"name": "Saint-Gobain Glass Partner", "category": "Glass & Aluminium", "outstanding": 0},
    {"name": "AluTech Fabricators", "category": "Glass & Aluminium", "outstanding": 38000},
    {"name": "Hettich Hardware Store", "category": "Hardware", "outstanding": 0},
    {"name": "BuildMart Hardware", "category": "Hardware", "outstanding": 0},
    {"name": "Jaquar Showroom — Banjara Hills", "category": "Sanitaryware", "outstanding": 0},
    {"name": "CeraStyle Bath Fittings", "category": "Sanitaryware", "outstanding": 0},
    {"name": "GreenScape Landscaping", "category": "Landscaping", "outstanding": 0},
    {"name": "Dr. Fixit Applicators", "category": "Waterproofing", "outstanding": 0},
    {"name": "Deccan Carriers", "category": "Transport & Logistics", "outstanding": 15000},
]

TASKS = [
    {"title": "Fitting team delay — Block C", "project": "Villa 12", "owner": "Anil Kumar", "due": "2026-09-29", "status": "overdue", "priority": "High"},
    {"title": "Review steel delivery delay", "project": "Villa 31", "owner": "Srinivas Reddy", "due": "2026-09-30", "status": "overdue", "priority": "High"},
    {"title": "Follow up payment — Mr. Suresh Babu", "project": "Villa 31", "owner": "Kiran Rao", "due": "2026-09-28", "status": "overdue", "priority": "High"},
    {"title": "Approve electrical PO", "project": "Villa 12", "owner": "Priya Sharma", "due": "2026-10-02", "status": "pending", "priority": "Medium"},
    {"title": "Client progress update", "project": "Villa 24", "owner": "Lakshmi Prasad", "due": "2026-10-02", "status": "pending", "priority": "Medium"},
    {"title": "Confirm site visit — Mr. Harish Gupta", "project": None, "owner": "Deepika Nair", "due": "2026-10-01", "status": "pending", "priority": "Medium"},
    {"title": "Interior material selection — Villa 7", "project": "Villa 7", "owner": "Arjun Reddy", "due": "2026-10-05", "status": "pending", "priority": "Low"},
    {"title": "Handover documentation — Villa 7", "project": "Villa 7", "owner": "Srinivas Reddy", "due": "2026-10-20", "status": "pending", "priority": "Medium"},
]

AI_INSIGHTS = [
    "Villa 12 is 6 days behind schedule — fitting team hasn't reached Block C.",
    "₹8.4 lakh is overdue from 3 customers.",
    "Steel purchases on Villa 31 are 11% above the project budget.",
    "Hyderabad Steel Traders has not delivered the expected material for Villa 31.",
]

RECENT_CONVERSATIONS = [
    {"contact": "Site Supervisor — Anil Kumar", "channel": "WhatsApp", "project": "Villa 12",
     "language": "Telugu", "preview": "Sir material vachindi, kaani fitting team inka site ki raledu", "status": "Flagged"},
    {"contact": "Mrs. Padmavathi", "channel": "Call", "project": "Villa 7",
     "language": "English", "preview": "Asked about interior finishing timeline", "status": "Answered"},
    {"contact": "Hyderabad Steel Traders", "channel": "Email", "project": "Villa 31",
     "language": "English", "preview": "Delivery delay notice for structural steel", "status": "Needs review"},
    {"contact": "Mr. Harish Gupta", "channel": "WhatsApp", "project": None,
     "language": "Hindi", "preview": "Kokapet wali villa ka rate kya hai?", "status": "New"},
]


def business_health():
    active = [p for p in PROJECTS if p["active"]]
    receivables = sum(c["outstanding"] for c in CUSTOMERS)
    payables = sum(v["outstanding"] for v in VENDORS)
    return {
        "revenue_ytd": 47600000,
        "receivables": receivables,
        "payables": payables,
        "active_projects": len(active),
        "leads": len(LEADS),
        "open_tickets": len([t for t in TASKS if t["status"] in ("overdue", "pending")]),
        "cash_position": 8900000,
    }


def overdue_tasks():
    return [t for t in TASKS if t["status"] == "overdue"]


def project_by_id(project_id: str):
    return next((p for p in PROJECTS if p["id"] == project_id), None)


def tasks_for_project(name: str):
    return [t for t in TASKS if t["project"] == name]
