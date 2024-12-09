/** @type {import('tailwindcss').Config} */
module.exports = {
  images: {
    domains: ['https://www.smtu.ru/ru/viewnews'],  // Разрешённые домены
  },
  
  content: [
    "./pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./components/**/*.{js,ts,jsx,tsx,mdx}",
    "./app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      colors: {
        background: "var(--background)",
        foreground: "var(--foreground)",
      },
    },
  },
  plugins: [],
};
