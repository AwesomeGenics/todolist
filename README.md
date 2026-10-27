# Tasks — Material Workspace

A focused, distraction-free task management application built with Flask and Google's Material Design 3 (M3). Designed around clarity, intentional whitespace, and purposeful motion.

---

## Design Philosophy

- **Google Material Design 3**: Built upon Google's M3 token architecture—dynamic tonal palettes (Google Blue primary, container tints, subtle surface elevations), rounded pill shapes, and official Material Symbols Rounded iconography.
- **Asymmetric Editorial Layouts**: Replaced repetitive 3-column card grids and hairline broadsheet borders with asymmetric, breathing space and high-contrast editorial typography.
- **Intentional Brand Voice**: Microcopy is calibrated for focus and calm confidence rather than sterile feature-spec bullet points.
- **Purposeful Motion**: Smooth transitions adhering to Material standard easing (`cubic-bezier(0.2, 0, 0, 1)`), stripping away bouncy springs, hover-scale jumps, and artificial glow blobs.

---

## Core Capabilities

- **User Authentication**: Secure multi-user login and registration with isolated task workspaces for each account.
- **Dynamic Task Lifecycle**: Seamlessly transition items between **In Progress** and **Completed** with interactive state markers.
- **Streamlined Quick-Add**: Minimalist task capture interface designed to record thoughts without breaking flow.
- **Archive & Clear Actions**: Dedicated controls to clear active tasks or wipe completed archives independently.
- **Mobile Responsive**: Fully adaptive top app bar, segmented controllers, and input cards tailored for both desktop and touch devices.

---

## Project Structure

```
trying_todolist/
├── app/
│   ├── __init__.py
│   ├── auth.py          # Authentication blueprint (login, registration, session clear)
│   ├── db.py            # SQLite database initialization & tables schema
│   └── tasks.py         # Task blueprint (add, list, complete, clear)
├── static/
│   └── css/
│       └── material.css # Google Material Design 3 tokens & component styles
├── templates/
│   ├── base.html        # Material 3 Top App Bar, typography, and footer shell
│   ├── listview.html    # Asymmetric dashboard with pending & completed tabs
│   ├── login.html       # Outlined credential sign-in card
│   ├── newtask.html     # Single-focus task creation card
│   └── register.html    # Outlined registration card
├── main.py              # Main Flask application entry point
├── .env                 # Environment configuration (SECRET_KEY)
├── tasks.db             # SQLite database storing users and owner tasks
├── requirements.txt     # Python dependencies
└── README.md
```

---

## Getting Started

### 1. Prerequisites
- Python 3.10+
- `pip` or virtualenv

### 2. Environment Setup

Clone or navigate to the project directory and activate your virtual environment:

```bash
cd trying_todolist
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

*Requirements include:*
- `Flask`
- `Flask-Session`
- `Werkzeug`
- `python-dotenv`
- `gunicorn`

### 4. Run the Application

**Development Server:**
```bash
python3 main.py
```

**Production with Gunicorn:**
```bash
gunicorn -w 4 -b 0.0.0.0:5000 main:app
```

The application will start on `http://0.0.0.0:5000` (or `http://127.0.0.1:5000`).

---

## Design System Tokens & Specs

| Token | Role | Hex Value |
|---|---|---|
| `--md-sys-color-primary` | Key brand actions & focus | `#0B57D0` |
| `--md-sys-color-primary-container` | Tonal chips & icon badges | `#D3E3FD` |
| `--md-sys-color-surface` | Background canvas | `#F8FAFD` |
| `--md-sys-color-surface-container-lowest` | Elevated cards & surfaces | `#FFFFFF` |
| `--md-sys-color-on-surface` | Primary typography | `#191C20` |
| `--md-sys-color-on-surface-variant` | Secondary descriptions | `#43474E` |
| `--md-sys-color-outline-variant` | Subtle component dividers | `#C3C7D0` |
