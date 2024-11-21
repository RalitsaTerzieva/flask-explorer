/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './*.html', // Adjust based on your folder structure
    './templates/**/*.html', // For Flask template folders
    './static/**/*.js', // For JS files if using dynamic classes
  ],
  theme: {
    extend: {},
  },
  plugins: [],
};