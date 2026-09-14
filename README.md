# Eljur to Obsidian

A Python tool that pulls data (marks, homework, grading periods) from the
[Eljur](https://eljur.ru) school diary API and turns it into Markdown notes
for [Obsidian](https://obsidian.md).

> **Status: work in progress.** Fetching data from the Eljur API and parsing
> it into structured objects is implemented. Generating and writing the
> actual Obsidian Markdown notes is not finished yet (`App.parse` and the
> `Md` class are still stubs).

## What it does today

- Authenticates against the Eljur API with a login/password or a saved auth
  token (`EljurParser.authenticate`).
- Downloads raw API responses for rules, marks, homework and grading periods
  and saves them as JSON under `responses/`.
- Parses those JSON responses into plain Python objects: students, subjects,
  marks, homework (with attached files) and grading periods
  (`ResponseParser`).
- Calculates mark statistics per subject via `MarkList`: the current average,
  how many of a given mark are needed to reach a desired average, and how
  many of a given mark can still be received without changing the current
  rounded average.

## Requirements

- Python 3.10+
- [`requests`](https://pypi.org/project/requests/)
- [`python-dotenv`](https://pypi.org/project/python-dotenv/)

```
pip install requests python-dotenv
```

## Configuration

### `config/config.json`

Describes what to fetch and where to write it. See the checked-in
`config/config.json` for a full example.

- `user.marks` / `user.homeworks` — per-feature settings:
  - `need` — whether this feature is enabled.
  - `path` — where the resulting Obsidian note should be written.
  - `date.start` / `date.end` — date range to fetch, `dd.mm.yyyy`.
  - `template.starts_with` / `template.ends_with` — Markdown files whose
    content is prepended/appended to the generated note (see
    `config/marks/` and `config/homeworks/`).
  - `desired` (marks only) — desired final mark per subject, e.g.
    `"Алгебра": 5`.
- `program.env` — path to the secrets file (see below).
- `program.responses` — where raw Eljur API responses are cached as JSON
  (`assessments`, `diary`, `homeworks`, `marks`, `periods`, `rules`,
  `schedule`).

### Secrets (`config/.env`)

Eljur credentials are kept out of `config.json` in a `.env` file (path set by
`program.env`, ignored by git):

```
ELJUR_LOGIN = your-login
ELJUR_PASSWORD = your-password
ELJUR_SCHOOL_CLASS = your-class
ELJUR_VENDOR = your-school-vendor-name
ELJUR_DEVKEY = your-devkey
ELJUR_AUTH_TOKEN = 
```

`ELJUR_VENDOR` is your school's subdomain on `eljur.ru`. `ELJUR_AUTH_TOKEN`
can be left empty; once you authenticate with a login/password, the token
returned by Eljur can be stored here to skip re-authenticating.

## Project layout

- `src/config/` — loads/writes `config.json` and the `.env` secrets into
  typed dataclasses.
- `src/eljur/` — the Eljur API client (`EljurParser`) and the response
  parser/domain objects (`ResponseParser`, `Subject`, `Homework`, `MarkList`,
  `Period`, `Student`).
- `src/md/` — Obsidian Markdown generation (currently a stub).
- `src/utils/date.py` — date conversion helpers between Eljur's `yyyymmdd`
  format and `dd.mm.yyyy`.
