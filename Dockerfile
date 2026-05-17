# syntax=docker/dockerfile:1
# Imagen 100% offline: construye el manifest con Python y sirve estáticos con nginx.
# Compatible con linux/arm64 (Raspberry Pi 3/4/5) y linux/amd64.

FROM python:3.12-alpine AS builder
WORKDIR /src
COPY build-manifest.py ./
COPY quiz-app.html ./
COPY fonts/ ./fonts/
COPY Bastionado/ ./Bastionado/
COPY Incidentes/ ./Incidentes/
COPY Normativas/ ./Normativas/
COPY Hacking/ ./Hacking/
COPY PPS/ ./PPS/
COPY ejemplo-historia-espana.json ./
RUN python3 build-manifest.py

FROM nginx:1.27-alpine
COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=builder /src/quiz-app.html /usr/share/nginx/html/index.html
COPY --from=builder /src/quizzes.json /usr/share/nginx/html/quizzes.json
COPY --from=builder /src/fonts/ /usr/share/nginx/html/fonts/
COPY --from=builder /src/Bastionado/ /usr/share/nginx/html/Bastionado/
COPY --from=builder /src/Incidentes/ /usr/share/nginx/html/Incidentes/
COPY --from=builder /src/Normativas/ /usr/share/nginx/html/Normativas/
COPY --from=builder /src/Hacking/ /usr/share/nginx/html/Hacking/
COPY --from=builder /src/PPS/ /usr/share/nginx/html/PPS/
COPY --from=builder /src/ejemplo-historia-espana.json /usr/share/nginx/html/
EXPOSE 80
