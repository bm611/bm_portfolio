import reflex as rx


def nav_section() -> rx.Component:
    return rx.center(
        rx.hstack(
            rx.link(
                rx.text("Home", class_name="text-2xl"),
                class_name="text-inherit cursor-pointer no-underline hover:text-inherit",
                href="/",
            ),
            rx.link(
                rx.text("Projects", class_name="text-2xl"),
                class_name="text-inherit cursor-pointer no-underline hover:text-inherit",
                href="/projects",
            ),
            rx.link(
                rx.text("Work", class_name="text-2xl"),
                class_name="text-inherit cursor-pointer no-underline hover:text-inherit",
                href="/work",
            ),
            class_name="flex justify-around items-center mb-20 mt-10 gap-12 md:gap-32",
        ),
    )
