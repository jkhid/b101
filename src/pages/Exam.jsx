import { useState, useMemo, useEffect, useRef, useCallback } from 'react'
import { useSearchParams } from 'react-router-dom'
import content from '../data/content.json'
import ProgressBar from '../components/ProgressBar'
import DifficultyBadge from '../components/DifficultyBadge'
import { useExamHistory } from '../hooks/useExamHistory'
import { useSettings } from '../hooks/useSettings'

// ─── Course exam schedule ──────────────────────────────────────────────────────
const EXAM_PRESETS = [
  {
    id: 'exam1',
    label: 'Exam I',
    date: 'June 26',
    chapterIds: ['ch1', 'ch2', 'ch3'],
    description: 'Scientific Study of Life · Chemistry of Life · Cells',
  },
  {
    id: 'exam2',
    label: 'Exam II',
    date: 'July 10',
    chapterIds: ['ch4', 'ch5', 'ch6'],
    description: 'Energy of Life · Photosynthesis · Respiration & Fermentation',
  },
  {
    id: 'exam3',
    label: 'Exam III',
    date: 'July 31',
    chapterIds: ['ch7', 'ch8', 'ch9', 'ch10', 'ch11'],
    description: 'DNA Structure · Replication & Mitosis · Meiosis · Inheritance · DNA Technology',
  },
  {
    id: 'exam4',
    label: 'Exam IV',
    date: 'Aug 7',
    chapterIds: ['ch12', 'ch13', 'ch14', 'ch15'],
    description: 'Evolutionary Change · Evidence of Evolution · Speciation · Origin of Life',
  },
]

function getPresetLabel(chapterIdsOrId) {
  if (!chapterIdsOrId) return null
  const ids = Array.isArray(chapterIdsOrId) ? chapterIdsOrId : [chapterIdsOrId]
  const preset = EXAM_PRESETS.find(p =>
    p.chapterIds.length === ids.length &&
    p.chapterIds.every(id => ids.includes(id))
  )
  return preset?.label ?? null
}

function getQuestionsForChapters(chapterIds) {
  if (chapterIds === 'all') return content.chapters.flatMap(c => c.quiz)
  const ids = Array.isArray(chapterIds) ? chapterIds : [chapterIds]
  return content.chapters.filter(c => ids.includes(c.id)).flatMap(c => c.quiz)
}

function shuffle(arr) {
  const a = [...arr]
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [a[i], a[j]] = [a[j], a[i]]
  }
  return a
}

function shuffleQuestion(q) {
  const indexed = q.choices.map((text, i) => ({ text, isCorrect: i === q.answerIndex }))
  const shuffled = shuffle(indexed)
  return {
    ...q,
    choices: shuffled.map(c => c.text),
    answerIndex: shuffled.findIndex(c => c.isCorrect),
  }
}

// ─── Selector ─────────────────────────────────────────────────────────────────

