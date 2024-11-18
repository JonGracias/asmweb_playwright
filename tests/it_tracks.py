from playwright.sync_api import Page

def run(page: Page):
    try:
        # Locate and test the accordion functionality
        accordion_buttons = page.query_selector_all("button.accordion")
        for button in accordion_buttons:
            # Click to open accordion
            button.click()
            # need to check not for sibling but next div
            is_open = "is-open" in button.get_attribute("class")
            #content_div = button.evaluate_handle("button => button.nextElementSibling")
            #has_max_height = content_div.get_attribute("style") == "max-height: 43px;"

            # If any button fails the check, return a failure message
            if not (is_open):
               return {"pass": False, "error_message": "Accordion did not open correctly"}

            # Click again to close (optional reset for testing)
            #button.click()

        # All checks passed
        return {"pass": True}

    except Exception as e:
        # Return an error message if any exception occurs
        return {"pass": False, "error_message": str(e)}
