import { describe, expect, it, vi, beforeEach } from 'vitest'
import { renderToString } from 'react-dom/server'
import { StaticRouter } from 'react-router-dom/server'
import BillingPage from './BillingPage'

beforeEach(() => {
  vi.restoreAllMocks()
})

describe('BillingPage', () => {
  it('renders the billing heading', () => {
    vi.spyOn(globalThis, 'fetch').mockResolvedValue(
      new Response(JSON.stringify([]), { status: 200 }),
    )

    const html = renderToString(
      <StaticRouter location="/billing">
        <BillingPage />
      </StaticRouter>,
    )

    expect(html).toContain('Billing')
    expect(html).toContain('License Status')
  })
})
