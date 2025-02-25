import reflex as rx


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
        "animate-slide-in-left" if index % 2 == 0 else "animate-slide-in-right"
    )
    delay_class = f"delay-{min(index + 1, 4)}"  # Limit delay classes to 4
    
    # Rotation for neo-brutalist look - alternating for each card
    rotation = "rotate-[2deg]" if index % 2 == 0 else "rotate-[-1deg]"
    
    # Background colors for neo-brutalist style
    bg_colors = ["rgb(255, 235, 130)", "rgb(130, 230, 255)", "rgb(255, 130, 200)", "rgb(180, 230, 180)"]
    bg_color = bg_colors[index % len(bg_colors)]

    return rx.box(
        rx.box(
            rx.image(
                src=image,
                alt=title,
                class_name="w-full h-full object-cover object-top",
                border_bottom="5px solid black",
            ),
            class_name="relative h-48 overflow-hidden",
        ),
        rx.box(
            rx.heading(
                title,
                class_name="text-2xl font-black tracking-tight mb-4 uppercase",
                color="black",
                style={"letter-spacing": "-0.03em"},
            ),
            rx.text(
                description,
                class_name="mb-6 text-xl font-medium",
                color="black",
            ),
            rx.flex(
                *[
                    rx.box(
                        rx.text(
                            tag,
                            class_name="text-sm font-bold",
                            color="white",
                        ),
                        background="black",
                        border="2px solid black",
                        padding="0.3em 0.7em",
                        transform=f"rotate({(index % 3) - 1}deg)",
                        transition="all 0.2s ease-in-out",
                        _hover={"transform": f"rotate({-(index % 3) + 1}deg) scale(1.05)"},
                    )
                    for tag in tags
                ],
                class_name="flex flex-wrap gap-3 mb-8",
            ),
            rx.hstack(
                rx.cond(
                    github_url is not None,
                    rx.link(
                        rx.hstack(
                            rx.icon("github", class_name="cursor-pointer", size=22),
                            rx.text("CODE", class_name="text-lg font-bold"),
                            class_name="flex items-center",
                            spacing="1",
                        ),
                        href=github_url,
                        class_name="text-white bg-black px-4 py-2 border-2 border-black hover:bg-[rgb(255,50,50)] hover:text-black transition-all duration-300",
                    ),
                ),
                rx.cond(
                    live_url is not None,
                    rx.link(
                        rx.hstack(
                            rx.icon(
                                "external-link", class_name="cursor-pointer", size=22
                            ),
                            rx.text("DEMO", class_name="text-lg font-bold"),
                            class_name="flex items-center",
                            spacing="1",
                        ),
                        href=live_url,
                        class_name="text-white bg-black px-4 py-2 border-2 border-black hover:bg-[rgb(50,50,255)] hover:text-black transition-all duration-300",
                    ),
                ),
                class_name="gap-8",
            ),
            class_name="p-6 bg-[" + bg_color + "]",
        ),
        class_name=f"border-[4px] border-black overflow-hidden transform transition-all duration-300 hover:scale-105 {rotation} hover:shadow-[12px_12px_0px_rgba(0,0,0,0.8)] {animation_class} {delay_class}",
        box_shadow="8px 8px 0px rgba(0, 0, 0, 0.8)",
        max_width="500px",
        margin="0 auto",
    )
