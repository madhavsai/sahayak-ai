# Sahayak AI — Long-Term Product Vision & Architecture Reference

*Saved 2026-10-01. This is the user's full long-term architecture/vision spec, pasted in full and
kept verbatim as a reference document. It is NOT the current build target — see `PRD.md` for what's
actually being built right now (Phase 1, UI-only validation demo).*

**Status:** reference / North Star only, not scoped for implementation yet. This describes a
production-grade, multi-tenant enterprise SaaS platform (47 screens, voice pipeline, knowledge graph,
OCR/document intelligence, agent builder, automation engine, full RBAC/audit/multi-tenancy) — realistically
a 12-24 month build for a funded team, not a next step from the Phase 1 validation demo. Revisit this
once Phase 1 (`PRD.md`) has produced real signup signal, and scope Phase 2/3 deliberately against that
signal rather than building toward this whole document at once.

---

[Full pasted specification follows, preserved verbatim as supplied by the user on 2026-10-01]

# ROLE

You are a senior product architect, UX designer, staff full-stack engineer, AI systems architect and SaaS product manager.

You are building a production-quality, multi-tenant, multilingual AI Business Operating System for Indian small and medium businesses.

The product consists of three integrated product surfaces:

1. AI Contact Center
2. Enterprise Brain
3. AI Business Operations OS

Do NOT treat these as three unrelated applications.

They must operate on top of one shared platform architecture.

The platform should allow an Indian business with 5–200 employees to manage customers, conversations, employees, projects, procurement, vendors, documents, knowledge, invoices, tasks, workflows and AI agents from one system.

The product must be designed around the actual operating behaviour of Indian SMBs:

- WhatsApp
- phone calls
- voice notes
- email
- Excel
- PDFs
- scanned bills
- Tally/accounting systems
- Google Drive
- informal communication
- regional Indian languages
- fragmented business information

The system must progressively convert this unstructured communication into structured business data.

---

# PRODUCT VISION

Build:

> "The AI operating system for Indian businesses."

The system should answer three questions:

1. What is happening in my business?
2. What needs my attention?
3. What can the AI do for me?

The user should not need to understand ERP terminology.

The system should hide complexity.

---

# PRIMARY DESIGN PRINCIPLES

1. AI-first, not ERP-first.
2. WhatsApp-first for field employees and customers.
3. Mobile-first for operational workers.
4. Desktop-first for owners and managers.
5. Multilingual from day one.
6. Every important action must have an audit trail.
7. Every AI response must show its source/context when appropriate.
8. Permission-aware retrieval.
9. Human approval for high-risk actions.
10. Every business object must be connected to other business objects.
11. The system should proactively surface problems.
12. The owner dashboard should focus on exceptions rather than raw data.
13. Do not overwhelm users with configuration.
14. Use progressive disclosure.
15. AI should perform work, not merely answer questions.

---

# PRODUCT SURFACES

## PRODUCT 1 — AI CONTACT CENTER

Channels:

- Phone
- WhatsApp
- Web chat
- Email
- SMS where available

Capabilities:

- inbound calls
- outbound calls
- AI voice agents
- human agents
- AI + human handoff
- conversation recording
- transcription
- sentiment/context analysis
- call summaries
- ticket creation
- CRM updates
- appointment booking
- lead qualification
- payment follow-up
- collections
- customer verification
- workflow execution
- multilingual conversations

---

# PRODUCT 2 — ENTERPRISE BRAIN

The Enterprise Brain is the company's permission-aware memory.

Sources:

- PDFs
- Word
- Excel
- PowerPoint
- images
- scanned documents
- audio
- video
- emails
- WhatsApp
- CRM
- ERP
- project management
- accounting
- cloud drives
- websites
- databases
- APIs
- MCP tools

Capabilities:

- semantic search
- keyword search
- hybrid search
- RAG
- knowledge graph
- entity extraction
- relationship extraction
- document intelligence
- audio transcription
- video understanding
- multilingual retrieval
- source citations
- permission-aware answers
- business analytics
- AI agents
- workflow actions

