# QuizMaster

Aplicación web sencilla para realizar tests de estudio interactivos mediante la carga de archivos de datos. Funciona localmente en el navegador y no requiere conexión a internet (las fuentes y todo lo demás vienen empaquetados).

## Funcionamiento

La aplicación permite cargar cuestionarios, responder preguntas con feedback inmediato y revisar los resultados finales.

Tres formas de cargar un test:

* **Biblioteca incluida**: si abres la app servida por HTTP (ver Docker más abajo), aparece la sección "📚 Biblioteca" con todos los JSON del repo agrupados por carpeta. Click → carga.
* **Arrastrar y soltar**: arrastra un `.json` dentro del recuadro punteado.
* **Selección manual**: haz clic en el recuadro y elige un `.json` del explorador.

> La biblioteca solo aparece cuando la app se sirve por HTTP. Si abres `quiz-app.html` directamente con doble clic (`file://`), los navegadores bloquean `fetch` a archivos locales y solo verás drag&drop / selección manual.

## Despliegue airgapped con Docker (Raspberry Pi)

La app está pensada para correr en una Raspberry sin acceso a internet. Todas las dependencias (fuentes incluidas) se sirven desde el contenedor.

```bash
docker compose up -d --build
# abrir http://<ip-de-la-raspberry>:8080
```

El `Dockerfile` es multi-stage:

1. `python:3-alpine` ejecuta [`build-manifest.py`](build-manifest.py) y genera `quizzes.json` con todos los tests detectados.
2. `nginx:alpine` sirve los estáticos.

Compatible con `linux/arm64` (Pi 3/4/5 con 64 bits) y `linux/amd64`.

### Añadir o modificar tests

1. Mete tu nuevo `.json` en una carpeta del repo (existente o nueva).
2. `docker compose up -d --build` — el manifest se regenera automáticamente.

Si quieres regenerar `quizzes.json` fuera de Docker (por ejemplo para abrir la app con `python3 -m http.server`):

```bash
python3 build-manifest.py
```

### Acceso desde fuera de la LAN

El contenedor escucha solo en HTTP, sin auth. Opciones recomendadas (de menos a más esfuerzo):

* **Tailscale** (más simple): instala Tailscale en la Pi y en tu portátil/móvil. Accede a `http://<tailscale-ip>:8080`. Cero apertura de puertos, cifrado punto a punto.
* **Cloudflare Tunnel**: expón un subdominio HTTPS sin tocar el router. Añade Access Policy si quieres login.
* **Reverse proxy con TLS** (Caddy / Traefik) + redirección de puerto en tu router. Más control, más superficie de ataque.

> No expongas el puerto 8080 directamente al WAN sin TLS ni autenticación.

## Estructura del JSON

Para crear nuevos cuestionarios, el archivo JSON debe cumplir estrictamente con el siguiente formato:

```json
{
  "tema": "Nombre del tema o título del quiz",
  "preguntas": [
    {
      "pregunta": "Texto de la pregunta",
      "respuestas": [
        {
          "texto": "Texto de la opción 1",
          "correcta": true,
          "explicacion": "Explicación de por qué es correcta o incorrecta"
        },
        {
          "texto": "Texto de la opción 2",
          "correcta": false,
          "explicacion": "Explicación de por qué es correcta o incorrecta"
        }
      ]
    }
  ]
}

```

## Disclaimer

Las preguntas están generadas con diferentes servicios de IA a partir de los temarios oficiales. No me hago responsable de su exactitud, ni puedo asegurar al 100% que no haya alguna alucinación. No seáis unos haraganes y leeros el temario, chic@s.
