"""Routes for the Knowledge Platform (Enterprise Brain) mini-app - UI only, seeded data."""
from pathlib import Path

from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app import knowledge_seed

BASE_DIR = Path(__file__).parent.parent
templates = Jinja2Templates(directory=BASE_DIR / "templates")
templates.env.globals["notifications"] = knowledge_seed.NOTIFICATIONS

router = APIRouter(prefix="/knowledge")

COMING_SOON = {}


@router.get("/home", response_class=HTMLResponse)
def knowledge_home(request: Request):
    return templates.TemplateResponse(
        "knowledge_home.html",
        {
            "request": request,
            "active": "home",
            "health": knowledge_seed.HEALTH,
            "ingestion": knowledge_seed.INGESTION_HEALTH,
            "ai_usage": knowledge_seed.AI_USAGE,
            "connectors": knowledge_seed.CONNECTORS,
            "suggestions": knowledge_seed.SEARCH_SUGGESTIONS,
        },
    )


@router.get("/connectors", response_class=HTMLResponse)
def knowledge_connectors(request: Request):
    return templates.TemplateResponse(
        "knowledge_connectors.html",
        {
            "request": request,
            "active": "connectors",
            "connectors": knowledge_seed.CONNECTORS,
            "categories": knowledge_seed.CONNECTOR_CATEGORIES,
        },
    )


@router.get("/connectors/{connector_id}", response_class=HTMLResponse)
def knowledge_connector_detail(request: Request, connector_id: str):
    connector = next((c for c in knowledge_seed.CONNECTORS if c["id"] == connector_id), None)
    if not connector:
        raise HTTPException(status_code=404, detail="Connector not found")
    return templates.TemplateResponse(
        "knowledge_connector_detail.html",
        {
            "request": request,
            "active": "connectors",
            "connector": connector,
            "errors": knowledge_seed.CONNECTOR_ERRORS.get(connector_id, []),
            "content_tree": knowledge_seed.CONNECTOR_CONTENT_TREE,
            "identity_mapping": knowledge_seed.IDENTITY_MAPPING,
        },
    )


@router.get("/connectors/{connector_id}/connect", response_class=HTMLResponse)
def knowledge_connector_setup(request: Request, connector_id: str):
    connector = next((c for c in knowledge_seed.CONNECTORS if c["id"] == connector_id), None)
    if not connector:
        raise HTTPException(status_code=404, detail="Connector not found")
    return templates.TemplateResponse(
        "knowledge_connector_setup.html",
        {
            "request": request,
            "active": "connectors",
            "connector": connector,
            "scope_options": knowledge_seed.CONNECTOR_SCOPE_OPTIONS,
            "permission_modes": knowledge_seed.CONNECTOR_PERMISSION_MODES,
            "content_types": knowledge_seed.CONNECTOR_CONTENT_TYPES,
            "content_tree": knowledge_seed.CONNECTOR_CONTENT_TREE,
            "sync_options": knowledge_seed.CONNECTOR_SYNC_OPTIONS,
            "connector_detail_url": f"/knowledge/connectors/{connector_id}",
        },
    )


@router.get("/capture", response_class=HTMLResponse)
def knowledge_capture(request: Request):
    return templates.TemplateResponse(
        "knowledge_capture.html",
        {
            "request": request,
            "active": "capture",
            "methods": knowledge_seed.CAPTURE_METHODS,
            "stages": knowledge_seed.PROCESSING_STAGES,
            "classifications": knowledge_seed.CLASSIFICATION_OPTIONS,
        },
    )


@router.get("/search", response_class=HTMLResponse)
def knowledge_search(request: Request, q: str = ""):
    answer = knowledge_seed.AI_ANSWERS.get(q.strip().lower()) if q else None
    return templates.TemplateResponse(
        "knowledge_search.html",
        {
            "request": request,
            "active": "search",
            "query": q,
            "answer": answer,
            "suggestions": knowledge_seed.SEARCH_SUGGESTIONS,
            "library": knowledge_seed.LIBRARY_ITEMS,
        },
    )


@router.get("/library", response_class=HTMLResponse)
def knowledge_library(request: Request):
    return templates.TemplateResponse(
        "knowledge_library.html",
        {"request": request, "active": "library", "items": knowledge_seed.LIBRARY_ITEMS},
    )


@router.get("/entities", response_class=HTMLResponse)
def knowledge_entities(request: Request):
    return templates.TemplateResponse(
        "knowledge_entities.html",
        {"request": request, "active": "entities", "entities": knowledge_seed.ENTITIES},
    )


@router.get("/entities/{entity_id}", response_class=HTMLResponse)
def knowledge_entity_detail(request: Request, entity_id: str):
    entity = knowledge_seed.ENTITIES.get(entity_id)
    if not entity:
        raise HTTPException(status_code=404, detail="Entity not found")
    return templates.TemplateResponse(
        "knowledge_entity_detail.html",
        {"request": request, "active": "entities", "entity": entity},
    )


@router.get("/ingestion", response_class=HTMLResponse)
def knowledge_ingestion(request: Request):
    return templates.TemplateResponse(
        "knowledge_ingestion.html",
        {"request": request, "active": "ingestion", "stages": knowledge_seed.INGESTION_STAGES,
         "queue": knowledge_seed.INGESTION_QUEUE},
    )


@router.get("/collections", response_class=HTMLResponse)
def knowledge_collections(request: Request):
    return templates.TemplateResponse(
        "knowledge_collections.html",
        {"request": request, "active": "collections", "collections": knowledge_seed.COLLECTIONS},
    )


@router.get("/data-quality", response_class=HTMLResponse)
def knowledge_data_quality(request: Request):
    return templates.TemplateResponse(
        "knowledge_data_quality.html",
        {
            "request": request, "active": "data-quality",
            "dq": knowledge_seed.DATA_QUALITY,
            "conflicts": knowledge_seed.DATA_CONFLICTS,
            "stale": knowledge_seed.STALE_ITEMS,
            "gaps": knowledge_seed.KNOWLEDGE_GAPS,
        },
    )


@router.get("/security", response_class=HTMLResponse)
def knowledge_security(request: Request):
    return templates.TemplateResponse(
        "knowledge_security.html",
        {
            "request": request, "active": "security",
            "ai_policy": knowledge_seed.AI_SOURCE_POLICY,
            "identity_mapping": knowledge_seed.IDENTITY_MAPPING,
        },
    )


@router.get("/audit", response_class=HTMLResponse)
def knowledge_audit(request: Request):
    return templates.TemplateResponse(
        "knowledge_audit.html",
        {"request": request, "active": "audit", "events": knowledge_seed.AUDIT_EVENTS},
    )


@router.get("/settings", response_class=HTMLResponse)
def knowledge_settings(request: Request):
    return templates.TemplateResponse(
        "knowledge_settings.html", {"request": request, "active": "settings"}
    )


@router.get("/coming-soon/{slug}", response_class=HTMLResponse)
def knowledge_coming_soon(request: Request, slug: str):
    name, description = COMING_SOON.get(slug, (slug.replace("-", " ").title(), "Not built yet."))
    return templates.TemplateResponse(
        "knowledge_coming_soon.html",
        {"request": request, "active": slug, "name": name, "description": description},
    )
