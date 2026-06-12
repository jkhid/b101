const PREFIX = 'biostudy:'

export const KEYS = {
  FLASHCARDS:   PREFIX + 'flashcards',
  QUIZ_STATS:   PREFIX + 'quizStats',
  EXAM_HISTORY: PREFIX + 'examHistory',
  SETTINGS:     PREFIX + 'settings',
}

export function storageGet(key, fallback = null) {
  try {
    const raw = localStorage.getItem(key)
    return raw !== null ? JSON.parse(raw) : fallback
  } catch {
    return fallback
  }
}

export function storageSet(key, value) {
  try {
    localStorage.setItem(key, JSON.stringify(value))
    return true
  } catch {
    return false
  }
}

export function storageRemove(key) {
  try {
    localStorage.removeItem(key)
  } catch {}
}

export function exportAllProgress() {
  const out = {}
  Object.values(KEYS).forEach(k => {
    const val = storageGet(k)
    if (val !== null) out[k] = val
  })
  return out
}

export function importAllProgress(blob) {
  Object.values(KEYS).forEach(k => {
    if (blob[k] !== undefined) storageSet(k, blob[k])
  })
}

export function resetProgress() {
  Object.values(KEYS).forEach(k => storageRemove(k))
}
