doc_id: PROD-WEB-015
title: WEB Local Development Setup
doc_type: how-to
scope_level: team
owner_team: WEB
owner_org: PROD
author_role: Tech Lead
status: approved
last_updated: 2026-04-08
supersedes:
fact_ids: 

---

# WEB Local Development Setup

How to get Console running on your laptop.

## Prerequisites

- Node.js 20 (use `nvm`)
- pnpm 9
- Git, and access to the `console` repository in GitHub Enterprise
- Docker, for the mock API server

## Steps

1. Clone the repository:
   ```
   git clone git@github.example.com:techsync/console.git
   ```
2. Install dependencies:
   ```
   pnpm install
   ```
3. Start the mock API server, which serves sample data for every product area:
   ```
   pnpm mocks:start
   ```
4. Start the development server:
   ```
   pnpm dev
   ```
5. Open `http://localhost:3000`. You are signed in as a sample user.

## Useful commands

| Command | What it does |
|---|---|
| `pnpm test` | Unit tests |
| `pnpm lint` | Lint and type checks |
| `pnpm storybook` | Prism component explorer |
| `pnpm e2e` | End-to-end tests against the mock server |

## Troubleshooting

- **Port already in use:** change the port with `PORT=3001 pnpm dev`.
- **Type errors after pulling:** run `pnpm install` again.
- **Mock server cannot start:** make sure Docker Desktop is running.

## Getting help

Ask in #prod-web.
