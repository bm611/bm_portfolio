import reflex as rx


def hero_section():
    return (
        rx.vstack(
            rx.heading(
                "Hi, I'm Bharath",
                class_name="text-4xl sm:text-5xl md:text-8xl animate-fade-in-up font-black tracking-tight transform rotate-[-1deg] text-shadow-[4px_4px_0px_rgba(0,0,0,0.2)]",
            ),
            rx.text(
                "I love building open-source applications.",
                class_name="text-xl sm:text-2xl md:text-4xl leading-none animate-fade-in-up delay-1 font-medium transform rotate-[1deg]",
                border="3px solid black",
                padding="0.4em 0.8em",
                background_color="rgb(255, 220, 100)",
                box_shadow="5px 5px 0px black",
                margin_top="0.8em",
            ),
            rx.box(
                rx.text(
                    "Data Science Engineer",
                    class_name="text-xl sm:text-2xl md:text-4xl font-black animate-fade-in-up delay-2 tracking-tight",
                    color="white",
                ),
                background="black",
                padding="0.3em 0.8em",
                margin_top="0.8em",
                transform="rotate(2deg)",
                border="3px solid black",
            ),
            rx.hstack(
                rx.link(
                    rx.icon(
                        "github",
                        class_name="cursor-pointer",
                        size=28,
                    ),
                    href="https://github.com/bm611/",
                    class_name="text-inherit p-2 border-2 border-black bg-[rgb(255,100,100)] hover:bg-[rgb(100,255,100)] transition-all duration-300",
                ),
                rx.link(
                    rx.icon(
                        "linkedin",
                        class_name="cursor-pointer",
                        size=28,
                    ),
                    href="https://www.linkedin.com/in/bharath-mohan/",
                    class_name="text-inherit p-2 border-2 border-black bg-[rgb(100,100,255)] hover:bg-[rgb(255,100,255)] transition-all duration-300",
                ),
                rx.link(
                    rx.icon(
                        "mail",
                        class_name="cursor-pointer",
                        size=28,
                    ),
                    href="mailto:bharath.moha.pro@gmail.com",
                    class_name="text-inherit p-2 border-2 border-black bg-[rgb(100,255,255)] hover:bg-[rgb(255,255,100)] transition-all duration-300",
                    is_external=True,
                ),
                class_name="mt-4 sm:mt-6 flex gap-3 sm:gap-4 animate-fade-in-up delay-3",
            ),
            class_name="px-4 sm:px-8 md:px-20 py-4 sm:py-6 md:py-8",
            spacing="0",
            align="center",
        ),
    )
