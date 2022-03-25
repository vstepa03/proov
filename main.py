"""Turniir."""


def loe_seis(fail: str) -> dict:
    result = {}
    with open(fail, 'r') as f:
        for line in f:
            if line.startswith("     "):
                continue
            m = line.replace("\n", "").split(" ")
            r = []
            for i in m[1:]:
                if i.isdigit():
                    r.append(int(i))
                else:
                    r.append(i)

            result[m[0]] = r
    return result


def lisa_tulemus(nimi: str, voor: int, results: dict, res: int) -> dict:

    # Проверяю есть ли такое имя в списке, не знаю, нужно ли, можно удалить, если не нужно
    if nimi not in results.keys():
        print("Seda nime nimekirjas pole!")
        return results

    inimese_tulemused = results[nimi]

    # Проверяю есть ли круг, не знаю, нужно ли, можно удалить, если не нужно
    if len(inimese_tulemused) < voor:
        print("Selle numbriga voore ei ole!")
        return results

    if inimese_tulemused[voor - 1] == '-':
        inimese_tulemused[voor - 1] = res
        results[nimi] = inimese_tulemused
        print("Tulemus lisatud!")
    else:
        print("Tulemus on juba varem lisatud!")

    return results


def leia_skoor(nimi: str, results: dict) -> int:

    # Проверяю есть ли такое имя в списке, не знаю, нужно ли, можно удалить, если не нужно
    if nimi not in results.keys():
        return 0

    result = 0
    for i in results[nimi]:
        if type(i) is int:
            result += i
    return result


# Делаем таблицу для 1 - Vaata punktitabelit
def punktitabel(results: dict) -> str:

    tabel = ""

    for name in results.keys():
        tabel += name + " "

        for element in results[name]:
            tabel += str(element) + " "
        tabel = tabel[:-1] + "\n"

    return tabel[:-1]


def program(src: str):
    data = loe_seis(src)

    while True:
        print("Vali tegevus:\n1 - Vaata punktitabelit\n2 - Lisa tulemus\n3 - Vaata skoori\n4 - Leia võitja\n5 - Lõpeta programmi töö")
        inp = input()

        if inp == '1':
            print(punktitabel(data))
        elif inp == '2':
            nimi = input("Sisesta nimi: ")
            voor = input("Sisesta voor: ")
            punktid = input("Sisesta punktid: ")
            data = lisa_tulemus(nimi, int(voor), data, int(punktid))
        elif inp == '3':
            nimi = input("Sisesta nimi: ")
            print(nimi + "skoor on " + str(leia_skoor(nimi, data)) + ".")
        elif inp == '4':
            max_punktid = 0
            voitja = ""
            for i in data.keys():
                p = leia_skoor(i, data)
                if p > max_punktid:
                    max_punktid = p
                    voitja = i

            print("Suurima skooriga on " + voitja + " (" + str(max_punktid) + " punkti).")
        elif inp == "5":
            vooride_number = 0
            result = ""

            for i in data.keys():
                if vooride_number == 0:
                    vooride_number = len(data[i])
                    result += "     "
                    for m in range(vooride_number):
                        result += str(m + 1) + " "
                    result = result[:-1] + "\n"
                    break
            result += punktitabel(data)

            with open("turniir_uus.txt", "w") as f:
                f.write(result)
            print("Programm lõpetas töö.")
            break


if __name__ == '__main__':
    program("turniir.txt")
