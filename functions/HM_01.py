#>>> splaszcz([1, 2, 3, [4, 5, [6]], 7])
#[1, 2, 3, 4, 5, 6, 7]
def spłaszcz(lista):
    result = [ ]
    for element in lista:
        if isinstance(element, list):
            for subelement in spłaszcz(element):
              result.append(subelement)
        else:
            result.append(subelement)
    return result


def test_falt_list():
    spłaszcz([1,2,23]) == [1,2,23]
def test_list_with_list():
    assert spłaszcz([1,12,[21,2]]) == [1,12,21,2]
def test_list_with_list_lv2():
    assert spłaszcz
