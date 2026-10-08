# Task 1: Heat map

**Goal:** show the coming week's temperature and humidity for Turkana's sub-counties and main towns, on a map with a table alongside, using the free [Open-Meteo forecast API](https://open-meteo.com/en/docs).

In the CIS, the same data drives a heat stress product that warns communities about dangerous heat. In Turkana, daytime temperatures often pass 35 °C.

**Where:** `backend/app/routers/heat.py`, `frontend/src/pages/HeatMapPage.tsx`, and any new files you need.
**Places:** [`data/turkana_places.json`](../../data/turkana_places.json): each place's name, sub-county and coordinates.

## Backend

Add an endpoint, for example `GET /api/heat/forecast`, that returns for each place:

- the place (name, sub-county, coordinates);
- for each of the next 7 days (dates in East Africa Time, `Africa/Nairobi`):
  - the highest temperature (°C), and when it is expected,
  - the relative humidity (%) at that time,
  - the lowest temperature (°C);
- when the forecast was fetched, and its source ("Open-Meteo").

Get hourly `temperature_2m` and `relative_humidity_2m` from Open-Meteo. Hint: one request can ask for many places at once (comma-separated latitudes and longitudes), and the answer is a list in the same order.

It must:

- [ ] **Not call Open-Meteo on every page load.** Keep the result for at least 15 minutes and reuse it.
- [ ] **Handle Open-Meteo being slow or down.** Use a timeout. If it fails, answer with a clear error (for example `503` and a message), not a crash and not an empty forecast that looks real.
- [ ] **Never turn missing values into numbers.** A missing hour is `null`, not `0`. A day with too few hours should be left out or marked incomplete, because it could miss the afternoon peak.
- [ ] Have tests that **do not call the real Open-Meteo** (fake its response): one for the summary (highest temperature and its humidity), one for missing values, and one for Open-Meteo failing.

## Frontend

On the Heat map page:

- [ ] A map of Turkana with a marker for every place. Colour each marker by the chosen day's highest temperature, and add a legend explaining the colours.
- [ ] Clicking a marker shows the place's name, sub-county, highest temperature, humidity and time.
- [ ] A table alongside: one row per place, one column per day, showing the highest temperature (and humidity).
- [ ] A day selector that changes the map colours.
- [ ] The source and time of the forecast on the page ("Forecast: Open-Meteo, fetched 14:05 EAT"), and the map's tile attribution.
- [ ] A loading state, and a clear message when the forecast is unavailable.
- [ ] Usable on a phone (about 390 px wide): the table may scroll sideways, but the page must not break.

Hints: [react-leaflet](https://react-leaflet.js.org/) is installed; also import `leaflet/dist/leaflet.css`, or the map tiles will be scattered. Turkana is roughly latitude 1.5°–5.5° N, longitude 34°–36.5° E. Use `https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png` tiles with the attribution "© OpenStreetMap contributors".

## Stretch goals

- **Heat index ("feels like"):** combine temperature and humidity with the NOAA/NWS [Heat Index formula](https://www.wpc.ncep.noaa.gov/html/heatindex_equation.shtml) (the Rothfusz regression, with its adjustments). Then show a level for each day: below 27 °C *normal*, 27–32 *caution*, 32–41 *extreme caution*, 41–54 *danger*, 54 or more *extreme danger*. Test your function against a few values from the NWS heat index chart.
- Let the user add a place by clicking the map.
- A small chart of the hourly temperature for one place.

## Done when

All the boxes above are ticked, through reviewed pull requests, and someone who did not build it can explain the page to a county officer.
