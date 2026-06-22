import { useState, useEffect, useCallback, useMemo } from 'react'
import { useSearchParams, Link } from 'react-router-dom'
import content from '../data/content.json'
import ProgressBar from '../components/ProgressBar'
import DifficultyBadge from '../components/DifficultyBadge'
import { useFlashcards } from '../hooks/useFlashcards'
import { isDueToday } from '../lib/sm2'

const EXAM_PRESETS = [
  { id: 'exam1', label: 'Exam I',   date: 'June 26', chapterIds: ['ch1','ch2','ch3'] },
  { id: 'exam2', label: 'Exam II',  date: 'July 10',  chapterIds: ['ch4','ch5','ch6'] },
  { id: 'exam3', label: 'Exam III', date: 'July 31',  chapterIds: ['ch7','ch8','ch9','ch10','ch11'] },
  { id: 'exam4', label: 'Exam IV',  date: 'Aug 7',    chapterIds: ['ch12','ch13','ch14','ch15'] },
]

function fcCount(chapterIds) {
  return content.chapters
    .filter(c => chapterIds.includes(c.id))
    .reduce((sum, c) => sum + c.flashcards.length, 0)
}

// Shuffle helper
function shuffle(arr) {
  const a = [...arr]
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [a[i], a[j]] = [a[j], a[i]]
  }
  return a
}

// ─── Card selector UI ────────────────────────────────────────────────────────

function Selector({ onStart }) {
  const [mode, setMode] = useState('chapter')
  const [chapterId, setChapterId] = useState(content.chapters[0]?.id ?? '')
  const [sectionId, setSectionId] = useState('')
  const [examId, setExamId] = useState(null)

  const chapter = content.chapters.find(c => c.id === chapterId)
  const sections = chapter?.sections ?? []
  const selectedExam = EXAM_PRESETS.find(e => e.id === examId)

  const canStart = mode !== 'exam' || (selectedExam && fcCount(selectedExam.chapterIds) > 0)

  function handleStart() {
    if (mode === 'exam') {
      onStart({ mode, chapterIds: selectedExam?.chapterIds ?? [] })
    } else {
      onStart({ mode, chapterId, sectionId })
    }
  }

  return (
    <div className="max-w-md mx-auto space-y-6">
      <h1 className="text-3xl font-bold tracking-tight">Flashcards</h1>

      <div className="card p-6 space-y-5">
        {/* Mode */}
        <div>
          <label className="block text-sm font-medium mb-2">Study mode</label>
          <div className="flex gap-2 flex-wrap">
            {[
              { value: 'due',     label: 'Due today' },
              { value: 'chapter', label: 'By chapter' },
              { value: 'section', label: 'By section' },
              { value: 'exam',    label: 'By exam' },
            ].map(opt => (
              <button
                key={opt.value}
                onClick={() => setMode(opt.value)}
                className={`px-4 py-2 rounded-xl text-sm font-medium border transition-all
                  ${mode === opt.value
                    ? 'bg-accent-600 text-white border-accent-600 dark:bg-accent-500 dark:border-accent-500'
                    : 'border-slate-200 text-slate-600 hover:bg-slate-50 dark:border-slate-700 dark:text-slate-400 dark:hover:bg-slate-800'
                  }`}
              >
                {opt.label}
              </button>
            ))}
          </div>
        </div>

        {/* Exam picker */}
        {mode === 'exam' && (
          <div className="grid grid-cols-2 gap-2">
            {EXAM_PRESETS.map(preset => {
              const count = fcCount(preset.chapterIds)
              const hasContent = count > 0
              const isSelected = examId === preset.id
              return (
                <button
                  key={preset.id}
                  onClick={() => hasContent && setExamId(preset.id)}
                  disabled={!hasContent}
                  className={`rounded-xl p-3 text-left border-2 transition-all
                    ${!hasContent
                      ? 'border-slate-100 dark:border-slate-800 opacity-40 cursor-not-allowed'
                      : isSelected
                        ? 'border-accent-500 bg-accent-50 dark:bg-accent-900/30'
                        : 'border-slate-200 dark:border-slate-700 hover:border-accent-300 dark:hover:border-accent-700'
                    }`}
                >
                  <p className={`font-bold text-sm ${isSelected ? 'text-accent-600 dark:text-accent-400' : 'text-slate-900 dark:text-slate-100'}`}>
                    {preset.label}
                  </p>
                  <p className="text-xs text-slate-400 dark:text-slate-500 mt-0.5">{preset.date}</p>
                  <p className="text-xs font-medium text-accent-600 dark:text-accent-400 mt-1">
                    {hasContent ? `${count} cards` : 'Coming soon'}
                  </p>
                </button>
              )
            })}
          </div>
        )}

        {/* Chapter picker */}
        {(mode === 'chapter' || mode === 'section') && (
          <div>
            <label className="block text-sm font-medium mb-2">Chapter</label>
            <select
              value={chapterId}
              onChange={e => { setChapterId(e.target.value); setSectionId('') }}
              className="w-full rounded-xl border border-slate-200 dark:border-slate-700
                         bg-white dark:bg-slate-900 px-3 py-2 text-sm focus:outline-none
                         focus:ring-2 focus:ring-accent-500"
            >
              {content.chapters.map(c => (
                <option key={c.id} value={c.id}>{c.id.toUpperCase()} — {c.title}</option>
              ))}
            </select>
          </div>
        )}

        {/* Section picker */}
        {mode === 'section' && (
          <div>
            <label className="block text-sm font-medium mb-2">Section</label>
            <select
              value={sectionId}
              onChange={e => setSectionId(e.target.value)}
              className="w-full rounded-xl border border-slate-200 dark:border-slate-700
                         bg-white dark:bg-slate-900 px-3 py-2 text-sm focus:outline-none
                         focus:ring-2 focus:ring-accent-500"
            >
              <option value="">All sections</option>
              {sections.map(s => (
                <option key={s.id} value={s.id}>{s.id} — {s.title}</option>
              ))}
            </select>
          </div>
        )}

        <button
          onClick={handleStart}
          disabled={!canStart}
          className="btn-primary w-full disabled:opacity-40"
        >
          Start Studying
        </button>
      </div>
    </div>
  )
}

