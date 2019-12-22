def formatuj(*args, **kwargs):
    results = "\n".join(args)
    for nazwa, wartosc in kwargs.items():
        results = results.replace("$"+nazwa, str(wartosc))

    return results


def test_formatuj_no_kwargs():
    expected = """aaa
    bbb
    ccc"""
    assert formatuj("aaa", "bbb", "ccc") == expected


def test_formatuj_with_kwargs():
    expected = "podróż z los angeles do yorktown zajmuje 5 h"
    assert formatuj("podróż z $miasto1 do $miasto2 zajmuje $czas h",
                    miasto1="los angeles", miasto2="yorktown", czas=5) == expected
def test_formatuj_multiple_lines_mutiple_kwargs():
    expected = "hej \nmam nowy samochód\nniebiseski dom i wiele róznych niebieskich rzeczy \n niebieski to mój ulubiony kolor"