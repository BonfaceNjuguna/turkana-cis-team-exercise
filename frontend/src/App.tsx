import { NavLink, Route, Routes } from 'react-router-dom';
import AlertsPage from './pages/AlertsPage';
import DatasetsPage from './pages/DatasetsPage';
import HeatMapPage from './pages/HeatMapPage';
import HomePage from './pages/HomePage';
import ResourcesPage from './pages/ResourcesPage';

// Every task's page is already linked here, so nobody needs to edit this file to start.
const NAV = [
  { to: '/', label: 'Home' },
  { to: '/heat', label: 'Heat map' },
  { to: '/datasets', label: 'Datasets' },
  { to: '/resources', label: 'Resources' },
  { to: '/alerts', label: 'Alerts' },
];

export default function App() {
  return (
    <div className="min-h-screen flex flex-col">
      <header className="bg-[#7a3b1d] text-white">
        <div className="max-w-6xl mx-auto px-4 py-3 flex flex-wrap items-center gap-x-6 gap-y-2">
          <span className="font-semibold">Turkana CIS exercise</span>
          <nav className="flex flex-wrap gap-1 text-sm" aria-label="Main">
            {NAV.map(item => (
              <NavLink key={item.to} to={item.to} end={item.to === '/'}
                className={({ isActive }) => `px-3 py-1.5 rounded ${isActive ? 'bg-white text-[#7a3b1d]' : 'hover:bg-white/15'}`}>
                {item.label}
              </NavLink>
            ))}
          </nav>
        </div>
      </header>
      <main className="flex-1 max-w-6xl w-full mx-auto px-4 py-6">
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/heat" element={<HeatMapPage />} />
          <Route path="/datasets" element={<DatasetsPage />} />
          <Route path="/resources" element={<ResourcesPage />} />
          <Route path="/alerts" element={<AlertsPage />} />
          <Route path="*" element={<p>Page not found.</p>} />
        </Routes>
      </main>
    </div>
  );
}
