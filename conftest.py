import pytest
import base64

@pytest.hookimpl(wrapper=True)
def pytest_runtest_makereport(item, call):
    # 1. Let the test execution phase finish (Teardown step)
    report = yield
    
    # 2. Check when the main test logic completes ("call" phase)
    if report.when == "call":
        # 3. Retrieve the active Playwright page object from the test arguments
        page = item.funcargs.get("page")
        if page:
            # 4. Capture browser screenshot as binary data
            screenshot_bytes = page.screenshot(type="png")
            # 5. Convert binary data into clean Base64 text string for HTML embedding
            screenshot_base64 = base64.b64encode(screenshot_bytes).decode("utf-8")
            
            # 6. Construct the HTML image tag container
            html = f'<div><p><b>Execution Screenshot:</b></p><img src="data:image/png;base64,{screenshot_base64}" style="width:600px;height:auto;" class="screenshot"></div>'
            
            # 7. Safe check and inject the visual markup into the PyTest HTML metadata
            extra = getattr(report, "extra", [])
            pytest_html = item.config.pluginmanager.getplugin("pytest_html")
            if pytest_html:
                extra.append(pytest_html.extras.html(html))
                report.extra = extra
                
    return report
