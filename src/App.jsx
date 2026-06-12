import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom'
import { useEffect } from 'react'
import Layout from './components/Layout'
import Dashboard from './pages/Dashboard'
import Flashcards from './pages/Flashcards'
import Quiz from './pages/Quiz'
import Exam from './pages/Exam'
import Settings from './pages/Settings'
import { storageGet, KEYS } from './lib/storage'

// Apply saved dark mode preference before first paint
function useDarkModeInit() {
  useEffect(() => {
    const saved = storageGet(KEYS.SETTINGS, {})
    if (saved.darkMode) {
      document.documentElement.classList.add('dark')
    }
  }, [])
}

export default function App() {
  useDarkModeInit()

  return (
    <BrowserRouter>
      <Layout>
        <Routes>
          <Route path="/"           element={<Dashboard />} />
          <Route path="/flashcards" element={<Flashcards />} />
          <Route path="/quiz"       element={<Quiz />} />
          <Route path="/exam"       element={<Exam />} />
          <Route path="/settings"   element={<Settings />} />
          <Route path="*"           element={<Navigate to="/" replace />} />
        </Routes>
      </Layout>
    </BrowserRouter>
  )
}
