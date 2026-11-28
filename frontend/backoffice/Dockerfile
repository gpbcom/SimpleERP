# syntax=docker/dockerfile:1
# Build context: the repository root (pnpm-lock.yaml lives there).
FROM node:22-alpine AS build
RUN corepack enable
WORKDIR /repo
COPY package.json pnpm-workspace.yaml pnpm-lock.yaml ./
COPY frontend/packages/ frontend/packages/
COPY frontend/backoffice/ frontend/backoffice/
RUN pnpm install --frozen-lockfile --filter "./frontend/backoffice..." --filter "./frontend/packages/*" \
    && pnpm --filter ./frontend/packages/tokens run build \
    && pnpm --filter ./frontend/packages/ui run build \
    && pnpm --filter ./frontend/backoffice run build

FROM nginxinc/nginx-unprivileged:alpine AS runtime
USER root
RUN apk upgrade --no-cache
USER 101
COPY frontend/backoffice/nginx.conf /etc/nginx/templates/default.conf.template
COPY --from=build /repo/frontend/backoffice/dist /usr/share/nginx/html
ENV ERP_PLATFORM_URL=http://platform:8000 NGINX_ENTRYPOINT_LOCAL_RESOLVERS=1
EXPOSE 8080
HEALTHCHECK --interval=10s --timeout=3s --start-period=5s --retries=3 \
    CMD wget -q -O /dev/null http://127.0.0.1:8080/ || exit 1