---

# PRODUCT 3 — AI BUSINESS OPERATING SYSTEM

Modules:

- Dashboard
- CRM
- Leads
- Customers
- Contacts
- Conversations
- Projects
- Tasks
- Procurement
- Purchase orders
- Vendors
- Materials
- Inventory
- Bills
- Expenses
- Payments
- Collections
- Employees
- Attendance
- Documents
- Knowledge
- Reports
- Automations
- AI Agents
- Client Portal
- Settings
- Security
- Audit Logs

The system must support industry templates.

Initial template:

# CONSTRUCTION / BUILDER BUSINESS

Example:

A 10-person luxury villa construction company in Hyderabad.

The system must support:

- projects
- sites
- BOQ
- materials
- vendors
- contractors
- labour
- procurement
- purchase orders
- bills
- payments
- project milestones
- site updates
- site photos
- daily progress reports
- client communication
- client portal
- budget tracking
- cost tracking
- collections
- approvals

---

# GLOBAL APPLICATION SHELL

Create a consistent application shell.

Desktop:

LEFT SIDEBAR

- Home
- Inbox
- CRM
- Projects
- Procurement
- Vendors
- Finance
- People
- Knowledge
- AI Agents
- Reports
- Automations
- Settings

TOP BAR

- Global search
- AI command box
- notifications
- tasks requiring approval
- language selector
- help
- user profile

RIGHT SIDE:

Contextual AI assistant panel.

The assistant should understand the currently open object.

Example:

If viewing a project:

"Ask anything about this project"

If viewing a vendor:

"Ask anything about this vendor"

If viewing a customer:

"Ask anything about this customer"

---

# GLOBAL AI COMMAND BAR

Create a command bar accessible using:

CMD/CTRL + K

Examples:

"Show delayed projects"

"Which customers haven't paid?"

"Find all invoices from ABC Traders"

"Summarize this project"

"Call all leads that haven't responded in 3 days"

"Create a purchase order for 100 cement bags"

"Show me everything discussed with Ramesh about Villa 24"

"Which vendor has the highest outstanding payment?"

"Prepare tomorrow's site meeting agenda"

"Send the client a project progress update"

For actions affecting external systems or money:

require approval.

---

# SCREEN 1 — LOGIN

Elements:

- company logo
- email/mobile login
- password
- OTP login
- Google login
- Microsoft login
- language selector
- privacy/security information

Indian-friendly authentication.

---

# SCREEN 2 — COMPANY ONBOARDING

Step 1:

Business name

Business type

Industry

City

State

GSTIN

Number of employees

Step 2:

Select business template:

- Construction
- Real estate
- Manufacturing
- Distribution
- Retail
- Professional services
- Healthcare
- Education
- Other

Step 3:

Connect existing systems:

- WhatsApp
- Gmail
- Google Drive
- Microsoft 365
- Tally
- Zoho
- Excel
- CRM
- accounting software

Step 4:

Invite employees.

Step 5:

Configure languages.

Primary language:

English / Hindi / Telugu / Tamil / Kannada / Malayalam / Marathi / Bengali / Gujarati / Punjabi / other.

Allow multiple languages.

---

# SCREEN 3 — BUSINESS HOME

This is the most important screen.

Do NOT make this a traditional dashboard.

Title:

"Good morning, [Owner Name]"

Subtitle:

"Here is what needs your attention."

Sections:

## TODAY

- overdue payments
- delayed projects
- pending approvals
- unresolved customer issues
- procurement requiring approval
- important calls
- important messages

## BUSINESS HEALTH

Cards:

- Revenue
- Receivables
- Payables
- Active Projects
- Leads
- Open Tickets
- Cash Position

## AI INSIGHTS

Examples:

"Villa 12 is 6 days behind schedule."

"₹8.4 lakh is overdue from 3 customers."

"Steel purchases are 11% above the project budget."

"ABC Suppliers has not delivered the expected material."

## QUICK ACTIONS

