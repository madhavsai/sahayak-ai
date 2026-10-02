"""Sample data for Procurement, Finance, and People - UI only.

Cross-references app/seed_data.py (Villa 12/24/31, vendors, employees) so this
reads as one connected business, not disconnected demo modules.
"""

# ===================== Procurement =====================

PROCUREMENT_METRICS = {
    "purchase_requests": 9,
    "pending_approval": 3,
    "open_rfqs": 2,
    "purchase_orders": 14,
    "awaiting_delivery": 4,
    "bills_pending": 3,
    "overdue_payments": 280000,
}

PROCUREMENT_ALERTS = [
    "Steel requirement for Villa 31 has not been fully ordered.",
    "PO-421 delivery is overdue by 4 days.",
    "Hyderabad Steel Traders increased cement prices by 8% this month.",
    "₹2.8 lakh in vendor bills are awaiting approval.",
    "Villa 12 has a material requirement due this week (fitting hardware).",
]

PROCUREMENT_PIPELINE = [
    {"stage": "Request", "count": 9, "value": 640000},
    {"stage": "Approval", "count": 3, "value": 210000},
    {"stage": "RFQ", "count": 2, "value": 180000},
    {"stage": "Purchase Order", "count": 14, "value": 2840000},
    {"stage": "Delivery", "count": 4, "value": 410000},
    {"stage": "Bill", "count": 3, "value": 280000},
]

PURCHASE_REQUESTS = [
    {"id": "PR-000421", "material": "Cement (OPC 53)", "quantity": "200 bags", "project": "Villa 31",
     "requester": "Srinivas Reddy", "required_date": "2026-10-05", "estimated_cost": 112000,
     "status": "Pending Approval", "reason": "Foundation pour scheduled next week, current stock insufficient."},
    {"id": "PR-000419", "material": "Electrical fittings — premium switches", "quantity": "1 lot", "project": "Villa 12",
     "requester": "Anil Kumar", "required_date": "2026-10-03", "estimated_cost": 64000,
     "status": "Approved", "reason": "Interior fitting phase starting after plumbing clears."},
    {"id": "PR-000415", "material": "Steel reinforcement bars (12mm)", "quantity": "4 tons", "project": "Villa 31",
     "requester": "Srinivas Reddy", "required_date": "2026-09-29", "estimated_cost": 268000,
     "status": "Converted to PO", "reason": "Structure phase — matches approved BOQ."},
    {"id": "PR-000410", "material": "Interior wood — teak panels", "quantity": "1 lot", "project": "Villa 7",
     "requester": "Arjun Reddy", "required_date": "2026-10-08", "estimated_cost": 185000,
     "status": "Pending Approval", "reason": "Interior finishing selection approved by client."},
]

PURCHASE_ORDERS = [
    {"id": "PO-421", "vendor": "Hyderabad Steel Traders", "project": "Villa 31", "amount": 268000,
     "status": "Awaiting Delivery", "expected_delivery": "2026-09-26", "items": "Steel reinforcement bars (12mm) — 4 tons",
     "overdue": True},
    {"id": "PO-418", "vendor": "Bright Electricals", "project": "Villa 12", "amount": 64000,
     "status": "Delivered", "expected_delivery": "2026-09-27", "items": "Premium switches — 1 lot", "overdue": False},
    {"id": "PO-412", "vendor": "Ramco Cement Dealers", "project": "Villa 24", "amount": 95000,
     "status": "Partially Delivered", "expected_delivery": "2026-09-30", "items": "Cement (OPC 53) — 150 bags", "overdue": False},
    {"id": "PO-405", "vendor": "Elegant Wood Works", "project": "Villa 7", "amount": 185000,
     "status": "Draft", "expected_delivery": "2026-10-08", "items": "Teak panels — 1 lot", "overdue": False},
]

GOODS_RECEIPT_DEMO_PO = {
    "id": "PO-412", "vendor": "Ramco Cement Dealers", "project": "Villa 24",
    "material": "Cement (OPC 53)", "ordered_quantity": "150 bags", "ordered_quantity_num": 150,
}

PROCUREMENT_BILLS = [
    {"bill": "INV-2291", "vendor": "Hyderabad Steel Traders", "po": "PO-421", "project": "Villa 31",
     "po_amount": 268000, "grn_amount": 268000, "bill_amount": 268000, "match_status": "Matched"},
    {"bill": "INV-1187", "vendor": "Ramco Cement Dealers", "po": "PO-412", "project": "Villa 24",
     "po_amount": 95000, "grn_amount": 85500, "bill_amount": 95000, "match_status": "Mismatch"},
    {"bill": "INV-0892", "vendor": "Bright Electricals", "po": "PO-418", "project": "Villa 12",
     "po_amount": 64000, "grn_amount": 64000, "bill_amount": 64000, "match_status": "Matched"},
]

