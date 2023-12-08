from shiny import App, ui

app_ui = ui.page_fluid('Hello world!')

def server(input, output, session):
    pass

app = App(app_ui, server)