import { useState, useCallback } from 'react'
import { storageGet, storageSet, KEYS } from '../lib/storage'

export function useQuizStats() {
  const [stats, setStats] = useState(() =>
    storageGet(KEYS.QUIZ_STATS, {})
  )

  const recordAnswer = useCallback((questionId, correct) => {
    setStats(prev => {
      const entry = prev[questionId] ?? { attempts: 0, correct: 0, lastResult: null }
      const next = {
        attempts: entry.attempts + 1,
        correct: entry.correct + (correct ? 1 : 0),
        lastResult: correct ? 'correct' : 'incorrect',
      }
      const updated = { ...prev, [questionId]: next }
      storageSet(KEYS.QUIZ_STATS, updated)
      return updated
    })
  }, [])

  return { stats, recordAnswer }
}
