export default function ProgressBar({ value, max, className = '', colorClass = 'bg-accent-500' }) {
  const pct = max > 0 ? Math.round((value / max) * 100) : 0
  return (
    <div className={`relative h-2 bg-slate-100 dark:bg-slate-800 rounded-full overflow-hidden ${className}`}>
      <div
        className={`absolute inset-y-0 left-0 rounded-full transition-all duration-500 ${colorClass}`}
        style={{ width: `${pct}%` }}
      />
    </div>
  )
}
