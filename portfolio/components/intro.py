import reflex as rx


def intro_section():
    return rx.box(
        rx.vstack(
            rx.heading(
                "About Me",
                font_size=["xl", "2xl", "3xl"],
                font_weight="black",
                padding="0.4em 0.8em",
                border="3px solid #334155",
                background="white",
                transform="rotate(-1deg)",
                box_shadow="5px 5px 0px rgba(30, 41, 59, 0.3)",
                class_name="animate-fade-in-up self-center mb-4 sm:mb-6",
                color="#1E293B",
            ),
            rx.text(
                "I'm a Data Science Engineer with expertise in machine learning, NLP, and cloud technologies. "
                "I specialize in building intelligent systems that solve real-world problems.",
                class_name="text-lg text-center animate-fade-in-up delay-1 mb-4",
            ),
            rx.hstack(
                rx.vstack(
                    rx.heading(
                        "Skills",
                        font_size=["md", "lg", "xl"],
                        font_weight="bold",
                        class_name="mb-2",
                    ),
                    rx.hstack(
                        *[
                            rx.box(
                                rx.text(
                                    skill,
                                    font_weight="bold",
                                    color="#1E293B",
                                ),
                                padding="4px 10px",
                                border_radius="4px",
                                background="rgba(255, 255, 255, 0.7)",
                                border="2px solid #334155",
                                margin="4px",
                                transition="all 0.2s ease",
                                _hover={
                                    "transform": "translateY(-2px)",
                                    "box_shadow": "2px 2px 0px rgba(30, 41, 59, 0.5)",
                                },
                            )
                            for skill in [
                                "Python",
                                "ML",
                                "NLP",
                                "GCP",
                                "PySpark",
                                "Reflex",
                            ]
                        ],
                        class_name="flex flex-wrap justify-center",
                    ),
                    class_name="animate-fade-in-up delay-2 text-center",
                    width="100%",
                ),
                rx.vstack(
                    rx.heading(
                        "Interests",
                        font_size=["md", "lg", "xl"],
                        font_weight="bold",
                        class_name="mb-2",
                    ),
                    rx.hstack(
                        *[
                            rx.box(
                                rx.text(
                                    interest,
                                    font_weight="bold",
                                    color="#1E293B",
                                ),
                                padding="4px 10px",
                                border_radius="4px",
                                background="rgba(255, 255, 255, 0.7)",
                                border="2px solid #334155",
                                margin="4px",
                                transition="all 0.2s ease",
                                _hover={
                                    "transform": "translateY(-2px)",
                                    "box_shadow": "2px 2px 0px rgba(30, 41, 59, 0.5)",
                                },
                            )
                            for interest in [
                                "AI",
                                "Web Dev",
                                "Open Source",
                                "LLMs",
                                "Data Viz",
                            ]
                        ],
                        class_name="flex flex-wrap justify-center",
                    ),
                    class_name="animate-fade-in-up delay-3 text-center",
                    width="100%",
                ),
                class_name="flex-col sm:flex-row gap-6 sm:gap-10 w-full justify-center",
            ),
            rx.hstack(
                rx.link(
                    rx.button(
                        "View Projects",
                        class_name="bg-[#334155] text-white hover:bg-[#1E293B] px-4 py-2 rounded-none border-2 border-black",
                    ),
                    href="/projects",
                ),
                rx.link(
                    rx.button(
                        "Work Experience",
                        class_name="bg-white text-[#1E293B] hover:bg-gray-100 px-4 py-2 rounded-none border-2 border-black",
                    ),
                    href="/work",
                ),
                class_name="mt-6 sm:mt-8 gap-4 animate-fade-in-up delay-4 flex-wrap justify-center",
            ),
            class_name="w-full max-w-3xl mx-auto px-4 sm:px-6 py-6 sm:py-8",
            spacing="4",
        ),
        class_name="w-full bg-[#F8FAFC] py-6 sm:py-10 border-y-2 border-[#E2E8F0]",
    )
