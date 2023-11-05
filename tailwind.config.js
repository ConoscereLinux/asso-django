/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
      "asso/templates/**/*.{html,js}",
      "asso/*/templates/**/*.{html,js}",
  ],
  theme: {
    colors: {
      blue: "#5498fe",
      "blue-dark": "#4479cd",
      orange: "#cc6600",
      black: "#000000",
      white: "#fefefe",
      "gray": "#777777",
      "gray-dark": "#333333",
      "gray-light": "#cccccc",
    },
    fontFamily: {
      sans: ['Open Sans', 'sans-serif'],
    },
    extend: {
      borderWidth: {'DEFAULT': '3px'},
      borderColor: {'DEFAULT': '#333'},
      gridTemplateColumns: {
        '1-2/3': '1fr 2fr',
        '1-3/4': '1fr 3fr',
      }
    },
  },
  plugins: [],
}

