# Sample files for Task 2

All data here is **synthetic** (random values made up for testing). Never use it as real climate data.

| File | What it is | Expected result |
|---|---|---|
| `rainfall_monthly_synthetic.nc` | NetCDF: monthly rainfall, Jan 2024 to Dec 2025, on a 0.25° grid over Turkana. Variable `precip` (mm/month) | **Accepted.** Variables, time range and area read from the file |
| `station_daily_synthetic.csv` | CSV: daily max/min temperature and rain at three stations, August 2026 | **Accepted.** Columns, row count (93) and date range read from the file |
| `empty.csv` | A file with nothing in it | **Rejected** (empty) |
| `not_really_netcdf.nc` | A text file renamed to `.nc` | **Rejected** (not NetCDF, whatever its name says) |
| `truncated.nc` | The first 300 bytes of a real NetCDF file, so it starts like one but cannot be read | **Rejected** (cannot be read) |
| `notes.txt` | A text file | **Rejected** (unsupported type) |

A rejected file must leave no record in the database and no file in storage.
