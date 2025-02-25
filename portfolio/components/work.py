import reflex as rx


def blip():
    return rx.box(
        width="15px",
        height="15px",
        border="3px solid black",
        background="rgb(50, 150, 255)",
        position="absolute",
        left="-8px",
        transform="rotate(45deg)",
    )


def wrapper(
    title: str, instructions: str, components: list[rx.Component] = [], **kwargs
):
    bg_colors = ["rgb(255, 235, 130)", "rgb(130, 230, 255)", "rgb(255, 130, 200)"]
    # Get a color based on the title's first character
    color_index = ord(title[0]) % len(bg_colors)
    bg_color = bg_colors[color_index]
    
    # Slight rotation for neo-brutalist style
    rotation = "rotate-[1deg]" if ord(title[0]) % 2 == 0 else "rotate-[-1deg]"
    
    return rx.hstack(
        rx.vstack(
            rx.vstack(
                rx.hstack(
                    blip(),
                    rx.text(
                        title, 
                        class_name="text-xl font-bold tracking-wide",
                        color="black",
                    ),
                    align="center",
                ),
                rx.box(
                    rx.text(
                        instructions,
                        class_name="text-2xl tracking-tight font-black uppercase",
                        color="white",
                        style={"letter-spacing": "-0.03em"},
                    ),
                    background="black",
                    padding="0.4em 0.8em",
                    border="3px solid black",
                    transform=rotation,
                ),
                spacing="4",
            ),
            *components,
        ),
        width="100%",
        align="start",
        justify="start",
        padding_left="25px",
        padding_top="20px",
        padding_bottom="20px",
        background=bg_color,
        border="4px solid black",
        box_shadow="8px 8px 0px rgba(0, 0, 0, 0.8)",
        margin_bottom="30px",
        **kwargs,
    )


def timeline_v1():
    return rx.vstack(
        rx.vstack(
            rx.box(
                wrapper(
                    "2023 - Present",
                    "Data Science Engineer",
                    [
                        rx.box(
                            rx.text(
                                "Motivity Labs (Google)",
                                class_name="text-xl md:text-2xl font-black",
                                transform="rotate(-1deg)",
                            ),
                            border_bottom="3px solid black",
                            margin_bottom="1em",
                            padding_bottom="0.5em",
                        ),
                        rx.text(
                            "Orchestrated PDF processing pipelines using Cloud Composer and Document AI for entity extraction, developed PII redaction workflows with spaCy and Google Cloud NLP, and built a self-service chatbot powered by Gemini LLM for automated query generation and insights delivery.",
                            class_name="text-xl md:text-2xl font-medium",
                        ),
                    ],
                ),
                position="relative",
                class_name="animate-fade-in-up delay-1",
            ),
            rx.box(
                wrapper(
                    "2018 - 2023",
                    "Data Scientist",
                    [
                        rx.box(
                            rx.text(
                                "Thermo Fisher Scientific",
                                class_name="text-xl md:text-2xl font-black",
                                transform="rotate(1deg)",
                            ),
                            border_bottom="3px solid black",
                            margin_bottom="1em",
                            padding_bottom="0.5em",
                        ),
                        rx.text(
                            "Developed multiple predictive models including BERT-based parts prediction and service ticket labeling, time series forecasting for service order volume, and propensity to buy models. Created ETL pipelines using PySpark and sparkSQL for data preparation and analysis. Successfully deployed recommendation systems and customer retention models at scale in production using Databricks.",
                            class_name="text-xl md:text-2xl font-medium",
                        ),
                    ],
                ),
                position="relative",
                class_name="animate-fade-in-up delay-2",
            ),
            rx.box(
                wrapper(
                    "2014 - 2016",
                    "Systems Engineer",
                    [
                        rx.box(
                            rx.text(
                                "Tata Consultancy Services",
                                class_name="text-xl md:text-2xl font-black",
                                transform="rotate(-1deg)",
                            ),
                            border_bottom="3px solid black",
                            margin_bottom="1em",
                            padding_bottom="0.5em",
                        ),
                        rx.text(
                            "Managed SCCM application deployments and built ad-hoc reports using SQL Server Reporting Services. Coordinated with IT teams to streamline software distribution processes, automated patch management schedules, and developed custom reporting solutions for asset tracking and compliance monitoring.",
                            class_name="text-xl md:text-2xl font-medium",
                        ),
                    ],
                ),
                position="relative",
                class_name="animate-fade-in-up delay-3",
            ),
            width="100%",
            border_left=f"4px solid black",
            spacing="10",
        ),
        width="100%",
        max_width="40em",
        align="center",
        justify="start",
        padding="24px 12px",
        overflow="auto",
    )