- Create customer
- Create project
- Create task
- Create purchase order
- Record expense
- Send WhatsApp
- Start AI call
- Ask AI

---

# SCREEN 4 — GLOBAL INBOX

Unified inbox.

Tabs:

- All
- WhatsApp
- Calls
- Email
- Chat
- Tasks
- Alerts

Each conversation should display:

- contact
- company
- project
- channel
- language
- priority
- sentiment/context
- assigned employee
- AI status
- last message

Actions:

- reply
- assign
- create task
- create ticket
- create customer
- link project
- summarize
- ask AI

---

# SCREEN 5 — WHATSAPP INBOX

Create a WhatsApp-style interface.

LEFT:

conversation list.

CENTER:

conversation.

RIGHT:

customer context.

Customer context:

- customer information
- projects
- outstanding payments
- previous conversations
- tasks
- documents
- AI summary

AI actions:

"Summarize"

"Find previous promises"

"Create follow-up"

"Draft response"

"Translate"

"Reply automatically"

---

# SCREEN 6 — CONTACT CENTER DASHBOARD

Show:

- active calls
- calls today
- AI handled
- human handled
- missed calls
- average duration
- appointments
- leads generated
- collections
- unresolved conversations

Real-time call activity.

---

# SCREEN 7 — AI AGENTS

Agent marketplace/dashboard.

Agent cards:

- Receptionist
- Sales Agent
- Support Agent
- Collections Agent
- Appointment Agent
- Lead Qualification Agent
- Follow-up Agent
- Procurement Agent
- Project Update Agent

Each card:

- status
- channels
- language
- calls today
- success rate
- human handoffs

---

# SCREEN 8 — AGENT BUILDER

Create a visual agent configuration interface.

Sections:

Identity

- agent name
- personality
- language
- voice

Goal

- objective
- success criteria

Knowledge

- documents
- websites
- company knowledge
- CRM data

Tools

- CRM
- calendar
- WhatsApp
- email
- payment
- ticketing
- APIs

Guardrails

- allowed actions
- prohibited actions
- approval requirements

Escalation

- when to transfer to human
- whom to transfer to

Evaluation

- test conversations
- expected responses
- hallucination detection
- task completion

Deploy:

- phone number
- WhatsApp
- website
- email

---

# SCREEN 9 — LIVE CALL

Real-time call interface.

Display:

- customer
- phone number
- detected language
- transcript
- AI reasoning/context summary
- tools being used
- customer information
- sentiment/context indicators
- call duration

Actions:

- transfer
- mute
- pause AI
- take over
- end call
- add note

Do not expose chain-of-thought.

Show only safe operational explanations such as:

"Checking customer record"

"Searching project information"

"Creating appointment"

---

# SCREEN 10 — CALL HISTORY

Filters:

- date
- agent
- language
- outcome
- customer
- project
- duration

Call card:

- recording
- transcript
- summary
- outcome
- extracted entities
- tasks created
- follow-up date

---

# SCREEN 11 — CRM

Main sections:

- Leads
- Customers
- Contacts
- Companies
- Opportunities

Views:

- table
- kanban
- timeline

Lead card:

- name
- company
- source
- value
- stage
- owner
- last interaction
- next action
- AI score/context

---

# SCREEN 12 — CUSTOMER DETAIL

Header:

Customer name

Company

Status

Owner

Tabs:

Overview

Conversations

Calls

Projects

Invoices

Payments

Documents

Tasks

Timeline

AI Summary

Right panel:

"Ask AI about this customer"

Example:

"What did they promise to pay?"

"When did we last speak?"

"What issues are unresolved?"

---

# SCREEN 13 — PROJECT LIST

Views:

- portfolio
- kanban
- list
- map if applicable

Each project:

- project name
- client
- manager
- progress
- budget
- spent
- pending payment
- deadline
- health

Health:

On track

At risk

Delayed

Blocked

---

# SCREEN 14 — PROJECT DETAIL

Header:

Project name

Client

Location

Project manager

Progress

Tabs:

Overview

Milestones

