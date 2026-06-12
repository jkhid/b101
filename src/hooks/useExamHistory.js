import { useState, useCallback } from 'react'
import { storageGet, storageSet, KEYS } from '../lib/storage'

export function useExamHistory() {
  const [history, setHistory] = useState(() =>
    storageGet(KEYS.EXAM_HISTORY, [])
  )

  const saveAttempt = useCallback((attempt) => {
    setHistory(prev => {
      const updated = [{ ...attempt, date: new Date().toISOString() }, ...prev]
      storageSet(KEYS.EXAM_HISTORY, updated)
      return updated
    })
  }, [])

  return { history, saveAttempt }
}
