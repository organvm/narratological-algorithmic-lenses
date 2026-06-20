import { describe, expect, it, vi, beforeEach } from 'vitest'
import { renderToString } from 'react-dom/server'
import { StaticRouter } from 'react-router-dom/server'
import StatusDashboard, { buildDashboardMetrics } from './StatusDashboard'
import type { ApiStats, StudySummary } from '../api/client'

beforeEach(() => {
  vi.restoreAllMocks()
})

const studies: StudySummary[] = [
  {
    id: 'aristotle',
    creator: 'Aristotle',
    work: 'Poetics',
    category: 'Classical',
    axiom_count: 3,
    algorithm_count: 2,
    question_count: 4,
  },
  {
    id: 'egri',
    creator: 'Lajos Egri',
    work: 'The Art of Dramatic Writing',
    category: 'Dramatic Structure',
    axiom_count: 4,
    algorithm_count: 5,
    question_count: 6,
  },
  {
    id: 'mckee',
    creator: 'Robert McKee',
    work: 'Story',
    category: 'Dramatic Structure',
    axiom_count: 2,
    algorithm_count: 1,
    question_count: 3,
  },
]

const stats: ApiStats = {
  study_count: 3,
  total_axioms: 9,
  total_algorithms: 8,
  total_diagnostic_questions: 13,
  categories: ['Classical', 'Dramatic Structure'],
  sequence_pairs: 2,
}

describe('StatusDashboard', () => {
  it('shows loading state during SSR', () => {
    vi.spyOn(globalThis, 'fetch').mockResolvedValue(
      new Response(JSON.stringify({ status: 'healthy' }), { status: 200 }),
    )

    const html = renderToString(
      <StaticRouter location="/dashboard">
        <StatusDashboard />
      </StaticRouter>,
    )

    expect(html).toContain('Loading dashboard...')
  })

  it('builds totals and averages from API stats', () => {
    const metrics = buildDashboardMetrics(stats, studies)

    expect(metrics.totals.studyCount).toBe(3)
    expect(metrics.totals.contentItemCount).toBe(30)
    expect(metrics.totals.sequencePairCount).toBe(2)
    expect(metrics.averageAlgorithmsPerStudy).toBeCloseTo(2.67)
    expect(metrics.averageQuestionsPerStudy).toBeCloseTo(4.33)
  })

  it('sorts categories and instrumented frameworks by activity', () => {
    const metrics = buildDashboardMetrics(stats, studies)

    expect(metrics.categoryBreakdown[0]).toMatchObject({
      category: 'Dramatic Structure',
      studyCount: 2,
      algorithmCount: 6,
      questionCount: 9,
    })
    expect(metrics.mostInstrumentedStudies[0]).toMatchObject({
      id: 'egri',
      score: 15,
    })
  })

  it('falls back to study summaries when stats are unavailable', () => {
    const metrics = buildDashboardMetrics(null, studies)

    expect(metrics.totals.axiomCount).toBe(9)
    expect(metrics.totals.algorithmCount).toBe(8)
    expect(metrics.totals.diagnosticQuestionCount).toBe(13)
    expect(metrics.totals.categoryCount).toBe(2)
  })
})