Tasks

Site Updates

Materials

Procurement

Vendors

Bills

Payments

Documents

Conversations

Team

Client Portal

AI

Overview:

- progress
- budget
- actual spend
- remaining budget
- upcoming milestone
- delayed items
- open issues

---

# SCREEN 15 — PROJECT TIMELINE

Visual timeline:

Planning

Design

Foundation

Structure

Electrical

Plumbing

Flooring

Interior

Finishing

Handover

Each milestone:

- planned date
- actual date
- completion
- dependencies
- owner
- documents
- tasks

---

# SCREEN 16 — DAILY SITE UPDATE

Designed primarily for mobile.

Large buttons:

+ Add Photo

+ Add Video

+ Record Voice

+ Add Material

+ Add Labour

+ Add Issue

+ Add Progress

Allow voice input.

Example:

Employee speaks Telugu:

"Today foundation work completed for block B. 14 workers attended."

AI converts this into structured information.

Show:

"Here is what I understood"

Project:

Block B

Activity:

Foundation

Progress:

Completed

Labour:

14

Button:

CONFIRM

---

# SCREEN 17 — MATERIALS

Inventory/material screen.

Columns:

Material

Quantity

Unit

Project

Available

Reserved

Ordered

Required

Low-stock alerts.

AI action:

"Predict material shortages"

---

# SCREEN 18 — PROCUREMENT

Procurement dashboard.

Sections:

Purchase Requests

RFQs

Quotes

Purchase Orders

Goods Received

Bills

Payments

Workflow:

Request

→ Approval

→ RFQ

→ Vendor Quotes

→ Comparison

→ Approval

→ PO

→ Delivery

→ GRN

→ Bill

→ Payment

---

# SCREEN 19 — PURCHASE REQUEST

Fields:

Project

Material

Quantity

Required date

Reason

Estimated cost

Requested by

Attachments

AI suggestion:

"Based on previous purchases, 3 suitable vendors are available."

---

# SCREEN 20 — VENDOR MANAGEMENT

Vendor list.

Vendor profile:

- company
- contact
- GST
- categories
- projects
- purchase history
- outstanding
- payment history
- delivery history
- quality issues
- conversations
- documents

AI summary:

"ABC Traders supplied ₹42 lakh of materials this year."

---

# SCREEN 21 — PURCHASE COMPARISON

Show vendor quotes side-by-side.

Columns:

Vendor

Price

Delivery

Payment terms

Quality history

Previous price

AI notes

Do not automatically select a vendor.

Allow:

Approve

Reject

Request clarification

---

# SCREEN 22 — BILLS

Upload:

- PDF
- photo
- scan

AI OCR extracts:

Vendor

GSTIN

Invoice number

Date

Items

Quantity

Tax

Total

Project

PO

Then perform validation:

Invoice ↔ PO ↔ Goods Received

Show mismatches.

---

# SCREEN 23 — EXPENSES

Create expense.

Input:

- amount
- category
- project
- employee
- receipt

Allow photo capture.

AI extracts receipt information.

---

# SCREEN 24 — FINANCE DASHBOARD

Do not try to replace full accounting initially.

Show operational finance:

- receivables
- payables
- project costs
- cash flow
- overdue invoices
- upcoming payments
- expenses

Integrate with accounting systems.

---

# SCREEN 25 — COLLECTIONS

Show:

Customer

Invoice

Amount

Due date

Days overdue

Last contact

Next action

AI actions:

Draft WhatsApp

Call customer

Send reminder

Schedule follow-up

For financial commitments, require configured approval policies.

---

# SCREEN 26 — CLIENT PORTAL

A client-facing simplified UI.

Client sees:

- project overview
- progress
- milestone status
- photos
- videos
- upcoming work
- documents
- invoices
- payments
- messages
- approvals

The client should NOT see internal business information.

---

# SCREEN 27 — CLIENT PROGRESS VIEW

Large visual progress.

Example:

Villa Construction

Overall:

72%

Sections:

Structure 100%

Electrical 80%

