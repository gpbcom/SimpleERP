import { callPlatform } from './platformClient'

/**
 * Call the platform's health endpoint once. A refusal shows as a banner with this check as its retry action, and the
 * error is caught so that the shell keeps running.
 */
export async function checkPlatform(): Promise<void> {
  try {
    await callPlatform((client) => client.GET('/v1/health'), {
      presentation: 'banner',
      onAction: () => {
        void checkPlatform()
      },
    })
  } catch {
    // The refusal is already in the error store.
  }
}
