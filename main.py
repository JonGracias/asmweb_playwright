import importlib
from playwright.sync_api import sync_playwright

# Define the list of tests with URLs and their unique identifiers
tests_to_run = [
    {"module": "it_tracks", "url": "https://jonnov2024.wpenginepowered.com/it-tracks/"}
]

def run_test():
    results = {}

    with sync_playwright() as p:
        browser = p.chromium.launch()

        for test in tests_to_run:
            module_name = test["module"]
            site_url = test["url"]
            try:
                # Import the test module dynamically based on the site name
                test_module = importlib.import_module(f"tests.{module_name}")
                page = browser.new_page()
                page.goto(site_url)

                # Run the test function and capture the result
                result = test_module.run(page)
                if result["pass"] == True:
                    results[module_name] = {"pass": "Test passed successfully"}
                else:
                    results[module_name] = {"fail": result["error_message"]}

                page.close()

            except Exception as e:
                # Capture any errors that occur and log them as failures
                results[module_name] = {"fail": str(e)}

        browser.close()
    
    return results