Plumbing 65%

Interior 42%

Finishing 20%

Photos.

Timeline.

Upcoming milestones.

Issues requiring client approval.

---

# SCREEN 28 — TASK MANAGEMENT

Views:

- My Tasks
- Team Tasks
- Project Tasks
- Overdue
- Calendar
- Kanban

Each task:

- owner
- due date
- project
- priority
- dependencies
- source conversation

Critical feature:

A task can originate from:

WhatsApp

Call

Email

AI agent

Meeting

Site update

Manual creation

---

# SCREEN 29 — KNOWLEDGE CENTER

This is the Enterprise Brain UI.

Sections:

- All Knowledge
- Documents
- Audio
- Video
- Conversations
- Emails
- Projects
- CRM
- Policies
- Contracts
- Vendors

Search box:

"Ask anything about your business"

---

# SCREEN 30 — AI SEARCH

Example query:

"Which projects are currently delayed because of material shortages?"

Results must show:

Answer

Sources

Projects

Documents

Conversations

Dates

People

Confidence/context indicators

Never present unsupported claims as facts.

---

# SCREEN 31 — KNOWLEDGE GRAPH

Interactive graph.

Entities:

People

Customers

Companies

Projects

Vendors

Documents

Invoices

Tasks

Conversations

Products

Materials

Relationships:

works_for

owns

manages

supplies

mentioned_in

belongs_to

paid_by

related_to

depends_on

Graph should support filtering and exploration.

---

# SCREEN 32 — DATA CONNECTORS

Connector marketplace.

Categories:

Communication

- WhatsApp
- Gmail
- Outlook
- Slack
- Teams

Storage

- Google Drive
- OneDrive
- SharePoint
- Dropbox

Business

- Zoho
- Salesforce
- HubSpot
- Tally
- ERP systems

Developer

- PostgreSQL
- APIs
- Webhooks
- MCP

Each connector shows:

Connected

Sync status

Last sync

Objects indexed

Errors

Permissions

---

# SCREEN 33 — CONNECTOR DETAIL

Show:

Connection status

Last synchronization

Records indexed

Errors

Permissions

Data types

Sync frequency

Actions enabled

Buttons:

Sync now

Pause

Reconnect

Delete

---

# SCREEN 34 — INGESTION PIPELINE

Show ingestion stages:

Source

→ Fetch

→ Parse

→ OCR

→ Transcribe

→ Chunk

→ Embed

→ Entity extraction

→ Permission mapping

→ Index

→ Knowledge graph

Each document should show processing status.

---

# SCREEN 35 — DOCUMENT VIEWER

Left:

document preview.

Right:

AI summary.

Metadata:

Owner

Created

Modified

Source

Permissions

Entities

Related projects

Related people

Related conversations

Actions:

Ask AI

Summarize

Translate

Extract fields

Create task

Create workflow

---

# SCREEN 36 — MULTIMODAL KNOWLEDGE

Audio:

Transcript

Speaker identification

Summary

Topics

Entities

Video:

Transcript

Scenes

Objects

People

Topics

Documents:

OCR

Tables

Images

Entities

All content must become searchable.

---

# SCREEN 37 — AI ASSISTANT

Global conversational interface.

User can ask:

"What happened this week?"

"Which projects are at risk?"

"Why did expenses increase?"

"Show outstanding customer payments."

"Summarize today's important conversations."

"Which vendors are late?"

"Prepare tomorrow's management meeting."

"Create follow-up tasks."

The assistant should have access only to information permitted for the current user.

---

# SCREEN 38 — AI ACTION APPROVAL CENTER

Critical screen.

Every AI action requiring approval appears here.

Examples:

Send message

Make call

Create purchase order

Approve expense

Change CRM record

Send invoice

Cancel appointment

Create payment instruction

Display:

AI requested action

Reason

Affected records

Potential impact

Source/context

Buttons:

Approve

Reject

Edit

---

# SCREEN 39 — AUTOMATION BUILDER

Visual workflow builder.

Trigger:

