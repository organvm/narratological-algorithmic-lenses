import { useEffect, useState } from 'react'
import {
  fetchApiStats,
  fetchHealth,
  fetchStudies,
  type ApiStats,
  type StudySummary,
} from '../api/client'

type ServiceStatus = 'loading' | 'online' | 'degraded' | 'offline'

interface DashboardTotals {
  studyCount: number
  axiomCount: number
  algorithmCount: number
  diagnosticQuestionCount: number
  categoryCount: number
  sequencePairCount: number
  contentItemCount: number
}

interface CategoryMetric {
  category: string
  studyCount: number
  algorithmCount: number
  questionCount: number
  share: number
}

interface StudyInstrumentation {
  id: string
  creator: string
  work: string
  score: number
  algorithmCount: number
  questionCount: number
}

interface DashboardMetrics {
  totals: DashboardTotals
  averageAlgorithmsPerStudy: number
  averageQuestionsPerStudy: number
  categoryBreakdown: CategoryMetric[]
  mostInstrumentedStudies: StudyInstrumentation[]
}

const numberFormatter = new Intl.NumberFormat('en-US')

function sumStudies(
  studies: StudySummary[],
  key: 'axiom_count' | 'algorithm_count' | 'question_count',
) {
  return studies.reduce((total, study) => total + study[key], 0)
}

function getStatusLabel(status: ServiceStatus) {
  switch (status) {
    case 'online':
      return 'API healthy'
    case 'degraded':
      return 'Partial data'
    case 'offline':
      return 'Unavailable'
    default:
      return 'Checking API'
  }
}

function formatNumber(value: number) {
  return numberFormatter.format(value)
}

function formatAverage(value: number) {
  return value.toFixed(1).replace(/\.0$/, '')
}

export function buildDashboardMetrics(
  stats: ApiStats | null,
  studies: StudySummary[],
): DashboardMetrics {
  const categories =
    stats?.categories ?? Array.from(new Set(studies.map((study) => study.category)))
  const studyCount = stats?.study_count ?? studies.length
  const axiomCount = stats?.total_axioms ?? sumStudies(studies, 'axiom_count')
  const algorithmCount = stats?.total_algorithms ?? sumStudies(studies, 'algorithm_count')
  const diagnosticQuestionCount =
    stats?.total_diagnostic_questions ?? sumStudies(studies, 'question_count')

  const categoryBreakdown = categories
    .map((category) => {
      const categoryStudies = studies.filter((study) => study.category === category)
      return {
        category,
        studyCount: categoryStudies.length,
        algorithmCount: sumStudies(categoryStudies, 'algorithm_count'),
        questionCount: sumStudies(categoryStudies, 'question_count'),
        share: studyCount > 0 ? categoryStudies.length / studyCount : 0,
      }
    })
    .sort((a, b) => b.studyCount - a.studyCount || a.category.localeCompare(b.category))

  const mostInstrumentedStudies = [...studies]
    .map((study) => ({
      id: study.id,
      creator: study.creator,
      work: study.work,
      score: study.axiom_count + study.algorithm_count + study.question_count,
      algorithmCount: study.algorithm_count,
      questionCount: study.question_count,
    }))
    .sort((a, b) => b.score - a.score || a.creator.localeCompare(b.creator))
    .slice(0, 3)

  return {
    totals: {
      studyCount,
      axiomCount,
      algorithmCount,
      diagnosticQuestionCount,
      categoryCount: categories.length,
      sequencePairCount: stats?.sequence_pairs ?? 0,
      contentItemCount: axiomCount + algorithmCount + diagnosticQuestionCount,
    },
    averageAlgorithmsPerStudy: studyCount > 0 ? algorithmCount / studyCount : 0,
    averageQuestionsPerStudy: studyCount > 0 ? diagnosticQuestionCount / studyCount : 0,
    categoryBreakdown,
    mostInstrumentedStudies,
  }
}

