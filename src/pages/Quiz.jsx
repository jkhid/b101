import { useState, useMemo, useEffect } from 'react'
import { useSearchParams } from 'react-router-dom'
import content from '../data/content.json'
import ProgressBar from '../components/ProgressBar'
import DifficultyBadge from '../components/DifficultyBadge'
import { useQuizStats } from '../hooks/useQuizStats'

const EXAM_PRESETS = [
  { id: 'exam1', label: 'Exam I',   date: 'June 26', chapterIds: ['ch1','ch2','ch3'] },
  { id: 'exam2', label: 'Exam II',  date: 'July 10',  chapterIds: ['ch4','ch5','ch6'] },
  { id: 'exam3', label: 'Exam III', date: 'July 31',  chapterIds: ['ch7','ch8','ch9','ch10','ch11'] },
  { id: 'exam4', label: 'Exam IV',  date: 'Aug 7',    chapterIds: ['ch12','ch13','ch14','ch15'] },
]

function quizCount(chapterIds) {
  return content.chapters
    .filter(c => chapterIds.includes(c.id))
    .reduce((sum, c) => sum + c.quiz.length, 0)
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
  const isSA = q.type === 'selectAll'
  const indexed = q.choices.map((text, i) => ({
    text,
    isCorrect: isSA ? (q.answerIndices ?? []).includes(i) : i === q.answerIndex,
  }))
  const shuffled = shuffle(indexed)
  return {
    ...q,
    choices: shuffled.map(c => c.text),
    ...(isSA
      ? { answerIndices: shuffled.reduce((acc, c, i) => c.isCorrect ? [...acc, i] : acc, []) }
      : { answerIndex: shuffled.findIndex(c => c.isCorrect) }
    ),
  }
}

// ─── Selector ─────────────────────────────────────────────────────────────────