New WhatsApp message

New call

New lead

Invoice overdue

Project delayed

Material below threshold

Vendor delivery late

New email

New document

Then:

Condition

AI interpretation

Action

Approval

Notification

Example:

Invoice overdue 7 days

→ AI checks customer history

→ draft WhatsApp

→ owner approval

→ send message

→ schedule follow-up

---

# SCREEN 40 — AI AGENT ANALYTICS

Metrics:

Conversations

Successful outcomes

Human handoffs

Task completion

Tool errors

Latency

Cost

Language distribution

Customer satisfaction

Failure reasons

Agent evaluation scores

---

# SCREEN 41 — REPORTS

Reports:

Sales

Customers

Projects

Procurement

Vendors

Finance

Employees

AI Agents

Operations

Custom reports

Allow natural-language report creation.

Example:

"Show material cost by project for the last 6 months."

---

# SCREEN 42 — NOTIFICATIONS

Notification types:

Approval

Mention

Task

Customer

Payment

Project

Procurement

AI

System

Allow granular preferences.

---

# SCREEN 43 — PEOPLE

Employee list.

Employee detail:

- role
- department
- projects
- tasks
- activity
- permissions
- conversations
- performance context

Do not expose sensitive information unnecessarily.

---

# SCREEN 44 — ROLES & PERMISSIONS

Roles:

Owner

Admin

Manager

Project Manager

Finance

Procurement

Sales

Support

Employee

External Client

Vendor

Permissions should operate at:

Organization

Module

Object

Field

Action

Project

Document

Conversation

---

# SCREEN 45 — AUDIT LOG

Every important operation must be logged.

Show:

Actor

AI/Human

Action

Object

Timestamp

Before

After

Source

Approval

IP/device where appropriate

---

# SCREEN 46 — SECURITY CENTER

Display:

Authentication

SSO

MFA

Sessions

API keys

Data encryption

Backups

Audit logs

Permissions

Data retention

AI data policies

Connector permissions

Tenant isolation

---

# SCREEN 47 — SETTINGS

Sections:

Company

Users

Roles

Languages

Notifications

Integrations

WhatsApp

Telephony

Email

AI

Billing

Security

Data

Audit

API

Webhooks

---

# MOBILE EXPERIENCE

Mobile app/web experience must prioritize:

- Inbox
- Calls
- Tasks
- Projects
- Site updates
- Approvals
- Procurement
- AI assistant

Large touch targets.

Minimal typing.

Voice input everywhere.

Camera capture everywhere relevant.

Offline-friendly site operations.

---

# MULTILINGUAL ARCHITECTURE

The application must support multilingual interaction.

Users may use:

English

Hindi

Telugu

Tamil

Kannada

Malayalam

Marathi

Bengali

Gujarati

Punjabi

Hinglish

Tanglish

Telugu-English code switching

etc.

Do not translate everything into English internally at the UI layer.

Maintain:

original content

detected language

normalized representation

translated representation where required.

A user should be able to speak Telugu to the AI and another employee should read the resulting structured record in English.

---

# BUSINESS DATA MODEL

Create shared entities:

Organization

User

Role

Permission

Customer

Contact

Lead

Conversation

Message

Call

Email

Ticket

Project

Milestone

Task

Employee

Vendor

Material

Product

PurchaseRequest

RFQ

VendorQuote

PurchaseOrder

GoodsReceipt

Invoice

Bill

Payment

Expense

Document

KnowledgeItem

Embedding

Entity

Relationship

Agent

Workflow

Automation

Approval

AuditEvent

Notification

Integration

Connector

---

# MULTI-TENANCY

Every record must belong to an organization/tenant.

Never allow cross-tenant access.

Implement tenant-aware:

database queries

cache

search

vector storage

object storage

background jobs

events

logs

analytics

AI retrieval

Connectors.

---

# AI RETRIEVAL SECURITY

The system must never retrieve information solely because it is semantically relevant.

Retrieval must consider:

tenant

user

role

source permissions

object permissions

document permissions

