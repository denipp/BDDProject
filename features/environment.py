from behave import use_fixture
from fixtures import browser_chrome
from web_source.web_factory import get_web


def before_all(context):
    web = get_web(context.config.userdata['browser'])
    context.web = web

def before_tag(context, tag):
    if tag == "fixture.browser.chrome":
        use_fixture(browser_chrome, context)