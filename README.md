# Core Platform

## Overview

The Core Platform is a scalable and modular backend solution designed for high-performance AI-driven applications, seamlessly integrated with blockchain and user management capabilities. Built by Squares AI, this platform serves as the backbone for decentralized, AI-enabled systems.

## Features

- Robust API for managing AI models and workflows.
- Secure and efficient blockchain-based transactions.
- Complex user authentication and authorization.

## Quick Start

### Prerequisites

- Docker
- Docker Compose

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/squares-ai/core-platform.git
   cd core-platform
   ```

2. Build and start the services:
   ```bash
   docker-compose up --build
   ```

3. Access the application at `http://localhost:8000`.

### Running Tests

Execute the following command to run the test suite:
```bash
docker-compose run core-platform pytest
```

## Architecture

The Core Platform follows a modular architecture:

- **src/app**: Main application code with routers, services, models, and schemas.
- **migrations**: Database schema management via Alembic.
- **docs**: Detailed documentation for APIs and architecture.

## Contributing

We welcome contributions! Please follow the guidelines in `CONTRIBUTING.md`.

## License

This project is licensed under the MIT License. See `LICENSE` for details.