// ─── Session ─────────────────────────────────────────────────────────────────

function Session({ cards: initialCards, onExit }) {
  const { getCardState, rate } = useFlashcards()
  const [queue, setQueue] = useState(() => shuffle(initialCards))
  const [index, setIndex] = useState(0)
  const [flipped, setFlipped] = useState(false)
  const [sessionDone, setSessionDone] = useState(false)
  const [rated, setRated] = useState(0) // how many rated this session

  const card = queue[index]
  const total = queue.length

  function flip() {
    setFlipped(f => !f)
  }

  function handleRate(rating) {
    rate(card.id, rating)
    setRated(r => r + 1)

    if (rating === 0) {
      // Put back near end of queue so it comes up again
      setQueue(prev => {
        const next = [...prev]
        const [removed] = next.splice(index, 1)
        const insertAt = Math.min(next.length, index + 3)
        next.splice(insertAt, 0, removed)
        return next
      })
      // Stay at same index (next card slides in)
      setFlipped(false)
    } else {
      if (index >= queue.length - 1) {
        setSessionDone(true)
      } else {
        setIndex(i => i + 1)
        setFlipped(false)
      }
    }
  }

  // Keyboard shortcuts
  useEffect(() => {
    function handler(e) {
      if (e.target.tagName === 'INPUT' || e.target.tagName === 'SELECT') return
      if (e.key === ' ') { e.preventDefault(); flip() }
      if (flipped) {
        if (e.key === '1') handleRate(0)
        if (e.key === '2') handleRate(1)
        if (e.key === '3') handleRate(2)
      }
    }
    window.addEventListener('keydown', handler)
    return () => window.removeEventListener('keydown', handler)
  }, [flipped, index, queue])

  if (total === 0) {
    return (
      <div className="max-w-lg mx-auto text-center space-y-4 pt-16">
        <p className="text-2xl font-semibold">No cards to study!</p>
        <p className="text-slate-500 dark:text-slate-400">Nothing is due in this selection.</p>
        <button onClick={onExit} className="btn-outline">Back</button>
      </div>
    )
  }

  if (sessionDone) {
    return (
      <div className="max-w-lg mx-auto text-center space-y-6 pt-16">
        <div className="text-5xl">🎉</div>
        <h2 className="text-2xl font-bold">Session Complete!</h2>
        <p className="text-slate-500 dark:text-slate-400">
          You rated {rated} card{rated !== 1 ? 's' : ''} this session.
        </p>
        <div className="flex gap-3 justify-center">
          <button onClick={onExit} className="btn-outline">Exit</button>
          <button onClick={() => { setQueue(shuffle(initialCards)); setIndex(0); setFlipped(false); setSessionDone(false); setRated(0) }}
                  className="btn-primary">
            Study Again
          </button>
        </div>
      </div>
    )
  }

  const progress = index / total

  return (
    <div className="max-w-2xl mx-auto space-y-6">
      {/* Header */}
      <div className="flex items-center justify-between">
        <button onClick={onExit} className="btn-ghost text-sm">
          ← Back
        </button>
        <div className="text-sm text-slate-500 dark:text-slate-400 font-medium">
          {index + 1} / {total}
        </div>
        <DifficultyBadge difficulty={card.difficulty} />
      </div>

      <ProgressBar value={index} max={total} />

      {/* Flip card */}
      <div
        className="flip-card w-full cursor-pointer"
        style={{ height: 'clamp(280px, 45vw, 380px)' }}
        onClick={flip}
        role="button"
        tabIndex={0}
        onKeyDown={e => e.key === 'Enter' && flip()}
        aria-label={flipped ? 'Show front' : 'Reveal answer'}
      >
        <div className={`flip-card-inner w-full h-full ${flipped ? 'flipped' : ''}`}>
          {/* Front */}
          <div className="flip-card-face absolute inset-0 card p-8 flex flex-col items-center justify-center text-center">
            {card.image && (
              <img
                src={card.image}
                alt=""
                className="max-w-full max-h-32 object-contain rounded-xl mb-4"
              />
            )}
            <p className="text-xl font-semibold leading-snug text-slate-900 dark:text-slate-100">
              {card.front}
            </p>
            <p className="mt-4 text-sm text-slate-400 dark:text-slate-500">
              tap or press Space to reveal
            </p>
          </div>
          {/* Back */}
          <div className="flip-card-face flip-card-back absolute inset-0 card p-8 flex flex-col items-center justify-center text-center bg-accent-50 dark:bg-accent-950/30 border-accent-200 dark:border-accent-800">
            {card.image && (
              <img
                src={card.image}
                alt=""
                className="max-w-full max-h-32 object-contain rounded-xl mb-4"
              />
            )}
            <p className="text-lg leading-relaxed text-slate-800 dark:text-slate-200">
              {card.back}
            </p>
          </div>
        </div>
      </div>

      {/* Rate buttons */}
      <div className={`grid grid-cols-3 gap-3 transition-opacity duration-200 ${flipped ? 'opacity-100' : 'opacity-0 pointer-events-none'}`}>
        <button
          onClick={() => handleRate(0)}
          className="btn border-2 border-red-200 bg-red-50 text-red-700 hover:bg-red-100
                     dark:border-red-800 dark:bg-red-950/30 dark:text-red-400 dark:hover:bg-red-900/40
                     flex-col py-3 gap-0.5"
        >
          <span className="font-bold">Again</span>
          <span className="text-xs opacity-70">1</span>
        </button>
        <button
          onClick={() => handleRate(1)}
          className="btn border-2 border-amber-200 bg-amber-50 text-amber-700 hover:bg-amber-100
                     dark:border-amber-800 dark:bg-amber-950/30 dark:text-amber-400 dark:hover:bg-amber-900/40
                     flex-col py-3 gap-0.5"
        >
          <span className="font-bold">Good</span>
          <span className="text-xs opacity-70">2</span>
        </button>
        <button
          onClick={() => handleRate(2)}
          className="btn border-2 border-green-200 bg-green-50 text-green-700 hover:bg-green-100
                     dark:border-green-800 dark:bg-green-950/30 dark:text-green-400 dark:hover:bg-green-900/40
                     flex-col py-3 gap-0.5"
        >
          <span className="font-bold">Easy</span>
          <span className="text-xs opacity-70">3</span>
        </button>
      </div>

      <p className="text-center text-xs text-slate-400 dark:text-slate-600">
        Space = flip · 1/2/3 = Again / Good / Easy
      </p>
    </div>
  )
}

