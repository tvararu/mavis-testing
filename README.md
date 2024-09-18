# Manage vaccinations in schools (Mavis) - End-to-end testing

This repository contains end-to-end tests for Manage vaccinations in schools
(Mavis).

## Getting started

You'll need Python and Poetry installed.

This project uses `asdf`. Use can use the following to install the required
tools:

```bash
bin/asdf
```

## Installing dependencies

```bash
bin/setup
```

## Configure environment variables

```bash
cp .env.example .env
```

Edit the `.env` file to set the username and password for the test environment.

## Running the tests

```bash
bin/test
```

## Running the linters

```bash
bin/lint
```

## Licence

[MIT](LICENCE).
