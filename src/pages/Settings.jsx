import { useState, useRef } from 'react'
import { useSettings } from '../hooks/useSettings'
import { exportAllProgress, importAllProgress, resetProgress } from '../lib/storage'

export default function Settings() {
  const { settings, setSettings } = useSettings()
  const [confirmReset, setConfirmReset] = useState(false)
  const [importMsg, setImportMsg] = useState(null)
  const fileRef = useRef()

  function handleExport() {
    const data = exportAllProgress()
    const blob = new Blob([JSON.stringify(data, null, 2)], { type: 'application/json' })
    const url  = URL.createObjectURL(blob)
    const a    = document.createElement('a')
    a.href = url
    a.download = `biostudy-backup-${new Date().toISOString().slice(0,10)}.json`
    a.click()
    URL.revokeObjectURL(url)
  }

  function handleImport(e) {
    const file = e.target.files?.[0]
    if (!file) return
    const reader = new FileReader()
    reader.onload = ev => {
      try {
        const blob = JSON.parse(ev.target.result)
        importAllProgress(blob)
        setImportMsg({ ok: true, text: 'Progress imported successfully. Refresh to apply.' })
      } catch {
        setImportMsg({ ok: false, text: 'Invalid file. Make sure it is a biostudy backup JSON.' })
      }
    }
    reader.readAsText(file)
    e.target.value = ''
  }

  function handleReset() {
    resetProgress()
    setConfirmReset(false)
    window.location.reload()
  }

  return (
    <div className="max-w-lg mx-auto space-y-8">
      <h1 className="text-3xl font-bold tracking-tight">Settings</h1>

      {/* Appearance */}
      <section className="card p-6 space-y-4">
        <h2 className="font-semibold text-sm uppercase tracking-wider text-slate-400 dark:text-slate-500">Appearance</h2>
        <div className="flex items-center justify-between">
          <div>
            <p className="font-medium">Dark mode</p>
            <p className="text-sm text-slate-400 dark:text-slate-500 mt-0.5">Switch between light and dark themes</p>
          </div>
          <button
            onClick={() => setSettings({ darkMode: !settings.darkMode })}
            className={`relative inline-flex h-7 w-12 shrink-0 cursor-pointer rounded-full border-2 border-transparent
                        transition-colors duration-200 focus:outline-none focus-visible:ring-2
                        focus-visible:ring-accent-500 focus-visible:ring-offset-2
                        ${settings.darkMode ? 'bg-accent-600' : 'bg-slate-200 dark:bg-slate-700'}`}
            role="switch"
            aria-checked={settings.darkMode}
          >
            <span className={`pointer-events-none inline-block h-6 w-6 transform rounded-full bg-white shadow
                              transition-transform duration-200
                              ${settings.darkMode ? 'translate-x-5' : 'translate-x-0'}`} />
          </button>
        </div>
      </section>

      {/* Exam */}
      <section className="card p-6 space-y-4">
        <h2 className="font-semibold text-sm uppercase tracking-wider text-slate-400 dark:text-slate-500">Exam defaults</h2>
        <div className="flex items-center justify-between gap-4">
          <div>
            <p className="font-medium">Exam duration (minutes)</p>
            <p className="text-sm text-slate-400 dark:text-slate-500 mt-0.5">Default total time allowed for an exam session</p>
          </div>
          <div className="flex items-center gap-2 shrink-0">
            <input
              type="number"
              min={5}
              max={240}
              value={settings.examDurationMins ?? 60}
              onChange={e => setSettings({ examDurationMins: Math.max(5, parseInt(e.target.value) || 60) })}
              className="w-20 rounded-xl border border-slate-200 dark:border-slate-700
                         bg-white dark:bg-slate-900 px-3 py-2 text-sm text-center
                         focus:outline-none focus:ring-2 focus:ring-accent-500"
            />
            <span className="text-sm text-slate-400">min</span>
          </div>
        </div>
      </section>

      {/* Data */}
      <section className="card p-6 space-y-4">
        <h2 className="font-semibold text-sm uppercase tracking-wider text-slate-400 dark:text-slate-500">Progress data</h2>

        <div className="flex items-start justify-between gap-4">
          <div>
            <p className="font-medium">Export progress</p>
            <p className="text-sm text-slate-400 dark:text-slate-500 mt-0.5">Download a backup JSON of all your study data</p>
          </div>
          <button onClick={handleExport} className="btn-outline shrink-0">Export</button>
        </div>

        <div className="flex items-start justify-between gap-4">
          <div>
            <p className="font-medium">Import progress</p>
            <p className="text-sm text-slate-400 dark:text-slate-500 mt-0.5">Restore from a previously exported backup</p>
          </div>
          <button onClick={() => fileRef.current?.click()} className="btn-outline shrink-0">Import</button>
          <input ref={fileRef} type="file" accept=".json" className="hidden" onChange={handleImport} />
        </div>

        {importMsg && (
          <div className={`rounded-xl px-4 py-3 text-sm font-medium
            ${importMsg.ok
              ? 'bg-green-50 text-green-700 dark:bg-green-900/30 dark:text-green-300'
              : 'bg-red-50 text-red-700 dark:bg-red-900/30 dark:text-red-300'
            }`}>
            {importMsg.text}
          </div>
        )}

        <hr className="border-slate-100 dark:border-slate-800" />

        <div className="flex items-start justify-between gap-4">
          <div>
            <p className="font-medium text-red-600 dark:text-red-400">Reset all progress</p>
            <p className="text-sm text-slate-400 dark:text-slate-500 mt-0.5">
              Permanently clears flashcard schedules, quiz stats, and exam history
            </p>
          </div>
          {!confirmReset ? (
            <button onClick={() => setConfirmReset(true)} className="btn-danger shrink-0">Reset</button>
          ) : (
            <div className="flex gap-2 shrink-0">
              <button onClick={() => setConfirmReset(false)} className="btn-ghost text-sm">Cancel</button>
              <button onClick={handleReset} className="btn-danger text-sm">Confirm</button>
            </div>
          )}
        </div>
      </section>

      <p className="text-xs text-center text-slate-300 dark:text-slate-700">
        All data stored locally in your browser via localStorage.
      </p>
    </div>
  )
}