// ─── Page root ────────────────────────────────────────────────────────────────

export default function Flashcards() {
  const [searchParams] = useSearchParams()
  const { schedules } = useFlashcards()

  const [session, setSession] = useState(null)

  // Pre-select from query params
  useEffect(() => {
    const mode = searchParams.get('mode')
    const chapter = searchParams.get('chapter')
    if (mode === 'due' || chapter) {
      setSession({ mode: mode ?? 'chapter', chapterId: chapter ?? content.chapters[0]?.id, sectionId: '' })
    }
  }, [])

  const sessionCards = useMemo(() => {
    if (!session) return []
    const { mode, chapterId, sectionId, chapterIds } = session
    let cards = []
    if (mode === 'due') {
      cards = content.chapters.flatMap(ch => ch.flashcards).filter(c => isDueToday(schedules[c.id]))
    } else if (mode === 'exam') {
      cards = content.chapters.filter(c => (chapterIds ?? []).includes(c.id)).flatMap(c => c.flashcards)
    } else if (mode === 'chapter') {
      cards = content.chapters.find(c => c.id === chapterId)?.flashcards ?? []
    } else {
      const ch = content.chapters.find(c => c.id === chapterId)
      cards = ch ? ch.flashcards.filter(c => !sectionId || c.section === sectionId) : []
    }
    return cards
  }, [session, schedules])

  if (session) {
    return <Session cards={sessionCards} onExit={() => setSession(null)} />
  }

  return <Selector onStart={setSession} />
}
