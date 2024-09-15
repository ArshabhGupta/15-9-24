class India():
    def capital(self):
        print("New Delhi")
    def language(self):
        print("Hindi")
    def type(self):
        print("A developing country")

class USA():
    def capital(self):
        print("Washinton D.C.")
    def language(self):
        print("English")
    def type(self):
        print("A developed country")

objindia = India()
objusa = USA()
for country in (objindia, objusa):
    country.capital()
    country.language()
    country.type()