function Selector({ onStart }) {
  const [tab, setTab] = useState('chapter')   // 'chapter' | 'exam'
  const [chapterId, setChapterId] = useState('all')
  const [sectionId, setSectionId] = useState('')
  const [examId, setExamId] = useState(null)

  const chapter = content.chapters.find(c => c.id === chapterId)
  const sections = chapter?.sections ?? []
  const selectedExam = EXAM_PRESETS.find(e => e.id === examId)

  const canStart = tab === 'chapter' || (selectedExam && quizCount(selectedExam.chapterIds) > 0)

  function handleStart() {
    if (tab === 'exam') {
      onStart({ examChapterIds: selectedExam?.chapterIds ?? [], chapterId: null, sectionId: '' })
    } else {
      onStart({ chapterId, sectionId, examChapterIds: null })
    }
  }

  return (
    <div className="max-w-md mx-auto space-y-6">
      <h1 className="text-3xl font-bold tracking-tight">Quiz</h1>

      {/* Tab toggle */}
      <div className="flex gap-1 p-1 bg-slate-100 dark:bg-slate-800 rounded-xl w-fit">
        {[{ value: 'chapter', label: 'By Chapter' }, { value: 'exam', label: 'By Exam' }].map(t => (
          <button
            key={t.value}
            onClick={() => setTab(t.value)}
            className={`px-5 py-1.5 rounded-lg text-sm font-semibold transition-all
              ${tab === t.value
                ? 'bg-white dark:bg-slate-900 shadow text-slate-900 dark:text-slate-100'
                : 'text-slate-500 dark:text-slate-400 hover:text-slate-700 dark:hover:text-slate-300'
              }`}
          >
            {t.label}
          </button>
        ))}
      </div>

      <div className="card p-6 space-y-5">
        {/* Exam preset picker */}
        {tab === 'exam' && (
          <div>
            <label className="block text-sm font-medium mb-3">Select exam</label>
            <div className="grid grid-cols-2 gap-2">
              {EXAM_PRESETS.map(preset => {
                const count = quizCount(preset.chapterIds)
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
                      {hasContent ? `${count} questions` : 'Coming soon'}
                    </p>
                  </button>
                )
              })}
            </div>
          </div>
        )}

        {/* Chapter picker */}
        {tab === 'chapter' && (
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
        )}

        {/* Section picker */}
        {tab === 'chapter' && chapterId !== 'all' && sections.length > 0 && (
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
  const [selected, setSelected] = useState(null)            // mc: chosen index
  const [selectedSet, setSelectedSet] = useState(new Set()) // selectAll: chosen indices
  const [submitted, setSubmitted] = useState(false)         // selectAll: has user submitted
  const [answerCorrect, setAnswerCorrect] = useState(null)  // for explanation display
  const [answers, setAnswers] = useState([])
  const [done, setDone] = useState(false)
  const [reviewMode, setReviewMode] = useState(false)
  const [reviewIndex, setReviewIndex] = useState(0)

  const q = questions[index]
  const isSA = q.type === 'selectAll'
  const answered = isSA ? submitted : selected !== null

  function choose(i) {
    if (isSA) {
      if (submitted) return
      setSelectedSet(prev => {
        const next = new Set(prev)
        if (next.has(i)) next.delete(i); else next.add(i)
        return next
      })
    } else {
      if (answered) return
      const correct = i === q.answerIndex
      setSelected(i)
      setAnswerCorrect(correct)
      recordAnswer(q.id, correct)
      setAnswers(prev => [...prev, { questionIndex: index, selectedIndex: i, correct }])
    }
  }

  function submitSelectAll() {
    if (submitted || selectedSet.size === 0) return
    const correct =
      selectedSet.size === q.answerIndices.length &&
      q.answerIndices.every(i => selectedSet.has(i))
    setSubmitted(true)
    setAnswerCorrect(correct)
    recordAnswer(q.id, correct)
    setAnswers(prev => [...prev, {
      questionIndex: index,
      selectedIndices: [...selectedSet],
      correct,
    }])
  }

  function next() {
    if (index < questions.length - 1) {
      setIndex(i => i + 1)
      setSelected(null)
      setSelectedSet(new Set())
      setSubmitted(false)
      setAnswerCorrect(null)
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
      if (isSA) {
        if (num >= 1 && num <= q.choices.length && !submitted) choose(num - 1)
        if (e.key === 'Enter' && !submitted && selectedSet.size > 0) submitSelectAll()
        if ((e.key === 'Enter' || e.key === 'ArrowRight') && submitted) next()
      } else {
        if (num >= 1 && num <= q.choices.length && !answered) choose(num - 1)
        if ((e.key === 'Enter' || e.key === 'ArrowRight') && answered) next()
      }
    }
    window.addEventListener('keydown', handler)
    return () => window.removeEventListener('keydown', handler)
  }, [answered, index, done, reviewMode, isSA, submitted, selectedSet])

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
    const rqSA = rq.type === 'selectAll'

    return (
      <div className="max-w-2xl mx-auto space-y-6">
        <div className="flex items-center justify-between">
          <button onClick={() => setReviewMode(false)} className="btn-ghost text-sm">← Results</button>
          <span className="text-sm text-slate-500">{reviewIndex + 1} / {missed.length}</span>
        </div>

        <div className="card p-6 space-y-5">
          {rq.image && <img src={rq.image} alt="" className="max-w-full max-h-40 object-contain rounded-xl" />}
          {rqSA && (
            <p className="text-xs font-semibold uppercase tracking-wide text-accent-600 dark:text-accent-400">
              Select all that apply
            </p>
          )}
          <p className="text-lg font-semibold leading-snug">{rq.question}</p>
          <div className="space-y-2">
            {rq.choices.map((choice, i) => {
              const isCorrect = rqSA ? rq.answerIndices.includes(i) : i === rq.answerIndex
              const wasSelected = rqSA
                ? (entry.selectedIndices ?? []).includes(i)
                : i === entry.selectedIndex

              let cls, badge
              if (isCorrect && wasSelected) {
                cls = 'border-green-400 bg-green-50 text-green-800 dark:bg-green-900/30 dark:text-green-300 dark:border-green-700'
                badge = ' ✓'
              } else if (isCorrect && !wasSelected) {
                cls = 'border-amber-400 bg-amber-50 text-amber-800 dark:bg-amber-900/30 dark:text-amber-300 dark:border-amber-700'
                badge = ' ✓ missed'
              } else if (!isCorrect && wasSelected) {
                cls = 'border-red-300 bg-red-50 text-red-800 dark:bg-red-900/30 dark:text-red-300 dark:border-red-700'
                badge = ' ✗'
              } else {
                cls = 'border-slate-100 dark:border-slate-800 text-slate-500 dark:text-slate-500'
                badge = ''
              }
              return (
                <div key={i} className={`rounded-xl px-4 py-3 text-sm font-medium border-2 ${cls}`}>
                  {choice}{badge}
                </div>
              )
            })}
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

        {isSA && (
          <p className="text-xs font-semibold uppercase tracking-wide text-accent-600 dark:text-accent-400">
            Select all that apply
          </p>
        )}

        <p className="text-lg font-semibold leading-snug">{q.question}</p>

        <div className="space-y-2.5">
          {q.choices.map((choice, i) => {
            let style
            let badge = ''

            if (isSA) {
              const isSelected = selectedSet.has(i)
              if (!submitted) {
                style = isSelected
                  ? 'border-2 border-accent-400 bg-accent-50 dark:bg-accent-900/20 text-accent-800 dark:text-accent-200'
                  : 'border-2 border-slate-200 dark:border-slate-700 text-slate-700 dark:text-slate-300 hover:border-accent-400 hover:bg-accent-50 dark:hover:bg-accent-900/20'
              } else {
                const isCorrect = q.answerIndices.includes(i)
                if (isCorrect && isSelected) {
                  style = 'border-2 border-green-400 bg-green-50 text-green-800 dark:bg-green-900/30 dark:text-green-300 dark:border-green-700'
                  badge = ' ✓'
                } else if (isCorrect && !isSelected) {
                  style = 'border-2 border-amber-400 bg-amber-50 text-amber-800 dark:bg-amber-900/30 dark:text-amber-300 dark:border-amber-700'
                  badge = ' ✓ missed'
                } else if (!isCorrect && isSelected) {
                  style = 'border-2 border-red-400 bg-red-50 text-red-800 dark:bg-red-900/30 dark:text-red-300 dark:border-red-700'
                  badge = ' ✗'
                } else {
                  style = 'border-2 border-slate-100 dark:border-slate-800 text-slate-400 dark:text-slate-600'
                }
              }
            } else {
              style = 'border-2 border-slate-200 dark:border-slate-700 text-slate-700 dark:text-slate-300 hover:border-accent-400 hover:bg-accent-50 dark:hover:bg-accent-900/20'
              if (answered) {
                if (i === q.answerIndex) {
                  style = 'border-2 border-green-400 bg-green-50 text-green-800 dark:bg-green-900/30 dark:text-green-300 dark:border-green-700'
                  badge = ' ✓'
                } else if (i === selected) {
                  style = 'border-2 border-red-400 bg-red-50 text-red-800 dark:bg-red-900/30 dark:text-red-300 dark:border-red-700'
                  badge = ' ✗'
                } else {
                  style = 'border-2 border-slate-100 dark:border-slate-800 text-slate-400 dark:text-slate-600'
                }
              }
            }

            return (
              <button
                key={i}
                onClick={() => choose(i)}
                disabled={isSA ? submitted : answered}
                className={`w-full rounded-xl px-4 py-3.5 text-sm font-medium text-left transition-all ${style} disabled:cursor-default`}
              >
                {/* Checkbox indicator for selectAll (before submitting) */}
                {isSA && !submitted && (
                  <span className={`inline-block w-4 h-4 mr-2 border-2 rounded align-middle flex-shrink-0 transition-colors
                    ${selectedSet.has(i)
                      ? 'bg-accent-500 border-accent-500'
                      : 'border-slate-400 dark:border-slate-500'}`}
                  />
                )}
                <span className="text-xs font-bold opacity-50 mr-2">{i + 1}</span>
                {choice}{badge}
              </button>
            )
          })}
        </div>

        {/* Submit button — selectAll only, before submitting */}
        {isSA && !submitted && (
          <div className="flex justify-end">
            <button
              onClick={submitSelectAll}
              disabled={selectedSet.size === 0}
              className="btn-primary disabled:opacity-40"
            >
              Submit
            </button>
          </div>
        )}

        {answered && (
          <div className="bg-slate-50 dark:bg-slate-800/50 rounded-xl p-4 text-sm text-slate-600 dark:text-slate-300">
            <span className="font-semibold">
              {answerCorrect ? '✓ Correct! ' : '✗ Incorrect. '}
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
    const { chapterId, sectionId, examChapterIds } = session
    let qs
    if (examChapterIds) {
      qs = content.chapters.filter(c => examChapterIds.includes(c.id)).flatMap(c => c.quiz)
    } else {
      qs = chapterId === 'all'
        ? content.chapters.flatMap(c => c.quiz)
        : content.chapters.find(c => c.id === chapterId)?.quiz ?? []
      if (sectionId) qs = qs.filter(q => q.section === sectionId)
    }
    return qs
  }, [session])

  if (session) return <QuizSession questions={questions} onExit={() => setSession(null)} />
  return <Selector onStart={setSession} />
}