export default function StatusDashboard() {
  const [stats, setStats] = useState<ApiStats | null>(null)
  const [studies, setStudies] = useState<StudySummary[]>([])
  const [status, setStatus] = useState<ServiceStatus>('loading')
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    let cancelled = false

    async function loadDashboard() {
      setLoading(true)
      setError(null)

      const [statsResult, studiesResult, healthResult] = await Promise.allSettled([
        fetchApiStats(),
        fetchStudies(),
        fetchHealth(),
      ])

      if (cancelled) {
        return
      }

      if (statsResult.status === 'fulfilled') {
        setStats(statsResult.value)
      }

      if (studiesResult.status === 'fulfilled') {
        setStudies(studiesResult.value)
      }

      const hasMetrics =
        statsResult.status === 'fulfilled' || studiesResult.status === 'fulfilled'
      const isHealthy =
        healthResult.status === 'fulfilled' && healthResult.value.status === 'healthy'

      setStatus(isHealthy ? 'online' : hasMetrics ? 'degraded' : 'offline')

      if (!hasMetrics) {
        setError('Dashboard metrics are unavailable.')
      } else if (statsResult.status === 'rejected' || studiesResult.status === 'rejected') {
        setError('Some dashboard metrics could not be loaded.')
      }

      setLoading(false)
    }

    loadDashboard()

    return () => {
      cancelled = true
    }
  }, [])

  const metrics = buildDashboardMetrics(stats, studies)

  if (loading) {
    return <div className="loading">Loading dashboard...</div>
  }

  if (error && metrics.totals.contentItemCount === 0 && metrics.totals.studyCount === 0) {
    return <div className="error">{error}</div>
  }

  return (
    <div className="status-dashboard">
      <div className="dashboard-heading">
        <div>
          <p className="dashboard-eyebrow">Product dashboard</p>
          <h2>Status and usage</h2>
          <p className="dashboard-summary">
            Current coverage across the narratological framework catalog.
          </p>
        </div>
        <div className={`status-indicator ${status}`} aria-label={`Service status: ${status}`}>
          <span aria-hidden="true" />
          {getStatusLabel(status)}
        </div>
      </div>

      {error && <div className="dashboard-alert">{error}</div>}

      <section className="metric-grid" aria-label="Key product metrics">
        <article className="metric-card">
          <span className="metric-label">Studies</span>
          <strong>{formatNumber(metrics.totals.studyCount)}</strong>
          <small>{formatNumber(metrics.totals.categoryCount)} categories represented</small>
        </article>
        <article className="metric-card">
          <span className="metric-label">Algorithms</span>
          <strong>{formatNumber(metrics.totals.algorithmCount)}</strong>
          <small>
            {formatAverage(metrics.averageAlgorithmsPerStudy)} per study on average
          </small>
        </article>
        <article className="metric-card">
          <span className="metric-label">Diagnostics</span>
          <strong>{formatNumber(metrics.totals.diagnosticQuestionCount)}</strong>
          <small>
            {formatAverage(metrics.averageQuestionsPerStudy)} checks per study
          </small>
        </article>
        <article className="metric-card">
          <span className="metric-label">Axioms</span>
          <strong>{formatNumber(metrics.totals.axiomCount)}</strong>
          <small>{formatNumber(metrics.totals.contentItemCount)} indexed items total</small>
        </article>
        <article className="metric-card">
          <span className="metric-label">Sequence pairs</span>
          <strong>{formatNumber(metrics.totals.sequencePairCount)}</strong>
          <small>Cross-framework comparison tracks</small>
        </article>
      </section>

      <div className="dashboard-layout">
        <section className="dashboard-panel">
          <h3>Category coverage</h3>
          <div className="category-breakdown">
            {metrics.categoryBreakdown.map((category) => (
              <div className="category-row" key={category.category}>
                <div className="category-row-header">
                  <strong>{category.category}</strong>
                  <span>{category.studyCount} studies</span>
                </div>
                <div className="category-meter" aria-hidden="true">
                  <span style={{ width: `${Math.max(category.share * 100, 4)}%` }} />
                </div>
                <small>
                  {category.algorithmCount} algorithms, {category.questionCount} diagnostics
                </small>
              </div>
            ))}
          </div>
        </section>

        <section className="dashboard-panel">
          <h3>Most instrumented frameworks</h3>
          <ol className="instrumented-list">
            {metrics.mostInstrumentedStudies.map((study) => (
              <li key={study.id}>
                <div>
                  <strong>{study.creator}</strong>
                  <span>{study.work}</span>
                </div>
                <small>
                  {study.score} items - {study.algorithmCount} algorithms -{' '}
                  {study.questionCount} diagnostics
                </small>
              </li>
            ))}
          </ol>
        </section>
      </div>
    </div>
  )
}