function Selector({ onStart, examHistory, initialPresetId }) {
  const { settings } = useSettings()
  const [mode, setMode] = useState('preset')
  const [selectedPreset, setSelectedPreset] = useState(() => {
    if (!initialPresetId) return null
    return EXAM_PRESETS.find(p => p.id === initialPresetId) ?? null
  })
  const [chapterId, setChapterId] = useState('all')
  const [count, setCount] = useState(() => {
    if (!initialPresetId) return 40
    const preset = EXAM_PRESETS.find(p => p.id === initialPresetId)
    if (!preset) return 40
    const available = getQuestionsForChapters(preset.chapterIds).length
    return Math.min(40, available)
  })
  const [durationMins, setDurationMins] = useState(settings.examDurationMins ?? 60)

  const activeChapterIds = mode === 'preset' && selectedPreset
    ? selectedPreset.chapterIds
    : chapterId

  const maxQuestions = useMemo(
    () => getQuestionsForChapters(activeChapterIds).length,
    [activeChapterIds]
  )

  const actualCount = Math.min(count, maxQuestions)

  function handlePresetClick(preset) {
    setSelectedPreset(preset)
    // Default to ~40 questions (or all if fewer available)
    const available = getQuestionsForChapters(preset.chapterIds).length
    setCount(Math.min(40, available))
  }

  function handleStart() {
    onStart({
      chapterIds: activeChapterIds,
      count: actualCount,
      durationMins,
      presetId: mode === 'preset' && selectedPreset ? selectedPreset.id : null,
    })
  }

  return (
    <div className="max-w-2xl mx-auto space-y-8">
      <h1 className="text-3xl font-bold tracking-tight">Exam Simulation</h1>

      {/* Mode toggle */}
      <div className="flex gap-1 p-1 bg-slate-100 dark:bg-slate-800 rounded-xl w-fit">
        {['preset', 'custom'].map(m => (
          <button
            key={m}
            onClick={() => setMode(m)}
            className={`px-5 py-1.5 rounded-lg text-sm font-semibold capitalize transition-all
              ${mode === m
                ? 'bg-white dark:bg-slate-900 shadow text-slate-900 dark:text-slate-100'
                : 'text-slate-500 dark:text-slate-400 hover:text-slate-700 dark:hover:text-slate-300'
              }`}
          >
            {m === 'preset' ? 'Exam Presets' : 'Custom'}
          </button>
        ))}
      </div>

      {/* ── Preset mode ── */}
      {mode === 'preset' && (
        <div className="space-y-4">
          <p className="text-sm text-slate-500 dark:text-slate-400">
            Select an exam to match your course schedule. Questions are randomly drawn from
            the full chapter pool — you'll get a different set each attempt.
          </p>
          <div className="grid grid-cols-2 gap-3">
            {EXAM_PRESETS.map(preset => {
              const available = getQuestionsForChapters(preset.chapterIds).length
              const isSelected = selectedPreset?.id === preset.id
              const hasContent = available > 0
              return (
                <button
                  key={preset.id}
                  onClick={() => hasContent && handlePresetClick(preset)}
                  disabled={!hasContent}
                  className={`relative rounded-2xl p-4 text-left border-2 transition-all
                    ${!hasContent
                      ? 'border-slate-100 dark:border-slate-800 opacity-40 cursor-not-allowed'
                      : isSelected
                        ? 'border-accent-500 bg-accent-50 dark:bg-accent-900/30'
                        : 'border-slate-200 dark:border-slate-700 hover:border-accent-300 dark:hover:border-accent-700 hover:bg-slate-50 dark:hover:bg-slate-800/60'
                    }`}
                >
                  <div className="flex items-start justify-between gap-2 mb-2">
                    <span className={`text-lg font-bold ${isSelected ? 'text-accent-600 dark:text-accent-400' : 'text-slate-900 dark:text-slate-100'}`}>
                      {preset.label}
                    </span>
                    <span className="text-xs text-slate-400 dark:text-slate-500 shrink-0 pt-0.5">{preset.date}</span>
                  </div>
                  <p className="text-xs text-slate-500 dark:text-slate-400 leading-relaxed mb-3">
                    {preset.description}
                  </p>
                  <div className="flex items-center gap-2">
                    <span className={`text-xs font-semibold px-2 py-0.5 rounded-full
                      ${hasContent
                        ? 'bg-accent-100 text-accent-700 dark:bg-accent-900/40 dark:text-accent-400'
                        : 'bg-slate-100 text-slate-400'
                      }`}>
                      {available} questions
                    </span>
                    {!hasContent && (
                      <span className="text-xs text-slate-400 italic">Coming soon</span>
                    )}
                    {isSelected && (
                      <span className="text-xs font-medium text-accent-600 dark:text-accent-400 ml-auto">Selected</span>
                    )}
                  </div>
                </button>
              )
            })}
          </div>
        </div>
      )}

      {/* ── Custom mode ── */}
      {mode === 'custom' && (
        <div className="card p-5 space-y-4">
          <div>
            <label className="block text-sm font-medium mb-2">Chapter</label>
            <select
              value={chapterId}
              onChange={e => setChapterId(e.target.value)}
              className="w-full rounded-xl border border-slate-200 dark:border-slate-700
                         bg-white dark:bg-slate-900 px-3 py-2 text-sm focus:outline-none
                         focus:ring-2 focus:ring-accent-500"
            >
              <option value="all">Whole course</option>
              {content.chapters.map(c => (
                <option key={c.id} value={c.id}>{c.id.toUpperCase()} — {c.title}</option>
              ))}
            </select>
          </div>
        </div>
      )}

      {/* ── Config (shared) ── */}
      {(mode === 'custom' || selectedPreset) && (
        <div className="card p-5 space-y-4">
          <div className="flex gap-4">
            <div className="flex-1">
              <label className="block text-sm font-medium mb-2">
                Questions <span className="text-slate-400 font-normal">(pool: {maxQuestions})</span>
              </label>
              <input
                type="number"
                min={1}
                max={maxQuestions}
                value={count}
                onChange={e => setCount(Math.max(1, Math.min(maxQuestions, parseInt(e.target.value) || 1)))}
                className="w-full rounded-xl border border-slate-200 dark:border-slate-700
                           bg-white dark:bg-slate-900 px-3 py-2 text-sm focus:outline-none
                           focus:ring-2 focus:ring-accent-500"
              />
            </div>
            <div className="flex-1">
              <label className="block text-sm font-medium mb-2">Duration (minutes)</label>
              <input
                type="number"
                min={5}
                max={240}
                value={durationMins}
                onChange={e => setDurationMins(Math.max(5, parseInt(e.target.value) || 60))}
                className="w-full rounded-xl border border-slate-200 dark:border-slate-700
                           bg-white dark:bg-slate-900 px-3 py-2 text-sm focus:outline-none
                           focus:ring-2 focus:ring-accent-500"
              />
            </div>
          </div>
          <p className="text-xs text-slate-400 dark:text-slate-500">
            {durationMins} min total · {actualCount} questions · ~{Math.round((durationMins * 60) / actualCount)}s per question
            {' · '}Drawing from a pool of {maxQuestions}
          </p>
          <button
            onClick={handleStart}
            disabled={actualCount === 0}
            className="btn-primary w-full disabled:opacity-40"
          >
            {mode === 'preset' && selectedPreset
              ? `Start ${selectedPreset.label} — ${actualCount} questions`
              : `Start Exam — ${actualCount} questions`}
          </button>
        </div>
      )}

      {mode === 'preset' && !selectedPreset && (
        <p className="text-sm text-slate-400 dark:text-slate-500 text-center">
          Select an exam above to configure and start.
        </p>
      )}

      {/* History */}
      {examHistory.length > 0 && (
        <div>
          <h2 className="text-base font-semibold mb-3">Recent Attempts</h2>
          <div className="card divide-y divide-slate-100 dark:divide-slate-800">
            {examHistory.slice(0, 8).map((h, i) => {
              const preset = EXAM_PRESETS.find(p => p.id === h.presetId || p.id === h.chapterId)
              const ch = content.chapters.find(c => c.id === h.chapterId)
              const label = preset?.label ?? ch?.title ?? (h.chapterId === 'all' ? 'Whole course' : h.chapterId)
              const pct = h.total > 0 ? Math.round((h.score / h.total) * 100) : 0
              const mins = Math.floor((h.timeSec ?? 0) / 60)
              const secs = (h.timeSec ?? 0) % 60
              return (
                <div key={i} className="flex items-center gap-4 px-5 py-3">
                  <div className="flex-1 min-w-0">
                    <p className="text-sm font-medium truncate">{label}</p>
                    <p className="text-xs text-slate-400 dark:text-slate-500">
                      {new Date(h.date).toLocaleDateString()} · {mins}m {secs}s
                    </p>
                  </div>
                  <span className={`text-sm font-bold shrink-0
                    ${pct >= 80 ? 'text-green-600 dark:text-green-400'
                    : pct >= 60 ? 'text-amber-600 dark:text-amber-400'
                    : 'text-red-600 dark:text-red-400'}`}>
                    {h.score}/{h.total} · {pct}%
                  </span>
                </div>
              )
            })}
          </div>
        </div>
      )}
    </div>
  )
}

