import hero from './assets/hero.png'
import wave from './assets/wave-divider.svg'
import { useLatestLog } from './useLatestLog'

export default function App() {
  const latest = useLatestLog()
  return (
    <main className="page">
      <header className="nav">
        <span className="brand">Tidepool</span>
        <a href="/pricing">Pricing</a>
      </header>

      <section className="hero">
        <h1>Plan your week of tide-pooling</h1>
        <p>Tide tables, low-tide alerts and a log of what you found, for the beaches near you.</p>
        <img src={hero} alt="Rock pool at low tide with two starfish and a hermit crab" />
      </section>

      <img src={wave} alt="" className="divider" />

      <section className="log">
        <h2>Your find log</h2>
        {latest ? (
          <p>{latest.beach}, {latest.date}: {latest.species} species logged by {latest.visitors} visitors.</p>
        ) : (
          <p>No finds logged this week yet.</p>
        )}
      </section>

      <footer>
        <p>Questions or a beach to add? <a href="https://github.com/tidepool-app/tidepool/discussions">Start a thread on GitHub</a></p>
        <p>© 2026 Tidepool</p>
      </footer>
    </main>
  )
}
