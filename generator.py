import secrets
import string
import flet as ft


class PasswordGenerator:
    def __init__(self, page: ft.Page):
        self.page = page
        self.copy_button = None
        self.password_output = None
        self.generate_button = None
        self.password_type = None
        self.length_password_entry = None

        # ==============================
        # Colors
        # ==============================
        self.colors = {
            "primary": ft.Colors.BLUE,
            "success": ft.Colors.GREEN,
            "error": ft.Colors.RED,
            "text": ft.Colors.WHITE,
            "background": ft.Colors.WHITE,
            "button": ft.Colors.BLUE,
            "button_text": ft.Colors.WHITE,
        }

        self.page.title = "Password Generator"

        self.page.window.width = 400
        self.page.window.height = 350
        self.page.window.icon = "../assets/icon/generator.ico"
        self.page.window.resizable = False
        self.page.window.maximizable = False

        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.page.vertical_alignment = ft.MainAxisAlignment.CENTER

        # Register keyboard event
        self.page.on_keyboard_event = self.keyboard_input

    def show_message(self, message, color=None):
        """
        Displays a SnackBar notification.
        """

        if color is None:
            color = self.colors["success"]

        snack_bar = ft.SnackBar(
            content=ft.Text(
                message,
                color=ft.Colors.WHITE,
            ),
            bgcolor=color,
        )

        self.page.show_dialog(snack_bar)
        self.page.update()

    async def keyboard_input(self, e):
        if e.key in ["Enter", "Numpad Enter"]:
            await self.generate_password(None)

    async def copy_password(self, e):
        if self.password_output.value:
            try:
                await ft.Clipboard().set(self.password_output.value)
            except Exception as ex:
                print(ex)

            self.show_message(message="Password copied!", color=self.colors["success"])
        else:
            self.show_message(message="No Password to copy.", color=self.colors["error"])
        self.page.update()

    async def create_widgets(self):
        self.length_password_entry = ft.TextField(
            label="Password Length",
            value="10",
            width=300,
            keyboard_type=ft.KeyboardType.NUMBER,
            input_filter=ft.NumbersOnlyInputFilter(),
            on_submit=self.generate_password,  # Enter inside TextField
        )

        self.password_type = ft.Dropdown(
            width=300,
            value="All Characters",
            options=[
                ft.dropdown.Option("Letters"),
                ft.dropdown.Option("Numbers"),
                ft.dropdown.Option("Symbols"),
                ft.dropdown.Option("Letters + Numbers"),
                ft.dropdown.Option("All Characters"),
            ],
        )

        self.generate_button = ft.ElevatedButton(
            "Generate Password",
            on_click=self.generate_password,
            width=300,
            bgcolor=self.colors["button"],
            color=self.colors["button_text"],
            style=ft.ButtonStyle(
                mouse_cursor=ft.MouseCursor.CLICK
            )
        )

        self.password_output = ft.TextField(
            label="Generated Password",
            width=300,
            read_only=True,
            can_reveal_password=True,
        )

        self.copy_button = ft.IconButton(
            icon=ft.Icons.COPY,
            tooltip="Copy Password",
            on_click=self.copy_password,
            icon_color=self.colors["primary"],
            mouse_cursor=ft.MouseCursor.CLICK
        )

        self.page.add(
            ft.Column(
                [
                    self.length_password_entry,
                    self.password_type,

                    # Download folder + folder picker
                    ft.Row(
                        [
                            self.password_output,
                            self.copy_button,
                        ],
                        alignment=ft.MainAxisAlignment.END,
                        spacing=5,
                    ),

                    self.generate_button,

                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=15,
            )
        )

        self.page.update()

    async def get_symbols(self):
        symbol_map = {
            "Letters": string.ascii_letters,
            "Numbers": string.digits,
            "Symbols": string.punctuation,
            "Letters + Numbers": string.ascii_letters + string.digits,
            "All Characters": (
                    string.ascii_letters
                    + string.digits
                    + string.punctuation
            ),
        }

        return symbol_map[self.password_type.value]

    async def generate_password(self, e):
        try:
            length = int(self.length_password_entry.value)

            if length < 2:
                self.show_message(message="Password length must be at least 2.", color=self.colors["error"])
                self.password_output.value = ""
                self.page.update()
                return

            if length > 2048:
                self.show_message(
                    message="Password length must be between 2 and 2048.",
                    color=self.colors["error"]
                )
                self.password_output.value = ""
                self.page.update()
                return

            symbols = await self.get_symbols()

            password = "".join(
                secrets.choice(symbols)
                for _ in range(length)
            )

            self.password_output.value = password
            self.show_message(message="Password generated successfully!")
            self.page.update()

        except (ValueError, TypeError):
            self.show_message(message="Filed not be empty", color=self.colors['error'])
            self.password_output.value = ""
            self.page.update()


class App:
    async def main(self, page: ft.Page):
        generator = PasswordGenerator(page)
        await generator.create_widgets()


if __name__ == "__main__":
    ft.app(target=App().main)
