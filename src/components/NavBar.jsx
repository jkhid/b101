import { Link, NavLink } from 'react-router-dom'

const links = [
  { to: '/',           label: 'Home' },
  { to: '/flashcards', label: 'Flashcards' },
  { to: '/quiz',       label: 'Quiz' },
  { to: '/exam',       label: 'Exam' },
  { to: '/settings',   label: 'Settings' },
]

export default function NavBar() {
  return (
    <header className="sticky top-0 z-50 bg-white/80 backdrop-blur-md border-b border-slate-100
                       dark:bg-slate-950/80 dark:border-slate-800">
      <nav className="max-w-5xl mx-auto px-4 h-14 flex items-center justify-between gap-4">
        <Link to="/" className="flex items-center gap-2 shrink-0">
          <span className="text-lg font-bold text-accent-600 dark:text-accent-400 tracking-tight">
            BIO 101
          </span>
        </Link>
        <ul className="flex items-center gap-1 overflow-x-auto">
          {links.map(({ to, label }) => (
            <li key={to}>
              <NavLink
                to={to}
                end={to === '/'}
                className={({ isActive }) =>
                  `px-3 py-1.5 rounded-lg text-sm font-medium transition-colors whitespace-nowrap
                   ${isActive
                     ? 'bg-accent-50 text-accent-700 dark:bg-accent-900/40 dark:text-accent-300'
                     : 'text-slate-500 hover:text-slate-900 hover:bg-slate-50 dark:text-slate-400 dark:hover:text-slate-100 dark:hover:bg-slate-800'
                   }`
                }
              >
                {label}
              </NavLink>
            </li>
          ))}
        </ul>
      </nav>
    </header>
  )
}
