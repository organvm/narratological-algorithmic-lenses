/**
 * API client for the narratological backend.
 */

const API_BASE = '/api'

export interface StudySummary {
  id: string
  creator: string
  work: string
  category: string
  axiom_count: number
  algorithm_count: number
  question_count: number
}

export interface Axiom {
  id: string
  name: string
  statement: string
  derivations: string[]
}

export interface Algorithm {
  name: string
  purpose: string
  pseudocode: string
  inputs: string[]
  outputs: string[]
}

export interface DiagnosticQuestion {
  id: string
  question: string
  valid_if: string
}

export interface HierarchyLevel {
  level: number
  name: string
  description: string
  elements: string[]
}

export interface Study {
  id: string
  creator: string
  work: string
  category: string
  axioms: Axiom[]
  structural_hierarchy: {
    levels: HierarchyLevel[]
  }
  core_algorithms: Algorithm[]
  diagnostic_questions: DiagnosticQuestion[]
  theoretical_correspondences: {
    maps_to: string[]
    sequence_pairs: string[]
  }
  quick_reference: {
    core_operations: string[]
    key_constraints: string[]
  }
}

export interface SequencePair {
  id: string
  name: string
  studies: string[]
  shared_principles: string[]
  contrasts: string[]
}

async function fetchJson<T>(url: string, init?: RequestInit): Promise<T> {
  const response = await fetch(url, init)
  if (!response.ok) {
    throw new Error(`API error: ${response.statusText}`)
  }
  return response.json()
}

export async function fetchStudies(category?: string): Promise<StudySummary[]> {
  const url = category
    ? `${API_BASE}/studies/?category=${encodeURIComponent(category)}`
    : `${API_BASE}/studies/`
  return fetchJson<StudySummary[]>(url)
}

export async function fetchStudy(studyId: string): Promise<Study> {
  return fetchJson<Study>(`${API_BASE}/studies/${studyId}`)
}

export async function fetchAxioms(studyId: string): Promise<Axiom[]> {
  return fetchJson<Axiom[]>(`${API_BASE}/studies/${studyId}/axioms`)
}

export async function fetchAlgorithms(studyId: string): Promise<Algorithm[]> {
  return fetchJson<Algorithm[]>(`${API_BASE}/studies/${studyId}/algorithms`)
}

export async function fetchQuestions(studyId: string): Promise<DiagnosticQuestion[]> {
  return fetchJson<DiagnosticQuestion[]>(`${API_BASE}/studies/${studyId}/questions`)
}

export async function fetchSequencePairs(): Promise<SequencePair[]> {
  return fetchJson<SequencePair[]>(`${API_BASE}/studies/pairs`)
}

export async function searchAxioms(query: string): Promise<Array<{
  study_id: string
  axiom: Axiom
}>> {
  return fetchJson(`${API_BASE}/studies/search/axioms?q=${encodeURIComponent(query)}`)
}

export async function searchAlgorithms(query: string): Promise<Array<{
  study_id: string
  algorithm: Algorithm
}>> {
  return fetchJson(`${API_BASE}/studies/search/algorithms?q=${encodeURIComponent(query)}`)
}

export async function fetchApiStats(): Promise<{
  study_count: number
  total_axioms: number
  total_algorithms: number
  total_diagnostic_questions: number
  categories: string[]
  sequence_pairs: number
}> {
  return fetchJson(`${API_BASE}/stats`)
}

export interface TierEntitlements {
  tier: 'free_trial' | 'creator' | 'studio'
  label: string
  price_monthly_usd: number
  monthly_quota: number
  max_input_chars: number
  algorithm_limit: number
  full_suite: boolean
  support: string
}

export interface BillingTier {
  tier: 'free_trial' | 'creator' | 'studio'
  entitlements: TierEntitlements
  checkout_available: boolean
}

export interface CheckoutSession {
  provider: 'stripe'
  checkout_session_id: string
  checkout_url: string
  tier: 'creator' | 'studio'
  mode: 'subscription'
}

export interface CheckoutLicense {
  license_key: string
  account_id: string
  tier: 'creator' | 'studio'
  status: string
  license_fingerprint: string
}

export interface SubscriptionStatus {
  account_id: string
  tier: 'free_trial' | 'creator' | 'studio'
  entitlements: TierEntitlements
  active: boolean
  source: string
  subscription_status: string | null
  billing_provider: string | null
  license_fingerprint: string
}

export async function fetchBillingTiers(): Promise<BillingTier[]> {
  return fetchJson<BillingTier[]>(`${API_BASE}/billing/tiers`)
}

export async function createCheckoutSession(
  tier: 'creator' | 'studio',
  email?: string,
): Promise<CheckoutSession> {
  return fetchJson<CheckoutSession>(`${API_BASE}/billing/checkout`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ tier, email: email || undefined }),
  })
}

export async function fetchCheckoutLicense(sessionId: string): Promise<CheckoutLicense> {
  return fetchJson<CheckoutLicense>(
    `${API_BASE}/billing/checkout-sessions/${encodeURIComponent(sessionId)}/license`,
  )
}

export async function fetchSubscriptionStatus(apiKey: string): Promise<SubscriptionStatus> {
  return fetchJson<SubscriptionStatus>(`${API_BASE}/billing/subscription`, {
    headers: {
      'X-API-Key': apiKey,
    },
  })
}

/**
 * Generic API object for GET/POST requests.
 */
export const api = {
  get: async <T>(path: string): Promise<T> => {
    const url = path.startsWith('/') ? `${API_BASE}${path}` : `${API_BASE}/${path}`
    return fetchJson<T>(url)
  },
  post: async <T>(path: string, body: any): Promise<T> => {
    const url = path.startsWith('/') ? `${API_BASE}${path}` : `${API_BASE}/${path}`
    const response = await fetch(url, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(body),
    })
    if (!response.ok) {
      throw new Error(`API error: ${response.statusText}`)
    }
    return response.json()
  }
}
