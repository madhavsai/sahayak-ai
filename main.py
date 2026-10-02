"""Sahayak AI.

Two things live in this one FastAPI app:
1. The public marketing/validation site at "/" (landing page + signup capture
   to data/signups.json) - see PRD.md.
2. The internal app shell at "/app/*" - a UI-only demo of the product itself,
   wired to seeded sample data (app/seed_data.py), not a real database or
   real AI. See VISION.md for the full long-term scope this is a first slice
   of, and the sidebar's "Coming soon" items for what isn't built yet.
"""
import json
from datetime import datetime, timezone
from pathlib import Path

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, Field

from app import seed_data
from app.knowledge_routes import router as knowledge_router
from app.ops_routes import router as ops_router

BASE_DIR = Path(__file__).parent
DATA_FILE = BASE_DIR / "data" / "signups.json"

app = FastAPI(title="Sahayak AI")
templates = Jinja2Templates(directory=BASE_DIR / "templates")


# ===================== Marketing site: signup API =====================

class SignupRequest(BaseModel):
    name: str = Field(min_length=1, max_length=200)
    contact: str = Field(min_length=3, max_length=200)
    business_type: str = Field(min_length=1, max_length=200)
    services: list[str] = Field(min_length=1)
    wants_call: bool = False


@app.post("/api/signup")
def create_signup(payload: SignupRequest):
    valid_services = {"contact_center", "enterprise_brain", "operations"}
    if not set(payload.services).issubset(valid_services):
        raise HTTPException(status_code=400, detail="Unknown service in selection")

    signups = json.loads(DATA_FILE.read_text(encoding="utf-8"))
    signups.append(
        {
            "name": payload.name.strip(),
            "contact": payload.contact.strip(),
            "business_type": payload.business_type.strip(),
            "services": payload.services,
            "wants_call": payload.wants_call,
            "submitted_at": datetime.now(timezone.utc).isoformat(),
        }
    )
    DATA_FILE.write_text(json.dumps(signups, indent=2, ensure_ascii=False), encoding="utf-8")
    return {"ok": True, "total_signups": len(signups)}


@app.get("/api/signups")
def list_signups():
    return json.loads(DATA_FILE.read_text(encoding="utf-8"))


# ===================== App shell: UI only, seeded data =====================

@app.get("/login", response_class=HTMLResponse)
def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@app.get("/app", response_class=HTMLResponse)
def app_root(request: Request):
    return home(request)


@app.get("/app/home", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        "home.html",
        {
            "request": request,
            "active": "home",
            "user": seed_data.CURRENT_USER,
            "overdue": seed_data.overdue_tasks(),
            "health": seed_data.business_health(),
            "insights": seed_data.AI_INSIGHTS,
        },
    )


@app.get("/app/inbox", response_class=HTMLResponse)
def inbox(request: Request):
    return templates.TemplateResponse(
        "inbox.html",
        {"request": request, "active": "inbox", "conversations": seed_data.RECENT_CONVERSATIONS},
    )


@app.get("/app/crm", response_class=HTMLResponse)
def crm(request: Request):
    return templates.TemplateResponse(
        "crm.html",
        {"request": request, "active": "crm", "leads": seed_data.LEADS, "customers": seed_data.CUSTOMERS},
    )


@app.get("/app/crm/customers/{index}", response_class=HTMLResponse)
def customer_detail(request: Request, index: int):
    if index < 0 or index >= len(seed_data.CUSTOMERS):
        raise HTTPException(status_code=404, detail="Customer not found")
    customer = seed_data.CUSTOMERS[index]
    project = None
    if customer.get("project"):
        project = next((p for p in seed_data.PROJECTS if p["name"] == customer["project"]), None)
    return templates.TemplateResponse(
        "customer_detail.html",
        {"request": request, "active": "crm", "customer": customer, "project": project},
    )


@app.get("/app/projects", response_class=HTMLResponse)
def projects_list(request: Request):
    return templates.TemplateResponse(
        "projects_list.html",
        {"request": request, "active": "projects", "projects": seed_data.PROJECTS},
    )


@app.get("/app/projects/{project_id}", response_class=HTMLResponse)
def project_detail(request: Request, project_id: str):
    project = seed_data.project_by_id(project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return templates.TemplateResponse(
        "project_detail.html",
        {
            "request": request,
            "active": "projects",
            "project": project,
            "tasks": seed_data.tasks_for_project(project["name"]),
        },
    )


@app.get("/app/tasks", response_class=HTMLResponse)
def tasks(request: Request):
    return templates.TemplateResponse(
        "tasks.html", {"request": request, "active": "tasks", "tasks": seed_data.TASKS}
    )


@app.get("/app/vendors", response_class=HTMLResponse)
def vendors(request: Request):
    return templates.TemplateResponse(
        "vendors.html", {"request": request, "active": "vendors", "vendors": seed_data.VENDORS}
    )


COMING_SOON = {
    "contact-center": ("Contact Center", "AI voice and chat agents that handle inbound/outbound calls, "
                        "WhatsApp, and email — with CRM and ticketing built in, replacing the BPO desk end to end."),
    "ai-agents": ("AI Agents", "Build and deploy AI agents — receptionist, sales, collections, follow-up — "
                   "with guardrails, tools, and approval rules."),
    "reports": ("Reports", "Natural-language reports across sales, projects, procurement, vendors, and finance."),
    "automations": ("Automations", "Visual workflow builder — trigger, condition, AI interpretation, action, approval."),
    "settings": ("Settings", "Company profile, users, roles, languages, integrations, billing, and security."),
}


@app.get("/app/coming-soon/{slug}", response_class=HTMLResponse)
def coming_soon(request: Request, slug: str):
    name, description = COMING_SOON.get(slug, (slug.replace("-", " ").title(), "Not built yet."))
    return templates.TemplateResponse(
        "coming_soon.html",
        {"request": request, "active": slug, "name": name, "description": description},
    )


app.include_router(knowledge_router)
app.include_router(ops_router)

app.mount("/app-static", StaticFiles(directory=BASE_DIR / "static" / "app"), name="app-static")
app.mount("/knowledge-static", StaticFiles(directory=BASE_DIR / "static" / "knowledge"), name="knowledge-static")

# Marketing site mount must stay last - it's a catch-all at "/".
app.mount("/", StaticFiles(directory=BASE_DIR / "static", html=True), name="static")
