def home_page():
    with open('templates/index.html') as tempate:
        return tempate.read()

def calc_total():
    with open('templates/total.html') as tempate:
        return tempate.read()