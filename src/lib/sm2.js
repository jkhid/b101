// Simplified SM-2 spaced repetition algorithm
// Rating: 0 = Again, 1 = Good, 2 = Easy

const EASE_FLOOR = 1.3
const EASE_START = 2.5

export function defaultCardState() {
  return {
    repetitions: 0,
    easeFactor: EASE_START,
    intervalDays: 0,
    dueDate: new Date().toISOString(),
  }
}

export function reviewCard(state, rating) {
  let { repetitions, easeFactor, intervalDays } = state

  if (rating === 0) {
    // Again — reset; due immediately
    repetitions = 0
    intervalDays = 0
    easeFactor = Math.max(EASE_FLOOR, easeFactor - 0.2)
  } else {
    // Good (1) or Easy (2)
    if (repetitions === 0) {
      intervalDays = 1
    } else if (repetitions === 1) {
      intervalDays = 6
    } else {
      intervalDays = Math.round(intervalDays * easeFactor)
    }
    repetitions += 1

    if (rating === 2) {
      easeFactor = Math.min(easeFactor + 0.15, 3.0)
      intervalDays = Math.round(intervalDays * 1.3)
    }
    // Good keeps easeFactor unchanged
  }

  const dueDate = new Date()
  if (intervalDays > 0) {
    dueDate.setDate(dueDate.getDate() + intervalDays)
  }

  return { repetitions, easeFactor, intervalDays, dueDate: dueDate.toISOString() }
}

export function isDueToday(state) {
  if (!state) return true
  return new Date(state.dueDate) <= new Date()
}