# ===================== Finance =====================

FINANCE_METRICS = {
    "revenue_ytd": 47600000,
    "receivables": 950000,
    "payables": 575000,
    "cash_position": 8900000,
    "overdue_receivables": 420000,
    "upcoming_payments": 268000,
    "monthly_expenses": 310000,
}

FINANCE_ALERTS = [
    "₹4.2 lakh is overdue from 3 customers.",
    "₹2.68 lakh vendor payment (PO-421) is due this week.",
    "Villa 31 is 11% over its procurement budget.",
    "Monthly expenses increased 9% versus last month.",
]

CASH_FLOW = {
    "opening_balance": 8900000,
    "expected_receipts_30d": 1500000,
    "expected_payments_30d": 843000,
}

INVOICES = [
    {"id": "INV-S-3301", "customer": "Mr. & Mrs. Chandrasekhar", "project": "Villa 12", "amount": 1200000,
     "paid": 780000, "due_date": "2026-10-10", "status": "Partially Paid"},
    {"id": "INV-S-3298", "customer": "Rajesh Enterprises", "project": "Villa 24", "amount": 2000000,
     "paid": 2000000, "due_date": "2026-09-15", "status": "Paid"},
    {"id": "INV-S-3290", "customer": "Mr. Suresh Babu", "project": "Villa 31", "amount": 950000,
     "paid": 600000, "due_date": "2026-09-20", "status": "Overdue"},
    {"id": "INV-S-3285", "customer": "Mrs. Padmavathi", "project": "Villa 7", "amount": 400000,
     "paid": 220000, "due_date": "2026-09-25", "status": "Overdue"},
]

RECEIVABLES_AGING = [
    {"bucket": "Current", "amount": 420000},
    {"bucket": "1-30 days", "amount": 350000},
    {"bucket": "31-60 days", "amount": 180000},
    {"bucket": "61-90 days", "amount": 0},
    {"bucket": "90+ days", "amount": 0},
]

COLLECTION_ITEMS = [
    {"customer": "Mr. Suresh Babu", "invoice": "INV-S-3290", "amount": 350000, "days_overdue": 10,
     "last_contact": "WhatsApp, 2026-09-28",
     "promise": "Said payment would follow after milestone sign-off.",
     "suggested_action": "Send a polite follow-up referencing the milestone approval."},
    {"customer": "Mrs. Padmavathi", "invoice": "INV-S-3285", "amount": 180000, "days_overdue": 5,
     "last_contact": "Call, 2026-09-26",
     "promise": "No commitment given yet.",
     "suggested_action": "Call to confirm a payment date."},
]

PAYABLES = [
    {"vendor": "Hyderabad Steel Traders", "bill": "INV-2291", "project": "Villa 31", "amount": 268000, "due_date": "2026-10-03", "status": "Due this week"},
    {"vendor": "Ramco Cement Dealers", "bill": "INV-1187", "project": "Villa 24", "amount": 95000, "due_date": "2026-10-08", "status": "Due this month"},
    {"vendor": "Elegant Wood Works", "bill": "INV-0750", "project": "Villa 7", "amount": 65000, "due_date": "2026-09-25", "status": "Overdue"},
]

EXPENSES = [
    {"employee": "Anil Kumar", "category": "Transport", "project": "Villa 12", "amount": 850, "date": "2026-09-29", "status": "Pending Approval"},
    {"employee": "Srinivas Reddy", "category": "Site materials (petty)", "project": "Villa 31", "amount": 2400, "date": "2026-09-27", "status": "Approved"},
]

def project_finance(project):
    """Derive committed/forecast finance figures for a project from its budget/spend and open POs."""
    committed_pos = sum(po["amount"] for po in PURCHASE_ORDERS if po["project"] == project["name"])
    committed = project["spent"] + committed_pos
    overrun_factor = 1.08 if project["health"] in ("At risk", "Delayed") else 1.0
    forecast = round(committed * overrun_factor)
    return {
        "contract_value": round(project["budget"] * 1.25),
        "revenue_received": project["budget"] - project["pending_payment"] - round(project["budget"] * 0.15),
        "outstanding": project["pending_payment"] + round(project["budget"] * 0.15),
        "budget": project["budget"],
        "committed": committed,
        "actual": project["spent"],
        "forecast": forecast,
        "variance": forecast - project["budget"],
    }

# ===================== People =====================

PEOPLE_METRICS = {
    "employees": 12,
    "active": 11,
    "on_leave": 1,
    "open_tasks": 8,
    "overdue_tasks": 3,
    "projects": 5,
    "pending_approvals": 4,
}

