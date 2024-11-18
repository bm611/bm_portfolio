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
            class_name="min-h-[40vh] md:min-h-[10vh]",
        ),
        size="4",
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
            "index": 3,
            "github_url": "https://github.com/bm611/chat-ui",
            "live_url": "",
        },
    ]

    return rx.container(
        rx.color_mode.button(position="bottom-right"),
        nav.nav_section(),
        rx.box(
            *[project_card.project_card(**project) for project in projects],
            class_name="w-full grid grid-cols-1 md:grid-cols-2 gap-8 max-w-5xl mx-auto mb-20",
        ),
        size="4",
    )


# WORK
@rx.page(route="/work", title="Work")
def work_page() -> rx.Component:
    return rx.container(
        rx.color_mode.button(position="bottom-right"),
        nav.nav_section(),
        rx.center(work.timeline_v1(), class_name=""),
        size="4",
    )


style = {
    "font_family": "Goudy",
}


app = rx.App(
    style=style,
    stylesheets=["/fonts/font.css", "/animate.css"],
)
