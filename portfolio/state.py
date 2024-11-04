import reflex as rx


class State(rx.State):
    @rx.var
    def get_page(self):
        return self.router.page.path.split("/")[-1]
