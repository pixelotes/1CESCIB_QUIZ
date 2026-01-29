# QuizMaster

Aplicación web sencilla para realizar tests de estudio interactivos mediante la carga de archivos de datos. Funciona localmente en el navegador y no requiere instalación ni conexión a internet.

## Funcionamiento

La aplicación permite cargar cuestionarios, responder preguntas con feedback inmediato y revisar los resultados finales.

Para utilizarla:

1. Abre el archivo `quiz-app.html` en tu navegador web.
2. Carga un archivo de preguntas utilizando uno de estos dos métodos:
   * **Arrastrar y soltar**: Arrastra el archivo .json dentro del recuadro punteado.
   * **Selección manual**: Haz clic en el recuadro para abrir el explorador de archivos y selecciona el .json.

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
