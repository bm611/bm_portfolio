import reflex as rx


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


def project_card(
    title: str,
    description: str,
    image: str,
    tags: list[str],
    index: int,
    github_url: str | None = None,
    live_url: str | None = None,
) -> rx.Component:
    # Determine animation class based on index
    animation_class = (
        "animate-fade-in-up" if index % 2 == 0 else "animate-fade-in-up"
    )
    delay_class = f"delay-{min(index + 1, 4)}"  # Limit delay classes to 4
    
    # Neutral background colors
    bg_colors = ["#F1F5F9", "#E2E8F0", "#F8FAFC", "#EFF6FF"]
    bg_color = bg_colors[index % len(bg_colors)]
    
    return rx.box(
        rx.vstack(
            # Image container with larger size
            rx.box(
                rx.image(
                    src=image,
                    alt=title,
                    class_name="w-full h-full object-cover transition-all duration-500 hover:scale-105",
                ),
                class_name="relative w-full h-64 md:h-72 lg:h-80 overflow-hidden rounded-t-lg",
                border_bottom="3px solid #334155",
            ),
            
            # Content container
            rx.vstack(
                # Title
                rx.heading(
                    title,
                    class_name="text-xl md:text-2xl font-black tracking-tight uppercase",
                    color="#1E293B",
                    style={"letter-spacing": "-0.03em"},
                    margin_bottom="0.75rem",
                    align_self="flex-start",
                ),
                
                # Description
                rx.text(
                    description,
                    class_name="text-base md:text-lg font-medium",
                    color="#334155",
                    margin_bottom="1rem",
                ),
                
                # Tags
                rx.box(
                    rx.flex(
                        *[skill_tag(tag) for tag in tags],
                        wrap="wrap",
                        width="100%",
                        margin_bottom="1.25rem",
                    ),
                    width="100%",
                ),
                
                # Buttons
                rx.hstack(
                    rx.cond(
                        github_url is not None,
                        rx.link(
                            rx.hstack(
                                rx.icon("github", class_name="cursor-pointer", size=20),
                                rx.text(
                                    "CODE", 
                                    class_name="text-sm md:text-base font-bold",
                                    color="#1E293B",
                                ),
                                spacing="1",
                                align_items="center",
                            ),
                            href=github_url,
                            is_external=True,
                            padding="4px 10px",
                            border_radius="4px",
                            background="rgba(255, 255, 255, 0.7)",
                            border="2px solid #334155",
                            transition="all 0.2s ease",
                            _hover={
                                "transform": "translateY(-2px)",
                                "box_shadow": "2px 2px 0px rgba(30, 41, 59, 0.5)",
                            },
                        ),
                    ),
                    rx.cond(
                        live_url is not None and live_url != "",
                        rx.link(
                            rx.hstack(
                                rx.icon(
                                    "external-link", class_name="cursor-pointer", size=20
                                ),
                                rx.text(
                                    "DEMO", 
                                    class_name="text-sm md:text-base font-bold",
                                    color="#1E293B",
                                ),
                                spacing="1",
                                align_items="center",
                            ),
                            href=live_url,
                            is_external=True,
                            padding="4px 10px",
                            border_radius="4px",
                            background="rgba(255, 255, 255, 0.7)",
                            border="2px solid #334155",
                            transition="all 0.2s ease",
                            _hover={
                                "transform": "translateY(-2px)",
                                "box_shadow": "2px 2px 0px rgba(30, 41, 59, 0.5)",
                            },
                        ),
                    ),
                    spacing="4",
                    align_self="flex-start",
                ),
                
                width="100%",
                align_items="flex-start",
                padding="1.25rem",
                background=bg_color,
                class_name="rounded-b-lg",
            ),
            
            spacing="0",
            width="100%",
            align_items="stretch",
        ),
        class_name=f"overflow-hidden transform transition-all duration-300 hover:translate-y-[-5px] {animation_class} {delay_class}",
        box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
        _hover={
            "box_shadow": "0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05)",
        },
        border="1px solid #E2E8F0",
        border_radius="lg",
        width="100%",
        overflow="hidden",
    )
