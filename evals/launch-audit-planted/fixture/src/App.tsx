import hero from './assets/hero.png'

export default function App() {
  return (
    <main className="page">
      <header className="nav">
        <span className="brand">Tidepool</span>
        <a href="/pricing">Pricing</a>
      </header>

      <section className="hero">
        <h1>Plan your week of tide-pooling</h1>
        <p>Tide tables, low-tide alerts and a log of what you found, for the beaches near you.</p>
        <img src={hero} alt="image" />
      </section>

      <section className="testimonials">
        <blockquote>
          "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
          <cite>John Doe, CEO of Your Company</cite>
        </blockquote>
      </section>

      <footer>
        <p>Contact us at hello@example.com</p>
        <p>© 2023 Tidepool</p>
      </footer>

      <a className="lovable-badge" href="https://lovable.dev">Edit with Lovable</a>
    </main>
  )
}
