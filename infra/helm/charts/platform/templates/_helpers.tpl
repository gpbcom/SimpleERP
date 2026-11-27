{{/* The full name of the resources: <release>-platform. */}}
{{- define "platform.fullname" -}}
{{- printf "%s-%s" .Release.Name .Chart.Name | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{/* The labels that select the pods. */}}
{{- define "platform.selectorLabels" -}}
app.kubernetes.io/name: {{ .Chart.Name }}
app.kubernetes.io/instance: {{ .Release.Name }}
{{- end -}}

{{/* The standard labels of every resource. */}}
{{- define "platform.labels" -}}
{{ include "platform.selectorLabels" . }}
app.kubernetes.io/version: {{ .Chart.AppVersion | quote }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
app.kubernetes.io/part-of: simpleerp
{{- end -}}

{{/* The image: <prefix>-<name>:<tag, else the app version>. */}}
{{- define "platform.image" -}}
{{- printf "%s-%s:%s" .Values.global.image.prefix .Values.image.name (.Values.global.image.tag | default .Chart.AppVersion) -}}
{{- end -}}
