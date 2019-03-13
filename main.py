import export
import ui


def main():
    export.init()
    app = ui.Tekken7App()
    app.mainloop()


main()
