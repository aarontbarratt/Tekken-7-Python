import test


def main():
    # should probably make sure path exists when the program initially starts
    # if paths don't exists create path, else createUI()
    app = test.ExpensesApp()
    app.mainloop()


main()
