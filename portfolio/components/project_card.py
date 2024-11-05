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
                            class_name="text-sm font-medium",
                        ),
                        class_name="bg-gray-100 dark:bg-gray-600 text-gray-800 dark:text-white px-3 py-1 rounded-full transition-all duration-300 hover:scale-105 hover:shadow-md",
                    )
                    for tag in tags
                ],
                class_name="flex flex-wrap gap-3 mb-6",
            ),
            rx.hstack(
                rx.cond(
                    github_url is not None,
                    rx.link(
                        rx.hstack(
                            rx.icon("github", class_name="cursor-pointer", size=20),
                            rx.text("Code", class_name="text-lg"),
                            class_name="flex items-center",
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
                            rx.icon(
                                "external-link", class_name="cursor-pointer", size=20
                            ),
                            rx.text("Demo", class_name="text-lg"),
                            class_name="flex items-center",
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
        class_name=f"border-2 border-slate-500 rounded-md overflow-hidden transform transition-all duration-300 hover:scale-110 hover:shadow-2xl {animation_class} {delay_class}",
    )
