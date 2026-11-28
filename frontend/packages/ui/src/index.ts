export { default as UiButton } from './components/UiButton.vue'
export { default as UiFormField } from './components/UiFormField.vue'
export { default as UiNavItem } from './components/UiNavItem.vue'
export { default as UiToast } from './components/UiToast.vue'
export { default as UiModal } from './components/UiModal.vue'
export { default as UiCard } from './components/UiCard.vue'
export { default as UiIcon } from './components/UiIcon.vue'
export { default as UiSpinner } from './components/UiSpinner.vue'
export { default as ErrorDialog } from './errors/ErrorDialog.vue'
export { default as ErrorBanner } from './errors/ErrorBanner.vue'

import type ErrorBannerComponent from './errors/ErrorBanner.vue'
import type ErrorDialogComponent from './errors/ErrorDialog.vue'

export type ErrorDialogProps = InstanceType<typeof ErrorDialogComponent>['$props']
export type ErrorBannerProps = InstanceType<typeof ErrorBannerComponent>['$props']
