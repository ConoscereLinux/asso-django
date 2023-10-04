/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
      "asso/templates/**/*.{html,js}",
      "asso/*/templates/**/*.{html,js}",
  ],
  theme: {
    colors: {
      blue: "#5498fe",
      orange: "#cc6600",
      black: "#000000",
      white: "#FFFFFF",
      "gray-dark": "#333333",
      "gray-light": "#666666",
    },
    fontFamily: {
      sans: ['Open Sans', 'sans-serif'],
    },
    extends: {},
  },
  plugins: [],
}

