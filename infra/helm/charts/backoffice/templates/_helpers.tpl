{{/*
Full name of the resources: the release name followed by the chart name.
*/}}
{{- define "backoffice.fullname" -}}
{{- printf "%s-%s" .Release.Name .Chart.Name | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{/*
Labels that select the pods of this chart.
*/}}
{{- define "backoffice.selectorLabels" -}}
app.kubernetes.io/name: {{ .Chart.Name }}
app.kubernetes.io/instance: {{ .Release.Name }}
{{- end -}}

{{/*
Standard labels of every resource.
*/}}
{{- define "backoffice.labels" -}}
{{ include "backoffice.selectorLabels" . }}
app.kubernetes.io/version: {{ .Chart.AppVersion | quote }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
app.kubernetes.io/part-of: simpleerp
helm.sh/chart: {{ printf "%s-%s" .Chart.Name .Chart.Version | replace "+" "_" | quote }}
{{- end -}}

{{/*
Image reference: the registry path, the image name and the tag.
*/}}
{{- define "backoffice.image" -}}
{{- printf "%s-%s:%s" .Values.global.image.prefix .Values.image.name (.Values.global.image.tag | default .Chart.AppVersion) -}}
{{- end -}}
