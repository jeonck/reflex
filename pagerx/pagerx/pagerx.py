"""Welcome to Reflex! This file outlines the steps to create a basic app."""

from chatrx.rxconfig import config

import reflex as rx

docs_url = "https://reflex.dev/docs/getting-started/introduction/"
filename = f"{config.app_name}/{config.app_name}.py"


class State(rx.State):
    """The app state."""


def index() -> rx.Component:
    return rx.center(
        rx.theme_panel(),
        rx.vstack(
            rx.heading("Welcome to Reflex!", size="9"),
            rx.text("Get started by editing ", rx.code(filename)),
            rx.button(
                "Check out our docs!",
                on_click=lambda: rx.redirect(docs_url),
                size="4",
            ),
            rx.logo(),
            align="center",
            spacing="7",
            font_size="2em",
        ),
        height="100vh",
    )

def about() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading("About Us", size="9"),
            rx.text("Learn more about what we do."),
            rx.button("Back to Home", on_click=lambda: rx.redirect("/"), size="4"),
            align="center",
            spacing="7",
            font_size="2em"
        ),
        height="100vh"
    )

app = rx.App()
app.add_page(index)
app.add_page(about)
