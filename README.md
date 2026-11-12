# GenAI-Program

A collection of small Python programs and experiments, including a student grade manager and browser automation examples.

## Programs

- **`grade_manager.py`** — interactive command-line grade manager. Add students with marks from 0–100, assign grades, and view average, highest, and lowest marks.
- **`cricbuzz_score.py`** — uses Playwright to open Cricbuzz's live-scores page and print text matching common cricket score formats. It saves a page screenshot as `score.png`.
- **`playwright_basic.py`** — a minimal Playwright example that opens `example.com` in Chromium and prints the page title.
- **`pyautogui.py`** — a short PyAutoGUI configuration example that enables the failsafe and sets a one-second pause.

## Requirements

- Python 3.8 or newer
- Playwright for the browser examples
- PyAutoGUI only if you are using `pyautogui.py`

Install the optional packages with:

```bash
python -m pip install playwright pyautogui
```

Install Playwright's Chromium browser for the Playwright examples:

```bash
python -m playwright install chromium
```

## Run

From the repository directory, run the program you want:

```bash
python grade_manager.py
python cricbuzz_score.py
python playwright_basic.py
```

`grade_manager.py` uses only the Python standard library. The browser scripts require an internet connection and an installed Playwright browser. The Cricbuzz page's content and layout can change, so score extraction may not always find results. The script runs with a visible browser by default.

## Notes

- `score.png` is also present in the repository; running `cricbuzz_score.py` writes a screenshot to that filename in the current directory.
- `pyautogui.py` only configures PyAutoGUI; it does not perform an automation task by itself. PyAutoGUI can control the desktop, so use it only in an environment where you understand and intend its actions.

## License

No license has been specified for this repository. Contact the repository owner before reusing or distributing its contents.
