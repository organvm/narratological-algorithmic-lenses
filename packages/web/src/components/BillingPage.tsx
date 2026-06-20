import { useEffect, useState } from 'react'
import { useSearchParams } from 'react-router-dom'
import {
  createCheckoutSession,
  fetchBillingTiers,
  fetchCheckoutLicense,
  fetchSubscriptionStatus,
  type BillingTier,
  type CheckoutLicense,
  type SubscriptionStatus,
} from '../api/client'

type PaidTier = 'creator' | 'studio'

function formatCharacters(value: number): string {
  return new Intl.NumberFormat().format(value)
}

function tierSummary(tier: BillingTier): string {
  const entitlements = tier.entitlements
  const suite = entitlements.full_suite
    ? 'Full 92-algorithm suite'
    : `${entitlements.algorithm_limit}-algorithm preview`
  return `${entitlements.monthly_quota} analyses / ${formatCharacters(
    entitlements.max_input_chars,
  )} chars / ${suite}`
}

export default function BillingPage() {
  const [searchParams] = useSearchParams()
  const sessionId = searchParams.get('session_id')
  const [tiers, setTiers] = useState<BillingTier[]>([])
  const [email, setEmail] = useState('')
  const [licenseKey, setLicenseKey] = useState('')
  const [checkoutLicense, setCheckoutLicense] = useState<CheckoutLicense | null>(null)
  const [subscription, setSubscription] = useState<SubscriptionStatus | null>(null)
  const [loadingTier, setLoadingTier] = useState<string | null>(null)
  const [loadingLicense, setLoadingLicense] = useState(false)
  const [loadingStatus, setLoadingStatus] = useState(false)
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    fetchBillingTiers()
      .then(setTiers)
      .catch((err) => setError(err.message))
  }, [])

  useEffect(() => {
    if (!sessionId) {
      return
    }
    setLoadingLicense(true)
    fetchCheckoutLicense(sessionId)
      .then(setCheckoutLicense)
      .catch((err) => setError(err.message))
      .finally(() => setLoadingLicense(false))
  }, [sessionId])

  const startCheckout = async (tier: PaidTier) => {
    setError(null)
    setLoadingTier(tier)
    try {
      const session = await createCheckoutSession(tier, email.trim() || undefined)
      window.location.href = session.checkout_url
    } catch (err: any) {
      setError(err.message || 'Checkout failed')
    } finally {
      setLoadingTier(null)
    }
  }

  const checkSubscription = async () => {
    setError(null)
    setSubscription(null)
    setLoadingStatus(true)
    try {
      setSubscription(await fetchSubscriptionStatus(licenseKey.trim()))
    } catch (err: any) {
      setError(err.message || 'License check failed')
    } finally {
      setLoadingStatus(false)
    }
  }

  return (
    <div className="billing-page">
      <header className="billing-header">
        <h2>Billing</h2>
        <p>Choose access for the gated narratological-92 API suite.</p>
      </header>

      {error && <div className="error">{error}</div>}

      {checkoutLicense && (
        <section className="license-panel">
          <div>
            <h3>License Ready</h3>
            <p>{checkoutLicense.tier} subscription is {checkoutLicense.status}.</p>
          </div>
          <code>{checkoutLicense.license_key}</code>
        </section>
      )}

      {loadingLicense && (
        <div className="loading">Waiting for checkout license...</div>
      )}

      <section className="checkout-controls">
        <label htmlFor="billing-email">Email</label>
        <input
          id="billing-email"
          type="email"
          value={email}
          placeholder="writer@example.com"
          onChange={(event) => setEmail(event.target.value)}
        />
      </section>

      <section className="tier-grid">
        {tiers.map((tier) => (
          <article key={tier.tier} className="tier-card">
            <div>
              <h3>{tier.entitlements.label}</h3>
              <p className="tier-price">
                ${tier.entitlements.price_monthly_usd}
                <span>/mo</span>
              </p>
            </div>
            <p>{tierSummary(tier)}</p>
            <p className="tier-support">{tier.entitlements.support}</p>
            {tier.checkout_available ? (
              <button
                onClick={() => startCheckout(tier.tier as PaidTier)}
                disabled={loadingTier !== null}
              >
                {loadingTier === tier.tier ? 'Opening...' : 'Checkout'}
              </button>
            ) : tier.tier === 'free_trial' ? (
              <span className="tier-badge">Free tier preserved</span>
            ) : (
              <span className="tier-badge">Checkout not configured</span>
            )}
          </article>
        ))}
      </section>

      <section className="license-checker">
        <h3>License Status</h3>
        <div className="license-checker-row">
          <input
            type="password"
            value={licenseKey}
            placeholder="API key or license key"
            onChange={(event) => setLicenseKey(event.target.value)}
          />
          <button
            onClick={checkSubscription}
            disabled={loadingStatus || licenseKey.trim().length === 0}
          >
            {loadingStatus ? 'Checking...' : 'Check'}
          </button>
        </div>

        {subscription && (
          <div className="subscription-result">
            <strong>{subscription.entitlements.label}</strong>
            <span>{subscription.active ? 'Active' : 'Inactive'}</span>
            <span>{subscription.source}</span>
          </div>
        )}
      </section>
    </div>
  )
}
