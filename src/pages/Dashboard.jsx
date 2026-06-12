import { useMemo, useState } from 'react'
import { Link } from 'react-router-dom'
import content from '../data/content.json'
import ProgressBar from '../components/ProgressBar'
import { useFlashcards } from '../hooks/useFlashcards'
import { useQuizStats } from '../hooks/useQuizStats'
import { useExamHistory } from '../hooks/useExamHistory'
import { isDueToday } from '../lib/sm2'

const EXAMS = [
  { id: 'exam1', label: 'Exam I',   date: 'June 26', chapterIds: ['ch1','ch2','ch3'] },
  { id: 'exam2', label: 'Exam II',  date: 'July 10',  chapterIds: ['ch4','ch5','ch6'] },
  { id: 'exam3', label: 'Exam III', date: 'July 31',  chapterIds: ['ch7','ch8','ch9','ch10','ch11'] },
  { id: 'exam4', label: 'Exam IV',  date: 'Aug 7',    chapterIds: ['ch12','ch13','ch14','ch15'] },
]

const EXAM_PRESET_LABELS = {
  exam1: 'Exam I (Ch 1–3)',
  exam2: 'Exam II (Ch 4–6)',
  exam3: 'Exam III (Ch 7–10)',
  exam4: 'Exam IV (Ch 12–15)',
}

function getQuestionCount(chapterIds) {
  return content.chapters
    .filter(c => chapterIds.includes(c.id))
    .reduce((sum, c) => sum + c.quiz.length, 0)
}

