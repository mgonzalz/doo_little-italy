# Changelog.

<sub>This file documents the major changes, enhancements, bug fixes, and updates applied to the project.</sub>

---

## [Unreleased.]

### Added

- Initial setup of the **Django** framework and project structure.
- Integration of **Edamam APIs** for Recipes and Nutrition.
- Implementation of a responsive design using **Builder.io** for HTML templates.
- Integration with **Stripe** for payment processing in test mode.
- User authentication system, including registration, login, logout, and profile management.
- Functional shopping cart with order tracking and order history views.

### Changed

- Optimized database connections by migrating to **PostgreSQL** on Railway.
- Improved UI and UX consistency with finalized Design System and Wireframes.

### Fixed

- Resolved security vulnerabilities by managing sensitive data in `.env` files.
- Corrected API endpoint bugs for Edamam integrations.

## [0.3.0]

### Added

- Continuous integration pipelines via **GitHub Actions** for periodic data updates and deployments.
- Full **Docker** support with detailed setup in `DockerSetUp.md`.
- Administrative order management through Django admin interface.

### Changed

- Enhanced payment validation workflows with **Stripe** webhooks.
- Refined custom pizza creation functionality with dynamic ingredient-based pricing.

### Removed

- Deprecated manual deployment scripts replaced by automated workflows.

## [0.2.0]

### Added

- Introduction of the **Cart** app for managing user orders and purchases.
- Secure email handling with **Mailtrap** for development and testing.
- Recipe browsing capabilities with integrated nutrition facts.

### Fixed

- Adjusted deployment configurations for compatibility with **Vercel**.

## [0.1.0]

### Added

- Basic project scaffolding with **Django** framework.
- Initial database setup using **SQLite**, later migrated to **PostgreSQL**.
- Core application setup for static files and template management.
