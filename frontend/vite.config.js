import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  root: '.', // Explicitly set root directory
  server: {
    port: 3000,
    host: true, // Permite el acceso desde fuera del contenedor
  },
  build: {
    outDir: 'dist',          // Asegura que se construya en /dist
    emptyOutDir: true,       // Limpia la carpeta antes de build
  },
  base: './',                // 👈 Rutas relativas para nginx
});
