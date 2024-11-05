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

    return rx.box(
        rx.box(
            rx.image(
                src=image,
                alt=title,
                class_name="w-full h-full object-cover object-top",
            ),
            class_name="relative h-48 overflow-hidden",
        ),
        rx.box(
            rx.heading(
                title,
                class_name="text-2xl tracking-wide mb-2",
            ),
            rx.text(
                description,
                class_name="mb-4 tracking-wide text-xl",
            ),
            rx.flex(
                *[
                    rx.box(
                        rx.text(
                            tag,
                            class_name="text-md",
                        ),
                        class_name="border-2 p-1 px-2 rounded-md",
                    )
                    for tag in tags
                ],
                class_name="flex flex-wrap gap-2 mb-4",
            ),
            rx.hstack(
                rx.cond(
                    github_url is not None,
                    rx.link(
                        rx.hstack(
                            rx.icon("github", class_name="cursor-pointer"),
                            rx.text("Code", class_name="text-xl"),
                            spacing="1",
                        ),
                        href=github_url,
                        class_name="text-inherit",
                    ),
                ),
                rx.cond(
                    live_url is not None,
                    rx.link(
                        rx.hstack(
                            rx.icon("external-link", class_name="cursor-pointer"),
                            rx.text("Live Demo", class_name="text-xl"),
                            spacing="1",
                        ),
                        href=live_url,
                        class_name="text-inherit",
                    ),
                ),
                class_name="gap-8",
            ),
            class_name="p-6",
        ),
        class_name=f"border-2 rounded-md overflow-hidden transform transition-all hover:scale-[1.02] {animation_class} {delay_class}",
    )
