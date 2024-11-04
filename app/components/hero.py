import reflex as rx


def hero_section():
    return (
        rx.vstack(
            rx.heading(
                "Hi, I'm Bharath", class_name="text-5xl tracking-wide md:text-7xl"
            ),
            rx.text(
                "I love building full stack AI/ML applications.",
                class_name="text-2xl leading-none",
            ),
            rx.vstack(
                rx.box(
                    rx.text(
                        "Data Science Engineer",
                        class_name="text-xl",
                    ),
                    class_name="border-2 rounded-md p-1 md:px-2",
                ),
                rx.box(
                    rx.text(
                        "Full Stack Developer",
                        class_name="text-xl",
                    ),
                    class_name="border-2 rounded-md p-1 md:px-2",
                ),
                class_name="md:flex-row md:gap-4 mt-4",
            ),
            rx.hstack(
                rx.link(
                    rx.icon("github", class_name="cursor-pointer "),
                    href="https://github.com/bm611/",
                    class_name="text-inherit",
                ),
                rx.link(
                    rx.icon("linkedin", class_name="cursor-pointer "),
                    href="https://www.linkedin.com/in/bharath-mohan/",
                    class_name="text-inherit",
                ),
                rx.link(
                    rx.icon("mail", class_name="cursor-pointer "),
                    href="mailto:bharath.moha.pro@gmail.com",
                    class_name="text-inherit",
                    is_external=True,
                ),
                class_name="mt-4 flex gap-4",
            ),
            class_name="px-8 md:px-20",
        ),
    )