EMPLOYEE_DETAIL = {
    "Ravi Kumar": {"department": "Leadership", "manager": "—", "status": "Active", "location": "Head Office",
                   "open_tasks": 0, "contact": "ravi.kumar@hyderabadluxuryvillas.in"},
    "Lakshmi Prasad": {"department": "Projects", "manager": "Ravi Kumar", "status": "Active", "location": "Site — rotating",
                        "open_tasks": 2, "contact": "lakshmi.prasad@hyderabadluxuryvillas.in"},
    "Srinivas Reddy": {"department": "Projects", "manager": "Ravi Kumar", "status": "Active", "location": "Site — Villa 31",
                        "open_tasks": 3, "contact": "srinivas.reddy@hyderabadluxuryvillas.in"},
    "Anil Kumar": {"department": "Site Operations", "manager": "Lakshmi Prasad", "status": "Active", "location": "Site — Villa 12",
                   "open_tasks": 2, "contact": "anil.kumar@hyderabadluxuryvillas.in"},
    "Venkat Rao": {"department": "Site Operations", "manager": "Srinivas Reddy", "status": "Active", "location": "Site — Villa 31",
                   "open_tasks": 1, "contact": "venkat.rao@hyderabadluxuryvillas.in"},
    "Priya Sharma": {"department": "Procurement", "manager": "Ravi Kumar", "status": "Active", "location": "Head Office",
                     "open_tasks": 2, "contact": "priya.sharma@hyderabadluxuryvillas.in"},
    "Kiran Rao": {"department": "Finance", "manager": "Ravi Kumar", "status": "Active", "location": "Head Office",
                  "open_tasks": 1, "contact": "kiran.rao@hyderabadluxuryvillas.in"},
    "Deepika Nair": {"department": "Sales", "manager": "Ravi Kumar", "status": "Active", "location": "Head Office",
                     "open_tasks": 1, "contact": "deepika.nair@hyderabadluxuryvillas.in"},
    "Sunitha Devi": {"department": "HR / Admin", "manager": "Ravi Kumar", "status": "On Leave", "location": "Head Office",
                     "open_tasks": 0, "contact": "sunitha.devi@hyderabadluxuryvillas.in"},
    "Arjun Reddy": {"department": "Projects", "manager": "Srinivas Reddy", "status": "Active", "location": "Site — Villa 7",
                    "open_tasks": 1, "contact": "arjun.reddy@hyderabadluxuryvillas.in"},
    "Ramesh Yadav": {"department": "Site Operations", "manager": "Lakshmi Prasad", "status": "Active", "location": "Site — rotating",
                     "open_tasks": 0, "contact": "ramesh.yadav@hyderabadluxuryvillas.in"},
    "Mohammed Irfan": {"department": "Site Operations", "manager": "Lakshmi Prasad", "status": "Active", "location": "Site — Villa 24",
                       "open_tasks": 1, "contact": "mohammed.irfan@hyderabadluxuryvillas.in"},
}

LEAVE_REQUESTS = [
    {"employee": "Sunitha Devi", "type": "Sick Leave", "start": "2026-09-29", "end": "2026-10-02",
     "status": "Approved", "manager": "Ravi Kumar"},
    {"employee": "Arjun Reddy", "type": "Casual Leave", "start": "2026-10-10", "end": "2026-10-11",
     "status": "Pending", "manager": "Srinivas Reddy"},
]

# ===================== Unified Approval Center =====================

def get_approvals():
    """Pull pending items from across the three domains into one list."""
    approvals = []
    for pr in PURCHASE_REQUESTS:
        if pr["status"] == "Pending Approval":
            approvals.append({
                "kind": "Purchase Request", "title": f"{pr['id']} — {pr['material']}",
                "amount": pr["estimated_cost"], "context": pr["project"], "requester": pr["requester"],
                "link": f"/app/procurement/requests/{pr['id']}",
            })
    for pay in PAYABLES:
        if pay["status"] == "Overdue":
            approvals.append({
                "kind": "Vendor Payment", "title": f"{pay['bill']} — {pay['vendor']}",
                "amount": pay["amount"], "context": pay["project"], "requester": "Finance",
                "link": "/app/finance/payables",
            })
    for exp in EXPENSES:
        if exp["status"] == "Pending Approval":
            approvals.append({
                "kind": "Employee Expense", "title": f"{exp['category']} — {exp['employee']}",
                "amount": exp["amount"], "context": exp["project"], "requester": exp["employee"],
                "link": "/app/people/employees",
            })
    for lv in LEAVE_REQUESTS:
        if lv["status"] == "Pending":
            approvals.append({
                "kind": "Leave Request", "title": f"{lv['type']} — {lv['employee']}",
                "amount": None, "context": f"{lv['start']} to {lv['end']}", "requester": lv["employee"],
                "link": "/app/people/leave",
            })
    return approvals
