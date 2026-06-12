import { useState, useCallback } from 'react'
import { storageGet, storageSet, KEYS } from '../lib/storage'
import { defaultCardState, reviewCard } from '../lib/sm2'

export function useFlashcards() {
  const [schedules, setSchedules] = useState(() =>
    storageGet(KEYS.FLASHCARDS, {})
  )

  const getCardState = useCallback((cardId) => {
    return schedules[cardId] ?? defaultCardState()
  }, [schedules])

  const rate = useCallback((cardId, rating) => {
    setSchedules(prev => {
      const current = prev[cardId] ?? defaultCardState()
      const next = reviewCard(current, rating)
      const updated = { ...prev, [cardId]: next }
      storageSet(KEYS.FLASHCARDS, updated)
      return updated
    })
  }, [])

  const isKnown = useCallback((cardId) => {
    const s = schedules[cardId]
    if (!s) return false
    return s.intervalDays >= 1
  }, [schedules])

  return { schedules, getCardState, rate, isKnown }
}