field-level restrictions where applicable.

Permission checks must happen at retrieval/action time.

---

# AI ARCHITECTURE

Use a model-agnostic architecture.

Support:

cloud LLMs

local LLMs

open-source models

different embedding models

different STT providers

different TTS providers

different vision models

different rerankers.

Do not hard-code the application to one AI vendor.

---

# VOICE ARCHITECTURE

Pipeline:

Telephony/WebRTC

→ VAD

→ STT

→ language detection

→ conversation manager

→ retrieval

→ tool execution

→ LLM

→ TTS

→ user

Support:

barge-in

interruptions

streaming

partial transcription

low latency

human transfer

recording

transcription

call metadata

---

# EVENT ARCHITECTURE

All important system actions should generate events.

Examples:

customer.created

message.received

call.completed

invoice.created

invoice.overdue

project.delayed

material.low_stock

purchase.requested

purchase.approved

vendor.delivery_received

task.created

agent.action_requested

agent.action_approved

agent.action_rejected

Use an event-driven architecture where appropriate.

---

# API ARCHITECTURE

Use REST APIs for core application functionality.

Use WebSockets/SSE for:

- live conversations
- call status
- notifications
- agent activity
- ingestion progress
- real-time dashboards.

Use webhooks for external integrations.

Provide API documentation.

---

# FRONTEND

Use:

HTML

CSS

JavaScript/TypeScript

Do not introduce unnecessary frontend frameworks.

Use reusable components.

Responsive desktop/mobile layouts.

Accessibility:

keyboard navigation

ARIA

contrast

focus states

screen-reader support.

---

# DESIGN SYSTEM

Visual style:

Modern

Minimal

Professional

Trustworthy

AI-native

Not futuristic gimmicky.

Use:

neutral backgrounds

cards

subtle borders

rounded corners

clear typography

high information density where useful

large whitespace on executive screens.

Use purple as a subtle brand accent.

Do not overuse gradients.

AI actions should be visually distinguishable from normal CRUD operations.

---

# COMPONENT LIBRARY

Build reusable components:

Button

IconButton

Input

Search

Select

Combobox

DatePicker

Tabs

Modal

Drawer

Toast

Tooltip

DataTable

Kanban

Timeline

ActivityFeed

Chat

MessageBubble

AudioPlayer

VideoPlayer

DocumentViewer

StatusBadge

ProgressBar

MetricCard

ApprovalCard

AgentCard

EntityCard

AIInsight

CommandBar

WorkflowNode

GraphNode

EmptyState

LoadingState

ErrorState

---

# AI UX RULES

Never pretend AI knows something it doesn't.

When answering from company knowledge:

show source references.

When uncertain:

say what is missing.

For actions:

show exactly what will happen.

For destructive or financial actions:

require confirmation according to configured policy.

Never expose hidden chain-of-thought.

Instead expose:

sources

tool actions

status

result

errors

approval requirements.

---

# AI BUSINESS ASSISTANT EXAMPLES

The assistant should be capable of:

"Show me all projects delayed more than 7 days."

"Why is Villa 14 delayed?"

"Find all conversations mentioning cement shortage."

"Which vendor supplied the most material this year?"

"Call customers with invoices overdue more than 30 days."

"Prepare today's management briefing."

"Create tasks for all unresolved issues."

"Send the client a progress update."

"Compare this month's expenses with last month."

"Find all contracts expiring in the next 60 days."

---

# OWNER EXPERIENCE

The owner should be able to use the product primarily through:

AI assistant

WhatsApp

mobile app

dashboard.

The owner should NOT need to understand:

RAG

embeddings

vector databases

knowledge graphs

agents

workflows.

All infrastructure complexity must remain invisible.

---

# ADMIN EXPERIENCE

Administrators need:

connector management

users

roles

permissions

AI policies

agent configuration

workflow configuration

data governance

audit logs

billing

usage

security.

---

# IMPLEMENTATION STRATEGY

Build in phases.

PHASE 1:

Core platform

