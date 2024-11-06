import reflex as rx


def hero_section():
    return (
        rx.vstack(
            rx.heading(
                "Hi, I'm Bharath",
                class_name="text-5xl tracking-wide md:text-8xl animate-fade-in-up",
            ),
            rx.text(
                "I love building open-source applications.",
                class_name="text-2xl md:text-4xl leading-none animate-fade-in-up delay-1",
            ),
            rx.text(
                "Data Science Engineer",
                class_name="text-2xl md:text-4xl mt-4 animate-fade-in-up delay-2 font-bold bg-gradient-to-r from-purple-500 to-pink-500 bg-clip-text text-transparent hover:from-blue-500 hover:to-teal-500 transition-all duration-500 tracking-wide",
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
                class_name="mt-4 flex gap-4 animate-fade-in-up delay-3",
            ),
            class_name="px-8 md:px-20",
        ),
    )
