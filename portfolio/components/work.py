import reflex as rx


def blip():
    return rx.box(
        width="10px",
        height="10px",
        border_radius="10px",
        background=rx.color("blue"),
        position="absolute",
        left="-5px",
    )


def wrapper(
    title: str, instructions: str, components: list[rx.Component] = [], **kwargs
):
    return rx.hstack(
        rx.vstack(
            rx.vstack(
                rx.hstack(
                    blip(),
                    rx.text(title, class_name="text-xl tracking-wide"),
                    align="center",
                ),
                rx.text(
                    instructions,
                    class_name="text-3xl tracking-wide font-bold",
                ),
                spacing="1",
            ),
            *components,
        ),
        width="100%",
        align="start",
        justify="start",
        padding_left="15px",
        border_radius="0px 5px 5px 0px",
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
                        rx.text(
                            "Motivity Labs (Google)",
                            class_name="text-xl md:text-2xl font-semibold text-slate-400",
                        ),
                        rx.text(
                            "Orchestrated PDF processing pipelines using Cloud Composer and Document AI for entity extraction, developed PII redaction workflows with spaCy and Google Cloud NLP, and built a self-service chatbot powered by Gemini LLM for automated query generation and insights delivery.",
                            class_name="text-xl md:text-2xl",
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
                        rx.text(
                            "Thermo Fisher Scientific",
                            class_name="text-xl md:text-2xl font-semibold text-slate-400",
                        ),
                        rx.text(
                            "Developed multiple predictive models including BERT-based parts prediction and service ticket labeling, time series forecasting for service order volume, and propensity to buy models. Created ETL pipelines using PySpark and sparkSQL for data preparation and analysis. Successfully deployed recommendation systems and customer retention models at scale in production using Databricks.",
                            class_name="text-xl md:text-2xl",
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
                        rx.text(
                            "Tata Consultancy Services",
                            class_name="text-xl md:text-2xl font-semibold text-slate-400",
                        ),
                        rx.text(
                            "Managed SCCM application deployments and built ad-hoc reports using SQL Server Reporting Services. Coordinated with IT teams to streamline software distribution processes, automated patch management schedules, and developed custom reporting solutions for asset tracking and compliance monitoring.",
                            class_name="text-xl md:text-2xl",
                        ),
                    ],
                ),
                position="relative",
                class_name="animate-fade-in-up delay-3",
            ),
            width="100%",
            border_left=f"1px solid {rx.color('gray', 5)}",
            spacing="7",
        ),
        width="100%",
        max_width="40em",
        align="center",
        justify="start",
        padding="24px 12px",
        overflow="auto",
    )
