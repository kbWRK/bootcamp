from matematica.geometry import figures

def test_square_area():
    assert figures.square_area(5) == 25
def test_triangle_area():
    assert figures.triangle(5,10) == 25