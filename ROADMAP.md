# **Project Roadmap**

<sub>_Este documento proporciona una visión general estructurada de los hitos clave, tareas completadas y objetivos futuros del proyecto._</sub>

## **Milestone 0.1.0: Configuración Inicial y Funcionalidades Básicas.**

**Focus**: Establecer la base técnica del proyecto y las funcionalidades fundamentales necesarias para su operación.

- **Project Setup.**

  - [x] Inicializar el proyecto con Django.
  - [x] Configurar PostgreSQL como base de datos mediante Railway.
  - [x] Desplegar la aplicación en Vercel.
  - [x] Crear la app `core` para gestionar elementos estáticos y la plantilla principal (`base.html`).

- **User Management.**

  - [x] Desarrollar la app `authentication` para registro, inicio/cierre de sesión y edición de perfiles.

- **API Integration.**
  - [x] Implementar la API de Recetas de Edamam (`recipes`) para recetas predefinidas.
  - [x] Integrar la API de Nutrición de Edamam (`nutrition`) para obtener información nutricional.

## **Milestone 0.2.0: Ampliación de Funcionalidades y Mejora de la Experiencia de Usuario.**

**Focus**: Expandir características principales, incluyendo carrito de compras y procesamiento de pagos.

- **Shopping Cart and Orders.**

  - [x] Implementar la app `cart` para gestionar un carrito dinámico.
  - [x] Añadir seguimiento de pedidos con actualizaciones desde Django admin.
  - [x] Incluir un historial de pedidos para los usuarios.

- **Payment Integration.**

  - [x] Configurar Stripe como pasarela de pago segura en modo de prueba.
  - [x] Implementar páginas de redirección tras éxito o cancelación del pago.

- **Design Enhancements.**
  - [x] Diseñar un sistema visual consistente con Figma.
  - [x] Convertir diseños a HTML/CSS utilizando Builder.io.

## **Milestone 0.3.0: Automatización, Optimización y Documentación.**

**Focus**: Optimizar el proyecto mediante automatización y mejora de la documentación.

- **CI/CD.**

  - [x] Configurar GitHub Actions para automatizar:
    - Actualizaciones mensuales de la base de datos con las APIs de Edamam.
    - Pruebas y despliegues continuos.

- **Documentation.**

  - [x] Crear `README.md` con una visión completa del proyecto.
  - [x] Generar automáticamente `CHANGELOG.md` con GitHub Actions.

- **Local Development with Docker.**
  - [x] Configurar Docker para entornos de desarrollo local.
  - [x] Documentar en `DockerSetUp.md` para guiar a los colaboradores.

<sub>_Este roadmap asegura un desarrollo estructurado, alineado con los objetivos estratégicos y enfocado en la entrega de valor._</sub>
