import { useState, useMemo, useEffect } from 'react'
import { useSearchParams } from 'react-router-dom'
import content from '../data/content.json'
import ProgressBar from '../components/ProgressBar'
import DifficultyBadge from '../components/DifficultyBadge'
import { useQuizStats } from '../hooks/useQuizStats'

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

function Selector({ onStart }) {
  const [chapterId, setChapterId] = useState('all')
  const [sectionId, setSectionId] = useState('')

  const chapter = content.chapters.find(c => c.id === chapterId)
  const sections = chapter?.sections ?? []

  return (
    <div className="max-w-md mx-auto space-y-6">
      <h1 className="text-3xl font-bold tracking-tight">Quiz</h1>
      <div className="card p-6 space-y-5">
        <div>
          <label className="block text-sm font-medium mb-2">Chapter</label>
          <select
            value={chapterId}
            onChange={e => { setChapterId(e.target.value); setSectionId('') }}
            className="w-full rounded-xl border border-slate-200 dark:border-slate-700
                       bg-white dark:bg-slate-900 px-3 py-2 text-sm focus:outline-none
                       focus:ring-2 focus:ring-accent-500"
          >
            <option value="all">All chapters</option>
            {content.chapters.map(c => (
              <option key={c.id} value={c.id}>{c.id.toUpperCase()} — {c.title}</option>
            ))}
          </select>
        </div>

        {chapterId !== 'all' && sections.length > 0 && (
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

        <button onClick={() => onStart({ chapterId, sectionId })} className="btn-primary w-full">
          Start Quiz
        </button>
      </div>
    </div>
  )
}

// ─── Session ─────────────────────────────────────────────────────────────────

function QuizSession({ questions: rawQuestions, onExit }) {
  const { recordAnswer } = useQuizStats()

  const questions = useMemo(() => shuffle(rawQuestions).map(shuffleQuestion), [])
  const [index, setIndex] = useState(0)
  const [selected, setSelected] = useState(null)
  const [answers, setAnswers] = useState([]) // { questionIndex, selectedIndex, correct }
  const [done, setDone] = useState(false)
  const [reviewMode, setReviewMode] = useState(false)
  const [reviewIndex, setReviewIndex] = useState(0)

  const q = questions[index]
  const answered = selected !== null

  function choose(i) {
    if (answered) return
    const correct = i === q.answerIndex
    setSelected(i)
    recordAnswer(q.id, correct)
    setAnswers(prev => [...prev, { questionIndex: index, selectedIndex: i, correct }])
  }

  function next() {
    if (index < questions.length - 1) {
      setIndex(i => i + 1)
      setSelected(null)
    } else {
      setDone(true)
    }
  }

  // Keyboard shortcuts
  useEffect(() => {
    function handler(e) {
      if (e.target.tagName !== 'BODY' && e.target.tagName !== 'MAIN') return
      if (done || reviewMode) return
      const num = parseInt(e.key)
      if (num >= 1 && num <= q.choices.length && !answered) choose(num - 1)
      if ((e.key === 'Enter' || e.key === 'ArrowRight') && answered) next()
    }
    window.addEventListener('keydown', handler)
    return () => window.removeEventListener('keydown', handler)
  }, [answered, index, done, reviewMode])

  // ── Results screen ──
  if (done && !reviewMode) {
    const score = answers.filter(a => a.correct).length
    const pct = Math.round((score / questions.length) * 100)
    const missed = answers.filter(a => !a.correct)

    return (
      <div className="max-w-lg mx-auto space-y-8">
        <div className="card p-8 text-center space-y-4">
          <p className={`text-6xl font-bold ${pct >= 80 ? 'text-green-500' : pct >= 60 ? 'text-amber-500' : 'text-red-500'}`}>
            {pct}%
          </p>
          <p className="text-lg font-semibold">{score} / {questions.length} correct</p>
          <ProgressBar
            value={score}
            max={questions.length}
            colorClass={pct >= 80 ? 'bg-green-500' : pct >= 60 ? 'bg-amber-500' : 'bg-red-500'}
            className="h-3"
          />
        </div>

        <div className="flex gap-3 flex-wrap">
          <button onClick={onExit} className="btn-outline">Exit</button>
          {missed.length > 0 && (
            <button onClick={() => { setReviewMode(true); setReviewIndex(0) }} className="btn-primary">
              Review {missed.length} missed
            </button>
          )}
        </div>
      </div>
    )
  }

  // ── Review missed ──
  if (reviewMode) {
    const missed = answers.filter(a => !a.correct)
    const entry = missed[reviewIndex]
    const rq = questions[entry.questionIndex]
    return (
      <div className="max-w-2xl mx-auto space-y-6">
        <div className="flex items-center justify-between">
          <button onClick={() => setReviewMode(false)} className="btn-ghost text-sm">← Results</button>
          <span className="text-sm text-slate-500">{reviewIndex + 1} / {missed.length}</span>
        </div>

        <div className="card p-6 space-y-5">
          {rq.image && <img src={rq.image} alt="" className="max-w-full max-h-40 object-contain rounded-xl" />}
          <p className="text-lg font-semibold leading-snug">{rq.question}</p>
          <div className="space-y-2">
            {rq.choices.map((choice, i) => (
              <div key={i} className={`rounded-xl px-4 py-3 text-sm font-medium border-2
                ${i === rq.answerIndex
                  ? 'border-green-400 bg-green-50 text-green-800 dark:bg-green-900/30 dark:text-green-300 dark:border-green-700'
                  : i === entry.selectedIndex
                    ? 'border-red-300 bg-red-50 text-red-800 dark:bg-red-900/30 dark:text-red-300 dark:border-red-700'
                    : 'border-slate-100 dark:border-slate-800 text-slate-500 dark:text-slate-500'
                }`}>
                {choice}
                {i === rq.answerIndex && ' ✓'}
                {i === entry.selectedIndex && i !== rq.answerIndex && ' ✗'}
              </div>
            ))}
          </div>
          <div className="bg-slate-50 dark:bg-slate-800/50 rounded-xl p-4 text-sm text-slate-600 dark:text-slate-300">
            <span className="font-semibold">Explanation: </span>{rq.explanation}
          </div>
        </div>

        <div className="flex gap-3">
          <button disabled={reviewIndex === 0} onClick={() => setReviewIndex(i => i - 1)} className="btn-outline disabled:opacity-40">
            Previous
          </button>
          <button disabled={reviewIndex >= missed.length - 1} onClick={() => setReviewIndex(i => i + 1)} className="btn-primary disabled:opacity-40">
            Next
          </button>
        </div>
      </div>
    )
  }

  // ── Active question ──
  return (
    <div className="max-w-2xl mx-auto space-y-6">
      <div className="flex items-center justify-between">
        <button onClick={onExit} className="btn-ghost text-sm">← Back</button>
        <div className="flex items-center gap-3">
          <DifficultyBadge difficulty={q.difficulty} />
          <span className="text-sm text-slate-500 dark:text-slate-400 font-medium">{index + 1}/{questions.length}</span>
        </div>
      </div>

      <ProgressBar value={index} max={questions.length} />

      <div className="card p-6 space-y-5">
        {q.image && <img src={q.image} alt="" className="max-w-full max-h-40 object-contain rounded-xl" />}
        <p className="text-lg font-semibold leading-snug">{q.question}</p>

        <div className="space-y-2.5">
          {q.choices.map((choice, i) => {
            let style = 'border-2 border-slate-200 dark:border-slate-700 text-slate-700 dark:text-slate-300 hover:border-accent-400 hover:bg-accent-50 dark:hover:bg-accent-900/20'
            if (answered) {
              if (i === q.answerIndex) {
                style = 'border-2 border-green-400 bg-green-50 text-green-800 dark:bg-green-900/30 dark:text-green-300 dark:border-green-700'
              } else if (i === selected) {
                style = 'border-2 border-red-400 bg-red-50 text-red-800 dark:bg-red-900/30 dark:text-red-300 dark:border-red-700'
              } else {
                style = 'border-2 border-slate-100 dark:border-slate-800 text-slate-400 dark:text-slate-600'
              }
            }
            return (
              <button
                key={i}
                onClick={() => choose(i)}
                disabled={answered}
                className={`w-full rounded-xl px-4 py-3.5 text-sm font-medium text-left transition-all ${style}
                            disabled:cursor-default`}
              >
                <span className="text-xs font-bold opacity-50 mr-2">{i + 1}</span>
                {choice}
              </button>
            )
          })}
        </div>

        {answered && (
          <div className="bg-slate-50 dark:bg-slate-800/50 rounded-xl p-4 text-sm text-slate-600 dark:text-slate-300">
            <span className="font-semibold">
              {selected === q.answerIndex ? '✓ Correct! ' : '✗ Incorrect. '}
            </span>
            {q.explanation}
          </div>
        )}
      </div>

      {answered && (
        <div className="flex justify-end">
          <button onClick={next} className="btn-primary">
            {index < questions.length - 1 ? 'Next →' : 'See Results →'}
          </button>
        </div>
      )}
    </div>
  )
}

// ─── Page root ────────────────────────────────────────────────────────────────

export default function Quiz() {
  const [searchParams] = useSearchParams()
  const [session, setSession] = useState(null)

  useEffect(() => {
    const chapter = searchParams.get('chapter')
    if (chapter) setSession({ chapterId: chapter, sectionId: '' })
  }, [])

  const questions = useMemo(() => {
    if (!session) return []
    const { chapterId, sectionId } = session
    let qs = chapterId === 'all'
      ? content.chapters.flatMap(c => c.quiz)
      : content.chapters.find(c => c.id === chapterId)?.quiz ?? []
    if (sectionId) qs = qs.filter(q => q.section === sectionId)
    return qs
  }, [session])

  if (session) return <QuizSession questions={questions} onExit={() => setSession(null)} />
  return <Selector onStart={setSession} />
}
