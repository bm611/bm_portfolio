import reflex as rx
from .components import nav
from .components import hero
from .components import project_card
from .components import work


# HOME
@rx.page(route="/", title="Portfolio")
def index() -> rx.Component:
    return rx.container(
        rx.color_mode.button(position="bottom-right"),
        nav.nav_section(),
        rx.center(
            hero.hero_section(),
            class_name="min-h-[30vh] md:min-h-[40vh]",
        ),
        size="4",
        max_width="100%",
        padding="0",
    )


# PROJECTS
@rx.page(route="/projects", title="Projects")
def project() -> rx.Component:
    projects = [
        {
            "title": "Cerebro - AI Quiz Generator",
            "description": "An AI-powered quiz generator that dynamically creates customized quizzes on any topic or subject area. Built using Google's Gemini API to analyze content and generate relevant questions.",
            "image": "/cerebro.jpg",
            "tags": ["Python", "Gemini", "TailwindCSS", "Reflex"],
            "index": 1,
            "github_url": "https://github.com/bm611/cerebro",
            "live_url": "https://cerebro.reflex.run",
        },
        {
            "title": "Byte-Bites - AI Recipe Generator",
            "description": "An AI-powered recipe generator that creates unique recipes based on user preferences and available ingredients. Features intelligent ingredient substitution and dynamic recipe scaling.",
            "image": "/recipe.jpg",
            "tags": ["Python", "Gemini", "Flux", "TailwindCSS", "Reflex"],
            "index": 2,
            "github_url": "https://github.com/bm611/byte-bites",
            "live_url": "https://recipe.reflex.run",
        },
        {
            "title": "Web Search",
            "description": "An advanced web search application integrating Brave Search API for real-time data retrieval and Gemini AI for enhanced result analysis and summarization. Features include comprehensive search results, AI-powered content interpretation, and efficient data processing.",
            "image": "/search.jpg",
            "tags": ["Python", "Gemini", "Brave", "Reflex"],
            "index": 3,
            "github_url": "https://github.com/bm611/aisearch",
            "live_url": "https://aisearch.reflex.com",
        },
        {
            "title": "Chat-UI",
            "description": "A modern chat interface built with Reflex that allows you to interact with various AI models through different providers or run completely locally using open-source models.",
            "image": "/chat.jpg",
            "tags": ["Python", "Reflex", "TailwindCSS", "Ollama", "OpenAI"],
            "index": 4,
            "github_url": "https://github.com/bm611/chat-ui",
            "live_url": "",
        },
    ]

    return rx.container(
        rx.color_mode.button(position="bottom-right"),
        nav.nav_section(),
        rx.vstack(
            rx.box(
                rx.grid(
                    *[project_card.project_card(**project) for project in projects],
                    class_name="w-full gap-6 md:gap-8",
                    template_columns="repeat(1, 1fr)",
                    sm_template_columns="repeat(1, 1fr)",
                    md_template_columns="repeat(2, 1fr)",
                    lg_template_columns="repeat(2, 1fr)",
                    spacing="6",
                ),
                class_name="w-full px-4 sm:px-6 md:px-8 max-w-7xl mx-auto",
            ),
            width="100%",
            spacing="8",
            padding_top="2em",
            padding_bottom="4em",
            class_name="min-h-screen",
        ),
        max_width="100%",
        padding="0",
        class_name="",
    )


# WORK
@rx.page(route="/work", title="Work")
def work_page() -> rx.Component:
    return rx.container(
        rx.color_mode.button(position="bottom-right"),
        nav.nav_section(),
        rx.center(
            work.timeline_v1(),
            class_name="w-full px-0 sm:px-2 md:px-4",
            width="100%",
        ),
        size="4",
        class_name="px-0",
        max_width="100%",
    )


style = {
    "font_family": "Goudy",
    "background_color": "rgb(255, 255, 240)",
    "color": "#000",
}

# Let's add our neo-brutalist style directly to the style object
style.update(
    {
        "accent_color": "rgb(255, 50, 50)",
        "border_radius": "0px",
    }
)

app = rx.App(
    style=style,
    stylesheets=["/fonts/font.css", "/animate.css"],
)
