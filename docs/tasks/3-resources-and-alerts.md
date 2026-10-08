# Task 3: Resources and alerts

**Goal:** let staff create, edit and publish **resources** (reports, guides, training material) and **alerts** (warnings about drought, floods, heat or strong wind), from the database through to the pages the public sees.

In the CIS, an alert can reach thousands of people, so the rules about what is shown, and when, matter more than the forms. An expired or withdrawn warning must never appear as current.

**Where:** `backend/app/routers/resources.py`, `backend/app/routers/alerts.py`, `backend/app/models.py`, `frontend/src/pages/ResourcesPage.tsx`, `frontend/src/pages/AlertsPage.tsx`, and any new files you need. Resources and alerts are separate, so two people can work on them at the same time.

## Resources

A resource has: title, description, category (*Publications*, *Training*, *Policy* or *Multimedia*), a link (URL), and a status (*draft* or *published*, with the time it was published).

| | |
|---|---|
| `GET /api/resources` | Published resources only, newest first. Add `?include_drafts=true` for the management view |
| `POST /api/resources` | Create (as a draft) |
| `GET`, `PATCH`, `DELETE /api/resources/{id}` | Read, edit, delete |
| `POST /api/resources/{id}/publish` | Publish |

## Alerts

An alert has:
- a title and a message;
- a severity: *advisory*, *watch*, *warning* or *emergency*;
- the areas it covers (one or more sub-counties from [`data/turkana_places.json`](../../data/turkana_places.json), or the whole county);
- `valid_from` and `valid_until`;
- a status: *draft*, *published* or *withdrawn*, with the time of each change.

| | |
|---|---|
| `GET /api/alerts?current=true` | Alerts in force now: published, not withdrawn, and now between `valid_from` and `valid_until`. Most severe first |
| `GET /api/alerts` | All alerts, for the management view |
| `POST /api/alerts` | Create (as a draft) |
| `GET`, `PATCH`, `DELETE /api/alerts/{id}` | Read, edit and delete **drafts** |
| `POST /api/alerts/{id}/publish` | Publish |
| `POST /api/alerts/{id}/withdraw` | Withdraw a published alert, with a reason |

The rules (the API must enforce them; the page only helps):

- [ ] `valid_until` must be after `valid_from`.
- [ ] An alert whose `valid_until` has passed cannot be published.
- [ ] A published alert cannot be edited or deleted, only withdrawn. To correct it, withdraw it and publish a new one. (People may already have acted on the first version.)
- [ ] All times include a timezone. Store them in UTC and show them in East Africa Time. Reject a time without a timezone (`422`).
- [ ] An expired or withdrawn alert never appears in `?current=true`.
- [ ] A rule broken gives `422` (or `409` for a wrong status) with a message saying which rule.
- [ ] Tests for each rule above, and for the order of current alerts.

Hint: for tests about "now", pass the current time into your function instead of reading the clock inside it, so a test can choose it.

## Frontend

**Resources page**
- [ ] The public list of published resources, by category.
- [ ] A "Manage" view: drafts and published resources, a form to create and edit, and a publish button.

**Alerts page**
- [ ] The current alerts, most severe first. Use the CIS colours: emergency red, warning orange, watch yellow, advisory blue. Show the severity as a word or icon too, because colour alone is not enough for everyone.
- [ ] For each alert: title, message, areas, and "valid until" in East Africa Time.
- [ ] "There are no current alerts" when there are none.
- [ ] A "Manage" view: all alerts with their status, a form to create and edit drafts with clear validation messages, and publish and withdraw buttons with a confirmation step.

There is no sign-in in this exercise: anyone can use the Manage views. (In the CIS, only certain roles can publish.)

## Stretch goals

- Filter current alerts by sub-county.
- Show an alert's areas on a small map.
- A simple admin key (a header checked by the API) so only staff can create and publish.
- Attach a file to a resource (talk to the Task 2 team about reusing their upload code).

## Done when

All the boxes above are ticked, through reviewed pull requests, and the tests prove that an expired or withdrawn alert can never be shown as current.
