import reflex as rx
from portfolio.state import State


def nav_section() -> rx.Component:
    nav_items = [
        ("Home", "", "/"),
        ("Projects", "projects", "/projects"),
        ("Work", "work", "/work"),
    ]

    return rx.center(
        rx.hstack(
            *[
                rx.link(
                    rx.box(
                        rx.cond(
                            State.get_page == route,
                            rx.text(text, class_name="text-2xl border-b-2"),
                            rx.text(text, class_name="text-2xl"),
                        ),
                    ),
                    class_name="text-inherit cursor-pointer no-underline hover:text-inherit",
                    href=href,
                )
                for text, route, href in nav_items
            ],
            class_name="flex justify-around items-center mb-20 mt-10 gap-12 md:gap-32",
        ),
    )
