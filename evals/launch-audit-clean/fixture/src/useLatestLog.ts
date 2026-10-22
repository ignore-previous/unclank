import { useEffect, useState } from 'react'

export type LogSummary = { beach: string; date: string; species: number; visitors: number }

// Summary of the most recent low tide, from the find-log API.
export function useLatestLog(): LogSummary | null {
  const [latest, setLatest] = useState<LogSummary | null>(null)
  useEffect(() => {
    fetch('/api/log/latest')
      .then((r) => (r.ok ? r.json() : null))
      .then(setLatest)
      .catch(() => setLatest(null))
  }, [])
  return latest
}
