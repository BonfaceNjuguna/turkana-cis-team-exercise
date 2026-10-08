// A small helper for calling the backend. Every path starts with /api, which the dev server forwards
// to the backend (see vite.config.ts).
//
//   const forecast = await api.get<Forecast>('/api/heat/forecast');
//   const alert = await api.post<Alert>('/api/alerts', { title: 'Strong wind', ... });
//
// For file uploads, pass a FormData as the body: api.post('/api/datasets', formData)

export class ApiError extends Error {
  constructor(public status: number, message: string) {
    super(message);
  }
}

async function request<T>(method: string, path: string, body?: unknown): Promise<T> {
  const isForm = body instanceof FormData;
  const response = await fetch(path, {
    method,
    headers: body === undefined || isForm ? undefined : { 'Content-Type': 'application/json' },
    body: body === undefined ? undefined : isForm ? body : JSON.stringify(body),
  });
  if (!response.ok) {
    // FastAPI puts its error message in "detail"; show that to the user when it is there.
    let message = `${response.status} ${response.statusText}`;
    try {
      const data = await response.json();
      if (typeof data.detail === 'string') message = data.detail;
      else if (Array.isArray(data.detail)) message = data.detail.map((d: { msg: string }) => d.msg).join('; ');
    } catch {
      // not JSON: keep the status text
    }
    throw new ApiError(response.status, message);
  }
  return (response.status === 204 ? undefined : await response.json()) as T;
}

export const api = {
  get: <T>(path: string) => request<T>('GET', path),
  post: <T>(path: string, body?: unknown) => request<T>('POST', path, body),
  patch: <T>(path: string, body: unknown) => request<T>('PATCH', path, body),
  delete: (path: string) => request<void>('DELETE', path),
};
