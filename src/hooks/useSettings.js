import { useState, useEffect } from 'react'
import { storageGet, storageSet, KEYS } from '../lib/storage'

const DEFAULTS = {
  darkMode: false,
  examDurationMins: 60,
}

export function useSettings() {
  const [settings, setSettingsState] = useState(() =>
    storageGet(KEYS.SETTINGS, DEFAULTS)
  )

  useEffect(() => {
    const root = document.documentElement
    if (settings.darkMode) {
      root.classList.add('dark')
    } else {
      root.classList.remove('dark')
    }
  }, [settings.darkMode])

  function setSettings(patch) {
    setSettingsState(prev => {
      const next = { ...prev, ...patch }
      storageSet(KEYS.SETTINGS, next)
      return next
    })
  }

  return { settings, setSettings }
}
