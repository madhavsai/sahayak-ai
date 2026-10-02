"""Routes for Procurement, Finance, and People - UI only, seeded data."""
from pathlib import Path

from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app import ops_seed, seed_data

BASE_DIR = Path(__file__).parent.parent
templates = Jinja2Templates(directory=BASE_DIR / "templates")

router = APIRouter(prefix="/app")


def _enriched_employees():
    out = []
    for e in seed_data.EMPLOYEES:
        detail = ops_seed.EMPLOYEE_DETAIL.get(e["name"], {})
        out.append({**e, "detail": detail})
    return out


# ===================== Procurement =====================

@router.get("/procurement", response_class=HTMLResponse)
def procurement_overview(request: Request):
    return templates.TemplateResponse(
        "procurement_overview.html",
        {
            "request": request, "active": "procurement",
            "m": ops_seed.PROCUREMENT_METRICS, "alerts": ops_seed.PROCUREMENT_ALERTS,
            "pipeline": ops_seed.PROCUREMENT_PIPELINE,
        },
    )


@router.get("/procurement/requests", response_class=HTMLResponse)
def procurement_requests(request: Request):
    return templates.TemplateResponse(
        "procurement_requests.html",
        {"request": request, "active": "procurement", "requests": ops_seed.PURCHASE_REQUESTS},
    )


@router.get("/procurement/requests/{pr_id}", response_class=HTMLResponse)
def procurement_request_detail(request: Request, pr_id: str):
    pr = next((p for p in ops_seed.PURCHASE_REQUESTS if p["id"] == pr_id), None)
    if not pr:
        raise HTTPException(status_code=404, detail="Purchase request not found")
    project = next((p for p in seed_data.PROJECTS if p["name"] == pr["project"]), None)
    budget_remaining = (project["budget"] - project["spent"]) if project else 0
    suggested_vendors = [v["name"] for v in seed_data.VENDORS[:3]]
    return templates.TemplateResponse(
        "procurement_request_detail.html",
        {
            "request": request, "active": "procurement", "pr": pr,
            "budget_remaining": budget_remaining,
            "suggested_vendors": suggested_vendors,
        },
    )


@router.get("/procurement/orders", response_class=HTMLResponse)
def procurement_orders(request: Request):
    return templates.TemplateResponse(
        "procurement_orders.html",
        {"request": request, "active": "procurement", "orders": ops_seed.PURCHASE_ORDERS},
    )


@router.get("/procurement/orders/{po_id}", response_class=HTMLResponse)
def procurement_order_detail(request: Request, po_id: str):
    po = next((p for p in ops_seed.PURCHASE_ORDERS if p["id"] == po_id), None)
    if not po:
        raise HTTPException(status_code=404, detail="Purchase order not found")
    return templates.TemplateResponse(
        "procurement_order_detail.html", {"request": request, "active": "procurement", "po": po}
    )


@router.get("/procurement/goods-receipt", response_class=HTMLResponse)
def procurement_goods_receipt(request: Request):
    return templates.TemplateResponse(
        "procurement_goods_receipt.html",
        {"request": request, "active": "procurement", "po": ops_seed.GOODS_RECEIPT_DEMO_PO},
    )


@router.get("/procurement/bills", response_class=HTMLResponse)
def procurement_bills(request: Request):
    return templates.TemplateResponse(
        "procurement_bills.html", {"request": request, "active": "procurement", "bills": ops_seed.PROCUREMENT_BILLS}
    )


# ===================== Finance =====================

@router.get("/finance", response_class=HTMLResponse)
def finance_overview(request: Request):
    return templates.TemplateResponse(
        "finance_overview.html",
        {
            "request": request, "active": "finance",
            "m": ops_seed.FINANCE_METRICS, "alerts": ops_seed.FINANCE_ALERTS, "cash": ops_seed.CASH_FLOW,
        },
    )


@router.get("/finance/invoices", response_class=HTMLResponse)
def finance_invoices(request: Request):
    return templates.TemplateResponse(
        "finance_invoices.html", {"request": request, "active": "finance", "invoices": ops_seed.INVOICES}
    )


@router.get("/finance/invoices/{inv_id}", response_class=HTMLResponse)
def finance_invoice_detail(request: Request, inv_id: str):
    inv = next((i for i in ops_seed.INVOICES if i["id"] == inv_id), None)
    if not inv:
        raise HTTPException(status_code=404, detail="Invoice not found")
    return templates.TemplateResponse(
        "finance_invoice_detail.html", {"request": request, "active": "finance", "inv": inv}
    )


@router.get("/finance/receivables", response_class=HTMLResponse)
def finance_receivables(request: Request):
    return templates.TemplateResponse(
        "finance_receivables.html",
        {"request": request, "active": "finance", "aging": ops_seed.RECEIVABLES_AGING, "collections": ops_seed.COLLECTION_ITEMS},
    )


@router.get("/finance/payables", response_class=HTMLResponse)
def finance_payables(request: Request):
    return templates.TemplateResponse(
        "finance_payables.html", {"request": request, "active": "finance", "payables": ops_seed.PAYABLES}
    )


@router.get("/finance/project/{project_id}", response_class=HTMLResponse)
def finance_project(request: Request, project_id: str):
    project = seed_data.project_by_id(project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return templates.TemplateResponse(
        "finance_project.html",
        {"request": request, "active": "finance", "project": project, "f": ops_seed.project_finance(project)},
    )


# ===================== People =====================

@router.get("/people", response_class=HTMLResponse)
def people_overview(request: Request):
    return templates.TemplateResponse(
        "people_overview.html",
        {"request": request, "active": "people", "m": ops_seed.PEOPLE_METRICS, "employees": _enriched_employees()},
    )


@router.get("/people/employees", response_class=HTMLResponse)
def people_employees(request: Request):
    return templates.TemplateResponse(
        "people_employees.html", {"request": request, "active": "people", "employees": _enriched_employees()}
    )


@router.get("/people/employees/{name}", response_class=HTMLResponse)
def people_employee_detail(request: Request, name: str):
    employee = next((e for e in seed_data.EMPLOYEES if e["name"] == name), None)
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    detail = ops_seed.EMPLOYEE_DETAIL.get(name, {})
    tasks = [t for t in seed_data.TASKS if t["owner"] == name]
    return templates.TemplateResponse(
        "people_employee_detail.html",
        {"request": request, "active": "people", "employee": {**employee, "detail": detail}, "tasks": tasks},
    )


@router.get("/people/leave", response_class=HTMLResponse)
def people_leave(request: Request):
    return templates.TemplateResponse(
        "people_leave.html", {"request": request, "active": "people", "leave": ops_seed.LEAVE_REQUESTS}
    )


# ===================== Unified Approvals =====================

@router.get("/approvals", response_class=HTMLResponse)
def approvals(request: Request):
    return templates.TemplateResponse(
        "approvals.html", {"request": request, "active": "approvals", "approvals": ops_seed.get_approvals()}
    )
