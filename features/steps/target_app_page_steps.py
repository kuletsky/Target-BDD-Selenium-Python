from behave import given, when, then


@given('Open Target App page')
def open_target_app(context):
    context.app.target_app_page.open_target_app()