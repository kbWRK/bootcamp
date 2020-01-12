from matematica.algebra import matrices
def test_add_matrices():
    m1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    m2 = [
        [9, 8, 7],
        [6, 5, 4],
        [3, 2, 1],
    ]

    assert matrices.add_matrices(m1,m2) == [[10, 10, 10], [10, 10, 10], [10, 10, 10]

def test_sub_matrices():
    m1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    m2 = [
        [9, 8, 7],
        [6, 5, 4],
        [3, 2, 1],
    ]

    assert matrices.add_matrices(m1, m2) == [[-8, -6, -4], [-2, 0, 2], [4, 6, 8]]
