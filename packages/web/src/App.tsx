import { Routes, Route, Link } from 'react-router-dom'
import StudyExplorer from './components/StudyExplorer'
import AlgorithmViewer from './components/AlgorithmViewer'
import DiagnosticRunner from './components/DiagnosticRunner'
import { ScriptDoctorWorkbench } from './components/ScriptDoctorWorkbench'
import StatusDashboard from './components/StatusDashboard'

function App() {
  return (
    <div className="app">
      <header className="app-header">
        <h1>Narratological Algorithmic Lenses</h1>
        <nav>
          <Link to="/dashboard">Dashboard</Link>
          <Link to="/">Studies</Link>
          <Link to="/algorithms">Algorithms</Link>
          <Link to="/diagnostics">Diagnostics</Link>
          <Link to="/script-doctor">Script Doctor</Link>
        </nav>
      </header>

      <main className="app-main">
        <Routes>
          <Route path="/dashboard" element={<StatusDashboard />} />
          <Route path="/" element={<StudyExplorer />} />
          <Route path="/study/:studyId" element={<StudyExplorer />} />
          <Route path="/algorithms" element={<AlgorithmViewer />} />
          <Route path="/algorithms/:studyId/:algoName" element={<AlgorithmViewer />} />
          <Route path="/diagnostics" element={<DiagnosticRunner />} />
          <Route path="/script-doctor" element={<ScriptDoctorWorkbench />} />
        </Routes>
      </main>

      <footer className="app-footer">
        <p>Narratological Algorithmic Lenses - Analyze narratives using formalized algorithms</p>
      </footer>
    </div>
  )
}

export default App
