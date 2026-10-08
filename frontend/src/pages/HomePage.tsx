import { useEffect, useState } from 'react';
import { api } from '../api/client';

interface Health {
  status: string;
  time: string;
  places: number;
}

// A working example of calling the backend, with loading and error states.
export default function HomePage() {
  const [health, setHealth] = useState<Health | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    api.get<Health>('/api/health').then(setHealth).catch((e: Error) => setError(e.message));
  }, []);

  return (
    <section className="space-y-4">
      <h1 className="text-2xl font-semibold">Turkana CIS team exercise</h1>
      <p className="text-gray-700 max-w-2xl">
        Three features of the Turkana County Climate Information System, built by the team. Start with
        Task 0 in the README, then use the pages above.
      </p>
      <div className="bg-white border border-gray-200 rounded-lg p-4 max-w-md text-sm">
        <h2 className="font-semibold mb-1">Backend</h2>
        {!health && !error && <p className="text-gray-500">Checking…</p>}
        {error && <p className="text-red-700">Cannot reach the backend: {error}. Is it running on port 8000?</p>}
        {health && <p className="text-green-800">Connected. {health.places} places loaded.</p>}
      </div>
    </section>
  );
}
