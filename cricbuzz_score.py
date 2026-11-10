
import re
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError

# Cricbuzz live scores website
URL = "https://www.cricbuzz.com/cricket-match/live-scores"

# Change to True after testing in headed mode
HEADLESS = False

# Cricket score pattern, e.g. 287-4 or 287/4 (45.2 Ov)
SCORE_PATTERN = r"\b\d{1,3}\s*[-/]\s*\d{1,2}\b"


def get_cricket_scores(page):

    # Find visible elements containing score-like text
    return page.evaluate("""
        (pattern) => {
            const regex = new RegExp(pattern);
            const elements = Array.from(
                document.querySelectorAll("body *")
            );

            const results = [];

            for (const element of elements) {
                const text = (element.innerText || "").trim();

                if (
                    text &&
                    text.length < 150 &&
                    regex.test(text)
                ) {
                    // Keep the smallest matching text elements
                    const childMatches = Array.from(element.children)
                        .some(child =>
                            regex.test((child.innerText || "").trim())
                        );

                    if (!childMatches) {
                        results.push(text);
                    }
                }
            }

            return [...new Set(results)];
        }
    """, SCORE_PATTERN)


def main():

    with sync_playwright() as p:

        # Launch Chromium browser
        browser = p.chromium.launch(headless=HEADLESS)

        page = browser.new_page(
            viewport={"width": 1366, "height": 768}
        )

        print("Opening Cricbuzz...")

        try:
            page.goto(
                URL,
                wait_until="domcontentloaded",
                timeout=60000
            )

            # Wait for score content instead of fixed sleep
            page.wait_for_function(
                """
                pattern => {
                    const regex = new RegExp(pattern);
                    return Array.from(
                        document.querySelectorAll("body *")
                    ).some(element => {
                        const text = (element.innerText || "").trim();
                        return text.length < 150 && regex.test(text);
                    });
                }
                """,
                arg=SCORE_PATTERN,
                timeout=20000
            )

            scores = get_cricket_scores(page)

            if scores:
                print("\nCricket scores found:\n")

                for score in scores:
                    print(score)

            else:
                print("No cricket scores found.")

        except PlaywrightTimeoutError:
            print("No score appeared within the waiting time.")
            print("There may be no available match score.")

        except Exception as error:
            print("An error occurred:", error)

        finally:
            # Save screenshot
            page.screenshot(
                path="score.png",
                full_page=True
            )

            print("\nScreenshot saved as score.png")

            browser.close()


if __name__ == "__main__":
    main()
