import reflex as rx


def timeline_dot():
    return rx.box(
        width="16px",
        height="16px",
        border_radius="50%",
        background="#3B82F6",  # More neutral blue
        border="3px solid #1E293B",  # Darker border
        position="absolute",
        left="0px",
        z_index="2",
    )


def skill_tag(skill: str):
    return rx.box(
        rx.text(
            skill,
            font_weight="bold",
            color="#1E293B",  # Dark slate
        ),
        padding="4px 10px",
        border_radius="4px",
        background="rgba(255, 255, 255, 0.7)",
        border="2px solid #334155",  # Slate
        margin_right="8px",
        margin_bottom="8px",
        transition="all 0.2s ease",
        _hover={
            "transform": "translateY(-2px)",
            "box_shadow": "2px 2px 0px rgba(30, 41, 59, 0.5)",
        },
    )


def work_card(
    period: str,
    title: str,
    company: str,
    description: str,
    skills: list[str] = [],
    delay: str = "delay-1",
):
    # Neutral colors
    bg_colors = ["#F1F5F9", "#E2E8F0", "#F8FAFC"]  # Light slate colors
    # Get a color based on the title's first character
    color_index = ord(title[0]) % len(bg_colors)
    bg_color = bg_colors[color_index]

    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.text(
                    period,
                    class_name="text-lg font-bold tracking-wide",
                    color="#1E293B",  # Dark slate
                    background="white",
                    padding="4px 10px",
                    border="2px solid #334155",  # Slate
                    border_radius="4px",
                ),
                rx.spacer(),
                width="100%",
                margin_bottom="12px",
            ),
            rx.vstack(
                rx.text(
                    title,
                    class_name="text-2xl tracking-tight font-black uppercase",
                    color="white",
                    style={"letter-spacing": "-0.03em"},
                    background="#1E293B",  # Dark slate
                    padding="0.4em 0.8em",
                    border="3px solid #0F172A",  # Darker slate
                    transform="rotate(-1deg)",
                    margin_bottom="16px",
                    align_self="flex-start",
                ),
                rx.box(
                    rx.text(
                        company,
                        class_name="text-xl md:text-2xl font-black",
                        transform="rotate(1deg)",
                        color="#1E293B",  # Dark slate
                    ),
                    border_bottom="3px solid #334155",  # Slate
                    margin_bottom="1em",
                    padding_bottom="0.5em",
                    width="100%",
                ),
                rx.text(
                    description,
                    class_name="text-lg md:text-xl font-medium",
                    margin_bottom="16px",
                    color="#334155",  # Slate
                ),
                rx.flex(
                    *[skill_tag(skill) for skill in skills],
                    spacing="2",
                    width="100%",
                    wrap="wrap",
                ),
                width="100%",
                align_items="flex-start",
            ),
            width="100%",
            align_items="flex-start",
            padding="24px",
        ),
        position="relative",
        width="100%",
        background=bg_color,
        border="3px solid #334155",  # Slate
        box_shadow="6px 6px 0px rgba(30, 41, 59, 0.3)",
        margin_bottom="30px",
        transition="all 0.3s ease",
        _hover={
            "transform": "translateY(-5px)",
            "box_shadow": "8px 8px 0px rgba(30, 41, 59, 0.4)",
        },
        class_name=f"animate-fade-in-up {delay}",
    )


def timeline_v1():
    return rx.vstack(
        rx.vstack(
            rx.box(
                timeline_dot(),
                work_card(
                    "2023 - Present",
                    "Data Science Engineer",
                    "Motivity Labs (Google)",
                    "Orchestrated PDF processing pipelines using Cloud Composer and Document AI for entity extraction, developed PII redaction workflows with spaCy and Google Cloud NLP, and built a self-service chatbot powered by Gemini LLM for automated query generation and insights delivery.",
                    ["Python", "GCP", "Gemini", "Document AI", "Cloud Composer", "NLP"],
                    "delay-1",
                ),
                position="relative",
                width="100%",
            ),
            rx.box(
                timeline_dot(),
                work_card(
                    "2018 - 2023",
                    "Data Scientist",
                    "Thermo Fisher Scientific",
                    "Developed multiple predictive models including BERT-based parts prediction and service ticket labeling, time series forecasting for service order volume, and propensity to buy models. Created ETL pipelines using PySpark and sparkSQL for data preparation and analysis. Successfully deployed recommendation systems and customer retention models at scale in production using Databricks.",
                    [
                        "Python",
                        "BERT",
                        "PySpark",
                        "SQL",
                        "Databricks",
                        "Time Series",
                        "ML",
                    ],
                    "delay-2",
                ),
                position="relative",
                width="100%",
            ),
            rx.box(
                timeline_dot(),
                work_card(
                    "2014 - 2016",
                    "Systems Engineer",
                    "Tata Consultancy Services",
                    "Managed SCCM application deployments and built ad-hoc reports using SQL Server Reporting Services. Coordinated with IT teams to streamline software distribution processes, automated patch management schedules, and developed custom reporting solutions for asset tracking and compliance monitoring.",
                    ["SQL", "SCCM", "Reporting Services", "IT Management"],
                    "delay-3",
                ),
                position="relative",
                width="100%",
            ),
            width="100%",
            spacing="10",
            position="relative",
            padding_left=["10px", "15px", "20px"],
        ),
        width="100%",
        max_width=["100%", "90%", "50em"],
        align="center",
        justify="center",
        padding=["16px 8px", "20px 10px", "24px 12px"],
        margin="0 auto",
        class_name="px-4 sm:px-6 md:px-8",
        overflow="auto",
    )
