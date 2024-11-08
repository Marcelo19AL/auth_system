/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './accounts/templates/**/*.html',  // Ruta a tus archivos HTML en templates
    './accounts/static/css/*.css',     // Opcional: incluye tu CSS si es necesario
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
