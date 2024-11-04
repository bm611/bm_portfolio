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
    return rx.container(
        rx.color_mode.button(position="bottom-right"),
        nav.nav_section(),
        rx.box(
            project_card.project_card(
                title="AI Chatbot Assistant",
                description="An intelligent conversational agent built with advanced NLP capabilities for natural language understanding and generation. Features include context awareness, multiple conversation styles, and integration with external APIs.",
                image="https://images.unsplash.com/photo-1624953587687-daf255b6b80a",
                tags=["Python", "NLP", "Transformers", "FastAPI"],
                github_url="https://github.com/username/repo",
                live_url="https://example.com",
            ),
            project_card.project_card(
                title="Code Analysis Tool",
                description="A static code analysis tool that helps developers identify potential bugs, security vulnerabilities, and maintainability issues in their codebase. Supports multiple programming languages and integrates with CI/CD pipelines.",
                image="https://images.unsplash.com/photo-1555066931-4365d14bab8c",
                tags=["Python", "AST", "Docker", "Jenkins"],
                github_url="https://github.com/username/repo",
                live_url="https://example.com",
            ),
            project_card.project_card(
                title="Portfolio Website",
                description="A modern, responsive portfolio website built with Reflex and Python. Features include dark mode support, responsive design, and dynamic content loading. Showcases projects and professional experience.",
                image="https://images.unsplash.com/photo-1498050108023-c5249f4df085",
                tags=["Python", "Reflex", "TailwindCSS", "TypeScript"],
                github_url="https://github.com/username/repo",
                live_url="https://example.com",
            ),
            class_name="w-full flex flex-col gap-8 max-w-2xl mx-auto mb-20",
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
    stylesheets=["/fonts/font.css"],
)