// ─── Active exam session ───────────────────────────────────────────────────────

function ExamSession({ questions, durationMins, chapterIds, presetId, onExit }) {
  const { saveAttempt } = useExamHistory()

  const totalSecs = (durationMins ?? 60) * 60
  const [timeLeft, setTimeLeft] = useState(totalSecs)
  const [index, setIndex] = useState(0)
  const [selections, setSelections] = useState({})
  const [submitted, setSubmitted] = useState(false)
  const [reviewIndex, setReviewIndex] = useState(0)
  const timeSaved = useRef(0)
  const submitCalled = useRef(false)

  useEffect(() => {
    if (submitted) return
    const id = setInterval(() => {
      setTimeLeft(t => {
        if (t <= 1) { clearInterval(id); doSubmit(true); return 0 }
        return t - 1
      })
    }, 1000)
    return () => clearInterval(id)
  }, [submitted])

  const doSubmit = useCallback((fromTimer = false) => {
    if (submitCalled.current) return
    submitCalled.current = true
    timeSaved.current = totalSecs - timeLeft
    const score = questions.filter((q, i) => selections[i] === q.answerIndex).length
    saveAttempt({
      chapterId: presetId ?? (Array.isArray(chapterIds) ? chapterIds.join(',') : chapterIds),
      presetId: presetId ?? null,
      score,
      total: questions.length,
      timeSec: timeSaved.current,
    })
    setSubmitted(true)
  }, [selections, timeLeft, submitted])

  const mins = Math.floor(timeLeft / 60)
  const secs = timeLeft % 60
  const timerPct = (timeLeft / totalSecs) * 100
  const timerColor = timerPct > 33 ? 'bg-accent-500' : timerPct > 15 ? 'bg-amber-500' : 'bg-red-500'

  // ── Results ──────────────────────────────────────────────────────────────────
  if (submitted) {
    const score = questions.filter((q, i) => selections[i] === q.answerIndex).length
    const pct = Math.round((score / questions.length) * 100)
    const usedMin = Math.floor(timeSaved.current / 60)
    const usedS   = timeSaved.current % 60

    const sections = {}
    questions.forEach((q, i) => {
      if (!sections[q.section]) sections[q.section] = { correct: 0, total: 0 }
      sections[q.section].total++
      if (selections[i] === q.answerIndex) sections[q.section].correct++
    })
    const secBreakdown = Object.entries(sections)
      .map(([k, v]) => ({ label: k, ...v, pct: Math.round((v.correct / v.total) * 100) }))
      .sort((a, b) => a.pct - b.pct)

    const rq = questions[reviewIndex]
    const sel = selections[reviewIndex]

    return (
      <div className="max-w-2xl mx-auto space-y-8">
        {/* Score */}
        <div className="card p-8 text-center space-y-4">
          <p className={`text-6xl font-bold ${pct >= 80 ? 'text-green-500' : pct >= 60 ? 'text-amber-500' : 'text-red-500'}`}>
            {pct}%
          </p>
          <p className="text-lg font-semibold">{score} / {questions.length} correct</p>
          <p className="text-sm text-slate-400">Time used: {usedMin}m {usedS}s</p>
          <ProgressBar
            value={score} max={questions.length}
            colorClass={pct >= 80 ? 'bg-green-500' : pct >= 60 ? 'bg-amber-500' : 'bg-red-500'}
            className="h-3"
          />
        </div>

        {/* Section breakdown */}
        <div>
          <h2 className="text-base font-semibold mb-3">Section breakdown</h2>
          <div className="card divide-y divide-slate-100 dark:divide-slate-800">
            {secBreakdown.map(s => (
              <div key={s.label} className="flex items-center gap-4 px-5 py-3">
                <span className="text-sm font-medium flex-1">{s.label}</span>
                <span className="text-xs text-slate-400">{s.correct}/{s.total}</span>
                <span className={`text-sm font-bold w-12 text-right
                  ${s.pct >= 80 ? 'text-green-600 dark:text-green-400'
                  : s.pct >= 60 ? 'text-amber-600 dark:text-amber-400'
                  : 'text-red-600 dark:text-red-400'}`}>
                  {s.pct}%
                </span>
              </div>
            ))}
          </div>
        </div>

        {/* Review */}
        <div>
          <h2 className="text-base font-semibold mb-3">Question review ({reviewIndex + 1}/{questions.length})</h2>
          <div className="card p-6 space-y-4">
            <div className="flex items-center justify-between">
              <DifficultyBadge difficulty={rq.difficulty} />
              <span className={`text-sm font-semibold ${sel === rq.answerIndex ? 'text-green-600 dark:text-green-400' : 'text-red-500'}`}>
                {sel === rq.answerIndex ? '✓ Correct' : sel === undefined ? '— Skipped' : '✗ Incorrect'}
              </span>
            </div>
            {rq.image && <img src={rq.image} alt="" className="max-w-full max-h-40 object-contain rounded-xl" />}
            <p className="font-semibold leading-snug">{rq.question}</p>
            <div className="space-y-2">
              {rq.choices.map((choice, i) => (
                <div key={i} className={`rounded-xl px-4 py-3 text-sm border-2
                  ${i === rq.answerIndex
                    ? 'border-green-400 bg-green-50 text-green-800 dark:bg-green-900/30 dark:text-green-300 dark:border-green-700'
                    : i === sel
                      ? 'border-red-300 bg-red-50 text-red-800 dark:bg-red-900/30 dark:text-red-300 dark:border-red-700'
                      : 'border-slate-100 dark:border-slate-800 text-slate-500 dark:text-slate-500'
                  }`}>
                  {choice}
                </div>
              ))}
            </div>
            <div className="bg-slate-50 dark:bg-slate-800/50 rounded-xl p-4 text-sm text-slate-600 dark:text-slate-300">
              <span className="font-semibold">Explanation: </span>{rq.explanation}
            </div>
          </div>
          <div className="flex gap-3 mt-4">
            <button disabled={reviewIndex === 0} onClick={() => setReviewIndex(i => i - 1)} className="btn-outline disabled:opacity-40">Previous</button>
            <button disabled={reviewIndex >= questions.length - 1} onClick={() => setReviewIndex(i => i + 1)} className="btn-primary disabled:opacity-40">Next</button>
            <button onClick={onExit} className="btn-ghost ml-auto">Exit</button>
          </div>
        </div>
      </div>
    )
  }

  // ── Active question ───────────────────────────────────────────────────────────
  const q = questions[index]

  return (
    <div className="max-w-2xl mx-auto space-y-6">
      <div className="flex items-center gap-4">
        <span className={`font-mono text-sm font-bold tabular-nums shrink-0 ${timeLeft <= 30 ? 'text-red-500 animate-pulse' : 'text-slate-600 dark:text-slate-400'}`}>
          {String(mins).padStart(2, '0')}:{String(secs).padStart(2, '0')}
        </span>
        <ProgressBar value={timeLeft} max={totalSecs} colorClass={timerColor} className="flex-1" />
        <span className="text-sm text-slate-500 dark:text-slate-400 font-medium shrink-0">
          {index + 1}/{questions.length}
        </span>
      </div>

      <ProgressBar value={index} max={questions.length} />

      <div className="card p-6 space-y-5">
        <div className="flex items-center justify-between">
          <DifficultyBadge difficulty={q.difficulty} />
          <span className="text-xs text-slate-400">{q.section}</span>
        </div>
        {q.image && <img src={q.image} alt="" className="max-w-full max-h-40 object-contain rounded-xl" />}
        <p className="text-lg font-semibold leading-snug">{q.question}</p>

        <div className="space-y-2.5">
          {q.choices.map((choice, i) => (
            <button
              key={i}
              onClick={() => setSelections(s => ({ ...s, [index]: i }))}
              className={`w-full rounded-xl px-4 py-3.5 text-sm font-medium text-left border-2 transition-all
                ${selections[index] === i
                  ? 'border-accent-500 bg-accent-50 text-accent-800 dark:bg-accent-900/30 dark:text-accent-300 dark:border-accent-600'
                  : 'border-slate-200 dark:border-slate-700 text-slate-700 dark:text-slate-300 hover:border-accent-300 hover:bg-accent-50/50 dark:hover:bg-accent-900/10'
                }`}
            >
              <span className="text-xs font-bold opacity-40 mr-2">{i + 1}</span>
              {choice}
            </button>
          ))}
        </div>
      </div>

      <div className="flex justify-between gap-3">
        <button onClick={onExit} className="btn-ghost text-sm">Quit</button>
        <div className="flex gap-3">
          {index > 0 && (
            <button onClick={() => setIndex(i => i - 1)} className="btn-outline">← Prev</button>
          )}
          {index < questions.length - 1 ? (
            <button onClick={() => setIndex(i => i + 1)} className="btn-primary">Next →</button>
          ) : (
            <button onClick={() => doSubmit()} className="btn-primary bg-green-600 hover:bg-green-700 dark:bg-green-600">
              Submit Exam
            </button>
          )}
        </div>
      </div>
    </div>
  )
}

// ─── Page root ─────────────────────────────────────────────────────────────────

export default function Exam() {
  const [searchParams] = useSearchParams()
  const { history } = useExamHistory()
  const { settings } = useSettings()
  const [session, setSession] = useState(null)

  const initialPresetId = searchParams.get('preset') ?? null

  useEffect(() => {
    const chapter = searchParams.get('chapter')
    if (chapter) {
      setSession({ chapterIds: chapter, count: 20, durationMins: settings.examDurationMins ?? 60, presetId: null })
    }
  }, [])

  const questions = useMemo(() => {
    if (!session) return []
    const pool = getQuestionsForChapters(session.chapterIds)
    return shuffle(pool).slice(0, session.count).map(shuffleQuestion)
  }, [session])

  if (session && questions.length > 0) {
    return (
      <ExamSession
        questions={questions}
        durationMins={session.durationMins}
        chapterIds={session.chapterIds}
        presetId={session.presetId}
        onExit={() => setSession(null)}
      />
    )
  }

  return <Selector onStart={setSession} examHistory={history} initialPresetId={initialPresetId} />
}
