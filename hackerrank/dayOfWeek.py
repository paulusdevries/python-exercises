import calendar

def weekDag(datum):
    dagen = {
        0: "MONDAY",
        1: "TUESDAY",
        2: "WEDNESDAY",
        3: "THURSDAY",
        4: "FRIDAY",
        5: "SATURDAY",
        6: "SUNDAY"
    }

    maand, dag, jaar = datum.split()
    print(dagen[calendar.weekday(int(jaar), int(maand), int(dag))])

weekDag(input())