export default function Dashboard() {
  const { schedules, isKnown } = useFlashcards()
  const { stats } = useQuizStats()
  const { history } = useExamHistory()
  const [chaptersOpen, setChaptersOpen] = useState(true)

  const chapterStats = useMemo(() => {
    return content.chapters.map(ch => {
      const totalCards = ch.flashcards.length
      const knownCards = ch.flashcards.filter(c => isKnown(c.id)).length
      const knownPct   = totalCards > 0 ? Math.round((knownCards / totalCards) * 100) : 0
      const dueCards   = ch.flashcards.filter(c => isDueToday(schedules[c.id])).length
      return { ch, totalCards, knownCards, knownPct, dueCards }
    })
  }, [schedules, isKnown])

  const weakTopics = useMemo(() => {
    const sectionMap = {}
    content.chapters.forEach(ch => {
      ch.sections.forEach(sec => {
        sectionMap[sec.id] = { chapterTitle: ch.title, sectionTitle: sec.title, attempts: 0, correct: 0 }
      })
      ch.quiz.forEach(q => {
        const s = stats[q.id]
        if (s && sectionMap[q.section]) {
          sectionMap[q.section].attempts += s.attempts
          sectionMap[q.section].correct  += s.correct
        }
      })
    })
    return Object.entries(sectionMap)
      .filter(([, v]) => v.attempts > 0)
      .map(([id, v]) => ({
        id,
        chapterTitle: v.chapterTitle,
        sectionTitle: v.sectionTitle,
        attempts: v.attempts,
        correct: v.correct,
        accuracy: v.attempts > 0 ? Math.round((v.correct / v.attempts) * 100) : 100,
      }))
      .sort((a, b) => a.accuracy - b.accuracy)
      .slice(0, 6)
  }, [stats])

  return (
    <div className="space-y-10">
      {/* Hero */}
      <div>
        <h1 className="text-3xl font-bold tracking-tight">Study Dashboard</h1>
        <p className="text-slate-500 dark:text-slate-400 mt-1 text-sm">
          {content.meta.course}
        </p>
      </div>

      {/* ── Exam Presets ── */}
      <section>
        <h2 className="text-lg font-semibold mb-4">Your Exams</h2>
        <div className="grid grid-cols-2 sm:grid-cols-4 gap-3">
          {EXAMS.map(exam => {
            const qCount = getQuestionCount(exam.chapterIds)
            const hasContent = qCount > 0
            const attempts = history.filter(h => h.presetId === exam.id)
            const bestPct = attempts.length > 0
              ? Math.max(...attempts.map(a => a.total > 0 ? Math.round((a.score / a.total) * 100) : 0))
              : null

            return (
              <div
                key={exam.id}
                className={`card p-4 flex flex-col gap-3 transition-opacity ${!hasContent ? 'opacity-40' : ''}`}
              >
                <div className="flex-1">
                  <p className="text-xs font-semibold text-accent-600 dark:text-accent-400 uppercase tracking-wider mb-1">
                    {exam.date}
                  </p>
                  <p className="text-2xl font-bold text-slate-900 dark:text-slate-100 leading-none">
                    {exam.label}
                  </p>
                  <p className="text-xs text-slate-400 dark:text-slate-500 mt-2">
                    {hasContent ? `${qCount} questions` : 'Coming soon'}
                  </p>
                  {bestPct !== null && (
                    <p className={`text-sm font-semibold mt-1
                      ${bestPct >= 80 ? 'text-green-500 dark:text-green-400'
                      : bestPct >= 60 ? 'text-amber-500 dark:text-amber-400'
                      : 'text-red-500 dark:text-red-400'}`}>
                      Best {bestPct}%
                    </p>
                  )}
                </div>
                {hasContent ? (
                  <Link
                    to={`/exam?preset=${exam.id}`}
                    className="btn-primary text-sm py-2 text-center w-full block"
                  >
                    Start Exam
                  </Link>
                ) : (
                  <div className="text-xs text-center text-slate-300 dark:text-slate-600 py-2 rounded-xl border border-slate-100 dark:border-slate-800">
                    Locked
                  </div>
                )}
              </div>
            )
          })}
        </div>
      </section>

      {/* ── Chapters (collapsible) ── */}
      <section>
        <button
          onClick={() => setChaptersOpen(o => !o)}
          className="flex items-center gap-2 text-lg font-semibold mb-4 w-full text-left
                     hover:text-accent-600 dark:hover:text-accent-400 transition-colors"
        >
          Chapters
          <span className={`text-slate-400 text-base transition-transform duration-200 ${chaptersOpen ? 'rotate-180' : ''}`}>
            ▾
          </span>
        </button>

        {chaptersOpen && (
          <div className="card divide-y divide-slate-100 dark:divide-slate-800">
            {chapterStats.map(({ ch, totalCards, knownCards, knownPct, dueCards }) => (
              <div key={ch.id} className="flex items-center gap-4 px-5 py-4">
                <div className="flex-1 min-w-0 space-y-1.5">
                  <div className="flex items-center gap-2.5 flex-wrap">
                    <span className="text-xs font-bold px-2 py-0.5 rounded-md
                                     bg-accent-100 dark:bg-accent-900/30
                                     text-accent-700 dark:text-accent-400 shrink-0">
                      {ch.id.toUpperCase()}
                    </span>
                    <span className="text-sm font-medium text-slate-900 dark:text-slate-100 truncate">
                      {ch.title}
                    </span>
                    {dueCards > 0 && (
                      <span className="text-xs font-semibold text-accent-600 dark:text-accent-400 shrink-0">
                        {dueCards} due
                      </span>
                    )}
                  </div>
                  <div className="flex items-center gap-2">
                    <ProgressBar value={knownCards} max={totalCards} className="flex-1 h-1.5" />
                    <span className="text-xs text-slate-400 dark:text-slate-500 shrink-0 tabular-nums w-8 text-right">
                      {knownPct}%
                    </span>
                  </div>
                  <p className="text-xs text-slate-400 dark:text-slate-500">
                    {knownCards}/{totalCards} flashcards · {ch.quiz.length} questions
                  </p>
                </div>
                <div className="flex gap-2 shrink-0">
                  <Link
                    to={`/flashcards?chapter=${ch.id}`}
                    className="btn-outline text-xs px-3 py-1.5"
                  >
                    Cards
                  </Link>
                  <Link
                    to={`/quiz?chapter=${ch.id}`}
                    className="btn-outline text-xs px-3 py-1.5"
                  >
                    Quiz
                  </Link>
                </div>
              </div>
            ))}
          </div>
        )}
      </section>

      {/* ── Weak Topics ── */}
      {weakTopics.length > 0 && (
        <section>
          <div className="flex items-center gap-3 mb-4">
            <h2 className="text-lg font-semibold">Weak Topics</h2>
            <span className="text-xs text-slate-400 dark:text-slate-500">needs most review</span>
          </div>
          <div className="card divide-y divide-slate-100 dark:divide-slate-800">
            {weakTopics.map((t, i) => (
              <div key={t.id} className="flex items-center gap-4 px-5 py-3.5">
                <span className={`text-lg font-bold w-6 text-center shrink-0
                  ${i === 0 ? 'text-red-500' : i === 1 ? 'text-amber-500' : 'text-slate-400'}`}>
                  {i + 1}
                </span>
                <div className="flex-1 min-w-0">
                  <p className="text-sm font-medium truncate">{t.sectionTitle}</p>
                  <p className="text-xs text-slate-400 dark:text-slate-500 truncate">{t.chapterTitle}</p>
                </div>
                <div className="shrink-0 text-right">
                  <span className={`text-sm font-bold
                    ${t.accuracy < 50 ? 'text-red-500' : t.accuracy < 70 ? 'text-amber-500' : 'text-slate-600 dark:text-slate-400'}`}>
                    {t.accuracy}%
                  </span>
                  <p className="text-xs text-slate-400 dark:text-slate-500">{t.correct}/{t.attempts}</p>
                </div>
              </div>
            ))}
          </div>
        </section>
      )}

      {/* ── Recent Exams ── */}
      {history.length > 0 && (
        <section>
          <h2 className="text-lg font-semibold mb-4">Recent Exams</h2>
          <div className="card divide-y divide-slate-100 dark:divide-slate-800">
            {history.slice(0, 5).map((h, i) => {
              const ch = content.chapters.find(c => c.id === h.chapterId)
              const presetLabel = h.presetId ? EXAM_PRESET_LABELS[h.presetId] : null
              const pct  = h.total > 0 ? Math.round((h.score / h.total) * 100) : 0
              const mins = Math.floor((h.timeSec ?? 0) / 60)
              const secs = (h.timeSec ?? 0) % 60
              return (
                <div key={i} className="flex items-center gap-4 px-5 py-3.5">
                  <div className="flex-1 min-w-0">
                    <p className="text-sm font-medium truncate">
                      {presetLabel ?? ch?.title ?? h.chapterId}
                    </p>
                    <p className="text-xs text-slate-400 dark:text-slate-500">
                      {new Date(h.date).toLocaleDateString()} · {mins}m {secs}s
                    </p>
                  </div>
                  <span className={`text-sm font-bold shrink-0
                    ${pct >= 80 ? 'text-green-600 dark:text-green-400'
                    : pct >= 60 ? 'text-amber-600 dark:text-amber-400'
                    : 'text-red-600 dark:text-red-400'}`}>
                    {h.score}/{h.total}
                  </span>
                </div>
              )
            })}
          </div>
        </section>
      )}
    </div>
  )
}