- authentication
- tenancy
- users
- permissions
- dashboard
- CRM
- contacts
- tasks
- conversations
- AI assistant

PHASE 2:

Business operations

- projects
- vendors
- procurement
- materials
- bills
- expenses
- payments
- client portal

PHASE 3:

Enterprise Brain

- connectors
- document ingestion
- OCR
- transcription
- embeddings
- hybrid search
- RAG
- knowledge graph
- permission-aware retrieval

PHASE 4:

Contact Center

- telephony
- inbound calls
- outbound calls
- voice agents
- call recording
- transcription
- human transfer

PHASE 5:

Agent platform

- agent builder
- tools
- workflows
- approvals
- evaluations
- analytics

PHASE 6:

Industry templates

- Construction
- Real estate
- Manufacturing
- Distribution
- Retail
- Professional services
- Healthcare
- Education

---

# CRITICAL PRODUCT REQUIREMENT

Do not build screens merely because they exist in traditional ERP software.

Every screen must answer:

"What user problem does this solve?"

If a feature can be performed naturally through the AI assistant, expose that path prominently.

Example:

Instead of:

Procurement → Purchase Request → Create

allow:

"Need 100 bags of cement for Villa 12 by Friday."

AI:

"Do you want me to create a purchase request for 100 bags of cement for Villa 12?"

Confirm.

Then execute.

---

# DEMO SCENARIO

Create a complete demo business:

Company:

Hyderabad Luxury Villas Pvt Ltd.

Employees:

12

Projects:

5

Customers:

8

Vendors:

25

Active projects:

3

Languages:

English + Telugu + Hindi

Channels:

WhatsApp + phone + email.

Populate realistic demo data.

The demo should demonstrate this complete flow:

Customer calls

→ AI receptionist answers in Telugu

→ identifies customer

→ identifies project

→ retrieves latest project status

→ answers customer

→ customer asks about payment

→ AI retrieves outstanding invoice

→ customer asks for progress update

→ AI generates summary

→ sends WhatsApp update

→ conversation is stored

→ project timeline updates

→ owner dashboard shows interaction

→ AI identifies a follow-up

→ creates task

→ task assigned to project manager.

Second scenario:

Site manager sends Telugu voice note.

→ STT

→ AI understands

→ material receipt created

→ labour update created

→ site progress updated

→ project dashboard changes

→ owner receives notification.

Third scenario:

Vendor sends invoice PDF.

→ OCR

→ extract invoice

→ match PO

→ match goods receipt

→ identify discrepancy

→ create approval request.

Fourth scenario:

Owner asks:

"Which of my projects are at risk and why?"

AI searches:

projects

tasks

procurement

vendor data

site updates

conversations

documents

financial information

and produces a grounded answer with sources.

---

# QUALITY REQUIREMENTS

Before declaring the application complete:

Test every screen.

Test every CRUD operation.

Test tenant isolation.

Test role permissions.

Test AI retrieval permissions.

Test connector failures.

Test multilingual inputs.

Test Telugu voice input.

Test Hinglish.

Test poor-quality audio.

Test duplicate invoices.

Test duplicate customers.

Test conflicting information.

Test AI hallucination scenarios.

Test approval workflows.

Test failed external API calls.

Test WebSocket reconnection.

Test mobile layout.

Test accessibility.

Test audit logging.

Test data deletion.

Test backup/recovery.

---

# FINAL PRODUCT PRINCIPLE

The final experience should feel like:

"Someone who understands my business is sitting beside me."

Not:

"I bought another ERP."

The product should progressively transform:

WhatsApp

+

phone calls

+

voice notes

+

documents

+

emails

+

Excel

+

CRM

+

ERP

+

projects

+

procurement

into:

ONE BUSINESS MEMORY

+

ONE BUSINESS WORKSPACE

+

ONE AI WORKFORCE

+

ONE OPERATING SYSTEM.

Build the foundation so that Contact Center, Enterprise Brain and Business Operations are different product surfaces over the same underlying business graph, identity system, workflow engine, AI layer and permission system.
