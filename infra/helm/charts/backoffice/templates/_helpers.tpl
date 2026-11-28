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

{{/*
Address the nginx of the back office proxies /v1/ to: platformUrl when it is set, otherwise the platform Service of
the same release, <release>-platform, named as the platform chart names it. The name is fully qualified
(<service>.<namespace>.svc.<clusterDomain>) because nginx resolves it through its own resolver, which does not apply
the search domains of the pod.
*/}}
{{- define "backoffice.platformUrl" -}}
{{- if .Values.platformUrl -}}
{{- .Values.platformUrl -}}
{{- else -}}
{{- $service := printf "%s-%s" .Release.Name "platform" | trunc 63 | trimSuffix "-" -}}
{{- printf "http://%s.%s.svc.%s:%v" $service .Release.Namespace .Values.clusterDomain .Values.platformPort -}}
{{- end -}}
{{- end -}}

{{/*
Environment variables of the container: ERP_PLATFORM_URL, then the env map, which wins on the same name.
*/}}
{{- define "backoffice.env" -}}
{{- $env := merge (dict) .Values.env (dict "ERP_PLATFORM_URL" (include "backoffice.platformUrl" .)) -}}
{{- range $name, $value := $env }}
- name: {{ $name }}
  value: {{ $value | quote }}
{{- end }}
{{- end -}}
