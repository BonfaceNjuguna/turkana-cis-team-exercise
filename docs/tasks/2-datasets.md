# Task 2: Datasets

**Goal:** a catalogue of climate data files: upload, list, view, edit and delete them, for **NetCDF** (`.nc`, the usual format for gridded climate data such as satellite rainfall) and **CSV** files.

In the CIS, partners (the meteorological department, universities, NGOs) upload their data this way. Real uploads go wrong in many ways: wrong formats, empty files, files renamed to the wrong extension. Handling those well is the main point of this task.

**Where:** `backend/app/routers/datasets.py`, `backend/app/models.py`, `frontend/src/pages/DatasetsPage.tsx`, and any new files you need.
**Uploaded files** go in the folder set by `STORAGE_DIR` (default `backend/storage/`, already ignored by Git).
**Test files:** [`data/samples`](../../data/samples), described in its [README](../../data/samples/README.md).

## Backend

A `Dataset` table with at least: name, description, source (who provided it), format, original file name, stored file name, size, upload time, last-updated time, and what was read from the file:

- **NetCDF:** the variables (with units where the file gives them), the time range, and the area covered (latitude and longitude range);
- **CSV:** the columns, the number of rows, and the time range if there is a date column.

Suggested endpoints:

| | |
|---|---|
| `POST /api/datasets` | Upload (multipart form: `file`, `name`, `description`, `source`). Returns `201` and the dataset |
| `GET /api/datasets` | List, newest first |
| `GET /api/datasets/{id}` | One dataset with its metadata |
| `PATCH /api/datasets/{id}` | Change name, description or source |
| `DELETE /api/datasets/{id}` | Delete the record **and** the stored file. Returns `204` |
| `GET /api/datasets/{id}/download` | The original file, under its original name |

It must:

- [ ] Accept only NetCDF and CSV, **checked by content, not just the extension**. A text file renamed to `.nc` must be rejected. Hint: NetCDF files start with `CDF` or `\x89HDF`.
- [ ] Reject empty files, and files over 50 MB (`413`).
- [ ] Reject files it cannot read, with a reason the user can act on (`422`, for example "The CSV has no header row").
- [ ] **Leave nothing behind on failure:** a rejected upload creates no database row and no stored file.
- [ ] Store files under a generated name (not the uploaded name), so two uploads called `data.nc` do not overwrite each other and a name like `../../etc/passwd` cannot escape the storage folder.
- [ ] Return `404` for a dataset that does not exist.
- [ ] Have tests for: a good NetCDF upload (metadata read correctly), a good CSV upload, each rejected sample file, edit, delete (file gone too), and download.

Hint: [xarray](https://docs.xarray.dev/) reads NetCDF (`xarray.open_dataset`) and [pandas](https://pandas.pydata.org/) reads CSV. Both are installed.

## Frontend

On the Datasets page:

- [ ] An upload form (file, name, description, source) that shows the API's error message when an upload is rejected.
- [ ] A list of datasets: name, format, size, upload date.
- [ ] A detail view with the metadata (variables, time range, area or columns), and a download link.
- [ ] Edit name, description and source.
- [ ] Delete, with a confirmation step.
- [ ] Loading and empty states ("No datasets yet").

## Stretch goals

- CSV preview: the first 20 rows as a table.
- For a NetCDF variable, a chart of its average over time (one value per time step).
- Upload progress for large files.
- Search the list by name or source.

## Done when

All the boxes above are ticked, through reviewed pull requests, and every file in `data/samples` behaves as its README says.
