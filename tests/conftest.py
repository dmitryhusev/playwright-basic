import pytest
from playwright.sync_api import expect, Page
import os

from tests.logger import LOG


RERUN_COUNT = os.getenv('RERUNS', 1)


class Action:

    def __init__(self, page, expect_object, locator):
        self.page = page
        self.expect = expect_object
        self.locator = locator
    
    def set_expect_timeout(self, timeout):
        self.expect.set_options(timeout)
        return self


@pytest.fixture
def browser(page: Page, request):
    LOG.info('Starting browser')
    if request.node.execution_count == RERUN_COUNT + 1:
        page.context.tracing.start(screenshots=True, snapshots=True, sources=True)


    default_timeout = 15000
    page.set_default_timeout(default_timeout)
    expect.set_options(timeout=default_timeout)
    yield Action(page, expect, page.locator)
    if (request.node.execution_count == 2) and request.node.rep_call.failed == True:
        page.context.tracing.stop(path = f"{request.node.name}.zip")
    page.close()
    LOG.info('Closing browser')

