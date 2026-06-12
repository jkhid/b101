export default function DifficultyBadge({ difficulty }) {
  const cls = {
    easy:   'badge-easy',
    medium: 'badge-medium',
    hard:   'badge-hard',
  }[difficulty] ?? 'badge bg-slate-100 text-slate-600'
  return <span className={cls}>{difficulty}</span>
}
