# Turkana CIS team exercise

A practical exercise for the team that will run and extend the **Turkana County Climate Information System (CIS)**.

You will build three small features that the real CIS already has, working **as a team in this repository**: each change on its own branch, through a pull request, reviewed by a teammate. How you work together counts as much as the code.

| Task | You build | Skills it shows |
|---|---|---|
| [1. Heat map](docs/tasks/1-heat-map.md) | Temperature and humidity forecast from Open-Meteo for Turkana's sub-counties and main towns, on a map with a table | Calling an outside API, handling its failures, maps |
| [2. Datasets](docs/tasks/2-datasets.md) | A page and API to upload, list, edit and delete climate data files, including NetCDF | File uploads, validation, reading scientific data, full CRUD |
| [3. Resources and alerts](docs/tasks/3-resources-and-alerts.md) | Create, edit and publish resources and alerts, from the database through to the page | Data modelling, validation rules, publishing workflow |

Start with **[Task 0: getting started](docs/tasks/0-getting-started.md)**. Everyone does it, and it is your first pull request.

---

## What is already here

A small starter so you can all work in parallel from day one. It runs, but none of the three features exist yet.

```
backend/    FastAPI + SQLAlchemy + SQLite (the database is a file, so data survives restarts)
  app/
    main.py          app setup; all routers are already registered
    db.py            database engine and the get_db dependency
    models.py        the Base class; add your tables here
    routers/         health.py works; heat.py, datasets.py, resources.py and alerts.py are empty for you
  tests/             pytest, with a fresh database for every test
frontend/   React + TypeScript + Vite + Tailwind; Leaflet is installed for the map
  src/
    App.tsx          layout, navigation and routes (already wired to your pages)
    api/client.ts    a small helper for calling the backend
    pages/           HeatMapPage, DatasetsPage, ResourcesPage, AlertsPage: placeholders for you
data/
  turkana_places.json   sub-counties and main towns with coordinates (for Task 1)
  samples/              files for testing uploads, including some that must be rejected (Task 2)
```

The real CIS uses the same tools (React, FastAPI, SQLAlchemy, Leaflet), with PostgreSQL instead of SQLite.

## Run it

You need **Python 3.12+**, **Node.js 22+** and **Git**.

```bash
# Backend: http://localhost:8000, API docs at http://localhost:8000/docs
cd backend
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements-dev.txt
uvicorn app.main:app --reload --port 8000

# Frontend: http://localhost:5173 (in a second terminal)
cd frontend
npm install
npm run dev
```

The frontend sends `/api/...` requests to the backend on port 8000. To use another port, set `VITE_API_TARGET`, for example `VITE_API_TARGET=http://localhost:8010 npm run dev`.

Checks (the same ones run automatically on every pull request):

```bash
cd backend && pytest
cd frontend && npm run typecheck && npm run build
```

## How we work

The full rules are in **[CONTRIBUTING.md](CONTRIBUTING.md)**. In short:

1. Pick up a task's issue and assign yourself. Agree as a team who does what.
2. Create a branch from `main` for each piece of work: `task-1/fetch-forecast`, `task-2/upload-endpoint`…
3. Make small commits with clear messages, and push your branch.
4. Open a pull request, fill in the template, and ask a teammate to review.
5. The checks must pass and **another team member must approve** before it is merged. Nobody merges their own work unreviewed, and `main` cannot be pushed to directly.

Split the big tasks into several pull requests (for example, the backend endpoint first, then the page). Small pull requests are reviewed faster and conflict less.

## What we look at

| | |
|---|---|
| **It works** | Each task's acceptance checklist is met, and the app runs from a fresh clone by following this README |
| **It fails well** | Bad input, an unavailable outside service or a missing file gives a clear message, never a crash or a blank page |
| **It is tested** | Backend tests for the main paths and the important failures |
| **It is readable** | Clear names, small functions, consistent style; a teammate could pick it up |
| **Teamwork** | Focused pull requests with useful descriptions; real reviews (questions, suggestions, requested changes); conflicts resolved, not avoided by one person doing everything |
| **Honesty about data** | Data shows its source and time, and nothing is invented. A missing value is shown as missing, not as zero |

You do not need to finish every stretch goal. A smaller set of features that works well beats everything half-done.

## Getting help

Ask in the team's chat first: explaining a problem to a teammate is part of the exercise. If you are stuck on something outside the code (access, setup, unclear requirements), open an issue with the `question` label.

## Data and licences

- Place coordinates: © OpenStreetMap contributors, [ODbL](https://www.openstreetmap.org/copyright).
- Forecasts: [Open-Meteo](https://open-meteo.com/), free for non-commercial use, [CC BY 4.0](https://open-meteo.com/en/license). Credit it on the page.
- The sample datasets in `data/samples` are **synthetic** (made up for testing) and must not be used as real climate data.

Code in this repository: [MIT licence](LICENSE).
