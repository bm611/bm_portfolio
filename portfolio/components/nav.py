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
                            rx.text(
                                text, 
                                class_name="text-2xl font-bold rotate-[-2deg]",
                                transform="translate(-2px, 0)",
                                color="rgb(255, 50, 50)",
                            ),
                            rx.text(
                                text, 
                                class_name="text-2xl font-bold",
                                _hover={"rotate": "-1deg", "color": "rgb(255, 50, 50)"},
                                transition="all 0.2s ease-in-out",
                            ),
                        ),
                    ),
                    class_name="text-inherit cursor-pointer no-underline hover:text-inherit px-4 py-2 border-[3px] border-black hover:bg-yellow-300 hover:border-black transition-all duration-300",
                    href=href,
                )
                for text, route, href in nav_items
            ],
            class_name="flex justify-around items-center mb-20 mt-10 gap-6 md:gap-16 animate-fade-in-down delay-1",
        ),
    )
