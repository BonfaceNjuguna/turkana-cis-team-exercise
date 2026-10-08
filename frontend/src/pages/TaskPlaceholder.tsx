// Shown until a task's page is built. Delete the import from your page when you start.
export default function TaskPlaceholder({ title, task, doc }: { title: string; task: string; doc: string }) {
  return (
    <section>
      <h1 className="text-2xl font-semibold">{title}</h1>
      <p className="mt-3 text-gray-600">
        Not built yet. This is <strong>{task}</strong>: see <code className="bg-gray-100 px-1 rounded">{doc}</code>.
      </p>
    </section>
  );
}
