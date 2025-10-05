# Contributing to pythOwO

Thank you for your interest in contributing! This project welcomes issues and pull requests of all sizes. During Hacktoberfest, documentation, tests, and small fixes are great places to start.

## Getting Started
- Clone and set up:
  - Requires Python 3.8+.
  - Create a virtual environment (recommended).
- Install local dependencies (none required currently). If we add any, they will be listed here.

## Project Structure
- `pythowo.py`: Interpreter implementation.
- `shwell.py`: Interactive shell.
- `exwamples/`: Sample `.pyowo` programs.
- `stwings_with_awwows.py`: String helpers.
- `test/`: Python `unittest` tests.

## Running
- Run a `.pyowo` file:
  ```sh
  python pythowo.py exwamples/hewwo.pyowo
  ```
- Interactive shell:
  ```sh
  python shwell.py
  (｡･ω･｡)ﾉ♡> rwun("exwamples/hewwo.pyowo")
  ```

## Testing
Run all tests using Python's unittest discovery:
```sh
python -m unittest
```

## Coding Guidelines
- Keep changes small and focused.
- Add or update tests in `test/` when you change behavior.
- Favor clear error messages and friendly UX in the shell.
- Match repository style and tone where appropriate.

## Commit Message Convention
- Use imperative mood, present tense. Examples:
  - docs: clarify shell usage and testing
  - fix: improve error message for lowercase IF
  - feat: support arrays in variable assignments

## Pull Request Checklist
- [ ] Title is clear and descriptive.
- [ ] Description explains what, why, and how to test.
- [ ] Updated docs (`README.md` or comments) if behavior changed.
- [ ] Added/updated tests if applicable.
- [ ] CI/tests pass locally: `python -m unittest`.

## Good First Issues
Some ideas if you're new:
- Improve documentation in `README.md`.
- Add more examples under `exwamples/`.
- Enhance error messages for common mistakes.
- Flesh out unit tests under `test/`.

## How to Submit a PR
1. Create a new branch:
   ```sh
   git checkout -b docs/improve-readme-and-contributing
   ```
2. Make changes and run tests:
   ```sh
   python -m unittest
   ```
3. Commit and push:
   ```sh
   git add -A
   git commit -m "docs: improve README and add CONTRIBUTING guide"
   git push -u origin docs/improve-readme-and-contributing
   ```
4. Open a pull request on GitHub.

Happy contribuwuting! uwu
