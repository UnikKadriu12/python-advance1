class Studenti:
    def __init__(self, emri, mbiemri):
        self.emri=emri
        self.mbiemri=mbiemri




studenti123 = Studenti("Donjeta","Zogaj")



studenti123.mbiemri="Mazreku"
studenti123.emri="Erona"
print(studenti123)
print(studenti123.emri)